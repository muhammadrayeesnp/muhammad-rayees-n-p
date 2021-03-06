f=open("input3.txt","r")
n=0
d={}
f=list(f)
line=f[0]
min=99999
minindex=0
output=""

for word in line.split():
            if word.isnumeric():
                n=int(word)
                
for line in f[3:]:
        if ":" in line:
            l=line.split(':')
            d[l[0]]=int(l[1])
            
d={k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
prices=[v for k,v in d.items()]

for i in range(len(prices)-n):
    if(prices[i+n-1]-prices[i]<min):
        min=prices[i+n-1]-prices[i]
        minindex=i
        
prices=prices[minindex:minindex+n]
output+="The goodies selected for distribution are:\n\n"
for k,v in d.items():
    if(v in prices):
        output+=k+":"+str(v)+"\n"
        
output+="\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(min)
f=open("output3.txt","w")
f.write(output)
print(output)
f.close()
