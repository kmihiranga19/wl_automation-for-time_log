from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://worklenz.com/auth")
driver.maximize_window()

faker = Faker()


def main():
    login()
    go_to_project_tab()


def login():
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Email']"))).send_keys(
        "coyonic318@hupoi.com")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))).send_keys(
        "Test@12345")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()
    time.sleep(5)


def go_to_project_tab():
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Projects']"))).click()
    time.sleep(10)


def team_select():
    header = driver.find_element(By.TAG_NAME, "worklenz-header")
    header_div = header.find_elements(By.TAG_NAME, "div")[1]
    header_ul = header_div.find_elements(By.TAG_NAME, "ul")[1]
    team_selection = header_ul.find_elements(By.TAG_NAME, "li")[0]
    team_selection.click()
    time.sleep(2)
    ul = driver.find_element(By.CLASS_NAME, "p-0")
    team = ul.find_elements(By.TAG_NAME, "li")[-1]
    team.click()
    time.sleep(2)


def select_page_counter():
    pagination = driver.find_element(By.TAG_NAME, "nz-pagination")
    page_drop_down = pagination.find_elements(By.TAG_NAME, "li")[-1]
    page_drop_down.click()
    time.sleep(2)
    page_count = driver.find_elements(By.TAG_NAME, "nz-option-item")[2]
    page_count.click()
    time.sleep(2)


def enter_time_log():
    hour = faker.random_int(min=0, max=9)
    minutes = faker.random_int(min=0, max=60)
    seconds = faker.random_int(min=0, max=100)
    t_body = driver.find_element(By.TAG_NAME, "tbody")
    rows = t_body.find_elements(By.TAG_NAME, "tr")
    for index in range(len(rows)):
        t_body = driver.find_element(By.TAG_NAME, "tbody")
        rows = t_body.find_elements(By.TAG_NAME, "tr")
        rows[index].click()
        time.sleep(3)
        tasks = driver.find_element(By.CLASS_NAME, "task-name-text")
        tasks.click()
        time.sleep(1)
        task_inner = driver.find_element(By.CLASS_NAME, "inner-task-name-container")
        task_open = task_inner.find_element(By.TAG_NAME, "button")
        task_open.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[contains(text(),'Time Log')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Add Timelog']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Hours']").send_keys(hour)
        driver.find_element(By.XPATH, "//input[@placeholder='Minutes']").send_keys(minutes)
        driver.find_element(By.XPATH, "//input[@placeholder='Seconds']").send_keys(seconds)
        driver.find_element(By.XPATH, "//span[normalize-space()='Log time']").click()
        time.sleep(2)
        driver.get("https://uat.worklenz.com/worklenz/projects")
        time.sleep(5)
        select_page_counter()
        time.sleep(3)

    pagination = driver.find_element(By.TAG_NAME, "nz-pagination")
    next_btn = pagination.find_element(By.CLASS_NAME, "ant-pagination-next")
    button = next_btn.find_element(By.TAG_NAME, "button")
    if button.is_enabled():
        next_btn.click()
        time.sleep(5)
        enter_time_log()

    return


main()
team_select()
select_page_counter()
enter_time_log()
