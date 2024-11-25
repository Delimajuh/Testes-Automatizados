from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Correção no import

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

# Função para verificar a presença de um elemento na página
def test_verificar_elemento():
    """
    Teste para verificar se um elemento específico está presente e visível na página.
    """
    print("Iniciando o teste de elemento...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")

    try:
        # Espera pelo carregamento 
        WebDriverWait(driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#framelive"))
        )
        print("Mudança para o iframe bem-sucedida.")

        # Verifica se o elemento ".main-title" está presente na página
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".main-title"))
        )
        elemento = driver.find_element(By.CSS_SELECTOR, ".main-title")
        print(f"Elemento encontrado: {elemento.text}")

        # Verifica se o elemento está visível na página
        assert elemento.is_displayed(), "O elemento não está visível na página"
        print("Teste de elemento passou!")

    except NoSuchElementException:
        print("Teste falhou: Elemento não encontrado!")
    except Exception as e:
        print(f"Teste falhou devido a um erro: {e}")
    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_verificar_elemento()
