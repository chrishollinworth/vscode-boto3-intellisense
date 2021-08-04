"""
Type annotations for transfer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/literals.html)

Usage::

    ```python
    from mypy_boto3_transfer.literals import DomainType

    data: DomainType = "EFS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DomainType",
    "EndpointTypeType",
    "HomeDirectoryTypeType",
    "IdentityProviderTypeType",
    "ListServersPaginatorName",
    "ProtocolType",
    "StateType",
)

DomainType = Literal["EFS", "S3"]
EndpointTypeType = Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]
HomeDirectoryTypeType = Literal["LOGICAL", "PATH"]
IdentityProviderTypeType = Literal["API_GATEWAY", "AWS_DIRECTORY_SERVICE", "SERVICE_MANAGED"]
ListServersPaginatorName = Literal["list_servers"]
ProtocolType = Literal["FTP", "FTPS", "SFTP"]
StateType = Literal["OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"]
