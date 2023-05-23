from selenium import webdriver
from bs4 import BeautifulSoup
import random
import json
import csv
import os

def driver_setup():
    # set up driver
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    options.add_argument('--headless')
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"]
    user_agent = random.choice(user_agents)
    #Specifying a random user agent
    options.add_argument(f'--user-agent={user_agent}')
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()

    return driver


def getstudentinfo(degree, depart):
    driver = driver_setup()

    if degree == 'BSMS' :
        url = "https://www.iiserpune.ac.in/institute/people/students/?year=2022" + str(depart) + "&degree=BSMS&department=0&alumni=False#Results"
    else:
        url = "https://www.iiserpune.ac.in/institute/people/students/?year=2022&degree=" + degree +"&department="+ str(depart) +"&alumni=False#Results"

     
    driver.get(url)
    try :
        pagesource = driver.page_source
        soup = BeautifulSoup(pagesource, 'html.parser')
        students = soup.select_one('div.student-list-group').text.split("\n\n\n")
        list_of_students = [student.replace("\r", " : ").replace("\n", "") if student is not None else student for student in students ]
        list_of_students = list_of_students[2:]
        for stud in list_of_students:
            student={}
            try:
                details = stud.split(":")
                student["Name"] = details[0].strip()
                student["RegistrationNumber"] =  details[1].replace(" Registration No." , "").strip()
                student["Degree"] = degree
                if degree != 'BSMS' and depart == 2:
                     student["Department"] = "Biology"

                elif degree != 'BSMS' and depart == 1:
                     student["Department"] = "Physics"

                elif degree != 'BSMS' and depart == 3:
                     student["Department"] = "Chemistry"

                elif degree != 'BSMS' and depart == 4:
                     student["Department"] = "Mathematics"

                elif degree != 'BSMS' and depart == 5:
                     student["Department"] = "Earth and Climate Science"
                
                elif degree != 'BSMS' and depart == 6:
                     student["Department"] = "Humanities and Social Science"
                
                elif degree != 'BSMS' and depart == 7:
                     student["Department"] = "Data Science"

                elif degree == 'BSMS':
                     student["Department"] = None                
                                
                print(student)
                list_iiser.append(student)
            except:
                pass

    except Exception as e:
        print(e)
    return list_iiser

def getalumniinfo(year, degree, depart):
    driver = driver_setup()

    if degree == 'BSMS' :
        url = "https://www.iiserpune.ac.in/institute/people/students?Alumni=True&Year="+ str(year) + "&Degree="+ degree +"&Department=0#Results"
    else:
        url = "https://www.iiserpune.ac.in/institute/people/students?Alumni=True&Year="+ str(year) + "&Degree="+ degree +"&Department=" + str(depart)+ "#Results"

     
    driver.get(url)
    try :
        pagesource = driver.page_source
        soup = BeautifulSoup(pagesource, 'html.parser')
        students = soup.select_one('div.student-list-group').text.split("\n\n\n")
        list_of_students = [student.replace("\r", " : ").replace("\n", "") if student is not None else student for student in students ]
        list_of_students = list_of_students[2:]
        for stud in list_of_students:
            student={}
            try:
                details = stud.split(":")
                student["Name"] = details[0].strip()
                student["RegistrationNumber"] =  details[1].replace(" Registration No." , "").strip()
                student["Degree"] = degree
                student["GraduatedYear"] = year
                if degree != 'BSMS' and depart == 2:
                     student["Department"] = "Biology"

                elif degree != 'BSMS' and depart == 1:
                     student["Department"] = "Physics"

                elif degree != 'BSMS' and depart == 3:
                     student["Department"] = "Chemistry"

                elif degree != 'BSMS' and depart == 4:
                     student["Department"] = "Mathematics"

                elif degree != 'BSMS' and depart == 5:
                     student["Department"] = "Earth and Climate Science"
                
                elif degree != 'BSMS' and depart == 6:
                     student["Department"] = "Humanities and Social Science"
                
                elif degree != 'BSMS' and depart == 7:
                     student["Department"] = "Data Science"

                elif degree == 'BSMS':
                     student["Department"] = None                
                                
                print(student)
                list_alumni.append(student)
            except:
                pass

    except Exception as e:
        print(e)
    return list_alumni


years = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
degrees = ['BSMS' , 'PhD' , 'Integrated Phd']
departments= [1,2,3,4,5,6,7]
list_iiser=[]


# for degree in degrees:
#      for depart in departments:
#           getstudentinfo(degree, depart)


# with open('iiserstudents.csv', 'w', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames= list_iiser[0].keys())
#         writer.writeheader()
#         writer.writerows(list_iiser)
file_exists = os.path.isfile('iiseralumni.csv')

for year in years:
    list_alumni=[]
    for degree in degrees:
        for depart in departments:
            getalumniinfo(year, degree, depart)
    with open('iiseralumni.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames= list_alumni[0].keys())
        if not file_exists:
            writer.writeheader()
            writer.writerows(list_alumni)
        else:
            writer.writerows(list_alumni)


#getstudentinfo('Phd', 2)

