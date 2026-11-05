# Phone Wallpaper Generator

A Python command-line tool that uses the OpenAI API to write prompts for portrait-oriented phone wallpapers. It uses five examples to generate new fantasy scenes, each featuring an ordinary raccoon observing the scene. The output is a text prompt you can paste into an image generator.

## Setup

Clone the repository and install the dependencies.

```powershell
git clone https://github.com/alexslep04/Phone-Wallpaper-Generator.git
cd Phone-Wallpaper-Generator
python -m pip install openai requests
```

In [main.py](main.py), add `import os` with the other imports and replace the empty API key assignment with `openai.api_key = os.environ["OPENAI_API_KEY"]`. Then set the key for your current PowerShell session and run the script.

```powershell
$env:OPENAI_API_KEY = "your-api-key"
python main.py
```

The script sends requests to the Chat Completions API with `gpt-4` as the model. If your account uses a different model for Chat Completions, update the `model` field in `main.py`.

## How it works

1. The script sends five example prompts and instructions for generating a new portrait scene.
2. It prints the generated prompt and asks whether you approve it. Enter `y` to add it to the in-memory list.
3. Enter `y` again to generate another prompt, or any other response to exit.

The script builds the API input once at startup, so each request uses the original examples. Approved prompts are held in memory for the current session.

## Project files

| File | Purpose |
| --- | --- |
| [main.py](main.py) | Seed prompts, API request, and interactive generation loop |
| [prompts.txt](prompts.txt) | Reference prompts. The script uses the examples defined in `main.py`. |
| [delete.py](delete.py) and [values.ini](values.ini) | Standalone configuration example |
