# Web interactable Led Matrix
## 1. Code -> github
1. git init
2. git add .
3. git remote add origin [branchadress]
4. git commit -am "first launch"
5. git push -u origin master

## 2. Install Flask
[Tutorial how to install flask](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/3)

### Make sure you have python 3 installed:

* sudo apt update
* sudo apt install python3 idle3

Test the install with code:

```python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello world'
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
```

You should get a Hello world on the ip address of your pi port 5000.

## 3. Install rpi_ws281x library
install this library from https://github.com/ssduracell/rpi_ws281x.git

make sure you install the python binding as well.
* sudo pip install rpi_ws281x

Build
As this is just a python wrapper for the library you must first follow the build instructions in the parent directory. When complete, you can build this python wrapper:

* sudo apt-get install python-dev swig
* python ./setup.py build

If you are rebuilding after fetching some updated commits, you might need to remove the build directory first

* rm -rf ./build

Install
If you want to install the library (in a virtualenv or in the system), so that you can import neopixel from anywhere, you need to run:

* python ./setup.py install
Depending on where you are installing, root privileges may be needed (prepend sudo to the install command).

Run a demo
* sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest.py
If you installed the library, there is no need to specify PYTHONPATH:

* sudo python examples/strandtest.py
