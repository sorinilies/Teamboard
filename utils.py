import subprocess
import psutil
import os
import pymysql.cursors

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_PROCESS = "TeamBoard.exe"
DRIVER_PROCESS = "Winium.Desktop.Driver.exe"

class WiniumDriver:

    def __init__(self):
        if get_process(DRIVER_PROCESS) is None:
            try:
                print("Attempting to start Winium Driver")
                self.process = subprocess.Popen(PROJECT_ROOT + "/resources/Winium.Desktop.Driver.exe", shell=True,
                                                stdout=subprocess.PIPE)
                print("Started succesfuly")
            except Exception as e:
                raise(e)


    def close_process(self):
        self.process.terminate()


class DbActions:

    def __init__(self):
        self.connection = pymysql.connect(host='192.168.66.76',
                                     user='svuser',
                                     password='Softvision10',
                                     db='qaresettooldb',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def execute(self, statement):
        with self.cursor as cursor:
            cursor.execute(statement)
            return cursor.fetchall()

    def close_connection(self):
        self.connection.close()


def get_process(processName=APP_PROCESS):
    try:
        for process in psutil.process_iter():
            if process.name() == processName:
                return process
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass