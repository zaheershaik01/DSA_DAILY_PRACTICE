'''
Docstring for 4. Web Scraping using Multithreading

Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web Scraping often involves making numerous network requests to fetch web pages. These tasks for I/O-bound they
spend a lot of time waiting for responses from servers. Multithreading can signficantly improve the performance
by allowing multiple web pages to be fetched concurrently. 
'''

'''
https://docs.langchain.com/oss/python/langchain/overview
https://docs.langchain.com/oss/python/langchain/quickstart
https://docs.langchain.com/oss/python/langchain/install
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',
    'https://docs.langchain.com/oss/python/langchain/quickstart',
    'https://docs.langchain.com/oss/python/langchain/install'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched.")