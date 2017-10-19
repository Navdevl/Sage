# Sage
Sage - A Discord Bot to Add/View/Delete Reminders. 

# Requirements
Python 3.5 or more

# Installation
### Installing Python 3
Go to https://www.python.org/downloads/ and download the package that matches required version.
### Installing Python Packages
Run [install.sh](https://github.com/Navdevl/Sage/blob/master/install.sh) from terminal. It will install all the necessary packages. If you wanted to manually install packages in any virtual environment, you can check the requirements.txt file to see the necessary packages with minimum version needed.

# Configuration
- Create a account in http://discordapp.com
- Go to https://discordapp.com/developers/applications/me
- Click on **New App**
- Fill all the details and create a new app
- Create a **Bot User**
- Copy the token
- Configure the token value in [config.py](https://github.com/Navdevl/Sage/blob/master/config.py)

# Invite the App to Server
Go to https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=1

# Usage
- **Initialize the channel for Sage to send reminders.**
Type `!init` on the channel where you want the bot to send messages
- **Add reminder to Sage.**
Type `!remind to do something at HH:MM(am|pm)`
- **Ask Sage to list all the reminders**
Type `!list` to get the list of reminders with its unique id.
- **Delete a reminder from Sage's list**
Type `!delete uid` to delete the remider

# License
MIT License

Copyright (c) 2017 Nav_devl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.