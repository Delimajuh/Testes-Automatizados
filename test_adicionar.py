from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Substituição correta

# Função para inicializar o driver
def init_driver():
    """
    Inicializa o driver do Edge usando o WebDriver Manager.
    """
    service = Service(EdgeChromiumDriverManager().install()) 
    driver = webdriver.Edge(service=service)
    return driver

# Função de teste
def test_adicionar_item():
    """
    Função de teste para adicionar um item no site de demonstração do PrestaShop.
    """
    print("Iniciando o teste de adicionar item...")
    driver = init_driver()

    try:
        # Acessa o site
        driver.get("https://demo.prestashop.com/#/en/front")
        print("Site carregado.")


        botao_adicionar = driver.find_element("xpath", "//button[@class='add-to-cart']")
        botao_adicionar.click()
        print("Item adicionado ao carrinho!")

    
        mensagem_sucesso = driver.find_element("xpath", "//div[@class='alert-success']")
        assert "Item added" in mensagem_sucesso.text, "Falha ao adicionar o item."
        print("Teste concluído com sucesso!")

    except Exception as e:
        print(f"Erro durante o teste: {e}")

    finally:
        # Fecha o navegador
        driver.quit()
        print("Navegador fechado. Teste finalizado.")

# Executa o teste
if __name__ == "__main__":
    test_adicionar_item()
