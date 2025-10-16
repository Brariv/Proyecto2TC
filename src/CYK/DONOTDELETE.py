
def read_txt_file(file_path):
    Gramar_Array = []
    with open(file_path, 'r') as file:
        content = file.read()
        Gramar_Array = content.splitlines()

    for i in range(len(Gramar_Array)):
        Gramar_Array[i] = Gramar_Array[i].split(" ")

    return Gramar_Array

print(read_txt_file('/Users/brandon/Documents/UVG/Github/Proyecto2TC/gramatica.txt'))