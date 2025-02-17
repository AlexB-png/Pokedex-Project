import customtkinter as ctk
import tkinter as tk
import hashlib
import pandas as pd
import requests
import time
from PIL import Image
import io

LoginSuccess = False
NewloginVariable = False
IWantMoreInfoNOW = False

Movelist = []


def button1():
    global fail, selection
    print('pokemon 1 replaced')
    PokeInput()
    if fail is False:
        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke1'] = Selection
        print(data)
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke1Label.configure(text=PokemonName, text_color='pink')


def button2():
    global fail, selection
    print('pokemon 2 replaced')
    PokeInput()
    if fail is False:
        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke2'] = Selection
        print(data)
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke2Label.configure(text=PokemonName, text_color='pink')


def button3():
    global fail, selection
    print('pokemon 3 replaced')
    PokeInput()
    if fail is False:
        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke3'] = Selection
        print(data)
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke3Label.configure(text=PokemonName, text_color='pink')


def button4():
    global fail, selection
    print('pokemon 4 replaced')
    PokeInput()
    if fail is False:
        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke4'] = Selection
        print(data)
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke4Label.configure(text=PokemonName, text_color='pink')


def button5():
    global fail, selection
    print('pokemon 5 replaced')
    PokeInput()
    if fail is False:
        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke5'] = Selection
        print(data)
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke5Label.configure(text=PokemonName, text_color='pink')


