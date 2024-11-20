from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    # Caminho para o msedgedriver.exe
    service = Service(executable_path="C:\\Users\\Juliana\\Desktop\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    return driver

def test_footer_informacoes():
    print("Iniciando o teste de footer...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    try:
        # Espera até 10 segundos até o footer ficar visível
        footer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer"))
        )
        assert footer.is_displayed(), "Footer não está visível"
        print("Footer visível com sucesso!")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

# Executando o teste
test_footer_informacoes()
