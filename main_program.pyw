import notifypy
import psutil
import time


def notification(title, text):
    n = notifypy.Notify()
    n.title = title
    n.message = text
    n.send(block=False)

    
warn_p = list(open("config.txt").readlines())

while True:
    battery = psutil.sensors_battery()
    plug = battery.power_plugged
    if plug == True:
        if int(battery.percent) > int(warn_p[0]):
            notification("Unplug charger", ("The Power is at "+str(battery.percent)))    
        time.sleep(15)
    else:
        if int(battery.percent) < int(warn_p[1]):
            notification("Low Battery, Plug-in charger", ("The Power is at "+str(battery.percent)))
       
        time.sleep(15)
