from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

class NeuralNetwork(object):
  def __init__(self):
    #weights initilization
    self.ran1=np.random.randint(0, 10)
    self.ran2=np.random.randint(0, 10)
    self.ran3=np.random.randint(0, 10)
    self.weights=[0]*3
    self.weights[0]=self.ran1
    self.weights[1]=self.ran2
    self.weights[2]=self.ran3
    #learning rate initilization
    self.learning_r=1
    #history variable initilization
    self.history={"wzero": [0]* 51,
                  "wone": [0]* 51,
                  "wtwo": [0]* 51,
                  "jtheta": [0]* 51}
    self.history["wzero"][0]=self.ran1
    self.history["wone"][0]=self.ran2
    self.history["wtwo"][0]=self.ran3

  def forward_propagation(self):
    rr,cc=self.inputs.shape
    a=0
    self.vf=((self.in1)*(self.weights[0]))+((self.in2)*(self.weights[1]))+((self.in3)*(self.weights[2]))
    return(self.vf)

  def train(self, inputs, labels, num_train_epochs=10):
    fig, axs = plt.subplots(2)
    self.xzero=[0]*10
    self.xza=0
    self.xone=[0]*10
    self.xoa=0
    self.xtwo=[0]*10
    self.xta=0
    self.fps=[0]*10
    self.fpsa=0
    self.inputs=inputs
    self.labels=labels
    self.dw0=0
    self.dw1=0
    self.dw2=0
    self.jt=0
    self.bc=0
    self.yy1=0
    self.yy2=0
    self.yy3=0
    xxx=[0]*51
    r,c=self.inputs.shape
    i=0
    b=0
    c=0
    for b in range (num_train_epochs):
      xxx[b]=b
      self.xzero=[0]*10
      self.xza=0
      self.xone=[0]*10
      self.xoa=0
      self.xtwo=[0]*10
      self.xta=0
      self.fps=[0]*10
      self.fpsa=0
      self.jt=0
      self.dw0=0
      self.dw1=0
      self.dw2=0
      self.bc=0
      self.y=0
      self.x=0
      self.bb=0
      self.yy1=0
      self.yy2=0
      self.yy3=0
      for i in  range (r):
        self.in1=self.inputs[i][0]
        self.in2=self.inputs[i][1]
        self.in3=self.inputs[i][2]

        self.xzero[i]=self.in1*(self.labels[i]-self.forward_propagation())
        self.xone[i]=self.in2*(self.labels[i]-self.forward_propagation())
        self.xtwo[i]=self.in3*(self.labels[i]-self.forward_propagation())

        self.fps[i]=(self.labels[i]-self.forward_propagation())**2
      
      for c in range (10):
        self.xza=self.xza+self.xzero[c]
        self.xoa=self.xza+self.xone[c]
        self.xta=self.xza+self.xtwo[c]

        self.fpsa=self.fpsa+self.fps[c]
      
      self.dw0=(self.learning_r/r)*self.xza
      self.dw1=(self.learning_r/r)*self.xoa
      self.dw2=(self.learning_r/r)*self.xta

      self.weights[0]=self.weights[0]+self.dw0
      self.weights[1]=self.weights[1]+self.dw1
      self.weights[2]=self.weights[2]+self.dw2

      self.history["wzero"][b+1]=self.weights[0]
      self.history["wone"][b+1]=self.weights[1]
      self.history["wtwo"][b+1]=self.weights[2]

      
      self.jt=self.fpsa/(2*r)
      self.history["jtheta"][b+1]=self.jt
      print(" ")
      print("---------------------------------")
      print("Epoch: ", b+1)
      print("w0: ", self.history["wzero"][b+1])
      print("w1: ", self.history["wone"][b+1])
      print("w2: ", self.history["wtwo"][b+1])
      print("J Theta: ", self.history["jtheta"][b+1])
      
      #classifier line every 5 epochs
      self.bc=(b+1)/5
      if self.bc%5==0 or b==0:
        self.x=self.weights[1]
        self.y=self.weights[2]*-1
        self.bb=self.weights[0]

        self.x=self.x/self.y
        self.bb=self.bb/self.y

        xx = [-3,0,3]
        self.yy1=(self.x*xx[0])+self.bb
        self.yy2=(self.x*xx[1])+self.bb
        self.yy3=(self.x*xx[2])+self.bb
        yy = [self.yy1, self.yy2, self.yy3 ]
        axs[1].plot(xx, yy)

    axs[0].plot(xxx, self.history["jtheta"])


inp=np.array([1,1,1, 1,1,0, 1,0,1, 1,-1,-1, 1,0.5,3, 1,0.7,2, 1,-1,0, 1,-1,1, 1,2,0, 1,-2,-1])
input=inp.reshape( (10,3) )
labels=[0]*10
labels[0]=1
labels[1]=1
labels[2]=-1
labels[3]=-1
labels[4]=1
labels[5]=1
labels[6]=-1
labels[7]=-1
labels[8]=1
labels[9]=-1
t=NeuralNetwork()

print( t.train(input,labels,50))
r,c=input.shape
i=0
for i in  range (r):
  if labels[i]==1:
    one, = plt.plot(input[i][1],input[i][2], "r^", markersize=10)
  else:
    none, = plt.plot(input[i][1],input[i][2], "bo", markersize=10)
