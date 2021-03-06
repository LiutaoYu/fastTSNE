import numpy as np

from .tsne import TSNEEmbedding


def pBIC(embedding: TSNEEmbedding) -> float:
    n_samples = embedding.shape[0]

    return 2 * embedding.kl_divergence + np.log(n_samples) * \
        embedding.affinities.perplexity / n_samples
