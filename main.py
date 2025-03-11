import customtkinter as ctk
import tkinter as tk
import hashlib
import pandas as pd
import requests
import time
from PIL import Image
from PIL import UnidentifiedImageError
import io
import os

# Hello :D #

LoginSuccess = False
NewloginVariable = False
IWantMoreInfoNOW = False
fail = False

Movelist = []

# Assume all the buttons have the same comments #


def button1():
    global fail
    PokeInput()
    if fail is False:
        print(fail)
        # Creates the URL for the pokemon #
        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        # Uses requests to get a JSON file #
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        # Creates a JSON file out of the response #
        JsonFile = poke_url_response.json()
        # Pulls values from the JSON file #
        image_url = JsonFile['sprites']['front_default']
        name = JsonFile['name']
        # if 678 is input then the amalgamate image is shown #
        try:
            # This takes the image from the json file #
            image_response = requests.get(image_url)
            # Renders the image #
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            # Creates the image #
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))
            # Changes the label to be the image #
            listofvalues[0].configure(image=poke_image)
        except UnidentifiedImageError:  # 678 error #
            print('678 error')
            ErrorImage = Image.open('amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage,
                                      size=(100, 100))
            listofvalues[0].configure(image=poke_image)
        # Changes the name label to the selected pokemons name #
        Poke1Label.configure(text=name)

        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke1'] = name
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)


def button2():
    global fail
    PokeInput()
    if fail is False:

        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        JsonFile = poke_url_response.json()
        image_url = JsonFile['sprites']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image_Error = ctk.CTkImage(light_image=poke_image_data,
                                            size=(100, 100))
            listofvalues[1].configure(image=poke_image_Error)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[1].configure(image=poke_image)

        Poke2Label.configure(text=name)

        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke2'] = name
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke2Label.configure(text=name, text_color='red')


def button3():
    global fail
    PokeInput()
    if fail is False:
        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        JsonFile = poke_url_response.json()
        image_url = JsonFile['sprites']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))

            listofvalues[2].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[2].configure(image=poke_image)

        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke3'] = name
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke3Label.configure(text=name, text_color='red')


def button4():
    global fail
    PokeInput()
    if fail is False:

        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        JsonFile = poke_url_response.json()
        image_url = JsonFile['sprites']['front_default']
        name = JsonFile['name']
        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))

            listofvalues[3].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[3].configure(image=poke_image)

        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke4'] = name
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke4Label.configure(text=name, text_color='red')


def button5():
    global fail
    PokeInput()
    if fail is False:

        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        JsonFile = poke_url_response.json()
        image_url = JsonFile['sprites']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))
            listofvalues[4].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[4].configure(image=poke_image)

        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke5'] = name
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke5Label.configure(text=name, text_color='red')


def button6():
    global fail
    PokeInput()
    if fail is False:
        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        JsonFile = poke_url_response.json()
        image_url = JsonFile['sprites']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))
            listofvalues[5].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[5].configure(image=poke_image)

        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke6'] = name
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke6Label.configure(text=name, text_color='red')


# End of button functions #


def LoginButton():
    global Username, Password, LoginSuccess, data
    # Grabs the input from the input box #
    Username = UsernameEntry.get()
    # Clears the username input #
    UsernameEntry.delete(0, tk.END)
    # Grabs the password entry #
    Password = PasswordEntry.get()
    # Clears the password entry #
    PasswordEntry.delete(0, tk.END)
    # Encrypts the password to check in csv #
    Password = hashlib.sha256(Password.encode('utf-8')).hexdigest()
    # Checks and loads the CSV #
    with open('passwords.csv', 'r') as data:
        data = pd.read_csv(data)
        Username2 = data.loc[data['username'] == Username]
        Password2 = Username2.loc[data['password'] == Password]
    if Password2.empty is True:
        print('Failure')
    else:
        LoginSuccess = True
        Login.destroy()


