"""
Type annotations for bedrock-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bedrock_runtime.type_defs import ContentBlockDeltaEventTypeDef

    data: ContentBlockDeltaEventTypeDef = {...}
    ```
"""

import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ConversationRoleType,
    ImageFormatType,
    StopReasonType,
    ToolResultStatusType,
    TraceType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ContentBlockDeltaEventTypeDef",
    "ContentBlockDeltaTypeDef",
    "ContentBlockStartEventTypeDef",
    "ContentBlockStartTypeDef",
    "ContentBlockStopEventTypeDef",
    "ContentBlockTypeDef",
    "ConverseMetricsTypeDef",
    "ConverseOutputTypeDef",
    "ConverseRequestRequestTypeDef",
    "ConverseResponseTypeDef",
    "ConverseStreamMetadataEventTypeDef",
    "ConverseStreamMetricsTypeDef",
    "ConverseStreamOutputTypeDef",
    "ConverseStreamRequestRequestTypeDef",
    "ConverseStreamResponseTypeDef",
    "ImageBlockTypeDef",
    "ImageSourceTypeDef",
    "InferenceConfigurationTypeDef",
    "InternalServerExceptionTypeDef",
    "InvokeModelRequestRequestTypeDef",
    "InvokeModelResponseTypeDef",
    "InvokeModelWithResponseStreamRequestRequestTypeDef",
    "InvokeModelWithResponseStreamResponseTypeDef",
    "MessageStartEventTypeDef",
    "MessageStopEventTypeDef",
    "MessageTypeDef",
    "ModelStreamErrorExceptionTypeDef",
    "ModelTimeoutExceptionTypeDef",
    "PayloadPartTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseStreamTypeDef",
    "SpecificToolChoiceTypeDef",
    "SystemContentBlockTypeDef",
    "ThrottlingExceptionTypeDef",
    "TokenUsageTypeDef",
    "ToolChoiceTypeDef",
    "ToolConfigurationTypeDef",
    "ToolInputSchemaTypeDef",
    "ToolResultBlockTypeDef",
    "ToolResultContentBlockTypeDef",
    "ToolSpecificationTypeDef",
    "ToolTypeDef",
    "ToolUseBlockDeltaTypeDef",
    "ToolUseBlockStartTypeDef",
    "ToolUseBlockTypeDef",
    "ValidationExceptionTypeDef",
)

ContentBlockDeltaEventTypeDef = TypedDict(
    "ContentBlockDeltaEventTypeDef",
    {
        "delta": "ContentBlockDeltaTypeDef",
        "contentBlockIndex": int,
    },
)

ContentBlockDeltaTypeDef = TypedDict(
    "ContentBlockDeltaTypeDef",
    {
        "text": str,
        "toolUse": "ToolUseBlockDeltaTypeDef",
    },
    total=False,
)

ContentBlockStartEventTypeDef = TypedDict(
    "ContentBlockStartEventTypeDef",
    {
        "start": "ContentBlockStartTypeDef",
        "contentBlockIndex": int,
    },
)

ContentBlockStartTypeDef = TypedDict(
    "ContentBlockStartTypeDef",
    {
        "toolUse": "ToolUseBlockStartTypeDef",
    },
    total=False,
)

ContentBlockStopEventTypeDef = TypedDict(
    "ContentBlockStopEventTypeDef",
    {
        "contentBlockIndex": int,
    },
)

ContentBlockTypeDef = TypedDict(
    "ContentBlockTypeDef",
    {
        "text": str,
        "image": "ImageBlockTypeDef",
        "toolUse": "ToolUseBlockTypeDef",
        "toolResult": "ToolResultBlockTypeDef",
    },
    total=False,
)

ConverseMetricsTypeDef = TypedDict(
    "ConverseMetricsTypeDef",
    {
        "latencyMs": int,
    },
)

ConverseOutputTypeDef = TypedDict(
    "ConverseOutputTypeDef",
    {
        "message": "MessageTypeDef",
    },
    total=False,
)

