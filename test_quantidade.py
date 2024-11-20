from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

def init_driver():
    service = Service(executable_path="C:\\Users\\Juliana\\Desktop\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)
    return driver

def test_quantidade_carrinho():
    print("Iniciando o teste de quantidade de produtos no carrinho...")
    driver = init_driver()
    
    try:
        driver.get("https://demo.prestashop.com/#/en/front")
        
        # Adiciona um produto ao carrinho
        produto = driver.find_element(By.CSS_SELECTOR, ".product-miniature")
        produto.click()
        botao_carrinho = driver.find_element(By.CSS_SELECTOR, "button.add-to-cart")
        botao_carrinho.click()
        
        # Verifica a quantidade no carrinho
        carrinho = driver.find_element(By.CSS_SELECTOR, ".shopping_cart")
        quantidade = carrinho.text
        assert "1" in quantidade, "Quantidade de produtos no carrinho está incorreta"
        
        print(f"Quantidade no carrinho: {quantidade}")
        print("Teste de quantidade no carrinho passou!")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_quantidade_carrinho()
