from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o driver
def init_driver():
    service = Service('C:/Users/Juliana/Desktop/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)  # Aguarda até 60 segundos pelo carregamento
    return driver

# Teste de pesquisa funcional
def test_pesquisa_funcional():
    print("Iniciando o teste de pesquisa...")
    driver = init_driver() 
    try:
        driver.get("https://demo.prestashop.com/#/en/front")  
        
        barra_pesquisa = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='s'][aria-label='Search']"))
        )
        barra_pesquisa.send_keys("dress")
        barra_pesquisa.submit()

        # Verifica se o resultado da pesquisa aparece
        resultados = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title"))  
        )
        print(f"Teste passou! Resultados encontrados: {resultados.text}")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_pesquisa_funcional()
