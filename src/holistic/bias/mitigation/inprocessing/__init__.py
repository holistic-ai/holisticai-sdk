# imports
from holistic.bias.mitigation.inprocessing.adversarial_debiasing.transformer import AdversarialDebiasing
from holistic.bias.mitigation.inprocessing.exponentiated_gradient.transformer import ExponentiatedGradientReduction
from holistic.bias.mitigation.inprocessing.fair_k_center_clustering.transformer import FairKCenterClustering
from holistic.bias.mitigation.inprocessing.fair_k_mediam_clustering.transformer import FairKMedianClustering
from holistic.bias.mitigation.inprocessing.fairlet_clustering.transformer import FairletClustering
from holistic.bias.mitigation.inprocessing.grid_search.transformer import GridSearchReduction
from holistic.bias.mitigation.inprocessing.matrix_factorization.blind_spot_aware import BlindSpotAwareMF
from holistic.bias.mitigation.inprocessing.matrix_factorization.debiasing_learning.transformer import (
    DebiasingLearningMF,
)
from holistic.bias.mitigation.inprocessing.matrix_factorization.popularity_propensity import PopularityPropensityMF
from holistic.bias.mitigation.inprocessing.meta_fair_classifier.transformer import MetaFairClassifier
from holistic.bias.mitigation.inprocessing.prejudice_remover.transformer import PrejudiceRemover
from holistic.bias.mitigation.inprocessing.two_sided_fairness.transformer import FairRec
from holistic.bias.mitigation.inprocessing.variational_fair_clustering.transformer import VariationalFairClustering

__all__ = [
    "ExponentiatedGradientReduction",
    "GridSearchReduction",
    "PrejudiceRemover",
    "MetaFairClassifier",
    "VariationalFairClustering",
    "FairKCenterClustering",
    "FairKMedianClustering",
    "FairletClustering",
    "BlindSpotAwareMF",
    "DebiasingLearningMF",
    "PopularityPropensityMF",
    "FairRec",
    "AdversarialDebiasing",
]
import importlib.util

cvxpy_spec = importlib.util.find_spec("cvxpy")
if cvxpy_spec is not None:
    from holistic.bias.mitigation.inprocessing.fair_scoring_classifier.transformer import FairScoreClassifier

    __all__ += ["FairScoreClassifier"]
