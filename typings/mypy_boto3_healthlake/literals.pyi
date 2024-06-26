"""
Type annotations for healthlake service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/literals.html)

Usage::

    ```python
    from mypy_boto3_healthlake.literals import AuthorizationStrategyType

    data: AuthorizationStrategyType = "AWS_AUTH"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthorizationStrategyType",
    "CmkTypeType",
    "DatastoreStatusType",
    "ErrorCategoryType",
    "FHIRVersionType",
    "JobStatusType",
    "PreloadDataTypeType",
)

AuthorizationStrategyType = Literal["AWS_AUTH", "SMART_ON_FHIR_V1"]
CmkTypeType = Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY"]
DatastoreStatusType = Literal["ACTIVE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
ErrorCategoryType = Literal["NON_RETRYABLE_ERROR", "RETRYABLE_ERROR"]
FHIRVersionType = Literal["R4"]
JobStatusType = Literal[
    "CANCEL_COMPLETED",
    "CANCEL_FAILED",
    "CANCEL_IN_PROGRESS",
    "CANCEL_SUBMITTED",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
PreloadDataTypeType = Literal["SYNTHEA"]
