
from networkx import nx
import time
MatrixState =[]
Score =[]

def ProcessScore():
   
   sum =0
   for j in range(len(MatrixState)):
       if MatrixState[0][j]==1:
           sum += Score[j]
   max = min = sum  
   tbmaxp = tbminp= 0   
   for i in range(1,len(MatrixState)):
       sum = 0
       for j in range(len(MatrixState)):
           if MatrixState[i][j]==1:
               sum += Score[j]
       if sum > max:
           max = sum
           tbmaxp = i
       if sum < min:
           min = sum
           tbminp = i
   return max,tbmaxp, min, tbminp

def Process(tbmaxp,tbminp):
   set1=[]
   set2=[]
   for i in range(len(MatrixState)):
       if MatrixState[tbmaxp][i] == 1 and MatrixState[tbminp][i] == 0 and tbminp != i:
           set1.append(i)
   for i in range(len(MatrixState)):
       if MatrixState[tbminp][i] == 1 and MatrixState[tbmaxp][i] == 0 and tbmaxp != i:
           set2.append(i)
   return set1,set2
   
def SwapMatrix(tbmaxp, tbminp, swmax,swmin):
   MatrixState[tbmaxp][swmax] = MatrixState[swmax][tbmaxp] = 0
   MatrixState[tbminp][swmin] = MatrixState[swmin][tbminp] = 0
   MatrixState[tbmaxp][swmin] = MatrixState[swmin][tbmaxp] = 1
   MatrixState[tbminp][swmax] = MatrixState[swmax][tbminp] = 1

def RestoreMatrix(tbmaxp, tbminp, swmax,swmin):
   MatrixState[tbmaxp][swmax] = MatrixState[swmax][tbmaxp] = 1
   MatrixState[tbminp][swmin] = MatrixState[swmin][tbminp] = 1
   MatrixState[tbmaxp][swmin] = MatrixState[swmin][tbmaxp] = 0
   MatrixState[tbminp][swmax] = MatrixState[swmax][tbminp] = 0

def writeFile(file_output):
   string = ""
   fileout = open(file_output,'w')
   for i in range(0,len(ResultMatrix)):
       for j in range(0,len(ResultMatrix)):
           if i != j and ResultMatrix[i][j]== 1:
               string += str(j+1) + '\n'
   fileout.write(string)
   fileout.close()
def main(file_input, file_output):
   # read input
   t = time.time()
   file = open(file_input,'r')
   line1 = file.readline()
   readN = False
   N =''
   K =''
   for i in line1:
       if (i >= '0') & (i <='9'):
           if readN == False:
               N += i
           else:
               K += i
       else:
           readN = True
   N = int(N)
   K = int(K)
   # Init score 
   
   for i in range(N):
       line = file.readline()
       Score.append(int(line))
   file.close()
   
   # init state
   
   for i in range(N):
       L=[]
       for j in range(N):
           L.append(0)
       MatrixState.append(L)

   graph = nx.random_regular_graph(K,N, seed=None)
   
   for i in range(N):
       for j in graph[i]:
           MatrixState[i][j]= MatrixState[j][i]= 1
   max,tbmaxp,min,tbminp = ProcessScore()
   while(True):
       result = max - min
       set =[-1,-1]
       setmax,setmin = Process(tbmaxp,tbminp)
       for i in setmax:
           for j in setmin:
               SwapMatrix(tbmaxp, tbminp, i,j)
               max1,tbmaxp1,min1,tbminp1 = ProcessScore()
               if max1-min1 < result:
                   result= max1-min1
                   set[0] = i
                   set[1] = j
               RestoreMatrix(tbmaxp, tbminp, i,j)
       
       if result == max - min:
           break
       else:
           SwapMatrix(tbmaxp, tbminp, set[0],set[1])
           max,tbmaxp,min,tbminp = ProcessScore()
               
  
   string = ""
   fileout = open(file_output,'w')
   for i in range(0,len(MatrixState)):
       for j in range(0,len(MatrixState)):
           if i != j and MatrixState[i][j]== 1:
               string += str(j+1) + '\n'
   fileout.write(string)
   fileout.close()
   print('Result: ',max- min)
   print('Time: ',time.time()  - t)
   print(MatrixState)
   return


main('input.txt', 'output1.txt')



