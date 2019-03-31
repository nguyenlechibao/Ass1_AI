import random
def main(output_file):
    file = open(output_file,'w')
    N = -1
    K = -1
    while (True):
        K = random.randint(2,20)
        N = random.randint(K+1,21)
        if K*N % 2 != 0 :
            continue
        else:
            break
    String = str(N) +" " + str(K)+'\n'
    for i in range(0,N):
        String += str(random.randint(1,10000)) + '\n'
    
    file.write(String)
    file.close()
                   
main('input.txt')
    