def button6():
    global fail, selection
    print('pokemon 6 replaced')
    PokeInput()
    if fail is False:
        with open('passwords.csv', 'r') as file:
            data = pd.read_csv(file)
        data.loc[data['username'] == Username, 'poke6'] = Selection
        print(data)
        with open('passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        Poke6Label.configure(text=PokemonName, text_color='pink')


def LoginButton():
    global Username, Password, LoginSuccess, data
    Username = UsernameEntry.get()
    UsernameEntry.delete(0, tk.END)
    Password = PasswordEntry.get()
    PasswordEntry.delete(0, tk.END)
    Password = hashlib.sha256(Password.encode('utf-8')).hexdigest()
    with open('passwords.csv', 'r') as data:
        data = pd.read_csv(data)
        Username2 = data.loc[data['username'] == Username]
        Password2 = Username2.loc[data['password'] == Password]
    if Password2.empty is True:
        print("Fail")
    else:
        print("Success")
        LoginSuccess = True
        Login.destroy()


def EnterNewData():
    NewUsername = UsernameNewEntry.get().strip()
    NewUsername = NewUsername.lower().strip()
    print(NewUsername)
    NewPassword = PasswordNewEntry.get()
    if NewPassword != "":
        NewPassword = hashlib.sha256(NewPassword.encode('utf-8')).hexdigest()
    print(NewPassword)
    PasswordNewEntry.delete(0, tk.END)
    UsernameNewEntry.delete(0, tk.END)

    d = {'username': [NewUsername], 'password': [NewPassword],
         'poke1': [pd.NA],
         'poke2': [pd.NA],
         'poke3': [pd.NA],
         'poke4': [pd.NA],
         'poke5': [pd.NA],
         'poke6': [pd.NA]
         }
    
    data = pd.DataFrame(data=d)

    with open('passwords.csv', 'r') as file:
        LoadedData = pd.read_csv(file)
        df = pd.concat([LoadedData, data], ignore_index=True)
        UserNameExists = LoadedData.loc[LoadedData['username'] == NewUsername]
        print(UserNameExists)
        if UserNameExists.empty is True and NewUsername != "" and NewPassword != "":
            print('The DataFrame Is Empty')
            df.to_csv('passwords.csv', index=False)
            StatusNewLogin.configure(text="Success!", text_color='green', font=('ariel', 25, 'bold'))
            StatusNewLogin.update()
            time.sleep(3)
        elif NewUsername != "" and NewPassword != "":
            StatusNewLogin.configure(text="Username in use!", text_color='green', font=('ariel', 20, 'bold'))
            StatusNewLogin.update()
        else:
            for i in range(1,20):
                if i % 2 == 0:
                    SirenColor = 'red'
                else:
                    SirenColor = 'blue'
                StatusNewLogin.configure(text="STOPPPP ITTTTTT", text_color=SirenColor, font=('ariel', 25, 'bold'))
                StatusNewLogin.update()
                time.sleep(0.1)
            StatusNewLogin.configure(text="Input some text!", text_color='purple', font=('ariel', 20, 'bold'))
            StatusNewLogin.update()


def NewLogin():
    global StatusNewLogin, UsernameNewEntry, PasswordNewEntry, NewLogin
    NewLogin = ctk.CTkToplevel()
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
    UsernameNewLabel = ctk.CTkLabel(NewLogin, text="Enter New Username:", bg_color='red', text_color='white', font=('ariel',20,'bold'))
    PasswordNewLabel = ctk.CTkLabel(NewLogin, text="Enter New Password:", bg_color='red', text_color='white', font=('ariel',20,'bold'))
    StatusNewLogin = ctk.CTkLabel(NewLogin, width=40, height=20, text="Input A New Username / Password", bg_color='white', text_color='red', font=('ariel',15,'bold'))

    UsernameNewEntry = ctk.CTkEntry(NewLogin, bg_color='white')
    PasswordNewEntry = ctk.CTkEntry(NewLogin, bg_color='white')

    EnterNewDataButton = ctk.CTkButton(NewLogin, text="Enter New Data", command=EnterNewData, bg_color='white', font=('ariel', 15, 'bold'), fg_color='red')

    # Grid Modules #
    UsernameNewLabel.grid(row=0, column=0, pady=20, padx=30)
    PasswordNewLabel.grid(row=1, column=0)

    UsernameNewEntry.grid(row=0, column=1, pady=20)
    PasswordNewEntry.grid(row=1, column=1)

    EnterNewDataButton.grid(row=2, column=1, pady=20)
    StatusNewLogin.grid(row=3, column=0)


def PokeInput():
    global fail, Selection
    Selection = PokeInputText.get('1.0', tk.END)
    PokeInputText.delete('1.0', tk.END)
    if Selection.strip() == "":
        print("Input a pokemon")
    else:
        url = "https://pokeapi.co/api/v2/pokemon/" + Selection
        url = url.strip()
        url_response = requests.get(url)
        if url_response.status_code != 200:
            TutorialLabel.configure(text='Invalid Pokemon', text_color='purple', font=('ariel', 30, 'bold'))
            TutorialLabel.update()
            time.sleep(3)
            TutorialLabel.configure(text='Pick A Pokemon To Replace', text_color='white', font=('ariel', 20, 'bold'))
            TutorialLabel.update()
            print(url)
            fail = True
        else:
            print("Success")
            fail = False


def MoreInfoPls():  # My variable names are out the window. Im tired :3 #
    global SelectBox, PokeActualImage, AccNameLabel, MoveLabel
    Info = ctk.CTkToplevel()
    Info.resizable(0, 0)  # Dont even try resizing #
    Info.attributes('-topmost', True)

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

    for i in range(1,5):
        Info.rowconfigure(i)

    # Modules #
    SelectLabel = ctk.CTkLabel(Info, text='Input Pokemon Here!')
    SelectLabel.grid(row=0, column=0)

    SelectBox = ctk.CTkEntry(Info, width=200, height=5)
    SelectBox.grid(row=0, column=1, padx=20)

    SelectButton = ctk.CTkButton(Info, text='Input!', command=CheckIfOnline)
    SelectButton.grid(row=0, column=2)

    # Pre Labels ( Before updates) #

    # Image of selection #
    PokeLabelImage = ctk.CTkLabel(Info, text='Pokemon Image:')
    PokeLabelImage.grid(row=1, column=0, pady=30)
    PokeActualImage = ctk.CTkLabel(Info, text="")
    PokeActualImage.grid(row=1, column=1)

    # Name of Selection #
    PokeNameLabel = ctk.CTkLabel(Info, text="Name Of pokemon")
    PokeNameLabel.grid(row=2, column=0, pady=20)
    AccNameLabel = ctk.CTkLabel(Info, text='')
    AccNameLabel.grid(row=2, column=1)

    # MoveList of the pokemon #
    scrollable_frame = ctk.CTkScrollableFrame(Info, orientation="horizontal", bg_color='white', height=50)
    scrollable_frame.grid(row=3, column=1, rowspan=5)

    MoveLabel = ctk.CTkLabel(scrollable_frame, text="", font=('ariel', 15, 'bold'))
    MoveLabel.grid(row=3, column=1)

    MoveLabelFirst = ctk.CTkLabel(Info, text="Moveset:")
    MoveLabelFirst.grid(row=3, column=0, pady=20)


def CheckIfOnline():
    Input = SelectBox.get()
    if Input.strip() != "":
        url = "https://pokeapi.co/api/v2/pokemon/" + Input
        url = url.strip()
        url_response = requests.get(url)
        if url_response.status_code == 200:
            JsonFile = url_response.json()

            PokemonName = JsonFile['name']
            AccNameLabel.configure(text=PokemonName)

            PokemonSprite = JsonFile['sprites']['front_default']
            PokemonSprite = requests.get(PokemonSprite)
            image_data = Image.open(io.BytesIO(PokemonSprite.content))
            poke_image = ctk.CTkImage(light_image=image_data, size=(100, 100))
            PokeActualImage.configure(image=poke_image)

            Moves = JsonFile['moves']
            for move in Moves:
                move_name = move['move']['name'] 
                Movelist.append(f"'{move_name}'")
            MoveLabel.configure(text=Movelist)
            MoveLabel.update()
        else:
            SelectBox.delete(0, tk.END)
    else:
        print("NO!")


# Login Window #
Login = ctk.CTk()
Login.resizable(0, 0) # NO MAXIMISING it breaks my app :3 #

# Bg colors #
frame_left = ctk.CTkFrame(Login, fg_color="red")
frame_left.grid(row=0, column=0, sticky="nsew", rowspan=5)

frame_right = ctk.CTkFrame(Login, fg_color="white")
frame_right.grid(row=0, column=1, sticky="nsew", rowspan=5)

# Lower the frames #
frame_left.lower()
frame_right.lower()

# Labels #
UsernameLabel = ctk.CTkLabel(Login, text="Username:", bg_color='red', text_color='white', font=('ariel',20,'bold'))
PasswordLabel = ctk.CTkLabel(Login, text="Password:", bg_color='red', text_color='white', font=('ariel',20,'bold'))

# Input Button #
EnterButton = ctk.CTkButton(Login, text="Login", command=LoginButton, bg_color='white', fg_color='red', font=('ariel', 15, 'bold'))
NewLoginButton = ctk.CTkButton(Login, text="New Login", fg_color='red', text_color="white", command=NewLogin, bg_color='white', font=('ariel', 15, 'bold'))

# Entry Boxes #
UsernameEntry = ctk.CTkEntry(Login, bg_color='white')
PasswordEntry = ctk.CTkEntry(Login, bg_color='white')

# PokeDictionary #
Guest = ctk.CTkButton(Login, text="Guest Account", command=MoreInfoPls, fg_color='red', text_color="white", bg_color='white', font=('ariel', 15, 'bold'))
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
    Main = ctk.CTk()
    Main.resizable(0, 0)

    Main.rowconfigure(0, weight=0)
    Main.rowconfigure(1, weight=0)
    Main.rowconfigure(2, weight=0)
    Main.rowconfigure(3, weight=0)
    for i in range(1,5):
        Main.columnconfigure(i, weight=1)

    # bg colors #
    frame_left = ctk.CTkFrame(Main, fg_color="red")
    frame_left.grid(row=0, column=0, sticky="nsew", rowspan=10)

    frame_middle = ctk.CTkFrame(Main, fg_color="white")
    frame_middle.grid(row=0, column=1, sticky="nsew", rowspan=10)

    frame_right = ctk.CTkFrame(Main, fg_color="red")
    frame_right.grid(row=0, column=2, sticky="nsew", rowspan=10)

    # frame_farRight = ctk.CTkFrame(Main, fg_color="white")
    # frame_farRight.grid(row=0, column=3, sticky="nsew", rowspan=10)

    # Lower to background #
    frame_left.lower()
    frame_middle.lower()
    # frame_right.lower()
    
    # Welcome Label #
    Welcome = ctk.CTkLabel(Main, text=f"Welcome", font=('arial', 45))
    Welcome.grid(row=0, column=0, sticky='ew')
    Welcome2 = ctk.CTkLabel(Main, text=Username, font=('arial', 45), text_color='lime')
    Welcome2.grid(row=0, column=1, sticky='ew')

    # Input Pokemon #
    PokeLabel = ctk.CTkLabel(Main, text="Input Pokemon here:", pady=50, bg_color='red', text_color='White', font=('ariel',20,'bold'))
    PokeLabel.grid(row=1, column=0)
    PokeInputText = ctk.CTkTextbox(Main, width=300, height=10)
    PokeInputText.grid(row=1, column=1)

    # Labels for pokemon #
    PokeLabelArray = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6']
    for i in PokeLabelArray:
        for x in range(1, 7):
            i = ctk.CTkLabel(Main, text=f"Pokemon {x}:", bg_color='red', text_color='white', font=('ariel',25,'bold'))
            i.grid(row=x+1, column=0)

    rowselect = 2
    
    value = data.loc[data['username'] == Username]
    
    value1 = value['poke1'].iloc[0]
    Poke1Label = ctk.CTkLabel(Main, text=str(value1).strip(), bg_color='white', font=('ariel', 30, 'bold'), text_color='red')
    Poke1Label.grid(column=1, row=2)
    
    value2 = value['poke2'].iloc[0]
    Poke2Label = ctk.CTkLabel(Main, text=str(value2).strip(), bg_color='white', font=('ariel', 30, 'bold'), text_color='red')
    Poke2Label.grid(column=1, row=3)
    
    value3 = value['poke3'].iloc[0]
    Poke3Label = ctk.CTkLabel(Main, text=str(value3).strip(), bg_color='white', font=('ariel', 30, 'bold'), text_color='red')
    Poke3Label.grid(column=1, row=4)
    
    value4 = value['poke4'].iloc[0]
    Poke4Label = ctk.CTkLabel(Main, text=str(value4).strip(), bg_color='white', font=('ariel', 30, 'bold'), text_color='red')
    Poke4Label.grid(column=1, row=5)

    value5 = value['poke5'].iloc[0]
    Poke5Label = ctk.CTkLabel(Main, text=str(value5).strip(), bg_color='white', font=('ariel', 30, 'bold'), text_color='red')
    Poke5Label.grid(column=1, row=6)
    
    value6 = value['poke6'].iloc[0]
    Poke6Label = ctk.CTkLabel(Main, text=str(value5).strip(), bg_color='white', font=('ariel', 30, 'bold'), text_color='red')
    Poke6Label.grid(column=1, row=7)
        
    button1 = ctk.CTkButton(Main, command=button1, text=f"Pokemon 1", fg_color='white', text_color='red', font=('ariel', 15, 'bold'), bg_color='red')
    button1.grid(row=2, column=2, padx=100, pady=20)

    button2 = ctk.CTkButton(Main, command=button2, text=f"Pokemon 2", fg_color='white', text_color='red', font=('ariel', 15, 'bold'), bg_color='red')
    button2.grid(row=3, column=2, padx=100, pady=20)

    button3 = ctk.CTkButton(Main, command=button3, text=f"Pokemon 3", fg_color='white', text_color='red', font=('ariel', 15, 'bold'), bg_color='red')
    button3.grid(row=4, column=2, padx=100, pady=20)

    button4 = ctk.CTkButton(Main, command=button4, text=f"Pokemon 4", fg_color='white', text_color='red', font=('ariel', 15, 'bold'), bg_color='red')
    button4.grid(row=5, column=2, padx=100, pady=20)

    button5 = ctk.CTkButton(Main, command=button5, text=f"Pokemon 5", fg_color='white', text_color='red', font=('ariel', 15, 'bold'), bg_color='red')
    button5.grid(row=6, column=2, padx=100, pady=20)

    button6 = ctk.CTkButton(Main, command=button6, text=f"Pokemon 6", fg_color='white', text_color='red', font=('ariel', 15, 'bold'), bg_color='red')
    button6.grid(row=7, column=2, padx=100, pady=20)

    OldImage = Image.open("pokedex2.png")
    scale = 0.5
    NewImage = new_size = (OldImage.width * scale, OldImage.height * scale)
    poke_image = ctk.CTkImage(light_image=OldImage, size=NewImage)
    PokeDictionary = ctk.CTkButton(Main, image=poke_image, text="", fg_color='white', bg_color='white', hover_color='grey', command=MoreInfoPls)
    PokeDictionary.grid(column=1, row=8)

    ShowThatItsAButtonSinceItsNotObvious = ctk.CTkLabel(Main, text='<-- Press here to see more data about a pokemon', font=('ariel', 20, 'bold'), bg_color='red', text_color='white')
    ShowThatItsAButtonSinceItsNotObvious.grid(column=2, row=8)

    # Tutorial #
    TutorialLabel = ctk.CTkLabel(Main, text='Select a pokemon To Replace', font=('ariel', 20, 'bold'), text_color='white', bg_color='red')
    TutorialLabel.grid(row=1, column=2)

    Main.mainloop()
