#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 29 "model.ump"
# line 59 "model.ump"
import os

class Ingreso():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Ingreso Attributes
    #Ingreso Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aFecha, aMonto, aFuente, aDescripcion, aUsuario):
        self._usuario = None
        self._descripcion = None
        self._fuente = None
        self._monto = None
        self._fecha = None
        self._fecha = aFecha
        self._monto = aMonto
        self._fuente = aFuente
        self._descripcion = aDescripcion
        didAddUsuario = self.setUsuario(aUsuario)
        if not didAddUsuario :
            raise RuntimeError ("Unable to create ingreso due to usuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

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

    def setFuente(self, aFuente):
        wasSet = False
        self._fuente = aFuente
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

    def getFuente(self):
        return self._fuente

    def getDescripcion(self):
        return self._descripcion

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
            existingUsuario.removeIngreso(self)
        self._usuario.addIngreso(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderUsuario = self._usuario
        self._usuario = None
        if not (placeholderUsuario is None) :
            placeholderUsuario.removeIngreso(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "monto" + ":" + str(self.getMonto()) + "," + "fuente" + ":" + str(self.getFuente()) + "," + "descripcion" + ":" + str(self.getDescripcion()) + "]" + str(os.linesep) + "  " + "fecha" + "=" + str((((self.getFecha().__str__().replaceAll("  ", "    ")) if not self.getFecha() == self else "this") if not (self.getFecha() is None) else "null")) + str(os.linesep) + "  " + "usuario = " + ((format(id(self.getUsuario()), "x")) if not (self.getUsuario() is None) else "null")

