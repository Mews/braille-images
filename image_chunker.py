from PIL import Image

def get_image_rows(image:Image):
    image = image.convert("RGBA")

    width = image.width
    height = image.height

    rows = []

    for y in range(height):
        row = []
        for x in range(width):
            row.append(image.getpixel((x,y)))
        
        rows.append(row)
    
    return rows

def get_image_chunk_rows(image:Image):
    width = image.width
    height = image.height

    rows = get_image_rows(image)
    chunk_rows = []

    for y in range(0, height, 3):
        row1 = rows[y]
        row2 = rows[y+1]
        row3 = rows[y+2]
        chunk_row = []

        for x in range(0, len(row1), 2):
            chunk = []
            chunk.append(row1[x])
            chunk.append(row1[x+1])
            chunk.append(row2[x])
            chunk.append(row2[x+1])
            chunk.append(row3[x])
            chunk.append(row3[x+1])

            chunk_row.append(chunk)
        
        chunk_rows.append(chunk_row)
        
    return chunk_rows

"""
#Code for testing chunk creation
test_image = Image.open("test.png").resize((300,300))

chunk_rows = get_image_chunk_rows(test_image)

new_image = Image.new("RGBA", (300, 300), (0,0,0,255))

for y, chunk_row in enumerate(chunk_rows):
    for x, chunk in enumerate(chunk_row):
        for xx, pixel in enumerate(chunk):
            new_image.putpixel( (2*x+xx//3, 3*y+xx%3) , pixel)

new_image.show()
"""