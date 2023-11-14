"""
Type annotations for keyspaces service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/literals.html)

Usage::

    ```python
    from mypy_boto3_keyspaces.literals import ClientSideTimestampsStatusType

    data: ClientSideTimestampsStatusType = "ENABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ClientSideTimestampsStatusType",
    "EncryptionTypeType",
    "ListKeyspacesPaginatorName",
    "ListTablesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "PointInTimeRecoveryStatusType",
    "SortOrderType",
    "TableStatusType",
    "ThroughputModeType",
    "TimeToLiveStatusType",
    "rsType",
)

ClientSideTimestampsStatusType = Literal["ENABLED"]
EncryptionTypeType = Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY"]
ListKeyspacesPaginatorName = Literal["list_keyspaces"]
ListTablesPaginatorName = Literal["list_tables"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
PointInTimeRecoveryStatusType = Literal["DISABLED", "ENABLED"]
SortOrderType = Literal["ASC", "DESC"]
TableStatusType = Literal[
    "ACTIVE",
    "CREATING",
    "DELETED",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "RESTORING",
    "UPDATING",
]
ThroughputModeType = Literal["PAY_PER_REQUEST", "PROVISIONED"]
TimeToLiveStatusType = Literal["ENABLED"]
rsType = Literal["MULTI_REGION", "SINGLE_REGION"]
