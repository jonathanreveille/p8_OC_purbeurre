from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from purbeurre.settings import BASE_DIR
from django.contrib.auth import get_user_model

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

class ChromeFunctionalTestCase(StaticLiveServerTestCase):
    """functional test for Chrome browser with
    tchappuis-webdriver in headless mode"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path = str(BASE_DIR/'webdrivers'/'chromedriver'),
            options=chrome_options,
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        User = get_user_model()
        User.objects.create_user(
            username="usertest123",
            password="bouYaka2021",
        )

    def test_search_in_purbeurre_search_bar_chrome(self):
        """Test if searchbar works well"""
        self.driver.get(self.live_server_url)
        self.assertIn("Purbeurre", self.driver.title)
        elem = self.driver.find_element_by_name("query_search")
        elem.send_keys("pizza")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    def test_user_on_homepage_can_send_email_from_homepage(self):
        self.driver.get(self.live_server_url)
        self.assertIn('Purbeurre - Accueil', self.driver.title)
        elem = self.driver.find_element_by_name("contact_email")
        elem.click()
        assert "contact_email" in self.driver.page_source

