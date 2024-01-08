from configparser import ConfigParser

class Config:
    def __init__(self,config:ConfigParser):
        self.config=config
        
    def get(self, key):
        return self.config.get("Configuracion",key)
    
    def getBoolean(self, key) -> bool:
        return self.config.getboolean("Configuracion", key)