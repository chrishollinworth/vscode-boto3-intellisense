"""
Main interface for sagemaker-runtime service type definitions.

Usage::

    ```python
    from mypy_boto3_sagemaker_runtime.type_defs import ResponseMetadata

    data: ResponseMetadata = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ResponseMetadata", "InvokeEndpointOutputTypeDef")

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredInvokeEndpointOutputTypeDef = TypedDict(
    "_RequiredInvokeEndpointOutputTypeDef", {"Body": Union[bytes, IO[bytes]]}
)
_OptionalInvokeEndpointOutputTypeDef = TypedDict(
    "_OptionalInvokeEndpointOutputTypeDef",
    {
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class InvokeEndpointOutputTypeDef(
    _RequiredInvokeEndpointOutputTypeDef, _OptionalInvokeEndpointOutputTypeDef
):
    pass