def EnterNewData():
    NewUsername = UsernameNewEntry.get().strip()
    NewUsername = NewUsername.lower().strip()
    NewPassword = PasswordNewEntry.get()
    if NewPassword != "":
        NewPassword = hashlib.sha256(NewPassword.encode('utf-8')).hexdigest()
    PasswordNewEntry.delete(0, tk.END)
    UsernameNewEntry.delete(0, tk.END)

    # Professor Oak has made a donation! ( Its to show features of my code ) #
    d = {'username': [NewUsername], 'password': [NewPassword],
         'poke1': ['pikachu'],
         'poke2': ['mew'],
         'poke3': ['mewtwo'],
         'poke4': ['meowstic-male'],
         'poke5': ['charizard'],
         'poke6': ['eevee']
         }

    data = pd.DataFrame(data=d)

    with open('passwords.csv', 'r') as file:
        LoadedData = pd.read_csv(file)
        df = pd.concat([LoadedData, data], ignore_index=True)
        UserNameExists = LoadedData.loc[LoadedData['username'] == NewUsername]
        # Checks if both inputs are empty #
        if UserNameExists.empty and NewUsername and NewPassword:
            # Adds the new login #
            df.to_csv('passwords.csv', index=False)
            StatusNewLogin.configure(text="Success!",
                                     text_color='green',
                                     font=('ariel', 25, 'bold'))
            StatusNewLogin.update()
            time.sleep(3)
        # If username and password has text in it #
        elif NewUsername != "" and NewPassword != "":
            StatusNewLogin.configure(text="Username in use!",
                                     text_color='green',
                                     font=('ariel', 20, 'bold'))
            StatusNewLogin.update()
        else:
            # Code is not happy with you #
            for i in range(1, 20):
                if i % 2 == 0:
                    SirenColor = 'red'
                else:
                    SirenColor = 'blue'
                StatusNewLogin.configure(text="STOPPPP ITTTTTT",
                                         text_color=SirenColor,
                                         font=('ariel', 25, 'bold'))
                StatusNewLogin.update()
                time.sleep(0.1)
            StatusNewLogin.configure(text="Input some text!",
                                     text_color='purple',
                                     font=('ariel', 20, 'bold'))
            StatusNewLogin.update()


def NewLogin():
    # This entire thing is just to make a window #
    global StatusNewLogin, UsernameNewEntry, PasswordNewEntry, NewLogin
    NewLogin = ctk.CTkToplevel()
    NewLogin.attributes("-topmost", True)
    NewLogin.resizable(0, 0)

    # Bg colors #
    frame_left = ctk.CTkFrame(NewLogin, fg_color="red")
    frame_left.grid(row=0, column=0, sticky="nsew", rowspan=5)

    frame_right = ctk.CTkFrame(NewLogin, fg_color="white")
    frame_right.grid(row=0, column=1, sticky="nsew", rowspan=5)

    # Lower the frames #
    frame_left.lower()
    frame_right.lower()

    # Modules #
    UsernameNewLabel = ctk.CTkLabel(NewLogin,
                                    text="Enter New Username:",
                                    bg_color='red',
                                    text_color='white',
                                    font=('ariel', 20, 'bold'))
    PasswordNewLabel = ctk.CTkLabel(NewLogin,
                                    text="Enter New Password:",
                                    bg_color='red',
                                    text_color='white',
                                    font=('ariel', 20, 'bold'))
    StatusNewLogin = ctk.CTkLabel(NewLogin,
                                  width=40,
                                  height=20,
                                  text="Input A New Username / Password",
                                  bg_color='white',
                                  text_color='red',
                                  font=('ariel', 15, 'bold'))

    UsernameNewEntry = ctk.CTkEntry(NewLogin, bg_color='white')
    PasswordNewEntry = ctk.CTkEntry(NewLogin, bg_color='white')

    EnterNewDataButton = ctk.CTkButton(NewLogin,
                                       text="Enter New Data",
                                       command=EnterNewData,
                                       bg_color='white',
                                       font=('ariel', 15, 'bold'),
                                       fg_color='red')

    # Grid Modules #
    # Labels
    UsernameNewLabel.grid(row=0, column=0, pady=20, padx=30)
    PasswordNewLabel.grid(row=1, column=0)

    # Inputs #
    UsernameNewEntry.grid(row=0, column=1, pady=20)
    PasswordNewEntry.grid(row=1, column=1)

    # Buttons #
    EnterNewDataButton.grid(row=2, column=1, pady=20)
    StatusNewLogin.grid(row=3, column=0)


