class EnvVariableNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": (
                    "STRING",
                    {
                        "default": "OPENAI_API_KEY",
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

        return (os.environ.get(key, ""),)
