#!/usr/bin/env python3
import json

# Read the manifest
with open('artworks-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# Read new artworks
with open('new-artwork.json', 'r', encoding='utf-8') as f:
    new_artwork = json.load(f)

with open('new-game.json', 'r', encoding='utf-8') as f:
    new_game = json.load(f)

# Add new artworks to the beginning
manifest['artworks'].insert(0, new_artwork)
manifest['artworks'].insert(1, new_game)

# Write the updated manifest
with open('artworks-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("✅ マニフェストを更新しました")
print(f"総作品数: {len(manifest['artworks'])}作品")
