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
    
    def createCopy(self):
        k = krita.intance()
        doc = k.activeDocument()
        
        if doc is not None:
            fileName, _ = QFileDialog.getSaveFileName(  
                                                       None, "Guardar Copia", "", "Archivos de Krita (*.kra);;PNG (*.png);;JPG (*.jpg)"
                                                       )
            if fileName:
                doc.exportImage(fileName, infoObject())
                print(f"Copia guardada en: {fileName}")
                
    def scaleDocument(self):
        k = krita.instance()
        
        doc = k.activeDocument()
        
        if doc:
            width = doc.width;
            height = doc.height;
            if height >= 3000 :
                new_height = 3000;
                new_width = (width * new_height ) / height ;
                doc.scaleImage(new_width, new_height, 72, 72, Bilinear);
                doc.refreshProjection()
                k.notifier().imageChanged.emit()
            else :
                print("To small");
        else:
            ("No document")
                
                    
        
    def exportDocument(self):
        # Get the document:
        doc =  Krita.instance().activeDocument()
        # Saving a non-existent document causes crashes, so lets check for that first.
        if doc is not None:
            # This calls up the save dialog. The save dialog returns a tuple.
            fileName = QFileDialog.getSaveFileName()[0]
            # And export the document to the fileName location.
            # InfoObject is a dictionary with specific export options, but when we make an empty one Krita will use the export defaults.
            doc.exportImage(fileName, InfoObject())
            
    def wraper (self):
        scaleDocument();
        createCopy();
        exportDocument();
        
    
# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(MyExtension(Krita.instance()))
