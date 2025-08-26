import tkinter as tk
from tkinter import ttk

# --- Pokémon Database (30 random Gen 1 Pokémon with abilities) ---
pokemon_db = [
    {"name": "Bulbasaur", "type": "Grass/Poison", "HP": 45, "Attack": 49, "Defense": 49, "Special": 65, "Speed": 45, "ability": "Overgrow"},
    {"name": "Charmander", "type": "Fire", "HP": 39, "Attack": 52, "Defense": 43, "Special": 50, "Speed": 65, "ability": "Blaze"},
    {"name": "Squirtle", "type": "Water", "HP": 44, "Attack": 48, "Defense": 65, "Special": 50, "Speed": 43, "ability": "Torrent"},
    {"name": "Pikachu", "type": "Electric", "HP": 35, "Attack": 55, "Defense": 30, "Special": 50, "Speed": 90, "ability": "Static"},
    {"name": "Jigglypuff", "type": "Normal", "HP": 115, "Attack": 45, "Defense": 20, "Special": 25, "Speed": 20, "ability": "Cute Charm"},
    {"name": "Meowth", "type": "Normal", "HP": 40, "Attack": 45, "Defense": 35, "Special": 40, "Speed": 90, "ability": "Pickup"},
    {"name": "Psyduck", "type": "Water", "HP": 50, "Attack": 52, "Defense": 48, "Special": 50, "Speed": 55, "ability": "Cloud Nine"},
    {"name": "Machop", "type": "Fighting", "HP": 70, "Attack": 80, "Defense": 50, "Special": 35, "Speed": 35, "ability": "Guts"},
    {"name": "Magnemite", "type": "Electric", "HP": 25, "Attack": 35, "Defense": 70, "Special": 95, "Speed": 45, "ability": "Magnet Pull"},
    {"name": "Gastly", "type": "Ghost/Poison", "HP": 30, "Attack": 35, "Defense": 30, "Special": 100, "Speed": 80, "ability": "Levitate"},
    {"name": "Onix", "type": "Rock/Ground", "HP": 35, "Attack": 45, "Defense": 160, "Special": 30, "Speed": 70, "ability": "Rock Head"},
    {"name": "Krabby", "type": "Water", "HP": 30, "Attack": 105, "Defense": 90, "Special": 25, "Speed": 50, "ability": "Hyper Cutter"},
    {"name": "Voltorb", "type": "Electric", "HP": 40, "Attack": 30, "Defense": 50, "Special": 55, "Speed": 100, "ability": "Soundproof"},
    {"name": "Exeggcute", "type": "Grass/Psychic", "HP": 60, "Attack": 40, "Defense": 80, "Special": 60, "Speed": 40, "ability": "Chlorophyll"},
    {"name": "Cubone", "type": "Ground", "HP": 50, "Attack": 50, "Defense": 95, "Special": 40, "Speed": 35, "ability": "Rock Head"},
    {"name": "Hitmonlee", "type": "Fighting", "HP": 50, "Attack": 120, "Defense": 53, "Special": 35, "Speed": 87, "ability": "Limber"},
    {"name": "Hitmonchan", "type": "Fighting", "HP": 50, "Attack": 105, "Defense": 79, "Special": 35, "Speed": 76, "ability": "Keen Eye"},
    {"name": "Rhyhorn", "type": "Ground/Rock", "HP": 80, "Attack": 85, "Defense": 95, "Special": 30, "Speed": 25, "ability": "Rock Head"},
    {"name": "Horsea", "type": "Water", "HP": 30, "Attack": 40, "Defense": 70, "Special": 70, "Speed": 60, "ability": "Swift Swim"},
    {"name": "Magikarp", "type": "Water", "HP": 20, "Attack": 10, "Defense": 55, "Special": 20, "Speed": 80, "ability": "Swift Swim"},
    {"name": "Lapras", "type": "Water/Ice", "HP": 130, "Attack": 85, "Defense": 80, "Special": 95, "Speed": 60, "ability": "Water Absorb"},
    {"name": "Ditto", "type": "Normal", "HP": 48, "Attack": 48, "Defense": 48, "Special": 48, "Speed": 48, "ability": "Limber"},
    {"name": "Eevee", "type": "Normal", "HP": 55, "Attack": 55, "Defense": 50, "Special": 45, "Speed": 55, "ability": "Adaptability"},
    {"name": "Vaporeon", "type": "Water", "HP": 130, "Attack": 65, "Defense": 60, "Special": 110, "Speed": 65, "ability": "Water Absorb"},
    {"name": "Jolteon", "type": "Electric", "HP": 65, "Attack": 65, "Defense": 60, "Special": 110, "Speed": 130, "ability": "Volt Absorb"},
    {"name": "Flareon", "type": "Fire", "HP": 65, "Attack": 130, "Defense": 60, "Special": 110, "Speed": 65, "ability": "Flash Fire"},
    {"name": "Snorlax", "type": "Normal", "HP": 160, "Attack": 110, "Defense": 65, "Special": 65, "Speed": 30, "ability": "Immunity"},
    {"name": "Articuno", "type": "Ice/Flying", "HP": 90, "Attack": 85, "Defense": 100, "Special": 125, "Speed": 85, "ability": "Pressure"},
    {"name": "Zapdos", "type": "Electric/Flying", "HP": 90, "Attack": 90, "Defense": 85, "Special": 125, "Speed": 100, "ability": "Pressure"},
    {"name": "Moltres", "type": "Fire/Flying", "HP": 90, "Attack": 100, "Defense": 90, "Special": 125, "Speed": 90, "ability": "Pressure"},
]

