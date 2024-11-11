
import fotoapp

def menu():
    print("Bienvenido a la App de edición de fotos")
    print("1. Redimensionar imagen")
    print("2. Ajustar contraste")
    print("3. Aplicar filtro")
    print("4. Crear boceto")
    print("5. Salir")
    
    image = None
    while True:
        try:
            option = int(input("Seleccione una opción: "))
            
            if option == 1:
                image_path = input("Ingrese la ruta o URL de la imagen:(Asegurese de que la imagen este en .jpg) ")
                platform = input("Ingrese la plataforma (Youtube, Instagram, Twitter, Facebook): ")
                image = fotoapp.resize_image(image_path, platform)
                print(f"Imagen redimensionada para {platform}.")

            elif option == 2:
                if image is None:
                    raise Exception("Primero debe cargar una imagen con la opción 1.")
                enhanced_image = fotoapp.adjust_contrast(image)
                enhanced_image.show()

            elif option == 3:
                if image is None:
                    raise Exception("Primero debe cargar una imagen con la opción 1.")
                filter_name = input("Ingrese el filtro a aplicar: ")
                filtered_image = fotoapp.apply_filter(image, filter_name)
                filtered_image.show()

            elif option == 4:
                if image is None:
                    raise Exception("Primero debe cargar una imagen con la opción 1.")
                persona = True  
                sketch = fotoapp.create_sketch(image, persona)
                sketch.show()

            elif option == 5:
                print("Gracias por usar la App de edición de fotos.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")
        
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    menu()
    
