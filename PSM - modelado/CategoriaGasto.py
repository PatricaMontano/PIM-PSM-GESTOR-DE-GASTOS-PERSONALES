#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 36 "model.ump"
# line 64 "model.ump"

class CategoriaGasto():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #CategoriaGasto Attributes
    #CategoriaGasto Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNombre, aDescripcion):
        self._gastos = None
        self._descripcion = None
        self._nombre = None
        self._nombre = aNombre
        self._descripcion = aDescripcion
        self._gastos = []

    #------------------------
    # INTERFACE
    #------------------------
    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setDescripcion(self, aDescripcion):
        wasSet = False
        self._descripcion = aDescripcion
        wasSet = True
        return wasSet

    def getNombre(self):
        return self._nombre

    def getDescripcion(self):
        return self._descripcion

    # Code from template association_GetMany 
    def getGasto(self, index):
        aGasto = self._gastos[index]
        return aGasto

    def getGastos(self):
        newGastos = tuple(self._gastos)
        return newGastos

    def numberOfGastos(self):
        number = len(self._gastos)
        return number

    def hasGastos(self):
        has = len(self._gastos) > 0
        return has

    def indexOfGasto(self, aGasto):
        index = (-1 if not aGasto in self._gastos else self._gastos.index(aGasto))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfGastos():
        return 0

    # Code from template association_AddManyToOne 
    def addGasto1(self, aFecha, aMonto, aDescripcion, aUsuario):
        from Gasto import Gasto
        return Gasto(aFecha, aMonto, aDescripcion, aUsuario, self)

    def addGasto2(self, aGasto):
        wasAdded = False
        if (aGasto) in self._gastos :
            return False
        existingCategoriaGasto = aGasto.getCategoriaGasto()
        isNewCategoriaGasto = not (existingCategoriaGasto is None) and not self == existingCategoriaGasto
        if isNewCategoriaGasto :
            aGasto.setCategoriaGasto(self)
        else :
            self._gastos.append(aGasto)
        wasAdded = True
        return wasAdded

    def removeGasto(self, aGasto):
        wasRemoved = False
        #Unable to remove aGasto, as it must always have a categoriaGasto
        if not self == aGasto.getCategoriaGasto() :
            self._gastos.remove(aGasto)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addGastoAt(self, aGasto, index):
        wasAdded = False
        if self.addGasto(aGasto) :
            if index < 0 :
                index = 0
            if index > self.numberOfGastos() :
                index = self.numberOfGastos() - 1
            self._gastos.remove(aGasto)
            self._gastos.insert(index, aGasto)
            wasAdded = True
        return wasAdded

    def addOrMoveGastoAt(self, aGasto, index):
        wasAdded = False
        if (aGasto) in self._gastos :
            if index < 0 :
                index = 0
            if index > self.numberOfGastos() :
                index = self.numberOfGastos() - 1
            self._gastos.remove(aGasto)
            self._gastos.insert(index, aGasto)
            wasAdded = True
        else :
            wasAdded = self.addGastoAt(aGasto, index)
        return wasAdded

    def delete(self):
        i = len(self._gastos)
        while i > 0 :
            aGasto = self._gastos[i - 1]
            aGasto.delete()
            i -= 1

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "descripcion" + ":" + str(self.getDescripcion()) + "]"

    def addGasto(self, *argv):
        from Gasto import Gasto
        if len(argv) == 4 and isinstance(argv[0], Date) and isinstance(argv[1], (float, int)) and isinstance(argv[2], str) and isinstance(argv[3], Usuario) :
            return self.addGasto1(argv[0], argv[1], argv[2], argv[3])
        if len(argv) == 1 and isinstance(argv[0], Gasto) :
            return self.addGasto2(argv[0])
        raise TypeError("No method matches provided parameters")

