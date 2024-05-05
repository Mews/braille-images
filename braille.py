from hex_math import add_hex

dot_to_hex = {
    1: "1",
    2: "2",
    3: "4",
    4: "8",
    5: "10",
    6: "20",
    7: "40",
    8: "80"
}

def get_braille_char(dots):
    braille_hex_code = "2800"
    for dot in dots:
        braille_hex_code = add_hex(braille_hex_code, dot_to_hex[dot])

    return chr(int(braille_hex_code, 16))