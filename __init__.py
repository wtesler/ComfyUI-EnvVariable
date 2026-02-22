from .nodes import EnvVariableNode


NODE_CLASS_MAPPINGS = {
    "Environment Variable": EnvVariableNode,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "Environment Variable": "Environment Variable",
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
