from pages.vendor_feature_page import VendorFeature
from TestCase.base_test import BaseTest


class VendorAddProduct(BaseTest):

    def test_vendor_add_product(self):
        vendor_feature = VendorFeature(self.driver)
        vendor_feature.login_vendor()
        # vendor_feature.add_product()
        vendor_feature.add_coupon()

# python3 -m unittest TestCase.test1
# python3 -m pytest -s TestCase/test1.py --alluredir=ReportAllure &&  allure serve ReportAllure/
