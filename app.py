from flask import Flask, render_template, request, abort
import json
import os
import sys
sys.path.append('rpi_ws281x/rpi_ws281x/python')
from ledstrip import *
app = Flask(__name__)

select = ""
stop = ""
@app.route("/")
@app.route("/home" ,methods=['GET','POST'])
def home():
    print("home")
    if request.method == 'POST':
        tag = request.form['favcolor']
        brightness = request.form.get('brigthnessSlider')
        strip=init(int(brightness))
        print("tag ",tag)
        print("brightness",brightness)
        rgb=hex_to_rgb(tag)
        print("waardes",rgb[0])
        bitmapData = convertPics()
        colorWipe(strip,Color(rgb[1],rgb[0],rgb[2]))
        """while(toggle == 1):
            for pics in range(0,len(bitmapData)):
                drawBitmap(strip, bitmapData[pics])
                time.sleep(30/1000.0)"""

        
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/modes" ,methods=['GET','POST'])
def modes():
    global select
    global stop
    strip=init(255)
    #colorWipe(strip,Color(0,0,0))
    print("colorswiped")

    if request.method == 'POST':
        if request.form.get('modeSelector') == None:
            select = select
        else:
            select = request.form.get('modeSelector')
            stop = ""
            modeSelector()
        
        if request.form.get('stop') == None:
            stop = stop
            print("tetten")
        else:
            stop = request.form.get('stop')
            modeSelector()
        
        print("select: ", select, " stop: ", stop)
        
        return render_template('modes.html')
    else:
        return render_template('modes.html')
    
def modeSelector(): 
    global select
    global stop
    
    strip=init(40)
    if select == "theaterChase":
            theaterChase(strip, Color(255,255,255), wait_ms=50, iterations=10)
    elif select == "colorWheel":
        pos = 0
        wheel(pos)
    elif select == "rainbow":
        rainbow(strip, wait_ms=20, iterations=1)
    elif select == "rainbowCycle":
        rainbowCycle(strip, wait_ms=20, iterations=5)
    elif select == "theaterCycleChase":
        theaterChaseRainbow(strip, wait_ms=50)
    elif select == "picture":
        bitmapData = convertPics()
        drawBitmap(strip, bitmapData[pics])

    elif select == "gifs":
        bitmapData = convertPics()
        while(stop != "stop"):
            print("select from modeSelector() : ", select, " stop from modeSelector() : ", stop)
            print("loop")
            for pics in range(0,len(bitmapData)):
                drawBitmap(strip, bitmapData[pics])
                time.sleep(30/1000.0)
                if stop == "stop":
                    break;
    else:
        colorWipe(strip,Color(0,0,0)) 
    
@app.route("/contact")
def contact():
    
    return render_template('contact.html')

@app.route("/foo", methods=['GET','POST']) 
def foo():
    if not request.json:
        abort(400)
    print(request.json)
    return json.dumps(request.json)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0', port=int("80"))
    