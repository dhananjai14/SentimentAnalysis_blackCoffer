import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import shutil
import os
import logger
import traceback


class DataExtract:
    def __init__(self, path_of_excel_file, path_of_target_file):
        """

        :param path_of_excel_file:
        :param path_of_target_file:
        :return: None
        """

        try:
            self.path = path_of_excel_file
            self.log = logger.logs()
            self.target = path_of_target_file
            self.log.write_log('DataExtraction', 'Inside the class data extraction')
            self.log.write_log('DataExtraction', 'file path is : {}'.format(self.path))
            self.log.write_log('DataExtraction', 'target path is : {}'.format(self.target))

        except:
            self.log.write_log('DataExtraction', traceback.format_exc(), 'error')

    def data_load(self, web_driver):
        """

        :param web_driver: Path of web driver
        :return: None
        """
        try:
            self.log.write_log('DataExtraction', "Inside the data_load method")
            self.log.write_log('DataExtraction', "Path of web_driveris {}".format(web_driver))
            driver = webdriver.Chrome(executable_path=web_driver)
            data = pd.read_excel(self.path, engine='openpyxl')
            self.log.write_log('DataExtraction', "excel file loaded")
            if os.path.isdir(self.target):
                shutil.rmtree(self.target)
                os.mkdir(self.target)
                self.log.write_log('DataExtraction', "Directory created {}".format(self.target))
            else:
                os.mkdir(self.target)
                self.log.write_log('DataExtraction', "Directory created {}".format(self.target))

            for i in range(len(data)):
                url_id, url = data.iloc[i, :][0], data.iloc[i, :][1]
                driver.get(url)
                self.log.write_log('DataExtraction', "Url fetched and loaded in driver")
                all_text = driver.find_elements(By.XPATH, '//p')

                if all_text == []:
                    all_text = driver.find_elements(By.XPATH, "//div[normalize-space()='Ooops... Error 404']")
                    self.log.write_log('DataExtraction', "Url does not exists")

                for txt in all_text:
                    with open(r"{}\{}.txt".format(self.target, url_id), 'a', encoding='utf-8') as f:
                        f.write("{} \n".format(txt.text))
                self.log.write_log('DataExtraction', "Data Loaded in file {}.txt".format(url_id))
            driver.close()
            return None
        except:
            self.log.write_log('DataExtraction', traceback.format_exc(), 'error')
            return traceback.format_exc()

