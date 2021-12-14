# YCWYAV

Automated Meningioma Grade Classification

This is only the model part, which needs to create input to run it. 
Our input was 4D medical data and output was the probability of grade for meningioma patients.
Describe of our model.

3D asymmetric CNN architecture with two encoding paths was built to capture the image features based on the two MR sequences (T1-CE and T2-FLAIR). 
Each path had the same 3×3×3 kernel with a different number of filters to control the special feature of each sequence. 
The asymmetric CNN implements an 18:2 ratio for the T1-CE vs. T2- FLAIR encoding paths. 
Such a network can learn the individual feature representation from the two sequences with higher weighting on the T1-CE while incorporating 
features from T2-FLAIR. Inside each encoding path, the corresponding kernel convolution was applied twice with a rectified linear unit (RELU), 
a dropout layer between the convolutions with a dropout rate of 0.3, and a 2×2×2 max-pooling operation in each layer. 
The number of feature channels was doubled after the max-pooling operation. After feature extraction by 3D convolutional layers, 
three fully connected layers were applied to map 3D features. Dropout layers with a rate of 0.3 were applied after each fully connected layer. 
In the final step, the last fully connected layer was used to feed a softmax, which maps the feature vector to binary classes.

<img width="1381" alt="Screen Shot 2021-12-14 at 9 53 16 AM" src="https://user-images.githubusercontent.com/96093712/146021899-57d88161-22f6-4337-8aa9-86b38205f86e.png">
