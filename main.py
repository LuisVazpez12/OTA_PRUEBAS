from ota import OTAUpdater
from WIFI import SSID, PASSWORD
import machine,time
from machine import Pin 

firmware_url ="https://raw.githubusercontent.com/LuisVazpez12/OTA_PRUEBAS/main"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()
led= Pin(2,Pin.OUT)
led.on()
time.sleep_ms(800)
led.off()
time.sleep_ms(800)

