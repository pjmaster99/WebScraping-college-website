import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from tqdm import tqdm


def get_driver():
    chrome_options = Options()
    ## The sandbox environment provides a testing and staging platform without allowing the code being tested to
    ## make changes to existing code and databases
    chrome_options.add_argument('--no-sandbox')
    ## A headless browser is a web browser without a graphical user interface. Headless browsers provide automated 
    ## control of a web page in an environment similar to popular web browsers, but they are executed via a 
    ## command-line interface or using network communication.
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    return driver