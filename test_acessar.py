from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeDriverManager

# Função para inicializar o driver
def init_driver():
    service = Service(EdgeDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver

# Função de teste
def test_acessar_site():
    print("Iniciando o teste...")  
    driver = init_driver()
    
    driver.get("https://demo.prestashop.com/#/en/front")
    print(f"Site carregado: {driver.current_url}")  # Imprime a URL carregada no terminal
    
    # Verificando se o site foi carregado corretamente
    assert driver.current_url == "https://demo.prestashop.com/#/en/front", "O site não foi carregado corretamente"
    
    print("Site carregado corretamente!") 

    driver.quit()
    print("Teste concluído!") 

test_acessar_site()
