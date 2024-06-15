<!-- # Facebook BOT -->
![Facebook BOT, by Alvaro624la - logotype.](/logo.png)
## Bot for post on Facebook Groups
This bot **post automatically** for you in every each of your Facebook groups, allowing you to **select witch group** you want to post it or witch you won't.

You can download it here: [DOWNLOAD APP HERE](https://drive.google.com/drive/folders/1TLD9rNhmRasQQvKDkr3XrRPsBRyoBVUq?usp=sharing)

> [!TIP]
> You have to extract it to let the BOT work correctly

This script can run in the background or in parallel. That's the difference between Selenium and Pyautogui, which was the first thing I used on my first Bot project.

For the moment, only can be used to text, links, etc. posts, no for multimedia stuff.

> [!NOTE]
> English version now available! Since v.2.1.0.

## Index
- [Exporting to an executable (.exe) and running it](#how-to-export-to-executable-exe-and-run-it)
- [Accessing the executable project](#how-access-to-this-executable-proyect)
- [Technical details](#technical-details)
- [Future development](#developing)

## How to export to executable [.exe] and run it
### 1. Virtual Studio Code
You have to **open the project folder in your VSC**, not only the file project. 

In this case: 
- ../Facebook BOT/ES/
- ../Facebook BOT/EN/

### 2. Pyinstaller tool
Install cx-Freeze in your terminal:
- ```pip install pyinstaller```

Build the complete executable folder
- ```pyinstaller py_file_name.py``` 

Example: pyinstaller robot_fb.py

## How access to this executable proyect?
- Enter into "**dist/py_file_name**" folder
- Click on **py_file_name.exe** file
- Enjoy!

## Technical details
### Requeriments:
- Chrome Driver: Go to https://chromedriver.chromium.org/downloads to download the correct ChromeDriver version, equivalent to your Google Chrome version.

### Extra requeriments:
- Google Chrome

### Tools and Python Modules:
- **Selenium**: A tool for automating web browsers. It provides a way for developers to write scripts in various programming languages to automate interactions with web applications. I personally used Python.
- **webdriver_manager**: To simplify management of binary drivers for different browsers. To not to repeat all these steps (download the chromedriver binary...unzip it somewhere on your PC...set the path to this driver) again and again every time a new version of the driver is released.
- **re**: Module in Python for regular expressions. It provides a set of functions that allows us to search a string for a match or replace matches with other strings. I use this module to find all the group links.
- **time**: A time module in Python that provides various time-related functions. I used that to have some time between some process to pause the script execution to production or for me as a developer to make the tests. Ex: ```time.sleep(5)```

## Done:
- Get all your group links.
- Show all the groups with their name and image, and select in what group you want to post or what you don't.

## Developing:
- Maybe improve the way you can write the post.
- Post images, videos, and more. Not only text.

<!--
!['s Stats](https://github-readme-stats.vercel.app/api?username=Alvaro624la&theme=vue-dark&show_icons=true&hide_border=true&count_private=true)
!['s Streak](https://github-readme-streak-stats.herokuapp.com/?user=Alvaro624la&theme=vue-dark&hide_border=true)
-->


<!--
SINTAXIS README.MD - GUIA:
https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings

https://markdownlivepreview.com/
-->