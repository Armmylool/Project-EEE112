from bs4 import BeautifulSoup
import requests
import time
import os

user = str(input("What do you want to eat : "))


def find() :
    page = 1
    while page <= 10 :
        html_text = requests.get('https://www.myfitnesspal.com/nutrition-facts-calories/'+ user + '/' + str(page)).text
        soup = BeautifulSoup(html_text, 'lxml')
        table = soup.find_all('div',class_ = "MuiBox-root css-1cheb17") 
        for e in table :
            menu = e.find('div',class_ = 'MuiBox-root css-x1sij0').text
            amount = e.find('p',class_ = 'MuiTypography-root MuiTypography-body1 css-w1kjmb').text
            more_info = e.a['href']
            nutrition = e.find('div',class_ = 'MuiBox-root css-2imjyh').text
            if user in menu :
                with open(f'Food.txt','a',encoding= "UTF-8") as f :
                    f.write(f"Menu :{menu.strip()} \n")
                    f.write(f"Amount :{amount.strip()} \n")
                    f.write(f"Nutrition :{nutrition.strip()} \n")
                    f.write(f"More info :{'https://www.myfitnesspal.com'+more_info.strip()} \n")
                    f.write(f'\n')
                print(f'''
                    menu : {menu}
                    amount : {amount}
                    more info : {'https://www.myfitnesspal.com'+more_info}
                    nutrition : {nutrition}
                    ''')            
        page += 1

if __name__ == '__main__' :
        find()
        time_wait = 10
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait * 1)