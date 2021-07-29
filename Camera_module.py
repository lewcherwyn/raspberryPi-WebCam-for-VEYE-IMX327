# camera.py
import cv2
import time
import multiprocessing as mp
import D_mipicamera as Dcam
 
def align_down(size, align):
    return (size & ~((align)-1))

def align_up(size, align):
    return align_down(size + align - 1, align) 


class PiVideoCamera(object):
    thread = None  # background thread that reads frames from camera
    pijpeg = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera


    def initialize(self,camera0,camera0_status):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
            # start background frame thread
        if camera0_status.value == 'free':
            PiVideoCamera.thread = mp.Process(target=self.pi_thread,args=(camera0,camera0_status,))
            PiVideoCamera.thread.start()
            camera0_status.value = 'busy'
        else:
            pass
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def piget_frame(self,camera0,camera0_status):
        #print(click_time)
        self.initialize(camera0,camera0_status)
        self.pijpeg = camera0.get()
        return self.pijpeg


    #@classmethod
    def pi_thread(self,camera0,camera0_status):
        click_time = time.time()
        #print(click_time)
        #print(time.time())
        #print(camera0_status)
        camera = Dcam.mipi_camera()
        print("Open camera...")
        camera.init_camera()
        height = int(align_up(1080, 16))
        width = int(align_up(1920, 32))
        while True:
            frame = camera.capture(encoding = 'i420')
            image = frame.as_array.reshape(int(height * 1.5), width)
            image = cv2.cvtColor(image, cv2.COLOR_YUV2BGR_I420)
            image = cv2.resize(image,(480,270),interpolation=cv2.INTER_CUBIC)
                # We are using Motion JPEG, but OpenCV defaults to capture raw images,
                # so we must encode it into JPEG in order to correctly display the
                # video stream.
                
            _, pijpeg = cv2.imencode('.jpg', image)
            pijpeg = pijpeg.tobytes()

            camera.release_buffer(frame)
            del frame
            if camera0.empty() is True:
                camera0.put(pijpeg)
                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                #print(time.time() - click_time.value)
                #print(time.time() - click_time)
                
                # print("Stop preview...")
                 # camera.stop_preview()
            if time.time() - click_time > 5:
                print("Close camera...")
                camera.close_camera()
                break
        #print("done")
        camera0_status.value = 'free'
        #print(camera0_status)
    # 对于 python2.7 或者低版本的 numpy 请使用 jpeg.tostring()


