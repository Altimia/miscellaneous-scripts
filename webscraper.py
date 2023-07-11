import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

def get_links():
    with open('links.txt', 'r') as f:
        links = f.read().splitlines()
    return links

# Write File
def write_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

links = get_links()

for i, link in enumerate(links, 1):
    driver.get(link)
    time.sleep(2)  # wait for javascript to load
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    strong_tag = soup.select_one('strong.text-muted.svelte-aoq06a')
    if strong_tag:
        write_to_file('out.txt', strong_tag.text)
    else:
        write_to_file('no-string-links.txt', link)
    print(f'Processed {i} of {len(links)} links.')

driver.quit()