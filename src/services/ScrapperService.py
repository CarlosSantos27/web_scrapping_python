from src.gateway import ScrapperGateway
from src.infraestructure import Config

class ScrapperService:
    def __init__(self,gategay:ScrapperGateway, config:Config):
        self.gateway=gategay
        self.config=config
    
    def process(self):
            return self.gateway.process(self, config=self.config)