from PIL import Image, ImageEnhance, ImageFilter

def resize_maintain_aspect_ratio(im: Image, x: int):
    ratio = im.size
    result = []

    for i in ratio:
        result.append(int(round(i / (max(ratio) / x), 0)))

    return im.resize(tuple(result))


def convert_lurl2xywh(coordinates: tuple[int, int, int, int]):
    return tuple(int(i) for i in [(coordinates[0] + coordinates[2]) / 2, 
            (coordinates[1] + coordinates[3]) / 2, 
            coordinates[2] - coordinates[0], 
            coordinates[3] - coordinates[1]])

im = Image.open('./cat.png').convert('RGB')
resize_maintain_aspect_ratio(im, 30).show()
enhancer = ImageEnhance.Contrast(im)
im_adjust = enhancer.enhance(2.0)
im_adjust.show()
im.filter(ImageFilter.GaussianBlur(10)).show()
gs_im = im.convert('L')
