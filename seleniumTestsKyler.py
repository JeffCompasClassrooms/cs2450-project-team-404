'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Specify the path to ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver" #you'll need to put the path to YOUR chromedriver here
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Don't specify chromedriver path!
driver = webdriver.Chrome(options=options)

try:
    tests_passed = 0
    tests_ran = 0
    driver.get("http://localhost:5000")
    time.sleep(2)

    # Find and fill the username field
    username_field = driver.find_element(By.NAME, "username")  # Change based on actual element
    username_field.send_keys("KylerS")  # Replace with your actual username

    # Find and fill the password field
    password_field = driver.find_element(By.NAME, "password")  # Change based on actual element
    password_field.send_keys("Pass1234!")  # Replace with your actual password

    # Submit the login form
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    login_button.click()
    time.sleep(2)
    print(driver.page_source)


    print("--= Beginning Tests - Kyler Sousley =--")
    logout_button = driver.find_element(By.CSS_SELECTOR, "button[name='logout']")
    time.sleep(2)
    if logout_button:
        print("[PASSED] - Logout Button Exists")
        tests_passed += 1
    else:
        print("[FAILED] - Logout Button Not Found")
    tests_ran += 1

    music_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Music']")
    time.sleep(2)
    if music_checkbox:
        print("[PASSED] - Music Tag Checkbox Exists")
        tests_passed += 1
    else:
        print("[FAILED] - Music Tag Checkbox Not Found")
    tests_ran += 1

    astronomy_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Astronomy']")
    time.sleep(2)
    if astronomy_checkbox:
        print("[PASSED] - Astronomy Tag Checkbox Exists")
        tests_passed += 1
    else:
        print("[FAILED] - Astronomy Tag Checkbox Not Found")
    tests_ran += 1

    gaming_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Gaming']")
    time.sleep(2)
    if gaming_checkbox:
        print("[PASSED] - Gaming Tag Checkbox Exists")
        tests_passed += 1
    else:
        print("[FAILED] - Gaming Tag Checkbox Not Found")
    tests_ran += 1

    post_field = driver.find_element(By.CSS_SELECTOR, "textarea[name='post']")
    post_field.send_keys("selenium testing")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[name='post-submit']")
    submit_button.click()
    time.sleep(2)

    error_popup = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-dismissible alert-danger fade show'][role='alert']")
    error_popup_text = error_popup.text.replace('×', '').strip()
    if error_popup:
        if error_popup_text == "Must select one or more tags.":
            print(f"[PASSED] - '{error_popup_text}' alert exists and text is correct")
            tests_passed += 1
        else:
            print(f"[FAILED] - 'Must select one or more tags.' alert text isnt correct. Text found: {error_popup_text}")
    else:
        print("[FAILED] - 'Must select one or more tags.' alert not found")
    tests_ran += 1
    
    post_field = driver.find_element(By.CSS_SELECTOR, "textarea[name='post']")
    post_field.send_keys("selenium testing")
    music_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Music']")
    music_checkbox.click()
    time.sleep(2)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[name='post-submit']")
    submit_button.click()
    post_text_field = driver.find_element(By.CSS_SELECTOR, "p[class='card-text']")
    post_text = post_text_field.text.strip()
    if post_text == 'selenium testing':
        print("[PASSED] - Post successfully submitted!")
        tests_passed += 1
    else:
        print("[FAILED] - Post did not submit")
    tests_ran += 1

    tags_field = driver.find_element(By.CSS_SELECTOR, "span[class='badge bg-secondary']")
    tag = tags_field.text.strip()
    if tag == "Music":
        print("[PASSED] - Tag on post matches selected Music tag")
        tests_passed += 1
    else:
        print("[FAILED] - Tag on post does not match selected Music tag")
    tests_ran += 1

    post_field = driver.find_element(By.CSS_SELECTOR, "textarea[name='post']")
    post_field.send_keys("selenium testing all tags")
    music_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Music']")
    music_checkbox.click()
    astronomy_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Astronomy']")
    astronomy_checkbox.click()
    gaming_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='Gaming']")
    gaming_checkbox.click()
    time.sleep(2)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[name='post-submit']")
    submit_button.click()
    tags_field = driver.find_elements(By.CSS_SELECTOR, "span[class='badge bg-secondary']")

    tags = [tag.text for tag in tags_field]
    expected_tags = ["Music", "Gaming", "Astronomy"]

    all_present = True
    for tag in tags:
        if tag not in expected_tags:
            all_present = False
            break
    if all_present:
        print("[PASSED] - All tags are on the post")
        tests_passed += 1
    else:
        print("[FAILED] - Some tags are not on the post")
    tests_ran += 1
    
    add_friend_field = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    add_friend_field.send_keys("TestAccount2")
    add_friend_submit = driver.find_element(By.CSS_SELECTOR, "button[name='addfriend']")
    add_friend_submit.click()
    time.sleep(2)
    alert = driver.find_element(By.CSS_SELECTOR, "div[role='alert']")
    alert_text = alert.text.replace('×', '').strip()
    if alert_text == "Friend TestAccount2 added successfully!":
        print("[PASSED] - Friend was added successfully")
        tests_passed += 1
    else:
        print("[FAILED] - Friend was not added successfully")
    tests_ran += 1

    add_friend_field = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    add_friend_field.send_keys("TestAccount2")
    add_friend_submit = driver.find_element(By.CSS_SELECTOR, "button[name='addfriend']")
    add_friend_submit.click()
    time.sleep(2)
    alert = driver.find_element(By.CSS_SELECTOR, "div[role='alert']")
    alert_text = alert.text.replace('×', '').strip()
    if alert_text == "You are already friends with TestAccount2.":
        print("[PASSED] - Friend already added alert exists")
        tests_passed += 1
    else:
        print("[FAILED] - Friend already added alert not found")
    tests_ran += 1

except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    print(f"{tests_ran} Tests Ran: {tests_passed} Tests Passed")
    driver.quit()
