import csv
import numpy as np

def ivt(data,v_threshold):
  times = data[:,[0]]
  ts = []

  # convert time to second
  for t in times:
    ts.append(float(t)/1000.0)
  
  Xs = data[:,[1]]
  Ys = data[:,[2]]

  diffX = [] #x values difference
  diffY = [] #y values difference 
  diffT = [] #time values difference

  # difX=x2-x1 and diffY=y2-y1
  for i in range(len(data) - 1):
    diffX.append(float(Xs[i+1]) - float(Xs[i]) )
    diffY.append(float(Ys[i+1]) - float(Ys[i]) )
    diffT.append(float(ts[i+1]) - float(ts[i]) )
  
  # distance = sqrt(x^2 + y^2)
  distance = np.sqrt(np.power(diffX,2) + np.power(diffY,2))
  
  # calculate velocity
  velocity = np.divide(distance,diffT)
  
  mvmts = []
  
  #store 1 in mvmts[] if velocity is less than threshold else store 0
  for v in velocity:
    if(v<v_threshold):
        mvmts.append(1)
    else:
        mvmts.append(0)
  
  

  fixations = []
  fs = []

  # storing index value of mvmts=1 to fs[]
  # when mvmts=0 append fs[] to fixation[]
  for m in range(len(mvmts)):
    if(mvmts[m] == 0):
      if(len(fs) > 0):
        fixations.append(fs)
        fs = []
    else:
      fs.append(m)

  # appending remaining values of fs[] to fixation[]
  if(len(fs) > 0):
    fixations.append(fs)

  centroidsX = []
  centroidsY = []
  time0 = []
  time1 = []

  #
  for f in fixations:
    cX = 0.0 
    cY = 0.0
    
    if(len(f) == 1):
      i = f[0]
      # print("i",i,"f",f)
      # print(data[i][1])
      cX = (float(data[i][1]) + float(data[i+1][1]))/2.0
      cY = (float(data[i][2]) + float(data[i+1][2]))/2.0
      t0 = float(data[i][0])
      t1 = float(data[i+1][0])
    else:
      t0 = float(data[f[0]][0])
      t1 = float(data[f[len(f)-1]+1][0])
      
      for e in range(len(f)):
        
        cX  += float(data[f[e]][1])
        cY  += float(data[f[e]][2])

      cX += float(data[f[len(f)-1]][1])
      cY += float(data[f[len(f)-1]][2])

      cX = cX / float(len(f)+1)
      cY = cY / float(len(f)+1)

    centroidsX.append(cX)
    centroidsY.append(cY)
    time0.append(t0)
    time1.append(t1)

  print("x",centroidsX)
  print("y",centroidsY)
  print("t0",time0)
  print("t1",time1)


if __name__ == '__main__':
  with open('real.csv', 'rb') as cf:
    reader = csv.reader(cf, delimiter=',')
    count = 0
    no_of_columns = len(next(reader)) 
    cf.seek(0)              
    sub = []
      
    for row in reader:
        sub.append(row)

  data = np.array(sub)
  
  ivt(data,100)