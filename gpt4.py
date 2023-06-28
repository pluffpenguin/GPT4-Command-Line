import os
import openai
import time

from dotenv import load_dotenv
from colorama import init
init()

load_dotenv()
ORG_KEY = os.getenv('ORG_KEY')
API_KEY = os.getenv('API_KEY')

openai.organization = ORG_KEY
openai.api_key = API_KEY

def print_line():
    print("\n\n===========================================\n\n")

def get_response(target_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=target_prompt,
        max_tokens=3900,
        temperature=0.05
    )
    return response

first_prompt = input(f'[?] What would you like to ask? \n>>> ')
first_response = get_response(first_prompt)

print(first_response["choices"]["text"])
print_line()

# loop
while True:
    prompt = input(f'[?] Continue: \n>>> ')
    response = get_response(prompt)
    print(response["choices"]["text"])
    print_line()
    time.sleep(1)