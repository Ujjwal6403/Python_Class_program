# Duck typing : It is a concept where the type of an object is determined 
# but its behaviour, not by its class
class InkjetPrinter:
   def printdocument(self,document):
      print("Inkjet printer printing : ",document)
      
class LaserPrinter:
   def printdocument(self,document):
      print("Laser printer printing : ",document)

class PDFWriter:
   def printdocument(self,document):
      print(f"Saving : {document} as pdf ")
   
def StartPrinting(Device):
   Device.printdocument("marvellous Notes")
   
def main():
   StartPrinting(InkjetPrinter())
   StartPrinting(LaserPrinter())
   StartPrinting(PDFWriter())

main()