import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getrand(a, b):
    return random.randint(a, b)


def click_radio(wait, index):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@role='radio'])[{index}]")))
        btn.click()
        print(f"Radio (XPath index {index}) clicked.")
        time.sleep(1)
    except Exception as exc:
        print(f"Error clicking radio {index}: {exc}")

def click_checkbox(wait, index):
    try:
        box = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@role='checkbox'])[{index}]")))
        box.click()
        print(f"Checkbox (XPath index {index}) clicked.")
        time.sleep(1)
    except Exception as exc:
        print(f"Error clicking checkbox {index}: {exc}")

url = "https://docs.google.com/forms/d/1-CAARECzVdbPQh2Is88dso7WHCfc4Jw3vSdMwT8ttag/viewform?edit_requested=true"

for _ in range(50):
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    # Q1 - Age: 1-4
    click_radio(wait, getrand(1, 2))



    # Scroll and submit
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    try:
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(., 'Submit')]"))
        )
        submit_button.click()
        print("Clicked 'Submit' button.")
        time.sleep(2)
        confirmation_text = driver.find_elements(By.XPATH, "//div[contains(text(),'Your response has been recorded')]")
        if confirmation_text:
            print("Form submitted successfully.")
    except Exception as exc:
        print(f"Error clicking Submit: {exc}")

    driver.quit()
