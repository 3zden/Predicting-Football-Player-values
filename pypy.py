pathvv = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # UPDATE THIS

# Set WebDriver options for Brave
options = Options()
options.binary_location = brave_path  # Point to Brave executable
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the driver (use ChromeDriver)
driver = webdriver.Chrome(
    service=Service(),  # Optional: Specify path if chromedriver isn't in PATH
    options=options
)

# Test navigation
driver.get("https://www.google.com")
print(driver.title)
driver.quit()