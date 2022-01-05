#Chris Costa
#7/12/21
#Intro to Python Programming
#A6
from google.colab import files
import csv
import math
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
uploaded = files.upload()
file = open("iris.csv", "r")
cf=csv.reader(file)

def csv_data():
  #Setosa
  ssll=[0.0]*51
  ssln=[0.0]*51
  sslnsd=[0.0]*52
  ssla=0.0

  sswl=[0.0]*51
  sswn=[0.0]*51
  sswnsd=[0.0]*52
  sswa=0.0

  spll=[0.0]*51
  spln=[0.0]*51
  splnsd=[0.0]*52
  spla=0.0

  spwl=[0.0]*51
  spwn=[0.0]*51
  spwnsd=[0.0]*52
  spwa=0.0

  #Versicolor
  vesll=[0.0]*51
  vesln=[0.0]*51
  veslnsd=[0.0]*52
  vesla=0.0

  veswl=[0.0]*51
  veswn=[0.0]*51
  veswnsd=[0.0]*52
  veswa=0.0

  vepll=[0.0]*51
  vepln=[0.0]*51
  veplnsd=[0.0]*52
  vepla=0.0

  vepwl=[0.0]*51
  vepwn=[0.0]*51
  vepwnsd=[0.0]*52
  vepwa=0.0

  #Virginica
  visll=[0.0]*51
  visln=[0.0]*51
  vislnsd=[0.0]*52
  visla=0.0

  viswl=[0.0]*51
  viswn=[0.0]*51
  viswnsd=[0.0]*52
  viswa=0.0

  vipll=[0.0]*51
  vipln=[0.0]*51
  viplnsd=[0.0]*52
  vipla=0.0

  vipwl=[0.0]*51
  vipwn=[0.0]*51
  vipwnsd=[0.0]*52
  vipwa=0.0

  i=0
  next(cf)
  for lines in cf:
    
    if lines[4]=="setosa":
      
      ssll[i]= float(lines[0])
      sswl[i]= float(lines[1])
      spll[i]= float(lines[2])
      spwl[i]= float(lines[3])

      i+=1
      if i>=50:
        i=0

    elif lines[4]=="versicolor":

      vesll[i]= float(lines[0])
      veswl[i]= float(lines[1])
      vepll[i]= float(lines[2])
      vepwl[i]= float(lines[3])

      i+=1
      if i>=50:
        i=0

    elif lines[4]=="virginica":

      visll[i]= float(lines[0])
      viswl[i]= float(lines[1])
      vipll[i]= float(lines[2])
      vipwl[i]= float(lines[3])

      i+=1
      if i>=50:
        i=0

  #normilization
  i=0
  while i<=49:
    #Setosa normalized
    ssln[i]=ssll[i]-min(ssll)
    ssln[i]=ssln[i]/(max(ssll)-min(ssll))

    sswn[i]=sswl[i]-min(sswl)
    sswn[i]=sswn[i]/(max(sswl)-min(sswl))

    spln[i]=spll[i]-min(spll)
    spln[i]=spln[i]/(max(spll)-min(spll))

    spwn[i]=spwl[i]-min(spwl)
    spwn[i]=spwn[i]/(max(spwl)-min(spwl))

    #Versicolor normalized
    vesln[i]=vesll[i]-min(vesll)
    vesln[i]=vesln[i]/(max(vesll)-min(vesll))

    veswn[i]=veswl[i]-min(veswl)
    veswn[i]=veswn[i]/(max(veswl)-min(veswl))

    vepln[i]=vepll[i]-min(vepll)
    vepln[i]=vepln[i]/(max(vepll)-min(vepll))

    vepwn[i]=vepwl[i]-min(vepwl)
    vepwn[i]=vepwn[i]/(max(vepwl)-min(vepwl))

    #Virginica normalized
    visln[i]=visll[i]-min(visll)
    visln[i]=visln[i]/(max(visll)-min(visll))

    viswn[i]=viswl[i]-min(viswl)
    viswn[i]=viswn[i]/(max(viswl)-min(viswl))

    vipln[i]=vipll[i]-min(vipll)
    vipln[i]=vipln[i]/(max(vipll)-min(vipll))

    vipwn[i]=vipwl[i]-min(vipwl)
    vipwn[i]=vipwn[i]/(max(vipwl)-min(vipwl))

    i+=1

  i=0
  while i<=49:
    #Setosa add part of avgs
    ssla+=ssln[i]
    sswa+=sswn[i]
    spla+=spln[i]
    spwa+=spwn[i]

    #Versicolor add part of avgs
    vesla+=vesln[i]
    veswa+=veswn[i]
    vepla+=vepln[i]
    vepwa+=vepwn[i]

    #Virginica add part of avgs
    visla+=visln[i]
    viswa+=viswn[i]
    vipla+=vipln[i]
    vipwa+=vipwn[i]

    i+=1
  #Setosa avgs
  ssla=ssla/50
  sswa=sswa/50
  spla=spla/50
  spwa=spwa/50

  #Versicolor avgs
  vesla=vesla/50
  veswa=veswa/50
  vepla=vepla/50
  vepwa=vepwa/50

  #Virginica avgs
  visla=visla/50
  viswa=viswa/50
  vipla=vipla/50
  vipwa=vipwa/50
  i=0
  while i<=49:
    #Setosa pows for standard div
    sslnsd[i]=pow(ssln[i]-ssla, 2)
    sswnsd[i]=pow(sswn[i]-sswa, 2)
    splnsd[i]=pow(spln[i]-spla, 2)
    spwnsd[i]=pow(spwn[i]-spwa, 2)

    #Versicolor pows for standard div
    veslnsd[i]=pow(vesln[i]-vesla, 2)
    veswnsd[i]=pow(veswn[i]-veswa, 2)
    veplnsd[i]=pow(vepln[i]-vepla, 2)
    vepwnsd[i]=pow(vepwn[i]-vepwa, 2)

    #Virginica pow for standard div
    vislnsd[i]=pow(visln[i]-visla, 2)
    viswnsd[i]=pow(viswn[i]-viswa, 2)
    viplnsd[i]=pow(vipln[i]-vipla, 2)
    vipwnsd[i]=pow(vipwn[i]-vipwa, 2)

    i+=1
  i=0
  while i<=49:
    #Setosa add for avg for sd
    sslnsd[50]+=sslnsd[i]
    sswnsd[50]+=sswnsd[i]
    splnsd[50]+=splnsd[i]
    spwnsd[50]+=spwnsd[i]

    #Versicolor add for avg for sd
    veslnsd[50]+=veslnsd[i]
    veswnsd[50]+=veswnsd[i]
    veplnsd[50]+=veplnsd[i]
    vepwnsd[50]+=vepwnsd[i]

    #Virginica add for avg for sd
    vislnsd[50]+=vislnsd[i]
    viswnsd[50]+=viswnsd[i]
    viplnsd[50]+=viplnsd[i]
    vipwnsd[50]+=vipwnsd[i]

    i+=1

  #Setosa square roots of avgs for sd
  sslnsd[51]=math.sqrt(sslnsd[50]/50)
  sswnsd[51]=math.sqrt(sswnsd[50]/50)
  splnsd[51]=math.sqrt(splnsd[50]/50)
  spwnsd[51]=math.sqrt(spwnsd[50]/50)

  #Versicolor square roots of avgs for sd
  veslnsd[51]=math.sqrt(veslnsd[50]/50)
  veswnsd[51]=math.sqrt(veswnsd[50]/50)
  veplnsd[51]=math.sqrt(veplnsd[50]/50)
  vepwnsd[51]=math.sqrt(vepwnsd[50]/50)

  #Virginica square roots of avgs for sd
  vislnsd[51]=math.sqrt(vislnsd[50]/50)
  viswnsd[51]=math.sqrt(viswnsd[50]/50)
  viplnsd[51]=math.sqrt(viplnsd[50]/50)
  vipwnsd[51]=math.sqrt(vipwnsd[50]/50)

  #Setosa dictonary
  sd={"mean": [round(ssla,2), round(sswa,2), round(spla,2), round(spwa,2)],
      "min": [min(ssln), min(sswn), min(spln), min(spwn)],
      "max": [max(ssln), max(sswn), max(spln), max(spwn)],
      "sd": [round(sslnsd[51],2), round(sswnsd[51],2), round(splnsd[51],2),round(spwnsd[51],2)]}
  
  #Versicolor dictonary
  ved={"mean": [round(vesla,2), round(veswa,2), round(vepla,2), round(vepwa,2)],
      "min": [min(vesln), min(veswn), min(vepln), min(vepwn)],
      "max": [max(vesln), max(veswn), max(vepln), max(vepwn)],
      "sd": [round(veslnsd[51],2), round(veswnsd[51],2), round(veplnsd[51],2), round(vepwnsd[51],2)]}
  
  #Virginica dictionary
  vid={"mean": [round(visla,2), round(viswa,2), round(vipla,2), round(vipwa,2)],
      "min": [min(visln), min(viswn), min(vipln), min(vipwn)],
      "max": [max(visln), max(viswn), max(vipln), max(vipwn)],
      "sd": [round(vislnsd[51],2), round(viswnsd[51],2), round(viplnsd[51],2), round(vipwnsd[51],2)]}
  
  print("Here are the attributes for every flower")
  print("-------------------------------------")

  print("Setosa -   Sepal Length   Sepal Width   Petal Width   Petal Length")                  
  print("Mean: ", sd["mean"])
  print("Minimum: ", sd["min"])
  print("Maximum: ", sd["max"])
  print("Standard Deviation: ", sd["sd"])

  print("-------------------------------------")
  print("Versicolor -   Sepal Length   Sepal Width   Petal Width   Petal Length")                  
  print("Mean: ", ved["mean"])
  print("Minimum: ",ved["min"])
  print("Maximum: ", ved["max"])
  print("Standard Deviation: ", ved["sd"])

  print("-------------------------------------")
  print("Virginica -   Sepal Length   Sepal Width   Petal Width   Petal Length")                  
  print("Mean: ", vid["mean"])
  print("Minimum: ",vid["min"])
  print("Maximum: ", vid["max"])
  print("Standard Deviation: ", vid["sd"])
