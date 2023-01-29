t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    z=a*b
    if(z>=c):
      a=c//b
      k=b*a 
      x=c-k
      op=(a*b*b)+x*x
      print(op)
    else:
        print(a*b*b)
