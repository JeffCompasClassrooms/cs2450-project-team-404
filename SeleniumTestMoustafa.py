from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Specify the path to ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver" #you'll need to put the path to YOUR chromedriver here
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")

    # Locate the "Sign Up" button using a CSS selector
    sign_up_button = driver.find_element(By.ID, "signup")  # Replace with the actual selector

    # Verify that the "Sign Up" button exists
    if sign_up_button:
        print("[PASSED] - 'Sign Up' button exists.")
    else:
        print("[FAILED] - 'Sign Up' button not found.")
    

    # Click the "Sign Up" button to test its functionality
    sign_up_button.click()
    time.sleep(10)
    # Validate the resulting page or action (e.g., a redirect)
    expected_url = 'http://localhost:5000/register'  # Replace with the expected URL
    if driver.current_url == expected_url:
        print("[PASSED] - 'Sign Up' button redirected correctly.")
    else:
        print(f"[FAILED] - 'Sign Up' button redirection failed. Current URL: {driver.current_url}")



except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")



try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    if login_button:
        print("[PASSED] - Login Button Exists.")
    else:
        print("[FAILED] - Login button not found.")


    # Find and fill the username field
    username_field = driver.find_element(By.NAME, "username")  # Change based on actual element
    username_field.send_keys("TuNe2025")  # Replace with your actual username

    # Find and fill the password field
    password_field = driver.find_element(By.NAME, "password")  # Change based on actual element
    password_field.send_keys("Abcd0123")  # Replace with your actual password

    # Submit the login form
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    login_button.click()

except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")


try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")

    setting_link = driver.find_element(By.CSS_SELECTOR, "a[class= 'nav-link'][href = '/settings']")
    if setting_link:
        print("[PASSED] - link Exists.")
    else:
        print("[FAILED] - link not found.")

    setting_link.click()
    time.sleep(5)
    # Validate the resulting page or action (e.g., a redirect)
    expected_url = 'http://localhost:5000/settings'  
    if driver.current_url == expected_url:
        print("[PASSED] - 'Settings link' button redirected correctly.")
    else:
        print(f"[FAILED] - 'Settings link' button redirection failed. Current URL: {driver.current_url}")

except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")

try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")
    profile_link = driver.find_element(By.CSS_SELECTOR, "a[class= 'nav-link'][href = '/profile']")
    if profile_link:
        print("[PASSED] - link Exists.")
    else:
        print("[FAILED] - link not found.")

    profile_link.click()
    time.sleep(10)
    # Validate the resulting page or action (e.g., a redirect)
    expected_url = 'http://localhost:5000/profile'  
    if driver.current_url == expected_url:
        print("[PASSED] - 'Profile' button redirected correctly.")
    else:
        print(f"[FAILED] - 'Profile' button redirection failed. Current URL: {driver.current_url}")

except Exception as e:
    print("Error:", e)
finally:
    print("--= Ending Tests =--")

try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")
    # Locate the target element by CSS selector
    element = driver.find_element(By.CSS_SELECTOR, "body")  # Replace with your selector
    # Get the background color of the element
    background_color = element.value_of_css_property('background-color')
    # Define the expected background color
    expected_color = 'rgba(47, 79, 79, 1)'  # Example: teal color in rgba format
    # Check if the background color matches the expected color
    if background_color == expected_color:
        print("[PASSED] - Background color matches.")
    else:
        print(f"[FAILED] - Background color does not match. Expected: {expected_color}, Found: {background_color}")


    element = driver.find_element(By.CSS_SELECTOR, "div")  
    text_color = element.value_of_css_property('color')
    expected_color = 'rgba(0, 0, 0, 1)'  
    if text_color == expected_color:
        print("[PASSED] - Text color matches.")
    else:
        print(f"[FAILED] - Text color does not match. Expected: {expected_color}, Found: {text_color}")


except Exception as e:
    print("Error:", e)
finally:
    print("--= Ending Tests =--")


try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")
    muse_link = driver.find_element(By.CSS_SELECTOR, "a[class= 'nav-link'][href = 'https://musescore.com']")
    if muse_link:
        print("[PASSED] - link Exists.")
    else:
        print("[FAILED] - link not found.")

    muse_link.click()
    time.sleep(10)
    # Validate the resulting page or action (e.g., a redirect)
    expected_url = 'https://musescore.com/'  
    if driver.current_url == expected_url:
        print("[PASSED] - 'musescore' button redirected correctly.")
    else:
        print(f"[FAILED] - 'Musescore' button redirection failed. Current URL: {driver.current_url}")    
    

    

except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    driver.quit()
