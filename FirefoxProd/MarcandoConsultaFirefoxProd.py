# minhas importacoes
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from win10toast import ToastNotifier
from faker import Faker
fake = Faker('pt_BR')



class Test_marcando_consulta():
    def setup_method(self):
        self.driver = webdriver.Firefox(executable_path=
                        'C:\\Users\\Juliana.bueno\\Desktop\\AutomacaoWebCludeSelenium\\drivers\\geckodriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2")
        self.driver.maximize_window()


        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("xx")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(30)

        # iniciando
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body'][contains(.,'Videoconsulta com médicos,  psicólogos e nutricionistas')]")
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body'][contains(.,'Videoconsulta com médicos,  psicólogos e nutricionistas')]").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body bg-light-2x-pink'][contains(.,'Agendar videoconsulta')]")
        self.driver.find_element(By.XPATH,
                                 "//div[@class='panel-body bg-light-2x-pink'][contains(.,'Agendar videoconsulta')]").click()
        dropdown = self.driver.find_element(By.NAME, "paciente").click()
        dropdown = self.driver.find_element(By.XPATH, "//option[@value='aafee064-1e5d-4517-9d05-434e2898139d']").click()


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
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'12')])[1]"))).click()
            print("foi escolhido o dia 12")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'30')])[1]"))).click()
            print("foi escolhido o dia 30")

        # Escolha o horario da consulta
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'07:40')])[12]"))).click()
            print("foi escolhido o horário 07:40")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'08:40')])[12]"))).click()
            print("foi escolhido o horário 08:40")

        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        # Questionário
        self.driver.find_element(By.NAME, "observacao").send_keys('teste')
        self.driver.find_element(By.NAME, "pergunta-e678d638-bfc3-451b-8b5f-c81e938b7dbf").click()
        self.driver.find_element(By.NAME, "pergunta-0e85afd9-2e5e-4d3d-94e8-77542460c5d3").click()
        self.driver.find_element(By.NAME, "pergunta-04326ea2-5ca3-4335-8b75-64d346ccc4e9").click()
        self.driver.find_element(By.NAME, "pergunta-867b7f49-d362-4503-8ecc-ec10c17e5945").click()
        self.driver.find_element(By.NAME, "pergunta-478b796a-1d4f-4e9f-baac-8e2a58ccec14").send_keys('teste')
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        # Confirmação de pagamento
        self.driver.find_element(By.ID, "ui-id-1").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-violet next-button']")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-violet next-button']").click()

        # Revise o pedido
        self.driver.find_element(By.XPATH, "//h2[@class='welcome-title'][contains(.,'Revise o pedido:')]")
        WebDriverWait(self.driver, 5)
        self.driver.find_element(By.NAME, "confirmar-pagamento").click()

        # toast = ToastNotifier()
        # toast.show_toast("Atenção!!!", "Resolva o captcha manualmente", duration=10, threaded=True)
        # self.driver.find_element(By.ID, "finalizar-pedido").click()
        # time.sleep(30)
        self.driver.find_element(By.ID, "finalizar-pedido")
        self.driver.find_element(By.ID, "finalizar-pedido").click()
        WebDriverWait(self.driver, 10)
        element = self.driver.find_element(By.CSS_SELECTOR, ".clude-modal-content")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.find_element(By.LINK_TEXT, "Fechar").click()
        # Fim do programa
        self.driver.close()