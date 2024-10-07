# ==================================================
#          TIMER ZONEProject
#          Using data sciencie and data base
#          Understanding methods in Python and datas
# ==================================================




import requests  # Import the library for making HTTP requests
from bs4 import BeautifulSoup  # Import the library for parsing HTML
import time  # Import the library for time manipulation

# Ask the user to input the name of a city to know the local time
print("Which country do you want to know about the timer (GMT)?")
user_choice = input("Please type the name of city: ")


# Function to display a waiting message
def beautifying():
    for x in range(2):  
        time.sleep(0.7)  
        print("Waiting...")  


# Call the waiting function to beautifying
beautifying()



# Function to get time information for a specified city
def time_info(choice):

    
    # Create a search URL for Google to get the time in the chosen city
    link = f"https://www.google.com/search?q=time+in+{choice}"


    
    # Define headers for the request, mimicking a web browser
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"
    }


    
    # Make the request to the URL
    requisição = requests.get(link, headers=header)


    
    # Parse the returned HTML using BeautifulSoup
    site = BeautifulSoup(requisição.text, "html.parser")


    
    # Fin
    d the div that contains the local time
    timer = site.find("div", class_="YwPhnf")
    timerr = timer.get_text()  # Extract the text from the div


    
    # Find the span that contains the day and time in GMT
    day_gmt = site.find("span", class_="KfQeJ")
    day_gmtr = day_gmt.get_text()  # Extract the text from the span


    
    # Find the span that contains the country zone
    country_zone = site.find("span", class_="vk_gy vk_sh")
    country_zoner = country_zone.get_text()  # Extract the text from the span


    
    # Display the obtained information
    print(f" {timerr}\n {day_gmtr}\n{country_zoner}")




# Call the time_info function following the variable user_choices
time_info(user_choice)
