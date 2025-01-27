from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_chromedriver():
    try:
        # Set up ChromeDriver service
        service = Service("D:/Java script/chromedriver/chromedriver.exe")  # Update the path to your ChromeDriver
        driver = webdriver.Chrome(service=service)

        # Open a webpage (Google)
        driver.get("https://www.google.com")
        print("Google opened successfully!")

        # Close the browser
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_chromedriver()
