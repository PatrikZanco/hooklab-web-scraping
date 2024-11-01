import requests
from bs4 import BeautifulSoup
import csv

# URL do subreddit
url = "https://www.reddit.com/r/programming/"



response = requests.get(url)


if response.status_code == 200:
    print(f"Conexão feita com sucesso. Status: {response.status_code}")
    
    
    html_page = response.content
    soup = BeautifulSoup(html_page, "html.parser")

    
    posts = soup.findAll("a", class_="absolute inset-0", limit=3) #buscar os 3 primeiros posts
    

    
    data = []

    for post in posts:
        
        title_tag = post.find("faceplate-screen-reader-content")  
        title = title_tag.get_text() if title_tag else "Título não encontrado"

        
        link = post['href'] if 'href' in post.attrs else "Link não encontrado"
        full_link = "https://www.reddit.com" + link

        
        upvotes_tag = post.find_previous_sibling("div", class_="upvote-count")  
        upvotes = upvotes_tag.get_text() if upvotes_tag else "N/A"

        
        data.append([title, upvotes, full_link])

    # Escreve os dados em um arquivo CSV e salva no diretório
    with open("questao1/reddit_posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Upvotes", "Link"])
        writer.writerows(data)

    print("Dados salvos no arquivo 'questao1/reddit_posts.csv'.")
else:
    print(f"Erro ao tentar fazer a requisição, status: {response.status_code}")