_RequiredConverseRequestRequestTypeDef = TypedDict(
    "_RequiredConverseRequestRequestTypeDef",
    {
        "modelId": str,
        "messages": List["MessageTypeDef"],
    },
)
_OptionalConverseRequestRequestTypeDef = TypedDict(
    "_OptionalConverseRequestRequestTypeDef",
    {
        "system": List["SystemContentBlockTypeDef"],
        "inferenceConfig": "InferenceConfigurationTypeDef",
        "toolConfig": "ToolConfigurationTypeDef",
        "additionalModelRequestFields": Dict[str, Any],
        "additionalModelResponseFieldPaths": List[str],
    },
    total=False,
)

class ConverseRequestRequestTypeDef(
    _RequiredConverseRequestRequestTypeDef, _OptionalConverseRequestRequestTypeDef
):
    pass

ConverseResponseTypeDef = TypedDict(
    "ConverseResponseTypeDef",
    {
        "output": "ConverseOutputTypeDef",
        "stopReason": StopReasonType,
        "usage": "TokenUsageTypeDef",
        "metrics": "ConverseMetricsTypeDef",
        "additionalModelResponseFields": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConverseStreamMetadataEventTypeDef = TypedDict(
    "ConverseStreamMetadataEventTypeDef",
    {
        "usage": "TokenUsageTypeDef",
        "metrics": "ConverseStreamMetricsTypeDef",
    },
)

ConverseStreamMetricsTypeDef = TypedDict(
    "ConverseStreamMetricsTypeDef",
    {
        "latencyMs": int,
    },
)

ConverseStreamOutputTypeDef = TypedDict(
    "ConverseStreamOutputTypeDef",
    {
        "messageStart": "MessageStartEventTypeDef",
        "contentBlockStart": "ContentBlockStartEventTypeDef",
        "contentBlockDelta": "ContentBlockDeltaEventTypeDef",
        "contentBlockStop": "ContentBlockStopEventTypeDef",
        "messageStop": "MessageStopEventTypeDef",
        "metadata": "ConverseStreamMetadataEventTypeDef",
        "internalServerException": "InternalServerExceptionTypeDef",
        "modelStreamErrorException": "ModelStreamErrorExceptionTypeDef",
        "validationException": "ValidationExceptionTypeDef",
        "throttlingException": "ThrottlingExceptionTypeDef",
    },
    total=False,
)

_RequiredConverseStreamRequestRequestTypeDef = TypedDict(
    "_RequiredConverseStreamRequestRequestTypeDef",
    {
        "modelId": str,
        "messages": List["MessageTypeDef"],
    },
)
_OptionalConverseStreamRequestRequestTypeDef = TypedDict(
    "_OptionalConverseStreamRequestRequestTypeDef",
    {
        "system": List["SystemContentBlockTypeDef"],
        "inferenceConfig": "InferenceConfigurationTypeDef",
        "toolConfig": "ToolConfigurationTypeDef",
        "additionalModelRequestFields": Dict[str, Any],
        "additionalModelResponseFieldPaths": List[str],
    },
    total=False,
)

class ConverseStreamRequestRequestTypeDef(
    _RequiredConverseStreamRequestRequestTypeDef, _OptionalConverseStreamRequestRequestTypeDef
):
    pass

ConverseStreamResponseTypeDef = TypedDict(
    "ConverseStreamResponseTypeDef",
    {
        "stream": "ConverseStreamOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageBlockTypeDef = TypedDict(
    "ImageBlockTypeDef",
    {
        "format": ImageFormatType,
        "source": "ImageSourceTypeDef",
    },
)

ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "bytes": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

InferenceConfigurationTypeDef = TypedDict(
    "InferenceConfigurationTypeDef",
    {
        "maxTokens": int,
        "temperature": float,
        "topP": float,
        "stopSequences": List[str],
    },
    total=False,
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
        "contentType": str,
        "accept": str,
        "trace": TraceType,
        "guardrailIdentifier": str,
        "guardrailVersion": str,
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
        "contentType": str,
        "accept": str,
        "trace": TraceType,
        "guardrailIdentifier": str,
        "guardrailVersion": str,
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

MessageStartEventTypeDef = TypedDict(
    "MessageStartEventTypeDef",
    {
        "role": ConversationRoleType,
    },
)

_RequiredMessageStopEventTypeDef = TypedDict(
    "_RequiredMessageStopEventTypeDef",
    {
        "stopReason": StopReasonType,
    },
)
_OptionalMessageStopEventTypeDef = TypedDict(
    "_OptionalMessageStopEventTypeDef",
    {
        "additionalModelResponseFields": Dict[str, Any],
    },
    total=False,
)

class MessageStopEventTypeDef(_RequiredMessageStopEventTypeDef, _OptionalMessageStopEventTypeDef):
    pass

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "role": ConversationRoleType,
        "content": List["ContentBlockTypeDef"],
    },
)

ModelStreamErrorExceptionTypeDef = TypedDict(
    "ModelStreamErrorExceptionTypeDef",
    {
        "message": str,
        "originalStatusCode": int,
        "originalMessage": str,
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
        "validationException": "ValidationExceptionTypeDef",
        "throttlingException": "ThrottlingExceptionTypeDef",
        "modelTimeoutException": "ModelTimeoutExceptionTypeDef",
    },
    total=False,
)

SpecificToolChoiceTypeDef = TypedDict(
    "SpecificToolChoiceTypeDef",
    {
        "name": str,
    },
)

SystemContentBlockTypeDef = TypedDict(
    "SystemContentBlockTypeDef",
    {
        "text": str,
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

TokenUsageTypeDef = TypedDict(
    "TokenUsageTypeDef",
    {
        "inputTokens": int,
        "outputTokens": int,
        "totalTokens": int,
    },
)

ToolChoiceTypeDef = TypedDict(
    "ToolChoiceTypeDef",
    {
        "auto": Dict[str, Any],
        "any": Dict[str, Any],
        "tool": "SpecificToolChoiceTypeDef",
    },
    total=False,
)

_RequiredToolConfigurationTypeDef = TypedDict(
    "_RequiredToolConfigurationTypeDef",
    {
        "tools": List["ToolTypeDef"],
    },
)
_OptionalToolConfigurationTypeDef = TypedDict(
    "_OptionalToolConfigurationTypeDef",
    {
        "toolChoice": "ToolChoiceTypeDef",
    },
    total=False,
)

class ToolConfigurationTypeDef(
    _RequiredToolConfigurationTypeDef, _OptionalToolConfigurationTypeDef
):
    pass

ToolInputSchemaTypeDef = TypedDict(
    "ToolInputSchemaTypeDef",
    {
        "json": Dict[str, Any],
    },
    total=False,
)

_RequiredToolResultBlockTypeDef = TypedDict(
    "_RequiredToolResultBlockTypeDef",
    {
        "toolUseId": str,
        "content": List["ToolResultContentBlockTypeDef"],
    },
)
_OptionalToolResultBlockTypeDef = TypedDict(
    "_OptionalToolResultBlockTypeDef",
    {
        "status": ToolResultStatusType,
    },
    total=False,
)

class ToolResultBlockTypeDef(_RequiredToolResultBlockTypeDef, _OptionalToolResultBlockTypeDef):
    pass

ToolResultContentBlockTypeDef = TypedDict(
    "ToolResultContentBlockTypeDef",
    {
        "json": Dict[str, Any],
        "text": str,
        "image": "ImageBlockTypeDef",
    },
    total=False,
)

_RequiredToolSpecificationTypeDef = TypedDict(
    "_RequiredToolSpecificationTypeDef",
    {
        "name": str,
        "inputSchema": "ToolInputSchemaTypeDef",
    },
)
_OptionalToolSpecificationTypeDef = TypedDict(
    "_OptionalToolSpecificationTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ToolSpecificationTypeDef(
    _RequiredToolSpecificationTypeDef, _OptionalToolSpecificationTypeDef
):
    pass

ToolTypeDef = TypedDict(
    "ToolTypeDef",
    {
        "toolSpec": "ToolSpecificationTypeDef",
    },
    total=False,
)

ToolUseBlockDeltaTypeDef = TypedDict(
    "ToolUseBlockDeltaTypeDef",
    {
        "input": str,
    },
)

ToolUseBlockStartTypeDef = TypedDict(
    "ToolUseBlockStartTypeDef",
    {
        "toolUseId": str,
        "name": str,
    },
)

ToolUseBlockTypeDef = TypedDict(
    "ToolUseBlockTypeDef",
    {
        "toolUseId": str,
        "name": str,
        "input": Dict[str, Any],
    },
)

ValidationExceptionTypeDef = TypedDict(
    "ValidationExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)
