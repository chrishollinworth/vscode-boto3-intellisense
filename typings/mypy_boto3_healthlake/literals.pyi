"""
Type annotations for healthlake service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/literals.html)

Usage::

    ```python
    from mypy_boto3_healthlake.literals import CmkTypeType

    data: CmkTypeType = "AWS_OWNED_KMS_KEY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CmkTypeType",
    "DatastoreStatusType",
    "FHIRVersionType",
    "JobStatusType",
    "PreloadDataTypeType",
)

CmkTypeType = Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY"]
DatastoreStatusType = Literal["ACTIVE", "CREATING", "DELETED", "DELETING"]
FHIRVersionType = Literal["R4"]
JobStatusType = Literal["COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"]
PreloadDataTypeType = Literal["SYNTHEA"]
