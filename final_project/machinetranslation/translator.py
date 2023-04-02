""" This module translates english to french and french to english using watson translator """

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    This function translates english text to french
    """
    msg = ""
    if english_text is None:
        msg = "null input"
    else:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        msg = french_text['translations'][0]['translation']
    return msg

def frenchToEnglish(french_text):
    """
    This function translates french text to english
    """
    msg = ""
    if french_text is None:
        msg = "null input"
    else:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        msg = english_text['translations'][0]['translation']
    return msg
