class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito= self.session["carrito"]
        else:
            self.carrito = carrito
            
            
    def agregar(self,articulo):
        id = str(articulo.idObra)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id":articulo.idObra,
                "nombre":articulo.nombre,
                "acumulado":articulo.precio,
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"]+=1
            self.carrito[id]["acumulado"]+=articulo.precio
        self.actualizar()
    
        
    def actualizar(self):
        self.session["carrito"]=self.carrito
        self.session.modified = True
        
        
    def resta(self,articulo):
        id= str(articulo.idObra)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["acumulado"]-=articulo.precio
            if self.carrito[id]["cantidad"]<=0:
                self.eliminar(articulo)
            self.actualizar()
            
    
    def eliminar(self,articulo):
        id = str(articulo.idObra)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.actualizar()
            
            
    def vaciar(self):
        self.session["carrito"]={}
        self.session.modified = True        
    
    def obtener_historial(self):
        historial = self.session.get("historial_compras", [])
        return historial

    def guardar_compra(self, usuario, total):
        compra = {
            "usuario": usuario,
            "productos": list(self.carrito.values()),
            "total": total
        }
        historial = self.obtener_historial()
        historial.append(compra)
        self.session["historial_compras"] = historial
        self.session.modified = True