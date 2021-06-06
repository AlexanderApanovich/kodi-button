# kodi-button

Python script to run/close Kodi on button push

Guide for Raspberry PI 4:
1. Connect button between GPIO 17 and ground  
(you can configure pin in kodi_button.py)  
2. git clone https://github.com/AlexanderApanovich/kodi-button.git
3. cd kodi-button
4. sudo ./install
5. sudo crontab -e  
Add following string: @reboot python /usr/local/bin/kodi_button.py &

Uninstallation guide:
1. sudo crontab -e  
Remove following string: @reboot python /usr/local/bin/kodi_button.py &
2. cd kodi-button
3. sudo ./uninstall
