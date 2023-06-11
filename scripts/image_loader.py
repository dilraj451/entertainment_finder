import io, cloudscraper

import PySimpleGUI as sg

import PIL
from PIL import Image


url = "https://m.media-amazon.com/images/M/MV5BZTQwNmY4MmEtYjNhZi00MzJjLTgxNGItNmQyNmI0YzQ4NWNhXkEyXkFqcGdeQXVyMTIwNjUyOTA3._V1_.jpg"

def loader(img_url: str):
    """Converts jpg image data to PNG format

    Args:
        img_url (str): URL for the .jpg image

    Returns:
        png_data (bytes): image pixel data in png format
    """
    # Only process if URL input (i.e. image is present)
    if img_url:
        # Extract jpg data
        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "linux", "mobile": False}
            )
            .get(img_url)
            .content
        )
        try:
            pil_image = Image.open(io.BytesIO(jpg_data))
        
        # Catch invalid image addresses
        except PIL.UnidentifiedImageError:
            print("Image address not valid")
        
        # Convert jpg data to png data and store as nested PySimpleGUI object
        else:
            png_bio = io.BytesIO()
            pil_image.save(png_bio, format="PNG")
            png_data = png_bio.getvalue()
            del pil_image
            return png_data
        
def resize(byte_data: bytes, resize_params: tuple):
    
    if byte_data:
        img = Image.open(io.BytesIO(byte_data))
        cur_width, cur_height = img.size
        new_width, new_height = resize_params

        scale_factor = min(new_width/cur_width, new_height/cur_height)
        img = img.resize((int(cur_width*scale_factor), int(cur_height*scale_factor)), Image.LANCZOS)
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
        

if __name__ == '__main__':

        Viewer = [[sg.Image(data=resize(loader(url), (500, 500)), key='-IMG-')]]

        layout = [[sg.Column(Viewer)]]

        window = sg.Window("Image_Test", layout)

        while True:
            event, values = window.read()
            if event == "EXIT" or event == sg.WIN_CLOSED:
                break
        window.close()
        image_loaded = True