def PokeInput():
    global fail, Selection
    Selection = PokeInputText.get('1.0', tk.END)
    PokeInputText.delete('1.0', tk.END)
    if Selection.strip() == "":
        print('Failure')
        fail = True
    else:
        print(Selection)
        try:
            url = "https://pokeapi.co/api/v2/pokemon/" + Selection
            url = url.strip()
            url_response = requests.get(url)
            if url_response.status_code != 200:
                TutorialLabel.configure(text='Invalid Pokemon',
                                        text_color='purple',
                                        font=('ariel', 30, 'bold'))
                TutorialLabel.update()
                time.sleep(3)
                TutorialLabel.configure(text='Pick A Pokemon To Replace',
                                        text_color='white',
                                        font=('ariel', 20, 'bold'))
                TutorialLabel.update()
                fail = True
            else:
                fail = False
        except KeyError:
            print('ERROR')
            fail = True


def MoreInfoPls():  # My variable names are out the window. Im tired :3 #
    global SelectBox, PokeActualImage, AccNameLabel, MoveLabel, SelectLabel
    Info = ctk.CTkToplevel()
    Info.resizable(0, 0)  # Dont even try resizing #
    Info.attributes('-topmost', True)

    # Colored frames for the UI #
    frame_left = ctk.CTkFrame(Info, fg_color="red")
    frame_left.grid(row=0, column=0, sticky="nsew", rowspan=50)

    frame_middle = ctk.CTkFrame(Info, fg_color="white")
    frame_middle.grid(row=0, column=1, sticky="nsew", rowspan=50)

    frame_right = ctk.CTkFrame(Info, fg_color="red")
    frame_right.grid(row=0, column=2, sticky="nsew", rowspan=50)

    # Lower the frames #
    frame_left.lower()
    frame_middle.lower()
    frame_right.lower()

    for i in range(1, 5):
        Info.rowconfigure(i)

    # Modules #
    SelectLabel = ctk.CTkLabel(Info, text='Input Pokemon Here!',
                               font=('arial', 20, 'bold'),
                               bg_color='red',
                               text_color='white')

    SelectLabel.grid(row=0, column=0, pady=10)

    SelectBox = ctk.CTkEntry(Info, width=200, height=5, bg_color='white')
    SelectBox.grid(row=0, column=1, padx=20)

    SelectButton = ctk.CTkButton(Info, text='Input!',
                                 command=Dictionary,
                                 bg_color='red',
                                 fg_color='white',
                                 text_color='red',
                                 font=('arial', 20, 'bold'))

    SelectButton.grid(row=0, column=2)

    # Pre Labels ( Before updates) #

    # Image of selection #
    PokeLabelImage = ctk.CTkLabel(Info,
                                  text='Pokemon Image:',
                                  bg_color='red',
                                  font=('arial', 20, 'bold'),
                                  text_color='white')
    PokeLabelImage.grid(row=1, column=0, pady=30)

    PokeActualImage = ctk.CTkLabel(Info,
                                   text="IMAGE HERE",
                                   font=('arial', 20, 'bold'),
                                   bg_color='white',
                                   text_color='red')
    PokeActualImage.grid(row=1, column=1)

    # Name of Selection #
    PokeNameLabel = ctk.CTkLabel(Info, text="Name Of pokemon",
                                 font=('arial', 20, 'bold'),
                                 bg_color='red',
                                 text_color='white')
    PokeNameLabel.grid(row=2, column=0, pady=20)
    AccNameLabel = ctk.CTkLabel(Info, text='')
    AccNameLabel.grid(row=2, column=1)

    # MoveList of the pokemon #
    scrollable_frame = ctk.CTkScrollableFrame(Info,
                                              orientation="horizontal",
                                              bg_color='white', height=50)
    scrollable_frame.grid(row=3, column=1, rowspan=5)

    MoveLabel = ctk.CTkLabel(scrollable_frame,
                             text="",
                             font=('ariel', 15, 'bold'))
    MoveLabel.grid(row=3, column=1)

    MoveLabelFirst = ctk.CTkLabel(Info,
                                  text="Moveset:",
                                  font=('arial', 20, 'bold'),
                                  text_color='white',
                                  bg_color='red')
    MoveLabelFirst.grid(row=3, column=0, pady=20)


