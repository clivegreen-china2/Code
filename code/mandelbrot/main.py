from Pillow import Image
from geometry.point import Point
from geometry.rectangle import Rectangle as Rect

center_x = -0.54
center_y = -0.54
viewport_size = 0.02
image_size = 1024
times = 2001

viewport_center = Point(center_x, center_y)
viewport_area = Rect(viewport_center, viewport_size, viewport_size)

image_width, image_height = image_size, image_size  # square image
image = Image.new("RGB", (image_width, image_height))

left = viewport_area.left
top = viewport_area.top
right = viewport_area.right
bottom = viewport_area.bottom

for y in range(image_height):

    zy = y * (bottom - top) / (image_height - 1) + top
    for x in range(image_width):
        zx = x * (right - left) / (image_width - 1) + left
        z = zx + zy * 1j
        c, i = z, 0
        for i in range(times):
            if abs(z) > 2.0:
                break
            z = z * z + c
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
image.show_stats()
