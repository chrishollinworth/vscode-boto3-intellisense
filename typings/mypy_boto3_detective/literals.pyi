"""
Type annotations for detective service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/literals.html)

Usage::

    ```python
    from mypy_boto3_detective.literals import DatasourcePackageIngestStateType

    data: DatasourcePackageIngestStateType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DatasourcePackageIngestStateType",
    "DatasourcePackageType",
    "InvitationTypeType",
    "MemberDisabledReasonType",
    "MemberStatusType",
)

DatasourcePackageIngestStateType = Literal["DISABLED", "STARTED", "STOPPED"]
DatasourcePackageType = Literal["ASFF_SECURITYHUB_FINDING", "DETECTIVE_CORE", "EKS_AUDIT"]
InvitationTypeType = Literal["INVITATION", "ORGANIZATION"]
MemberDisabledReasonType = Literal["VOLUME_TOO_HIGH", "VOLUME_UNKNOWN"]
MemberStatusType = Literal[
    "ACCEPTED_BUT_DISABLED", "ENABLED", "INVITED", "VERIFICATION_FAILED", "VERIFICATION_IN_PROGRESS"
]
