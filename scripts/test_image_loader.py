from image_loader import loader, resize
import PIL, io
import pytest

test_url = "https://m.media-amazon.com/images/M/MV5BZTQwNmY4MmEtYjNhZi00MzJjLTgxNGItNmQyNmI0YzQ4NWNhXkEyXkFqcGdeQXVyMTIwNjUyOTA3._V1_.jpg"
false_url = "https://m.media-amazon.com/images/M/33MV5BZTQwNmY4MmEtYjNhZi00MzJjLTgxNGItNmQyNmI0YzQ4NWNhXkEyXkFqcGdeQXVyMTIwNjUyOTA3._V1_.jpg"

def test_loader():
    
    # Confirm valid image URL processed correctly
    png_data = loader(test_url)
    assert type(png_data) is bytes
    img = PIL.Image.open(io.BytesIO(png_data))
    assert type(img) is PIL.PngImagePlugin.PngImageFile
    del img
    
    # Invalid image URL returns nothing
    false_viewer = loader(false_url)
    assert false_viewer is None

def test_resize():

    # Load original image and set scale factor = 2
    original = loader(test_url)
    org_img = PIL.Image.open(io.BytesIO(original))
    new_width, new_height = 2 * org_img.size[0], 2 * org_img.size[1]

    # Resize image and confirm return type is bytes
    scaled = resize(original, (new_width, new_height))
    assert type(scaled) is bytes

    # Confirm dimensions have scaled up by factor 2
    new_img = PIL.Image.open(io.BytesIO(scaled))
    assert new_img.size[0] == 2 * org_img.size[0]
    assert new_img.size[1] == 2 * org_img.size[1]
    del org_img, new_img

    # Confirm invalid URL returns nothing
    false_resize = resize(loader(false_url), (100, 100))
    false_resize is None