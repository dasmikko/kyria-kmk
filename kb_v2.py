import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        pins[6],
        pins[7],
        pins[8],
        pins[9],
        pins[10],
        pins[11],
        pins[12],
        pins[13],
    )
    row_pins = (pins[17], pins[16], pins[15], pins[14])
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = pins[1]
    rgb_pixel_pin = pins[0]

    coord_mapping = []
    coord_mapping.extend(ic(0, x, 8) for x in range(6))
    coord_mapping.extend(ic(4, x, 8) for x in range(5, -1, -1))
    coord_mapping.extend(ic(1, x, 8) for x in range(6))
    coord_mapping.extend(ic(5, x, 8) for x in range(5, -1, -1))
    coord_mapping.extend(ic(2, x, 8) for x in range(8))
    coord_mapping.extend(ic(6, x, 8) for x in range(7, -1, -1))
    coord_mapping.extend(ic(3, x, 8) for x in range(3, 8))
    coord_mapping.extend(ic(7, x, 8) for x in range(7, 2, -1))
    
    print(coord_mapping)