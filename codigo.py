from selenium import webdriver  # Metodo Selenium
from time import sleep  # Pausas do site exemplo sleep(5), pausa por 5 seg
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


index = 0


class Automacao:
    def __init__(self):
        # Caminho do driver, se estiver em outra pasta fevemos especificar o caminho, ex: ../../Pyprojects/
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        # Carrega o perfil do Chromen como um default, ou você pode especificar
        self.options.add_argument(
            r'user-data-dir=C:\Users\#usuario\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome()

    def enter_Fiel(self, site):
        self.chrome.get(site)

    def exit_Fiel(self):
        self.chrome.quit()

    def close_add(self):
        try:
            command = self.chrome.find_element(
                by=By.CLASS_NAME, value='popup__close')
            command.click()
        except Exception as e:
            print('Erro ao tentar fechar o anuncio', e)

    def enter_log(self):
        try:
            command = self.chrome.find_element(by=By.LINK_TEXT, value='ENTRAR')
            command.click()
        except Exception as e:
            print('Erro ao clicar em entrar', e)

    def input_user(self):
        try:
            command_login = self.chrome.find_element(
                by=By.ID, value='ANomeLogin')
            command_password = self.chrome.find_element(
                by=By.ID, value='Asenha')
            command_recapcha = self.chrome.find_element(
                by=By.CLASS_NAME, value='g-recaptcha')
            command_commit = self.chrome.find_element(
                by=By.CSS_SELECTOR, value='#FormLogin > div > div:nth-child(3) > button')

            command_login.send_keys('#username')
            command_password.send_keys('#senha')
            command_recapcha.click()
            sleep(8)
            command_commit.click()

        except Exception as e:
            print('Erro no Input User', e)

    def enter_buy_tickets(self):
        try:
            command = self.chrome.find_element(
                by=By.LINK_TEXT, value='Compra de ingressos')
            command.click()
        except Exception as e:
            print('Erro no enter_buy_tickets', e)

    def terms(self):
        try:
            command = self.chrome.find_element(
                by=By.XPATH, value='//*[@id="formCompra"]/div[2]/div/label[1]')
            command_commit = self.chrome.find_element(
                by=By.XPATH, value='//*[@id="btnComprar"]')
            command.click()
            sleep(0.9)
            command_commit.click()
        except Exception as e:
            print('Erro no terms', e)

    def terms2(self):
        try:
            command_rpa = self.chrome.find_element(
                by=By.XPATH, value='//*[@id="formCompra"]/div[1]/label[1]')
            command_recaptcha = self.chrome.find_element(
                by=By.CSS_SELECTOR, value='#formCompra > div.g-recaptcha.fade__items')
            command_recaptcha.click()
            command_rpa.click()
            sleep(7)
            command_buybtn = self.chrome.find_element(
                by=By.ID, value='btnComprar')
            command_buybtn.click()
        except Exception as e:
            print('Erro no terms2', e)

    def changeWins(self):
        try:
            self.chrome.switch_to.window(self.chrome.window_handles[index])
        except Exception as e:
            print('Erro no ChangeWins: ', e)


if __name__ == '__main__':
    chrome = Automacao()

    chrome.enter_Fiel('https://www.fieltorcedor.com.br/')
    sleep(1)
    chrome.close_add()
    chrome.enter_log()
    sleep(2)
    chrome.input_user()
    sleep(2)
    chrome.enter_buy_tickets()
    sleep(2)
    chrome.changeWins()
    index += 1
    sleep(0.9)
    chrome.changeWins()
    index -= 1
    sleep(1)
    chrome.terms()
    chrome.changeWins()
    index += 1
    sleep(0.9)
    chrome.changeWins()
    chrome.terms2()
