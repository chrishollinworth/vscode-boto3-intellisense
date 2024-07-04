"""
Type annotations for osis service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/literals.html)

Usage::

    ```python
    from mypy_boto3_osis.literals import ChangeProgressStageStatusesType

    data: ChangeProgressStageStatusesType = "COMPLETED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeProgressStageStatusesType",
    "ChangeProgressStatusesType",
    "PipelineStatusType",
    "VpcEndpointManagementType",
    "VpcEndpointServiceNameType",
)

ChangeProgressStageStatusesType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]
ChangeProgressStatusesType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]
PipelineStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATING",
    "DELETING",
    "STARTING",
    "START_FAILED",
    "STOPPED",
    "STOPPING",
    "UPDATE_FAILED",
    "UPDATING",
]
VpcEndpointManagementType = Literal["CUSTOMER", "SERVICE"]
VpcEndpointServiceNameType = Literal["OPENSEARCH_SERVERLESS"]
