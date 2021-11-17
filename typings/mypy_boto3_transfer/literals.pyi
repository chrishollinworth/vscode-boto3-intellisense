"""
Type annotations for transfer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/literals.html)

Usage::

    ```python
    from mypy_boto3_transfer.literals import CustomStepStatusType

    data: CustomStepStatusType = "FAILURE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CustomStepStatusType",
    "DomainType",
    "EndpointTypeType",
    "ExecutionErrorTypeType",
    "ExecutionStatusType",
    "HomeDirectoryTypeType",
    "IdentityProviderTypeType",
    "ListServersPaginatorName",
    "OverwriteExistingType",
    "ProtocolType",
    "StateType",
    "WorkflowStepTypeType",
)

CustomStepStatusType = Literal["FAILURE", "SUCCESS"]
DomainType = Literal["EFS", "S3"]
EndpointTypeType = Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]
ExecutionErrorTypeType = Literal["PERMISSION_DENIED"]
ExecutionStatusType = Literal["COMPLETED", "EXCEPTION", "HANDLING_EXCEPTION", "IN_PROGRESS"]
HomeDirectoryTypeType = Literal["LOGICAL", "PATH"]
IdentityProviderTypeType = Literal[
    "API_GATEWAY", "AWS_DIRECTORY_SERVICE", "AWS_LAMBDA", "SERVICE_MANAGED"
]
ListServersPaginatorName = Literal["list_servers"]
OverwriteExistingType = Literal["FALSE", "TRUE"]
ProtocolType = Literal["FTP", "FTPS", "SFTP"]
StateType = Literal["OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"]
WorkflowStepTypeType = Literal["COPY", "CUSTOM", "DELETE", "TAG"]
