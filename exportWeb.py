from krita import *
import os  
from PyQt5.QtWidgets import QFileDialog

class MyExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
      
        action = window.createAction("exportadorAction", "Exportador web", "tools/scripts")
        action.triggered.connect(self.wrapper)

    def exportToJPG(self):
        doc = Krita.instance().activeDocument()
        
       
        if not doc:
            print("No hay documento activo.")
            return

        original_path = doc.fileName()
        
        
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
           
            Krita.instance().action('flatten_image').trigger()
            doc.refreshProjection()
            print("Capas unidas.")
        
    def wrapper(self):
        
        self.flat_document()
        self.exportToJPG()


Krita.instance().addExtension(MyExtension(Krita.instance()))