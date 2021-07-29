from flask import Flask, render_template, Response
from Camera_module import PiVideoCamera
import multiprocessing as mp
from ctypes import c_char_p
import os
process_status = list()

app = Flask(__name__)
 
camera0_status = mp.Manager().Value(c_char_p,'free')
camera0 = mp.Queue(1)

@app.route('/')
def index():
    return render_template('index.html',process_status=process_status)
 
def pigen(Camera_module):
        #while True:
    pi_frame = Camera_module.piget_frame(camera0,camera0_status)
    yield (b'--pi_frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + pi_frame + b'\r\n\r\n')

@app.route('/Pi_image')
def Pi_image():
    return Response(pigen(PiVideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=Out_frame')

def pigen(Camera_module):
        #while True:
    Out_frame = Camera_module.piget_frame(camera0,camera0_status)
    return (b'--Out_frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + Out_frame + b'\r\n\r\n')
 
@app.route('/image', methods=['GET'])
def image():
    img = pigen(PiVideoCamera())
    #img = img.encode()
    return img

@app.route('/BlackWhiteOn/<num>', methods=['POST'])
def blackwhite_on(num):
    num = int(num)
    print(111)
    process_status.append(num)
    os.system('cd /home/pi/raspberrypi/i2c_cmd/bin && ./veye_mipi_i2c.sh -w -f daynightmode -p1 0xFE -b 0') #black&white    process_status.append(num)
    return ''

@app.route('/BlackWhiteOff/<num>', methods=['POST'])
def blackwhite_off(num):
    """Get all profiles (JSON)"""
    num = int(num)
    print(111)
    os.system('cd /home/pi/raspberrypi/i2c_cmd/bin && ./veye_mipi_i2c.sh -w -f daynightmode -p1 0xFF -b 0') #color
    if num in process_status:
        process_status.remove(num)# 存在值即为真
    else:
        pass
    return ''




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8616, debug=True)

