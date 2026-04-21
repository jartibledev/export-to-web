from krita import *
from PyQt5.QtWidgets import QFileDialog

class MyExtension(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("myAction", "My Script")
        action.triggered.connect(self.wrapper)

    def exportToJPG():
        # Obtener el documento activo
        doc = Krita.instance().activeDocument()
        original_path = doc.fileName()
        directory = os.path.dirname(original_path)
        # --- CONFIGURA TU NOMBRE PREDETERMINADO AQUÍ ---
        base = os.path.splitext(original_path)[0]
        new_name = base + "_copy_web.jpg"
        new_path = os.path.join(directory, new_name)
        #if not doc:
            #return

        # Pedir ubicación del archivo
        #filename, _ = QFileDialog.getSaveFileName(None, "Exportar a JPG", "", "JPG Images (*.jpg *.jpeg)")
        
        #if filename:
            # Configurar opciones de exportación (opcional)
        exportParameters = InfoObject()
        exportParameters.setProperty("quality", 80) # Calidad 0-100
        exportParameters.setProperty("saveProfile", False) 
        
        
            # Exportar
        doc.exportImage(new_path, exportParameters)
        print(f"Imagen exportada a: {new_path}")
   
         
    def flat_document ():
        currentDocument = Krita.instance().activeDocument()
        Krita.instance().action('flatten_image').trigger()
        currentDocument.refreshProjection()
        print("Capas unidas.")
        
    
    
    
    def wrapper (self):
        self.flat_document
        self.exportToJPG
        
    
# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(MyExtension(Krita.instance()))
