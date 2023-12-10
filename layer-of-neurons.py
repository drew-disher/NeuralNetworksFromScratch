inputs  = [ 1.00, 2.00, 3.00, 2.50 ]

weights1 = [ 0.20, 0.80, -0.50, 1.00 ]
weights2 = [ 0.50, -0.91, 0.26, -0.50 ]
weights3 = [ -0.26, -0.27, 0.17, 0.87 ]

bias1 = 2.00
bias2 = 3.00
bias3 = 0.50

outputs = [
    #Neuron 1:        
        inputs[ 0 ] * weights1[ 0 ] 
    +   inputs[ 1 ] * weights1[ 1 ] 
    +   inputs[ 2 ] * weights1[ 2 ] 
    +   inputs[ 3 ] * weights1[ 3 ] 
    +   bias1

    #Neuron 2:        
    ,   inputs[ 0 ] * weights2[ 0 ] 
    +   inputs[ 1 ] * weights2[ 1 ] 
    +   inputs[ 2 ] * weights2[ 2 ] 
    +   inputs[ 3 ] * weights2[ 3 ] 
    +   bias2

    #Neuron 3:        
    ,   inputs[ 0 ] * weights3[ 0 ] 
    +   inputs[ 1 ] * weights3[ 1 ] 
    +   inputs[ 2 ] * weights3[ 2 ] 
    +   inputs[ 3 ] * weights3[ 3 ] 
    +   bias3
]

print(outputs)
