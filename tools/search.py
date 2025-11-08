import requests
from bs4 import BeautifulSoup

class Search:
    def search(self, query):
        """
        Searches the web for the given query and returns the top 3 results.
        """
        try:
            url = f"https://www.google.com/search?q={query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            search_results = []
            for g in soup.find_all('div', class_='g'):
                anchors = g.find_all('a')
                if anchors:
                    link = anchors[0]['href']
                    title = g.find('h3').text
                    item = {
                        "title": title,
                        "link": link
                    }
                    search_results.append(item)
                    if len(search_results) == 3:
                        break
            return str(search_results)
        except Exception as e:
            return f"An error occurred while searching: {e}"
