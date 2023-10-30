# Fisher vector fundamentals

### Table of Contents

- [Normalization and improved Fisher vectors](https://www.vlfeat.org/api/fisher-fundamentals.html#fisher-normalization)
- [Faster computations](https://www.vlfeat.org/api/fisher-fundamentals.html#fisher-fast)

This page describes the *Fisher Vector* (FV) of [23](https://www.vlfeat.org/api/citelist.html#CITEREF_perronnin06fisher) [24](https://www.vlfeat.org/api/citelist.html#CITEREF_perronnin10improving) . See [Fisher Vector encoding (FV)](https://www.vlfeat.org/api/fisher.html) for an overview of the C API and [Fisher kernel](https://www.vlfeat.org/api/fisher-kernel.html) for its relation to the more general notion of Fisher kernel.

The FV is an image representation obtained by pooling local image features. It is frequently used as a global image descriptor in visual classification.

While the FV can be [derived](https://www.vlfeat.org/api/fisher-kernel.html) as a special, approximate, and improved case of the general Fisher Kernel framework, it is easy to describe directly. Let $I = (\mathbf{x}_1,\dots,\mathbf{x}_N)$ be a set of $D$ dimensional feature vectors (e.g. SIFT descriptors) extracted from an image. Let $\Theta=(\mu_k,\Sigma_k,\pi_k:k=1,\dots,K)$ be the parameters of a [Gaussian Mixture Model](https://www.vlfeat.org/api/gmm.html) fitting the distribution of descriptors. The GMM associates each vector $\mathbf{x}_i$ to a mode $k$ in the mixture with a strength given by the posterior probability:

$$
q_{ik} = \frac {\exp\left[-\frac{1}{2}(\mathbf{x}_i - \mu_k)^T \Sigma_k^{-1} (\mathbf{x}_i - \mu_k)\right]} {\sum_{t=1}^K \exp\left[-\frac{1}{2}(\mathbf{x}_i - \mu_t)^T \Sigma_k^{-1} (\mathbf{x}_i - \mu_t)\right]}. 
$$

For each mode $k$, consider the mean and covariance deviation vectors

$$
\begin{align*} u_{jk} &= {1 \over {N \sqrt{\pi_k}}} \sum_{i=1}^{N} q_{ik} \frac{x_{ji} - \mu_{jk}}{\sigma_{jk}}, \\ v_{jk} &= {1 \over {N \sqrt{2 \pi_k}}} \sum_{i=1}^{N} q_{ik} \left[ \left(\frac{x_{ji} - \mu_{jk}}{\sigma_{jk}}\right)^2 - 1 \right]. \end{align*}
$$

where $j=1,2,\dots,D$ spans the vector dimensions. The FV of image $I$ is the stacking of the vectors $\mathbf{u}_k$ and then of the vectors $\mathbf{v}_k$ for each of the $K$ modes in the Gaussian mixtures:

$$
\Phi(I) = \begin{bmatrix} \vdots \\ \mathbf{u}_k \\ \vdots \\ \mathbf{v}_k \\ \vdots \end{bmatrix}.
$$

# Normalization and improved Fisher vectors

The *improved* Fisher Vector [[24$$](https://www.vlfeat.org/api/citelist.html#CITEREF_perronnin10improving) (IFV) improves the classification performance of the representation by using to ideas:

1. *Non-linear additive kernel.* The Hellinger's kernel (or Bhattacharya coefficient) can be used instead of the linear one at no cost by signed squared rooting. This is obtained by applying the function $|z| \mathrm{sign} z$ to each dimension of the vector $\Phi(I)$. Other [additive kernels](https://www.vlfeat.org/api/homkermap.html) can also be used at an increased space or time cost.
2. *Normalization.* Before using the representation in a linear model (e.g. a [support vector machine](https://www.vlfeat.org/api/svm.html)), the vector $\Phi(I)$ is further normalized by the $l^2$ norm (note that the standard Fisher vector is normalized by the number of encoded feature vectors).

After square-rooting and normalization, the IFV is often used in a linear classifier such as an [SVM](https://www.vlfeat.org/api/svm.html).

# Faster computations

In practice, several data to cluster assignments $q_{ik}$ are likely to be very small or even negligible. The *fast* version of the FV sets to zero all but the largest assignment for each input feature $\mathbf{x}_i$.