import numpy as np

inputs  = [ 1.00, 2.00, 3.00, 2.50 ]

weights = [[  0.20,  0.80, -0.50,  1.00 ]
          ,[  0.50, -0.91,  0.26, -0.50 ]
          ,[ -0.26, -0.27,  0.17,  0.87 ]]

biases = [ 2.00, 3.00, 0.50 ]

layer_outputs = np.dot(weights, inputs) + biases

print(layer_outputs);
