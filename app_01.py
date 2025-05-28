import requests

def fetch_page(url):
    response = requests.get(url)
    return (response.text)

if __name__ == "__main__":
    url = "https://produto.mercadolivre.com.br/MLB-3925753517-console-sony-playstation-5-slim-digital-branco-1tb-jogos-ratchet-and-clank-e-returnal-_JM#polycard_client=recommendations_vpp-pdp-v2p-pom&reco_backend=ranker_retrieval_system_vpp_v2p&reco_model=ranker_entity_v2_retrieval_system_vpp_v2p&reco_client=vpp-pdp-v2p-pom&reco_item_pos=0&reco_backend_type=low_level&reco_id=3e834eea-ba24-4619-92f2-0b4e48069f93"
    page_content = fetch_page(url)
    print(page_content)