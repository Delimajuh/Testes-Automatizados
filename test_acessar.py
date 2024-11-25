from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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

def test_acessar_site():
    """
    Função de teste para acessar o site demo do PrestaShop.
    """
    print("Iniciando o teste...")
    driver = init_driver()

    try:
        # Acessa o site
        url = "https://demo.prestashop.com/#/en/front"
        driver.get(url)
        print(f"Site carregado: {driver.current_url}")  # Imprime a URL carregada no terminal

        # Verifica se o site foi carregado corretamente
        assert driver.current_url == url, f"Erro: esperado {url}, mas carregado {driver.current_url}"
        print("Teste concluído com sucesso! Site carregado corretamente.")

    except AssertionError as ae:
        print(f"Falha no teste de validação: {ae}")

    except Exception as e:
        print(f"Erro durante o teste: {e}")

    finally:
        # Fecha o navegador
        driver.quit()
        print("Navegador fechado. Teste finalizado.")

if __name__ == "__main__":
    test_acessar_site()
