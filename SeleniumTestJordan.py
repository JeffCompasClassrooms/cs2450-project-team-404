from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://localhost:5000/loginscreen")
    time.sleep(2)

    print("Beginning Tests - Jordan Coleman")
    #login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    form = driver.find_element(By.CSS_SELECTOR, 'form[class="form"][method="post"]')

    form_type = form.get_attribute("action")

    print(form_type)


    button = driver.find_element(By.CSS_SELECTOR, 'button[class="button3"]')
    


    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"][type="password"]') #Test 1
    Login = driver.find_element(By.CSS_SELECTOR, 'button[class="button1"]')

    Taggle_login_logo = driver.find_element(By.CSS_SELECTOR, 'p[id="heading"][name="type"]')

    logo_color = Taggle_login_logo.value_of_css_property("color")


    driver.get("http://localhost:5000")

    sign_up = driver.find_element(By.CSS_SELECTOR, 'a[class="btn btn-primary"]')

    driver.get("http://localhost:5000/register")


    register_button = driver.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"][name="type"][value="Register"]')
    color = register_button.value_of_css_property("background-color")


    login_redirect = driver.find_element(By.CSS_SELECTOR, 'a[id="login_link"]')
    href = login_redirect.get_attribute("href")

    confirm = driver.find_element(By.CSS_SELECTOR, 'input[class="form-control"][name="cpassword"]')


    email = driver.find_element(By.CSS_SELECTOR, 'input[class="form-control"][name="email"]')

    email_type = email.get_attribute("type")


    if form_type == "http://localhost:5000/login":
        print("[PASSED] - The Login Page Successfully logs you in")

    else:
        print("[FAILED] - The Loggin Page does not successfully log you in")

    if button:
        print("[PASSED] - There is a forgot password button there")

    else:
        print("[FAILED] - There is not a forgot password button there")

    if password_input: #1
        print("[PASSED] - Password Input Exists.")
    else:
        print("[FAILED] - Password Input not found.")


    if Login: #2
        print("[PASSED] - The Login Button Exists")

    else:
        print("[FAILED] - The Login Button not found")


    if logo_color == "rgba(8, 109, 139, 1)": #3
        print("[PASSED] - Taggle logo on loggin screen correct color")

    else:
        print("[FAILED] - Taggel logo on loggin screen not correct color")

    if sign_up: #4
        print("[PASSED] - A Sign-Up button is there")

    else:
        print("[FAILED] - A Sign-Up button not found")

    if color == "rgba(3, 26, 34, 0.91)": #5
        print("[PASSED] - Register button is the correct color")

    else:
        print("[FAILED] - Register button is not the correct color")

    
    if href == "http://localhost:5000/loginscreen": #6
        print("[PASSED] - 'Login Here!' successfully brings you back to the login screen")

    else:
        print("[FAILED] - 'Login Here!' does not bring you back to the login screen")


    if confirm: #7
        print("[PASSED] - There is a password confirm field")

    else:
        print("[FAILED] - There is not a password confirm field")


    if email_type == "email": #8
        print("[PASSED] - The site takes someones email correctly")
        

    else:
        print("[FAILED] - The site does not take someones email correctly")


except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    driver.quit()