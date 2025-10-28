from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import Oled, OledDisplayMode
from kmk.modules.rgb import RGB
import board
import time

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP26, board.GP27)
keyboard.col_pins = (board.GP28, board.GP29, board.GP4)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW


layers = Layers()
encoder = EncoderHandler()
oled = Oled()
rgb = RGB(pixel_pin=board.GP3, num_pixels=12, hue_default=0)

keyboard.modules = [layers, encoder, oled, rgb]


oled.display_mode = OledDisplayMode.MANUAL 

LAYER_TEXTS = [
    "Layer 0: Base\nShortcuts & Typing",
    "Layer 1: Functions\nArrows & F-Keys",
    "Layer 2: Media\nPlayback & Volume",
]

def draw_oled(oled_obj, layer):
    oled_obj.clear()
    oled_obj.text(LAYER_TEXTS[layer], 0, 0)
    oled_obj.show()


encoder.pins = ((board.GP0, board.GP2, board.GP1),)

encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),
]

last_encoder_button = False

def check_encoder_press():
    global last_encoder_button
    pressed = not keyboard.io.digital_read(board.GP1)
    if pressed and not last_encoder_button:
        new_layer = (keyboard.active_layers[0] + 1) % 3
        keyboard.activate_layer(new_layer)
        draw_oled(oled, new_layer)
    last_encoder_button = pressed


rgb.hue_step = 10
rgb.sat_step = 10
rgb.val_step = 10
rgb.animation_mode = None  

def rgb_layer_effect(layer):
    if layer == 0:
        rgb.set_hsv_fill(0, 255, 100)     # Red
    elif layer == 1:
        rgb.set_hsv_fill(85, 255, 100)    # Green
    elif layer == 2:
        rgb.set_hsv_fill(170, 255, 100)   # Blue

keyboard.after_layer_change = rgb_layer_effect


keyboard.keymap = [
    [  # Layer 0 - Base
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
    ],
    [  # Layer 1 - Fn1
        KC.F1, KC.F2, KC.F3,
        KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [  # Layer 2 - Media
        KC.MPRV, KC.MPLY, KC.MNXT,
        KC.VOLD, KC.VOLU, KC.MUTE,
    ],
]


def on_startup():
    rgb_layer_effect(0)
    draw_oled(oled, 0)

on_startup()


if __name__ == '__main__':
    while True:
        keyboard.tick()  
        check_encoder_press()
        time.sleep(0.01)
