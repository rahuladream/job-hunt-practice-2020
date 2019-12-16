"""
INPUT
5 2
1 0 1 1 0
1 2
0 1 4

<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=def%20binaryQueries%28%29%3A%0A%20%20%20%20n,%20q%20%3D%20map%28int,%20input%28%29.split%28%29%29%0A%20%20%20%20l%20%3D%20input%28%29.split%28%29%0A%20%20%20%20for%20i%20in%20range%280,q%29%3A%0A%20%20%20%20%20%20%20%20k%20%3D%20input%28%29.split%28%29%0A%20%20%20%20%20%20%20%20if%20k%5B0%5D%20%3D%3D%20'0'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20l%5Bint%28k%5B2%5D%29-1%5D%20%3D%3D%20'1'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22ODD%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22EVEN%22%29%0A%20%20%20%20%20%20%20%20if%20k%5B1%5D%20%3D%3D%20'1'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20l%5Bint%28k%5B1%5D%29%20-%201%5D%20%3D%3D%20'0'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l%5Bint%28k%5B1%5D%29%20-%201%5D%20%3D%20'1'%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20'0'%0A%0Aif%20__name__%20%3D%3D%20'__main__'%3A%0A%20%20%20%20binaryQueries%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=19&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%225%202%22,%221%200%201%201%200%22,%221%202%22,%220%201%204%22%5D&textReferences=false"> </iframe>

OUTPUT 
ODD
"""

def binaryQueries():
    n, q = map(int, input().split())
    l = input().split()
    for i in range(0,q):
        k = input().split()
        if k[0] == '0':
            if l[int(k[2])-1] == '1':
                print("ODD")
            else:
                print("EVEN")
        if k[1] == '1':
            if l[int(k[1]) - 1] == '0':
                l[int(k[1]) - 1] = '1'
            else:
                '0'

if __name__ == '__main__':
    binaryQueries()