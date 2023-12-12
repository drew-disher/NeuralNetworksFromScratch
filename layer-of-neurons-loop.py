inputs  = [ 1.00, 2.00, 3.00, 2.50 ]

weights = [[ 0.20, 0.80, -0.50, 1.00 ]
          ,[ 0.50, -0.91, 0.26, -0.50 ]
          ,[ -0.26, -0.27, 0.17, 0.87 ]]

biases = [ 2.00, 3.00, 0.50 ];

# Output of current layer
layer_outputs = []

# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    #   Zerored output of given neuron
    neuron_output = 0
    print(neuron_weights)
    print(neuron_bias)
    #   For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by the associated weight
        # and add to the neuron's output variable
        neuron_output += n_input*weight
    # Add bias
    neuron_output += neuron_bias
    # Put neuron's result to the layer's output list
    layer_outputs.append(neuron_output)

print(layer_outputs)
