from string import ascii_lowercase
L=str
D=None
G=open
X=list
O=len
Q=tuple
I=bool
B=set
J=True
S=False
q=int
M=input
K=KeyError
o=print
def j(w:L)->L:
 a=D
 with G(w,'r')as rf:
  a=rf.read()
 return a
def E(w:L,a:L)->D:
 with G(w,'w')as wf:
  wf.write(a)
def F(e:L,a:L)->L:
 v=X(e)
 while O(v)<O(a):
  v.extend(e)
 return "".join(v)[:O(a)+1]
def z(p:L)->Q:
 d=ascii_lowercase
 C='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
 if p in d or p in C:
  R=d if p in d else C
  return(R,O(R))
 else:
  return(D,D)
def s(e:L)->I:
 C='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
 if not O(B(e.lower())-B(ascii_lowercase)):
  return J
 elif not O(B(e.lower())-B(C)):
  return J
 else:
  return S
def r(a:L,e:L,l:q)->L:
 H=[]
 i=0
 for p in a:
  A,k=z(p.lower())
  if A is D:
   H.append(p)
   continue
  kv=A.find(e[i].lower())
  if l:
   N=(A.find(p.lower())-kv+k)%k
  else:
   N=(A.find(p.lower())+kv)%k
  u=A[N]
  H.append(u if p.islower()else u.upper())
  i+=1
 return "".join(H)
def V():
 while J:
  w=M("Enter filepath: ")
  e=M("Enter key: ")
  l=M("Enter mode:\n 0 - encrypt\n 1 - decrypt\n")
  if l.isdigit():
   try:
    if not s(e):
     raise K
    a=j(w)
    e=F(e,a)
    H=r(a,e,q(l))
    g=w+"_mod_by_vigenere"
    E(g,H)
    o("Check file")
   except FileNotFoundError:
    o("File not found")
   except K:
    o("The key is not only letters")
  else:
   o("The mode must be a number!")
if __name__=="__main__":
 V()
