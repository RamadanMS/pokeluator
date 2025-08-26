import tkinter as tk
from tkinter import ttk

# Pokémon data (name: [hp, attack, defense, special, speed, type, (ability, desc)])
pokemon_data = {
    "Bulbasaur": [45, 49, 49, 65, 45, "Grass", ("Overgrow", "Powers up Grass moves by 1.5× if HP is low")],
    "Charmander": [39, 52, 43, 55, 65, "Fire", ("Blaze", "Powers up Fire moves by 1.5× if HP is low")],
    "Squirtle": [44, 48, 65, 57, 43, "Water", ("Torrent", "Powers up Water moves by 1.5× if HP is low")],
    "Pikachu": [35, 55, 40, 50, 90, "Electric", ("Static", "May paralyze on contact")],
    "Jigglypuff": [115, 45, 20, 45, 20, "Normal", ("Cute Charm", "May infatuate on contact")],
    "Gengar": [60, 65, 60, 130, 110, "Ghost", ("Levitate", "Not affected by Ground moves")]
}

class PokeLuatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokéluator (GEN-1 Edition)")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")
        
        # Header
        header = ttk.Label(root, text="Pokéluator", font=("Arial", 24, "bold"), background="#f0f0f0")
        header.pack(pady=10)
        subheader = ttk.Label(root, text="GEN-1 Edition", font=("Arial", 16), background="#f0f0f0")
        subheader.pack()
        
        # Dropdown menus (moved up to ensure they're created first)
        self.pokemon1_var = tk.StringVar()
        self.pokemon2_var = tk.StringVar()
        
        self.pokemon1_dropdown = ttk.Combobox(root, textvariable=self.pokemon1_var, 
                                            values=list(pokemon_data.keys()), width=15)
        self.pokemon1_dropdown.pack(pady=10)
        
        self.pokemon2_dropdown = ttk.Combobox(root, textvariable=self.pokemon2_var, 
                                            values=list(pokemon_data.keys()), width=15)
        self.pokemon2_dropdown.pack(pady=10)
        
        # Comparison frame
        self.comparison_frame = ttk.Frame(root)
        self.comparison_frame.pack(pady=20)
        
        # Pokémon 1 frame
        self.pokemon1_frame = ttk.Frame(self.comparison_frame, padding=20)
        self.pokemon1_frame.grid(row=0, column=0, padx=20)
        
        # VS label
        vs_label = ttk.Label(self.comparison_frame, text="VS", font=("Arial", 24, "bold"), background="#f0f0f0")
        vs_label.grid(row=0, column=1, padx=20)
        
        # Pokémon 2 frame
        self.pokemon2_frame = ttk.Frame(self.comparison_frame, padding=20)
        self.pokemon2_frame.grid(row=0, column=2, padx=20)
        
        # Result label (created before any methods might try to use it)
        self.result_label = ttk.Label(root, text="", font=("Arial", 16, "bold"), background="#f0f0f0")
        self.result_label.pack(pady=20)
        
        # Set default Pokémon
        self.pokemon1_var.set("Charmander")
        self.pokemon2_var.set("Squirtle")
        
        # Bind events after all widgets are created
        self.pokemon1_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_pokemon_display(1))
        self.pokemon2_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_pokemon_display(2))
        
        # Initialize displays
        self.update_pokemon_display(1)
        self.update_pokemon_display(2)
    
    def update_pokemon_display(self, pokemon_num):
        if pokemon_num == 1:
            pokemon_name = self.pokemon1_var.get()
            display_frame = self.pokemon1_frame
            bg_color = "#ffcccc"  # Light red
        else:
            pokemon_name = self.pokemon2_var.get()
            display_frame = self.pokemon2_frame
            bg_color = "#ccccff"  # Light blue
        
        # Clear previous display
        for widget in display_frame.winfo_children():
            widget.destroy()
        
        if pokemon_name not in pokemon_data:
            return
            
        data = pokemon_data[pokemon_name]
        
        # Configure frame background
        self.style = ttk.Style()
        self.style.configure('Custom.TFrame', background=bg_color)
        display_frame.configure(style='Custom.TFrame')
        
        # Pokémon type header
        type_header = ttk.Label(display_frame, text=data[5], font=("Arial", 14, "bold"), 
                              background=bg_color)
        type_header.pack()
        
        # Pokémon name
        name_label = ttk.Label(display_frame, text=pokemon_name, font=("Arial", 18, "bold"), 
                             background=bg_color)
        name_label.pack(pady=5)
        
        # Stats
        stats_frame = ttk.Frame(display_frame, style='Custom.TFrame')
        stats_frame.pack(pady=10)
        
        stat_names = ["HP", "Attack", "Defense", "Special", "Speed"]
        for i, stat in enumerate(stat_names):
            ttk.Label(stats_frame, text=f"{stat}: {data[i]}", font=("Arial", 12), 
                     background=bg_color).grid(row=i, column=0, sticky='w', pady=2)
        
        # Ability
        ability_frame = ttk.Frame(display_frame, style='Custom.TFrame')
        ability_frame.pack(pady=10)
        
        ability_name, ability_desc = data[6]
        ttk.Label(ability_frame, text=ability_name, font=("Arial", 12, "bold"), 
                 background=bg_color).pack()
        ttk.Label(ability_frame, text=ability_desc, font=("Arial", 10), wraplength=200, 
                 background=bg_color).pack()
        
        # Update comparison result
        self.compare_pokemon()
    
    def compare_pokemon(self):
        pokemon1 = self.pokemon1_var.get()
        pokemon2 = self.pokemon2_var.get()
        
        if pokemon1 not in pokemon_data or pokemon2 not in pokemon_data:
            return
        
        data1 = pokemon_data[pokemon1]
        data2 = pokemon_data[pokemon2]
        
        # Simple comparison - sum of stats
        total1 = sum(data1[:5])
        total2 = sum(data2[:5])
        
        if total1 > total2:
            result = f"{pokemon1.upper()} IS BETTER!"
        elif total2 > total1:
            result = f"{pokemon2.upper()} IS BETTER!"
        else:
            result = "IT'S A TIE!"
        
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = PokeLuatorApp(root)
    root.mainloop()