import unittest

import networkx as nx
import numpy as np

# from toponetx.simplicial_complex import SimplicialComplex
from topomodelx.normalization import (
    _compute_B1_normalized,
    _compute_B1T_normalized,
    _compute_B2_normalized,
    _compute_B2T_normalized,
)
from topomodelx.normalization.normalization import get_normalized_2d_operators

from toponetx.classes.simplicial_complex import SimplicialComplex

# sys.path.append("..")


class test_normalization(unittest.TestCase):
    def test_compute_B1_normalized(self):
        G = nx.karate_club_graph()
        cliques = list(nx.enumerate_all_cliques(G))

        SC = SimplicialComplex(cliques)
        B1 = SC.get_boundary_operator(1)
        B2 = SC.get_boundary_operator(2)
        B1N, B1TN, B2N, B2TN = get_normalized_2d_operators(B1, B2)
        assert B1.shape == B1N.shape
        assert B2.shape == B2N.shape
        assert B1TN.shape == B1.T.shape
        assert B2.T.shape == B2TN.shape
        assert (
            _compute_B1_normalized(B1.toarray(), B2.toarray()).all()
            == _compute_B1_normalized(B1, B2).toarray().all()
        )

        assert (
            _compute_B1T_normalized(B1.toarray(), B2.toarray()).all()
            == _compute_B1T_normalized(B1, B2).toarray().all()
        )

        assert (
            _compute_B2_normalized(B2.toarray()).all()
            == _compute_B2_normalized(B2).toarray().all()
        )

        assert (
            _compute_B2T_normalized(B2.toarray()).all()
            == _compute_B2T_normalized(B2).toarray().all()
        )

        assert np.sign(B1N.toarray()).all() == B1.toarray().all()
        assert np.sign(B1TN.toarray()).all() == B1.T.toarray().all()
        assert np.sign(B2N.toarray()).all() == B2.toarray().all()
        assert np.sign(B2TN.toarray()).all() == B2.T.toarray().all()


# if __name__ == "__main__":
#    unittest.main()