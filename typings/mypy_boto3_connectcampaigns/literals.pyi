"""
Type annotations for connectcampaigns service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/literals.html)

Usage::

    ```python
    from mypy_boto3_connectcampaigns.literals import CampaignStateType

    data: CampaignStateType = "Failed"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CampaignStateType",
    "EncryptionTypeType",
    "FailureCodeType",
    "GetCampaignStateBatchFailureCodeType",
    "InstanceIdFilterOperatorType",
    "InstanceOnboardingJobFailureCodeType",
    "InstanceOnboardingJobStatusCodeType",
    "ListCampaignsPaginatorName",
)

CampaignStateType = Literal["Failed", "Initialized", "Paused", "Running", "Stopped"]
EncryptionTypeType = Literal["KMS"]
FailureCodeType = Literal["InvalidInput", "RequestThrottled", "UnknownError"]
GetCampaignStateBatchFailureCodeType = Literal["ResourceNotFound", "UnknownError"]
InstanceIdFilterOperatorType = Literal["Eq"]
InstanceOnboardingJobFailureCodeType = Literal[
    "EVENT_BRIDGE_ACCESS_DENIED",
    "EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED",
    "IAM_ACCESS_DENIED",
    "INTERNAL_FAILURE",
    "KMS_ACCESS_DENIED",
    "KMS_KEY_NOT_FOUND",
]
InstanceOnboardingJobStatusCodeType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ListCampaignsPaginatorName = Literal["list_campaigns"]
