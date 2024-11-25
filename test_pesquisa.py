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
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver

# Teste de pesquisa funcional
def test_pesquisa_funcional():
    """
    Realiza o teste de pesquisa no site demo do PrestaShop.
    """
    print("Iniciando o teste de pesquisa...")
    driver = init_driver()
    
    try:
        # Acessa o site
        driver.get("https://demo.prestashop.com/#/en/front")
        
        # Aguarda e muda para o iframe onde o conteúdo está carregado
        WebDriverWait(driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#framelive"))
        )
        print("Mudança para o iframe realizada com sucesso.")

        # Localiza a barra de pesquisa
        barra_pesquisa = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='s']"))
        )
        print("Barra de pesquisa localizada.")
        
        # Envia a pesquisa por "dress"
        barra_pesquisa.send_keys("dress")
        barra_pesquisa.submit()

        # Verifica se os resultados aparecem
        resultados = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title"))
        )
        print(f"Teste passou! Resultados encontrados: {resultados.text}")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_pesquisa_funcional()
