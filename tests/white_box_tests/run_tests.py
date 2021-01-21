from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
# chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


def login(without_close):

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

  if(without_close == False):
    if(driver.current_url == success_page):
      print('Login Testi Basarili')
    else:
      print('Login Testi Basarisiz :(')
      driver.close()


def register():

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
  email_input.send_keys('deneme6@hotmail.com')
  password_input_1.send_keys('deneme123')
  password_input_2.send_keys('deneme123')

  sleep(1)
  submit_btn.click()
  sleep(3)
  if(driver.current_url == 'http://localhost:8080/login'):
    print('Register testi Başarısız (Butona basıldığında hata oluştu)')
    driver.close()
  driver.refresh()
  sleep(3)
  columns = driver.find_elements_by_class_name('column')
  sleep(3)
  if(len(columns) > 0):
    print('Register testi Başarılı')
  else:
    print('Register testi Başarısız')
  driver.close()

def add_task():

  login(without_close=True)
  sleep(8)
  add_task_btn = driver.find_element_by_id('add-task-btn')

  add_task_btn.click()
  sleep(1)
  task_name_input = driver.find_element_by_id('task-name-input')
  task_desc_input = driver.find_element_by_id('task-desc-input')
  task_notes_input = driver.find_element_by_id('task-notes-input')
  create_todo_btn = driver.find_element_by_id('create-todo-btn')
  todo_tasks_count_before = len(driver.find_elements_by_class_name('todoTask'))


  task_name_input.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum lorem justo, lobortis in auctor id, ornare eu elit. Pellentesque nec metus dictum, vehicula dui id')
  task_desc_input.send_keys('Phasellus porttitor ultrices mi at bibendum. Sed interdum rutrum orci, sit amet suscipit lectus sollicitudin sit amet.')
  task_notes_input.send_keys('Vivamus at tincidunt elit. Ut dictum, odio a condimentum dapibus, nibh arcu convallis lorem')
  create_todo_btn.click()
  sleep(2)
  if(len(driver.find_elements_by_class_name('todoTask')) > todo_tasks_count_before):
    print('Task başarıyla Todo kolonuna eklenmiştir. add_task testi başarılı')
  else:
    print('add_task testi başarısız')



login(without_close=False)
register()
add_task()