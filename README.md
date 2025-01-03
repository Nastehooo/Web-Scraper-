# News Article Scraper Application
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

# How to Use:
  1. Enter a valid article URL in the text field.
  2. Click the "Scrape Article" button to fetch and display the article's title and content.
  3. Review the content and click "Save Article" to store it in your desired format.

# Technical Highlights:
  - Parsing Logic: The scraper extracts the article’s heading tag for the title and all paragraph tags for content.
  - Markdown Integration: The content is formatted as Markdown, making it suitable for web or document editors.
  - Cross-Platform Compatibility: The app runs on Windows, macOS, and Linux.
