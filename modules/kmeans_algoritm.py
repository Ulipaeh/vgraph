import numpy as np

def kmeans(data, k=2, normalize=True, limit=1000):
    if normalize:
        stats = (data.mean(axis=0), data.std(axis=0))
        data = (data - stats[0]) / stats[1]
    centers = data[:k]
    for i in range(limit):
        classifications = np.argmin(((data[:, :, None] - centers.T[None, :, :])**2).sum(axis=1), axis=1)
        new_centers = np.array([data[classifications == j, :].mean(axis=0) for j in range(k)])
        if (new_centers == centers).all():
            break
        else:
            centers = new_centers
    else:
        raise RuntimeError("Clustering algorithm did not complete within {limit} iterations")
    if normalize:
        centers = centers * stats[1] + stats[0]
    print("Clustering completed after {i} iterations")
    return classifications, centers