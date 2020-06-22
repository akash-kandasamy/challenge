import psutil
import time
import winsound as wins

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)

    print('battery ' +str(battery.percent) + '%')
    if battery.percent < 30:
        print('put charger')
        wins.Beep(2500,100)
    elif plugged == True and battery.percent > 90:
        print('overflow and plug out')
        wins.Beep(2500,100)

    time.sleep(2)


