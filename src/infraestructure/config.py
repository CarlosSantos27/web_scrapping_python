class Config:
    def __init__(self,config):
        self.config=config
        
    def get(self, key):
        return self.config.get("Configuracion",key)