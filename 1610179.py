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
    # Set time
    t = time.time()
    # read input

    file = open(file_input,'r')
    line1 = file.readline()
    readN = True
    N =''
    K =''
    for i in line1:
        if (i >= '0') & (i <='9'):
            if readN == True:
                N += i
            else:
                K += i
        else:
            readN = False
    N = int(N)
    K = int(K)
    
    # Init score 
    
    for i in range(N):
        line = file.readline()
        Score.append(int(line))
    file.close()
    
    # Ma trận chứa trạng thái tối ưu cuối cùng
    ResultMatrix = []
    # Giá trị hàm lượng giá của ma trận ResultMatrix
    FinalResult = -1
    # Init Result Matrix
    for i in range(N):
        L=[]
        for j in range(N):
            L.append(0)
        ResultMatrix.append(L)
    
    # init Matrix state
    for i in range(N):
        L=[]
        for j in range(N):
            L.append(0)
        MatrixState.append(L)
    """
     Ta sinh ra 10 trạng thái ban đầu bằng cách  tạo ra ngẫu nhiên 10 đồ thị đều bậc k ( regular graph).
     Cứ mỗi trạng thái ban đầu được tạo ra, ta sẽ tìm ra trạng thái con tốt nhất trong tập trạng thái con được sinh ra, sau đó nhảy đến trạng thái đó.
     Vì sử dụng giải thuật leo đồi như trên nên tỷ lệ rơi vào trường hợp tối ưu cục bộ, đồng bằng, rìa đồi là dễ xảy ra.
     => Tạo ra 10 trạng thái ban đầu để làm giảm tỷ lệ các trường hợp đó, tìm được cái tốt nhất trong những cái cục bộ. Nếu may mắn, đó có thể là trạng thái tối ưu nhất.
    """
    # Biến count thể hiện số lần tạo ra trạng thái ban đầu. count <= 10
    count = 1
    
    
    while (count <= 10):
        # Khởi tạo lại Matrix State với MatrixState[i][j] = 0
        for i in range(N):
            for j in range(N):
                MatrixState[i][j] = 0
        # Sinh ra 1 đồ thị đều bậc K, N đỉnh 
        graph = nx.random_regular_graph(K,N, seed=None)
        
        # Tạo MatrixState
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
                
        if FinalResult == -1 or FinalResult > max - min:
            FinalResult = max - min
            for i in range(0,N):
                for j in range(0,N):
                    ResultMatrix[i][j] = MatrixState[i][j]
        count += 1
            
             
    string = ""
    fileout = open(file_output,'w')
    for i in range(0,N):
        for j in range(0,N):
            if i != j and ResultMatrix[i][j]== 1:
                string += str(j+1) + '\n'
    fileout.write(string)
    fileout.close()
    print("Result: ",FinalResult)
    print("Time: ", time.time()- t)
    print(ResultMatrix)
    return


main('input.txt', 'output.txt')


