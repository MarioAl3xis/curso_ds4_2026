"""
Dollar Exchange Module
"""
import os
import requests
import argparse
from bs4 import BeautifulSoup

def scrap_web_page(url:str) -> str:
    """Scrap the content of a web page and return it as a string."""
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve the web page. Status code: {response.status_code}")

def get_dollar_exchange_rate(content:str) -> str:
    """Extract the dollar exchange rate from the web page content."""
    soup = BeautifulSoup(content, 'html.parser')
    main_table = soup.find('table', id='dllsTable')
    if main_table:
        rows = main_table.find_all('tr')
        price_list = []
        for row in rows:
            cols = row.find_all('td')
            for i,col in enumerate(cols):
                print(f"i: {i}, col: {col.text.strip()}")
            if len(cols) == 4:
                sell_price = cols[3].text.strip()
                buy_price = cols[4].text.strip()
                bank_name = cols[1].text.strip()
            if len(cols) == 5:
                sell_price = cols[3].text.strip()
                buy_price = cols[4].text.strip()
                bank_name = cols[2].text.strip()
            price_list.append((bank_name, sell_price, buy_price))
            return price_list

def main(args):
    """Main function to scrap a web page and save the content to a file."""
    url = args.url
    output_file = args.output_file
    try:
        content = scrap_web_page(url)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"web page content from {url} has been saved to {output_file}.")
        price_list = get_dollar_exchange_rate(content)
        if price_list:
            print("Dollar Exchange Rates:")
            for bank_name, sell_price, buy_price in price_list:
                print(f"Bank: {bank_name}, Sell Price: {sell_price}, Buy Price: {buy_price}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrap a web page and save its content to a file.")
    parser.add_argument("url", type=str, help="URL of the web page to scrap.")
    parser.add_argument("output_file", type=str, help="Path to the output file where the content will be saved.")
    args = parser.parse_args()
    main(args)