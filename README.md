# Dream Journaller
## About the .bat file
You can run this bat file to create an executable of program if you have pyinstaller installed through "pip install pyinstaller".

This is not necessary for functionality (you can just run main.py if you have python installed) but is just a little thing I did for convenience.
Of course, always check the bat file before running, and make sure you know what it does.
##
A journaling application written in Python with the Qt GUI library and SQLite3.
##
I am in the process of digitizing my dream journals from the past few years, and thought that having a dedicated program to do so would be helpful, so I made this.

The user is able to enter a title, date, and related tags to an entry and save it under the name of a specific journal to keep things more organized.

The GUI is made in Qt Designer, which generates code from a drag-and-drop interface to use with PyQt, where UI elements can be connected to Python code. SQLite3 is used to store and manage data entered by the user, such as saving, overwriting, deleting, and loading entries.

![image](https://user-images.githubusercontent.com/63424655/130374384-3f346663-0b00-4a23-9e35-cfd651e16aa5.png)
