from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium driver
driver = webdriver.Chrome()
url ="https://www.amazon.jobs/content/en/career-programs/university"
driver.get(url)

time.sleep(2)  # Wait for the page to load

    # Scroll to load all reviews or click 'load more' if necessary
scroll_pause = 2  # Adjust based on site behavior
for _ in range(5):  # Adjust scroll count as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)

    # Extract HTML and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
Job_titles = soup.find_all("a", {"class": "header-module_mobile__Nl1un header-module_title__9-W3R"})  # Modify selector based on page

    # Close the driver

driver.quit()
print(Job_titles)
for jobs in Job_titles:
    print(jobs.text)
