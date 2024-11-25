from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Função para inicializar o driver
def init_driver():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver

# Teste de navegação e pesquisa funcional
def test_pesquisa_funcional():
    print("Iniciando o teste de pesquisa e navegação...")
    driver = init_driver()
    try:
        # Acessa a página
        driver.get("https://legit-approval.demo.prestashop.com/en")
        
        # Interagir com o menu
        menu_clothes = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "category-3"))
        )
        menu_clothes.click()  # Clica no item "Clothes"
        
        # Espera o submenu aparecer
        submenu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "top_sub_menu_68733"))
        )
        
        # Ações no submenu 
        submenu_men = driver.find_element(By.ID, "category-4")
        submenu_men.click()
        
        # Aguarda a página carregar
        WebDriverWait(driver, 10).until(
            EC.title_contains("Men")  # Verifica se a página de "Men" carregou
        )

        # Pesquisa
        barra_pesquisa = driver.find_element(By.CSS_SELECTOR, "input[name='s'][aria-label='Search']")
        barra_pesquisa.send_keys("dress")  # Realiza a pesquisa
        barra_pesquisa.submit()

        # Verifica se o resultado da pesquisa aparece
        resultados = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title"))
        )
        print(f"Teste passou! Resultados encontrados: {resultados.text}")
    except Exception as e:
        print(f"Teste falhou: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_pesquisa_funcional()
