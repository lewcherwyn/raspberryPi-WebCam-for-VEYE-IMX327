from flask import Flask, render_template, Response
import requests
process_status = list()

app = Flask(__name__)
 


@app.route('/')
def index():
    return render_template('index2.html',process_status=process_status)
 

@app.route('/Pi_image')
def Pi_image():
    img = requests.get("http://0.0.0.0:8616/image")
    #img = img.decode()
    print(111)
    return Response(img,mimetype='multipart/x-mixed-replace; boundary=pi_frame')

@app.route('/BlackWhiteOn/<num>', methods=['POST'])
def blackwhite_on(num):
    num = int(num)
    process_status.append(num)
    num = str(num)
    add = "http://0.0.0.0:8616/BlackWhiteOn/"
    ip = add + num
    requests.post(ip)
    return ''

@app.route('/BlackWhiteOff/<num>', methods=['POST'])
def blackwhite_off(num):
    """Get all profiles (JSON)"""
    num = str(num)
    add = "http://0.0.0.0:8616/BlackWhiteOff/"
    ip = add + num
    requests.post(ip)
    num = int(num)
    if num in process_status:
        process_status.remove(num)# 存在值即为真
    else:
        pass
    return ''



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8626, debug=True)

