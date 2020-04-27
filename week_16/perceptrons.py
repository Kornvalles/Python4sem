import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import my_perceptron as pc


def activation_function(x):
    """
    Step function to respond with y = 1 or -1
    Parameter:
    x: An x (numeric) value that will have a corresponding y value of 1 or -1
    """
    if x < 0:
        return -0.25
    else:
        return 0.25
    
rnge = np.linspace(-5.5, 5.0, num=1000)
print(rnge[0:5])
values = [activation_function(i) for i in rnge]
plt.plot(rnge, values)
plt.axis([-10, 9, -2, 2])
plt.show()

def perceptron(inp, weights):
    """
    Given a list of input (x) values and a list of weights, 
    calculates the dot product of the 2 lists and returns 1 or -1 (fire or don't)
    Parameters:
    inp: vector of input predictors
    weights: vector of weights to be ajusted for precise prediction of output.
    """
    # This is the same as the dot product np.dot(i, w)
    # dot_product = sum([i * w for i, w in zip(inp, weights)])
    dot_product = np.dot(inp,weights)
    output = activation_function(dot_product)
    return output

print(perceptron([1, 2, 3, 4, 5], [1, 1, 2, 1, 1]))

"""
Part two: rodent data
1. Make a new scatter plot with datapoints of weights vs heights. Choose different colors for rats and mice
2. Manually find the optimal linear function to divide the 2 groups (y = aX+b). Plot it on the scatter plot
3. What is the slope and intercept of the linear function?
4. Now change the 'type' column to represent rats as 1 and mice as -1
5. Clean up any rows with null data
6. Use these weights herè [40,-190] to determine if the following 3 animals are mice or rats:

    [[231.32446731816555,26.03382997978225],
    [17.906954059999567,6.846576762459397],
    [230.276522831171,24.077799766119398]]

7. Find the (approximately) optimal weights using the perceptron learning algorithm
8. Plot the weightline
9. Plot the division line"""

rodents = pd.read_csv('./rodents.csv',sep=';',keep_default_na='true')
rodents = rodents[pd.notnull(rodents['weight'])]
rodents = rodents[pd.notnull(rodents['height'])]
rodents.dropna()
rodents['type'] = rodents['type'].apply(lambda x: 1 if str(x).strip() == 'rat' else -1)

rodents_np = rodents.to_numpy()
#print(rodents_np)
rodents_fmt = [(data[:2],data[2]) for data in rodents_np]
#print(rodents_fmt['type'])
weights,_ = pc.pla(rodents_fmt)
print(weights)