from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()


def test_scores_service():
    web_driver.get('http://127.0.0.1:5000')
    score_test = web_driver.find_element(By.XPATH, '//*[@id="score"]')
    n_score = int(score_test.text)

    if n_score >= 1 or n_score <= 1000:
        return True
    else:
        return False


def main_function():
    valid = test_scores_service()
    if valid:
        return 0
    else:
        return -1



