from selenium.webdriver.common.by import By
from selenium_recaptcha_solver import RecaptchaSolver, RecaptchaException

from src.factory import WebDriverFactory
from src.infraestructure import DriverWebEnum, ERRORS, ErrorCode
from src.infraestructure.config import Config

class ScrapperGateway:
    def process(self, config: Config):
        
        driver_factory=WebDriverFactory(config.get("default_web_browser"))
        driver=driver_factory.build(config=config)
        try:
        
            solver = RecaptchaSolver(driver=driver)

            driver.get('https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php')

            recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
            
            input_email= driver.find_element(By.XPATH, '//*[@name="ex-a"]')
            email=input_email.get_attribute("value")
            
            input_color= driver.find_element(By.XPATH, '//*[@name="ex-b"]')
            color=input_color.get_attribute("value")

            solver.click_recaptcha_v2(iframe=recaptcha_iframe)
            
            driver.implicitly_wait(3)
            return {"message":"success","email": email, "color": color}
        except RecaptchaException:
            raise ERRORS[ErrorCode.E002]
        except Exception:
            raise ERRORS[ErrorCode.E001]
    
    
# pip install ffmpeg-downloader
# ffdl install --add-path