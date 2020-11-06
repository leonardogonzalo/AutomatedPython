import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
from util import Util

class Velocity:

    def __init__(self,driver):
        self.driver = driver
        self.usuariologin = 'soporteprol@belcorp.biz'
        self.passlogin ='Enero2020$'
        self.usuario = 'MXDTI'
        self.url = 'https://velocity.belcorp.biz/login'
        self.wait = WebDriverWait(driver,60)

    def login(self):
        try:
            driver = self.driver
            driver.get(self.url)
            linklogin = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div[3]/a')
            linklogin.click()
            txtusuario = driver.find_element_by_id("userNameInput")
            txtusuario.send_keys(self.usuariologin)
            txtpassword = driver.find_element_by_id("passwordInput")
            txtpassword.send_keys(self.passlogin)
            btiniciar = driver.find_element_by_id("submitButton")
            btiniciar.click()
        except Exception as ex:
            driver.quit()
            print(ex)

    def programar_backups(self):
        try:
            driver = self.driver
            wait = self.wait
            self.login()
            linkoperacion = driver.find_element_by_xpath('//*[@id="js_tabs"]/li[4]/a/span[1]/span[2]')
            linkoperacion.click()
            linkbackup = driver.find_element_by_xpath('//*[@id="backups"]/div/ul/li[2]/a')
            linkbackup.click()
            linkopcionesguardada = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/span[1]')
            linkopcionesguardada.click()
            driver.execute_script("window.scrollTo(0, 200)")
            time.sleep(5)
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div/div/div[2]/ul/li[14]/span')))
            linkbasesprol = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div/div/div[2]/ul/li[14]/span')
            linkbasesprol.click()
            driver.execute_script("window.scrollTo(0, 600)")
            txtusuariobd = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/form/div[3]/div[2]/div/div[1]/input')
            txtusuariobd.send_keys(self.usuario)
            linkcalendario = driver.find_element_by_xpath('//*[@id="datetimepicker"]/span')
            linkcalendario.click()
            btprogramar = driver.find_element_by_name("submit")
            btprogramar.click()
            time.sleep(3)
            self.capturar_proceso()

        except Exception as ex:
            driver.quit()
            print(ex)

    def capturar_proceso(self):
        try:
            driver = self.driver
            driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(5)
            linkpanel = driver.find_element_by_xpath('//*[@id="js_tabs"]/li[1]/a')
            linkpanel.click()
            linkrequeprogramado = driver.find_element_by_xpath('//*[@id="home"]/div/ul/li[2]/a')
            linkrequeprogramado.click()
            time.sleep(3)
            driver.save_screenshot("captura.png")
            contenedorprogramado = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div')
            u = Util()
            u.captura_elemento('captura.png',contenedorprogramado,'elemento_1.png')   
        except Exception as ex:
            driver.quit()
            print(ex)









