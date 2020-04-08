# Uses Python 3.8.2 64bit
# Home control hub prototype Alpha V0.5
# basic function and networking test

    # Imports

from tkinter import *
    # Imports the full tkinter library, NB: false posative error, linter notes that not all of tkinter's methods and functions are not used

from tkinter import filedialog, Text, messagebox           
    # Explicitly imports filedialog and Text from the tkinter library,
    # filedialog allows tkinter to call OS classes,
    # Text allows text to be shown over multiple lines

import tkinter as tk
    # Sets tkinter to the veriable tk

import os 
    # Imports the Operating system interfacing library

import csv 
    # imports the comma seperated value parsing library

import hashlib 
    # imports the hasing library to form the encryption key


Roost = tk.Tk() 
    # Sets tkinter's TK Function to the Roost constant


class interfacing:

    def __init__(self):
        print('')
    
    def newUser(self, userName, userPassword):
        # New user function
        print('This is a test function')

    def existingUser(self, userName, userPassword):
        # Existing User Function

        for Widget in deviceList.winfo_children():
            Widget.destroy()
        # stops duplicate entries from loops 

        userName = str(userName)
        # Holds the passed userName variable
    
        fileType = str('.txt')
        # Holds the file type extention for concaternation

        userFile = userName + fileType
        # Concatenates the userName wuth a .txt file extension to open the user's file

        userPassword = userPassword
        # Holds the passed userPassword variable

        userFileExists = os.path.isfile(userFile)
        # Returns True(0) if file exists

        if userFileExists == True:
        # Checks if the user file exists

            with open (userFile , newline = '') as temp:
            # Opens user file

                userConfigListReader = csv.reader(temp, deliminator = ",")
                # Loads in the user file as a comma seoerated value with the deliminator of a comma

                userConfig = list(userConfigListReader)
                # Formats the imported file as a multi-layerd list with the first column as the first layer then second [1st value][2nd value]

            if userPassword == userConfig[1][0]:
                print('Debug: Password Matched')
                # checks for a matching password and logs a posative to console if true

                for device in userConfig:
                # Iterates the user file for device lists, IP addresses and Ports

                    if i == userName or userPassword: # NB: false posative error, variable used in the loop

                        skip = True
                        # Skips entry if userName or userPassword returns true

                        continue
                        # Skips over user name and password to stop them being added 

                    if skip:
                        skip = False
                        continue
                        # Resets skip command if it was used

                    label = Label(deviceList, text=device, bg="grey")
                    label.pack()
                    # Adds returned device to the user interface

                return

            else:
                messagebox.showinfo('Sorry', 'Password Incorrect, Please try again')
                # Opens up a popup box to advise of an incorrect password

                print('Debug: Password incorrect')
                # Console debug message for incorrect password

                return
                       
        else:
            messagebox.showinfo('Sorry', 'Username is not found, please try again')
            # Opens up a popup if user file does not match
            
            print('User Name incorrect')
            # Console debug for missing user file
            return

def roostHelp():
    messagebox.showinfo('Help', 'For help and advice please visit: https://github.com/PeterFlint/Roost')
        # Opens a popup containing help website

def closeWindow ():
    Roost.destroy()
        # This Function closes the tkinter window correctly

inter = interfacing()
    # Sets the interfacing class to inter

roostHelp = Button(Roost, text = 'Help', font=("Helvetica", 12, "bold"), justify='center', width=20, height = 3, fg = 'red', bd = 5, 
relief = RAISED, command = roostHelp)
roostHelp.grid(row = 0, column = 0, columnspan = 4) 
    # Creates and places the help button that calls roostHelp when pressed

endRoost = Button(Roost, text = 'Time to leave the Roost?', font=("Helvetica", 12, "bold"), justify='center', width=20, height = 3, fg = 'red', bd = 5, 
relief = RAISED, command = closeWindow)
endRoost.grid(row = 0, column = 8, columnspan=4, sticky = W)
    # Creates and places the quit button that calls closeWindow when pressed

deviceList = Frame(Roost, height=384, width=700, bg='white')
deviceList.grid(row=1, column=0, sticky='nsew', columnspan=10)
    # Creates and places a object that can hold objects

userNamelabel = Label(Roost, text = 'User Name:', font=("Helvetica", 12), justify='center', width=20, height = 3, fg = 'black', bd = 5)
userNamelabel.grid(row = 2, column = 0, sticky = E)
    # Creates and places an object to display text

userPasswordlabel = Label(Roost, text = 'Password:', font=("Helvetica", 12), justify='center', width=20, height = 3, fg = 'black', bd = 5)
userPasswordlabel.grid(row = 3, column = 0, sticky = E)
    # Creates and places an object to display text

userNameEntry = Entry(Roost)
userNameEntry.grid(row = 2, column = 1)
#userName = userNameEntry
    # Creates and places a text input and places
    #  into userName variable

userPasswordEntry = Entry(Roost)
userPasswordEntry.grid(row = 3, column = 1)
#userPassword = userPasswordEntry
    # Creates and places a text input and places into userPassword variable

exsistingUser = Button(Roost, text = 'Log In',font=("Helvetica", 12, "bold"), justify='center', width=20, height = 3, fg = 'green', bd = 5, 
                                relief = RAISED, command = inter.existingUser(userNameEntry, userPasswordEntry))
exsistingUser.grid(row = 2, column = 8, columnspan = 4)
    # Creates and places the log in button that calls existinguser function

newUser = Button(Roost, text = 'Create New Account',font=("Helvetica", 12, "bold"), justify='center', width=20, height = 3, fg = 'blue', bd = 5, 
                                relief = RAISED, command = inter.newUser(userNameEntry, userPasswordEntry))
newUser.grid(row = 3, column = 8, columnspan = 4)
    # Creates and places the create new user button and calls newUser when pressed

userNamelabel = Label(Roost, text = 'User Name:', font=("Helvetica", 12), justify='center', width=20, height = 3, fg = 'black', bd = 5)
userNamelabel.grid(row = 2, column = 0, sticky = E)
    # Creates and places an object to display text

userPasswordlabel = Label(Roost, text = 'Password:', font=("Helvetica", 12), justify='center', width=20, height = 3, fg = 'black', bd = 5)
userPasswordlabel.grid(row = 3, column = 0, sticky = E)
    # Creates and places an object to display text


Roost.geometry("700x768")
    # Sets the window size in pixels
Roost.title('Roost')
    # Sets the title of the window

Roost.mainloop()
    # runs tkinter as a infinate loop