from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Specify the path to ChromeDriver
chrome_driver_path = "/home/cmaxwell2/chromedriver-linux64/chromedriver" #you'll need to put the path to YOUR chromedriver here
service = Service(chrome_driver_path)
#driver = webdriver.Chrome(service=service)

try:
    driver.get("http://localhost:5000")
    time.sleep(2)

    print("--= Beginning Tests - Creed Maxwell =--")

    testsPassed = 0
    testsRan = 0

    # Find and fill the username field
    username_field = driver.find_element(By.NAME, "username")  # Change based on actual element
    testsRan += 1
    if username_field:
        print("[PASSED] - Username Field Exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Username Field not found.")
    username_field.send_keys("test123")  # Replace with your actual username

    # Find and fill the password field
    password_field = driver.find_element(By.NAME, "password")  # Change based on actual element
    testsRan += 1
    if password_field:
        print("[PASSED] - Password Field Exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Password Field not found.")
    password_field.send_keys("Test1234")  # Replace with your actual password

    # Submit the login form
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    login_button.click()
    
    '''
    # find sign up button
    signup_btn = driver.find_element(By.ID, "signup")
    signup_btn.click()

    time.sleep(2)

    # Find and fill the username field
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("test123") 

    # Find and fill the email field
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("foo@gmail.com")

    # Find and fill the password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Test1234")
    cpassword_field = driver.find_element(By.NAME, "cpassword")
    cpassword_field.send_keys("Test1234")

    # Find and fill the tags form
    music_tag = driver.find_element(By.ID, "tag_Music")
    astronomy_tag = driver.find_element(By.ID, "tag_Astronomy")
    music_tag.click()
    astronomy_tag.click()

    # Submit the login form
    register_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Register']")
    register_button.click()

    time.sleep(2)

    print("--= Register Successful =--")
    '''

    # post button test
    post_button = driver.find_element(By.CSS_SELECTOR, "button[name='post-submit']")

    testsRan += 1
    if post_button:
        print("[PASSED] - Post Button Exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Post button not found.")

    # post
    post_area = driver.find_element(By.CSS_SELECTOR, "textarea[class='form-control'][name='post']")
    testsRan += 1
    if post_area:
        print("[PASSED] - Post input exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Post input not found.")

    # post tags
    post_tags = driver.find_element(By.CSS_SELECTOR, "div[id='tag-container']")
    testsRan += 1
    if post_tags:
        print("[PASSED] - Post tags exist.")
        testsPassed += 1
    else:
        print("[FAILED] - Post tags not found.")

    # post creation
    testsRan += 1
    if post_area:
        post_text = "Test post"
        post_area.send_keys(post_text)
        if post_tags:
            tag_check = driver.find_element(By.ID, "tag_Astronomy")
            tag_check.click()
            if post_button:
                post_button.click()
            else:
                print("[FAILED] - Post button not found.")
        else:
            print("[FAILED] - Post tags not found.")
        
    else:
        print("[FAILED] - Post input not found.")
    
    time.sleep(2)
    created_post = driver.find_element(By.XPATH, f"//*[contains(text(), '{post_text}')]")
    if created_post:
        print("[PASSED] - Post created.")
        testsPassed += 1

        # Verify if the post contains the tag "Astronomy"
        testsRan += 1
        post_with_tag = created_post.find_element(By.XPATH, "./following-sibling::p[span[contains(text(), 'Astronomy')]]")
        if post_with_tag:
            print("[PASSED] - Post has correct tag.")
            testsPassed += 1
        else:
            print("[FAILED] - Post does not have the correct tag.")
    else:
        print("[FAILED] - Post not found in feed.")
    
    # add friend button
    add_friend_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][name='addfriend']")
    testsRan += 1
    if add_friend_button:
        print("[PASSED] - Add Friend Button Exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Add Friend Button not found.")

    # add friend field
    add_friend_field = driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='name']")    
    testsRan +=1 
    if add_friend_field:
        print("[PASSED] - Add friend username field exists.")
        testsPassed += 1
        # add friend test
        testsRan += 1
        add_friend_username = "hello1234"
        add_friend_field.send_keys(add_friend_username)
        if add_friend_button:
            add_friend_button.click()
            time.sleep(2)
            friend_li = driver.find_element(By.XPATH, f"//a[contains(text(), '{add_friend_username}')]")
            if friend_li:
                print("[PASSED] - Added friend successfully.")
                testsPassed += 1
            else:
                print("[FAILED] - Friend not added successfully.")
        else:
            print("[FAILED] - Add Friend button not found.]")
    else:
        print("[FAILED] - Add friend field not found.")

    '''
    # test the alert
    testsRan += 1
    alert = driver.find_element(By.CSS_SELECTOR, "div.alert-dismissible")

    if alert:
        print("[PASSED] - Alert exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Alert not found.")
    
    # test alert close button
    testsRan += 1
    alert_button = alert.find_element(By.CSS_SELECTOR, "button.close")

    if alert_button:
        print("[PASSED] - Alert close button exists.")
        testsPassed += 1
    else:
        print("[FAILED] - Alert close button not found.")
    '''
    

except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    print(testsRan, " Tests Ran: ", testsPassed, " Tests Passed")
    driver.quit()