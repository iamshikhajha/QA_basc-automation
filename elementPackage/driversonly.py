from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class drivers:
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    url ="https://students.bishalkarki.com.np"
