# ComfyUI-EnvVariable

Minimal ComfyUI custom node that reads an environment variable by key and outputs it as a string.

## Node

- Name: `Environment Variable`
- Input: `key` (STRING)
- Output: `value` (STRING)

At runtime, the node returns the value of `os.environ[key]` if it exists, otherwise an empty string.
