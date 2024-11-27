import requests
from bs4 import BeautifulSoup

def get_video_tags(video_url):
    response = requests.get(video_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract meta tag content
        meta = soup.find("meta", attrs={"name": "keywords"})
        if meta:
            tags = meta["content"].split(",")
            return [tag.strip() for tag in tags]
        else:
            return None
    else:
        return None

# # Example Usage
# video_url = "https://www.youtube.com/watch?v=oQ5UfJqW5Jo"
# tags = get_video_tags(video_url)
# if tags:
#     print("Extracted Tags:", tags)
# else:
#     print("No tags found or failed to fetch video metadata.")
