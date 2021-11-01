import pathlib
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from testconf.run_configuration import headless, linux


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        if headless:
            options.add_argument("--headless")
        # options.add_argument("--headless")
        # options.add_argument("--start-fullscreen")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--start-maximized")
        # options.add_argument("-–incognito")
        # options.add_argument("-–disable-notifications")  # only for chrome
        # options.add_argument("download.default_directory=" + "Test/data")
        # or
        # options.add_argument("--start-fullscreen","-–incognito","-–disable-notifications" )
        options.add_argument("--window-size=1920,1080")
        if linux:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # else:
            # self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver.exe", options=options)

        self.driver.maximize_window()
        self.driver.set_page_load_timeout(3000)
        self.driver.get('https://shanjida.ajaira.website/')

    def tearDown(self):
        self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
