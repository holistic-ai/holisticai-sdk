"""
The :mod:`holistic.utils` module includes utils helper tools
"""

# formatting
from holistic.utils._commons import concatenate_metrics
from holistic.utils._definitions import (
    BinaryClassificationProxy,
    ClusteringProxy,
    ConditionalImportances,
    Importances,
    LocalConditionalImportances,
    LocalImportances,
    ModelProxy,
    MultiClassificationProxy,
    PartialDependence,
    RegressionProxy,
    create_proxy,
)
from holistic.utils._formatting import (
    extract_columns,
    extract_group_vectors,
    mat_to_binary,
    normalize_tensor,
    recommender_formatter,
)

# plotting
from holistic.utils._plotting import get_colors
from holistic.utils.surrogate_models import (
    BinaryClassificationSurrogate,
    ClusteringSurrogate,
    MultiClassificationSurrogate,
    RegressionSurrogate,
)

__all__ = [
    "extract_columns",
    "mat_to_binary",
    "normalize_tensor",
    "get_colors",
    "recommender_formatter",
    "extract_group_vectors",
    "BinaryClassificationProxy",
    "MultiClassificationProxy",
    "RegressionProxy",
    "create_proxy",
    "Importances",
    "LocalImportances",
    "LocalConditionalImportances",
    "PartialDependence",
    "ConditionalImportances",
    "ModelProxy",
    "concatenate_metrics",
    "ClusteringProxy",
    "ClusteringSurrogate",
    "RegressionSurrogate",
    "MultiClassificationSurrogate",
    "BinaryClassificationSurrogate",
]
