__author__ = 'd.shklyannik'

import unittest
from TestQa.SeleniumTest import page

from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "python.org title doesn't match."
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

    # http://username:password@the-site.com
