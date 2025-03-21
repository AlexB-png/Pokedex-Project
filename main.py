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
import random
from fuzzywuzzy import fuzz

# Hello :D #

# Variables #
LoginSuccess = False
NewloginVariable = False
IWantMoreInfoNOW = False
fail = False
Press = False

Movelist = []

# This is the same font used for a majority of text #
TextFont = ('arial', 20, 'bold')

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
        image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
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
            ErrorImage = Image.open('./images/amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage,
                                      size=(100, 100))
            listofvalues[0].configure(image=poke_image)
        # Changes the name label to the selected pokemons name #
        Poke1Label.configure(text=name)

        with open('./data/passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke1'] = name
        with open('./data/passwords.csv', 'w') as file:
            data.to_csv(file, index=False)


def button2():
    global fail
    PokeInput()
    if fail is False:

        poke_url = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        poke_url_response = requests.get(poke_url)
        poke_url_response.raise_for_status()
        JsonFile = poke_url_response.json()
        image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image_Error = ctk.CTkImage(light_image=poke_image_data,
                                            size=(100, 100))
            listofvalues[1].configure(image=poke_image_Error)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('./images/amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[1].configure(image=poke_image)

        Poke2Label.configure(text=name)

        with open('./data/passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke2'] = name
        with open('./data/passwords.csv', 'w') as file:
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
        image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))

            listofvalues[2].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('./images/amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[2].configure(image=poke_image)

        with open('./data/passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke3'] = name
        with open('./data/passwords.csv', 'w') as file:
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
        image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
        name = JsonFile['name']
        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))

            listofvalues[3].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('./images/amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[3].configure(image=poke_image)

        with open('./data/passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke4'] = name
        with open('./data/passwords.csv', 'w') as file:
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
        image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))
            listofvalues[4].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('./images/amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[4].configure(image=poke_image)

        with open('./data/passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke5'] = name
        with open('./data/passwords.csv', 'w') as file:
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
        image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
        name = JsonFile['name']

        try:
            image_response = requests.get(image_url)
            poke_image_data = Image.open(io.BytesIO(image_response.content))
            poke_image = ctk.CTkImage(light_image=poke_image_data,
                                      size=(100, 100))
            listofvalues[5].configure(image=poke_image)
        except UnidentifiedImageError:
            print('678 error')
            ErrorImage = Image.open('./images/amalgamate.png')
            poke_image = ctk.CTkImage(light_image=ErrorImage, size=(100, 100))
            listofvalues[5].configure(image=poke_image)

        with open('./data/passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke6'] = name
        with open('./data/passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke6Label.configure(text=name, text_color='red')


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
                Selection = get_label_tags(3, Selection)
                SimilarList = []
                try:
                    for i in range(0, 3):
                        Selection2 = Selection[i][0]
                        SimilarList.append(Selection2)
                    TutorialLabel.configure(text=f"Did you mean {SimilarList}?")
                except IndexError:
                    TutorialLabel.configure(text=f"Did you mean {Selection[0][0]}?")
                fail = True
            else:
                fail = False
        except KeyError:
            print('ERROR')
            fail = True


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
    with open('./data/passwords.csv', 'r') as data:
        data = pd.read_csv(data)
        Username2 = data.loc[data['username'] == Username]
        Password2 = Username2.loc[data['password'] == Password]
    if Password2.empty is True:
        Pep = 'Incorrect Username or Password'
        UsernameLabel.configure(text=Pep)
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

    # Professor Oak has NOT made a donation! You're poor! #
    d = {'username': [NewUsername], 'password': [NewPassword],
         'poke1': [pd.NA],
         'poke2': [pd.NA],
         'poke3': [pd.NA],
         'poke4': [pd.NA],
         'poke5': [pd.NA],
         'poke6': [pd.NA]
         }

    data = pd.DataFrame(data=d)

    with open('./data/passwords.csv', 'r') as file:
        LoadedData = pd.read_csv(file)
        df = pd.concat([LoadedData, data], ignore_index=True)
        UserNameExists = LoadedData.loc[LoadedData['username'] == NewUsername]
        # Checks if both inputs are empty #
        if UserNameExists.empty and NewUsername and NewPassword:
            # Adds the new login #
            df.to_csv('./data/passwords.csv', index=False)
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


def MoreInfoPls():  # My variable names are out the window. Im tired :3 #
    global SelectBox, PokeActualImage, AccNameLabel, MoveLabel, Typelabel
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
                               font=TextFont,
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
                                 font=TextFont)

    SelectButton.grid(row=0, column=2)

    RandomButton = ctk.CTkButton(Info,
                                 text='Random!',
                                 bg_color='red',
                                 fg_color='white',
                                 text_color='red',
                                 font=TextFont,
                                 command=randompoke)
    RandomButton.grid(row=1, column=2)

    # Pre Labels ( Before updates) #

    # Image of selection #
    PokeLabelImage = ctk.CTkLabel(Info,
                                  text='Pokemon Image:',
                                  bg_color='red',
                                  font=TextFont,
                                  text_color='white')
    PokeLabelImage.grid(row=1, column=0, pady=30)

    PokeActualImage = ctk.CTkLabel(Info,
                                   text="IMAGE HERE",
                                   font=TextFont,
                                   bg_color='white',
                                   text_color='red')
    PokeActualImage.grid(row=1, column=1)

    # Name of Selection #
    PokeNameLabel = ctk.CTkLabel(Info, text="Name Of pokemon",
                                 font=TextFont,
                                 bg_color='red',
                                 text_color='white')
    PokeNameLabel.grid(row=2, column=0, pady=20)

    AccNameLabel = ctk.CTkLabel(Info, text='')
    AccNameLabel.grid(row=2, column=1)

    MoveLabel = ctk.CTkLabel(Info,
                             text="",
                             font=('ariel', 15, 'bold'))
    MoveLabel.grid(row=3, column=1)

    MoveLabelFirst = ctk.CTkLabel(Info,
                                  text="Moveset:",
                                  font=TextFont,
                                  text_color='white',
                                  bg_color='red')
    MoveLabelFirst.grid(row=3, column=0, pady=20)

    # This is just the label of what the type is #
    TypePoke = ctk.CTkLabel(Info,
                            text='Types:',
                            text_color='white',
                            font=TextFont,
                            bg_color='red')
    TypePoke.grid(row=4, column=0, pady=40)
    # This is the actual type #
    Typelabel = ctk.CTkLabel(Info,
                             text='Input a pokemon!',
                             font=TextFont,
                             text_color='red',
                             bg_color='white')
    Typelabel.grid(row=4, column=1)


def randompoke():
    global Press
    if Press is not True:
        SelectBox.delete(0, tk.END)
        pokemon = random.randint(1, 1025)
        Press = True
        SelectBox.insert(0, pokemon)
        print(pokemon)
        Dictionary()


def MenuPoke():
    for i in range(0, 6):
        try:
            url = "https://pokeapi.co/api/v2/pokemon/"
            url2 = listofvalues[i]
            poke_url = url + url2
            poke_url_response = requests.get(poke_url)
            poke_url_response.raise_for_status()
            JsonFile = poke_url_response.json()
            image_url = JsonFile['sprites']['other']['official-artwork']['front_default']
            image_response = requests.get(image_url)

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
            Unidentified(1, i)
        except TypeError:
            Unidentified(0, i)


def NoButton():
    DeleteWindow.destroy()


def YesButton():
    # Read the CSV file into a DataFrame
    data = pd.read_csv('./data/passwords.csv')

    # Remove the row where the 'username' matches the current username
    data = data[data['username'] != Username]

    # Save the updated DataFrame back to the CSV file
    data.to_csv('./data/passwords.csv', index=False)

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


def change():
    global InputName, InputPass, ChangeWindow, Label
    # New Window #
    ChangeWindow = ctk.CTkToplevel()
    ChangeWindow.resizable(0, 0)
    ChangeWindow.attributes('-topmost', True)
    ChangeWindow.geometry('350x300')

    # Make the grid expand #
    ChangeWindow.grid_rowconfigure(0, weight=1)
    ChangeWindow.grid_columnconfigure(0, weight=1)

    # Frame #
    frame = ctk.CTkFrame(ChangeWindow, fg_color='red')
    frame.grid(row=0, column=0, sticky='nesw')
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Modules #
    text = "What would you like to change your username to?"  # PEP8 #
    Label = ctk.CTkLabel(frame,
                         text=text,
                         font=TextFont,
                         text_color='white')
    Label.grid(row=0, column=0, sticky='nesw', pady=10, padx=10)

    PassLabel = ctk.CTkLabel(frame,
                             text='New Password!',
                             font=TextFont,
                             text_color='white')
    PassLabel.grid(row=2, column=0, sticky='nesw', pady=10, padx=10)

    InputName = ctk.CTkEntry(frame)
    InputName.grid(row=1, column=0, pady=10)

    InputPass = ctk.CTkEntry(frame)
    InputPass.grid(row=3, column=0, pady=10)

    InputButton = ctk.CTkButton(frame,
                                text='Input!',
                                text_color='red',
                                bg_color='red',
                                fg_color='white',
                                font=TextFont,
                                command=replace)
    InputButton.grid(row=5, column=0, pady=40)


def replace():
    InputUser = InputName.get()
    InputPassword = InputPass.get()
    # RData refers to replacement data #
    RData = pd.read_csv('./data/passwords.csv')

    # This checks if the Username already exists #
    check = RData.loc[data['username'] == InputUser]
    # This encrypts the password #
    PassWord = hashlib.sha256(InputPassword.encode('utf-8')).hexdigest()

    if check.empty:
        # Changes Username #
        RData.loc[RData['username'] == Username, 'username'] = InputUser
        # Changes Password #
        RData.loc[RData['username'] == InputUser, 'password'] = PassWord
        RData.to_csv('./data/passwords.csv', index=False)

        # Deletes the windows on success #
        Main.destroy()
    else:
        Label.configure(text="Username already exists!")


def FuncList():
    # This handles extra fuctions as specified #
    top = ctk.CTkToplevel()
    top.resizable(0, 0)
    top.attributes("-topmost", True)

    # TOP 10 SIMILARITIES #
    button10 = ctk.CTkButton(top,
                             text='More info!',
                             bg_color='red',
                             fg_color='white',
                             text_color='red',
                             font=FontType,
                             command=Extras)
    button10.grid(row=0, column=0, sticky='ew', padx=20, pady=50)


def Extras():
    Top10Level = ctk.CTkToplevel()
    Top10Level.resizable(0, 0)
    Top10Level.attributes("-topmost", True)

    pep = 'Do try inputting 678! Professor Oak made an abomination!'
    # Label
    Guide = ctk.CTkLabel(Top10Level,
                         text=pep,
                         font=FontType,
                         text_color='red')
    Guide.grid(row=0, column=0, sticky='nesw', padx=50)


def get_similarity_score(LocalArray):
    return LocalArray[1]


def get_label_tags(HowMany, input):
    url = "https://pokeapi.co/api/v2/pokemon?limit=1025&offset=0"
    url_Match_response = requests.get(url.strip())
    matches = url_Match_response.json()
    LocalArray = []
    for i in range(0, 1025):
        pokemon = matches['results'][i]['name']
        ratio = fuzz.partial_ratio(pokemon, input)
        LocalArray.append((pokemon, ratio))
    SortedArray = sorted(LocalArray,
                         key=get_similarity_score,
                         reverse=True)[:HowMany]
    return SortedArray


def Unidentified(insert, i):
    print("Image doesn't exist!")
    if insert == 1:
        image = ('./images/amalgamate.png')
    else:
        image = ('./images/bigz.png')
    ErrorImage = Image.open(image)
    poke_image = ctk.CTkImage(light_image=ErrorImage,
                              size=(100, 100))

    listofvalues[i] = ctk.CTkLabel(Main,
                                   image=poke_image,
                                   text="")

    listofvalues[i].grid(row=i+2,
                         column=3,
                         padx=10,
                         pady=10)


def Dictionary():
    global Press
    Input = SelectBox.get()
    x = get_label_tags(3, Input)
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
                                   font=TextFont)

            try:
                # Renders image and puts in the dictionary #
                PokemonSprite = JsonFile['sprites']['other']['official-artwork']['front_default']
                PokemonSprite = requests.get(PokemonSprite)
                poke_image_data = Image.open(io.BytesIO(PokemonSprite.content))
                poke_image = ctk.CTkImage(light_image=poke_image_data,
                                          size=(100, 100))
                # Puts the image into the label #
                PokeActualImage.configure(image=poke_image, text="")
            except UnidentifiedImageError:  # 678 error #
                ErrorImage = Image.open('./images/amalgamate.png')
                poke_image = ctk.CTkImage(light_image=ErrorImage,
                                          size=(100, 100))
                PokeActualImage.configure(image=poke_image, text="")

            # Also places the moves #
            Movelist = []
            for i in range(0, 3):
                try:
                    Moves = JsonFile['abilities'][i]['ability']['name']
                    Movelist.append(Moves)
                except IndexError:
                    print('Invalid Move key')
            MoveLabel.configure(text=Movelist,
                                bg_color='white',
                                text_color='red',
                                font=TextFont)
            MoveLabel.update()

            # This just makes the label that says its type #
            TypePokeList = []
            for i in range(0, 3):
                try:
                    typepoke = JsonFile['types'][i]['type']['name']
                    TypePokeList.append(typepoke)
                except IndexError:
                    print('pokemon move slot done!')
            Typelabel.configure(text=TypePokeList)
        else:
            SelectBox.delete(0, tk.END)
            SelectBox.insert(0, x[0][0])
            print(Input)
    else:
        print("Fail")
    Press = False


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
PasswordEntry = ctk.CTkEntry(Login, bg_color='white', show="*")

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
    global listofvalues, TutorialLabel
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

    # Lower to background #
    frame_left.lower()
    frame_middle.lower()

    # Welcome Label #
    Welcome = ctk.CTkLabel(Main, text="Welcome", font=('arial', 45))
    Welcome.grid(row=0, column=0, sticky='ew')
    Welcome2 = ctk.CTkLabel(Main,
                            text=Username,
                            font=('arial', 45),
                            text_color='lime')

    Welcome2.grid(row=0, column=1, sticky='ew')

    # Change Login Button #
    Change = ctk.CTkButton(Main,
                           text="Change Name!",
                           text_color='red',
                           bg_color='red',
                           fg_color='white',
                           font=TextFont,
                           command=change)
    Change.grid(row=0, column=2)

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
        OldImage = Image.open("./images/pokedex2.png")
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
                                 font=TextFont,
                                 text_color='red',
                                 command=DELETEACCOUNT)  # BE CAREFUL #
    DeleteButton.grid(row=8, column=0, pady=20)

    Main.mainloop()
