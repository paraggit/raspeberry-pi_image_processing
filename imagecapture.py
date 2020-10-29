from time import sleep
from picamera import PiCamera
from datetime import datetime
#from config.env import VID_DIR, IMAGE_DIR

VID_DIR="/var/www/html/vid/"
IMAGE_DIR="/var/www/html/images/"

def capture():
    """
    """
    fileformat="%d%m%y%H%M%S"
    camera = PiCamera()
    camera.resolution = (2048,1536)
    camera.start_preview()
    sleep(2)
    dt = datetime.now()
    filename="{}/{}.jpg".format(IMAGE_DIR,dt.strftime(fileformat))
    camera.capture(filename)
    camera.stop_preview()


if __name__ == "__main__":
    capture()
