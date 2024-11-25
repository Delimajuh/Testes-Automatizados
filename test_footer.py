from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager  

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

def test_footer_informacoes():
    """
    Teste para verificar se o footer está visível na página.
    """
    print("Iniciando o teste de footer...")
    driver = init_driver()
    driver.get("https://demo.prestashop.com/#/en/front")
    
    try:
        # Aguarda o carregamento do iframe do demo e muda para ele
        WebDriverWait(driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#framelive"))
        )
        print("Mudança para o iframe bem-sucedida.")
        
        # Aguarda até que o footer esteja visível na página
        footer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer"))
        )
        
        # Verifica se o footer está visível
        assert footer.is_displayed(), "Footer não está visível"
        print("Teste de footer passou: Footer visível com sucesso!")
    
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_footer_informacoes()
