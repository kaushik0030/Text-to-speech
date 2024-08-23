import os
import sys

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    line_number = exc_tb.tb_lineno
    return f"Error occurred in Python script '{file_name}' at line number {line_number}: {str(error)}"

class TTSException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

