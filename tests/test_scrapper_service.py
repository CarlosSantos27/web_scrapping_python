from src.gateway import ScrapperGateway

def test_scrapper_service():
    instanceScrapper=ScrapperGateway()
    response=instanceScrapper.process()
    print(response)
    pass