from collections import namedtuple

from holistic.utils.transformers.bias._group_utils import SensitiveGroups
from holistic.utils.transformers.bias._inprocessing import BMInprocessing
from holistic.utils.transformers.bias._postprocessing import BMPostprocessing
from holistic.utils.transformers.bias._preprocessing import BMPreprocessing

BiasMitigationTags = namedtuple("BiasMitigationTags", ["PRE", "INP", "POST"])  # noqa: PYI024
BIAS_TAGS = BiasMitigationTags(PRE="bm_pre", INP="bm_inp", POST="bm_pos")

__all__ = ["BMInprocessing", "BMPostprocessing", "BMPreprocessing", "SensitiveGroups"]
