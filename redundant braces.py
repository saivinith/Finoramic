class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        a=[]
        for i in A:
            if (i!=')'):
                if(i!=' '):
                    a.append(i)
            else:
                i=0
                l=len(a)
                j=a.pop(l-1)
                l=l-1
                while (j!='('):
                    i=i+1
                    j=a.pop(l-1)
                    l=l-1

                if(i<=1):
                    return 1
        return 0
            
