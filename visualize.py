import final1

#print final1.avg
#for i in range(12):
#    print "Length of cluster " + str(i) + " is " + str(len(final1.clusters[i]))
import matplotlib.pyplot as plt
import numpy as np

color1 = ['red','black','blue','yellow','green','red','purple','black','blue','yellow','green','purple']

x = np.linspace(0, 1, 10)
for i in range(0, 12):
    print "value of " + str(i) " is " + str(len(final1.clusters[i]))
    for j in range(0,len(final1.clusters[i])):
        plt.scatter(final1.clusters[i][j][1],final1.clusters[i][j][2], color = color1[i])
    #plt.scatter(i, i+1, color='blue')
#plt.legend(loc='best')
plt.show()
