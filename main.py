import machine,time
from machine import Pin 
from OTA import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
import machine,time
from machine import Pin

botUp = Pin(7, Pin.IN)
led= Pin(48,Pin.OUT)
def upa():
    firmware_url = "https://github.com/LuisVazpez12/OTA_PRUEBAS/"
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()
def main():
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)

    
while(1):
    if (botUp.value()==1):
        print(upa())
        time.sleep(5)
    else:
        main()
