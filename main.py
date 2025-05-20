import numpy as np
import math
import random
import functions
import package
import matplotlib.pyplot as plt
import matplotlib.cm as cmap

lst_packages = []
lst_computers = functions.lst_computers
delta = functions.delta_generate(functions.distribution_delta(0.1,1))
for i in range(1,10001):
    package1 = package.Package(i)
    lst_packages.append(package1)

for i in lst_packages:
    i.time_of_package(delta)
    i.size_gen()
    i.origin_address()
    i.dest_address()

lst_recived = []
lst_sent = []
lst_sentbytes = []
lst_recbytes = []
for j in range(1,1025):
    pac_rec = 0
    pac_sen = 0
    pacsen_bytes = 0
    pacrec_bytes = 0
    for pack in lst_packages:
        if pack.to_add == j:
            pac_rec = pac_rec+1
            pacrec_bytes = pacrec_bytes+pack.size
    lst_recbytes.append(pacrec_bytes)
    lst_recived.append(pac_rec)
    for pack in lst_packages:
        if pack.from_add == j:
            pac_sen = pac_sen+1
            pacsen_bytes = pacsen_bytes+pack.size
    lst_sentbytes.append(pacsen_bytes)
    lst_sent.append(pac_sen)
time = []
bytes_for_time = []
for i in lst_packages:
    time.append(i.time)
    bytes_for_time.append(i.size)

Heatmap = np.zeros((1024,1024))
for pack in lst_packages:
    Heatmap[pack.to_add-1,pack.from_add-1] = Heatmap[pack.to_add-1,pack.from_add-1] + pack.size


plt.figure(1)
plt.subplot(3,2,1)
plt.plot(lst_computers,lst_sent)
plt.title("section_A")
plt.xlabel("computer address")
plt.ylabel("num of packages")
plt.subplot(3,2,2)
plt.plot(lst_computers,lst_recived)
plt.title("section_B")
plt.xlabel("computer address")
plt.ylabel("num of packages")
plt.subplot(3,2,3)
plt.plot(lst_computers,lst_sentbytes)
plt.title("sectionC")
plt.xlabel("computer address")
plt.ylabel("num of bytes")
plt.subplot(3,2,4)
plt.plot(lst_computers,lst_recbytes)
plt.title("sectionD")
plt.xlabel("computer address")
plt.ylabel("num of bytes")
plt.subplot(3,2,5)
plt.plot(time,bytes_for_time)
plt.title("sectionE")
plt.xlabel("time")
plt.ylabel("num of bytes")
plt.figure(2)
plt.imshow(Heatmap, cmap='hot', interpolation='nearest',vmax = 1000)
plt.colorbar()
plt.show()