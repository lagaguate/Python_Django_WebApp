

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro")
        
        if not self.carro:
            self.carro = self.session["carro"]={}
        #else:
        #    self.carro = carro    
        
    def agregar(self, producto):

        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":float(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else: 
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]= float(value["precio"])+float(producto.precio)
                    break
        
        self.guardar_carro()


    def guardar_carro(self):
        self.session["carro"]= self.carro
        self.session.modified =True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]    
            self.guardar_carro()

    def restart_producto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]= float(value["precio"]-float(producto.precio))
                    if value["cantidad"] < 1:
                       self.eliminar(producto) 
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}        
        self.session.modified =True


        
