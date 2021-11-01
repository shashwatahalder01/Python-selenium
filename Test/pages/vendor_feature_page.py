# from data.data import Data
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
import random, string
import allure


class VendorData(object):
    vendor_username = "shashwatahalder01@gmail.com"
    vendor_password = "11Shashwata11"
    product_price = "200"


class VendorLocators(object):
    login_link = (By.XPATH, '//ul[@class="nav navbar-nav navbar-right"]//a[@class="dokani-menu-login"]')
    username = (By.XPATH, '//input[@id="username"]')
    password = (By.XPATH, '//input[@id="password"]')
    login = (By.XPATH, '//button[normalize-space()="Login"]')
    products = (By.XPATH, '//li[@class="products"]//a')
    add_new_product = (By.XPATH, '//a[@class="dokan-btn dokan-btn-theme dokan-add-new-product"]')
    product_name = (By.XPATH, '//input[@placeholder="Product name.."]')
    product_price = (By.XPATH, '//input[@id="_regular_price"]')
    product_category = (By.XPATH, '//span[@id="select2-product_cat-container"]')
    # product_category_type = (By.XPATH, '//li[@id="select2-product_cat-result-qmpt-15"]')
    product_category_type = (By.XPATH, '//li[contains(text(),"Uncategorized")]')
    create_product = (By.XPATH, '//input[@id="dokan-create-new-product-btn"]')
    coupons = (By.XPATH, '//li[@class="coupons"]//a')
    add_new_coupon = (By.XPATH, '//a[@class="dokan-btn dokan-btn-theme dokan-right"]')
    coupon_title = (By.XPATH, '//input[@id="title"]')
    coupon_amount = (By.XPATH, '//input[@id="coupon_amount"]')
    coupon_product = (By.XPATH, '//a[normalize-space()="Select all"]')
    show_on_store = (By.XPATH, '//input[@id="checkboxes-3"]')
    create_coupon = (By.XPATH, '//input[@name="coupon_creation"]')


class VendorFeature(BasePage):
    def __init__(self, driver):
        self.locator = VendorLocators
        self.data = VendorData
        super().__init__(driver)

    def login_vendor(self):
        sleep(2)
        self.click(self.locator.login_link)
        sleep(3)
        self.clear_field_and_send_keys(self.data.vendor_username, self.locator.username)
        sleep(1)
        self.clear_field_and_send_keys(self.data.vendor_password, self.locator.password)
        sleep(1)
        self.click(self.locator.login)
        sleep(3)
        print('successfully logged-In')

    @staticmethod
    def random_product(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def add_product(self):
        self.click(self.locator.products)
        self.click(self.locator.add_new_product)
        self.clear_field_and_send_keys(self.random_product(8), self.locator.product_name)
        self.clear_field_and_send_keys(self.data.product_price, self.locator.product_price)
        self.click(self.locator.product_category)
        sleep(1)
        self.click(self.locator.product_category_type)
        sleep(1)
        self.click(self.locator.create_product)
        sleep(2)

    @staticmethod
    def random_coupon(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def add_coupon(self):
        self.click(self.locator.coupons)
        self.click(self.locator.add_new_coupon)
        self.clear_field_and_send_keys(f'SH_{self.random_coupon(3)}', self.locator.coupon_title)
        self.clear_field_and_send_keys(self.data.product_price, self.locator.coupon_amount)
        self.click(self.locator.coupon_product)
        self.click(self.locator.show_on_store)
        self.click(self.locator.create_coupon)
        sleep(1)

    # def invalid_logIn(self, email, password):
    #     self.clear_field_and_send_keys(email, *self.locator.email)
    #     sleep(1)
    #     self.clear_field_and_send_keys(password, *self.locator.password)
    #     sleep(1)
    #     self.click(*self.locator.loginIn)
    #
    # def logout(self):
    #     self.click(*self.locatorAdminDashboardPage.username)
    #     sleep(2)
    #     self.click(*self.locatorAdminDashboardPage.logOut)
    #     print('successfully logged-out')
    #
    # @allure.step("verify super admin and can login with correct credential")
    # def test_C9192_verify_super_admin_login_with_correct_credential(self):
    #
    #     self.logIn(self.data.username, self.data.userPassword)
    #     sleep(1)
    #     res = self.element_is_displayed(*self.locatorAdminDashboardPage.dashboard)
    #     assert res is True
    #     print('Dashboard found in admin Dashboard page')
    #     res = self.element_is_displayed(*self.locatorAdminDashboardPage.username)
    #     assert res is True
    #     print('User menu found in admin Dashboard page')
    #
    # @allure.step("verify super admin cannot login with invalid credential")
    # def test_C9193_verify_super_admin_cannot_login_with_invalid_credential(self):
    #
    #     email = [self.data.incorrectUsername, self.data.username, self.data.incorrectUsername]
    #     password = [self.data.incorrectUserPassword, self.data.incorrectUserPassword, self.data.userPassword]
    #
    #     for i in range(3):
    #         self.invalid_logIn(email[i], password[i])
    #         res = self.element_is_displayed(*self.locator.loginAlert)
    #         assert res is True
    #         print('Error message shown')
    #         sleep(3)
    #
    # @allure.step("verify super admin don't get blocked for max invalid login attempts")
    # def test_C9194_verify_super_admin_dont_get_blocked_for_max_invalid_login_attempts(self):
    #
    #     for _ in range(10):
    #         self.invalid_logIn(self.data.incorrectUsername, self.data.incorrectUserPassword)
    #         sleep(1)
    #
    #     self.logIn(self.data.username, self.data.userPassword)
    #     res = self.element_is_displayed(*self.locatorAdminDashboardPage.dashboard)
    #     assert res is True
    #     print('Dashboard found in admin Dashboard page')
    #     res = self.element_is_displayed(*self.locatorAdminDashboardPage.username)
    #     assert res is True
    #     print('User menu found in admin Dashboard page')
