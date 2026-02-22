# ComfyUI-EnvVariable

Minimal ComfyUI custom node that reads an environment variable by key and outputs it as a string.

## Node

- Name: `Environment Variable`
- Input: `key` (`STRING`)
- Output: `value` (`STRING`)

Behavior:
- Returns `os.environ[key]` when present.
- Raises `KeyError` when the key is missing.

## Install

1. Clone into `ComfyUI/custom_nodes/`:

```bash
git clone https://github.com/wtesler/ComfyUI-EnvVariable.git
```

There are no additional requirements to install.

2. Search and download "ComfyUI-EnvVariable" from Custom Nodes Manager.

## Environment Variable Setup

Set the variable either in System Environment Variables or in your ComfyUI launch script (`set MY_KEY=...`).
Then fully close and relaunch ComfyUI so the process receives updated environment values.
