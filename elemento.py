from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def init_driver():
    service = Service('C:/Users/Juliana/Desktop/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    return driver

def test_verificar_elemento():
    print("Iniciando o teste de elemento...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    try:
        # Verifica se o elemento está presente na página
        elemento = driver.find_element(By.CSS_SELECTOR, ".main-title")
        print(f"Elemento encontrado: {elemento.text}")
        assert elemento.is_displayed(), "O elemento não está visível na página"
        print("Teste de elemento passou!")
    except NoSuchElementException:
        print("Teste falhou: Elemento não encontrado!")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_verificar_elemento()
