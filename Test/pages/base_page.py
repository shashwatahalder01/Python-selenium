from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from time import sleep


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 90

    # common scenarios___________________________________

    # Open link in new Tab
    def open_link_new_tab(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    # Open link in new window
    def open_link_new_window(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.SHIFT).click(element).key_down(Keys.SHIFT).perform()

    # Get text of multiple elements ✓✓
    def get_text_of_multiple_element(self, *locator):
        # elements = self.driver.find_elements(*locator)
        elements = self.find_elements(*locator)
        val = []
        for element in elements:
            val.append(element.text)
        return val

    # Get attribute of multiple elements ✓✓
    def get_attribute_of_multiple_element(self, attribute, *locator):
        elements = self.driver.find_elements(*locator)
        val = []
        for element in elements:
            attr = element.get_attribute(attribute)
            val.append(attr)
        return val

    # Interacting with the page_________________________

    # Locate elements _________________________________

    # # Find single element  ✓✓
    # def find_element(self, *locator):
    #     return self.driver.find_element(*locator)

    # Find single element
    def find_element(self, *locator):
        return self.wait_till_visibility_of_element_located(30, *locator)

    # Find multiple elements  ✓✓
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    # Mouse hover on an element  ✓✓
    def hover(self, *locator):
        # element = self.driver.find_element(*locator)
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # Element properties______________________________________________

    # Element is displayed or not  ✓✓
    def element_is_displayed(self, *locator):
        # element = self.driver.find_element(*locator)
        element = self.find_element(*locator)
        res = element.is_displayed()
        return res

    # Element is enabled or not
    def element_is_enabled(self, *locator):
        element = self.driver.find_element(*locator)
        res = element.is_enabled()
        return res

    # Element is selected or not   # checkbox/Radio
    def element_is_selected(self, *locator):
        element = self.driver.find_element(*locator)
        res = element.is_selected()
        return res

    # Get attribute ✓✓
    def get_attribute_value(self, attribute, *locator):
        element = self.driver.find_element(*locator)
        val = element.get_attribute(attribute)
        # print(val)
        return val

    # Get multiple attribute value of single element ✓✓
    def get_multiple_attribute_value(self, attributes, *locator):
        element = self.driver.find_element(*locator)
        val = []
        for attribute in attributes:
            val.append(element.get_attribute(attribute))
        return val

    # Get CSS property ✓✓
    def get_css_property(self, attribute, *locator):
        # element = self.driver.find_element(*locator)
        element = self.find_element(*locator)
        val = element.value_of_css_property(attribute)
        # print(val)
        return val

    # Get text ✓✓
    def get_text(self, *locator):
        # element = self.driver.find_element(*locator)
        element = self.find_element(*locator)
        val = element.text
        # print(val)
        return val

    # Text field ___________________________________

    # Send data ✓✓
    def send_data(self, data, *locator):
        # self.driver.find_element(*locator).send_keys(data)
        self.find_element(*locator).send_keys(data)

    # Clear input field ✓✓
    def clear_field(self, *locator):
        # self.driver.find_element(*locator).clear()
        self.find_element(*locator).clear()

        # or force clear

    def clear_input_field(self, *locator):
        # element = self.driver.find_element(*locator)
        element = self.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    # Clear input field and then send data to input field ✓✓
    def clear_input_field_and_send_keys(self, data, *locator):
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(data)

        # or

    def clear_field_and_send_keys(self, data, *locator):
        # element = self.driver.find_element(*locator)
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(data)

    # Filling in forms_________________________________

    # Get num of dropdown element ✓✓
    def get_num__of_dropdown_element(self, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        options = select.options
        return len(options)

    # Get list of dropdown element ✓✓
    def get_list_of_dropdown_element(self, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        options = select.options
        option_values = []
        for option in options:
            option_values.append(option.text)
        return option_values

    # Get active option in select ✓✓
    def get_active_option_of_dropdown_element(self, *locator):
        select = Select(self.driver.find_element(*locator))
        selected_option_text = select.first_selected_option.text
        return selected_option_text

    # Select dropdown elements ✓✓
    def select_dropdown_element(self, name, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        options = select.options
        option_values = []
        for option in options:
            option_values.append(option.text)
        # print(option_values)
        select.select_by_index(option_values.index(name))

    # Select 'Select' element by index value
    def select_by_index(self, index, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        return select.select_by_index(index)

    # Select 'Select' element by visible text
    def select_by_visible_text(self, text, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        return select.select_by_visible_text(text)

    # Select 'Select' element by value
    def select_by_value(self, value, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        return select.select_by_value(value)

    # De-select all 'Select' element
    def deselect_all(self, *locator):
        select = Select(self.driver.find_element(*locator))
        select.deselect_all()

    # Get list of all default selected options
    def get_selected_options(self, *locator):
        select = Select(self.driver.find_element(*locator))
        all_selected_options = select.all_selected_options
        return all_selected_options

    # Get list of all options
    def get_all_options(self, *locator):
        # select = Select(self.driver.find_element(*locator))
        select = Select(self.find_element(*locator))
        options = select.options
        return options

    # Submit form
    def submit_form(self, *locator):
        element = self.driver.find_element(*locator)
        element.submit()

    # screenshot________________________________________

    # save screenshot   # format must be png
    def take_screenshot(self, image_path):
        self.driver.save_screenshot(image_path + '/sample_screenshot_1.png')

    def get_screenshot(self, image_path):
        self.driver.get_screenshot_as_file(image_path + '/sample_screenshot_2.png')

    # returns binary data
    def take_binary_screenshot(self):
        self.driver.get_screenshot_as_png('sample_screenshot_1.png')
        # import StringIO
        # from PIL import Image
        # screenshot = driver.get_screenshot_as_png()
        #
        # size = (0, 0, 680, 400)
        # image = Image.open(StringIO.StringIO(screen))
        # region = image.crop(size)
        # region.save('sample_screenshot_3.jpg', 'JPEG', optimize=True, quality=95)

    # take element screenshot
    def take_element_screentshot(self, imagepath, *locator):
        # from PIL import Image
        element = self.driver.find_element(*locator)
        # location = element.location
        # size = element.size
        # self.driver.save_screenshot("/data/image.png")
        # x = location['x']
        # y = location['y']
        # width = location['x'] + size['width']
        # height = location['y'] + size['height']
        #
        # im = Image.open('/data/WorkArea/image.png')
        # im = im.crop((int(x), int(y), int(width), int(height)))
        # im.save('/data/image.png')

    # Mouse actions_____________________________________

    # Click ✓✓
    def click(self, *locator):
        # self.driver.find_element(*locator).click()
        self.find_element(*locator).click()

    # Double click ✓✓
    def double_click(self, *locator):
        self.driver.find_element(*locator).double_click()

    # Click and hold
    def click_and_hold(self, *locator):
        self.driver.find_element(*locator).click_and_hold()

    # contest click/ right click
    def context_click(self, *locator):
        self.driver.find_element(*locator).context_click()

    def right_click(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver).move_to_element(element)
        actions.context_click().perform()

    # Move cursor to element then click / click drop down item
    def move_cursor_and_click(self, menu, submenu1):
        menu = self.driver.find_element(menu)
        submenu = self.driver.find_element(submenu1)
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(menu).click(submenu).perform()

    #  move cursor by offset
    def move_cursor_by_offset(self, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.move_by_offset(x_offset, y_offset)

    # move cursor to element  # same  as hover function
    def move_cursor_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        sleep(1)

    # move cursor to element with offset
    def move_cursor_to_element_offset(self, x_offset, y_offset, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, x_offset, y_offset)
        actions.perform()

    # Drag and drop______________________________________

    # Drag and drop an element
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(source_locator)
        target = self.driver.find_element(target_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop(source, target)
        drag_and_drop.perform()

    # Drag and drop by offset
    def drag_and_drop_offset(self, source_locator, xoffset, yoffset):
        source = self.driver.find_element(source_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop_by_offset(source, xoffset, yoffset)
        drag_and_drop.perform()

    # modifier key + key:  CONTROL+C
    def command_perform(self, modifier_key, key):
        actions = ActionChains(self.driver)
        actions.key_down(f'Keys.{modifier_key}')  # hold key
        actions.send_keys(key)
        actions.key_down(f'Keys.{modifier_key}')  # release key
        actions.perform()

    # Sends keys to current focused element
    def send_keys_action_chains(self, key):
        actions = ActionChains(self.driver)
        actions.send_keys(key)

    # Sends keys to an element
    def send_keys_to_element_action_chains(self, key, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(element, key)

    # Press Enter key
    def press_enter(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    # Moving between windows and frames____________________

    # switch tab
    def switch_tab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

    # Switch to window by window(e.g. CDwindow-BD9C79EE569362CD463868B54C725BEF [get by current window handle] )
    def switch_to_window_by_window(self, window):
        return self.driver.switch_to.window(window)
        # return self.driver.switch_to_window(window) # deprecated

    # Switch to window by window handle number
    def switch_to_window_by_handle_number(self, handle_number):
        return self.driver.switch_to.window(self.driver.window_handles[handle_number])


    # Get current window handle
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    # Get list of all window handles
    def get_all_window_handles(self):
        return self.driver.window_handles

    # Get length of all window handles
    def get_number_of_all_window_handles(self):
        handles = self.driver.window_handles
        return len(handles)

    # count iframe
    def iframe_count(self):
        iframe_list = self.driver.find_elements_by_tag_name("iframe")
        length = len(iframe_list)
        print(length)
        return length

    # Switch to frame or iframe  #  argument frame can be index, id ,name of frame or web element of frame (for web-element method might be different)
    def switch_to_frame(self, frame):
        return self.driver.switch_to_frame(frame)

    # Switch to sub_frame or iframe
    def switch_to_sub_frame(self, parent_frame, child_frame):
        return self.driver.switch_to_frame(parent_frame + '.' + child_frame)

    # Switch back to parent frame  # or can use switch to frame method
    def switch_to_parent_frame(self):
        return self.driver.switch_to.parent_frame()

    # Switch back to main frame
    def switch_to_main_frame(self):
        return self.driver.switch_to_default_content()

    # Switch to parent window not working it may from switch to main frame
    def switch_to_parent_window(self):
        # return self.driver.switch_to_default_content() dont know which one is correct
        return self.driver.switch_to.default_content() # this is correct one may be and it for switch frame not window

    # Switch to window
    def switch_to_window(self, window):
        return self.driver.switch_to_window(self.driver.window_handles[window])

    # Popup dialogs______________________________________

    # Switch to alert
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    # Accept alert
    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    # Dismiss alert
    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    # get alert text
    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        val = alert.text
        return val

    # send text to alert
    def send_text_to_alert(self, text):
        alert = self.driver.switch_to.alert
        val = alert.send_keys(text)

    # Read browser details______________________________

    # Get title of the url ✓✓
    def get_title(self):
        return self.driver.title

    #  TODO: which one are correct???
    # def get_window_handle(self, num):
    #     return self.driver.window_handles[num]
    #
    # def switch_window(self, win):
    #     return self.driver.switch_to_window(win)

    # Get window handles
    def get_window_handles(self):
        return self.driver.window_handles

    # Get current window handles
    def get_current_window_handles(self):
        return self.driver.current_window_handles

    # Get current url
    def get_current_url(self):
        return self.driver.current_url

    # Get page source
    def get_page_source(self):
        return self.driver.page_source

    #  Navigation _______________________________________

    # Open url
    def open_url(self, url):
        self.driver.get(url)

    # Open sub_url of main domain
    def open_sub_url(self, url):
        #  Base url is the main domain
        url = self.base_url + url
        self.driver.get(url)

    # Get current page url
    def get_url(self):
        return self.driver.current_url

    # Refresh page
    def refresh_page(self):
        return self.driver.refresh()

    # Go to forward page
    def go_forward(self):
        return self.driver.forward()

    # Go back to previous page
    def go_back(self):
        return self.driver.back()

    # open new tab
    def open_new_tab(self):
        self.driver.execute_script("window.open('');")
        self.switch_to_window_by_handle_number(-1)

    # open url on new tab
    def open_url_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}','_blank')")
        self.switch_to_window_by_handle_number(-1)

    # open url on new window opening in new tab not window
    def open_url_new_window(self, url):
        self.driver.execute_script(f"window.open('{url}','new_window')")
        self.switch_to_window_by_handle_number(-1)

    #  Cookies ___________________________________________

    # Set cookie for the entire domain
    def set_cookies(self, url, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.get(url)
        self.driver.add_cookie(cookie)

    # Get all the available cookies for the current URL
    def get_cookies(self, url):
        self.driver.get(url)
        self.driver.get_cookies()

    # TODO: add agent functions

    # Get User-Agent value

    def get_user_agent_value(self):
        agent = self.driver.execute_script("return navigator.userAgent")
        print(agent)

    # User - Agent setup in Chrome:
    # With Chrome, you have to use Options instance to set the user - agent value.
    #
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    #
    # opts = Options()
    # opts.add_argument("user-agent=[user-agent string]")
    # # Below is tested line
    # # opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    #
    # driver = webdriver.Chrome(chrome_options=opts)
    # Alternative   way    to  pass driver path along with other details:
    #
    # driver = webdriver.Firefox(profile, executable_path="path to geckodriver")
    # driver = webdriver.Chrome(chrome_options=opts, executable_path="path to chromedriver")

    # Waits__________________________________________________

    # Explicit wait

    # TODO: title is ??

    # TODO:  title contains ??

    #  wait till presence of element is located
    def wait_till_presence_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.presence_of_element_located(*locator))
        return element

    #  wait till visibility_of_element_located
    def wait_till_visibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.visibility_of_element_located(*locator))
        return element

    # def wait_element(self, *locator):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
    #         self.driver.quit()

    # def wait_element1(self, *locator):
    #     try:
    #         ignored_exceptions = (NoSuchElementException, StaleElementReferenceException )
    #         WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
    #         self.driver.quit()

    # wait till visibility_of_element_located
    def wait_till_visibility_of_element_located_with_exception(self, seconds, *locator):
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            wait = WebDriverWait(self.driver, seconds, ignored_exceptions=ignored_exceptions)
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {seconds}")

    #  wait till visibility_of_element_located Loop : indefinitely
    def wait_till_visibility_of_element_located_with_tries_indefinitely(self, seconds, *locator):
        while True:
            try:
                ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
                wait = WebDriverWait(self.driver, seconds, ignored_exceptions=ignored_exceptions)
                element = wait.until(ec.visibility_of_element_located(locator))
                return element
            except TimeoutException:
                print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {seconds}")

    #  wait till visibility_of_element_located Loop : tries 3
    def wait_till_visibility_of_element_located_with_tries_count(self, seconds, *locator):
        tries = 3
        for i in range(tries):
            try:
                ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
                wait = WebDriverWait(self.driver, seconds, ignored_exceptions=ignored_exceptions)
                element = wait.until(ec.visibility_of_element_located(locator))
                return element
            except TimeoutException:
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {seconds}")

    # TODO:  visibility of ??

    #  wait till presence_of_all_elements_located
    def wait_till_presence_of_all_elements_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.presence_of_all_elements_located(*locator))
        return element

    #  wait till text_to_be_present_in_element
    def wait_till_text_to_be_present_in_element(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.text_to_be_present_in_element(*locator))
        return element

    #  wait till text_to_be_present_in_element_value
    def wait_till_text_to_be_present_in_element_value(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.text_to_be_present_in_element_value(*locator))
        return element

    #  wait till frame_to_be_available_and_switch_to_it
    def wait_till_frame_to_be_available_and_switch_to_it(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.frame_to_be_available_and_switch_to_it(*locator))
        return element

    #  wait till invisibility_of_element_located
    def wait_till_invisibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.invisibility_of_element_located(*locator))
        return element

    #  wait till element_to_be_clickable
    def wait_till_element_to_be_clickable(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.element_to_be_clickable(*locator))
        return element

    # TODO: staleness of ??

    #  wait till element_to_be_selected
    def wait_till_element_to_be_selected(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.element_to_be_selected(*locator))
        return element

    #  wait till element_located_to_be_selected
    def wait_till_element_located_to_be_selected(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.element_located_to_be_selected(*locator))
        return element

    #  wait till element_selection_state_to_be
    def wait_till_element_selection_state_to_be(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.element_selection_state_to_be(*locator))
        return element

    #  wait till element_located_selection_state_to_be
    def wait_till_element_located_selection_state_to_be(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.element_located_selection_state_to_be(*locator))
        return element

    #  wait till alert_is_present
    def wait_till_alert_is_present(self, seconds):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.alert_is_present)
        return element

    # TODO: custom wait ??

    # implicit wait
    def implicit_waits(self, seconds):
        return self.driver.implicitly_wait(seconds)

    # TODO: add js executor for all function alternatives
    # TODO: 'document.getElementById("context-menu").style.display="block"'

    # JS functions_________________________________________________________

    # perform Js command
    def execute_javascript(self, command):
        self.driver.execute_script(command)

    # Js element click
    def js_click(self, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Js scroll to element
    def js_scroll_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Js scroll by pixel value
    def js_scroll_by_pixel(self, x_axis_value, y_axis_value, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(f"javascript:window.scrollBy({x_axis_value},{y_axis_value});", element)

    # Js accept alert
    def js_accept_alert(self):
        self.driver.execute_script("window.confirm = function(){return true;}")

    def js_remove_attribute(self):
        js = 'document.getElementById("upload-button").removeAttribute("onclick");'
        self.driver.execute_script(js)

    # Scroll to bottom____________________________________________

    # scroll page with down key
    def scroll_page(self):
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

    # scroll
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # scroll
    def scroll1(self):
        self.driver.execute_script("window.scrollTo(0, 100);")

    # scroll scrollable element ✓✓
    def scroll_scrollable_element(self, *locator):
        element = self.find_element(*locator)
        vertical_ordinate = 100
        # change number of scrollls
        for i in range(0, 40):
            # print(vertical_ordinate)
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, vertical_ordinate)
            sleep(0.2)
            vertical_ordinate += 100
            sleep(0.2)

    # Assertions_________________________________________________________

    # Assert value is True
    @staticmethod
    def assert_true(result):
        assert result is True

    # Assert value is False
    @staticmethod
    def assert_false(self, result):
        assert result is False

    # Assert value is null
    @staticmethod
    def assert_null(self, result):
        assert result is None

    # Assert value is not null
    @staticmethod
    def assert_not_null(self, result):
        assert result is not None

    # Assert value in data
    @staticmethod
    def assert_in(self, result, data):
        assert result in data

    # Assert value not in data
    @staticmethod
    def assert_not_in(self, result, data):
        assert result not in data

    # Assert element is displayed ✓✓
    def assert_element_is_displayed(self, message="element is found", *locator):
        res = self.element_is_displayed(*locator)
        # print(res)
        assert res is True
        print(message)

    # Assert element is not displayed ✓✓
    def assert_element_is_not_displayed(self, message="element is not found", *locator):
        # print(locator)
        try:
            element = self.driver.find_element(*locator)
            res = element.is_displayed()
            # print('>>>', res)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            # print(e)
            res = False
            # print('<<<', res)
        # print(res)
        assert res is False
        print(message)

    # Assert element has/hasn't css property ✓✓
    def assert_css_property_value(self, choice, attribute, expected_val, *locator):
        val = self.get_css_property(attribute, *locator)
        # print(val)
        if val.startswith('rgba'):
            val = self.rgba_to_hex(val)
            # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    # Assert element has/hasn't attribute ✓✓
    def assert_get_attribute_value(self, choice, attribute, expected_val, *locator):
        val = self.get_attribute_value(attribute, *locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    # Assert element attribute in  expected value
    def assert_get_attribute_value_in(self, choice, attribute, expected_val, *locator):
        val = self.get_attribute_value(attribute, *locator)
        # print(val)
        if choice == 'In':
            assert val in expected_val
        else:
            assert val not in expected_val

    # Assert element text ✓✓
    def assert_get_text(self, choice, expected_val, *locator):
        val = self.get_text(*locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    # Assert element text in  expected value
    def assert_get_text_in(self, choice, expected_val, *locator):
        val = self.get_text(*locator)
        # print(val)
        if choice == 'In':
            assert expected_val in val
        else:
            assert expected_val not in val

    # Assert expected value in element text
    def assert_val_in_get_text(self, choice, expected_val, *locator):
        val = self.get_text(*locator)
        # print(val)
        if choice == 'In':
            assert val in expected_val
        else:
            assert val not in expected_val

    # Assert blank checkbox  ✓✓
    def assert_blank_checkbox_element(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    # Assert not blank checkbox
    def assert_checkbox_element(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    # Assert element has attribute or not ✓✓
    # N.B. For present: result = 'true' and not_present: result = None
    def assert_is_attribute_present(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    # CSS related function

    # Convert rgba to hex ✓✓
    @staticmethod
    def rgba_to_hex(rgba):
        rgba = eval(rgba.split('a')[-1])
        return '#{:02x}{:02x}{:02x}'.format(*rgba)

