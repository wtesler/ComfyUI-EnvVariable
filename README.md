# ComfyUI-EnvVariable

Minimal ComfyUI custom node that reads an environment variable by key and outputs it as a string.

## Node

- Name: `Environment Variable`
- Input: `key` (STRING)
- Output: `value` (STRING)

At runtime, the node returns the value of `os.environ[key]` if it exists, otherwise it throws an exception.

## Usage

<img width="1214" height="556" alt="Usage" src="https://github.com/user-attachments/assets/e40d0b0b-f9e2-4214-935a-bbbdd234bef7" />

## Environment Variable Setup

### Windows

#### Option 1: Add an environment variable the basic way:
<img width="545" height="553.5" alt="Windows Environment Variable" src="https://github.com/user-attachments/assets/3fc439ca-6c6c-4d2d-99bd-43a43a3dfbcb" />

NOTE: You must completely close and re-open ComfyUI after adding/updating an environment variable in order for it to get picked up. Restarting from ComfyUI Manager is not good enough, you need to ensure the terminal window is closed and re-opened.

#### Option 2: Add environment variable to your ComfyUI bat script.

At the top of your run bat script, add:

`set MY_KEY=SOME_KEY`

### Linux / MacOS

1. At the top of your ComfyUI launch script, you can add environment variables like:

`export MY_KEY=SOME_KEY`

Generally this node will read from your environment variables in a normal manner.


