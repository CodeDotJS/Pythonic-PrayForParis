from PIL import Image
from PIL import ImageEnhance

img_location = raw_input(" Image's Name : ")

tracked_image = Image.open(img_location)

main_height = tracked_image.size[1]

main_width = tracked_image.size[0]

tracked_image = tracked_image.convert("RGB")

france_flage = Image.new("RGB", [main_height, main_width], (255, 255, 255, 255))

flag_division = []
for sections in range(0, main_height, int(main_height/3)):
    flag_division.append(sections)

flag_division.append(flag_division[2]+int(main_height/3))

flag_colors = [(0, 0, 128), (245, 245, 245), (255, 0, 0)]

add_colors = france_flage.load()

for g in range(0, 3):
    for i in range(main_width):
        for t in range(flag_division[g], flag_division[g+1]):
            add_colors[t, i] = flag_colors[g]

france_flage = france_flage.rotate(270)

enhancer = ImageEnhance.Color(tracked_image)

tracked_image = enhancer.enhance(1.4)

new_image = Image.blend(tracked_image, france_flage, 0.4)

new_image.show()

new_image.save('index.jpg')

print "Done! Open your index.jpg file to check the changes."
