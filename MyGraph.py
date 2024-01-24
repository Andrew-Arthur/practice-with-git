import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

# Installing a Library:
# 1) Create a virtual environment (in terminal):
#       py -3 -m venv ~environmentName~
# 2) Activate your VE
#       ~environmentName~\Scripts\activate
# 3) Install 3p library
#       pip3 install ~libraryName~
