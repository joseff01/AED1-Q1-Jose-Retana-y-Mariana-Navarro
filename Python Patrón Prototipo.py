import copy

class Oveja:
    def __init__ (self, nombre, ID, color, enfermedades, listaMediciones):
        self.nombre = nombre
        self.ID = ID
        self.color = color
        self.enfermedades = enfermedades
        self.listaMediciones = listaMediciones

    def __copy__(self):
        copyNombre = copy.copy(self.nombre)
        copyID = copy.copy(self.ID)
        copyColor = copy.copy(self.color)
        copyEnfermedades = copy.copy(self.enfermedades)
        copyListaMediciones = copy.copy(self.listaMediciones)

        copyOveja = self.__class__(self.nombre,self.ID,self.color,self.enfermedades, self.listaMediciones)
        copyOveja.__dict__.update(self.__dict__)

        return copyOveja

    def __deepcopy__(self,memo={}):
        copyNombre = copy.deepcopy(self.nombre,memo)
        copyID = copy.deepcopy(self.ID,memo)
        copyColor = copy.deepcopy(self.color,memo)
        copyEnfermedades = copy.deepcopy(self.enfermedades,memo)
        copyListaMediciones = copy.deepcopy(self.listaMediciones,memo)

        deepCopyOveja = self.__class__(self.nombre,self.ID,self.color,self.enfermedades,self.listaMediciones)

        deepCopyOveja.__dict__ = copy.deepcopy(self.__dict__, memo)

        return deepCopyOveja
        
class Enfermedades():

    def __init__ (self,ojos,corazon,huesos):
        self.ojos = ojos
        self.corazon = corazon
        self.huesos = huesos
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
    


if __name__ == "__main__":
    
    enfermedadesDolly = Enfermedades("buena vista","débil","sanos")
    oveja1 = Oveja("Dolly","01","blanco",enfermedadesDolly, [15,20,50])
    enfermedadesDolly.set_parent(oveja1)

    #Copia regular de un objeto:
    
    shallowCopyOveja = copy.copy(oveja1)

        # Verificación de cambio de atributos:
    shallowCopyOveja.nombre = "Shelly"

    if shallowCopyOveja.nombre == oveja1.nombre:
        print( "shallowCopyOveja y oveja1 tienen el mismo nombre: " + shallowCopyOveja.nombre)

    else:
        print( "shallowCopyOveja y oveja1 tienen diferentes nombres: " + shallowCopyOveja.nombre + " y " + oveja1.nombre)


        #Verificación de cambio de objetos hijos:
    shallowCopyOveja.enfermedades.ojos = "mala vista"
    if shallowCopyOveja.enfermedades.ojos == oveja1.enfermedades.ojos:
        print( "shallowCopyOveja y oveja1 tienen la misma vista")

    else:
        print( "shallowCopyOveja y oveja1 tienen vistas distintas")

        #Verificación de cambio de listas:
    shallowCopyOveja.listaMediciones.append(55)
    if shallowCopyOveja.listaMediciones[-1] == oveja1.listaMediciones[-1]:
        print( "shallowCopyOveja y oveja1 tienen la misma lista de mediciones")

    else:
        print( "shallowCopyOveja y oveja1 tienen distintas listas de mediciones")

    #Copia "Profunda" de un objeto:

    enfermedadesPoppy = Enfermedades("buena vista","débil","sanos")
    oveja2 = Oveja("Poppy","02","negro",enfermedadesPoppy, [20,25,55])
    enfermedadesPoppy.set_parent(oveja2)

    deepCopyOveja = copy.deepcopy(oveja2)
        

        # Verificación de cambio de atributos:
    deepCopyOveja.nombre = "Frosty"

    if deepCopyOveja.nombre == oveja2.nombre:
        print( "deepCopyOveja y oveja2 tienen el mismo nombre: " + deepCopyOveja.nombre)

    else:
        print( "deepCopyOveja y oveja2 tienen diferentes nombres: " + deepCopyOveja.nombre + " y " + oveja2.nombre)


        #Verificación de cambio de objetos hijos:
    deepCopyOveja.enfermedades.ojos = "mala vista"
    if deepCopyOveja.enfermedades.ojos == oveja2.enfermedades.ojos:
        print( "deepCopyOveja y oveja2 tienen la misma vista")

    else:
        print( "deepCopyOveja y oveja2 tienen vistas distintas")

        #Verificación de cambio de listas:
    deepCopyOveja.listaMediciones.append(60)
    if deepCopyOveja.listaMediciones[-1] == oveja2.listaMediciones[-1]:
        print( "deepCopyOveja y oveja2 tienen la misma lista de mediciones")

    else:
        print( "deepCopyOveja y oveja2 tienen distintas listas de mediciones")
    

    
    
