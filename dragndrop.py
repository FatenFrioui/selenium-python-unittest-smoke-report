import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class Mydrap(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    def test_dragdrop(self):
        # given
        driver = self.driver
        driver.maximize_window()
        driver.get("https://qavbox.github.io/demo/dragndrop/")
        # When
        drag1 = driver.find_element_by_id('draggable')
        drop1 = driver.find_element_by_id('droppable')
        time.sleep(3)
        action = ActionChains(driver)
        #L'objet chaîne d'action implémente les ActionChains sous la forme d'une file d'attente, puis exécute la méthode perform(). En appelant la méthode perform(), toutes les actions sur les chaînes d'action seront effectuées.
        action.drag_and_drop(drag1, drop1).perform()
        # drag_and_drop: Cette méthode effectue l'action de maintenir le bouton gauche de la souris sur l'élément source. Se déplace ensuite vers l'élément cible et relâche enfin le bouton de la souris.
        # perform() - Cette méthode exécute toutes les actions en file d'attente les unes après les autres
        time.sleep(3)
        # then
        self.assertEqual("Dropped!", drop1.text)
        time.sleep(2)
        # methode2
        # action = ActionChains(driver)
        # drag1 = driver.find_element_by_id('draggable')
        # action.drag_and_drop_by_offset(drag1,166,100).perform()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
