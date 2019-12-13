from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from SeleniumLibrary.base import keyword
from SeleniumLibrary import SeleniumLibrary

class LoginPage(PageObject):

    _locators = {
        "username": "name=uname",
        "password": "name=psw",
        "submit_button": "name=submit",
        "main_message": "id=main-message",
    }
    
    def login_as_a_normal_user(self):
        logger.info(self._locators['username'])
        logger.info("WE ARE HERE ::::: HELL WITH IT")
        username = BuiltIn().get_variable_value("${USERNAME}")
        password = BuiltIn().get_variable_value("${PASSWORD}") 
        self.se2lib.input_text(self.locator.username, username)
        self.se2lib.input_text(self.locator.password, password)
        with self._wait_for_page_refresh():
           self.selib.click_button(self.locator.submit_button)
        errorinfo = self.selib.get_text(self.locator.main_message)
        if errorinfo != "Hello":
           raise AssertionError("Doesn't Match")
        #  logger.info(errorinfo)


    def handle_alert_if_shown(self):
        try:
            alertMessage = self.handle_alert("ACCEPT", "0s")
            logger.info("Alert was present when test finished: " + alertMessage, html=False)
        except:
            pass

    def return_browser_console_log(self):
        log = self.driver.get_log('browser')

        result = ["There was following content in the browser console when test failed:"]
        for row in log:
            if row["message"] not in result:
                result.append(row["message"])

        return result

    def print_browser_console_log(self, log):
        if log.__len__() > 1:
            for message in log:
                print(message)            

    @keyword('Generic Test Teardown')
    def generic_test_teardown(self):
        self.handle_alert_if_shown()
        test_status = BuiltIn().get_variable_value("${TEST STATUS}")
        try:
           if test_status == "FAIL":
               self.selib.capture_page_screenshot()
               log = self.return_browser_console_log()
               self.print_browser_console_log(log)
        except:
           pass
           # print("No Failure!!")  

    # @keyword('Input username')
    # def input_username(self,username):
    #     username = BuiltIn().get_variable_value("${USERNAME}")
    #     self.se2lib.input_text(self.locator.username, username)

    # @keyword('Input pwd')
    # def input_pwd(self,password):
    #     # password = BuiltIn().get_variable_value("${password}") 
    #     self.se2lib.input_text(self.locator.password, password) 

    # @keyword('click login button')
    # def click_submit(self):
    #      self.selib.click_button(self.locator.submit_button)

    @keyword('Error page should be visible')
    def error_info(self):
         errorinfo = self.selib.get_text(self.locator.main_message)
         if errorinfo != "Hello":
            raise AssertionError("Doesn't Match")                        

