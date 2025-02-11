import customtkinter as ctk
import tkinter as tk
import hashlib
import pandas as pd
import requests
import math

LoginSuccess = False


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
    if data.empty is True:
        print("Fail")
        print(Password2)
    else:
        print("Success")
        LoginSuccess = True
        Login.destroy()


def PokeInput():
    global fail
    data = pd.read_csv('passwords.csv')
    print(data)
    Selection = PokeInputText.get('1.0', tk.END)
    PokeInputText.delete('1.0', tk.END)
    if Selection.strip() == "":
        print("Input a pokemon")
    else:
        URL = "https://pokeapi.co/api/v2/pokemon/" + Selection.strip()
        Response = requests.get(URL)
        if Response.status_code != 200:
            print(Response.status_code)
            print("Server does not exist")
            fail = True
        else:
            fail = False
        if fail is False:
            Number = 1
            local = 'This is just here so the loop doesn"t break lmao'
            while pd.isna(local) is False and Number < 7:
                loca = ((f"poke{Number}").strip())
                local = data[loca].iloc[0]
                if pd.isna(local) is True:
                    Replaced = data.loc[Username, Number] = Selection
                    print(Replaced)
                    print("Empty")
                else:
                    Number += 1


def NewPokemon():
    KillPokemon = ctk.CTkToplevel()
    KillPokemon.title('"Replace" a pokemon')


# Login Window #
Login = ctk.CTk()
Login.geometry("400x600")

# Labels #
UsernameLabel = ctk.CTkLabel(Login, text="Username:")
PasswordLabel = ctk.CTkLabel(Login, text="Password:")

# Input Button #
EnterButton = ctk.CTkButton(Login, text="Login", command=LoginButton)

# Entry Boxes #
UsernameEntry = ctk.CTkEntry(Login)
PasswordEntry = ctk.CTkEntry(Login)

# Grid the modules #
UsernameLabel.grid(row=0, column=0)
PasswordLabel.grid(row=1, column=0, pady=20)

UsernameEntry.grid(row=0, column=1)
PasswordEntry.grid(row=1, column=1)

EnterButton.grid(row=2, column=0)

Login.mainloop()

if LoginSuccess is True:
    Main = ctk.CTk()
    Main.geometry('1000x1000')

    Main.rowconfigure(0, weight=0)
    Main.rowconfigure(1, weight=0)
    Main.rowconfigure(2, weight=0)
    Main.rowconfigure(3, weight=0)
    for i in range(1,5):
        Main.columnconfigure(i, weight=1)

    # Welcome Label #
    Welcome = ctk.CTkLabel(Main, text=f"Welcome", font=('arial', 45))
    Welcome.grid(row=0, column=0, sticky='ew')
    Welcome2 = ctk.CTkLabel(Main, text=Username, font=('arial', 45), text_color='lime')
    Welcome2.grid(row=0, column=1, sticky='ew')

    # Input Pokemon #
    PokeLabel = ctk.CTkLabel(Main, text="Input Pokemon here:", pady=50)
    PokeLabel.grid(row=1, column=0)
    PokeInputText = ctk.CTkTextbox(Main, width=300, height=10)
    PokeInputText.grid(row=1, column=1)
    PokeInputButton = ctk.CTkButton(Main, text="Enter", command=PokeInput)
    PokeInputButton.grid(row=1, column=2)

    # Labels for pokemon #
    PokeLabelArray = ['Label1','Label2','Label3','Label4','Label5','Label6']
    for i in PokeLabelArray:
        for x in range(1,7):
            i = ctk.CTkLabel(Main, text=f"Pokemon {x}:", font=('arial', 25))
            i.grid(row=x+1, column=0)

    SelectPokeArray = ['poke1','poke2','poke3','poke4','poke5','poke6']
    rowselect=2
    for i in SelectPokeArray:
        value = data[i].iloc[0]
        value = str(value)
        print(value)
        label = ctk.CTkLabel(Main, text=value, font=('arial', 25))
        label.grid(row=rowselect, column=1, padx=100)
        rowselect += 1
    Main.mainloop()
