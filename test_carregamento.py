from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Função para inicializar o driver do Edge
def init_driver():
    service = Service(executable_path="C:\\Users\\Juliana\\Desktop\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(60)  # Aguarda até 60 segundos para o carregamento da página
    return driver

def test_tempo_carregamento():
    print("Iniciando o teste de tempo de carregamento...")
    driver = init_driver()
    
    # Registra o início do carregamento
    inicio = time.time()
    
    # Acessa o site
    driver.get("https://demo.prestashop.com/#/en/front")
    
    # Espera o corpo da página ser carregado completamente (ajuste se necessário)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Registra o tempo após o carregamento
    fim = time.time()
    
    # Calcula o tempo de carregamento
    tempo_carregamento = fim - inicio
    
    # Verifica se o tempo de carregamento é abaixo do limite de 10 segundos
    assert tempo_carregamento < 10, f"Tempo de carregamento muito alto: {tempo_carregamento} segundos"
    print(f"Teste de tempo de carregamento passou: {tempo_carregamento} segundos")
    
    driver.quit()

# Executa o teste
if __name__ == "__main__":
    test_tempo_carregamento()
