# Flet Assets Server Example

A simple demonstration of how to use `flet-assets` to serve static files in your Flet applications.

## Overview

AssetsServer simplifies mobile development by serving local files over HTTP, enabling URL-based access for testing Flet apps on physical devices. Automatically detects your local IP for seamless multi-device access.

This example shows how to create a Flet application that uses `AssetsServer` to serve static assets like images and audio files from a local directory.

## Installation

First, install the required packages:

```bash
pip install flet-assets --upgrade
```

Make sure you have the latest version of `flet-assets` for the best experience.

## Project Structure

```
project/
├── main.py
└── src/
    └── assets/
        ├── icon.png
        └── mp3/
            └── anime/
                └── yamate.mp3
        └── ...other assets...
```

## Example Code

```python
import flet as ft
from flet_assets import AssetsServer

# Initialize the assets server pointing to your assets directory
server = AssetsServer(directory="src/assets")

def main(page: ft.Page):
    # Create an audio element pointing to a file in your assets
    audio = ft.Audio(src=f"{server.assets}/mp3/anime/yamate.mp3")
    page.overlay.append(audio)
    
    # Add an image and a button to play the audio
    page.add(
        ft.Image(src=f"{server.assets}/icon.png"),
        ft.Button("Play", on_click=lambda _: audio.play()),
    )

# Start the Flet app
ft.app(main)
```

## How It Works

1. `AssetsServer` automatically starts a FastAPI server on a separate thread
2. It detects your local IP address and chooses an available port (default: 1111)
3. Assets are served from the specified directory (`src/assets` in this example)
4. The `server.assets` property gives you the base URL to access your files
5. You can reference any file in your assets directory using this URL

## Customization

You can customize the server by providing additional parameters:

```python
server = AssetsServer(
    directory="path/to/assets",  # Path to your assets directory
    mount_path="/",              # URL path to mount the assets (default: /)
    port=3000,                   # Custom port number (default: 1111)
    verbose=True                 # Enable/disable detailed output (default: True)
)
```

## License

MIT