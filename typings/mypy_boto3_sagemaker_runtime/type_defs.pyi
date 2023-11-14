"""
Type annotations for sagemaker-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_runtime.type_defs import InternalStreamFailureTypeDef

    data: InternalStreamFailureTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "InternalStreamFailureTypeDef",
    "InvokeEndpointAsyncInputRequestTypeDef",
    "InvokeEndpointAsyncOutputTypeDef",
    "InvokeEndpointInputRequestTypeDef",
    "InvokeEndpointOutputTypeDef",
    "InvokeEndpointWithResponseStreamInputRequestTypeDef",
    "InvokeEndpointWithResponseStreamOutputTypeDef",
    "ModelStreamErrorTypeDef",
    "PayloadPartTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseStreamTypeDef",
)

InternalStreamFailureTypeDef = TypedDict(
    "InternalStreamFailureTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredInvokeEndpointAsyncInputRequestTypeDef = TypedDict(
    "_RequiredInvokeEndpointAsyncInputRequestTypeDef",
    {
        "EndpointName": str,
        "InputLocation": str,
    },
)
_OptionalInvokeEndpointAsyncInputRequestTypeDef = TypedDict(
    "_OptionalInvokeEndpointAsyncInputRequestTypeDef",
    {
        "ContentType": str,
        "Accept": str,
        "CustomAttributes": str,
        "InferenceId": str,
        "RequestTTLSeconds": int,
        "InvocationTimeoutSeconds": int,
    },
    total=False,
)

class InvokeEndpointAsyncInputRequestTypeDef(
    _RequiredInvokeEndpointAsyncInputRequestTypeDef, _OptionalInvokeEndpointAsyncInputRequestTypeDef
):
    pass

InvokeEndpointAsyncOutputTypeDef = TypedDict(
    "InvokeEndpointAsyncOutputTypeDef",
    {
        "InferenceId": str,
        "OutputLocation": str,
        "FailureLocation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeEndpointInputRequestTypeDef = TypedDict(
    "_RequiredInvokeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalInvokeEndpointInputRequestTypeDef = TypedDict(
    "_OptionalInvokeEndpointInputRequestTypeDef",
    {
        "ContentType": str,
        "Accept": str,
        "CustomAttributes": str,
        "TargetModel": str,
        "TargetVariant": str,
        "TargetContainerHostname": str,
        "InferenceId": str,
        "EnableExplanations": str,
    },
    total=False,
)

class InvokeEndpointInputRequestTypeDef(
    _RequiredInvokeEndpointInputRequestTypeDef, _OptionalInvokeEndpointInputRequestTypeDef
):
    pass

InvokeEndpointOutputTypeDef = TypedDict(
    "InvokeEndpointOutputTypeDef",
    {
        "Body": bytes,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeEndpointWithResponseStreamInputRequestTypeDef = TypedDict(
    "_RequiredInvokeEndpointWithResponseStreamInputRequestTypeDef",
    {
        "EndpointName": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalInvokeEndpointWithResponseStreamInputRequestTypeDef = TypedDict(
    "_OptionalInvokeEndpointWithResponseStreamInputRequestTypeDef",
    {
        "ContentType": str,
        "Accept": str,
        "CustomAttributes": str,
        "TargetVariant": str,
        "TargetContainerHostname": str,
        "InferenceId": str,
    },
    total=False,
)

class InvokeEndpointWithResponseStreamInputRequestTypeDef(
    _RequiredInvokeEndpointWithResponseStreamInputRequestTypeDef,
    _OptionalInvokeEndpointWithResponseStreamInputRequestTypeDef,
):
    pass

InvokeEndpointWithResponseStreamOutputTypeDef = TypedDict(
    "InvokeEndpointWithResponseStreamOutputTypeDef",
    {
        "Body": "ResponseStreamTypeDef",
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelStreamErrorTypeDef = TypedDict(
    "ModelStreamErrorTypeDef",
    {
        "Message": str,
        "ErrorCode": str,
    },
    total=False,
)

PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "Bytes": bytes,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResponseStreamTypeDef = TypedDict(
    "ResponseStreamTypeDef",
    {
        "PayloadPart": "PayloadPartTypeDef",
        "ModelStreamError": "ModelStreamErrorTypeDef",
        "InternalStreamFailure": "InternalStreamFailureTypeDef",
    },
    total=False,
)
