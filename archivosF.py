import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
def busqueda_archivo():
    while True:
        t="""Escriba la opcion que desee
            1. Consultar historial de busqueda
            2. Consultar estadisticas y graficas de repositorios"""
        print(t)
        

        try:
            op=int(input("Opcion: "))
            if op in [1,2]:
                break
        except ValueError:
            print("Dato invalido")
            continue
        
    if op==1:
        historial()
    if op==2:
        estadisticas()
        plt.show()

    


def historial():

    print("Los registros guardados son:")
    archivos=os.listdir("registros/historial")
    if len(archivos)>1:

        for i,n in enumerate(archivos):
            print(f"id: {i+1} Nombre: {n}")
        
        while True:
            try:
                op=int(input("Selecciona el id del archivo que quieres consultar: "))
            except ValueError:
                print("Dato invalido")
                continue


            if op-1<len(archivos) and op-1>=0:
                with open(f"registros/historial/{archivos[op-1]}") as archivo:
                    contenido=archivo.read()
                    print(contenido)

                   

                    #ver si tiene internet

                    
            else:
                print("Opcion invalida")
                continue
    else:
        print("No hay registros guardados")


def estadisticas():
    if not os.path.exists("registros/estadisticas_re"):
        os.makedirs("registros/estadisticas_re")
    archivos=os.listdir("registros/estadisticas_re")

    print("Los repositorios consultados son:")
    if len("archivos")>0:
        for i,n in enumerate(archivos):
            print(f"Id:{i+1} {n}")
        
        

        while True:
            try:
                op=int(input("Selecciona el id del archivo que deses consultar: "))
                if op-1<len(archivos) and op>0:
                    break
                
            except ValueError:
                print("Dato invalido")
        
        with open(f"registros/estadisticas_re/{archivos[op-1]}") as f:
            contenido=f.read()
            print(contenido)
        n=archivos[op-1]
        n=n[:len(n)-4]

        print("Se mostraran las graficas generadas del repositorio")
        print(n)

        r=f"graficas/estadisticas/{n}"
        for grafica in os.listdir(r):
            img = mpimg.imread(os.path.join(r, grafica))
            plt.figure()
            imgplot = plt.imshow(img)
            plt.show(block=False)

        print(n)

if __name__ =="__main__":
    busqueda_archivo()