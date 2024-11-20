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

def test_navegacao_categorias():
    print("Iniciando o teste de navegação de categorias...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    try:
        # Aguarda até que o link da categoria "Women" esteja visível
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Women"))
        )
        
        categoria = driver.find_element(By.LINK_TEXT, "Women")
        categoria.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Women")  
        )
        
        assert "Women" in driver.title, "Navegação para a categoria falhou"
        print("Teste de navegação de categorias passou!")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

# Executa o teste
if __name__ == "__main__":
    test_navegacao_categorias()
