from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Função para inicializar o driver do Edge
def init_driver():
    service = Service('C:/Users/Juliana/Desktop/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)  # Aguarda até 60 segundos para o carregamento da página
    return driver

def test_validacao_preco():
    print("Iniciando o teste de validação de preço do produto...")

    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")

    try:
        # Localiza os produtos
        produtos = driver.find_elements(By.CSS_SELECTOR, ".product-miniature, .js-product-miniature")

        # Itera sobre cada produto encontrado
        for produto in produtos:
            # Obtém o nome do produto
            nome_produto = produto.find_element(By.CSS_SELECTOR, ".product-title").text
            print(f"Produto encontrado: {nome_produto}")

            # Obtém o preço regular e o preço com desconto
            preco_regular = produto.find_element(By.CSS_SELECTOR, ".regular-price").text
            preco_desconto = produto.find_element(By.CSS_SELECTOR, ".price").text
            print(f"Preço regular: {preco_regular} | Preço com desconto: {preco_desconto}")

            # Verifica se o preço com desconto está presente e se o desconto é menor que o preço regular
            if preco_desconto and preco_regular:
                preco_regular_num = float(preco_regular.replace('€', '').replace(',', '.'))
                preco_desconto_num = float(preco_desconto.replace('€', '').replace(',', '.'))
                
                assert preco_desconto_num < preco_regular_num, f"O preço com desconto ({preco_desconto}) é maior que o preço regular ({preco_regular})"

        print("Teste de validação de preço passou!")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

test_validacao_preco()