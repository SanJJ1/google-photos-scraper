from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import shelve

class Google:

    def __init__(self):
        self.browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
        with open('keys.txt') as f:
            user, pw = f.readlines()
        self.google_login(user, pw)

    def google_login(self, user, pw):
        self.browser.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.browser.find_element_by_xpath('//input[@type="email"]').send_keys(user)
        try:
            self.browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
        except:
            pass
        sleep(1)
        self.browser.find_element_by_xpath('//input[@type="password"]').send_keys(pw)
        self.browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)

    def photos_script(self):
        data = []
        self.browser.get('https://photos.google.com')
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/c-wiz/div[3]/c-wiz/div/c-wiz/div/div[1]/div[2]/div[1]/div[2]/a/div').click()
        arrow = self.browser.find_element_by_xpath('/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/c-wiz[3]/div[2]/div[2]')

        info = self.browser.find_element_by_xpath('/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/c-wiz[2]/div[2]/span/div/div[7]/button')
        info.click()
        sleep(2)
        while True:
            try:
                link = []
                link.append(self.browser.current_url)
                print(self.browser.current_url)
                sleep(.5)
                try:
                    filename = self.browser.find_element_by_xpath('/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div')
                    link.append(filename.get_attribute('innerText'))
                    print(filename.get_attribute('innerText'))
                except:
                    try:
                        filename = self.browser.find_element_by_xpath(
                            '/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[1]/div')
                        link.append(filename.get_attribute('innerText'))
                        print(filename.get_attribute('innerText'))
                    except:
                        link.append("wasn't able to find filename")
                        print("wasn't able to find filename")

                hover = ActionChains(self.browser).move_to_element(arrow)
                hover.perform()
                arrow.click()
                data.append(link)
            except:
                break

        with shelve.open('data') as db:
            db['links'] = data

    def quit(self):
        self.browser.quit()


google = Google()
google.photos_script()
input("pause: ")
print("resume")
google.quit()

"""
/html/body/div[1]/div/c-wiz/div[3]/c-wiz/div/c-wiz/div/div[1]/div[2]/div[9]/div[2]/a/div
/html/body/div[1]/div/c-wiz/div[3]/c-wiz[1]/div/c-wiz/div/div[1]/div[3]/div/div[2]/a/div

/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div/div[3]/dl/div[2]
/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[1]/div/div[3]/dl/div[2]
/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div/div[3]/dl/div[2]
/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div/div[3]/dl/div[2]
/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div/div[3]/dl/div[2]
/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div/div[3]/dl/div[2]

"""
