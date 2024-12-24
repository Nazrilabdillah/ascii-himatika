from flask import Flask,Response
import os
import time
import random
#from PIL import Image as img


def get_file_path(relative_path):
    return os.path.join(os.path.dirname(__file__), "static", relative_path)

def fr(path):
    file = open("bird_text/"+path,"r")
    return file.read()
app = Flask(__name__)
@app.route('/')
def animated_ascii():
    
    return os.path.dirname(__file__) #"iii" + open(get_file_path("i.txt),"r").read()
"""
    def generate():

         while True:
            frame = open("/logo_ascii.txt","r").read()
            ran_num = random.randint(33,40)
            yield f"\033[1;34m{frame}\n"
            time.sleep(5)
            
    return Response(generate(), mimetype='text/plain')
"""
@app.route('/bird')
def index():
    def generate():
        while True:
            for frame in os.listdir("bird_text"):
                 ran_num = random.randint(31,40)
                 yield f"\033[1;{ran_num}m{fr(frame)}\n"
                 time.sleep(0.2)  # jeda antar frame
    return Response(generate(), mimetype='text/plain')
@app.route('/test')
def test():
    return str(os.getcwd())

