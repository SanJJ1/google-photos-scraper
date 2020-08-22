from selenium import webdriver
from time import sleep


class Google:

    def __init__(self):
        self.browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
        with open('keys.txt') as f:
            user, pw = f.readlines()
        self.google_login(user, pw)

    def google_login(self, user, pw):
        self.browser.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(3)
        self.browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.browser.find_element_by_xpath('//input[@type="email"]').send_keys(user)
        try:
            self.browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
        except:
            pass
        sleep(3)
        self.browser.find_element_by_xpath('//input[@type="password"]').send_keys(pw)
        self.browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)

    def photos_script(self):
        self.browser.get('https://photos.google.com')
        sleep(5)

    def quit(self):
        self.browser.quit()


google = Google()
google.photos_script()
google.quit()
