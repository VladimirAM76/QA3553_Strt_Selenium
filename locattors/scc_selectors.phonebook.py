import time


from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Chrome()

try:
    driver.get("https://telranedu.web.app/login")

    links = driver.find_elements(By.TAG_NAME, "a")
    print(len(links))
    for link in links:
        print(link.text)

    links1 = driver.find_elements(By.CSS_SELECTOR, "a")
    print(len(links1))
    for link in links1:
        print(link.text)

    links = driver.find_elements(By.TAG_NAME, "input")
    print(len(links))
    for link in links:
        print(link.text)

    links1 = driver.find_elements(By.CSS_SELECTOR, "input")
    print(len(links1))
    for link in links1:
        print(link.text)

    button = driver.find_element(By.TAG_NAME, "button")
    button1 = driver.find_element(By.CSS_SELECTOR, "button")

    print(button.tag_name)
    print(button.text)

    print(button1.tag_name)
    print(button1.text)

        # by.class

    #abn_style = driver.find_element(By.CLASS_NAME, "abn_style")
    #abn_style_1 = driver.find_element(By.CSS_SELECTOR, ".abn_style")
    #print("abn_style class: ", abn_style.get_attribute("class"))
    #print("abn_style class: ", abn_style.get_attribute("class"))

    time.sleep(3)

    navbar = driver.find_element(By.CLASS_NAME, "navbar-component_nav__1X_4m")
    navbar_1 = driver.find_element(By.CSS_SELECTOR, ".navbar-component_nav__1X_4m")
    print("navbar class (CLASS_NAME):", navbar.get_attribute("class"))
    print("navbar_1 class (CSS_SELECTOR):", navbar_1.get_attribute("class"))

    div = driver.find_element(By.ID, "root")
    div_1 = driver.find_element(By.CSS_SELECTOR, "#root")

    print("div id: ", div.tag_name)
    print("div id: ", div_1.tag_name)

#driver.close()

finally:
    driver.quit()
