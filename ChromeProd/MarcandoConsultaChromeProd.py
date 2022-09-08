# minhas importacoes
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from win10toast import ToastNotifier
from faker import Faker
fake = Faker('pt_BR')


class Test_marcando_consulta():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                       "C:\\Users\\Juliana.bueno\\Desktop\\TesteMarcandoConsultas\\drivers\\chromedriver.exe")
    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2")
        self.driver.maximize_window()


        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("xxx")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(30)

        # iniciando
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='panel-body flex-column'][contains(.,'Videoconsulta')]")
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body flex-column'][contains(.,'Videoconsulta')]").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body bg-light-2x-pink'][contains(.,'Agendar videoconsulta')]")
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body bg-light-2x-pink'][contains(.,'Agendar videoconsulta')]").click()
        dropdown = self.driver.find_element(By.NAME, "paciente").click()
        dropdown = self.driver.find_element(By.XPATH, "//option[@value='cb7fd5fd-10cb-453f-9e6d-a500d60eeb13']").click()

        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()
        self.driver.find_element(By.ID, "ui-id-1").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        dropdown = self.driver.find_element(By.NAME, "especialidade").click()
        dropdown = self.driver.find_element(By.XPATH, "//option[contains(.,'Clínica médica')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        chekbox = self.driver.find_element(By.NAME, "chkAceite").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()
        print("Consulta marcada")

        # Escolha a data da consulta
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'25')])[1]"))).click()
            print("foi escolhido o dia 25")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'30')])[1]"))).click()
            print("foi escolhido o dia 30")

        # Escolha o horario da consulta
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'08:00')])[12]"))).click()
            print("foi escolhido o horário 08:00")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'16:00')])[12]"))).click()
            print("foi escolhido o horário 16:00")

        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        # Questionário
        self.driver.find_element(By.NAME, "observacao").send_keys('teste')
        self.driver.find_element(By.ID, "c8272066-6776-4f28-90cc-046b932fcfe8").click()
        self.driver.find_element(By.ID, "715eda97-f2fa-4832-9fa1-d3f81e9d69a0").click()
        self.driver.find_element(By.ID, "ae7304c9-f593-441d-a089-e7beeb96849e").click()
        self.driver.find_element(By.ID, "051680d2-b92b-4cf2-8d79-c8902c5c3f77").click()
        self.driver.find_element(By.ID, "1f1345b0-d724-4248-a910-146715e6548a").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        # Confirmação de pagamento
        WebDriverWait(self.driver, 5)
        self.driver.find_element(By.NAME, "confirmar-pagamento").click()

        toast = ToastNotifier()
        toast.show_toast("Atenção!!!", "Resolva o captcha manualmente", duration=20, threaded=True)
        time.sleep(25)
        self.driver.find_element(By.ID, "finalizar-pedido").click()

        WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-violet'][contains(.,'Fechar')]")
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-violet'][contains(.,'Fechar')]").click()

        # Fim do programa
        self.driver.close()

