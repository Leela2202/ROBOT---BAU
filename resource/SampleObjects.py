from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary.base import keyword
from SeleniumLibrary import SeleniumLibrary
from robot.api import logger

class SampleObjects(SeleniumLibrary):
    
    @keyword("Enter into text field")
    def enter_username(self,username):
        """Enter the given string into the username field"""
        logger.info("WE ARE HERE :::::")
        self.driver.find_element_by_id(username).send_keys(username)