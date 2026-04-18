#!/bin/bash

# Script to package Lumina Network for FalixNodes deployment
echo "Packaging Lumina Network for FalixNodes..."

DIST_DIR="dist"
PROXY_DIST="$DIST_DIR/falix_proxy"
BACKEND_DIST="$DIST_DIR/falix_backend"

# Clear old dist
rm -rf "$DIST_DIR"
mkdir -p "$PROXY_DIST" "$BACKEND_DIST"

# 1. Package Proxy
echo "Collecting Proxy files..."
cp -r proxy/plugins "$PROXY_DIST/"
cp proxy/config.yml "$PROXY_DIST/"
cp proxy/waterfall.yml "$PROXY_DIST/"
cp proxy/modules.yml "$PROXY_DIST/"
# Remove corrupted/temp files if any
rm -f "$PROXY_DIST/plugins/EaglercraftXBungee-Latest.jar"

# 2. Package Backend (Lobby & Minigames combined or separate?)
# On Falix free, usually you have 2 servers. 
# Let's assume Backend hosts both Lobby and Fireball for now to save a server, 
# or the user can split them.
echo "Collecting Backend files..."
cp -r backend/plugins "$BACKEND_DIST/"
cp -r backend/config "$BACKEND_DIST/"
cp backend/server.properties "$BACKEND_DIST/"
cp backend/spigot.yml "$BACKEND_DIST/"
cp backend/bukkit.yml "$BACKEND_DIST/"
# Include the generated maps
mkdir -p "$BACKEND_DIST/plugins/FastAsyncWorldEdit/schematics"
cp backend/plugins/FastAsyncWorldEdit/schematics/*.schem "$BACKEND_DIST/plugins/FastAsyncWorldEdit/schematics/"

# 3. Create Deployment Instructions
cp docs/falixnodes-deployment.md "$DIST_DIR/README.md"

echo "Zenith Network packaged in ./dist/"
echo "Instructions:"
echo "1. Upload falix_proxy contents to your Waterfall server."
echo "2. Upload falix_backend contents to your Paper server."
echo "3. Follow docs/falixnodes-deployment.md for port setup."
