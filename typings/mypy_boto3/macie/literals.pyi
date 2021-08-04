"""
Type annotations for macie service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/literals.html)

Usage::

    ```python
    from mypy_boto3_macie.literals import ListMemberAccountsPaginatorName

    data: ListMemberAccountsPaginatorName = "list_member_accounts"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListMemberAccountsPaginatorName",
    "ListS3ResourcesPaginatorName",
    "S3ContinuousClassificationTypeType",
    "S3OneTimeClassificationTypeType",
)

ListMemberAccountsPaginatorName = Literal["list_member_accounts"]
ListS3ResourcesPaginatorName = Literal["list_s3_resources"]
S3ContinuousClassificationTypeType = Literal["FULL"]
S3OneTimeClassificationTypeType = Literal["FULL", "NONE"]
