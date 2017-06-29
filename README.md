# WBCodeTest
WB CODE TEST 


This code was written by Randy Mazin as a test for WB Games. This module is written in Python.

```
** Requirements **
- Python 2.7.x
```

Simply clone the repository and run the script from a terminal or command window from the directory in which this script is stored with the following command:

```shell

python playerProfile.py

```

The Script will prompt to enter player personal information into the window, it will proceed to run an example MUD styel minigame which will create and log the profile as well as a couple of achievements for the user based on the user's input.  At the end it will show what would essentially be the user's leaderboard information.

The code will create a JSON file with the profile information in the same directory as the python script.  The goal would be that this JSON is the beginnings of what a REST API would output. In this case a "user profile".

For this particular information there wouldn't necessarily be a build and deployment process since it's only a simple script/applicaiton and does not require a server to run.  It's not designed as a web application and currently does not have a GUI.
