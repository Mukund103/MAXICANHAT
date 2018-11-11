import matplotlib.pyplot as py
r1=1
r2=2
w1=0.6
w2=-0.4
epoch_max=15
x_max=4
s=[0,0.5,0.8,1.0,0.8,0.5,0]
epoch=1
x_old=s
x_in=[0]*len(x_old)
x=[1,2,3,4,5,6,7]
py.plot(x,s)
while(epoch<=epoch_max):
    #step3 (compute net i/p to a node)
    for i in range(len(x_old)):
            a=[x_old[j] for j in range(i-r1,i+r1+1) if j>=0 and j<len(x_old)]
            b=[x_old[j] for j in range(i+r1+1,i+r2+1) if j<len(x_old)]
            c=[x_old[j] for j in range(i-r1-1,i-r1-r2,-1) if j>=0 and j<len(x_old)]
            x_in[i]=w1*sum(a)+w2*sum(b)+w2*sum(c)
    #step 4 (apply activation function )
    for i in range(len(x_old)):
            x_in[i]=min(max(0,x_in[i]),x_max)
            #step 5(update x_old)
            x_old[i]=x_in[i]
            py.plot(x,x_old)
    #step 6 (increment epoch)       
    epoch+=1
py.plot(x,x_old)
