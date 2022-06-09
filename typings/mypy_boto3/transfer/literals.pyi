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
    "ListAccessesPaginatorName",
    "ListExecutionsPaginatorName",
    "ListSecurityPoliciesPaginatorName",
    "ListServersPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListUsersPaginatorName",
    "ListWorkflowsPaginatorName",
    "OverwriteExistingType",
    "ProtocolType",
    "ServerOfflineWaiterName",
    "ServerOnlineWaiterName",
    "SetStatOptionType",
    "StateType",
    "TlsSessionResumptionModeType",
    "WorkflowStepTypeType",
)

CustomStepStatusType = Literal["FAILURE", "SUCCESS"]
DomainType = Literal["EFS", "S3"]
EndpointTypeType = Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]
ExecutionErrorTypeType = Literal[
    "ALREADY_EXISTS",
    "BAD_REQUEST",
    "CUSTOM_STEP_FAILED",
    "INTERNAL_SERVER_ERROR",
    "NOT_FOUND",
    "PERMISSION_DENIED",
    "THROTTLED",
    "TIMEOUT",
]
ExecutionStatusType = Literal["COMPLETED", "EXCEPTION", "HANDLING_EXCEPTION", "IN_PROGRESS"]
HomeDirectoryTypeType = Literal["LOGICAL", "PATH"]
IdentityProviderTypeType = Literal[
    "API_GATEWAY", "AWS_DIRECTORY_SERVICE", "AWS_LAMBDA", "SERVICE_MANAGED"
]
ListAccessesPaginatorName = Literal["list_accesses"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListSecurityPoliciesPaginatorName = Literal["list_security_policies"]
ListServersPaginatorName = Literal["list_servers"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListUsersPaginatorName = Literal["list_users"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
OverwriteExistingType = Literal["FALSE", "TRUE"]
ProtocolType = Literal["FTP", "FTPS", "SFTP"]
ServerOfflineWaiterName = Literal["server_offline"]
ServerOnlineWaiterName = Literal["server_online"]
SetStatOptionType = Literal["DEFAULT", "ENABLE_NO_OP"]
StateType = Literal["OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"]
TlsSessionResumptionModeType = Literal["DISABLED", "ENABLED", "ENFORCED"]
WorkflowStepTypeType = Literal["COPY", "CUSTOM", "DELETE", "TAG"]
