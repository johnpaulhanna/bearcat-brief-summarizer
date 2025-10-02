import requests
from bs4 import BeautifulSoup
from transformers import pipeline

URL = "https://www.binghamton.edu/news/"

print(f"fetching news from {URL}")
try: 
    response = requests.get(URL)
    print(f"Status code:", {response.status_code})
    soup = BeautifulSoup(response.content, "html.parser")

    heading_div = soup.find("section", id="feature-story")

    if heading_div:
        article_link_tag = heading_div.find("a")
        headline_tag = heading_div.find("h2", class_="headline")
        if article_link_tag and headline_tag:
            top_story_headline_text = headline_tag.text.strip()
            print(f"\nSUCCESS! Found the top story headline: {top_story_headline_text}")
            
            partial_link = article_link_tag['href']
            story_url = partial_link if partial_link.startswith("http") else f"https://www.binghamton.edu{partial_link}"
            print("\n")
            print(f"the story url is: {story_url}")
            print("\n")
            
            story_response = requests.get(story_url)
            story_soup = BeautifulSoup(story_response.content, "html.parser")
            
            description = story_soup.find("div", id="story-body")

            if description:
                description_text = description.text.strip()
                print(f"Found description: \n\n{description_text[:500]}...")
                text_to_summarize = f"{top_story_headline_text}. {description_text}"
    
    else:
            print("\nCould not find the headline. The website structure might have changed.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")