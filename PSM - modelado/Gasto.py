#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 23 "model.ump"
# line 54 "model.ump"
import os

class Gasto():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Gasto Attributes
    #Gasto Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aFecha, aMonto, aDescripcion, aUsuario, aCategoriaGasto):
        self._categoriaGasto = None
        self._usuario = None
        self._descripcion = None
        self._monto = None
        self._fecha = None
        self._fecha = aFecha
        self._monto = aMonto
        self._descripcion = aDescripcion
        didAddUsuario = self.setUsuario(aUsuario)
        if not didAddUsuario :
            raise RuntimeError ("Unable to create gasto due to usuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddCategoriaGasto = self.setCategoriaGasto(aCategoriaGasto)
        if not didAddCategoriaGasto :
            raise RuntimeError ("Unable to create gasto due to categoriaGasto. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setFecha(self, aFecha):
        wasSet = False
        self._fecha = aFecha
        wasSet = True
        return wasSet

    def setMonto(self, aMonto):
        wasSet = False
        self._monto = aMonto
        wasSet = True
        return wasSet

    def setDescripcion(self, aDescripcion):
        wasSet = False
        self._descripcion = aDescripcion
        wasSet = True
        return wasSet

    def getFecha(self):
        return self._fecha

    def getMonto(self):
        return self._monto

    def getDescripcion(self):
        return self._descripcion

    # Code from template association_GetOne 
    def getUsuario(self):
        return self._usuario

    # Code from template association_GetOne 
    def getCategoriaGasto(self):
        return self._categoriaGasto

    # Code from template association_SetOneToMany 
    def setUsuario(self, aUsuario):
        wasSet = False
        if aUsuario is None :
            return wasSet
        existingUsuario = self._usuario
        self._usuario = aUsuario
        if not (existingUsuario is None) and not existingUsuario == aUsuario :
            existingUsuario.removeGasto(self)
        self._usuario.addGasto(self)
        wasSet = True
        return wasSet

    # Code from template association_SetOneToMany 
    def setCategoriaGasto(self, aCategoriaGasto):
        wasSet = False
        if aCategoriaGasto is None :
            return wasSet
        existingCategoriaGasto = self._categoriaGasto
        self._categoriaGasto = aCategoriaGasto
        if not (existingCategoriaGasto is None) and not existingCategoriaGasto == aCategoriaGasto :
            existingCategoriaGasto.removeGasto(self)
        self._categoriaGasto.addGasto(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderUsuario = self._usuario
        self._usuario = None
        if not (placeholderUsuario is None) :
            placeholderUsuario.removeGasto(self)
        placeholderCategoriaGasto = self._categoriaGasto
        self._categoriaGasto = None
        if not (placeholderCategoriaGasto is None) :
            placeholderCategoriaGasto.removeGasto(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "monto" + ":" + str(self.getMonto()) + "," + "descripcion" + ":" + str(self.getDescripcion()) + "]" + str(os.linesep) + "  " + "fecha" + "=" + str((((self.getFecha().__str__().replaceAll("  ", "    ")) if not self.getFecha() == self else "this") if not (self.getFecha() is None) else "null")) + str(os.linesep) + "  " + "usuario = " + str(((format(id(self.getUsuario()), "x")) if not (self.getUsuario() is None) else "null")) + str(os.linesep) + "  " + "categoriaGasto = " + ((format(id(self.getCategoriaGasto()), "x")) if not (self.getCategoriaGasto() is None) else "null")

