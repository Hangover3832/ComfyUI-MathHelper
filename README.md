# ComfyUI MathHelper – Custom Node

Ein **ComfyUI Custom Node** für grundlegende mathematische Operationen.
Erhältlich als wiederverwendbarer Knoten im ComfyUI Node-Menü.

## Funktionen

| # | Operation | Beschreibung |
|---|-----------|--------------|
| 1 | **add** | Addition (a + b) |
| 2 | **subtract** | Subtraktion (a − b) |
| 3 | **multiply** | Multiplikation (a × b) |
| 4 | **divide** | Division (a ÷ b) |
| 5 | **power** | Potenz (aᵇ) |
| 6 | **sqrt_a** | Quadratwurzel von a |
| 7 | **sqrt_b** | Quadratwurzel von b |
| 8 | **modulo** | Modulo (a % b) |
| 9 | **round_a** | a auf nächste Ganze runden |
| 10 | **round_b** | b auf nächste Ganze runden |
| 11 | **floor** | Floor von a |
| 12 | **ceil** | Ceiling von a |
| 13 | **minimum** | Minimum von a und b |
| 14 | **maximum** | Maximum von a und b |

### Outputs
- **result** — Float-Ergebnis
- **result_int** — Integer-Ergebnis (gerundet)

### Optional: Clamping
Ergebnis kann auf einen Wertebereich beschränkt werden (z.B. 0.0–1.0 für Helligkeits-Werte).

## Installation

### Methode 1: ComfyUI Manager (Empfohlen)

1. Öffne ComfyUI Manager
2. Suche nach **`ComfyUI-MathHelper`**
3. Klicke auf **Install**
4. Starte ComfyUI neu

### Methode 2: Manuelles Installation

Klon das Repository direkt in den `custom_nodes`-Ordner:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Hangover3832/ComfyUI-MathHelper.git
cd MathHelper
pip install -e .
```

Dann ComfyUI neu starten.

## Verwendung

1. Füge den Node über **Add Node** → **`utils/math`** → **`Math Helper`** hinzu
2. Gib zwei Zahlen (`a` und `b`) ein
3. Wähle eine Operation
4. Optional: Aktiviere Clamping für Wertebereich-Beschränkung

## Node-Screenshot (Beschreibung)

```
┌─────────────────────────────────────────┐
│ Math Helper                             │
│                                         │
│  a:        [ 42.00 ]  ◀ FLOAT          │
│  b:        [  7.00 ]  ◀ FLOAT          │
│  operation: [ add      ]  ◀ Auswahl     │
│  clamp_result: [ ]  ◀ BOOLEAN           │
│  clamp_min:    [ 0.00 ]                 │
│  clamp_max:    [ 1.00 ]                 │
│                                         │
│  result:   ──▶ (FLOAT)                  │
│  result_int: ──▶ (INT)                  │
└─────────────────────────────────────────┘
```

## Lizenz

[MIT License](LICENSE)
