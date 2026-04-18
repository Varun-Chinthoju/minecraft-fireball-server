# FalixNodes Deployment Guide: Cross-Play Minigame Network

To deploy your server on free FalixNodes hosting, you need to split the Proxy and the Backend servers into two separate FalixNodes instances. This is because free plans have limited RAM and ports.

## Architecture
1.  **Server A: Proxy (Waterfall)**
    - RAM: 1GB - 2GB
    - Role: Entry point for Java, Bedrock, and Eaglercraft.
2.  **Server B: Backend (Paper 1.21)**
    - RAM: 2GB - 4GB
    - Role: Hosts the Lobby and Fireball Fight minigames.

---

## Step 1: Set Up Server A (Proxy)
1.  Create a new server on FalixNodes and select **Waterfall** as the software.
2.  **Ports (Crucial):**
    - Java: Default port (e.g., `25565`).
    - Bedrock: Go to the "Ports" tab and create a **UDP** port (e.g., `19132`).
    - Eaglercraft: Create another **TCP** port (e.g., `8081`).
3.  **Plugins:**
    - Upload `Geyser-BungeeCord.jar`, `floodgate-bungee.jar`, `ViaBungee.jar`, `EaglerXServer.jar`, and `EaglerMOTD.jar` to the `plugins/` folder.
    - Create a folder `plugins/ViaVersion/` and upload `ViaVersion.jar`, `ViaBackwards.jar`, and `ViaRewind.jar` inside it.
4.  **Configuration:**
    - In `config.yml`, set `ip_forward: true` and `online_mode: false`.
    - Under `servers:`, add the address of **Server B** (e.g., `server-b.falix.gg:25566`).
    - In `plugins/Geyser-BungeeCord/config.yml`, set `auth-type: floodgate` and update the Bedrock port to your assigned UDP port.
    - In `plugins/EaglercraftXServer/listeners.yml`, set `inject_address` to your proxy's main Java port and assigned WebSocket port.

## Step 2: Set Up Server B (Backend)
1.  Create a second server on FalixNodes and select **Paper 1.21** as the software.
2.  **Ports:** Use the default assigned TCP port (e.g., `25566`).
3.  **Plugins:**
    - Upload `AuthMe.jar`, `OldCombatMechanics.jar`, `ThrowableFireballs.jar`, and `FastAsyncWorldEdit.jar`.
4.  **Configuration:**
    - In `spigot.yml`, set `bungeecord: true`.
    - In `config/paper-global.yml`, set `proxies.bungee-cord.online-mode: false`.
    - In `server.properties`, set `online-mode=false`.

## Step 3: Link the Servers
1.  Restart Server B (Backend) first.
2.  Restart Server A (Proxy).
3.  Check the Proxy logs to ensure it successfully connected to Server B.

## Step 4: Loading Maps
1.  Upload `fireball_arena.schem` to Server B's `plugins/FastAsyncWorldEdit/schematics/` folder.
2.  Join the server and run:
    - `//schem load fireball_arena`
    - `//paste`
