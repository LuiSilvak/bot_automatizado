from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def configurar_driver(caminho_driver):
   # Configura o serviço do ChromeDriver
    service = Service(caminho_driver)

    # Inicializa o driver usando o serviço configurado
    driver = webdriver.Chrome(service=service)
    return driver

def acessar_site(driver, url):
    """Acessa o site fornecido."""
    driver.get(url)
    print(f"Acessando o site: {url}")
    time.sleep(2)   # Ajuste conforme necessário

def interagir_com_elementos(driver):
    """Interage com elementos do site."""
    try:
        # Exemplo de interação: clique em um botão
        ### button = driver.find_element(By.ID, "id_do_botao")
        ### button.click()

        # Exemplo de preenchimento de campo
        ### input_field = driver.find_element(By.NAME, "nome_do_campo")
        ### input_field.send_keys("texto_a_inserir")
        ### input_field.send_keys(Keys.RETURN)

        print("Interação concluída com sucesso!")
    except Exception as e:
        print(f"Erro durante a interação: {e}")

def fechar_driver(driver):
    """Fecha o WebDriver."""
    print("Fechando o navegador...")
    driver.quit()

def main():
    caminho_driver = "./chromedriver.exe"
    url = "https://escex.tcema.tc.br/site/"

    # Configurar o WebDriver
    driver = configurar_driver(caminho_driver)

    try:
        # Acessar o site
        acessar_site(driver, url)

        # Interagir com elementos (se necessário)
        interagir_com_elementos(driver)

    finally:
        # Fechar o WebDriver
        fechar_driver(driver)

if __name__ == "__main__":
    main()