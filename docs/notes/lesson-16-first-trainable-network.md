1. Why does X have shape (5,1) instead of (5,) ?

We wanted to the data to be explicitly represented as 5 examples 1 feature.

2. Why is: W1 = (1,4) ?

It means 1 input passed to 4 neurons.

3. Why does: X @ W1 produce (5,4)?

X with shape (5,1) @ W with shape (1,4) where @ is Matrix multiplication which produces (5,4) shaped output. 

4. Why do we need ReLU between the two linear layers?

Because Multiple Linear Transformations collapse into another linear transformation.

5. Derive:

dL/dprediction

for:

L = mean((prediction-y)²)

dL/dprediction = 2(prediction-y) / N

6. Explain this: dW2 = A1.T @ dZ2 in plain English.

This has arrived when we want to know the change in the Loss with respect to dW2.

7. Why does gradient descent subtract the gradient?

Because Subtraction is the best possible operation to get the minimum loss.

8. What would happen if we used an extremely large learning rate?

When we use extremely large learning rate we jump over the best possible solution.

9. What would happen if the learning rate were extremely small?

If the learning rate is extremely small then it is possible that we will never reach the best solution.

10. Explain the entire training loop without using the words "AI learns".

First we initialized the parameters.
Random Initialization of Weights.
Then we have did the Forward Pass.
Then we calculate the loss.
Then we calculate the Gradients and forward it backwards called Backpropagation.
Then we update the Parameters - Weights and Bias.
