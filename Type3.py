import tkinter as tk
from tkinter import ttk

# Pokémon data (name: [hp, attack, defense, special, speed, type1, type2, (ability1, desc1), (ability2, desc2)])
pokemon_data = {
    "Bulbasaur": [45, 49, 49, 65, 45, "Grass", "Poison", 
                 ("Overgrow", "Powers up Grass-type moves when HP is low"), 
                 ("", "")],
    "Ivysaur": [60, 62, 63, 80, 60, "Grass", "Poison", 
               ("Overgrow", "Powers up Grass-type moves when HP is low"), 
               ("", "")],
    "Venusaur": [80, 82, 83, 100, 80, "Grass", "Poison", 
                ("Overgrow", "Powers up Grass-type moves when HP is low"), 
                ("Chlorophyll", "Boosts Speed in sunshine")],
    "Charmander": [39, 52, 43, 60, 65, "Fire", "", 
                  ("Blaze", "Powers up Fire-type moves when HP is low"), 
                  ("", "")],
    "Charmeleon": [58, 64, 58, 80, 80, "Fire", "", 
                  ("Blaze", "Powers up Fire-type moves when HP is low"), 
                  ("", "")],
    "Charizard": [78, 84, 78, 109, 100, "Fire", "Flying", 
                 ("Blaze", "Powers up Fire-type moves when HP is low"), 
                 ("", "")],
    "Squirtle": [44, 48, 65, 50, 43, "Water", "", 
                ("Torrent", "Powers up Water-type moves when HP is low"), 
                ("", "")],
    "Wartortle": [59, 63, 80, 65, 58, "Water", "", 
                 ("Torrent", "Powers up Water-type moves when HP is low"), 
                 ("", "")],
    "Blastoise": [79, 83, 100, 85, 78, "Water", "", 
                 ("Torrent", "Powers up Water-type moves when HP is low"), 
                 ("Rain Dish", "Gradually recovers HP in rain")],
    "Pikachu": [35, 55, 40, 50, 90, "Electric", "", 
               ("Static", "May paralyze opponents on contact"), 
               ("Lightning Rod", "Draws in all Electric-type moves to boost Sp. Atk")],
    "Raichu": [60, 90, 55, 90, 110, "Electric", "", 
              ("Static", "May paralyze opponents on contact"), 
              ("", "")],
    "Nidoran♂": [46, 57, 40, 40, 50, "Poison", "", 
                ("Poison Point", "May poison opponents on contact"), 
                ("Rivalry", "Deals more damage to same gender opponents")],
    "Nidorino": [61, 72, 57, 55, 65, "Poison", "", 
                ("Poison Point", "May poison opponents on contact"), 
                ("Rivalry", "Deals more damage to same gender opponents")],
    "Nidoking": [81, 102, 77, 75, 85, "Poison", "Ground", 
                ("Poison Point", "May poison opponents on contact"), 
                ("Rivalry", "Deals more damage to same gender opponents")],
    "Clefairy": [70, 45, 48, 60, 35, "Fairy", "", 
                ("Cute Charm", "May infatuate opponents on contact"), 
                ("Magic Guard", "Only takes damage from attacks")],
    "Clefable": [95, 70, 73, 95, 60, "Fairy", "", 
                ("Cute Charm", "May infatuate opponents on contact"), 
                ("Magic Guard", "Only takes damage from attacks")],
    "Vulpix": [38, 41, 40, 65, 65, "Fire", "", 
              ("Flash Fire", "Powers up Fire moves if hit by one"), 
              ("Drought", "Summons sunlight when entering battle")],
    "Ninetales": [73, 76, 75, 100, 100, "Fire", "", 
                 ("Flash Fire", "Powers up Fire moves if hit by one"), 
                 ("Drought", "Summons sunlight when entering battle")],
    "Jigglypuff": [115, 45, 20, 45, 20, "Normal", "Fairy", 
                  ("Cute Charm", "May infatuate opponents on contact"), 
                  ("Competitive", "Sharply raises Sp. Atk when stats are lowered")],
    "Wigglytuff": [140, 70, 45, 85, 45, "Normal", "Fairy", 
                  ("Cute Charm", "May infatuate opponents on contact"), 
                  ("Competitive", "Sharply raises Sp. Atk when stats are lowered")],
    "Zubat": [40, 45, 35, 40, 55, "Poison", "Flying", 
             ("Inner Focus", "Prevents flinching"), 
             ("", "")],
    "Golbat": [75, 80, 70, 75, 90, "Poison", "Flying", 
              ("Inner Focus", "Prevents flinching"), 
              ("", "")],
    "Oddish": [45, 50, 55, 75, 30, "Grass", "Poison", 
              ("Chlorophyll", "Boosts Speed in sunshine"), 
              ("", "")],
    "Gloom": [60, 65, 70, 85, 40, "Grass", "Poison", 
             ("Chlorophyll", "Boosts Speed in sunshine"), 
             ("", "")],
    "Vileplume": [75, 80, 85, 110, 50, "Grass", "Poison", 
                 ("Chlorophyll", "Boosts Speed in sunshine"), 
                 ("Effect Spore", "May cause status on contact")],
    "Paras": [35, 70, 55, 55, 25, "Bug", "Grass", 
             ("Effect Spore", "May cause status on contact"), 
             ("Dry Skin", "Heals in rain, hurt by sun/fire")],
    "Parasect": [60, 95, 80, 80, 30, "Bug", "Grass", 
                ("Effect Spore", "May cause status on contact"), 
                ("Dry Skin", "Heals in rain, hurt by sun/fire")],
    "Venonat": [60, 55, 50, 40, 45, "Bug", "Poison", 
               ("Compound Eyes", "Increases move accuracy"), 
               ("Tinted Lens", "Powers up 'not very effective' moves")],
    "Venomoth": [70, 65, 60, 90, 90, "Bug", "Poison", 
                ("Shield Dust", "Prevents added effects of moves"), 
                ("Tinted Lens", "Powers up 'not very effective' moves")],
    "Diglett": [10, 55, 25, 45, 95, "Ground", "", 
               ("Sand Veil", "Boosts evasion in sandstorms"), 
               ("Arena Trap", "Prevents opponents from fleeing")]
}

class PokemonComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gen 1 Pokémon Comparison Tool")
        self.root.geometry("1000x700")
        
        # Set style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Stat.TLabel', font=('Arial', 10, 'bold'))
        self.style.configure('Ability.TLabel', font=('Arial', 9), wraplength=150)
        
        # Create main frames
        self.header_frame = ttk.Frame(root)
        self.header_frame.pack(pady=10)
        
        self.comparison_frame = ttk.Frame(root)
        self.comparison_frame.pack(pady=10)
        
        self.pokemon1_frame = ttk.Frame(self.comparison_frame)
        self.pokemon1_frame.grid(row=0, column=0, padx=20)
        
        self.vs_frame = ttk.Frame(self.comparison_frame)
        self.vs_frame.grid(row=0, column=1, padx=20)
        
        self.pokemon2_frame = ttk.Frame(self.comparison_frame)
        self.pokemon2_frame.grid(row=0, column=2, padx=20)
        
        # Header
        ttk.Label(self.header_frame, text="Pokémon Gen 1 Comparison Tool", style='Header.TLabel').pack()
        
        # VS label
        ttk.Label(self.vs_frame, text="VS", style='Header.TLabel').pack(pady=50)
        
        # Dropdown menus
        self.pokemon1_var = tk.StringVar()
        self.pokemon2_var = tk.StringVar()
        
        self.pokemon1_dropdown = ttk.Combobox(self.pokemon1_frame, textvariable=self.pokemon1_var, 
                                             values=list(pokemon_data.keys()), width=15)
        self.pokemon1_dropdown.pack(pady=5)
        self.pokemon1_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_pokemon_display(1))
        
        self.pokemon2_dropdown = ttk.Combobox(self.pokemon2_frame, textvariable=self.pokemon2_var, 
                                             values=list(pokemon_data.keys()), width=15)
        self.pokemon2_dropdown.pack(pady=5)
        self.pokemon2_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_pokemon_display(2))
        
        # Set default Pokémon
        self.pokemon1_var.set("Bulbasaur")
        self.pokemon2_var.set("Charmander")
        
        # Pokémon display areas
        self.pokemon1_display = ttk.Frame(self.pokemon1_frame)
        self.pokemon1_display.pack(pady=10)
        
        self.pokemon2_display = ttk.Frame(self.pokemon2_frame)
        self.pokemon2_display.pack(pady=10)
        
        # Initialize displays
        self.update_pokemon_display(1)
        self.update_pokemon_display(2)
        
        # Compare button
        ttk.Button(self.header_frame, text="Compare", command=self.compare_stats).pack(pady=10)
        
        # Stats comparison frame
        self.stats_comparison_frame = ttk.Frame(root)
        self.stats_comparison_frame.pack(pady=10)
        
    def update_pokemon_display(self, pokemon_num):
        if pokemon_num == 1:
            pokemon_name = self.pokemon1_var.get()
            display_frame = self.pokemon1_display
        else:
            pokemon_name = self.pokemon2_var.get()
            display_frame = self.pokemon2_display
        
        # Clear previous display
        for widget in display_frame.winfo_children():
            widget.destroy()
        
        if pokemon_name not in pokemon_data:
            return
            
        data = pokemon_data[pokemon_name]
        
        # Pokémon name
        ttk.Label(display_frame, text=pokemon_name, style='Header.TLabel').pack()
        
        # Pokémon image (placeholder)
        try:
            color = self.get_type_color(data[5])
            img_frame = tk.Frame(display_frame, width=150, height=150, bg=color)
            img_frame.pack_propagate(False)
            img_frame.pack(pady=5)
            ttk.Label(img_frame, text=pokemon_name, background=color).pack(expand=True)
        except Exception as e:
            print(f"Error loading image: {e}")
        
        # Pokémon type(s)
        type_text = data[5]
        if data[6]:
            type_text += f" / {data[6]}"
        ttk.Label(display_frame, text=type_text).pack()
        
        # Stats
        stats_frame = ttk.Frame(display_frame)
        stats_frame.pack(pady=5)
        
        stat_names = ["HP", "Attack", "Defense", "Special", "Speed"]
        for i, stat in enumerate(stat_names):
            ttk.Label(stats_frame, text=f"{stat}:", style='Stat.TLabel').grid(row=i, column=0, sticky='e')
            ttk.Label(stats_frame, text=data[i]).grid(row=i, column=1, sticky='w')
        
        # Abilities with descriptions
        abilities_frame = ttk.Frame(display_frame)
        abilities_frame.pack(pady=5)
        
        ttk.Label(abilities_frame, text="Abilities:", style='Stat.TLabel').grid(row=0, column=0, sticky='ne')
        
        ability1_name, ability1_desc = data[7]
        ability2_name, ability2_desc = data[8]
        
        if ability1_name:
            ttk.Label(abilities_frame, text=f"{ability1_name}:", style='Stat.TLabel').grid(row=1, column=0, sticky='e')
            ttk.Label(abilities_frame, text=ability1_desc, style='Ability.TLabel').grid(row=1, column=1, sticky='w')
        
        if ability2_name:
            ttk.Label(abilities_frame, text=f"{ability2_name}:", style='Stat.TLabel').grid(row=2, column=0, sticky='e')
            ttk.Label(abilities_frame, text=ability2_desc, style='Ability.TLabel').grid(row=2, column=1, sticky='w')
    
    def compare_stats(self):
        # Clear previous comparison
        for widget in self.stats_comparison_frame.winfo_children():
            widget.destroy()
        
        pokemon1 = self.pokemon1_var.get()
        pokemon2 = self.pokemon2_var.get()
        
        if pokemon1 not in pokemon_data or pokemon2 not in pokemon_data:
            return
            
        data1 = pokemon_data[pokemon1]
        data2 = pokemon_data[pokemon2]
        
        # Comparison table
        ttk.Label(self.stats_comparison_frame, text="Stats Comparison", style='Header.TLabel').pack()
        
        # Create comparison table
        comparison_table = ttk.Frame(self.stats_comparison_frame)
        comparison_table.pack(pady=10)
        
        # Headers
        ttk.Label(comparison_table, text="Stat", style='Stat.TLabel').grid(row=0, column=0, padx=5)
        ttk.Label(comparison_table, text=pokemon1, style='Stat.TLabel').grid(row=0, column=1, padx=5)
        ttk.Label(comparison_table, text=pokemon2, style='Stat.TLabel').grid(row=0, column=2, padx=5)
        ttk.Label(comparison_table, text="Difference", style='Stat.TLabel').grid(row=0, column=3, padx=5)
        
        # Stats rows
        stat_names = ["HP", "Attack", "Defense", "Special", "Speed"]
        for i, stat in enumerate(stat_names):
            ttk.Label(comparison_table, text=stat).grid(row=i+1, column=0, padx=5, sticky='e')
            ttk.Label(comparison_table, text=data1[i]).grid(row=i+1, column=1, padx=5)
            ttk.Label(comparison_table, text=data2[i]).grid(row=i+1, column=2, padx=5)
            
            diff = data1[i] - data2[i]
            diff_text = f"{'+' if diff > 0 else ''}{diff}"
            color = "green" if diff > 0 else "red" if diff < 0 else "black"
            ttk.Label(comparison_table, text=diff_text, foreground=color).grid(row=i+1, column=3, padx=5)
    
    def get_type_color(self, pokemon_type):
        type_colors = {
            "Normal": "#A8A878",
            "Fire": "#F08030",
            "Water": "#6890F0",
            "Electric": "#F8D030",
            "Grass": "#78C850",
            "Ice": "#98D8D8",
            "Fighting": "#C03028",
            "Poison": "#A040A0",
            "Ground": "#E0C068",
            "Flying": "#A890F0",
            "Psychic": "#F85888",
            "Bug": "#A8B820",
            "Rock": "#B8A038",
            "Ghost": "#705898",
            "Dragon": "#7038F8",
            "Dark": "#705848",
            "Steel": "#B8B8D0",
            "Fairy": "#EE99AC"
        }
        return type_colors.get(pokemon_type, "#777777")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonComparisonApp(root)
    root.mainloop()