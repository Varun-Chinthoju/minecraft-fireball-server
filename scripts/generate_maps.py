import mcschematic
import os

def generate_arena(name, teams, output_dir):
    schem = mcschematic.MCSchematic()
    
    # 1. Generate Center Island (8x8 stone/grass)
    for x in range(-4, 4):
        for z in range(-4, 4):
            for y in range(-2, 0):
                schem.setBlock((x, y, z), "minecraft:stone")
            schem.setBlock((x, 0, z), "minecraft:grass_block")

    # 2. Generate Team Islands
    for team in teams:
        tx, ty, tz = team["pos"]
        # Small 5x5 platform
        for dx in range(-2, 3):
            for dz in range(-2, 3):
                schem.setBlock((tx + dx, ty - 1, tz + dz), team["color"])
        
        # Place a "Bed" (Red Bed as placeholder for minigame logic)
        schem.setBlock((tx, ty, tz), "minecraft:red_bed[part=foot,facing=north]")
        schem.setBlock((tx, ty, tz - 1), "minecraft:red_bed[part=head,facing=north]")

    # 3. Save the schematic
    schem.save(output_dir, name, mcschematic.Version.JE_1_21)
    print(f"Schematic saved to {output_dir}/{name}.schem")

def main():
    output_dir = "backend/plugins/FastAsyncWorldEdit/schematics"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1v1 Mode
    teams_1v1 = [
        {"name": "red", "color": "red_wool", "pos": (20, 0, 0)},
        {"name": "blue", "color": "blue_wool", "pos": (-20, 0, 0)}
    ]
    generate_arena("fireball_1v1", teams_1v1, output_dir)

    # 4-Player Mode
    teams_4p = [
        {"name": "red", "color": "red_wool", "pos": (20, 0, 0)},
        {"name": "blue", "color": "blue_wool", "pos": (-20, 0, 0)},
        {"name": "green", "color": "green_wool", "pos": (0, 0, 20)},
        {"name": "yellow", "color": "yellow_wool", "pos": (0, 0, -20)}
    ]
    generate_arena("fireball_4p", teams_4p, output_dir)

if __name__ == "__main__":
    main()
