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

    # def test_user_can_connect_and_disconnect(self):
    #     """test if user can access sign in page, and 
    #     then disconnect"""

    #     self.driver.get(self.live_server_url)
    #     self.driver.find_element_by_css_selector('#button-login').click()
    #     self.driver.find_element_by_css_selector('#id_username').send_keys(
    #         "usertest123"
    #     )
    #     self.driver.find_element_by_css_selector('#id_password').send_keys(
    #         "bouYaka2021"
    #     )
    #     self.driver.find_element_by_css_selector('#button-submit').click()

    #     self.driver.find_element_by_css_selector('#button-logout').click()
    #     self.assertIn("Purbeurre - Déconnexion", self.driver.title)

# class PurbeurreFunctionalSearchTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_search_in_purbeurre_search_bar_chrome(self):
#         driver = self.driver
#         driver.get("http://localhost:8000/")
#         self.assertIn("Purbeurre", driver.title)
#         elem = driver.find_element_by_name("query_search")
#         elem.send_keys("pizza")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source

#     def tearDown(self):
#         self.driver.close()
#         self.driver.quit()

# class PurbeurreFunctionalUserLogInTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.user = User.objects.create_user(
#             username="usertest123",
#             email="usertest@occompany.com",
#             password="bouyaka231",
#             )

#     def test_user_login_to_existing_account_chrome(self):
#         driver = self.driver
#         driver.get("http://localhost:8000/login/")
#         self.assertIn("Purbeurre - Se connecter", driver.title)
#         elem = driver.find_element_by_name("username")
#         elem.send_keys("usertest123")
#         elem2 = driver.find_element_by_name("password")
#         elem2.send_keys("bouyaka231")
#         elem2.send_keys(Keys.RETURN)
#         assert "fas fa-sign-out-alt" in driver.page_source
#         assert "fas fa-sign-in-alt" not in driver.page_source

#     def tearDown(self):
#         self.driver.close()
#         self.driver.quit()

# class PurbeurreFunctionalUserCreationTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_new_user_to_create_account_chrome(self):
#         driver = self.driver
#         driver.get("http://localhost:8000/register/")
#         self.assertIn('Purbeurre - Créer un compte', driver.title)
#         new_username = driver.find_element_by_name("username")
#         new_username.send_keys("usertest123")
#         email = driver.find_element_by_name("email")
#         email.send_keys("userOctest@comp.com")
#         password1 = driver.find_element_by_name("password1")
#         password1.send_keys("bouyaka231")
#         password2 = driver.find_element_by_name("password2")
#         password2.send_keys("bouyaka231")
#         password2.send_keys(Keys.RETURN)
#         assert "fas fa-user" not in driver.page_source
#         assert "fas fa-carrot" not in driver.page_source

#     def tearDown(self):
#         self.driver.close()
#         self.driver.quit()

# class PurbeurreFunctionalUserSendEmailToPurbeurreHomePage(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_user_on_homepage_can_send_email_from_homepage(self):
#         driver = self.driver
#         driver.get("http://localhost:8000/")
#         self.assertIn('Purbeurre - Accueil', driver.title)
#         elem = driver.find_element_by_name("contact_email")
#         elem.click()
#         assert "contact_email" in driver.page_source

#     def tearDown(self):
#         self.driver.close()
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()