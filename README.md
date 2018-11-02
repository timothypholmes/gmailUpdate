# gmailUpdate


## gmailUpdate.py
This script updates the number of emails in your gmail account using a raspberry pi GPIO pins, a 74HC595 shift register, and displays new emails on a 7 segment display.


### Automize the script on the raspberry pi to run every minute.

1. Enter the following command into the terminal.
  > crontab -e
  
2. Copy, paste, and exit using control x.
  > * * * * * python /"PATH TO YOUR DIRECTORY"/gmailUpdate.py 
  
  
