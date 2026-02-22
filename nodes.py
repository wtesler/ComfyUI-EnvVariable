class EnvVariableNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": (
                    "STRING",
                    {
                        "default": "ENV_VARIABLE_KEY",
                        "multiline": False,
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "utils"

    def get_value(self, key):
        import os

        if key not in os.environ:
            raise KeyError(f"Environment variable '{key}' was not found.")

        return (os.environ[key],)
