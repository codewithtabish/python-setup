import requests
from bs4 import BeautifulSoup

def get_video_tags_and_title(video_url):
    try:
        response = requests.get(video_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print("The url in the method again ",video_url)


            # Extract meta tag content for keywords (tags)
            meta_tags = soup.find("meta", attrs={"name": "keywords"})
            tags = meta_tags["content"].split(",") if meta_tags else None

            # Extract title
            title_tag = soup.find("title")
            title = title_tag.text.strip() if title_tag else None

            return {
                "tags": [tag.strip() for tag in tags] if tags else None,
                "title": title
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching video details: {e}")
        return None

# Example Usage
# video_url = "https://www.youtube.com/watch?v=oQ5UfJqW5Jo"
# result = get_video_tags_and_title(video_url)
# if result:
#     print("Extracted Tags:", result['tags'])
#     print("Extracted Title:", result['title'])
# else:
#     print("Failed to fetch video metadata.")
