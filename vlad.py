import cv2
import numpy as np
import skimage.io as io
from sklearn.cluster import MiniBatchKMeans


# get a img SIFT
def get_sift(img: str):
    mat = cv2.imread(str(img))
    siftt = cv2.SIFT_create()
    kp, des = siftt.detectAndCompute(mat, None)
    return des


# use all extracted features to train a codebook
def train_code_book(features, batch_size=1000, clusters=64):
    database = []
    for i in range(len(features)):
        for j in range(len(features[i])):
            database.append(features[i][j])
    database = np.array(database)

    kmeans = MiniBatchKMeans(
        init="k-means++",
        n_clusters=clusters,
        max_iter=1000,
        batch_size=batch_size,
        n_init=10,
        max_no_improvement=10,
        verbose=0,
    ).fit(database)
    label = kmeans.labels_
    centroid = kmeans.cluster_centers_
    return kmeans, label, centroid


def vlad(kmeans, locdes, centroid, clusters=64):
    # assign the sift vector to corresponding centroid by nearest neighbor
    labels = kmeans.predict(locdes)
    des = []
    # iterate through the clusters, by first finding the local
    # descriptors that belong to that cluster, then summing.
    for i in range(clusters):
        des.append(np.zeros(shape=(1, 128)))
        matched = np.argwhere(labels == i)
        if len(matched) == 0:
            des[i] = np.zeros_like(centroid[0])
        else:
            # calculate the sum of subtraction and l2 normlization
            for idx in matched:
                des[i] += locdes[idx] - centroid[i]
            des[i] /= np.linalg.norm(des[i], ord=2)
    # reshape to a single vector
    des = np.concatenate(des, axis=-1)
    return des


if __name__ == "__main__":
    # train codebook
    folder = "./images/*.jpg"
    imgs = io.ImageCollection(folder)  # read a collection of images
    print(f"pictures numbers: {len(imgs):d}")

    features = [ cv2.SIFT_create().detectAndCompute(img, None)[1] for img in imgs]

    kmeans, _, centroid = train_code_book(features)

    # get a img VLAD feature
    des = get_sift("./images/frame_00281.jpg")
    ans = vlad(kmeans, des, centroid)
    print(ans.shape)
