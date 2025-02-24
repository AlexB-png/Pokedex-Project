import pandas as pd
import customtkinter as ctk
import requests
from PIL import Image
import io

Username = 'admin'

def PokemonImages():
    global Pokemon1Image
    with open('passwords.csv', 'r') as file:
        data = pd.read_csv(file)

    data = data.loc[data['username'] == Username]
    
    # Ensure the extracted Pokémon name is a clean string
    Poke1name = data['poke1'].iloc[0].strip()
    print(Poke1name)  # Debugging output

    url = f"https://pokeapi.co/api/v2/pokemon/{Poke1name}"
    
    url_response = requests.get(url)
    if url_response.status_code == 200:
        JsonFile = url_response.json()

        # Extract the sprite URL
        PokemonSprite = JsonFile['sprites']['front_default']
        
        # Fetch the image data
        PokemonSprite = requests.get(PokemonSprite)
        image_data = Image.open(io.BytesIO(PokemonSprite.content))

        # Initialize the GUI
        root = ctk.CTk()
        root.title(f"{Poke1name.capitalize()} Sprite")

        # Convert the image for CTkinter
        poke_image = ctk.CTkImage(light_image=image_data, size=(100, 100))

        # Create and place the label
        PokeActualImage = ctk.CTkLabel(root, text="", image=poke_image)
        PokeActualImage.pack(pady=20)

        root.mainloop()
    else:
        print('Failed to fetch Pokémon data')

PokemonImages()
