# gmailUpdate


## gmailUpdate.py
This script updates the number of emails in your gmail account using a raspberry pi GPIO pins, a 74HC595 shift register, and displays new emails on a 7 segment display.

## gmail python library
This project uses the gmail library from charlierguo, the author Charlie Guo, which can be found [here](https://github.com/charlierguo/gmail). This can also be obtained using the command below, 

'''
git clone git://github.com/charlierguo/gmail.git
'''

After downloading place the gmail file that come with the link above along with the python script in the same folder.


### Automize the script on the raspberry pi to run every minute.

1. Enter the following command into the terminal.
  > crontab -e
  
2. Copy, paste, and exit using control x.
  > \* \* \* \* \* python /"PATH TO YOUR DIRECTORY"/gmailUpdate.py 
  
  
