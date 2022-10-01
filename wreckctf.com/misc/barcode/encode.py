from PIL import (
    Image,
    ImageDraw,
)

OUTPUT_PATH = 'output.png'
FLAG_PATH = 'flag.txt'

STRIPE_WIDTH = 16
STRIPE_HEIGHT = 128

with open(FLAG_PATH, 'r') as f:
    flag = f.read().strip()

flag = list(map(int, ''.join(f'{ord(c):08b}' for c in flag)))
image = Image.new(
    'RGB',
    ((len(flag) * STRIPE_WIDTH), STRIPE_HEIGHT),
    color='white'
)

draw = ImageDraw.Draw(image)
ones = [i for i, x in enumerate(flag) if x == 1]
for i in ones:
    draw.rectangle(
        (i * STRIPE_WIDTH, 0, (i + 1) * STRIPE_WIDTH - 1, STRIPE_HEIGHT - 1),
        fill='black'
    )

image.save(OUTPUT_PATH)
