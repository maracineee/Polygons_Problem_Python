import math
from Point import *
from FunctiiAjutatoare import *
class Poligon:
   
    def __init__(self,nrPuncte):
        self.nrPuncte=nrPuncte
        if self.nrPuncte<3:
            print("Poligonul trebuie sa aiba minim 3 puncte!")
        else:
            Points=[]
            for i in range(nrPuncte):
                print("Introdu abscisa punctului",i+1,":")
                a=int(input())
                print("Introdu ordonata punctului",i+1,":")
                b=int(input())
                p1=Point(a,b)
                Points.append(p1)
            self.listaPuncte=Points

    def printPoligon(self):
        for i in range(self.nrPuncte):
            print("Punctul ",i+1," are coordonatele: (",self.listaPuncte[i].x,",",self.listaPuncte[i].y,")")

    def perimetruPoligon(self):
        suma=0
        n=self.nrPuncte
        per=self.listaPuncte
        for i in range(n-1):
            suma=suma+lungimeLatura(per[i].x,per[i].y,per[i+1].x,per[i+1].y)
        suma=suma+lungimeLatura(per[n-1].x,per[n-1].y,per[0].x,per[0].y)
        print("Perimetrul poligonului este:")
        return suma

    def ariePoligon(self):
        aria=0
        per=self.listaPuncte
        n=self.nrPuncte
        for i in range(n-1):
            aria=aria+((per[i].x*per[i+1].y)-(per[i].y*per[i+1].x))
        aria=aria+((per[n-1].x*per[0].y)-(per[n-1].y*per[0].x))
        return (abs(aria))/2
            
    def gravityCenter(self):
        gc=self.listaPuncte
        coordY=0
        coordX=0
        n=self.nrPuncte
        for i in range(n-1):
            coordX=coordX+(gc[i].x+gc[i+1].x)*(gc[i].x*gc[i+1].y-gc[i+1].x*gc[i].y)
            coordY=coordY+(gc[i].y+gc[i+1].y)*(gc[i].x*gc[i+1].y-gc[i+1].x*gc[i].y)
        aria=self.ariePoligon()
        aria=abs(aria)/2
        print("Abscisa este: ",coordX/(6*aria))
        print("Ordonata este: ",coordY/(6*aria))


    def comparisonAreas(self,poli2):
        area1=self.ariePoligon()
        area2=poli2.ariePoligon()
        if area1>area2:
            print("Aria primului poligon este mai mare decat a celui de-al doilea")
        elif area1<area2:
            print("Aria celui de al doilea poligon este mai mare decat a primului poligon")
        else:
           print("Ariile sunt egale.")

    def concatenarePoligoane(self,b):
        pol1=self.listaPuncte
        pol2=b.listaPuncte
        n=self.nrPuncte
        bnr=b.nrPuncte
        p=[]
        for i in range(n):
            p.append(pol1[i])
        for i in range(bnr):
            p.append(pol2[i])
        print("Noul poligon rezultat are coordonatele punctelor:")
        return convexHull(p,len(p))

    

    def rectangleMinArea(self):
        maxX=-100000
        minX=100000
        maxY=-100000
        minY=100000
        lista=self.listaPuncte
        n=self.nrPuncte
        for i in range(n):
            if(lista[i].x<minX):
                minX=lista[i].x
            if(lista[i].x>maxX):
                maxX=lista[i].x
            if(lista[i].y<minY):
                minY=lista[i].y
            if(lista[i].y>maxY):
                maxY=lista[i].y
        print("Coordonatele dreptunghiului cu arie minima sunt:")
        p1=Point(minX,maxY)
        p1.printPoint()
        p2=Point(maxX,maxY)
        p2.printPoint()
        p3=Point(minX,minY)
        p3.printPoint()
        p4=Point(maxX,minY)
        p4.printPoint()

    

    

def meniu():
    print("Buna ziua! Introduceti cifra corespunzatoare alegerii pe care vreti sa o faceti:")
    print("1-->Crearea altui poligon")
    print("2-->Afisarea unui poligon")
    print("3-->Perimetrul unui poligon")
    print("4-->Aria unui poligon")
    print("5-->Compararea ariilor a 2 poligoane")
    print("6-->Calcularea centrului de gravitatie a unui poligon")
    print("7-->Concatenarea a doua poligoane")
    print("8-->Dreptunghiul cu arie minima din interiorul poligonului.")
    print("9-->Iesire din program")
    alegere=int(input())
    if alegere==9:
        print("La revedere!")
    if alegere!=9:
        
        if alegere==1:
            print("Introduceti numarul de puncte al poligonului:")
            y=int(input())
            poli2=Poligon(y)
            print("Poligonul a fost creat!")

        if(alegere!=1):
            print("Introduceti numarul de puncte al poligonului:")
            n=int(input())
            poli= Poligon(n)
            if alegere==2:
                poli.printPoligon()
            elif alegere==3:
                print(poli.perimetruPoligon())
            elif alegere==4:
                print(poli.ariePoligon())
            elif alegere==5:
                print("Numarul de puncte al celuilalt poligon este:")
                b=int(input())
                poli3=Poligon(b)
                
                poli.comparisonAreas(poli3)
            elif alegere==6:
                poli.gravityCenter()
            elif alegere==7:
                print("Numarul de puncte al celui de al doilea poligon este:")
                b=int(input())
                poli3=Poligon(b)
                poli.concatenarePoligoane(poli3)
            elif alegere==8:
                poli.rectangleMinArea()