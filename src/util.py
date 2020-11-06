from PIL import Image


class Util:

    def captura_elemento(self,ima_original,elemento,ruta_destino):
            location = elemento.location
            size = elemento.size

            x = location['x']
            y = location['y']
            width = x + size['width']
            height = y + size['height']
            
            ima = Image.open(ima_original)
            ima = ima.crop((int(x),int(y),int(width),int(height)))
            ima.save(ruta_destino)

