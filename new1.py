import requests
import json
from datetime import datetime
import re

def fetch_in_the_news():
    # Wikimedia REST API endpoint for 'Main_Page'
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": "Main_Page",
        "format": "json",
        "prop": "text",
        "section": 0
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['parse']['text']['*']  # This is the HTML content of the Main Page
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def extract_news_items_with_images(news_html):
    """Extracts news items along with their associated images."""
    # Locate the "In the news" list items (<ul>)
    start = news_html.find('id="mp-itn"')
    items_start = news_html.find("<ul>", start)
    items_end = news_html.find("</ul>", items_start)
    news_items_html = news_html[items_start:items_end + 5]

    # Split the list items by <li> tags (these are the individual news stories)
    news_items = re.findall(r'<li>(.*?)</li>', news_items_html, re.DOTALL)
    
    news_data = []
    for item in news_items:
        # Extract the image within the <div role="figure" class="itn-img"> if it exists
        image_match = re.search(r'<div role="figure" class="itn-img">(.*?)</div>', item, re.DOTALL)
        image_html = image_match.group(1).strip() if image_match else None
        
        # Store the item data including the original HTML structure of the image
        news_data.append({
            "story": re.sub(r'<[^>]+>', '', item).strip(),  # Remove HTML tags to get raw story text
            "image": image_html  # Keep the original HTML structure of the image if found
        })
    
    return news_data

def main():
    html_content = fetch_in_the_news()

    if html_content:
        processed_news = extract_news_items_with_images(html_content)

        # Save the processed news, including images specific to each news item
        output = {
            "date": datetime.now().isoformat(),
            "news_items": processed_news
        }

        # Save to JSON file
        with open('processed_news.json', 'w') as f:
            json.dump(output, f, indent=2)

        print("News data with specific images processed and saved to 'processed_news.json'")
    else:
        print("No news data to process")

if __name__ == "__main__":
    main()
