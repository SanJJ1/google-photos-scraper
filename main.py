from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import shelve


class Google:

    def __init__(self, headlessness: bool):
        """
        initializes webdriver and browser.
        """
        options = Options()
        options.headless = headlessness
        self.browser = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
        with open('keys.txt') as f:
            user, pw = f.readlines()
        # self.google_login(user, pw)

    def wait_until_load(self, element_wait_for_load):
        """
        Waits until the input WebDriver element is loaded.
        :param element_wait_for_load: a WebDriver that element that
        needs to be loaded in
        :return: None
        """

        def link_has_gone_stale():
            try:
                # poll the link with an arbitrary call
                self.browser.find_element_by_xpath(element_wait_for_load)
                print('loaded')
                return False
            except Exception as e:
                print(e)
                return True

        i = 1
        while link_has_gone_stale():
            i += 1
            print(i)
            sleep(.1)
            pass

    def login(self):
        """
        Logs in to Google using redirect method, meaning that the script logs into StackOverFlow,
        then goes to the google photos site.
        :return: None
        """
        with open('keys.txt') as f:
            user, pw = f.readlines()

        # logs into StackOverFlow
        self.browser.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        self.browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

        # types in username
        self.browser.find_element_by_xpath('//input[@type="email"]').send_keys(user)

        # this try-except shouldn't exist, but for some reason it returns an error
        # after clicking the element. Tldr; it works but still returns an error.
        try:
            self.browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
        except Exception as e:
            print(e)

        sleep(2)

        # types in password
        self.browser.find_element_by_xpath('//input[@type="password"]').send_keys(pw)
        self.browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)

    def get_links(self):
        data = []  # A list where all of the data will be entered
        hover = ActionChains(self.browser)
        self.browser.get('https://photos.google.com')
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/c-wiz/div[3]/c-wiz/div/c-wiz/div/div[1]/div[2]/div[1]/div[2]/a/div').click()
        arrow = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/c-wiz[3]/div[2]/div[2]')

        self.wait_until_load('/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/c-wiz[2]/div[2]/span/div/div[7]/button')
        info = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/c-wiz[2]/div[2]/span/div/div[7]/button')
        hover.move_to_element(info)
        hover.perform()
        info.click()
        sleep(2)
        while True:
            try:
                link = [self.browser.current_url]
                print(self.browser.current_url)
                sleep(1)
                try:
                    filename = self.browser.find_element_by_xpath(
                        '/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/div[2]/c-wiz[2]/div')
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

                hover.move_to_element(arrow)
                hover.perform()
                arrow.click()
                data.append(link)
            except:
                break
        # 'caches' data
        with shelve.open('data') as db:
            db['links2'] = data

    def get_data(self):
        with shelve.open('data') as db:
            links = db['links2']

        tiktoks = []
        for link in links:
            for attrib in link[1].split('\n'):
                if '.mp4' in attrib and len(attrib) == 36:
                    # print(attrib)
                    tiktoks.append(link[0])

        actions = ActionChains(self.browser)
        actions.key_down(Keys.SHIFT).send_keys("d").key_up(Keys.SHIFT)
        for vid in tiktoks:
            self.browser.get(vid)
            sleep(1)
            actions.perform()
            sleep(3)
            trash = '/html/body/div[1]/div/c-wiz/div[4]/c-wiz/div[1]/c-wiz[2]/div[2]/span/div/div[9]'
            self.browser.find_element_by_xpath(trash).click()
            confirm = '/html/body/div[1]/div/div[2]/div/div[2]/div[3]/button[2]'
            self.browser.find_element_by_xpath(confirm).click()

    def quit(self):
        self.browser.quit()


# with shelve.open('data') as db:
#     print(db['links'])

google = Google(headlessness=False)
google.login()
google.get_links()
# google.get_links()
google.quit()
