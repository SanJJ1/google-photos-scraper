from selenium import webdriver
from time import sleep


class Google:

    def __init__(self, user, pw):
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
        self.google_login(user, pw)

    def google_login(self, user, pw):
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)

    def photos_script(self):
        self.driver.get('https://photos.google.com')
        sleep(5)


username = '21janardhansanjay@gmail.com'
password = 'lisztchopinrachmaninoff'
browse = Google(username, password)

input("pause:   ")
print("resumed")

browse.photos_script()
