import subprocess
import time
import RPi.GPIO as GPIO

gpio_pin = 17

allProcessesCommand = "pgrep -f kodi.bin".split()
runKodiCommand = "kodi".split()
closeKodiCommand = "pkill kodi".split()
openGUICommand = "chvt 7".split()

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getKodiIsRunning():
    try:
        pids = subprocess.check_output(allProcessesCommand).split()
        pids = map(int, pids)
        return len(pids) > 0
    except Exception:
        #TODO logging
        return False


def runKodi():
    try:
        subprocess.check_output(runKodiCommand)
    except Exception:
        #TODO logging
        pass


def closeKodi():
    try:
        subprocess.check_output(closeKodiCommand)
        subprocess.check_output(openGUICommand)
    except Exception:
        #TODO logging
        pass


def update():
    kodiIsRunning = getKodiIsRunning()
    if kodiIsRunning:
        closeKodi()
    else:
        runKodi()


def init():
    while True:
        time.sleep(0.1)
        if GPIO.input(gpio_pin) == False:
            while GPIO.input(gpio_pin) == False:
                time.sleep(1)
            update()


init()
