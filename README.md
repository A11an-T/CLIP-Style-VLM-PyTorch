# CLIP-Style-VLM-PyTorch

A tiny CLIP-style vision-language model built from scratch in PyTorch: my own image encoder, text encoder and contrastive loss, trained on a small dataset and compared against a pretrained CLIP.

**Budget:** about 3 hours every weekend.
**Soft deadline:** end of winter break (Jan 3): all three pieces (loss, text encoder, image encoder) built and tested.
**Hard deadline:** Feb 28: trained model, evaluated, compared to pretrained CLIP, written up.

Each weekend has a **Task**, a **Done when** check, and a **Minimum** for weekends that go badly. Code for each weekend goes in its own folder (`weekend01/`, `weekend02/`, ...).

---

## Part 1: Foundations (Python → PyTorch)

### Weekend 1 (Oct 10–11): Python basics
Task: Variables, if/else, loops, functions, lists and dicts. Use *Automate the Boring Stuff with Python*, chapters 1–5, and don't start a second resource. Start the exercises first and read only the section you're stuck on.
Done when: you can write a function that takes a list of numbers and returns the average and the largest value without using Python's built-in `max`, and a second function that counts how often each word appears in a sentence using a dict.
Minimum: the average function.

### Weekend 2 (Oct 17–18): PID class, part A
Task: Write the PID class and print its output over a few steps.

### Weekend 3 (Oct 24–25): PID class, part B
Task: Simulate a simple system and plot it with matplotlib.

### Weekend 4 (Oct 31–Nov 1): NumPy
Task: Redo the simulation with arrays, testing 500 or more gain combinations in one pass with no loop over combinations. Pick the best one by error.
Done when: you can predict the shape of every array before you run the code.
Minimum: broadcasting and reshape exercises only.

### Weekend 5 (Nov 7–8): Autograd
Task: Derive the gradient of a simple function by hand and check it against PyTorch's autograd. Then fit a line with gradient descent, first manually, then with torch.
Done when: your hand gradient matches autograd, and both fits land on the same line.
Minimum: the gradient check only.

### Weekend 6 (Nov 14–15): MNIST loop
Task: Train an MNIST classifier with your own training loop. Don't use a high-level trainer.
Done when: test accuracy is roughly 97%, and you can explain what `zero_grad`, `backward` and `step` each do.
Minimum: a loop that runs, even at lower accuracy.

### Weekend 7 (Nov 21–22): Contrastive loss, your first CLIP piece
Task: Write the symmetric contrastive loss with a temperature parameter, and test it on random embeddings.
Done when: the loss on random embeddings with batch size N comes out near ln N, and much lower on aligned embeddings.
Minimum: write the loss without the tests.

---

## Part 2: Build the pieces (CIFAR-10 with template captions)

Starting on CIFAR-10 with captions like "a photo of a dog" keeps the data simple, so when something breaks, it's your model and not your data.

### Weekend 8 (Nov 28–29): Image-caption dataset
Task: Load CIFAR-10 with torchvision and write a `Dataset` that returns `(image, caption)`, where the caption is a template like "a photo of a {label}". Wrap it in a `DataLoader`.
Done when: one batch prints an image tensor of shape `[B, 3, 32, 32]` and a list of B captions, and you can explain each dimension.
Minimum: `__getitem__` returns one correct pair.

### Dec 5–6, Dec 12–13, Dec 19–20: OFF
Exam prep and fall exams (Dec 10–22). No project work.

### Weekend 9 (Dec 26–27): Tokenizer and text encoder v0
Task: Build a word-level tokenizer (a dict from word to id, which is Weekend 1 again), pad captions to a fixed length, then encode with `nn.Embedding` → mean pooling → linear projection.
Done when: a batch of captions becomes a tensor of shape `[B, D]`, and you can say what the padding does to the mean.
Minimum: the tokenizer, with captions turned into padded id tensors.

### Weekend 10 (Jan 2–3): Image encoder
Task: A small CNN (three conv blocks) → pooling → linear projection to the same D as the text encoder.
Done when: a batch of images becomes `[B, D]`, and you can predict the shape after every layer before running it. ✅ **Soft deadline.**
Minimum: the CNN runs on one batch.

---

## Part 3: Make it learn

Use a free Google Colab GPU for training weekends if your laptop is slow.

### Weekend 11 (Jan 9–10): Wire up CLIP
Task: Combine both encoders, L2-normalize the embeddings, add a learnable temperature, and plug in your Weekend 7 loss. Write the training loop.
Done when: the model overfits a single batch until the loss is near zero. If it can't overfit one batch, there's a bug.
Minimum: one forward and backward pass with no errors.

### Weekend 12 (Jan 16–17): Full training run
Task: Train on all of CIFAR-10 and plot the training loss.
Done when: the loss starts near ln(batch size) and ends clearly below it, and you have the plot saved in the repo.
Minimum: a run of a few epochs, plotted.

### Weekend 13 (Jan 23–24): Zero-shot classification
Task: Encode "a photo of a {class}" for all 10 classes, then classify each test image by which caption embedding it's closest to (cosine similarity). No classifier training.
Done when: zero-shot test accuracy is clearly above 10% (random chance), and you can explain why this works without ever training a classifier.
Minimum: predictions for one batch.

> **Cut line:** if you're more than one weekend behind here, skip Weekends 14–16 and do the comparison (Weekend 17) on CIFAR-10 only.

---

## Part 4: Real captions and the comparison

### Weekend 14 (Jan 30–31): Flickr8k dataset
Task: Download Flickr8k (8,000 images, 5 captions each). Write a `Dataset` that resizes images to 64×64 and picks one of the 5 captions at random. Rebuild the vocab. Hold out 1,000 images for testing.
Done when: a batch loads with the right shapes and the captions match their images when you look at them.
Minimum: images and captions load as pairs.

### Weekend 15 (Feb 6–7): Transformer text encoder
Task: Replace mean pooling with `nn.TransformerEncoder` plus positional embeddings, and train on Flickr8k.
Done when: the loss decreases, and you can explain why word order matters now and didn't before.
Minimum: the new encoder outputs `[B, D]`.

### Weekend 16 (Feb 13–14): Retrieval evaluation
Task: On the 1,000 held-out images, compute Recall@1, @5 and @10 for image→text and text→image. Save a grid of example retrievals.
Done when: Recall@10 is clearly above random (1%), and you have a results table.
Minimum: Recall@10 for one direction.

### Weekend 17 (Feb 20–21): Compare against pretrained CLIP
Task: Load a pretrained CLIP (`open_clip` or Hugging Face `transformers`) and run the exact same evaluations: CIFAR-10 zero-shot and Flickr8k retrieval.
Done when: one table shows your model next to pretrained CLIP on every metric, and you can name two reasons for the gap.
Minimum: CIFAR-10 zero-shot for both models.

### Weekend 18 (Feb 27–28): Write-up 🏁 **Hard deadline**
Task: Rewrite this README into a project page: what you built, the results table, loss curve, retrieval examples, and what you'd do next (embedded CLIP).
Done when: someone else could clone the repo and reproduce your numbers.
Minimum: the results table and loss curve, with one paragraph each.
