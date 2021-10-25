import unittest
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ponto_juridico.config.settings.base import ROOT_DIR, env

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.accessibility = self.create_accessibility()

    def create_accessibility(self):
        return self.Accessibility(self)

    def tearDown(self):
        self.browser.quit()

    class Accessibility:
        def __init__(self, ft):
            self.ft = ft

        def check(self):
            self.visual_impaired()

        def visual_impaired(self):
            # Check if all images have `alt` attribute
            images = self.ft.browser.find_elements_by_tag_name('img')
            self.ft.assertTrue(
                all(image.get_attribute('alt') != '' for image in images), 'Image without `alt` attribute'
            )


class NewVisitorTest(FunctionalTest):
    def test_can_see_dashboard(self):
        # Acessando o endereço local do servidor (localhost), o usuário pode acessar o IoT Server
        self.browser.get('http://localhost:8000')
        self.accessibility.check()

        # Ao acessar o link, ele encontra o nome do projeto e uma tela de Login.
        self.assertIn("Entrar", self.browser.title)
        email = self.browser.find_element_by_name('login')
        passwd = self.browser.find_element_by_name('password')

        # Inserindo as credenciais corretas, ele é redirecionado para a dashboard
        email.send_keys(env.str("USERNAME"))
        passwd.send_keys(env.str("PASSWD"))
        email.submit()
        WebDriverWait(self.browser, 10).until(
            EC.title_is("ponto_juridico")
        )
        self.accessibility.check()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
