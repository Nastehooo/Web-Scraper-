import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, filedialog

def scrape_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No Title Found"
        paragraphs = soup.find_all('p')
        content = '\n'.join([p.get_text(strip=True) for p in paragraphs])

        return title, content

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch the article:\n{e}")
        return None, None

def format_output(title, content):
    formatted_title = f"# {title}\n\n"
    formatted_content = content.replace('http', '[Link](http')
    return formatted_title + formatted_content

def save_article(title, content):
    filename = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt"), ("All files", "*.*")],
        title="Save Article"
    )
    if filename:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(format_output(title, content))
        messagebox.showinfo("Success", f"Article saved as '{filename}'")

def scrape_button_action():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    title, content = scrape_article(url)
    if title and content:
        title_var.set(title)
        content_text.delete(1.0, tk.END)
        content_text.insert(tk.END, content)
    else:
        content_text.delete(1.0, tk.END)
        content_text.insert(tk.END, "Failed to retrieve content.")

def save_button_action():
    title = title_var.get()
    content = content_text.get(1.0, tk.END).strip()
    if title and content:
        save_article(title, content)
    else:
        messagebox.showwarning("Save Error", "No article content to save.")

# Tkinter GUI setup
root = tk.Tk()
root.title("News Article Scraper")
root.geometry("800x600")
root.configure(bg="#f2b4cb")  # Light pink background

# Input URL Frame
url_frame = tk.Frame(root, bg="#f2b4cb")
url_frame.pack(pady=10)

tk.Label(url_frame, text="Enter Article URL:", bg="#f2b4cb", font=("Arial", 15)).pack(side=tk.LEFT, padx=5)
url_entry = tk.Entry(url_frame, width=50, font=("Arial", 15), fg="black")
url_entry.pack(side=tk.LEFT, padx=5)

# Article Title Display
title_var = tk.StringVar()
title_label = tk.Label(root, textvariable=title_var, font=("Arial", 16), wraplength=700, justify="center", bg="#f2b4cb", fg="#ffffff")
title_label.pack(pady=10)

# Article Content Display
content_frame = tk.Frame(root, bg="#f2b4cb")
content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

content_text = tk.Text(content_frame, wrap=tk.WORD, font=("Arial", 20), bg="#ffffff")
content_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Save Button
save_button = tk.Button(root, text="Save Article", command=save_button_action, font=("Arial", 12, "bold"), relief="raised", bd=2, bg="#ff99cc", fg="black")
save_button.pack(pady=10)

# Scrape Button
scrape_button = tk.Button(url_frame, text="Scrape Article", command=scrape_button_action, font=("Arial", 12, "bold"), relief="raised", bd=2, bg="#ff99cc", fg="black")
scrape_button.pack(side=tk.LEFT, padx=5)
root.mainloop()
