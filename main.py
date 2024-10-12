import os

def search_word_in_files(input_directory, search_word):
    # Crear una lista para almacenar los archivos que contienen la palabra
    files_with_word = []
    
    # Iterar sobre todos los archivos en el directorio
    for filename in os.listdir(input_directory):
        # Verificar si el archivo tiene extensión .txt
        if filename.endswith('.txt'):
            file_path = os.path.join(input_directory, filename)
            
            # Abrir el archivo y buscar la palabra
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Buscar si la palabra está en el contenido del archivo
                if search_word in content:
                    print(f"Palabra '{search_word}' encontrada en: {filename}")
                    files_with_word.append(filename)
    
    # Retornar la lista de archivos donde se encontró la palabra
    return files_with_word

# Ejecutar la función
input_directory = './txt_files_directory'  # Reemplaza con la ruta de tu directorio con los archivos .txt
search_word = 'palabra_a_buscar'  # Reemplaza con la palabra que deseas buscar

# Llamada a la función y obtener los archivos donde se encontró la palabra
files_found = search_word_in_files(input_directory, search_word)

# Mostrar los resultados
if files_found:
    print("\nArchivos donde se encontró la palabra:")
    for file in files_found:
        print(file)
else:
    print(f"\nNo se encontró la palabra '{search_word}' en ningún archivo.")
