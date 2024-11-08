# Imports
from holistic.bias.mitigation.preprocessing.correlation_remover import CorrelationRemover
from holistic.bias.mitigation.preprocessing.fairlet_clustering.transformer import FairletClusteringPreprocessing
from holistic.bias.mitigation.preprocessing.learning_fair_representation import LearningFairRepresentation
from holistic.bias.mitigation.preprocessing.reweighing import Reweighing

__all__ = [
    "LearningFairRepresentation",
    "Reweighing",
    "CorrelationRemover",
    "FairletClusteringPreprocessing",
]

import importlib

networkx_spec = importlib.util.find_spec("networkx")
if networkx_spec is not None:
    from holistic.bias.mitigation.preprocessing.disparate_impact_remover import DisparateImpactRemover

__all__ += ["DisparateImpactRemover"]
