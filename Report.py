import os
import unittest

from HTMLTestRunner import HTMLTestRunner

import WikiTest
import YoutubeTest
import dragndrop
import googleTest
import scrollbars

direct=os.getcwd()




class MyTestSuite(unittest.TestCase):
    def test_Issue(self):
        suite_smoke_test=unittest.TestSuite()
        suite_smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(YoutubeTest.MyYoutubeTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(WikiTest.MyWikiTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(googleTest.MyGoogleTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(dragndrop.Mydrap),
            unittest.defaultTestLoader.loadTestsFromTestCase(scrollbars.MyScroll),
        ])
        chemin=open(direct+"\SmokeTest.html","w")

        runner1=HTMLTestRunner.HTMLTestRunner(
            stream=chemin,
            title='Test Report',
            description='Smoke Tests'

        )
        runner1.run(suite_smoke_test)

if __name__ == '__main__':
    unittest.main()
