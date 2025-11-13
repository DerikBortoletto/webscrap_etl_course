import requests
from bs4 import BeautifulSoup
import os

def extract_data(output_dir):
    url = "https://en.wikipedia.org/wiki/COVID-19_pandemic"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table', {'class': 'wikitable'})
    print(f"Found {len(tables)} tables.")

    for i, table in enumerate(tables):
        file_path = os.path.join(output_dir, f"table_{i}.html")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(table))
        print(f"Saved table {i} to {file_path}")


if __name__ == "__main__":
    raw_data_dir = os.path.join("data", "raw")
    os.makedirs(raw_data_dir, exist_ok=True)
    extract_data(raw_data_dir)
