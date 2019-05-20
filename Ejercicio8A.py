#Jorge_Hinostrosa_Paula
#paulajhinostrosa@ciencias.unam.mx    

class Inventario:

#A)  
  def __init__(self,listaProductos,cantidadProductos,precioProductos):
    self.listaProductos=listaProductos
    self.cantidadProductos=cantidadProductos
    self.precioProductos=precioProductos

#B)  
  def agregarProducto(self,producto,unidades,precio):
    self.listaProductos.append(producto)
    self.cantidadProductos.append(unidades)
    self.precioProductos.append(precio) 
    return Inventario(self.listaProductos,self.cantidadProductos,self.precioProductos)
  
#C.1) 
  def adquerirProducto(self,producto):
    if producto in self.listaProductos:
      for i in range(len(self.listaProductos)):
        self.cantidadProductos[i] = self.cantidadProductos[i]+1
        return Inventario(self.listaProductos,self.cantidadProductos,self.precioProductos)
    else: 
      print("El producto no fue encontrado dentro del inventario")
  
#C.2)  
  def venderProducto(self,producto):
    for i in range(len(self.listaProductos)):
      if producto == self.listaProductos[i]:
        self.cantidadProductos[i] = self.cantidadProductos[i]-1
      else: 
        print("El producto no fue encontrado dentro del inventario")

#D)  
  def guardarLista(self,archivo):
    archivo = open(archivo+".txt","w")
    for linea in archivo:
      datos = linea.split()
      cadena = datos[0] + "\n"
      archivo.write(cadena)
    with open("E10.txt","r") as archivo10:
      for linea in archivo10:
        print(linea.rstrip())
    archivo.close()

listaP=["blusa","pantalon","playera","zapatos","tenis"]
listaC=[3,5,6,8,2]
listP=[252.50,465.00,389.90,799.99,1099.99]

I1=Inventario(listaP,listaC,listP)
print(I1.listaProductos)
print(I1.cantidadProductos)
print(I1.precioProductos)
I2=I1.agregarProducto("short",7,149.90)
print(I2.listaProductos)
print(I2.cantidadProductos)
print(I2.precioProductos)
I3=I1.adquerirProducto('blusa')
print(I3.cantidadProductos)
I4=I1.adquerirProducto('collar')
I1.guardarLista("Producto")
