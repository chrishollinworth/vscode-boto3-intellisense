"""
Type annotations for account service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/literals.html)

Usage::

    ```python
    from mypy_boto3_account.literals import AlternateContactTypeType

    data: AlternateContactTypeType = "BILLING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AlternateContactTypeType", "ListRegionsPaginatorName", "RegionOptStatusType")

AlternateContactTypeType = Literal["BILLING", "OPERATIONS", "SECURITY"]
ListRegionsPaginatorName = Literal["list_regions"]
RegionOptStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLED_BY_DEFAULT", "ENABLING"]
