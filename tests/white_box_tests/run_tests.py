from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
# chrome_options.add_argument("--headless")  


def login():
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
  driver.get("http://localhost:8080/login")
  sleep(3)
  email_input =  driver.find_element_by_id('exampleInputEmail1')
  pass_input = driver.find_element_by_id('exampleInputPassword1')
  login_btn = driver.find_element_by_id('login-btn')


  email_input.send_keys('deneme@hotmail.com')
  pass_input.send_keys('deneme123')

  sleep(1)
  login_btn.click()

  sleep(3)
  success_page = "http://localhost:8080/"
  
  print(driver.current_url)
  if(driver.current_url == success_page):
    print('Login Testi Basarili')
  else:
    print('Login Testi Basarisiz :(')

  driver.close()


def register():
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

  driver.get("http://localhost:8080/login")

  sleep(2)

  register_btn = driver.find_element_by_id('register-btn')

  sleep(1)

  register_btn.click()

  sleep(3)
  name_input = driver.find_element_by_id('name')
  last_name_input = driver.find_element_by_id('last-name')
  email_input = driver.find_element_by_id('exampleInputEmail')
  password_input_1 = driver.find_element_by_id('exampleInputPassword1')
  password_input_2 = driver.find_element_by_id('exampleInputPassword2')
  submit_btn = driver.find_element_by_id('submit-btn')

  name_input.send_keys('umut')
  last_name_input.send_keys('bozdaG')
  email_input.send_keys('hello@hotmail.com')
  password_input_1.send_keys('deneme123')
  password_input_2.send_keys('deneme123')

  sleep(1)
  submit_btn.click()
  

# login()
register()
