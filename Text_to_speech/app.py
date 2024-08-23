from Text_to_speech.exception import TTSException
from flask import Flask,request,render_template
from flask_cors import CORS, cross_origin
from Text_to_speech.components.get_accent import get_accent_message,get_accent_tld
import sys 
from Text_to_speech.components.textToSpeech import TTSapplication



app= Flask(__name__)
CORS(app)

@app.route('/',methods=['GEt'])
@cross_origin()
def home():
    try:
         accent_list= get_accent_message()
         return render_template('index.html',accent_list=accent_list)
    
    except Exception as e:
         raise TTSException(e,sys)

@app.route("/predict",methods=['GET','POST'])
@cross_origin()
def predict():
     try:
          if request == 'POST':
               text = request.json['text']
               accent_input = request.json['accent']
               accent = get_accent_tld(accent_input)
               result = TTSapplication().text2speech(text,accent)
               accent = request.form['accent']
               return {'text':result.decode("utf-8")}
          
     except Exception as e:
          raise TTSException(e,sys)


if __name__ == "__main__" :
     app.run(debug=True,port=5000)
