
from selenium import webdriver
import unittest

base_url = "http://SMARTLOG\D.shklyannik:Happy12345@vm-app.smartlog.loc/BackOffice/Reports/"

class ReportsSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(base_url)

    def page_is_exist_checks(self):
        assert "Please, generate a report to get results." not in self.driver.page_source
        assert "Ooops!" not in self.driver.title
        assert "Access denied" not in self.driver.title
        assert "Authorization required" not in self.driver.title
        assert "Page Not Found" not in self.driver.title

    # Transaction Reports pages
    def test_account_summary(self):
        self.driver.get(base_url + "AccountSummaryReport.aspx")
        assert "Amaryllis Payment Solutions - Backoffice: Account Summary" in self.driver.title
        elem = self.driver.find_element_by_name("ctl00$ctl00$pnlSearchFilter$i0$cphButtons$cphButtons$btnSearch_input")
        elem.click()
        self.page_is_exist_checks()

    def test_generic_transactions(self):
        self.driver.get(base_url + "GenericTransactionsReport.aspx")
        assert "Amaryllis Payment Solutions - Backoffice: Generic Transactions" in self.driver.title
        elem = self.driver.find_element_by_name("ctl00$ctl00$pnlSearchFilter$i0$cphButtons$cphButtons$btnSearch_input")
        elem.click()
        self.page_is_exist_checks()

    def test_transactions_summary(self):
        self.driver.get(base_url + "TransactionsSummaryReport.aspx")
        assert "Amaryllis Payment Solutions - Backoffice: Transactions Summary" in self.driver.title
        elem = self.driver.find_element_by_name("ctl00$ctl00$pnlSearchFilter$i0$cphButtons$cphButtons$btnSearch_input")
        elem.click()
        self.page_is_exist_checks()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
