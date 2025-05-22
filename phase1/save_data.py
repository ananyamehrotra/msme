import json
from scraper.basic_scraper import scrape_website

url = "https://www.bonkerscorner.com"

data = scrape_website(url)

print("Scraped Data:")
print(json.dumps(data, indent=4))

with open("model_training/output.json", "w") as f:
    json.dump(data, f, indent=4)
