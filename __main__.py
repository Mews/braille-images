import argparse
from PIL import Image
from converter import resize_image, chunks_to_braille
from image_chunker import get_image_chunk_rows
from pyperclip import copy

parser = argparse.ArgumentParser(
                    prog="Braille-Images",
                    description="Converts images to text using braille characters")

parser.add_argument("imagedir", 
                    metavar="The path to the image", 
                    type=str)
parser.add_argument("-t", "--threshold", 
                    default=255//2, 
                    metavar="The threshold to use when deciding whether a pixel should be rendered in text", 
                    type=int)
parser.add_argument("-s", "--size", 
                    default=20, 
                    metavar="This reffers to how many lines the output should take", 
                    type=int)
parser.add_argument("-i", "--invert", 
                    default=False, 
                    action=argparse.BooleanOptionalAction, 
                    metavar="Whether or not to invert the output", 
                    type=bool)

args = parser.parse_args()

imagedir = args.imagedir
threshold = args.threshold
size = args.size
inverted = args.invert

image = Image.open(imagedir)
image = resize_image(image, size)

image_chunks = get_image_chunk_rows(image)
braille_image = chunks_to_braille(image_chunks, inverted=inverted, threshold=threshold)

print(braille_image)
print("Output was",len(braille_image.replace("\n", "")),"characters")
print("Copied output to clipboard")
copy(braille_image)