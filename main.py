from PIL import Image

image_files = ['images.jpeg', 'indir1.jpeg']
image_objects = [Image.open(file) for file in image_files]

image_objects[0].save('output.gif', save_all=True, append_images=image_objects[1:], duration=500, loop=0)