type_colors = {
    "Fire": "#FF6B6B",
    "Water": "#4FC3F7",
    "Grass": "#81C784",
    "Electric": "#FFF176",
    "Normal": "#E0E0E0",
    "Fighting": "#F08030",
    "Rock": "#BCAAA4",
    "Ground": "#D2B48C",
    "Ice": "#B3E5FC",
    "Ghost": "#9575CD",
    "Poison": "#CE93D8",
    "Psychic": "#F48FB1",
    "Flying": "#B3E5FC"
}

names = [p["name"] for p in pokemon_db]

def find_pokemon(name):
    return next(p for p in pokemon_db if p["name"] == name)

def draw_bar(parent, value, color):
    frame = tk.Frame(parent, bg="white", height=10)
    frame.pack(pady=1, fill="x")
    bar = tk.Frame(frame, bg=color, width=value, height=10)
    bar.pack(side="left")

def get_type_color(p_type):
    main_type = p_type.split("/")[0]
    return type_colors.get(main_type, "white")

def update_display():
    p1 = find_pokemon(combo1.get())
    p2 = find_pokemon(combo2.get())
    draw_pokemon(left_frame, p1)
    draw_pokemon(right_frame, p2)
    compare_stats(p1, p2)

def draw_pokemon(frame, p):
    for widget in frame.winfo_children():
        widget.destroy()
    bg_color = get_type_color(p["type"])
    frame.config(bg=bg_color)
    tk.Label(frame, text=p["name"], font=("Arial", 14, "bold"), bg=bg_color).pack()
    tk.Label(frame, text=p["type"], font=("Arial", 12), bg=bg_color).pack()
    tk.Label(frame, text=f"Ability: {p['ability']}", font=("Arial", 10), bg=bg_color).pack()
    for stat, color in zip(["HP", "Attack", "Defense", "Special", "Speed"],
                           ["green", "orange", "blue", "cyan", "purple"]):
        tk.Label(frame, text=f"{stat}: {p[stat]}", bg=bg_color).pack()
        draw_bar(frame, p[stat], color)

def compare_stats(p1, p2):
    total1 = sum(p1[s] for s in ["HP", "Attack", "Defense", "Special", "Speed"])
    total2 = sum(p2[s] for s in ["HP", "Attack", "Defense", "Special", "Speed"])
    better = p1["name"] if total1 > total2 else p2["name"]
    result_label.config(text=f"{better.upper()} IS BETTER!")

# --- GUI ---
root = tk.Tk()
root.title("Pokéluator (Gen-1 Edition)")

left_frame = tk.Frame(root, bd=2, relief="solid", width=200, height=300)
left_frame.grid(row=0, column=0, padx=20, pady=20)

center_frame = tk.Frame(root, bg="white", bd=2, relief="solid", width=200, height=100)
center_frame.grid(row=0, column=1, padx=20, pady=20)
result_label = tk.Label(center_frame, text="", font=("Arial", 14, "bold"), bg="white")
result_label.place(relx=0.5, rely=0.5, anchor="center")

right_frame = tk.Frame(root,_
