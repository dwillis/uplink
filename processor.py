import os
import json
import time
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def process_text(filename):
    with open(f"text/{filename}", 'r') as file:
        text = file.read()
        try:
            response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "Produce a JSON array containing one or more objects with the following keys: 'year', 'month', 'headline', 'author_name', 'author_title', 'summary', 'keywords', of which keywords is an array of no more than 3 words. summary is a brief description of each piece, and you should process all stories in each file. Do not include any other text, no yapping."
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": text
                    }
                ]
                }
            ],
            response_format={
                "type": "json_object"
            },
            temperature=1,
            max_tokens=8192,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            response_content = response.choices[0].message.content
            # Parse the JSON response
            parsed_response = json.loads(response_content)
            return parsed_response
        except:
            raise
            #return None


def combine_stories(filename):
    with open(f"text/{filename}", 'r') as file:
        text = file.read()
        try:
            response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "Produce a JSON array containing one or more objects representing distinct articles with the following keys: 'year', 'month', 'headline', 'author_name', 'author_title', 'full_text', where full_text is the complete text of each story, including any jumps to later parts of the file, and you should process all stories in each file. Do not include any introductory text, but include the full text of each story, no yapping."
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": text
                    }
                ]
                }
            ],
            response_format={
                "type": "json_object"
            },
            temperature=1,
            max_tokens=8192,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            response_content = response.choices[0].message.content
            # Parse the JSON response
            parsed_response = json.loads(response_content)
            return parsed_response
        except:
            raise
            #return None    


def main():
    for filename in os.listdir("text"):
        if filename.endswith(".txt"):
            print(f"Processing {filename}")
            with open(f"articles/{filename.replace('.txt', '.json')}", 'w') as file:
                articles = combine_stories(filename)
                json.dump(articles, file, indent=4)
    
    
    
if __name__ == "__main__":
    main()