def Dictionary():
    Input = SelectBox.get()
    if Input.strip() != "":
        # Makes the URL and gets the JSON
        url = "https://pokeapi.co/api/v2/pokemon/" + Input
        url = url.strip()
        url_response = requests.get(url)
        # Checks if the server exists #
        if url_response.status_code == 200:
            JsonFile = url_response.json()

            PokemonName = JsonFile['name']
            # Puts the name into the disctionary #
            AccNameLabel.configure(text=PokemonName,
                                   text_color='red',
                                   bg_color='white',
                                   font=('arial', 20, 'bold'))

            try:
                # Renders image and puts in the dictionary #
                PokemonSprite = JsonFile['sprites']['front_default']
                PokemonSprite = requests.get(PokemonSprite)
                poke_image_data = Image.open(io.BytesIO(PokemonSprite.content))
                poke_image = ctk.CTkImage(light_image=poke_image_data,
                                          size=(100, 100))
                # Puts the image into the label #
                PokeActualImage.configure(image=poke_image, text="")
            except UnidentifiedImageError:  # 678 error #
                ErrorImage = Image.open('amalgamate.png')
                poke_image = ctk.CTkImage(light_image=ErrorImage,
                                          size=(100, 100))
                PokeActualImage.configure(image=poke_image, text="")

            # Also places the moves into a scrollable frame #
            Moves = JsonFile['moves']
            for move in Moves:
                move_name = move['move']['name']
                Movelist.append(f"'{move_name}'")
            MoveLabel.configure(text=Movelist)
            MoveLabel.update()
        else:
            SelectBox.delete(0, tk.END)
    else:
        print("Fail")


def MenuPoke():
    try:
        for i in range(0, 6):
            url = "https://pokeapi.co/api/v2/pokemon/"
            url2 = listofvalues[i].strip()
            poke_url = url + url2
            poke_url_response = requests.get(poke_url)
            poke_url_response.raise_for_status()
            JsonFile = poke_url_response.json()
            image_url = JsonFile['sprites']['front_default']
            image_response = requests.get(image_url)

            try:
                poke_image_data = Image.open(
                    io.BytesIO(
                        image_response.content))
                poke_image = ctk.CTkImage(light_image=poke_image_data,
                                          size=(100, 100))

                listofvalues[i] = ctk.CTkLabel(Main,
                                               image=poke_image,
                                               text="")

                listofvalues[i].grid(row=i+2, column=3, padx=10, pady=10)
            except UnidentifiedImageError:
                print('678 error')
                ErrorImage = Image.open('amalgamate.png')
                poke_image = ctk.CTkImage(light_image=ErrorImage,
                                          size=(100, 100))

                listofvalues[i] = ctk.CTkLabel(Main,
                                               image=poke_image,
                                               text="")

                listofvalues[i].grid(row=i+2,
                                     column=3,
                                     padx=10,
                                     pady=10)
    except AttributeError:
        print('Not every slot is full, fill them for images!')


