import requests
from bs4 import BeautifulSoup as BS
URL = "https://neman.kg/lekarstvennye-sredstva/"


def get_response(url):     # это функция проверяет сайт работает ли он или нет 
    response = requests.get(url)
    if response.status_code == 200: 
        return response.text
    else:
        return "Error"





def anekdot(html):                    
    soup = BS(html, 'html.parser') 
    content1 = soup.find("div", {"class":"row-fluid"}).find("div",{"class":"span16"})
    content2 = content1.find("div",{"class":"row-fluid"}).find("div",{"class":"span12"})
    content3 = content2.find("div",{"id":"category_products_12"}).find("div",{"calss":"ty-pagination-container cm-pagination-container"})
    content4 = content3.find("div",{"class":"grid-list"}).find("div",{"class":"categories_view_pagination_contents"})
    content5 = content4.find("div",{"class":"ty-column3"})
    print(content5)





# <div id="categories_view_pagination_contents">





# <div class="ty-pagination-container cm-pagination-container" id="pagination_contents">







def main():     #это функция выполняет все функции 
    URL = "https://neman.kg/lekarstvennye-sredstva/"
    main = anekdot(get_response(URL))
    


if __name__ == "__main__": #он вызывает функцию main() автоматически
    main()