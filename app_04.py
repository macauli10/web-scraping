import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_page():
    url = 'https://produto.mercadolivre.com.br/MLB-3925753517-console-sony-playstation-5-slim-digital-branco-1tb-jogos-ratchet-and-clank-e-returnal-_JM#polycard_client=recommendations_vpp-pdp-v2p-pom&reco_backend=ranker_retrieval_system_vpp_v2p&reco_model=ranker_entity_v2_retrieval_system_vpp_v2p&reco_client=vpp-pdp-v2p-pom&reco_item_pos=0&reco_backend_type=low_level&reco_id=3e834eea-ba24-4619-92f2-0b4e48069f93'
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_='ui-pdp-title').get_text(strip=True)
    prices = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price = int(prices[0].get_text(strip=True).replace('.', ''))
    new_price = int(prices[1].get_text(strip=True).replace('.', ''))
    installment_price = int(prices[2].get_text(strip=True).replace('.', ''))

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price,
        'timestamp': timestamp
    }

def save_to_dataframe(product_info, df):
    new_row = pd.DataFrame([product_info])
    """Salva uma linha de dados no banco de dados SQLite usando pandas."""
    df = pd.concat([df, new_row], ignore_index=True)
    return df

if __name__ == '__main__':
    df = pd.DataFrame()

    while True:
        page_content = fetch_page()
        product_info = parse_page(page_content)
        df = save_to_dataframe(product_info, df)
        print(df)
        time.sleep(10)