def NoButton():
    DeleteWindow.destroy()


def YesButton():
    # Read the CSV file into a DataFrame
    data = pd.read_csv('passwords.csv')

    # Remove the row where the 'username' matches the current username
    data = data[data['username'] != Username]

    # Save the updated DataFrame back to the CSV file
    data.to_csv('passwords.csv', index=False)

    # Print confirmation and the updated DataFrame
    print("Account deleted.")
    print(data)
    Main.destroy()


def DELETEACCOUNT():
    global DeleteWindow
    DeleteWindow = ctk.CTkToplevel()
    DeleteWindow.resizable(0, 0)
    DeleteWindow.attributes("-topmost", True)

    # Are you suree? #

    Frame = ctk.CTkFrame(DeleteWindow, fg_color='red')
    Frame.grid(row=0, column=0, rowspan=10)
    Frame.lower()

    part1 = "Are you sure you want to "
    part2 = f"delete your account {Username}?"
    Label = ctk.CTkLabel(Frame,
                         text=part1 + part2)
    Label.pack()

    Yes = ctk.CTkButton(Frame, text='Yes',
                        text_color='red',
                        fg_color='Lime',
                        command=YesButton)

    No = ctk.CTkButton(Frame, text='No',
                       text_color='white',
                       fg_color='orange',
                       command=NoButton)

    Yes.pack(pady=20)
    No.pack(pady=20)


# Login Window #
Login = ctk.CTk()
Login.resizable(0, 0)  # NO MAXIMISING it breaks my app :3 #

# Bg colors #
frame_left = ctk.CTkFrame(Login, fg_color="red")
frame_left.grid(row=0, column=0, sticky="nsew", rowspan=5)

frame_right = ctk.CTkFrame(Login, fg_color="white")
frame_right.grid(row=0, column=1, sticky="nsew", rowspan=5)

# Lower the frames #
frame_left.lower()
frame_right.lower()

# Labels #
UsernameLabel = ctk.CTkLabel(Login, text="Username:", bg_color='red',
                             text_color='white',
                             font=('ariel', 20, 'bold'))

PasswordLabel = ctk.CTkLabel(Login, text="Password:", bg_color='red',
                             text_color='white',
                             font=('ariel', 20, 'bold'))

# Input Button #
EnterButton = ctk.CTkButton(Login,
                            text="Login",
                            command=LoginButton,
                            bg_color='white',
                            fg_color='red',
                            font=('ariel', 15, 'bold'))

NewLoginButton = ctk.CTkButton(Login, text="New Login",
                               fg_color='red',
                               text_color="white",
                               command=NewLogin,
                               bg_color='white', font=('ariel', 15, 'bold'))

# Entry Boxes #
UsernameEntry = ctk.CTkEntry(Login, bg_color='white')
PasswordEntry = ctk.CTkEntry(Login, bg_color='white')

# PokeDictionary #
Guest = ctk.CTkButton(Login, text="Guest Account",
                      command=MoreInfoPls,
                      fg_color='red',
                      text_color="white",
                      bg_color='white',
                      font=('ariel', 15, 'bold'))

Guest.grid(row=4, column=1)

# Grid the modules #
UsernameLabel.grid(row=0, column=0)
PasswordLabel.grid(row=1, column=0, pady=20)

UsernameEntry.grid(row=0, column=1)
PasswordEntry.grid(row=1, column=1)

EnterButton.grid(row=2, column=1)
NewLoginButton.grid(row=3, column=1, pady=20)

Login.mainloop()


