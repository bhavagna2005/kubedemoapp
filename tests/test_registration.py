

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration():
    driver = webdriver.Chrome()

    try:
        driver.get("http://127.0.0.1:5000")

        driver.find_element(By.NAME, "name").send_keys("Bhavagna")
        driver.find_element(By.NAME, "email").send_keys("test@example.com")
        driver.find_element(By.TAG_NAME, "button").click()

        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "p"))
        )

        assert "Registration successful" in message.text
        print("Test Passed:", message.text)

    finally:
        driver.quit()

