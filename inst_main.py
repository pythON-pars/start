from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def face_book(login=None, password=None):

    PATH = r'chromedriver.exe'

    driver = webdriver.Chrome(PATH)
    driver.get('https://www.tiktok.com/')

    sleep(6)
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/button').click()

        sleep(2)

        iframe = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/iframe')
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/a').click()
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[4]/div[2]').click()

        driver.switch_to.window(driver.window_handles[1])

        sleep(5)

        gistr_log = driver.find_element_by_xpath('//*[@id="email"]')
        gistr_log.send_keys(login)

        gistr_password = driver.find_element_by_xpath('//*[@id="pass"]')
        gistr_password.send_keys(password)
        gistr_password.send_keys(Keys.ENTER)
        sleep(20)
    except:
        print('Error element or user [INFO]400')

        driver.close()
        driver.quit()

    print('Регистрация прошла успешно!')

def vk(login=None, password=None):

    PATH = r'chromedriver.exe'

    driver = webdriver.Chrome(PATH)
    driver.get('https://www.tiktok.com/')

    sleep(6)
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/button').click()

        sleep(2)

        iframe = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/iframe')
        driver.switch_to.frame(iframe)

        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/a').click()

        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]').click()

        driver.switch_to.window(driver.window_handles[1])

        sleep(5)

        gistr_log = driver.find_element_by_xpath('//*[@id="login_submit"]/div/div/input[6]')
        gistr_log.send_keys(login)

        gistr_password = driver.find_element_by_xpath('//*[@id="login_submit"]/div/div/input[7]')
        gistr_password.send_keys(password)
        gistr_password.send_keys(Keys.ENTER)
        sleep(20)
    except:
        print('Error element or user [INFO]400')

        driver.close()
        driver.quit()

    print('Регистрация прошла успешно!')

def main():

    chak = input('Как будем проходить регитср?\n1.VK\n2.facebook\nНажмите просто цифру!\n----->')

    try:
        if chak == '2':
            log = input('Login: ')
            pas = input('Password: ')

            face_book(login=log, password=pas)

        elif chak == '1':
            log = input('Login: ')
            pas = input('Password: ')

            vk(login=log, password=pas)
    except:
        print('Error [INFO]--> USER!')
        main()

if __name__ == '__main__':
    main()
