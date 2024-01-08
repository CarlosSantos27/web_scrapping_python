import os
from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.infraestructure import ErrorCode, ERRORS, DriverWebEnum, Config


class WebDriverFactory:
    def __init__(self, browser):
        self.__browser= browser
        
    def browser(self)->str:
        return self.__browser
    
    def build(self, config:Config)-> webdriver:
        test_driver = self.__chooise_browser(config=config)
        return test_driver
    
    def __buildChromeOptions(self)-> ChromeOptions:
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        options = self.__buildGeneralOptions(ChromeOptions())
        
        # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)

        options.add_argument('--user-agent={ua}')
        return options
    
    def __buildFirefoxOptions(self)-> FirefoxOptions:
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        options = self.__buildGeneralOptions(FirefoxOptions())
        options.headless = True
        options.set_preference("general.useragent.override", ua)
        return options
    
    def __buildGeneralOptions(self, options: ArgOptions)->ArgOptions:
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        return options
    
    def __chooise_browser(self, config:Config):
        path_driver=os.getcwd()+"/files"
        match self.__browser:
            case DriverWebEnum.CHROME:
                path=path_driver + "/chromedriver/" + config.get("web_driver")
                return webdriver.Chrome(executable_path=path, options=self.__buildChromeOptions())
            case DriverWebEnum.FIREFOX:
                path_driver='{path_driver}/geckodriver/' + config.get("web_driver")
                return webdriver.Firefox(executable_path=path_driver, options=self.__buildFirefoxOptions())
            case _:
                raise ERRORS[ErrorCode.E003]