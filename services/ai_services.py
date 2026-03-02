from sqlalchemy.orm import sessionmaker

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("openapi_key"))

def generate_book_summary(book_title: str, book_author: str) -> str:

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates summaries for books."
            },
            {
                "role": "user",
                "content": f"Generate a summary for the book '{book_title}' by {book_author}."
            }
        ]
    )
    
    
    return response['choices'][0]['message']['content']


def generate_book_recommendations(book_title: str, book_author: str) -> str:

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates book recommendations based on a given book."
            },
            {
                "role": "user",
                "content": f"Generate book recommendations based on the book '{book_title}' by {book_author}."
            }
        ]
    )
    
    
    return response.choices[0].message.content