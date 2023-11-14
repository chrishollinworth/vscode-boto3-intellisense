"""
Type annotations for bedrock-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bedrock_runtime.type_defs import InternalServerExceptionTypeDef

    data: InternalServerExceptionTypeDef = {...}
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
    "InternalServerExceptionTypeDef",
    "InvokeModelRequestRequestTypeDef",
    "InvokeModelResponseTypeDef",
    "InvokeModelWithResponseStreamRequestRequestTypeDef",
    "InvokeModelWithResponseStreamResponseTypeDef",
    "ModelStreamErrorExceptionTypeDef",
    "ModelTimeoutExceptionTypeDef",
    "PayloadPartTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseStreamTypeDef",
    "ThrottlingExceptionTypeDef",
    "ValidationExceptionTypeDef",
)

InternalServerExceptionTypeDef = TypedDict(
    "InternalServerExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

_RequiredInvokeModelRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeModelRequestRequestTypeDef",
    {
        "body": Union[bytes, IO[bytes], StreamingBody],
        "modelId": str,
    },
)
_OptionalInvokeModelRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeModelRequestRequestTypeDef",
    {
        "accept": str,
        "contentType": str,
    },
    total=False,
)

class InvokeModelRequestRequestTypeDef(
    _RequiredInvokeModelRequestRequestTypeDef, _OptionalInvokeModelRequestRequestTypeDef
):
    pass

InvokeModelResponseTypeDef = TypedDict(
    "InvokeModelResponseTypeDef",
    {
        "body": bytes,
        "contentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeModelWithResponseStreamRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeModelWithResponseStreamRequestRequestTypeDef",
    {
        "body": Union[bytes, IO[bytes], StreamingBody],
        "modelId": str,
    },
)
_OptionalInvokeModelWithResponseStreamRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeModelWithResponseStreamRequestRequestTypeDef",
    {
        "accept": str,
        "contentType": str,
    },
    total=False,
)

class InvokeModelWithResponseStreamRequestRequestTypeDef(
    _RequiredInvokeModelWithResponseStreamRequestRequestTypeDef,
    _OptionalInvokeModelWithResponseStreamRequestRequestTypeDef,
):
    pass

InvokeModelWithResponseStreamResponseTypeDef = TypedDict(
    "InvokeModelWithResponseStreamResponseTypeDef",
    {
        "body": "ResponseStreamTypeDef",
        "contentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelStreamErrorExceptionTypeDef = TypedDict(
    "ModelStreamErrorExceptionTypeDef",
    {
        "message": str,
        "originalMessage": str,
        "originalStatusCode": int,
    },
    total=False,
)

ModelTimeoutExceptionTypeDef = TypedDict(
    "ModelTimeoutExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "bytes": bytes,
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
        "chunk": "PayloadPartTypeDef",
        "internalServerException": "InternalServerExceptionTypeDef",
        "modelStreamErrorException": "ModelStreamErrorExceptionTypeDef",
        "modelTimeoutException": "ModelTimeoutExceptionTypeDef",
        "throttlingException": "ThrottlingExceptionTypeDef",
        "validationException": "ValidationExceptionTypeDef",
    },
    total=False,
)

ThrottlingExceptionTypeDef = TypedDict(
    "ThrottlingExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ValidationExceptionTypeDef = TypedDict(
    "ValidationExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)
