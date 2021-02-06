from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello python eka'

@app.route('/raspberrypi')
def raspberrypi():
    return 'Raspberry PI page here page here.. eka!'

@app.route('/arduino')
def arduino():
    return 'Arduino page here.. eka!'

@app.route('/arduino/relay')
def arduinorelay():
    return 'Arduino relay page here.. eka!'

@app.route('/adafruit')
def adafruit():
    return 'Adafruit page here.. eka!'

@app.route('/odroid')
def odroid():
    return 'Odroid page here.. eka!'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.1.1', port=5000)
