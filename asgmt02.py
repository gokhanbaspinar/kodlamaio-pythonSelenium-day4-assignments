from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_Sauce:
    
    def testEmptyLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)

        loginBtn.click()
        errorMessage = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"

        print(f"RESULT: {testResult}")
    
    def testEmptyPassword(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("q")
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)

        loginBtn.click()
        errorMessage = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"

        print(f"RESULT: {testResult}")

    def lockedOutUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)

        loginBtn.click()
        errorMessage = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

        print(f"RESULT: {testResult}")

    def errorButton(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        cancelBtn = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        cancelBtn.click()

        print("Error button closed.")

    def enterInventoryPage(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(3)

        inventoryList = driver.find_elements(By.CLASS_NAME, "inventory_item")

        print(f"There are {len(inventoryList)} items in list")


testClass = Test_Sauce()

testClass.testEmptyLogin()
testClass.testEmptyPassword()
testClass.lockedOutUser()
testClass.errorButton()
testClass.enterInventoryPage()