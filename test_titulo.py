from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    service = Service(executable_path="C:\\Users\\Juliana\\Desktop\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    return driver

def test_verificar_titulo():
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")  

    try:
        WebDriverWait(driver, 10).until(EC.title_is("Título esperado"))
        assert driver.title == "Título esperado", "O título da página está incorreto"
        print("Teste passou! O título está correto.")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()


test_verificar_titulo()
