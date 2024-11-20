from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Inicializa o driver
def init_driver():
    # Caminho do driver do Edge (ajuste o caminho conforme necessário)
    service = Service(executable_path='C:/Users/Juliana/Desktop/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)  # Aguarda até 60 segundos pelo carregamento
    return driver

# Função para realizar o teste de adicionar ao carrinho
def test_adicionar_ao_carrinho():
    print("Iniciando o teste de adicionar ao carrinho...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")

    try:
        # Espera até que o primeiro produto esteja visível na página
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-miniature"))
        )
        
        # Encontra o primeiro produto e clica nele
        produto = driver.find_element(By.CSS_SELECTOR, ".product-miniature")
        produto.click()
        
        # Espera até o botão "Adicionar ao carrinho" estar visível e clica nele
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        botao_carrinho = driver.find_element(By.CSS_SELECTOR, "button.add-to-cart")
        botao_carrinho.click()
        
        # Espera pela mensagem de sucesso de adição ao carrinho
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-dialog .modal-body"))
        )
        mensagem_sucesso = driver.find_element(By.CSS_SELECTOR, ".modal-dialog .modal-body")
        
        # Verifica se a mensagem de sucesso contém "Product successfully added"
        assert "Product successfully added" in mensagem_sucesso.text, "Produto não foi adicionado ao carrinho"
        
        print("Teste de adicionar ao carrinho passou!")
        
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

# Executa o teste
if __name__ == "__main__":
    test_adicionar_ao_carrinho()
