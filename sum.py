class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
	    r=100**100
	    sum1=0
	    A.sort()
	    l=len(A)
	    for i in range(0,l-1):
	        j=i+1
	        k=len(A)-1
	        while(j<k):
	            s=A[i]+A[j]+A[k]
	            d=abs(s-B)
	            if(d==0):
	                return s
	            if(d<r):
	                r=d
	                sum1=s
	            if(s<=B):
	                j=j+1
	            elif(s>B):
	                k=k-1
	    return sum1 
	                
	    
