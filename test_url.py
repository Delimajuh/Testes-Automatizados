from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeDriverManager

# Função para inicializar o driver
def init_driver():
    service = Service(EdgeDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver

def test_verificar_url():
    print("Iniciando o teste de URL...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    url_atual = driver.current_url
    print(f"URL atual: {url_atual}")
    assert url_atual.startswith("https://demo.prestashop.com"), f"A URL está incorreta: {url_atual}"
    
    print("Teste de URL passou!")
    driver.quit()

if __name__ == "__main__":
    test_verificar_url()
