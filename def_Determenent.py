import numpy as np

def myDet(A):
    det = 0 #결과값
    global n,m
    i = len(A) #행렬의 길이(크기)
    j = len(A) 
                
    #2x2일 때 ad-bc
    if i == 2: 
        det = A[0][0]*A[1][1] - A[1][0]*A[0][1]

    else :
        #0의 위치 찾기
        for i in range(1,i+1):
            for j in range(1,j+1):
                if (A[i-1][j-1] == 0):
                    n = i
                    m = j

                
        for row in range(len(A)):

            #원소 추출
            a = A[n][row]
 
            #소행렬식 추출
            sub = np.delete(A,n,axis=0)
            sub = np.delete(sub,row,axis=1)

            #재귀함수
            mD = myDet(sub) 

            C = (-1)**(row)

            #부호 설정
            det += a*C*mD

    return det
    
    
A = np.array([[1,0,-3,4],[2,-2,2,2],[-3,2,3,4],[4,2,4,-4]])
print("myDet(A) = ", myDet(A))
print("np.linalg.det(A) = ", np.linalg.det(A))
