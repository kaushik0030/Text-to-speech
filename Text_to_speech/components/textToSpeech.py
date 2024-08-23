import os 
import sys 



from Text_to_speech.exception import TTSException
from Text_to_speech.logger import logging
from Text_to_speech.entity.config_entity import TTSConfig
from gtts import gtts
import base64
import io


from Text_to_speech.constants import TEXT_FILE_NAME,CURRENT_TIME_STAMP
class TTSapplication():
    def __init__(self, app_config=TTSConfig())-> None:
        try:
            self.app_config = app_config
            self.artifacts_dir = app_config.artifacts_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e :
            raise TTSException(e,sys) 
        
    def text2speech(self,text,accent):
        try:
            text_filename = TEXT_FILE_NAME
            text_file_path = os.path.join(self.text_dir, TEXT_FILE_NAME)
            with open(text_file_path, 'a+') as file:
                file.write(f'\n{text}')

            # create object for gtts 
            tts = gtts(text=text, lang='en',tld='acent',slow=False)

            file_name = f"converted_file(CURRENT_TIME_STAMP).mp3"
            audio_path = os.path.join(self.audio_dir, file_name)

            tts.save(audio_path)

            with open(audio_path,'rb') as file:
                my_strings = base64.b64encode(file.read())

            return my_strings
        
        except Exception as e :
            raise TTSException(e,sys)
            