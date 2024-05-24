#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 17 "model.ump"
# line 52 "model.ump"
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
    @classmethod
    def alternateConstructor(cls, aId, aFecha, aMonto, aCategoria, aDescripcion, aCategoriaGasto, aUsuario):
        self = cls.__new__(cls)
        self._usuario = None
        self._categoriaGasto = None
        self._descripcion = None
        self._categoria = None
        self._monto = None
        self._fecha = None
        self._id = None
        self._id = aId
        self._fecha = aFecha
        self._monto = aMonto
        self._categoria = aCategoria
        self._descripcion = aDescripcion
        if aCategoriaGasto is None or not (aCategoriaGasto.getGasto() is None) :
            raise RuntimeError ("Unable to create Gasto due to aCategoriaGasto. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._categoriaGasto = aCategoriaGasto
        didAddUsuario = self.setUsuario(aUsuario)
        if not didAddUsuario :
            raise RuntimeError ("Unable to create gasto due to usuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        return self

    def __init__(self, aId, aFecha, aMonto, aCategoria, aDescripcion, aNombreForCategoriaGasto, aDescripcionForCategoriaGasto, aUsuario):
        from CategoriaGasto import CategoriaGasto
        self._usuario = None
        self._categoriaGasto = None
        self._descripcion = None
        self._categoria = None
        self._monto = None
        self._fecha = None
        self._id = None
        self._id = aId
        self._fecha = aFecha
        self._monto = aMonto
        self._categoria = aCategoria
        self._descripcion = aDescripcion
        self._categoriaGasto = CategoriaGasto.alternateConstructor(aNombreForCategoriaGasto, aDescripcionForCategoriaGasto, self)
        didAddUsuario = self.setUsuario(aUsuario)
        if not didAddUsuario :
            raise RuntimeError ("Unable to create gasto due to usuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setId(self, aId):
        wasSet = False
        self._id = aId
        wasSet = True
        return wasSet

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

    def setCategoria(self, aCategoria):
        wasSet = False
        self._categoria = aCategoria
        wasSet = True
        return wasSet

    def setDescripcion(self, aDescripcion):
        wasSet = False
        self._descripcion = aDescripcion
        wasSet = True
        return wasSet

    def getId(self):
        return self._id

    def getFecha(self):
        return self._fecha

    def getMonto(self):
        return self._monto

    def getCategoria(self):
        return self._categoria

    def getDescripcion(self):
        return self._descripcion

    # Code from template association_GetOne 
    def getCategoriaGasto(self):
        return self._categoriaGasto

    # Code from template association_GetOne 
    def getUsuario(self):
        return self._usuario

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

    def delete(self):
        existingCategoriaGasto = self._categoriaGasto
        self._categoriaGasto = None
        if not (existingCategoriaGasto is None) :
            existingCategoriaGasto.delete()
        placeholderUsuario = self._usuario
        self._usuario = None
        if not (placeholderUsuario is None) :
            placeholderUsuario.removeGasto(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "id" + ":" + str(self.getId()) + "," + "monto" + ":" + str(self.getMonto()) + "," + "categoria" + ":" + str(self.getCategoria()) + "," + "descripcion" + ":" + str(self.getDescripcion()) + "]" + str(os.linesep) + "  " + "fecha" + "=" + str((((self.getFecha().__str__().replaceAll("  ", "    ")) if not self.getFecha() == self else "this") if not (self.getFecha() is None) else "null")) + str(os.linesep) + "  " + "categoriaGasto = " + str(((format(id(self.getCategoriaGasto()), "x")) if not (self.getCategoriaGasto() is None) else "null")) + str(os.linesep) + "  " + "usuario = " + ((format(id(self.getUsuario()), "x")) if not (self.getUsuario() is None) else "null")




