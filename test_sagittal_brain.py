import numpy as np
import subprocess

input = np.zeros((20, 20))
input[-1, :] = 1

expected = np.zeros(20)
expected[-1] = 1

np.savetxt("brain_sample.csv", input, fmt='%d', delimiter=',')

subprocess.run(["python", "sagittal_brain.py"])

output = np.loadtxt("brain_average.csv",delimiter = ',')

assert (output == expected).all()