1. Define:

i. scalar - A single number or a 0-dimensional tensor.
ii. vector - It is a 1-dimensional tensor.
iii. matrix - It is a 2-dimensional tensor.
iv. tensor - A structure capable of representing any type of shape of numbers.

2. Explain

i. (3,) - It is a vector with 3 values.
ii. (4,3) - It is a matrix with 4 rows and 3 cols.
iii. (32,224,224,3) - It is a tensor with 4 axes.
iv. (4,128,768) - It is a tensor with 3 axes.

in plain English.

3. Explain

Why:

(4,3) @ (3,2)

produces:

(4,2) Because each of the 4 rows of W interacts with the 2 cols of x.

4. Explain

Why broadcasting allows:

(4,2) + (2,) because if anything is missin it adds imaginary 2 (here) to perform the operation smoothly.

5. Answer these

Q1. Is every matrix a tensor?

Yes every matrix is tensor.

Q2. Is every tensor a matrix?

No every tensor is not a matrix.

Q3. What does the batch dimension represent?

Batch dimension represents the batch meaning how many numbers or any vectors are passed in a batch.

Q4. Why do neural networks need tensors?

Neural networks need tensor because a neural network can be a n-dimensional structure and to represent this n-dimensional structure tensor is only used.

Q5. What does shape (4,128,768) mean in a language model?

It means 4 sequences, 128 tokens and 768 features per token.