"""
The :mod:`holistic.datasets` module includes dataloaders for quick experimentation
"""

from holistic.datasets._dataloaders import (
    load_acsincome,
    load_acspublic,
    load_adult,
    load_bank_marketing,
    load_census_kdd,
    load_compas_is_recid,
    load_compas_two_year_recid,
    load_diabetes,
    load_german_credit,
    load_heart,
    load_last_fm,
    load_law_school,
    load_student,
    load_us_crime,
)
from holistic.datasets._dataset import DataLoader, Dataset, DatasetDict, GroupByDataset, concatenate_datasets
from holistic.datasets._load_dataset import load_dataset

__all__ = [
    "load_dataset",
    "Dataset",
    "DatasetDict",
    "GroupByDataset",
    "DataLoader",
    "concatenate_datasets",
    "load_adult",
    "load_last_fm",
    "load_law_school",
    "load_heart",
    "load_student",
    "load_us_crime",
    "load_german_credit",
    "load_census_kdd",
    "load_bank_marketing",
    "load_compas_two_year_recid",
    "load_compas_is_recid",
    "load_diabetes",
    "load_acsincome",
    "load_acspublic",
]
