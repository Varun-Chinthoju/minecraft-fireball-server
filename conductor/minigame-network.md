# Minigame Network Server Plan

## Objective
Evolve the current Fireball Fight server into a full Minigame Network with a dedicated Lobby server. The setup will be prepared for deployment on two separate free FalixNodes servers (Proxy vs. Backend) and include automated map generation using the `mcschematic` Python library.

## Key Files & Context
- `docker-compose.yml`: Will be updated to include a `lobby` server alongside the `proxy` and `backend` (minigame) servers for local development.
- `proxy/config.yml`: Will route players to the new `lobby` server first.
- `scripts/generate_maps.py`: A Python script using `mcschematic` to generate Fireball Fight arena schematics (islands, beds, spawns).
- `docs/falixnodes-deployment.md`: Instructions on how to deploy this exact setup to free FalixNodes hosting.
- `backend/plugins/`: Will now include FastAsyncWorldEdit (FAWE) for loading generated `.schem` files in-game.

## Implementation Steps
1.  **Add Lobby Server for Local Development:**
    - Update `docker-compose.yml` to add a `lobby` container running Paper 1.21.
    - Set up a basic `lobby` folder with necessary plugins (AuthMe will be moved here, plus a server selector/NPC plugin).
2.  **Update BungeeCord Routing:**
    - Modify `proxy/config.yml` to set `lobby` as the default server and fallback server.
    - Add the `lobby` and `backend` to the proxy's server list.
3.  **Install FAWE (FastAsyncWorldEdit):**
    - Add FAWE to the backend node so generated `.schem` files can be pasted and tested in-game (`//schem load` and `//paste`).
4.  **Generate Minigame Maps (mcschematic):**
    - Create a Python virtual environment and install `mcschematic`.
    - Write a script (`generate_maps.py`) that procedurally generates a 4-team Fireball Fight map.
    - The script will build a center island (e.g., stone/grass), 4 wool-themed team islands (Red, Blue, Green, Yellow), and place bed placeholders.
    - Run the script to output a `.schem` file directly into `backend/plugins/FastAsyncWorldEdit/schematics/`.
5.  **Create FalixNodes Deployment Guide:**
    - Write a detailed Markdown guide (`docs/falixnodes-deployment.md`) explaining how to split this setup into two free FalixNodes servers (Server A: Waterfall Proxy, Server B: Paper Minigames).
    - Include steps for SFTP upload, port allocation (crucial for Geyser UDP and Eaglercraft WebSockets), and BungeeCord IP forwarding on FalixNodes.

## Verification & Testing
- The Docker Compose network spins up all 3 containers (Proxy, Lobby, Backend).
- Connecting to the proxy lands the player in the Lobby.
- The Python script successfully generates a valid `.schem` file that can be loaded in-game via FAWE.
- The FalixNodes guide covers all necessary port configurations for Java, Bedrock, and Eaglercraft cross-play.
