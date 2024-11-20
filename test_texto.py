from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeDriverManager

# Função para inicializar o driver
def init_driver():
    service = Service(EdgeDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver
def test_verificar_texto():
    print("Iniciando o teste de texto...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    try:
        # Localiza o texto esperado
        texto_elemento = driver.find_element(By.CSS_SELECTOR, ".main-title").text
        print(f"Texto encontrado: {texto_elemento}")
        assert "PrestaShop" in texto_elemento, f"O texto está incorreto: {texto_elemento}"
        print("Teste de texto passou!")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_verificar_texto()
