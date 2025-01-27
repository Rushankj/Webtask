from flask import Flask, request, jsonify
from selenium import webdriver
from flask_cors import CORS
from selenium.webdriver.common.by import By
import time
import os

app = Flask(__name__)
CORS(app)

# Set up the path for ChromeDriver
chromedriver_path = os.path.join(os.getcwd(), "chromedriver", "chromedriver.exe")  # Update for Windows

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url")
    scrape_type = data.get("scrapeType")

    if not url:
        return jsonify({"error": "URL is required"}), 400
    if scrape_type != "commenters":
        return jsonify({"error": "Only 'commenters' scrapeType is supported"}), 400

    try:
        # Setup WebDriver
        driver = webdriver.Chrome(executable_path= " chromedriver/chromedriver.exe " )
        driver.get(url)
        time.sleep(5)  # Wait for page to load

        # Scroll and load comments dynamically
        while True:
            try:
                load_more_button = driver.find_element(By.XPATH, "//button[text()='Load more comments']")
                load_more_button.click()
                time.sleep(2)
            except:
                break  # No more comments to load

        # Extract comments
        comments = []
        comment_elements = driver.find_elements(By.XPATH, "//ul[@role='list']//li/div/div/div/span")
        username_elements = driver.find_elements(By.XPATH, "//ul[@role='list']//li/div/div/div/h3")

        for username, comment in zip(username_elements, comment_elements):
            comments.append({
                "username": username.text.strip(),
                "comment": comment.text.strip()
            })

        driver.quit()
        return jsonify({"results": comments})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
