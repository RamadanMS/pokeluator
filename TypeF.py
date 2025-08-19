import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io

# List of 30 Pokémon from Gen 1
pokemon_list = [
    "bulbasaur", "ivysaur", "venusaur",
    "charmander", "charmeleon", "charizard",
    "squirtle", "wartortle", "blastoise",
    "caterpie", "metapod", "butterfree",
    "weedle", "kakuna", "beedrill",
    "pidgey", "pidgeotto", "pidgeot",
    "rattata", "raticate", "spearow",
    "fearow", "ekans", "arbok",
    "pikachu", "raichu", "sandshrew",
    "sandslash", "nidoran-f"
]

# Function to fetch Pokémon data from PokeAPI
def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Function to update the Pokémon display
def update_pokemon(frame, pokemon_name):
    data = get_pokemon_data(pokemon_name)
    if data:
        # Show name
        name_label = tk.Label(frame, text=pokemon_name.capitalize(), font=("Arial", 14, "bold"))
        name_label.pack()

        # Show image
        img_url = data["sprites"]["front_default"]
        img_data = requests.get(img_url).content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((96, 96))
        img_tk = ImageTk.PhotoImage(img)

        img_label = tk.Label(frame, image=img_tk)
        img_label.image = img_tk
        img_label.pack()

        # Show abilities
        abilities = ", ".join([a["ability"]["name"].capitalize() for a in data["abilities"]])
        abilities_label = tk.Label(frame, text=f"Abilities: {abilities}", font=("Arial", 10))
        abilities_label.pack()

        # Show stats
        stats_dict = {stat['stat']['name']: stat['base_stat'] for stat in data["stats"]}
        stats_text = "\n".join([f"{k.capitalize()}: {v}" for k, v in stats_dict.items()])
        stats_label = tk.Label(frame, text=stats_text, font=("Arial", 10))
        stats_label.pack()

        return stats_dict
    else:
        tk.Label(frame, text="Error: Pokémon not found!", fg="red").pack()
        return None

# Function to compare Pokémon
def compare():
    for widget in left_frame.winfo_children():
        widget.destroy()
    for widget in right_frame.winfo_children():
        widget.destroy()
    for widget in middle_frame.winfo_children():
        widget.destroy()

    left_stats = update_pokemon(left_frame, left_choice.get())
    right_stats = update_pokemon(right_frame, right_choice.get())

    if left_stats and right_stats:
        tk.Label(middle_frame, text="Stat Differences", font=("Arial", 12, "bold")).pack()
        for stat in left_stats:
            diff = left_stats[stat] - right_stats[stat]
            diff_text = f"{stat.capitalize()}: {diff:+}"  # + shows sign
            color = "green" if diff > 0 else "red" if diff < 0 else "black"
            tk.Label(middle_frame, text=diff_text, fg=color).pack()

# Main window
root = tk.Tk()
root.title("Pokémon Comparison")
root.geometry("900x400")

# Dropdown selectors
left_choice = tk.StringVar()
right_choice = tk.StringVar()

left_dropdown = ttk.Combobox(root, textvariable=left_choice, values=pokemon_list)
left_dropdown.set(pokemon_list[0])
left_dropdown.grid(row=0, column=0, padx=10, pady=10)

right_dropdown = ttk.Combobox(root, textvariable=right_choice, values=pokemon_list)
right_dropdown.set(pokemon_list[1])
right_dropdown.grid(row=0, column=2, padx=10, pady=10)

# Frames for each Pokémon
left_frame = tk.Frame(root)
left_frame.grid(row=1, column=0, padx=20)

middle_frame = tk.Frame(root)
middle_frame.grid(row=1, column=1, padx=20)

right_frame = tk.Frame(root)
right_frame.grid(row=1, column=2, padx=20)

# Compare button
compare_button = tk.Button(root, text="Compare", command=compare)
compare_button.grid(row=0, column=1)

root.mainloop()