import os
import openai
import time

from dotenv import load_dotenv
from colorama import just_fix_windows_console, Fore, Back, Style
just_fix_windows_console()

load_dotenv()

ORG_KEY = os.getenv('ORG_KEY')
API_KEY = os.getenv('API_KEY')

openai.organization = ORG_KEY
openai.api_key = API_KEY

def print_line():
    print(Fore.YELLOW + "\n\n===========================================" + Fore.WHITE + "\n")

def get_response(target_prompt):
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=target_prompt,
    #     max_tokens=3900,
    #     temperature=0.3
    # )

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": target_prompt}
        ]
    )

    # print(completion.choices[0].message)

    return completion

first_prompt = input(Fore.YELLOW + f'[?] What would you like to ask?' + Fore.WHITE + '\n>>> ')
first_completion = get_response(first_prompt)

print(Fore.CYAN + f'\n[ RESPONSE ]\n{first_completion.choices[0].message.content}')

print_line()

# loop
while True:
    prompt = input(Fore.YELLOW + f'[?] Continue: ' + Fore.WHITE + '\n>>> ')
    completion = get_response(prompt)
    print(Fore.YELLOW + f'\n[ RESPONSE ]' + Fore.CYAN + f'\n{completion.choices[0].message.content}')
    print_line()
    time.sleep(1/10)