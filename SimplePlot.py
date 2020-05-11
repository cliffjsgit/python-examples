# Matplotlib plotting library: https://matplotlib.org/
# Matplotlib User's Guide: https://matplotlib.org/users/index.html
import matplotlib
import matplotlib.pyplot as plt

# https://numpy.org/
# NumPy is the fundamental package for scientific computing with Python
import numpy as np

# Matplotlib is a plotting library. It relies on some backend to actually
# render the plots. The default backend is the agg backend,
# which only renders PNGs. Comment out the next line, to only display the plot.

matplotlib.use("Agg")            # Use Agg backend to only renders PNG files

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("SimplePlot.png")  # Save resulting plot to a png file
# plt.show()                   # Display plot if not in PythonAnywhere

