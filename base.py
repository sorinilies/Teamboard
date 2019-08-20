from selenium import webdriver
from utils import *
from objects import Objects


CAPABILITIES = {
                "debugConnectToRunningApp": "False",
                "app": r"d:\hackaton\Debug\TeamBoard.exe",
                "launchDelay": 100
                }


class App(WiniumDriver):

    def __init__(self, remote_url="http://localhost:9999"):
        # Winium Driver
        super().__init__()

        # Closing app if already running
        if get_process() is not None:
            get_process().kill()

        self.driver = webdriver.Remote(
                command_executor=remote_url,
                desired_capabilities=CAPABILITIES)

    def click(self, elem, parent=None):
        if parent is not None:
            elem = parent.find_element(*elem)
        else :
            elem = self.driver.find_element(*elem)
        elem.click()

    def get_elem_text(self, elem, parent=None):
        if parent is not None:
            elem = parent.find_element(*elem)
        else:
            elem = self.driver.find_element(*elem)

        return elem.text

    def get_list(self, elem="ListBoxItem"):
        list_view = self.list_view()
        results = list_view.find_elements_by_class_name(elem)
        return results

    def get_list_fields(self):
        pass

    def get_list_names(self, attr = "Name"):
        results = []
        for item in self.get_list():
            labels = item.find_elements_by_id("lblName")
            for item in labels:
                res = item.find_element_by_class_name("TextBlock")
                results.append(res.get_attribute("Name"))

        if len(results) > 0:
            return results
        else:
            return None

    def tree_view(self):
        return self.driver.find_element_by_class_name(Objects.TREE_VIEW)

    def list_view(self):
        return self.driver.find_element_by_class_name(Objects.LIST_VIEW)

    def is_checked(self, elem):
        parent = self.tree_view()
        elem = parent.find_element(*elem)
        return elem.is_selected()

    def cleanup(self):
        self.driver.close()
        self.driver.quit()
