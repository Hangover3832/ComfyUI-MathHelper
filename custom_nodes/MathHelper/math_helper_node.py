"""MathHelper – Node-Implementierung für ComfyUI.

Bietet grundlegende mathematische Operationen als wiederverwendbaren Node.
"""

import math


class MathHelper:
    """Führt mathematische Operationen auf zwei Zahlen aus."""

    CATEGORY = "utils/math"
    DESCRIPTION = (
        "Grundlegende mathematische Operationen: Addition, Subtraktion, "
        "Multiplikation, Division, Potenz, Wurzel, Modulo und Runden."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.01}),
                "b": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.01}),
                "operation": (
                    [
                        "add",
                        "subtract",
                        "multiply",
                        "divide",
                        "power",
                        "sqrt_a",
                        "sqrt_b",
                        "modulo",
                        "round_a",
                        "round_b",
                        "floor",
                        "ceil",
                        "minimum",
                        "maximum",
                    ],
                    {"default": "add"},
                ),
            },
            "optional": {
                "clamp_result": ("BOOLEAN", {"default": False}),
                "clamp_min": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.01}),
                "clamp_max": ("FLOAT", {"default": 1.0, "min": -999999.0, "max": 999999.0, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("result", "result_int")
    FUNCTION = "compute"
    OUTPUT_TOOLTIPS = [
        "Das berechnete Ergebnis als Float.",
        "Das berechnete Ergebnis als Integer (abgerundet).",
    ]

    def compute(self, a: float, b: float, operation: str, clamp_result: bool = False,
                clamp_min: float = 0.0, clamp_max: float = 1.0):
        """Führt die gewählte Operation aus und gibt Ergebnis zurück."""
        result = self._apply_operation(a, b, operation)

        if clamp_result:
            result = max(clamp_min, min(clamp_max, result))

        return (result, int(round(result)))

    @staticmethod
    def _apply_operation(a: float, b: float, op: str) -> float:
        """Wendet die angegebene Operation auf a und b an."""
        ops = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: a / b if b != 0 else float("nan"),
            "power": lambda a, b: a ** b,
            "sqrt_a": lambda a, b: math.sqrt(a) if a >= 0 else float("nan"),
            "sqrt_b": lambda a, b: math.sqrt(b) if b >= 0 else float("nan"),
            "modulo": lambda a, b: a % b if b != 0 else float("nan"),
            "round_a": lambda a, b: round(a),
            "round_b": lambda a, b: round(b),
            "floor": lambda a, b: math.floor(a),
            "ceil": lambda a, b: math.ceil(a),
            "minimum": lambda a, b: min(a, b),
            "maximum": lambda a, b: max(a, b),
        }
        return ops[op](a, b)
