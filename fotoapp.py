from PIL import Image, ImageEnhance, ImageFilter,ImageOps
import requests
from io import BytesIO
from PIL import ImageOps
from matplotlib import pyplot as plt


DIMENSIONS = {
    "Youtube": (1280, 720),
    "Instagram": (1080, 1080),
    "Twitter": (1200, 675),
    "Facebook": (1200, 630)
}


def resize_image(image_path, platform):
    
    if platform not in DIMENSIONS:
        raise ValueError("Plataforma no soportada. Elija entre 'Youtube', 'Instagram', 'Twitter' o 'Facebook'. ")

    
    target_width, target_height = DIMENSIONS[platform]

    
    try:
        if image_path.startswith('http'):
            response = requests.get(image_path)
            img = Image.open(BytesIO(response.content))
        
        with Image.open(image_path) as img:
            target_size = DIMENSIONS[platform]
            resized_img = img.resize(target_size, Image.LANCZOS)
            resized_image_path = f"redimensionada_para{platform}.jpg"
            resized_img.save(resized_image_path)
        return resized_img

    except Exception as e:
        raise IOError(f"Error al abrir la imagen: {e}")

    
    img.thumbnail((target_width, target_height), Image.LANCZOS)
    return img



def adjust_contrast(image, output_path="imagen_con_contraste.jpg"):
    #
    equalized_img = ImageOps.equalize(image)
    
    
    equalized_img.save(output_path)
    
    return equalized_img


FILTERS = {
    "BLUR": ImageFilter.BLUR,
    "CONTOUR": ImageFilter.CONTOUR,
    "DETAIL": ImageFilter.DETAIL,
    "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
    "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
    "EMBOSS": ImageFilter.EMBOSS,
    "FIND_EDGES": ImageFilter.FIND_EDGES,
    "SHARPEN": ImageFilter.SHARPEN,
    "SMOOTH": ImageFilter.SMOOTH
}

def apply_filter(image, filter_name, output_path="imagen_filtrada.jpg"):
    
    if filter_name not in FILTERS:
        raise ValueError(f"Filtro '{filter_name}' no soportado.")
    
    
    filtered_img = image.filter(FILTERS[filter_name])
    
    
    filtered_img.save(output_path)
    
    
    plt.imshow(filtered_img)
    plt.title(f"Filtro aplicado: {filter_name}")
    plt.axis("off")
    plt.show()
    
    return filtered_img



def create_sketch(image, persona,output_path="sketch_de_imagen.jpg"):
    if persona:
        
        sketch = image.convert("L").filter(ImageFilter.FIND_EDGES)
        
        
        sketch.save(output_path)
        
        return sketch
    else:
        raise ValueError("La imagen no contiene una persona.")





