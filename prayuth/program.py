from PIL import Image, ImageEnhance
import numpy as np

# img1 = Image.open('./problems/img1.png')
# img1_copy = Image.open('./prayuth.png').crop((350, 200, 700, 800))
# img1_copy.show()
# print(np.mean((np.array(img1) - np.array(img1_copy)) ** 2))

# img2 = Image.open('./problems/img2.png')
# img2_copy = Image.open('./prayuth.png').transpose(1).rotate(20, expand=True, fillcolor=(134, 120, 227, 255)).resize((1450, 1116))
# img2_copy.show()
# print(np.mean((np.array(img2) - np.array(img2_copy)) ** 2))

# img3 = Image.open('./problems/img3.png')
# img3_copy = Image.open('./prayuth.png')
# enhancer = ImageEnhance.Brightness(img3_copy)
# img3_copy = enhancer.enhance(1.5)
# enhancer = ImageEnhance.Contrast(img3_copy)
# img3_copy = enhancer.enhance(2).rotate(39, expand=True, fillcolor=(34, 20, 27, 255)).rotate(12, expand=True, fillcolor=(255, 255, 255, 255)).resize((1702, 1638))
# img3_copy.show()
# print(np.mean((np.array(img3) - np.array(img3_copy)) ** 2))

img4 = Image.open('./problems/img4.png')
img4_copy = Image.open('./prayuth.png')
enhancer = ImageEnhance.Contrast(img4_copy)
img4_copy = enhancer.enhance(2)
enhancer = ImageEnhance.Brightness(img4_copy)
img4_copy = enhancer.enhance(0.5)
enhancer = ImageEnhance.Contrast(img4_copy)
img4_copy = enhancer.enhance(1.5)
x = 325
y = 217
img4_copy = img4_copy.transpose(0).rotate(203, expand=True, fillcolor=(222, 109, 13, 255)).crop((0+x, 0+y, 350+x, 350+y)).rotate(39, expand=True, fillcolor=(0, 128, 0, 255)).resize((450, 450))
img4_copy.show()
img4.show()
Image.fromarray((np.array(img4) - np.array(img4_copy)) ** 2).show()
print(np.mean((np.array(img4) - np.array(img4_copy)) ** 2))
