from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
import math
import requests
chrome_driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

skills = [
    "mobile-app-development", 
    "machine-learning",
    "frontend-development",
    "nodejs",
    "react-js",
    "django",
    "data-analysis",
    "web-development",
    "python",
    "javascript"
    ]
name = []
country = []
hourly_paid = []
reviews = []
over_all_rating = []
on_time = []
on_budget = []
accept_rate = []
repeat_hire_rate = []
joinded = []
specialization  = []
links = []
def is_internet_available():

    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False
def get_freelancers(skills, name, country, hourly_paid, reviews, over_all_rating, links):
    for skill in range(len(skills)):
        c = 1
        while True:
                try:
                    while True:
                        try:
                            driver.get(f"https://www.freelancer.com/freelancers/skills/{skills[skill]}/{c}")
                            break
                        except Exception as e:
                            print(f"Error:{e}, Waiting for internet connection...")
                            while not is_internet_available():
                                print("No internet connection, Retrying in 5 Seconds....")
                                time.sleep(5)
                                continue
                    time.sleep(5)
                    result = wait.until(
                            EC.presence_of_element_located((By.CLASS_NAME, "result-amount"))
                            )
                    num_result = re.search(r'\d+', result.text)

                    country_freelancer = wait.until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "flag-icon"))
                    )
                    for i in country_freelancer:
                        country.append(i.get_attribute('alt'))
                    name_freelancer = wait.until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "find-freelancer-username"))
                    )
                    for i in name_freelancer:
                        name.append(i.text)
                        links.append(i.get_attribute('href'))
                        specialization.append(skills[skill])
                    rate_freelancer = wait.until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, "Rating.Rating--labeled"))
                        )
                    hour_pay = wait.until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "user-hourly-rate"))
                    )
                    for i in hour_pay:
                        hourly_paid.append(i.text)
                        hourly_paid =  [item for item in hourly_paid if item != '']

                    for i in rate_freelancer:
                            over_all_rating.append(i.get_attribute("data-star_rating"))
                    num_projects = wait.until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "directory-freelancer-rating"))
                    )
                    for i in num_projects:
                        num = re.search(r'\d+', i.text)
                        reviews.append(int(num.group()))
                    if c == (math.ceil(int(num_result.group())/10)):
                            break
                    print("*"*100)
                    print(len(name))
                    print(len(hourly_paid))
                    print(len(over_all_rating))
                    print(len(country))
                    print(len(reviews))
                    print(f"Page {c} is done for {skills[skill]}")
                    print("*"*100)
                    c += 1
                except:
                     break

    return name, hourly_paid, over_all_rating, country, reviews, links, specialization
# name, hourly_paid, over_all_rating, country, reviews, links, specialization = get_freelancers(skills, name, country, hourly_paid, reviews, over_all_rating, links)

def profile(links, joined, on_time, on_budget, accept_rate, repeat_hire_rate):
    for i in links:
        while True:
            try:
                driver.get(i)
                break
            except Exception as e:
                print(f"Error:{e}, Waiting for internet connection...")
                while not is_internet_available():
                    print("No internet connection, Retrying in 5 Seconds....")
                    time.sleep(5)
                    continue
        time.sleep(1)
        try:
            elements = driver.find_element(By.XPATH, "//div[contains(text(), 'Joined on')]")
            joinded.append(elements.text)
        except:
            joinded.append("0%")
        try:
            onTime = driver.find_element(By.XPATH, "/html/body/app-root/app-logged-out-shell/div/app-user-profile/div[2]/div[2]/fl-container/fl-grid/fl-col[1]/app-user-profile-summary-redesign/div/fl-grid/fl-col[2]/div/app-user-profile-stats/fl-card/div/div/div/div[2]/app-user-profile-stats-reputation/app-user-profile-stats-reputation-item[1]/div/div/fl-text/div")
            on_time.append(onTime.text)
        except:
             on_time.append("0%")
        try:
            onBudget = driver.find_element(By.XPATH, "/html/body/app-root/app-logged-out-shell/div/app-user-profile/div[2]/div[2]/fl-container/fl-grid/fl-col[1]/app-user-profile-summary-redesign/div/fl-grid/fl-col[2]/div/app-user-profile-stats/fl-card/div/div/div/div[2]/app-user-profile-stats-reputation/app-user-profile-stats-reputation-item[2]/div/div/fl-text/div")
            on_budget.append(onBudget.text)
        except:
             on_budget.append("0%")
        try:
            acceptRate = driver.find_element(By.XPATH,"/html/body/app-root/app-logged-out-shell/div/app-user-profile/div[2]/div[2]/fl-container/fl-grid/fl-col[1]/app-user-profile-summary-redesign/div/fl-grid/fl-col[2]/div/app-user-profile-stats/fl-card/div/div/div/div[2]/app-user-profile-stats-reputation/app-user-profile-stats-reputation-item[3]/div/div/fl-text/div")
            accept_rate.append(acceptRate.text)
        except:
             accept_rate.append("0%")
        try:
            hireRepeat = driver.find_element(By.XPATH, "/html/body/app-root/app-logged-out-shell/div/app-user-profile/div[2]/div[2]/fl-container/fl-grid/fl-col[1]/app-user-profile-summary-redesign/div/fl-grid/fl-col[2]/div/app-user-profile-stats/fl-card/div/div/div/div[2]/app-user-profile-stats-reputation/app-user-profile-stats-reputation-item[4]/div/div/fl-text/div")
            repeat_hire_rate.append(hireRepeat.text)
        except:
            repeat_hire_rate.append("0%")
        c = 1
        remain = len(links) - c
        print(f"Remain {remain}")
        c += 1
    return on_time, on_budget, accept_rate, repeat_hire_rate, joinded

# on_time, on_budget, accept_rate, repeat_hire_rate, joinded = profile(links)

def save(name, country, hourly_paid, reviews, over_all_rating, specialization, on_time, on_budget, accept_rate, repeat_hire_rate, joinded):
    data = {
        "Name" : name,
        "Country" : country,
        "Hourly_Paid" :hourly_paid,
        "Reviews" : reviews,
        "Rating" : over_all_rating,
        "Skill" : specialization,
        "On_Time" : on_time,
        "On_Budget" : on_budget,
        "Accept_Rate" : accept_rate,
        "Repeat_Hire" : repeat_hire_rate,
        "Joined" :joinded
    }

    Data = pd.DataFrame(data)
    Data.to_excel("online_freelancers.xlsx", index=False)
# save(name, country, hourly_paid, reviews, over_all_rating, specialization, on_time, on_budget, accept_rate, repeat_hire_rate, joinded)
