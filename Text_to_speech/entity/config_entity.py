from dataclasses import dataclass

import os
from Text_to_speech.constants import *


CURRENT_DIR = os.getcwd()


class   TTSConfig:
    app_name: str = APPLICATION_NAME
    artifacts_dir: str = os.path.join(CURRENT_DIR,app_name, ARTIFACT_DIR_KEY)
    audio_dir : str = os.getpid.join(artifacts_dir,AUDIO_DIR)
    text_dir : str = os.path.join(artifacts_dir,TEXT_DIR)
