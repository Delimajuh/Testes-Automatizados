from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Função para testar a navegação em categorias
def test_navegacao_categorias():
    """
    Teste para verificar a navegação para a categoria 'Women' no site do PrestaShop Demo.
    """
    print("Iniciando o teste de navegação de categorias...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")

    try:
        # Espera até que o iframe do demo seja carregado e muda para o contexto do iframe
        WebDriverWait(driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#framelive"))
        )
        print("Mudança para o iframe bem-sucedida.")

        # Aguarda até que o link da categoria "Women" esteja visível
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Women"))
        )
        categoria = driver.find_element(By.LINK_TEXT, "Women")
        categoria.click()

        # Aguarda até que o título da página contenha "Women"
        WebDriverWait(driver, 15).until(
            EC.title_contains("Women")
        )
        
        # Valida que o título contém a categoria esperada
        assert "Women" in driver.title, "Navegação para a categoria 'Women' falhou"
        print("Teste de navegação de categorias passou!")

    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_navegacao_categorias()
