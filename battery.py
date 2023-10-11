import psutil
from pydub import AudioSegment
from pydub.playback import play
import time

# Path to your sound files
charged_sound = "charged_sound.mp3"
battery_saver_sound = "battery_saver_sound.mp3"


# Function to check the battery status
def check_battery_status():
    battery = psutil.sensors_battery()
    if battery.percent == 100:
        print("Your laptop is now fully charged.")
        play(AudioSegment.from_mp3(charged_sound))
    elif battery.power_plugged and battery.percent < 100:
        print(f"Your laptop is charging ({battery.percent}%).")
    else:
        print(f"Your laptop battery is at {battery.percent}%.")

    if battery.power_save:
        print("Battery Saver Mode is enabled.")
        play(AudioSegment.from_mp3(battery_saver_sound))


# Main loop to continuously check battery status
while True:
    check_battery_status()
    time.sleep(60)  # Check every 60 seconds
