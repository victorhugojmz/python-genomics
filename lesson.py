#managing strings
#coding=utf-
dna = "gtaccccccctagata"
print(dna[0])
print(dna[-3])
print(dna[0:8])
print(dna[:8])
print(dna[6:])
print(dna[3:len(dna)])
num = dna.count('c')
print(num)
dna_u = dna.upper()
print(dna_u)
pos = dna.find('ta')
print(pos)
pos2 = dna.find('ta',3)
print(pos2)
pos3 = dna.rfind('ta')
print(pos3)
string = "LOLhhhhhh"
bolstr = string.islower()
print(bolstr)
newstr = dna.replace('g','G')
print(newstr) 
print(dna)
dna = 'acgtcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'
numc  = dna.count('c')
dnastring = raw_input("Insert dna string")
#it counts the number of characters in one string
nuc = dnastring.count('c')
nug = dnastring.count('g')
#len()takes the lenght of a string (int)
lenght_dna =  len(dnastring)
percent = (nuc+nug)*100.0/lenght_dna
print(str(percent) +'%')
chr(65)
list_ = ['Victor', 2230,'gtctctctctcgacccaattatagatatgaga',5.16e-08]
for _ in list_: 
    print (_)
print(list_[0])#prints the first element of list_
#Slice an element inside an object in pos -3
posminusthree = list_[-3:]
print(posminusthree)
allelements = list_[:]
print(allelements)
#this will clean all elements in list_
list_[:] = [ ]
print(list_)
#concatenation between lists 
list_two = list_+['POS',20,1996]
print(list_two)
sliced_list = list_two[0:2]
print(sliced_list)
sliced_list = list_two[0:len(list_two)]
del(list_two[1])
print(list_two)
#Counting number of times  pos string inside list  
elemwithpos = list_two.count('POS')
print(elemwithpos)
l = [0,'One',2,'three',4,'five']
#The method reverse reverses all elements in the list 
l.reverse()
print(l)
#List as Stacks
stack = ['a','b','c','z','g']
stack.append('s')
last = stack.pop()
print(last)
#Sorting list samples
s  = sorted(stack)
print(s)
stack.sort()#sort method modifies the list
print(stack)
#Tuples son una estructura de datos como strings y listas
t = 1,2,3
type(t)
print(t)

