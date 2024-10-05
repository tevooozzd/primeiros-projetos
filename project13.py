import requests
from bs4 import BeautifulSoup

print("Which of these cities do you want to know the time for?")
print(" São Paulo - 1 (GMT -3)\n California - 2 (GMT -7)\n Tokyo - 3 (GMT +9)\n Berlin - 4 (GMT +2)")
user_choice = int(input("Please enter your choice: "))

def time_info(choice):
    if choice == 1:
        selected_city = "Brasilia (GMT: -3)"
        link = "https://www.google.com/search?q=current+time+in+brasilia"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"
        }
        request = requests.get(link, headers=header)
        site = BeautifulSoup(request.text, "html.parser")
        search_result = site.find("div", class_="YwPhnf")
        print(f"Your selected city is {selected_city}, and the time is {search_result.get_text()}")
    elif choice == 2:
        selected_city = "California (GMT: -7)"
        link = "https://www.google.com/search?q=current+time+in+california"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"
        }
        request = requests.get(link, headers=header)
        site = BeautifulSoup(request.text, "html.parser")
        search_result = site.find("div", class_="YwPhnf")
        print(f"Your selected city is {selected_city}, and the time is {search_result.get_text()}")
    elif choice == 3:
        selected_city = "Tokyo (GMT: +9)"
        link = "https://www.google.com/search?q=current+time+in+tokyo"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"
        }
        request = requests.get(link, headers=header)
        site = BeautifulSoup(request.text, "html.parser")
        search_result = site.find("div", class_="YwPhnf")
        print(f"Your selected city is {selected_city}, and the time is {search_result.get_text()}")
    else:
        selected_city = "Berlin (GMT: +2)"
        link = "https://www.google.com/search?q=current+time+in+berlin"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"
        }
        request = requests.get(link, headers=header)
        site = BeautifulSoup(request.text, "html.parser")
        search_result = site.find("div", class_="YwPhnf")
        print(f"Your selected city is {selected_city}, and the time is {search_result.get_text()}")

time_info(user_choice)
