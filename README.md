# Laptop Battery Checker and Notifier

This Python script checks your laptop's battery status and plays sounds based on specific conditions. It can play a sound when the battery is fully charged (100%) and when battery saver mode is enabled.

## Prerequisites

Before running the script, you need to install the following Python libraries:

- [psutil](https://pypi.org/project/psutil/): A cross-platform library for accessing system details, including battery information.
- [pydub](https://pypi.org/project/pydub/): A library for audio file manipulation.

You can install these libraries using `pip`:

```bash
pip install psutil pydub
```

## Usage
Clone or download this repository to your local machine.

1) Place your sound files in the same directory as the Python script and update the file paths in the script as follows:

```python
charged_sound = "charged_sound.mp3"
battery_saver_sound = "battery_saver_sound.mp3"
```
2) Replace "charged_sound.mp3" and "battery_saver_sound.mp3" with the actual file paths of your sound files.

3) Run the script using the following command:
```
python battery_checker.py
```
4) The script will continuously check the battery status and play sounds when the conditions are met.
5) To stop the script, press `Ctrl + C` in the terminal.

## Customization
You can customize the script by adjusting the conditions for playing sounds, changing the sound files, or modifying the check frequency (default is every 60 seconds) by updating the while loop in the script.
```
# Main loop to continuously check battery status
while True:
    check_battery_status()
    time.sleep(60)  # Check every 60 seconds
```

    
