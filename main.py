import numpy as np
print(np.__version__)

def createArray():
  nullD = np.array([1, 2, 3, 4, 5])
  OneD = np.array([[1, 2, 3] , [3, 4, 5]] , dtype = int)
  ZweiD = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9] , [10, 11, 12]]], dtype = int)
  #print(type(OneD))
  #print(type(nullD))
  #print(type(ZweiD))
  OneD = np.delete(OneD, 0, 1)
  #print(OneD)
  b = np.arange(1,16)
  #print(b)
  #print(ZweiD)
  first = np.zeros((1,15), dtype = int)
  #print(first)
  second = np.ones(((1,15)),dtype = int)
  #print(second)
  hi = np.concatenate((first, second), axis=None)
  ho = np.concatenate((hi, b), axis=None)
  #print(hi)
  print(ho)
  shapeArray(ho)

def shapeArray(arr):
  #No esošā masīva izdeivojiet daudzdimensionālu masīvu. Kollonnu un rindu skaits pēc brīvas izvēles
  x = arr.reshape(9,5)
  print(x)
  #Padod masīvu sliceArray()
  sliceArray(x)

def sliceArray(arr):
#Sagriez masīvu tā, lai tiktu izvēlēti visi otrās kolonnas elementi
  x = arr[0:, 2]
  #print(x)
#Padod sagriezto masīvu arrayIO()
  arrayIO(x)
  

def arrayIO(arr):
 #Ieraksti rezultātus failā. Faila nosaukums pēc brīvas izvēles. Var katram ierakstam veidot savu failu, bet vēlams ierakstīt vienā failā 
 
  return None

#def readArray():
#Ielasi masīvu no kāda izveidotā faila un saglabā jaunā masīvā
#Jauno masīvu padod arithmetic() funkcijai

#def arithmetic():
#Izveido jaunu masīvu
#Veic trīs aritimētiskās operācijas pēc brīvas izvēles ar abiem masīviem
#Rezultātus saglabā failā 'results'

#def statistics():
#Ielasi rezultātus jaunā masīvā
#Aprēķini rezultātu vidējo aritimētisko
#Aptrēķini rezultātu korelācijas koeficientu
#Aprēķini mediānu
#Ieraksti rezultātus 'stats' failā



createArray()
