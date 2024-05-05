from braille import get_braille_char

def brightness(pixel):
    r,g,b,a = pixel
    
    lum = sum((r,g,b))/3

    return lum * (a/255)

def get_chunk_dots(chunk, inverted, threshold):
    index_to_dot_number = {
        0: 1,
        1: 4,
        2: 2,
        3: 5,
        4: 3,
        5: 6
    }

    dots = []

    for i, pixel in enumerate(chunk):
        b = brightness(pixel)

        if not inverted:
            if b >= threshold:
                dots.append(index_to_dot_number[i])
        elif inverted:
            if b <= threshold:
                dots.append(index_to_dot_number[i])
    
    return dots


def chunks_to_braille(chunk_rows, inverted=False, threshold=255//2):
    output = ""

    for chunk_row in chunk_rows:
        for chunk in chunk_row:
            output += get_braille_char(get_chunk_dots(chunk, inverted, threshold))

        output += "\n"
    
    return output

def resize_image(image, output_height):
        image_height = output_height*3
        image_width = (image.width*output_height*3)//image.height
        if not image_width % 2 == 0:
            image_width += 1

        return image.resize((image_width, image_height))