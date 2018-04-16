import numpy as np
import matplotlib.pyplot as plt

instances=[0,3,5,6,8]
error=[0,3,4,5,6]
time=[0.25,0.49,0.98,0.87,1.34]


#plt.figure("figa")
plt.figure(1)
# plt.subplot(211)
plt.plot(instances,error,"r*")
plt.plot(instances,error,label="$label_plot$",color="red",linewidth=2)
plt.xlabel("data")
plt.ylabel("label ")
plt.title("a simple plot")
plt.legend()
#plt.show()
#plt.savefig("plot_label.jpg")

#plt.figure("figb")
plt.figure(2)
plt.plot(instances,time,label="$time_plot$",color="red",linewidth=2)
plt.xlabel("data")
plt.ylabel("time")
plt.title("a simple plot")
plt.legend()
plt.show()
#plt.savefig("plot_time.jpg")