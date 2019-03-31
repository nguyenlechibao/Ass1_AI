from itertools import combinations 
import time
MatrixState =[]
Score =[]
Count=[]
Result =[-1]
ResultMatrix =[]
def ScoreMatrix():
    sum =0
    for j in range(len(MatrixState)):
        if MatrixState[0][j]==1:
            sum += Score[j]
    max = min = sum    
    for i in range(1,len(MatrixState)):
        sum = 0
        for j in range(len(MatrixState)):
            if MatrixState[i][j]==1:
                sum += Score[j]
        if sum > max:
            max = sum
        if sum < min:
            min = sum
    return max - min
def Check(N,K):
    for i in range(0,N):
        if Count[i] < K:
            return False
    return True

def COPY(ResultMatrix, MatrixState):
    for i in range(0,len(MatrixState)):
        for j in range(0,len(MatrixState)):
            ResultMatrix[i][j] = MatrixState[i][j]
    return 
    
def DFS( vertex,N,K,file_output):

    global ResultMatrix
    set =[] 
    for i in range(N):
        if vertex != i and Count[i] < K and MatrixState[vertex][i] == 0:
            set.append(i)
    if set ==[]:
        if Check(N,K) is True:
            score = ScoreMatrix()
            if Result[0] == -1:
                Result[0] = score
                COPY(ResultMatrix,MatrixState)
            elif Result[0] > score:
                Result[0] = score
                COPY(ResultMatrix,MatrixState)
        return
        
    comb = combinations( set, K - Count[vertex])
    OldCount = Count[vertex]
    for i in list(comb):
        Lcomb = list(i)
        Count[vertex]= K
        for x in Lcomb:
            Count[x] += 1
            MatrixState[vertex][x] = MatrixState[x][vertex] = 1
        for x in Lcomb:
            DFS(x,N,K,file_output)
        for x in Lcomb:
            Count[x] -= 1
            MatrixState[vertex][x] = MatrixState[x][vertex] = 0
        Count[vertex] = OldCount


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
        Count.append(0)
    

    for i in range(N):
        L =[]
        for j in range(N):
            L.append(0)
        MatrixState.append(L)
        
    for i in range(N):
        L =[]
        for j in range(N):
            L.append(0)
        ResultMatrix.append(L)
    
    DFS(1,N,K,file_output)
    writeFile(file_output)
    print("Result: ",Result[0])
    print("Time: ", time.time() - t)
    print(ResultMatrix)
    return


main('input.txt', 'output.txt')

