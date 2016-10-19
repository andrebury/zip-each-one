import os
import zipfile

def zipar(listadir, arq):
   file = zipfile.ZipFile(listadir + arq + ".zip", 'w', zipfile.ZIP_DEFLATED)
   file.write(listadir + arq)
   file.close()


def checarzip(listadir):
   totalarqs = os.listdir(listadir)
   for arq in totalarqs:
       if arq.lower().find("zip") < 1 and arq.lower().find("wav") > 1 and os.path.isfile(listadir + arq):
           zipar(listadir, arq)
           print(arq)

checarzip("C:\\CLIENTIS_VIVO\\Julho\\FASE1_Julho16_Entrega_26072016\\Chamadas Consolidadas_ Fase 1_Julho16\\")
print("Acabou!")
