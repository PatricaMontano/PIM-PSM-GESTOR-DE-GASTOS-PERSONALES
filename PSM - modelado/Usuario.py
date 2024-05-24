#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 2 "model.ump"
# line 45 "model.ump"

class Usuario():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Usuario Attributes
    #Usuario Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNombre, aCorreoElectronico, aContrasena, aSaldo):
        self._ingresos = None
        self._gastos = None
        self._saldo = None
        self._contrasena = None
        self._correoElectronico = None
        self._nombre = None
        self._nombre = aNombre
        self._correoElectronico = aCorreoElectronico
        self._contrasena = aContrasena
        self._saldo = aSaldo
        self._gastos = []
        self._ingresos = []

    #------------------------
    # INTERFACE
    #------------------------
    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setCorreoElectronico(self, aCorreoElectronico):
        wasSet = False
        self._correoElectronico = aCorreoElectronico
        wasSet = True
        return wasSet

    def setContrasena(self, aContrasena):
        wasSet = False
        self._contrasena = aContrasena
        wasSet = True
        return wasSet

    def setSaldo(self, aSaldo):
        wasSet = False
        self._saldo = aSaldo
        wasSet = True
        return wasSet

    def getNombre(self):
        return self._nombre

    def getCorreoElectronico(self):
        return self._correoElectronico

    def getContrasena(self):
        return self._contrasena

    def getSaldo(self):
        return self._saldo

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

    # Code from template association_GetMany 
    def getIngreso(self, index):
        aIngreso = self._ingresos[index]
        return aIngreso

    def getIngresos(self):
        newIngresos = tuple(self._ingresos)
        return newIngresos

    def numberOfIngresos(self):
        number = len(self._ingresos)
        return number

    def hasIngresos(self):
        has = len(self._ingresos) > 0
        return has

    def indexOfIngreso(self, aIngreso):
        index = (-1 if not aIngreso in self._ingresos else self._ingresos.index(aIngreso))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfGastos():
        return 0

    # Code from template association_AddManyToOne 
    def addGasto1(self, aId, aFecha, aMonto, aCategoria, aDescripcion, aCategoriaGasto):
        from Gasto import Gasto
        return Gasto(aId, aFecha, aMonto, aCategoria, aDescripcion, aCategoriaGasto, self)

    def addGasto2(self, aGasto):
        wasAdded = False
        if (aGasto) in self._gastos :
            return False
        existingUsuario = aGasto.getUsuario()
        isNewUsuario = not (existingUsuario is None) and not self == existingUsuario
        if isNewUsuario :
            aGasto.setUsuario(self)
        else :
            self._gastos.append(aGasto)
        wasAdded = True
        return wasAdded

    def removeGasto(self, aGasto):
        wasRemoved = False
        #Unable to remove aGasto, as it must always have a usuario
        if not self == aGasto.getUsuario() :
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

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfIngresos():
        return 0

    # Code from template association_AddManyToOne 
    def addIngreso1(self, aId, aFecha, aMonto, aFuente, aDescripcion):
        from Ingreso import Ingreso
        return Ingreso(aId, aFecha, aMonto, aFuente, aDescripcion, self)

    def addIngreso2(self, aIngreso):
        wasAdded = False
        if (aIngreso) in self._ingresos :
            return False
        existingUsuario = aIngreso.getUsuario()
        isNewUsuario = not (existingUsuario is None) and not self == existingUsuario
        if isNewUsuario :
            aIngreso.setUsuario(self)
        else :
            self._ingresos.append(aIngreso)
        wasAdded = True
        return wasAdded

    def removeIngreso(self, aIngreso):
        wasRemoved = False
        #Unable to remove aIngreso, as it must always have a usuario
        if not self == aIngreso.getUsuario() :
            self._ingresos.remove(aIngreso)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addIngresoAt(self, aIngreso, index):
        wasAdded = False
        if self.addIngreso(aIngreso) :
            if index < 0 :
                index = 0
            if index > self.numberOfIngresos() :
                index = self.numberOfIngresos() - 1
            self._ingresos.remove(aIngreso)
            self._ingresos.insert(index, aIngreso)
            wasAdded = True
        return wasAdded

    def addOrMoveIngresoAt(self, aIngreso, index):
        wasAdded = False
        if (aIngreso) in self._ingresos :
            if index < 0 :
                index = 0
            if index > self.numberOfIngresos() :
                index = self.numberOfIngresos() - 1
            self._ingresos.remove(aIngreso)
            self._ingresos.insert(index, aIngreso)
            wasAdded = True
        else :
            wasAdded = self.addIngresoAt(aIngreso, index)
        return wasAdded

    def delete(self):
        i = len(self._gastos)
        while i > 0 :
            aGasto = self._gastos[i - 1]
            aGasto.delete()
            i -= 1

        i = len(self._ingresos)
        while i > 0 :
            aIngreso = self._ingresos[i - 1]
            aIngreso.delete()
            i -= 1

    # line 8 "model.ump"
    def ingresarGasto(self, monto):
        print()
        

    # line 9 "model.ump"
    def ingresarIngreso(self, monto):
        print()

    # line 10 "model.ump"
    def verHistorialGastos(self):
        print()

    # line 11 "model.ump"
    def verBalance(self):
        print()

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "correoElectronico" + ":" + str(self.getCorreoElectronico()) + "," + "contrasena" + ":" + str(self.getContrasena()) + "," + "saldo" + ":" + str(self.getSaldo()) + "]"

    def addGasto(self, *argv):
        from Gasto import Gasto
        if len(argv) == 6 and isinstance(argv[0], int) and isinstance(argv[1], Date) and isinstance(argv[2], (float, int)) and isinstance(argv[3], str) and isinstance(argv[4], str) and isinstance(argv[5], CategoriaGasto) :
            return self.addGasto1(argv[0], argv[1], argv[2], argv[3], argv[4], argv[5])
        if len(argv) == 1 and isinstance(argv[0], Gasto) :
            return self.addGasto2(argv[0])
        raise TypeError("No method matches provided parameters")

    def addIngreso(self, *argv):
        from Ingreso import Ingreso
        if len(argv) == 5 and isinstance(argv[0], int) and isinstance(argv[1], Date) and isinstance(argv[2], (float, int)) and isinstance(argv[3], str) and isinstance(argv[4], str) :
            return self.addIngreso1(argv[0], argv[1], argv[2], argv[3], argv[4])
        if len(argv) == 1 and isinstance(argv[0], Ingreso) :
            return self.addIngreso2(argv[0])
        raise TypeError("No method matches provided parameters")




