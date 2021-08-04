"""
Type annotations for detective service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/literals.html)

Usage::

    ```python
    from mypy_boto3_detective.literals import MemberDisabledReasonType

    data: MemberDisabledReasonType = "VOLUME_TOO_HIGH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MemberDisabledReasonType", "MemberStatusType")

MemberDisabledReasonType = Literal["VOLUME_TOO_HIGH", "VOLUME_UNKNOWN"]
MemberStatusType = Literal[
    "ACCEPTED_BUT_DISABLED", "ENABLED", "INVITED", "VERIFICATION_FAILED", "VERIFICATION_IN_PROGRESS"
]
