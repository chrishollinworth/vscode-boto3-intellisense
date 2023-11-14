"""
Type annotations for bedrock service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/literals.html)

Usage::

    ```python
    from mypy_boto3_bedrock.literals import CommitmentDurationType

    data: CommitmentDurationType = "OneMonth"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CommitmentDurationType",
    "FineTuningJobStatusType",
    "InferenceTypeType",
    "ListCustomModelsPaginatorName",
    "ListModelCustomizationJobsPaginatorName",
    "ListProvisionedModelThroughputsPaginatorName",
    "ModelCustomizationJobStatusType",
    "ModelCustomizationType",
    "ModelModalityType",
    "ProvisionedModelStatusType",
    "SortByProvisionedModelsType",
    "SortJobsByType",
    "SortModelsByType",
    "SortOrderType",
)

CommitmentDurationType = Literal["OneMonth", "SixMonths"]
FineTuningJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
InferenceTypeType = Literal["ON_DEMAND", "PROVISIONED"]
ListCustomModelsPaginatorName = Literal["list_custom_models"]
ListModelCustomizationJobsPaginatorName = Literal["list_model_customization_jobs"]
ListProvisionedModelThroughputsPaginatorName = Literal["list_provisioned_model_throughputs"]
ModelCustomizationJobStatusType = Literal[
    "Completed", "Failed", "InProgress", "Stopped", "Stopping"
]
ModelCustomizationType = Literal["FINE_TUNING"]
ModelModalityType = Literal["EMBEDDING", "IMAGE", "TEXT"]
ProvisionedModelStatusType = Literal["Creating", "Failed", "InService", "Updating"]
SortByProvisionedModelsType = Literal["CreationTime"]
SortJobsByType = Literal["CreationTime"]
SortModelsByType = Literal["CreationTime"]
SortOrderType = Literal["Ascending", "Descending"]
