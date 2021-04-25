# todo: closeKodi() black screen issue

import subprocess
import time
import RPi.GPIO as GPIO

gpio_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getKodiIsRunning():
    try:
        pids = subprocess.check_output(["pgrep", "-f", 'kodi']).split()
        pids = map(int, pids)
        return len(pids) > 0
    except Exception:
        return False


def runKodi():
    try:
        subprocess.check_output(["nohup", "kodi", "&"])
    except Exception:
        pass


def closeKodi():
    try:
        command = "kodi-send --host=192.168.100.17 --action='Quit'"
        subprocess.check_output([])
    except Exception:
        pass


def update():
    kodiIsRunning = getKodiIsRunning()
    if kodiIsRunning:
        pass
        # closeKodi()
    else:
        runKodi()


def init():
    while True:
        time.sleep(0.2)
        if GPIO.input(gpio_pin) == False:
            pressed_time = time.time()
            while GPIO.input(gpio_pin) == False:
                time.sleep(0.2)
            update()


init()