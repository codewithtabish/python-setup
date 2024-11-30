from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep

def extract_seo_tags_with_selenium(url):
    try:
        # Set up Selenium WebDriver using WebDriver Manager
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        # Wait for the page to fully load
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "meta"))
        )
        sleep(5)  # Allow additional time for JavaScript to load
        
        # Extract the HTML after JavaScript execution
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        # Extract SEO-related tags
        seo_tags = {
            "title": soup.title.string.strip() if soup.title else None,
            "description": soup.find('meta', attrs={'name': 'description'}).get('content') if soup.find('meta', attrs={'name': 'description'}) else None,
            "keywords": soup.find('meta', attrs={'name': 'keywords'}).get('content') if soup.find('meta', attrs={'name': 'keywords'}) else None,
            "canonical": soup.find('link', attrs={'rel': 'canonical'}).get('href') if soup.find('link', attrs={'rel': 'canonical'}) else None,
            "robots": soup.find('meta', attrs={'name': 'robots'}).get('content') if soup.find('meta', attrs={'name': 'robots'}) else None,
            "og:title": soup.find('meta', attrs={'property': 'og:title'}).get('content') if soup.find('meta', attrs={'property': 'og:title'}) else None,
            "og:description": soup.find('meta', attrs={'property': 'og:description'}).get('content') if soup.find('meta', attrs={'property': 'og:description'}) else None,
            "og:image": soup.find('meta', attrs={'property': 'og:image'}).get('content') if soup.find('meta', attrs={'property': 'og:image'}) else None,
            "twitter:card": soup.find('meta', attrs={'name': 'twitter:card'}).get('content') if soup.find('meta', attrs={'name': 'twitter:card'}) else None,
            "structured_data": [script.string for script in soup.find_all('script', type='application/ld+json')]
        }

        return seo_tags

    except Exception as e:
        return {"error": f"Failed to fetch URL: {str(e)}"}
