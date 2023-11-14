"""
Type annotations for docdb-elastic service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/literals.html)

Usage::

    ```python
    from mypy_boto3_docdb_elastic.literals import AuthType

    data: AuthType = "PLAIN_TEXT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthType",
    "ListClusterSnapshotsPaginatorName",
    "ListClustersPaginatorName",
    "StatusType",
)

AuthType = Literal["PLAIN_TEXT", "SECRET_ARN"]
ListClusterSnapshotsPaginatorName = Literal["list_cluster_snapshots"]
ListClustersPaginatorName = Literal["list_clusters"]
StatusType = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDS",
    "INVALID_SECURITY_GROUP_ID",
    "INVALID_SUBNET_ID",
    "IP_ADDRESS_LIMIT_EXCEEDED",
    "UPDATING",
    "VPC_ENDPOINT_LIMIT_EXCEEDED",
]
