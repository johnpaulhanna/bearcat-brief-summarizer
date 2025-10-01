import requests
from bs4 import BeautifulSoup
from transformers import pipeline

URL = "https://www.binghamton.edu/news/"

print(f"fetching news from {URL}")
try: 
    response = requests.get(URL)
    print(f"response status code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")

    top_story_headline = soup.find("h2", class_= "headline")

    if top_story_headline:
        print("\nSUCCESS! Found the top story headline:")
        top_story_headline_text = top_story_headline.text.strip()
        print(top_story_headline_text)
    else:
        print("\nCould not find the headline. The website structure might have changed.")
    #this has to be moved inside "top_story_headline" if statement
    description = soup.find("div", id="story-body")

    print(description)
    if description:
        description_text = description.text.strip()
        print(f"Found description: {description_text}")
        text_to_summarize = f"{top_story_headline_text}. {description_text}"
    #from this to the last comment

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


#this comment is to see if my contributions go up