from krita import *
import os  # <-- Faltaba esta importación para manejar rutas
from PyQt5.QtWidgets import QFileDialog

class MyExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        # Asegúrate de que el ID "myAction" sea único
        action = window.createAction("exportadorAction", "Exportador web", "tools/scripts")
        action.triggered.connect(self.wrapper)

    def exportToJPG(self):
        doc = Krita.instance().activeDocument()
        
        # Validación de seguridad: ¿Hay un documento abierto?
        if not doc:
            print("No hay documento activo.")
            return

        original_path = doc.fileName()
        
        # Si el documento nunca se ha guardado, fileName() está vacío
        if not original_path:
            print("Guarda el documento primero para obtener una ruta base.")
            return

        directory = os.path.dirname(original_path)
        base = os.path.splitext(original_path)[0]
        new_name = base + "_copy_web.jpg"
        new_path = os.path.join(directory, new_name)

        exportParameters = InfoObject()
        exportParameters.setProperty("quality", 80)
        exportParameters.setProperty("saveProfile", False) 
        
        # Exportar
        doc.exportImage(new_path, exportParameters)
        print(f"Imagen exportada a: {new_path}")
         
    def flat_document(self):
        doc = Krita.instance().activeDocument()
        if doc:
            # Usar la acción de Krita para acoplar
            Krita.instance().action('flatten_image').trigger()
            doc.refreshProjection()
            print("Capas unidas.")
        
    def wrapper(self):
        # IMPORTANTE: En Python, los métodos se llaman con paréntesis ()
        self.flat_document()
        self.exportToJPG()

# Registrar la extensión
Krita.instance().addExtension(MyExtension(Krita.instance()))