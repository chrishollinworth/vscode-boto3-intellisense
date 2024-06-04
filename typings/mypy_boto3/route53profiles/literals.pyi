"""
Type annotations for route53profiles service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/literals.html)

Usage::

    ```python
    from mypy_boto3_route53profiles.literals import ListProfileAssociationsPaginatorName

    data: ListProfileAssociationsPaginatorName = "list_profile_associations"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListProfileAssociationsPaginatorName",
    "ListProfileResourceAssociationsPaginatorName",
    "ListProfilesPaginatorName",
    "ProfileStatusType",
    "ShareStatusType",
)

ListProfileAssociationsPaginatorName = Literal["list_profile_associations"]
ListProfileResourceAssociationsPaginatorName = Literal["list_profile_resource_associations"]
ListProfilesPaginatorName = Literal["list_profiles"]
ProfileStatusType = Literal["COMPLETE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
ShareStatusType = Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
