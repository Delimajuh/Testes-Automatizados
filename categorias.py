from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para inicializar o driver do Edge
def init_driver():
    # Caminho para o msedgedriver.exe
    service = Service('C:/Users/Juliana/Desktop/edgedriver_win64/msedgedriver.exe')  
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)  # Aguarda até 60 segundos para o carregamento da página
    return driver

# Função para testar a navegação para a categoria "Women"
def test_navegacao_categorias():
    print("Iniciando o teste de navegação de categorias...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    try:
        # Aguarda até que o link da categoria "Women" esteja visível
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Women"))
        )
        
        # Encontra o link da categoria "Women" e clica nele
        categoria = driver.find_element(By.LINK_TEXT, "Women")
        categoria.click()

        # Aguarda até que a página da categoria "Women" tenha sido carregada
        WebDriverWait(driver, 10).until(
            EC.title_contains("Women")  
        )
        
        # Verifica se o título da página contém "Women" (confirma a navegação correta)
        assert "Women" in driver.title, "Navegação para a categoria falhou"
        print("Teste de navegação de categorias passou!")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

# Executa o teste
if __name__ == "__main__":
    test_navegacao_categorias()
