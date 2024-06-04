"""
Type annotations for cleanroomsml service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/literals.html)

Usage::

    ```python
    from mypy_boto3_cleanroomsml.literals import AudienceExportJobStatusType

    data: AudienceExportJobStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AudienceExportJobStatusType",
    "AudienceGenerationJobStatusType",
    "AudienceModelStatusType",
    "AudienceSizeTypeType",
    "ColumnTypeType",
    "ConfiguredAudienceModelStatusType",
    "DatasetTypeType",
    "ListAudienceExportJobsPaginatorName",
    "ListAudienceGenerationJobsPaginatorName",
    "ListAudienceModelsPaginatorName",
    "ListConfiguredAudienceModelsPaginatorName",
    "ListTrainingDatasetsPaginatorName",
    "PolicyExistenceConditionType",
    "SharedAudienceMetricsType",
    "TagOnCreatePolicyType",
    "TrainingDatasetStatusType",
)

AudienceExportJobStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_PENDING"
]
AudienceGenerationJobStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_PENDING",
]
AudienceModelStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_PENDING",
]
AudienceSizeTypeType = Literal["ABSOLUTE", "PERCENTAGE"]
ColumnTypeType = Literal[
    "CATEGORICAL_FEATURE", "ITEM_ID", "NUMERICAL_FEATURE", "TIMESTAMP", "USER_ID"
]
ConfiguredAudienceModelStatusType = Literal["ACTIVE"]
DatasetTypeType = Literal["INTERACTIONS"]
ListAudienceExportJobsPaginatorName = Literal["list_audience_export_jobs"]
ListAudienceGenerationJobsPaginatorName = Literal["list_audience_generation_jobs"]
ListAudienceModelsPaginatorName = Literal["list_audience_models"]
ListConfiguredAudienceModelsPaginatorName = Literal["list_configured_audience_models"]
ListTrainingDatasetsPaginatorName = Literal["list_training_datasets"]
PolicyExistenceConditionType = Literal["POLICY_MUST_EXIST", "POLICY_MUST_NOT_EXIST"]
SharedAudienceMetricsType = Literal["ALL", "NONE"]
TagOnCreatePolicyType = Literal["FROM_PARENT_RESOURCE", "NONE"]
TrainingDatasetStatusType = Literal["ACTIVE"]
