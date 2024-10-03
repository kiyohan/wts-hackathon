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
        data = response.json()
        return data['parse']['text']['*']  # This is the HTML content of the Main Page
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def extract_links(html_content):
    """Extracts all links from the provided HTML content."""
    links = re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', html_content)
    parsed_links = []
    for link in links:
        url, title = link
        full_url = f"https://en.wikipedia.org{url}"
        print(full_url)
        parsed_links.append({"title": title, "url": full_url})
    return parsed_links

def extract_images(html_content):
    """Extracts all images from the provided HTML content."""
    images = re.findall(r'<img src="([^"]+)"[^>]*>', html_content)
    parsed_images = []
    for img in images:
        full_img_url = f"https:{img}"  # Most image URLs start with //
        parsed_images.append({"url": full_img_url})
    return parsed_images

def process_news_item(item_html):
    """Processes a news item, extracting text, links, and images."""
    story_text = re.sub(r'<[^>]+>', '', item_html).strip()  # Remove all HTML tags to get raw text
    links = extract_links(item_html)  # Extract links from the news item
    return {
        "story": story_text,
        "links": links
    }

def main():
    html_content = fetch_in_the_news()

    if html_content:
        # Locate the "In the news" section
        start = html_content.find('id="mp-itn"')
        end = html_content.find('id="mp-upper"', start)
        in_the_news_html = html_content[start:end]

        # Extract all images from the "In the news" section
        images = extract_images(in_the_news_html)

        # Extract the list items (<li>) from the "In the news" section
        items_start = in_the_news_html.find("<ul>")
        items_end = in_the_news_html.find("</ul>", items_start)
        news_items_html = in_the_news_html[items_start:items_end+5]

        # Split the list items by <li> tags (these are the individual news stories)
        news_items = re.findall(r'<li>(.*?)</li>', news_items_html, re.DOTALL)

        # Process each news item
        processed_news = [process_news_item(item) for item in news_items]

        # Save the processed news, including all images from the section
        output = {
            "date": datetime.now().isoformat(),
            "news_items": processed_news,
            "images": images  # Include all images extracted from the section
        }

        # Save to JSON file
        with open('processed_news_with_images.json', 'w') as f:
            json.dump(output, f, indent=2)

        print("News data with images processed and saved to 'processed_news_with_images.json'")
    else:
        print("No news data to process")

if __name__ == "__main__":
    main()
