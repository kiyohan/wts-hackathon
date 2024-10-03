# README

## Overview

This repository contains a Python script that processes HTML content from the Wikipedia "Main Page" to extract and save news items and images from the "In the news" section. The extracted data is saved in a JSON file with the current date and time.

## Code Explanation

The script performs the following steps:

1. **Fetch HTML Content**: Fetches the HTML content of the Wikipedia "Main Page" using the Wikimedia REST API.
2. **Extract Images**: Extracts images from the "In the news" section that have the specified class.
3. **Extract Links**: Extracts all links from the provided HTML content.
4. **Process News Items**: Processes each news item, extracting text, links, and images.
5. **Save Data**: Saves the processed news items and images to a JSON file with the current date and time.

### Functions

- `fetch_in_the_news()`: Fetches the HTML content of the Wikipedia "Main Page".
- `extract_images_from_itn(html_content)`: Extracts images from the "In the news" section.
- `extract_links(item_html)`: Extracts all links from the provided HTML content.
- `process_news_item(item_html)`: Processes a news item, extracting text, links, and images.
- `main()`: Main function that orchestrates the fetching, processing, and saving of news data.

## Requirements

- Python 3.x
- `requests` library
- `re` module (standard library)
- `datetime` module (standard library)
- `json` module (standard library)

## Usage

To use this code, ensure you have Python installed on your system. You can run the script using the following command in your terminal:

```bash
python final.py
```

## Output

The script will generate a JSON file named `processed_news_with_itn_images.json` containing the processed news items and images. Here is an excerpt from the JSON file:

```json
{
  "story": "In Australian rules football, the Brisbane Lions defeat the Sydney Swans to win the AFL Grand Final.",
  "sub_links": [
    {
      "url": "https://en.wikipedia.org('/wiki/Australian_rules_football', 'Australian rules football')"
    },
    {
      "url": "https://en.wikipedia.org('/wiki/Brisbane_Lions', 'Brisbane Lions')"
    },
    {
      "url": "https://en.wikipedia.org('/wiki/Sydney_Swans', 'Sydney Swans')"
    },
    {
      "url": "https://en.wikipedia.org('/wiki/2024_AFL_Grand_Final', 'the AFL Grand Final')"
    }
  ]
},
{
  "story": "Hurricane Helene leaves more than 100 people dead across the southeastern United States.",
  "sub_links": [
    {
      "url": "https://en.wikipedia.org('/wiki/Hurricane_Helene', 'Hurricane Helene')"
    }
  ]
},
{
  "story": "British actress Maggie Smith dies at the age of 89.",
  "sub_links": [
    {
      "url": "https://en.wikipedia.org('/wiki/Maggie_Smith', 'Maggie Smith')"
    }
  ]
}
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or issues, please open an issue in the repository or contact the maintainer.

---
