# Instructions for Lumina Network on TickHosting (Single Server)

1.  **Server Software:** Set your server to **Paper 1.21**.
2.  **Ports:**
    *   **Port 1 (Primary):** Use this for both Java and Bedrock (Geyser is set to "clone" this port).
    *   **Port 2 (Additional):** You MUST edit `plugins/EaglercraftXServer/listeners.yml` and change the port `8081` to your **Port 2**.
3.  **Upload:**
    *   Upload all contents of `dist/tickhosting_combined/plugins` to your server's `plugins` folder.
    *   Start the server, wait for it to load, then stop it to generate config folders.
4.  **Security:**
    *   Since it's a single server, AuthMe will handle login protection in the main world.
