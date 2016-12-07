from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import numpy as np



Y, X = np.mgrid[-6:6:15j, -6:6:15j]
U = X-Y
V = X**2-4
speed = np.sqrt(U**2 + V**2)
UN = U/speed
VN = V/speed




plot1 = plt.figure()
plt.quiver(X, Y, UN, VN,        # data
           U,                   # colour the arrows based on this array
           cmap=cm.seismic,     # colour map
           headlength=7)        # length of the arrows

plt.colorbar()                  # adds the colour bar

plt.title('Quive Plot, Dynamic Colours')
plt.show(plot1)                 # display the plot



plot2 = plt.figure()
plt.quiver(X, Y, UN, VN, 
           color='Teal', 
           headlength=7)

plt.title('Quiver Plot, Single Colour')
plt.show(plot2)



plot3 = plt.figure()
plt.streamplot(X, Y, U, V,          # data
               color=speed,         # array that determines the colour
               cmap=cm.cool,        # colour map
               linewidth=2,         # line thickness
               arrowstyle='->',     # arrow style
               arrowsize=1.5)       # arrow size

plt.colorbar()                      # add colour bar on the right

plt.title('Stream Plot, Dynamic Colour')
plt.show(plot3)                     # display the plot



plot4 = plt.figure()
lw = 5*speed/speed.max()            # line width proportional to speed

plt.streamplot(X, Y, U, V,          # data
               density=[0.5, 1],
               color='DarkRed', 
               linewidth=lw)

plt.title('Stream Plot, Dynamic Line Width')
plt.show(plot4)

