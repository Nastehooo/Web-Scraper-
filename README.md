# News Article Scraper Application
Here is the layout of the News Article Scraper:
<img width="1292" alt="Screenshot 2025-01-03 at 14 46 28" src="https://github.com/user-attachments/assets/49e9df27-88f8-45fa-88c9-886bf0276b4a" />

# Key Features:
  1. Scrape and Display News Articles:
      - Users input an article URL, and the app retrieves the article's title and content using the requests library and BeautifulSoup for HTML parsing.
      - The article title is prominently displayed, and the content is shown dynamically in a text area.
      - Markdown Formatting and Saving:
      - Articles can be saved in Markdown or text format.
      - The saved content includes a formatted title (as a Markdown header) and body text, with URLs converted into clickable Markdown links.

  2. Interactive GUI:
     - Built with tkinter, the app has an intuitive layout:
        - A field to input the article URL.
        - A "Scrape Article" button to fetch and display the article's content.
        - A "Save Article" button to store the content in a chosen file format.
        - The GUI's light pink background creates a visually appealing design.
          
  3. Error Handling:
     - The app provides clear error messages if the URL is invalid, the article cannot be fetched, or there's a connectivity issue.
       
  4. Customization:
     - Fonts and layout components are styled for user-friendliness and readability.
     - A compact, user-centered design ensures seamless interaction.


# How to Import and Use the Python Module
If you plan to integrate the scraper into other Python projects or scripts, here's how to do it:

  1. Save the Script as a Module:
       - Save the script in a .py file, such as article_scraper.py.
  
  2. Import the Module:
      -  In your Python script, import the module:
           [ from article_scraper import scrape_article, format_output, save_article ]
  3. Use the Functions Programmatically:
      - Fetch and process an article:
           [ url = "https://example.com/article-url"
            title, content = scrape_article(url)
            if title and content:
                formatted_output = format_output(title, content)
                print(formatted_output)  # Print or handle the formatted article content ]
      - Save the article to a file:
            [ save_article(title, content) ]
  
  4. Run the App's GUI:
      - If you want to use the GUI, run the script directly:
           [ python article_scraper.py ]
  
  5. Install Required Libraries:
      - Install dependencies before running the script:
            [ pip install requests beautifulsoup4 ]


# How to Use:
  1. Enter a valid article URL in the text field.
  2. Click the "Scrape Article" button to fetch and display the article's title and content.
  3. Review the content and click "Save Article" to store it in your desired format.

# Technical Highlights:
  - Parsing Logic: The scraper extracts the article’s heading tag for the title and all paragraph tags for content.
  - Markdown Integration: The content is formatted as Markdown, making it suitable for web or document editors.
  - Cross-Platform Compatibility: The app runs on Windows, macOS, and Linux.
