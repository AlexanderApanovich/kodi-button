# kodi-button

Python script to run/close Kodi on button push

Guide for Raspberry PI 4:
1. Connect button between GPIO 17 and ground
2. git clone https://github.com/AlexanderApanovich/kodi-button.git
3. cd kodi-button
4. sudo ./install
5. sudo crontab -e
Add following string:
@reboot python /bin/kodi_button.py &

Uninstallation guide:
1. cd kodi-button
2. sudo ./uninstall
