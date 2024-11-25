from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Substituição correta

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

def test_tempo_carregamento():
    """
    Testa o tempo de carregamento da página do PrestaShop Demo.
    """
    print("Iniciando o teste de tempo de carregamento...")
    driver = init_driver()

    try:
        # Registra o início do carregamento
        inicio = time.time()
        
        # Acessa o site
        driver.get("https://demo.prestashop.com/#/en/front")
        
        # Espera o corpo da página ser carregado completamente
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Registra o tempo após o carregamento
        fim = time.time()
        
        # Calcula o tempo de carregamento
        tempo_carregamento = fim - inicio
        
        # Verifica se o tempo de carregamento é abaixo do limite de 10 segundos
        assert tempo_carregamento < 10, f"Tempo de carregamento muito alto: {tempo_carregamento:.2f} segundos"
        print(f"Teste de tempo de carregamento passou: {tempo_carregamento:.2f} segundos")

    except AssertionError as ae:
        print(f"Falha no teste: {ae}")
    except Exception as e:
        print(f"Erro durante o teste: {e}")
    finally:
        # Fecha o navegador
        driver.quit()
        print("Navegador fechado. Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_tempo_carregamento()
