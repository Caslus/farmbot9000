from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import pyperclip

class User:
    def __init__(self, config):
        self.config = config
        options = Options()
        scriptPath = pathlib.Path().absolute()
        if self.config.getboolean('Browser', 'disableSeleniumLogs'):
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if self.config.getboolean('Browser', 'saveSession'):
            options.add_argument(f'user-data-dir={scriptPath}\\driver\\selenium')
        self.driver = webdriver.Chrome(executable_path=f'{scriptPath}\\driver\\chromedriver.exe', options=options)
        self.login()

    def login(self):
        self.browse = self.driver.get("https://discord.com/login")
    
    def send(self, msg):
        input = self.driver.switch_to.active_element
        if self.config.getboolean('Messages', 'clearInput'):
            input.send_keys(Keys.CONTROL + "a")
            input.send_keys(Keys.DELETE)
        if self.config.getboolean('Messages', 'useMessagePasting'):
            pyperclip.copy(msg)
            input.send_keys(Keys.CONTROL + "v")
        else:
            input.send_keys(msg)
        input.send_keys(Keys.ENTER)