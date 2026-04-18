# Fireball Fight Server Implementation Plan

## Objective
Set up a Docker Compose-based Minecraft server architecture to host a "Fireball Fight" minigame with native support for Java Edition (1.20+), Bedrock Edition, and Eaglercraft (1.8.8).

## Key Files & Context
- `docker-compose.yml`: Defines the Proxy (BungeeCord/Velocity) and Backend (PaperMC) nodes.
- `proxy/plugins/`: GeyserMC, Floodgate, EaglerXBungee, ViaVersion, ViaBackwards, ViaRewind.
- `backend/plugins/`: FireballFite/ThrowableFireballs, OldCombatMechanics.

## Implementation Steps
1.  **Initialize Project Structure:**
    - Create directories for `proxy`, `proxy/plugins`, `backend`, and `backend/plugins`.
2.  **Create Docker Compose Configuration:**
    - Write a `docker-compose.yml` defining the Proxy and Backend services using open-source Minecraft Docker images (e.g., `itzg/minecraft-server` and `itzg/bungeecord`).
    - Expose necessary ports: `25565` (Java), `19132` (Bedrock/UDP), and `8081` (Eaglercraft WebSockets).
3.  **Configure Proxy Node:**
    - Configure BungeeCord/Velocity to forward connections to the Backend node.
    - Set up GeyserMC and Floodgate to allow Bedrock clients.
    - Set up EaglerXBungee for WebSocket connections.
    - Install ViaVersion, ViaBackwards, and ViaRewind to support Eaglercraft 1.8.8 clients.
4.  **Configure Backend Node:**
    - Set up PaperMC 1.20+.
    - Configure `spigot.yml` and `server.properties` for proxy forwarding (`bungeecord=true`).
    - Install and configure OldCombatMechanics to restore 1.8 PvP mechanics.
    - Install and configure the Fireball Fight plugin to manage arenas and fireball mechanics.
5.  **Final Review & Testing:**
    - Start the Docker network.
    - Verify server logs for errors and test connections from all three client types.

## Verification & Testing
- Both Docker containers must start cleanly without fatal plugin errors.
- Players from Java, Bedrock, and Eaglercraft must be able to join and interact in the same world.
- Fireball jumping and BedWars mechanics must function correctly with no weapon cooldowns (1.8 PvP).
