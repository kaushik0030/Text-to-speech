from Text_to_speech.exception import TTSException
from Text_to_speech.logger import logging

import sys 

def get_accent_tld(user_input):
    try:
        accent_input = {
            'Australian':'com.au',
            'British':'com.uk',
            'Canadian':'com.ca',
            'Irish':'com.ie',
            'Indian':'com.in',
            'New Zealand':'com.nz',
            'South African':'com.za',
            'American':'com.us',

        }
        tld = accent_input.get(user_input)
        return tld
    except Exception as e:
        raise TTSException(e,sys)



def get_accent_message():
    try :
        accent = ['Australian', "South Africa" ,"British","Indian","Canadian","Irish","Spanish"]

        return accent
    except Exception as e:
        raise TTSException(e,sys)from e 
