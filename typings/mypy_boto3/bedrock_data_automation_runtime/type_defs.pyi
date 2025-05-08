"""
Type annotations for bedrock-data-automation-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bedrock_data_automation_runtime.type_defs import BlueprintTypeDef

    data: BlueprintTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import AutomationJobStatusType, BlueprintStageType, DataAutomationStageType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlueprintTypeDef",
    "DataAutomationConfigurationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EventBridgeConfigurationTypeDef",
    "GetDataAutomationStatusRequestTypeDef",
    "GetDataAutomationStatusResponseTypeDef",
    "InputConfigurationTypeDef",
    "InvokeDataAutomationAsyncRequestTypeDef",
    "InvokeDataAutomationAsyncResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotificationConfigurationTypeDef",
    "OutputConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
)

class BlueprintTypeDef(TypedDict):
    blueprintArn: str
    version: NotRequired[str]
    stage: NotRequired[BlueprintStageType]

class DataAutomationConfigurationTypeDef(TypedDict):
    dataAutomationProjectArn: str
    stage: NotRequired[DataAutomationStageType]

class EncryptionConfigurationTypeDef(TypedDict):
    kmsKeyId: str
    kmsEncryptionContext: NotRequired[Mapping[str, str]]

class EventBridgeConfigurationTypeDef(TypedDict):
    eventBridgeEnabled: bool

class GetDataAutomationStatusRequestTypeDef(TypedDict):
    invocationArn: str

class OutputConfigurationTypeDef(TypedDict):
    s3Uri: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class InputConfigurationTypeDef(TypedDict):
    s3Uri: str

class TagTypeDef(TypedDict):
    key: str
    value: str

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceARN: str

class UntagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tagKeys: Sequence[str]

class NotificationConfigurationTypeDef(TypedDict):
    eventBridgeConfiguration: EventBridgeConfigurationTypeDef

class GetDataAutomationStatusResponseTypeDef(TypedDict):
    status: AutomationJobStatusType
    errorType: str
    errorMessage: str
    outputConfiguration: OutputConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeDataAutomationAsyncResponseTypeDef(TypedDict):
    invocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class InvokeDataAutomationAsyncRequestTypeDef(TypedDict):
    inputConfiguration: InputConfigurationTypeDef
    outputConfiguration: OutputConfigurationTypeDef
    dataAutomationProfileArn: str
    clientToken: NotRequired[str]
    dataAutomationConfiguration: NotRequired[DataAutomationConfigurationTypeDef]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    notificationConfiguration: NotRequired[NotificationConfigurationTypeDef]
    blueprints: NotRequired[Sequence[BlueprintTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]
