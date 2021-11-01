from pages.customer_feature_page import CustomerFeature
from TestCase.base_test import BaseTest


class VendorAddProduct(BaseTest):

    def test_vendor_add_product(self):
        customer_feature = CustomerFeature(self.driver)
        customer_feature.login_customer()
        customer_feature.place_order()

# python3 -m unittest TestCase.test1
# python3 -m pytest -s TestCase/test1.py --alluredir=ReportAllure &&  allure serve ReportAllure/
