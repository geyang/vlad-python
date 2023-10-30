# VLAD Minimal Implementation and Example

This repo contains a minimal implementation of VLAD. Write for a project I am working on.

List of image-feature pooling methods:
- VLAD
- Fisher Vectors (FV)
- Bag of Features (BOF)
- NetVLAD (use CNN trained for place recognition)

VLAD involves the following steps:

1. Extract the SIFT descriptors of the image.
2. Use the extracted SIFT descriptors (which are the SIFT of all training images) to train a codebook, using K-means as the training method.
3. Now given a test image, collect SIFT descriptors, and assign each to the closest vector in the codebook.
4. Now to generate the image feature, we sum the residual of each cluster, with respect to the centroid. (i.e., sum up all the SIFTs belonging to the current cluster and subtract the center). Normalize this sum using L2 normalization, and then concatenate the k vectors, one for each cluster, into a vector shaped as kx128. 128 is the length of a single SIFT feature.

**References**:
- NetVLAD
- Forked from https://github.com/saijunhu/VLAD-python
- which in turn https://blog.csdn.net/zshluckydogs/article/details/81003966