if LoginSuccess is True:
    global listofvalues
    Main = ctk.CTk()
    Main.resizable(0, 0)

    for i in range(1, 4):
        Main.rowconfigure(i)
    for i in range(1, 3):
        Main.columnconfigure(i, weight=1)

    # bg colors #
    frame_left = ctk.CTkFrame(Main, fg_color="red")
    frame_left.grid(row=0, column=0, sticky="nsew", rowspan=10)

    frame_middle = ctk.CTkFrame(Main, fg_color="white")
    frame_middle.grid(row=0,
                      column=1,
                      sticky="nsew",
                      rowspan=10)

    frame_right = ctk.CTkFrame(Main,
                               fg_color="red")

    frame_right.grid(row=0, column=2,
                     sticky="nsew",
                     rowspan=10)

    frame_far_right = ctk.CTkFrame(Main, fg_color="white")
    frame_far_right.grid(row=0,
                         column=3,
                         sticky="nsew",
                         rowspan=10)

    # frame_farRight = ctk.CTkFrame(Main, fg_color="white")
    # frame_farRight.grid(row=0, column=3, sticky="nsew", rowspan=10)

    # Lower to background #
    frame_left.lower()
    frame_middle.lower()
    # frame_right.lower()

    # Welcome Label #
    Welcome = ctk.CTkLabel(Main, text="Welcome", font=('arial', 45))
    Welcome.grid(row=0, column=0, sticky='ew')
    Welcome2 = ctk.CTkLabel(Main,
                            text=Username,
                            font=('arial', 45),
                            text_color='lime')

    Welcome2.grid(row=0, column=1, sticky='ew')

    # Input Pokemon #
    PokeLabel = ctk.CTkLabel(Main,
                             text="Input Pokemon here:",
                             pady=50,
                             bg_color='red',
                             text_color='White',
                             font=('ariel', 20, 'bold'))
    PokeLabel.grid(row=1, column=0)
    PokeInputText = ctk.CTkTextbox(Main, width=300, height=10)
    PokeInputText.grid(row=1, column=1)

    # Labels for pokemon #
    PokeLabelArray = ['Label1',
                      'Label2',
                      'Label3',
                      'Label4',
                      'Label5',
                      'Label6']
    for x in range(1, 7):
        # Grids all 6 labels 1-6 #
        i = ctk.CTkLabel(Main,
                         text=f"Pokemon {x}:", bg_color='red',
                         text_color='white',
                         font=('ariel', 25, 'bold'))
        i.grid(row=x+1, column=0)

    rowselect = 2

    value = data.loc[data['username'] == Username]

    # All of this just reads the pokemon name from the CSV #
    value1 = value['poke1'].iloc[0]
    Poke1Label = ctk.CTkLabel(Main,
                              text=str(value1).strip(),
                              bg_color='white',
                              font=('ariel', 30, 'bold'),
                              text_color='red')
    Poke1Label.grid(column=1, row=2)

    value2 = value['poke2'].iloc[0]

    Poke2Label = ctk.CTkLabel(Main,
                              text=str(value2).strip(),
                              bg_color='white',
                              font=('ariel', 30, 'bold'),
                              text_color='red')

    Poke2Label.grid(column=1, row=3)

    value3 = value['poke3'].iloc[0]

    Poke3Label = ctk.CTkLabel(Main,
                              text=str(value3).strip(),
                              bg_color='white',
                              font=('ariel', 30, 'bold'),
                              text_color='red')

    Poke3Label.grid(column=1, row=4)

    value4 = value['poke4'].iloc[0]
    Poke4Label = ctk.CTkLabel(Main,
                              text=str(value4).strip(),
                              bg_color='white',
                              font=('ariel', 30, 'bold'),
                              text_color='red')

    Poke4Label.grid(column=1, row=5)

    value5 = value['poke5'].iloc[0]
    Poke5Label = ctk.CTkLabel(Main,
                              text=str(value5).strip(), bg_color='white',
                              font=('ariel', 30, 'bold'),
                              text_color='red')

    Poke5Label.grid(column=1, row=6)

    value6 = value['poke6'].iloc[0]
    Poke6Label = ctk.CTkLabel(Main,
                              text=str(value6).strip(),
                              bg_color='white',
                              font=('ariel', 30, 'bold'),
                              text_color='red')
    Poke6Label.grid(column=1, row=7)

    listofvalues = [value1, value2, value3, value4, value5, value6]
    # The list of value get changed to the pokemon #
    MenuPoke()

    # Packs all 6 buttons that enable replacement #
    button1 = ctk.CTkButton(Main,
                            command=button1,
                            text="Pokemon 1",
                            fg_color='white',
                            text_color='red',
                            font=('ariel', 15, 'bold'),
                            bg_color='red')
    button1.grid(row=2, column=2, padx=100, pady=20)

    button2 = ctk.CTkButton(Main,
                            command=button2,
                            text="Pokemon 2",
                            fg_color='white',
                            text_color='red',
                            font=('ariel', 15, 'bold'),
                            bg_color='red')
    button2.grid(row=3, column=2, padx=100, pady=20)

    button3 = ctk.CTkButton(Main,
                            command=button3,
                            text="Pokemon 3",
                            fg_color='white',
                            text_color='red',
                            font=('ariel', 15, 'bold'),
                            bg_color='red')
    button3.grid(row=4, column=2, padx=100, pady=20)

    button4 = ctk.CTkButton(Main,
                            command=button4,
                            text="Pokemon 4",
                            fg_color='white',
                            text_color='red',
                            font=('ariel', 15, 'bold'),
                            bg_color='red')
    button4.grid(row=5, column=2, padx=100, pady=20)

    button5 = ctk.CTkButton(Main,
                            command=button5,
                            text="Pokemon 5",
                            fg_color='white',
                            text_color='red',
                            font=('ariel', 15, 'bold'),
                            bg_color='red')
    button5.grid(row=6, column=2, padx=100, pady=20)

    button6 = ctk.CTkButton(Main,
                            command=button6,
                            text="Pokemon 6",
                            fg_color='white',
                            text_color='red',
                            font=('ariel', 15, 'bold'),
                            bg_color='red')
    button6.grid(row=7, column=2, padx=100, pady=20)

    try:
        OldImage = Image.open("pokedex2.png")
        scale = 0.5
        NewImage = new_size = (OldImage.width * scale, OldImage.height * scale)
        poke_image = ctk.CTkImage(light_image=OldImage, size=NewImage)
        PokeDictionary = ctk.CTkButton(Main,
                                       image=poke_image,
                                       text="",
                                       fg_color='white',
                                       bg_color='white',
                                       hover_color='grey',
                                       command=MoreInfoPls)
        PokeDictionary.grid(column=1, row=8)
    except FileNotFoundError:  # image doesn't exist in files #
        os.system('cls')
        print('file download error')

    # Makes a label for the unaware #
    TextType = '<-- Press here to see more data about a pokemon'
    FontType = ('ariel', 19, 'bold')
    ShowThatItsAButtonSinceItsNotObvious = ctk.CTkLabel(Main,
                                                        text=TextType,
                                                        font=FontType,
                                                        bg_color='red',
                                                        text_color='white')
    ShowThatItsAButtonSinceItsNotObvious.grid(column=2, row=8)

    # Tutorial #
    TutorialLabel = ctk.CTkLabel(Main,
                                 text='Select a pokemon To Replace',
                                 font=FontType,
                                 text_color='white',
                                 bg_color='red')
    TutorialLabel.grid(row=1, column=2)

    DeleteButton = ctk.CTkButton(Main,
                                 text='DELETE ACCOUNT',
                                 bg_color='red',
                                 fg_color='white',
                                 font=('arial', 20, 'bold'),
                                 text_color='red',
                                 command=DELETEACCOUNT)  # BE CAREFUL #
    DeleteButton.grid(row=8, column=0, pady=20)

    Main.mainloop()
