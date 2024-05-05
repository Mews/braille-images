from tkinter.filedialog import askopenfilename
from PIL import Image
from image_chunker import get_image_chunk_rows
from converter import chunks_to_braille

def resize_image(image, output_height):
    image_height = output_height*3
    image_width = (image.width*output_height*3)//image.height
    if not image_width % 2 == 0:
        image_width += 1

    return image.resize((image_width, image_height))

image = Image.open(askopenfilename())
image = resize_image(image, 50)

image_chunk_rows = get_image_chunk_rows(image)
braille_image = chunks_to_braille(image_chunk_rows)
print(braille_image)