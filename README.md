# TimelapsePy
Library of simple scripts to automate timelapse photography using a Raspberry Pi. There are several scripts, the "main" script being **timelapse.py**, although user settings should be editted in *usersettings.py*. 
To fully automate the program, add to your cron table with the terminal command: 

<code>crontab -e</code>

Next add the following line to the bottom of the crontab file. **Don't forget to add an *ampersand* at the end of the line**

<code>@reboot python /home/*username*/TimelapsePy/timelapse.py &</code>

### Documentation
I'm still working on creating docstrings, etc., but for those who are so inclined to tinker: you'll probably understand what's going on. It's very simple code.
<a href="https://github.com/benstanfish/TimelapsePy/blob/main/docs/TimelapsePy%20Documentation.pdf">Read the documentation here.</a>
