from collections import OrderedDict
import numpy as np

class maximize:
    def _init_(self):
        pass
    def do(self, x_vars, top, left, matrix, maxim):
        while True:
            #check end condition
            minimum=min(matrix[len(matrix)-1])
            for i in range(len(matrix)-1):
                if matrix[len(matrix)-1][i]<=minimum:
                    minimum=matrix[len(matrix)-1][i]
            if minimum>=0:
                break
            #pick most negative
            c=matrix[len(matrix)-1].index(minimum) #pivot col
            
            hence=0
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if j==c:
                        if matrix[i][j]>0:
                            hence=matrix[i][j]
            if hence<=0:
                return False
                
            
            arr=[-1]*(len(matrix)-1)
            for i in range(len(matrix)-1):
                if matrix[i][c]>0:
                    arr[i]=matrix[i][len(matrix[i])-1]/matrix[i][c]


            r=0 #pivot row
            for i in range(len(arr)):
                if arr[i]>=0:
                    r=i
            for i in range(len(arr)):
                if arr[i]<=arr[r]:
                    if arr[i]>=0:
                        r=i
            

            temp=matrix[r][c]
            if matrix[r][c]!=1:
                for i in range(len(matrix[r])):
                    matrix[r][i]=matrix[r][i]/temp
                    
            if matrix[r][c]==0:
                for i in range(len(matrix[r])):
                    matrix[r][i]=matrix[r][i]+1

            for i in range(len(matrix)):
                x=-1*matrix[i][c]
                if matrix[i][c]!=0 and i!=r:
                    for j in range(len(matrix[i])):            
                        matrix[i][j]=matrix[i][j]+(x*matrix[r][j])

            #swaps label variables in column/row
            if 'x' in top[c]:
                left[r]=top[c]

        d={}
        for i in range(len(left)):
            if 'x' in left[i]:
                d[i]=left[i]

        dd = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

        temp=1
        i=1
        ddd=[]
        dim=0
        for key in dd:

            if i==1 and temp-int(dd[key][1:])< 0:
                ddd.append('x'+str(i))
                temp=int(dd[key][1:])
            if int(dd[key][1:])-temp >1:
                ddd.append('x'+str(i))
                temp=int(dd[key][1:])
                i+=1
            if int(dd[key][1:])-temp <=1:
                temp=int(dd[key][1:])
                i+=1

        while x_vars!=temp:
            ddd.append('x'+str(temp+1))
            dim+=1
            temp+=1

        if dim>1:
            for x in ddd:
                dd.update({'zero' : x})
        elif dim==1:
            dd.update({'zero':ddd[0]})
        
        
        for x in ddd:
            dd.update({'zero' : x})
        
        dd2 = OrderedDict(sorted(dd.items(), key=lambda x: x[1]))
        
        result=[]
        
        for key in dd2:
            if key=='zero':
                #print(dd2[key],' = 0')
                result.append(dd2[key]+' = 0')
            else:
                result.append(dd2[key]+' = '+'{:f}'.format(matrix[key][len(matrix[key])-1]))
                #print(dd2[key],' = ','{:.4f}'.format(matrix[key][len(matrix[key])-1]))
        result.append('Z(x) = '+'{:f}'.format(float(matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1])))
        #print('Z(x) = ', end='')
        #print('{:.4f}'.format(float(matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1])))
        if maxim==True:
            return result
        else:
            return matrix[len(matrix)-1]
        #method takes x_vars, top, left, matrix
        