import unittest
import logging

import HtmlTestRunner

from base import App
from objects import Objects
log = logging.getLogger("TestLog")

class Testcase(unittest.TestCase):
    def setUp(self):
        self.app = App()
        print("1. Application was started")

    def test_select_qa_automation(self):
        # Select QA Automation team members
        self.app.click(Objects.QA_AUTOMATION, parent=self.app.tree_view())
        self.app.click(Objects.FILTER)
        # Validate Automation team members displayed
        member1 = 'Sorin'
        member2 = 'Dorin'
        self.assertIn(member2, self.app.get_list_names())
        self.assertIn(member1, self.app.get_list_names())

        print("2. Check QA Automation team: ", self.app.get_list_names())

    def test_deselect_auto_select_dev(self):
        # Deselect QA Automation team members
        self.app.click(Objects.QA_AUTOMATION, parent=self.app.tree_view())
        self.app.click(Objects.QA_AUTOMATION, parent=self.app.tree_view())

        # Select Dev team
        self.app.click(Objects.DEV, parent=self.app.tree_view())
        self.app.click(Objects.FILTER)

        # Validate Automation team members are not displayed
        auto1 = 'Sorin'
        auto2 = 'Dorin'

        dev1 = 'Norbert'
        dev2 = 'Darius'

        # Assert that automation members are not displayed
        self.assertNotIn(auto1, self.app.get_list_names())
        self.assertNotIn(auto2, self.app.get_list_names())

        # Assert that dev members are displayed
        self.assertIn(dev1, self.app.get_list_names())
        self.assertIn(dev2, self.app.get_list_names())

        print("2. Dev members displayed: ", self.app.get_list_names())

    def test_select_tl_return_nothing(self):
        # Select TL role
        self.app.click(Objects.TL, parent=self.app.tree_view())
        self.app.click(Objects.FILTER)

        # validate that nothing is displayed
        self.assertIsNone(self.app.get_list_names(), "Members are displayed while there shouldn't!")
        print("2. Members displayed: ", self.app.get_list_names())



    def tearDown(self):
        self.app.cleanup()
        print("3. Application is closed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
