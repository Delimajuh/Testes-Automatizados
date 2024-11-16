from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
import time

# Inicializa o driver
def init_driver():
    service = Service(executable_path='C:/Users/Juliana/Desktop/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)  # Aguarda até 60 segundos pelo carregamento
    return driver

# Função de teste de adicionar produto ao carrinho
def test_adicionar_ao_carrinho():
    print("Iniciando o teste de adicionar produto ao carrinho...")

    driver = init_driver()

    # Acessando o site
    driver.get("https://grand-coil.demo.prestashop.com")

    # Espera para garantir que a página carregou
    time.sleep(3)

    # Navegar até a página do produto específico
    produto_link = driver.find_element(By.CSS_SELECTOR, ".product-miniature a")
    produto_link.click()

    # Espera para garantir que a página do produto carregou
    time.sleep(2)

    # Clicar no botão "Adicionar ao carrinho"
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".add-to-cart")
    add_to_cart_button.click()

    # Espera para garantir que o produto foi adicionado ao carrinho
    time.sleep(2)

    # Verificar se o carrinho foi atualizado
    try:
        # Verificar a quantidade no carrinho
        cart_button = driver.find_element(By.CSS_SELECTOR, ".shopping_cart")
        cart_button.click()
        
        time.sleep(2)

        # Verifica se o produto foi adicionado ao carrinho
        item_in_cart = driver.find_element(By.CSS_SELECTOR, ".cart-items .product-name")
        print(f"Produto adicionado ao carrinho: {item_in_cart.text}")
    except Exception as e:
        print(f"Erro ao verificar carrinho: {e}")

    # Fechar o driver
    driver.quit()

# Executando o teste
test_adicionar_ao_carrinho()
