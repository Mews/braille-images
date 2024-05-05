def int_to_hex(integer):
    return format(integer, '02x')

def add_hex(*hexes):
    total = 0
    for hex_num in hexes:
        total += int(hex_num,16)
    
    return int_to_hex(total)