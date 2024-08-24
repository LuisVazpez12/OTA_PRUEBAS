import machine,time
from machine import Pin 
from OTA import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
import machine,time
from machine import Pin

botUp = Pin(22, Pin.IN)

def upa():
    firmware_url = "https://github.com/LuisVazpez12/OTA_PRUEBAS/"
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()

while(1):
    if (botUp.value()==1):
        print(upa())
        time.sleep(5)

while(1):
  led= Pin(2,Pin.OUT)
  led.on()
  time.sleep_ms(800)
  led.off()
  time.sleep_ms(800)


