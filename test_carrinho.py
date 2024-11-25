from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Correção do import

# Função para inicializar o driver
def init_driver():
    """
    Inicializa o driver do Edge usando o WebDriver Manager.
    """
    try:
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("Driver inicializado com sucesso!")
        return driver
    except Exception as e:
        print(f"Erro ao inicializar o driver: {e}")
        raise

# Função para realizar o teste de adicionar ao carrinho
def test_adicionar_ao_carrinho():
    """
    Teste para verificar a funcionalidade de adicionar produtos ao carrinho no PrestaShop Demo.
    """
    print("Iniciando o teste de adicionar ao carrinho...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")

    try:
        # Espera até que o iframe do demo seja carregado e mude o contexto para ele
        WebDriverWait(driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#framelive"))
        )
        print("Mudança para o iframe bem-sucedida.")

        # Espera até que o primeiro produto esteja visível na página
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-miniature"))
        )
        produto = driver.find_element(By.CSS_SELECTOR, ".product-miniature")
        produto.click()

        # Espera até o botão "Adicionar ao carrinho" estar visível e clica nele
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        botao_carrinho = driver.find_element(By.CSS_SELECTOR, "button.add-to-cart")
        botao_carrinho.click()

        # Espera pela mensagem de sucesso de adição ao carrinho
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-dialog .modal-body"))
        )
        mensagem_sucesso = driver.find_element(By.CSS_SELECTOR, ".modal-dialog .modal-body")

        # Verifica se a mensagem de sucesso contém "Product successfully added"
        assert "Product successfully added" in mensagem_sucesso.text, "Produto não foi adicionado ao carrinho"
        print("Teste de adicionar ao carrinho passou!")

    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_adicionar_ao_carrinho()
