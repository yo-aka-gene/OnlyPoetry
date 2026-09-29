from typing import Optional

import anndata as ad


def transfer_embedding_info(
    adata_source: ad.AnnData, adata_target: ad.AnnData, overwrite: bool = False
) -> Optional[ad.AnnData]:
    """
    Transfer embedding and neighborhood graph information from one AnnData to another.

    This function copies PCA, UMAP, neighborhood graph parameters (`uns["neighbors"]`),
    and pairwise connectivity matrices (`obsp`) from `adata_source` to `adata_target`.
    Both AnnData objects must have the exact same number of observations (n_obs).

    Parameters
    ----------
    adata_source : ad.AnnData
        The source AnnData object containing the computed embeddings and graphs.
    adata_target : ad.AnnData
        The target AnnData object to receive the embeddings.
    overwrite : bool, optional
        If True, modifies `adata_target` in-place and returns None.
        If False (default), returns a modified copy of `adata_target`.

    Returns
    -------
    Optional[ad.AnnData]
        A new AnnData object with transferred embeddings if `overwrite=False`,
        otherwise None (modifies in-place).

    Examples
    --------
    >>> import anndata as ad
    >>> import numpy as np
    >>> from scipy import sparse
    >>> # Setup mock AnnData objects (3 cells, 5 genes)
    >>> X_mock = np.zeros((3, 5))
    >>> adata_src = ad.AnnData(X_mock)
    >>> adata_tgt = ad.AnnData(X_mock)
    >>>
    >>> # Add mock embeddings and graphs to source
    >>> adata_src.obsm["X_pca"] = np.ones((3, 2)) * 1.5
    >>> adata_src.obsm["X_umap"] = np.ones((3, 2)) * 2.5
    >>> adata_src.uns["neighbors"] = {"params": {"n_neighbors": 15}}
    >>> adata_src.obsp["distances"] = sparse.csr_matrix(np.eye(3))
    >>>
    >>> # Test with overwrite=False
    >>> adata_res = transfer_embedding_info(adata_src, adata_tgt, overwrite=False)
    >>> adata_res.obsm["X_umap"][0, 0]
    np.float64(2.5)
    >>> adata_tgt.obsm is None or "X_umap" not in adata_tgt.obsm
    True
    >>>
    >>> # Test with overwrite=True
    >>> res = transfer_embedding_info(adata_src, adata_tgt, overwrite=True)
    >>> res is None
    True
    >>> adata_tgt.obsm["X_pca"][0, 0]
    np.float64(1.5)
    """
    adata_return = adata_target if overwrite else adata_target.copy()

    adata_return.obsm["X_pca"] = adata_source.obsm["X_pca"].copy()
    adata_return.obsm["X_umap"] = adata_source.obsm["X_umap"].copy()

    if "neighbors" in adata_source.uns:
        import copy

        adata_return.uns["neighbors"] = copy.deepcopy(adata_source.uns["neighbors"])

    for key, value in adata_source.obsp.items():
        adata_return.obsp[key] = value.copy()

    return None if overwrite else adata_return
