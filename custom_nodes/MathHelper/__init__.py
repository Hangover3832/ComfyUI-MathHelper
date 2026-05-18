"""MathHelper – Ein Beispiel-Custom-Node für ComfyUI.

Bietet grundlegende mathematische Operationen als wiederverwendbaren Node.
"""

from math_helper_node import MathHelper

NODE_CLASS_MAPPINGS = {
    "MathHelper": MathHelper,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MathHelper": "Math Helper",
}
