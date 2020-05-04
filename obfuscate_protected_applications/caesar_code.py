import string
x=str
B=None
G=open
e=tuple
K=len
m=int
q=True
A=input
s=print
h=string.ascii_lowercase
def T(Y:x)->x:
 X=B
 with G(Y,'r')as rf:
  X=rf.read()
 return X
def I(Y:x,X:x)->B:
 with G(Y,'w')as wf:
  wf.write(X)
def F(S:x)->e:
 W=h
 k='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
 if S in W or S in k:
  j=W if S in W else k
  return(j,K(j))
 else:
  return(B,B)
def P(X:x,d:m,f:m)->x:
 w=[]
 for S in X:
  l,N=F(S.lower())
  if l is B:
   w.append(S)
   continue
  if f:
   E=(l.find(S.lower())-d+N)%N
  else:
   E=(l.find(S.lower())+d)%N
  H=l[E]
  w.append(H if S.islower()else H.upper())
 return "".join(w)
def c():
 while q:
  Y=A("Enter filepath: ")
  d=A("Enter key: ")
  f=A("Enter mode:\n 0 - encrypt\n 1 - decrypt\n")
  if d.isdigit()and f.isdigit():
   try:
    X=T(Y)
    w=P(X,m(d),m(f))
    i=Y+"_mod_by_caesar"
    I(i,w)
    s("Check file")
   except FileNotFoundError:
    s("File not found")
  else:
   s("The key or mode must be a number!")
if __name__=="__main__":
 c()
