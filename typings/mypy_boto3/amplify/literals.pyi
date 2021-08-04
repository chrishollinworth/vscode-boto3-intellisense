"""
Type annotations for amplify service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/literals.html)

Usage::

    ```python
    from mypy_boto3_amplify.literals import DomainStatusType

    data: DomainStatusType = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DomainStatusType",
    "JobStatusType",
    "JobTypeType",
    "ListAppsPaginatorName",
    "ListBranchesPaginatorName",
    "ListDomainAssociationsPaginatorName",
    "ListJobsPaginatorName",
    "PlatformType",
    "StageType",
)

DomainStatusType = Literal[
    "AVAILABLE",
    "CREATING",
    "FAILED",
    "IN_PROGRESS",
    "PENDING_DEPLOYMENT",
    "PENDING_VERIFICATION",
    "REQUESTING_CERTIFICATE",
    "UPDATING",
]
JobStatusType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "PENDING", "PROVISIONING", "RUNNING", "SUCCEED"
]
JobTypeType = Literal["MANUAL", "RELEASE", "RETRY", "WEB_HOOK"]
ListAppsPaginatorName = Literal["list_apps"]
ListBranchesPaginatorName = Literal["list_branches"]
ListDomainAssociationsPaginatorName = Literal["list_domain_associations"]
ListJobsPaginatorName = Literal["list_jobs"]
PlatformType = Literal["WEB"]
StageType = Literal["BETA", "DEVELOPMENT", "EXPERIMENTAL", "PRODUCTION", "PULL_REQUEST"]
