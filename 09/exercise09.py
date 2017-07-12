from bs4 import BeautifulSoup


def parser(file):
    html_content = open(file, 'r', encoding='utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    list = soup.find_all('p')
    text = set()
    for t in list:
        text.add(t.get_text())
    return text


if __name__ == '__main__':
    text = parser('index.html')
    for t in text:
        print(t)
