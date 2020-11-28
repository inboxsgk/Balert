import notifypy
import psutil
import time


def notification(title, text):
    n = notifypy.Notify()
    n.title = title
    n.message = text
    n.send(block=False)



warn_p = int(open("config.txt").read())

while True:
    battery = psutil.sensors_battery()
    plug = battery.power_plugged
    if plug == True:
        time.sleep(15)
    else:
        notification("On Battery", "Power Source Disconnected")
        time.sleep(25)
        battery = psutil.sensors_battery()
        plug = battery.power_plugged
        lev = int(battery.percent)
        while plug == False:
            battery = psutil.sensors_battery()
            plug = battery.power_plugged
            if (int(battery.percent) <= warn_p) and (int(battery.percent)!= lev):
                notification("Emergency", ("The Power is at "+str(batter.percent)))
                lev = int(battery.percent)
            time.sleep(10)

        else:
            notification("Charger Connected", "Power source is now restored")
