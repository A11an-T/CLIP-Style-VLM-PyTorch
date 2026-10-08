

Weekend 1 (Oct 10-11): Python basics. Cover variables, if/else, loops, functions, lists, and dicts. The free book "Automate the Boring Stuff with Python" is a good single source. Read its first five chapters, and don't start a second resource.
Done when: you can write a function that takes a list of numbers and returns the average and the largest value without using Python's built-in max, and a second function that counts how often each word appears in a sentence using a dict.
Minimum: the average function.

Weekend 2 (Oct 17-18): PID class, part A. Write the class and print its output over a few steps.

Weekend 3 (Oct 24-25): PID class, part B. Simulate a simple system and plot it with matplotlib

Weekend 4 (Oct 30-31): NumPy 
Task: Redo the simulation with arrays, testing 500 or more gain combinations in one pass with no loop over combinations. Pick the best one by error.
Done when: you can predict the shape of every array before you run the code.
Minimum: broadcasting and reshape exercises only.

Weekend 5 (Nov 7-8): Autograd
Task: Derive the gradient of a simple function by hand and check it against PyTorch's autograd. Then fit a line with gradient descent, first manually, then with torch.
Done when: your hand gradient matches autograd, and both fits land on the same line.
Minimum: the gradient check only.

Weekend 6 (Nov 10 -Nov 11): MNIST loop
Task: Train an MNIST classifier with your own training loop. Don't use a high-level trainer.
Done when: test accuracy is roughly 97%, and you can explain what zero_grad, backward and step each do. [Likely]
Minimum: a loop that runs, even at lower accuracy.

Weekend 7 (Nov 24-25): Contrastive loss, your first CLIP piece
Task: Write the symmetric contrastive loss with a temperature parameter, and test it on random embeddings.
Done when: the loss on random embeddings with batch size N comes out near ln N, and much lower on aligned embeddings. [Certain for the ln N result]
Minimum: write the loss without the tests.

Soft Deadline before January 1st (midterms) 
Hard Dead line before Febuary 28th
