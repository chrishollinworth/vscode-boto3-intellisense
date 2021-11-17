"""
Type annotations for cloudcontrol service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudcontrol.literals import HandlerErrorCodeType

    data: HandlerErrorCodeType = "AccessDenied"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "HandlerErrorCodeType",
    "OperationStatusType",
    "OperationType",
    "ResourceRequestSuccessWaiterName",
)

HandlerErrorCodeType = Literal[
    "AccessDenied",
    "AlreadyExists",
    "GeneralServiceException",
    "InternalFailure",
    "InvalidCredentials",
    "InvalidRequest",
    "NetworkFailure",
    "NotFound",
    "NotStabilized",
    "NotUpdatable",
    "ResourceConflict",
    "ServiceInternalError",
    "ServiceLimitExceeded",
    "ServiceTimeout",
    "Throttling",
]
OperationStatusType = Literal[
    "CANCEL_COMPLETE", "CANCEL_IN_PROGRESS", "FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"
]
OperationType = Literal["CREATE", "DELETE", "UPDATE"]
ResourceRequestSuccessWaiterName = Literal["resource_request_success"]
