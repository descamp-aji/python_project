priority = 0

#netacad email
email='descampwarnaaji@gmail.com'

#Graded
def isPointInCircle(x,y,r,center=(0,0)):
  titik_uji = ((x-center[0])**2 + ((y-center[1])**2))
  if  titik_uji <= r**2 :
    return True
  else : 
    return False
  pass

#CEK OUTPUT KODE ANDA
print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),
      isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))

#Graded
import random
def generateRandomSquarePoints(n,length,center=(0,0)):
  minx = center[0]-length/2
  maxx = center[0]+length/2
  miny = center[1]-length/2
  maxy = center[1]+length/2
  point = list([(random.uniform(minx,maxx)),(random.uniform(miny,maxy))] for i in range(n))
  return point

#CEK OUTPUT KODE ANDA
random.seed(0)
titik = generateRandomSquarePoints(100,1)
print(titik[10:15])

#Graded
def MCCircleArea(r,n=100,center=(0,0)):
  titik_true = 0
  list_titik = generateRandomSquarePoints(n,(r*2))
  for elem in range(len(list_titik)) :
    titik_uji = isPointInCircle(list_titik[elem][0],list_titik[elem][1],r)
    if titik_uji == True :
      titik_true += 1
  
  Luas_lingkaran = titik_true/len(list_titik)*((2*r)**2)
  return Luas_lingkaran
  pass

#CEK OUTPUT KODE ANDA
random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))

#graded
def LLNPiMC(nsim,nsample):
  totalLuas_lingkaran = 0
  for i in range(nsim) :
    luas_lingkaran = MCCircleArea(1,nsample)
    totalLuas_lingkaran += luas_lingkaran
  mean_luas_lingkaran = totalLuas_lingkaran/nsim
  return mean_luas_lingkaran
  pass

#CEK OUTPUT KODE ANDA
import math
random.seed(0)
estpi = LLNPiMC(10000,500)
print('est_pi:',estpi)
print('act_pi:',math.pi)

# Graded
def relativeError(act,est):
  relatif_error = abs((est-act)/act)*100
  return relatif_error
  pass
#CEK OUTPUT KODE ANDA
print('error relatif:',relativeError(math.pi,estpi),'%')