# 🕹️ WebScrapingETL - Preços de Playstation 5

Este projeto realiza **Web Scraping** de preços de consoles **Playstation 5**, salva os dados em um **banco de dados SQLite**, organiza o processo como um **ETL completo (Extração, Transformação e Carga)**, e pode ser executado em contêiner via **Docker** com **deploy na AWS EC2**.

---

## 🚀 Funcionalidades

- 🔍 Extração de dados de preços diretamente da web
- 🧹 Transformação e limpeza dos dados
- 💾 Armazenamento em banco de dados SQLite
- 🔄 Execução automatizada do pipeline ETL
- 🐳 Empacotamento com Docker
- ☁️ Deploy em servidor EC2 da AWS

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta       | Finalidade                                  |
|------------------|---------------------------------------------|
| Python           | Lógica do ETL, Web Scraping e Banco de Dados|
| SQLite           | Banco de dados leve e local                 |
| Docker           | Containerização da aplicação                |
| AWS EC2          | Hospedagem do projeto em nuvem              |
| VSCode           | Desenvolvimento e testes                    |
| BeautifulSoup    | Web scraping de dados HTML                  |
| Requests         | Requisições HTTP para extração de páginas   |
| Pandas           | Manipulação e tratamento dos dados          |

---

## 📦 Estrutura do Projeto

📁 WebScrapingEtl/
│
├── src/                        
│   ├── dev/                     
│   │   ├── app_01.py
│   │   ├── app_02.py
│   │   ├── app_03.py
│   │   ├── app_04.py
│   │   └── app_05.py
│   │
│   ├── main/                   
│   │   ├── app.06.py             
│   
│
├── data/                       
│   └── ps5_prices.db
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md 

yaml
Copy
Edit

---

## ⚙️ Executando Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/macauli10/web-scraping.git
cd web-scraping
2. Crie um ambiente virtual (opcional)
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
3. Instale as dependências
bash
Copy
Edit
pip install -r requirements.txt
4. Execute o pipeline
bash
Copy
Edit
python app_06.py
🐳 Executando com Docker
1. Build da imagem Docker
bash
Copy
Edit
docker build -t webscraping-etl .
2. Rode o contêiner
bash
Copy
Edit
docker run webscraping-etl
☁️ Deploy na AWS EC2
Crie uma instância EC2 com Amazon Linux ou Ubuntu.

Instale Docker na instância:

bash
Copy
Edit
sudo apt update && sudo apt install docker.io -y
sudo systemctl start docker
sudo usermod -aG docker ubuntu
Transfira os arquivos do projeto para a EC2 com scp.

Construa e execute o container na EC2:

bash
Copy
Edit
docker build -t webscraping-etl .
docker run webscraping-etl
🧠 Aprendizados
Este projeto consolida conhecimentos em:

Web Scraping com Python

Estruturação de um pipeline ETL real

Uso de banco de dados SQLite

Criação de contêineres com Docker

Deploy em servidor AWS EC2

Organização de projeto para produção