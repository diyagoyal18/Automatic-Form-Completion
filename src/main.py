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

url = "https://docs.google.com/forms/d/e/1FAIpQLScppDx0zUIpjzQRSLj97ewdXEoNtMqaywh3GWRdIHkyvjKMng/viewform?usp=sharing"

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
    click_radio(wait, getrand(1, 4))

    # Q2 - Gender: 5-7
    click_radio(wait, getrand(5, 6))

    # Q3 - Academic Year: 8-12
    click_radio(wait, getrand(8, 12))

    # Q4 - Frequency of nostalgia: 13-17
    click_radio(wait, getrand(13, 17))

    # Q5 - Nostalgia triggers (checkboxes): 1-7
    for i in random.sample(range(1, 8), random.randint(2, 4)):
        click_checkbox(wait, i)

    # Q6 - Feelings (checkboxes): 8-13
    for i in random.sample(range(8, 13), random.randint(2,4)):
        click_checkbox(wait, i)


##5 


    # Q7 - Coping with stress: 18-22
    click_radio(wait, getrand(18, 22))

    # Q8 - Reconnect with someone: 23-25
    click_radio(wait, getrand(23, 25))

    # Q9 - Social connection: 26-28
    click_radio(wait, getrand(26, 28))

    # Q10 - Motivation/Reflection: 29-31
    click_radio(wait, getrand(29, 31))

    # Q11 - Confidence/Inspiration: 32-35
    click_radio(wait, getrand(32, 35))

    # Q12 - Types of memories: checkboxes 14–19
    for i in random.sample(range(14, 20), 2):
        click_checkbox(wait, i)

    # Q13 - Linear scale: 36–40
    click_radio(wait, getrand(36, 40))

    # Q14 - People/Places/Things: 41–44
    click_radio(wait, getrand(41, 44))

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
