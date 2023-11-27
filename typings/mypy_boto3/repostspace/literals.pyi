"""
Type annotations for repostspace service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/literals.html)

Usage::

    ```python
    from mypy_boto3_repostspace.literals import ConfigurationStatusType

    data: ConfigurationStatusType = "CONFIGURED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConfigurationStatusType",
    "ListSpacesPaginatorName",
    "TierLevelType",
    "VanityDomainStatusType",
)

ConfigurationStatusType = Literal["CONFIGURED", "UNCONFIGURED"]
ListSpacesPaginatorName = Literal["list_spaces"]
TierLevelType = Literal["BASIC", "STANDARD"]
VanityDomainStatusType = Literal["APPROVED", "PENDING", "UNAPPROVED"]
