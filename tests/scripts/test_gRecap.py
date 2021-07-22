import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestgRecap(BaseTest):
    def test_gRecap(self):
        logger.info("test gRecap started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(3)
        logger.info("End of entry test gRecap")
    def test_verify(self):
        import os
        import urllib
        import ffmpy
        import requests
        import speech_recognition as sr
        from pydub import AudioSegment
        r = sr.Recognizer()

        logger.info("verify process started")
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(frames[0])
        sleep(3)
        # click on checkbox to activate recaptcha
        self.driver.find_element_by_class_name("recaptcha-checkbox-border").click()
        sleep(3)
        # switch to recaptcha audio control frame
        self.driver.switch_to.default_content()
        frames = self.driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(frames[0])
        sleep(3)
        # click on audio challenge
        self.driver.find_element_by_id("recaptcha-audio-button").click()

        # switch to recaptcha audio challenge frame
        self.driver.switch_to.default_content()
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(frames[-1])
        sleep(5)
        # click on the play button
        self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
        sleep(15)

        # Step 3: Download audio challenge MP3 file
        # get the mp3 audio file
        src = self.driver.find_element_by_id("audio-source").get_attribute("src")
        print("[INFO] Audio src: %s" % src)
        # download the mp3 audio file from the source

        mpPath = ".\\tests\\RecapAudio\\gRecap.wav"
        tst = urllib.request.urlretrieve(src, mpPath)
        print("audio file success ", tst)
        # Step 4: Convert from MP3 to WAV format
        sleep(10)
        # sound = AudioSegment.from_mp3(mpPath)
        # sound.export(".\\tests\\RecapAudio\\gRecap_wave.wav", format="wav")
        sample_audio = sr.AudioFile(".\\tests\\RecapAudio\\gRecap.wav")
        sleep(10)
        # Step5: Use Google speech to text API to decipher audio challenge
        # translate audio to text with google voice recognition
        # with
        key = r.recognize_google(sample_audio)
        print("[INFO] Recaptcha Passcode: %s" % key)

        # Step6: Fill in the Recaptcha passcode and press verify
        from selenium.webdriver.common.keys import Keys
        self.driver.find_element_by_id("audio-response").send_keys(key.lower())
        self.driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()
        sleep(5)
        self.driver.find_element_by_id("recaptcha-demo-submit").click()
        sleep(10)




