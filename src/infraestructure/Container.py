from lagom import Container
from src.gateway import ScrapperGateway
from src.services import ScrapperService
from configparser import ConfigParser
from src.infraestructure.config import Config


config = ConfigParser()
config.read('config.ini')
configInstance=Config(config=config)

container=Container()

container[Config]= configInstance
container[ScrapperGateway]= ScrapperGateway()
container[ScrapperService]= ScrapperService(ScrapperGateway,config=configInstance)