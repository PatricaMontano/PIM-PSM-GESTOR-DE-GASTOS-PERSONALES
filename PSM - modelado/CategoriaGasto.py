#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 36 "model.ump"
# line 64 "model.ump"
import os

class CategoriaGasto():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #CategoriaGasto Attributes
    #CategoriaGasto Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    @classmethod
    def alternateConstructor(cls, aNombre, aDescripcion, aGasto):
        self = cls.__new__(cls)
        self._gasto = None
        self._descripcion = None
        self._nombre = None
        self._nombre = aNombre
        self._descripcion = aDescripcion
        if aGasto is None or not (aGasto.getCategoriaGasto() is None) :
            raise RuntimeError ("Unable to create CategoriaGasto due to aGasto. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._gasto = aGasto
        return self

    def __init__(self, aNombre, aDescripcion, aIdForGasto, aFechaForGasto, aMontoForGasto, aCategoriaForGasto, aDescripcionForGasto, aUsuarioForGasto):
        from Gasto import Gasto
        self._gasto = None
        self._descripcion = None
        self._nombre = None
        self._nombre = aNombre
        self._descripcion = aDescripcion
        self._gasto = Gasto.alternateConstructor(aIdForGasto, aFechaForGasto, aMontoForGasto, aCategoriaForGasto, aDescripcionForGasto, self, aUsuarioForGasto)

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

    # Code from template association_GetOne 
    def getGasto(self):
        return self._gasto

    def delete(self):
        existingGasto = self._gasto
        self._gasto = None
        if not (existingGasto is None) :
            existingGasto.delete()

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "descripcion" + ":" + str(self.getDescripcion()) + "]" + str(os.linesep) + "  " + "gasto = " + ((format(id(self.getGasto()), "x")) if not (self.getGasto() is None) else "null")




