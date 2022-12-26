import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator( '{apikey}')
language_translator = LanguageTranslatorV3 (
    version=' {version}',
    authenticator=authenticator
)
language_translator.set_service_uri('https://api.us-south.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    translation = language_translator.translate(
    text='Hello, how are you today?' model_id='en-fr') .get_result ()
    frenchText=json. dumps (translation, indent=2,
    return frenchText

def frenchToEnglish(frenchText):
    translation = language_translator. translate
    text=frenchText, model_id='en-fr').get_result()
    englishText-json. dumps(translation, indent-2, ensure_ascii-False)
    return englishText