# VLAD fundamentals

### Table of Contents

- [VLAD normalization](https://www.vlfeat.org/api/vlad-fundamentals.html#vlad-normalization)

This page describes the *Vector of Locally Aggregated Descriptors* (VLAD) image encoding of [11](https://www.vlfeat.org/api/citelist.html#CITEREF_jegou10aggregating) . See [Vector of Locally Aggregated Descriptors (VLAD) encoding](https://www.vlfeat.org/api/vlad.html) for an overview of the C API.

VLAD is a *feature encoding and pooling* method, similar to [Fisher vectors](https://www.vlfeat.org/api/fisher.html). VLAD encodes a set of local feature descriptors $I=(\mathbf{x}_1,\dots,\mathbf{x}_n)$ extracted from an image using a dictionary built using a clustering method such as [Gaussian Mixture Models (GMM)](https://www.vlfeat.org/api/gmm.html) or [K-means clustering](https://www.vlfeat.org/api/kmeans.html). Let $q_{ik}$ be the strength of the association of data vector $\mathbf{x}_i$ to cluster $\mu_k$, such that $q_{ik} \geq 0$ and $\sum_{k=1}^K q_{ik} = 1$. The association may be either soft (e.g. obtained as the posterior probabilities of the GMM clusters) or hard (e.g. obtained by vector quantization with K-means).

$\mu_k$ are the cluster *means*, vectors of the same dimension as the data $\mathbf{x}_i$. VLAD encodes feature $\mathbf{x}$ by considering the *residuals*

$$
\mathbf{v}_k = \sum_{i=1}^{N} q_{ik} (\mathbf{x}_{i} - \mu_k).
$$
The residulas are stacked together to obtain the vector

$$
\hat\Phi(I) = \begin{bmatrix} \vdots \\ \mathbf{v}_k \\ \vdots \end{bmatrix}
$$

Before the VLAD encoding is used it is usually normalized, as explained [VLAD normalization](https://www.vlfeat.org/api/vlad-fundamentals.html#vlad-normalization) next.

# VLAD normalization

VLFeat VLAD implementation supports a number of different normalization strategies. These are optionally applied in this order:

- **Component-wise mass normalization.** Each vector $\mathbf{v}_k$ is divided by the total mass of features associated to it $\sum_{i=1}^N q_{ik}$.
- **Square-rooting.** The function $\mathrm{sign}(z)\sqrt{|z|}$ is applied to all scalar components of the VLAD descriptor.
- **Component-wise $l^2$ normalization.** The vectors $\mathbf{v}_k$ are divided by their norm $\|\mathbf{v}_k\|_2$.
- **Global $l^2$ normalization.** The VLAD descriptor $\hat\Phi(I)$ is divided by its norm $\|\hat\Phi(I)\|_2$.