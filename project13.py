import requests
from bs4 import BeautifulSoup
import webbrowser


print("Which country do you want to know about the timer (GMT)")
user_choice = input("Please type the name of city: ")

def time_info(choice):
    link = f"https://www.google.com/search?q=time+in+{choice}"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"                 }
    requisição = requests.get(link, headers = header)
    site = BeautifulSoup(requisição.text, "html.parser")

    timer = site.find("div", class_ ="YwPhnf")
    timerr = timer.get_text()


    day_gmt = site.find("span", class_ = "KfQeJ")
    day_gmtr = day_gmt.get_text()

    country_zone = site.find("span", class_ = "vk_gy vk_sh")
    country_zoner = country_zone.get_text()

    print(f" {timerr}\n {day_gmtr}\n{country_zoner}")




time_info(user_choice)

