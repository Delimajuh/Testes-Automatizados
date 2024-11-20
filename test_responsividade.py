from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeDriverManager

# Função para inicializar o driver
def init_driver():
    service = Service(EdgeDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver
# Função para testar a responsividade do site
def test_responsividade():
    print("Iniciando o teste de responsividade...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    # Espera até que o corpo da página seja carregado
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Define uma lista de resoluções para testar
    tamanhos = [(1920, 1080), (768, 1024), (375, 667)]
    
    for largura, altura in tamanhos:
        driver.set_window_size(largura, altura)
        print(f"Testando com resolução {largura}x{altura}")
        
        # Espera o carregamento da página após o ajuste da resolução
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        try:
            # Verifica se o corpo da página está visível
            assert driver.find_element(By.TAG_NAME, "body").is_displayed(), "Site não responsivo"
            print(f"Resolução {largura}x{altura} passou!")
        except Exception as e:
            print(f"Erro na resolução {largura}x{altura}: {e}")
    
    print("Teste de responsividade passou!")
    driver.quit()

# Executa o teste
if __name__ == "__main__":
    test_responsividade()
