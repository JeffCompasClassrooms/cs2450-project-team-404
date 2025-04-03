"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service"""
"""import time"""

# Specify the path to ChromeDriver
"""chrome_driver_path = "/usr/local/bin/chromedriver" #you'll need to put the path to YOUR chromedriver here
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(ChromeDriverManager().install())
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
    time.sleep(2)
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

    pygame_link = driver.find_element(By.CSS_SELECTOR, "a[class= 'nav-link'][href = 'https://www.pygame.org/wiki/Contribute']")
    if pygame_link:
        print("[PASSED] - link Exists.")
    else:
        print("[FAILED] - link not found.")

    pygame_link.click()
    time.sleep(2)
    # Validate the resulting page or action (e.g., a redirect)
    expected_url = 'https://www.pygame.org/wiki/Contribute'  
    if driver.current_url == expected_url:
        print("[PASSED] - 'PYgame link' button redirected correctly.")
    else:
        print(f"[FAILED] - 'PYgame link' button redirection failed. Current URL: {driver.current_url}")


except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")


try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")
    space_X_link = driver.find_element(By.CSS_SELECTOR, "a[class= 'nav-link'][href = 'https://www.spacex.com']")
    if space_X_link:
        print("[PASSED] - link Exists.")
    else:
        print("[FAILED] - link not found.")

    space_X_link.click()
    time.sleep(10)
    # Validate the resulting page or action (e.g., a redirect)
    expected_url = 'https://www.spacex.com/'  
    if driver.current_url == expected_url:
        print("[PASSED] - 'space X' button redirected correctly.")
    else:
        print(f"[FAILED] - 'space X' button redirection failed. Current URL: {driver.current_url}")

except Exception as e:
    print("Error:", e)
finally:
    print("--= Ending Tests =--")



# Set up the WebDriver
try:
    driver.get("http://localhost:5000/loginscreen")# Navigate to the web page you want to test
    time.sleep(2)

    print("--= Beginning Tests =--")

    # Resize the browser window to a smaller width
    driver.set_window_size(480, 800)
    time.sleep(2)  # Wait for the resize to take effect

    # Check if the hamburger menu is present
    try:
        hamburger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
        print("Hamburger menu is present.")
    except:
        print("Hamburger menu is not present.")

# Close the browser
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


    # Locate the navigation bar using a CSS selector
    nav_bar = driver.find_element(By.CSS_SELECTOR, "nav")  # Replace "nav" with the actual selector of your nav bar

    # Verify if the nav bar exists
    if nav_bar:
        print("[PASSED] - Navigation bar exists.")
    else:
        print("[FAILED] - Navigation bar not found.")


    taggle = driver.find_element(By.CSS_SELECTOR, "a[class= 'navbar-brand'][href = '/']")
    if taggle:
        print("[PASSED] - Exists.")
    else:
        print("[FAILED] - not found.")
   
except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    driver.quit()
