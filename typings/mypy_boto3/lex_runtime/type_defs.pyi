"""
Type annotations for lex-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStatusType,
    DialogActionTypeType,
    DialogStateType,
    FulfillmentStateType,
    MessageFormatTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActiveContextOutputTypeDef",
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ActiveContextUnionTypeDef",
    "BlobTypeDef",
    "ButtonTypeDef",
    "DeleteSessionRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionOutputTypeDef",
    "DialogActionTypeDef",
    "DialogActionUnionTypeDef",
    "GenericAttachmentTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "IntentConfidenceTypeDef",
    "IntentSummaryOutputTypeDef",
    "IntentSummaryTypeDef",
    "IntentSummaryUnionTypeDef",
    "PostContentRequestTypeDef",
    "PostContentResponseTypeDef",
    "PostTextRequestTypeDef",
    "PostTextResponseTypeDef",
    "PredictedIntentTypeDef",
    "PutSessionRequestTypeDef",
    "PutSessionResponseTypeDef",
    "ResponseCardTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentResponseTypeDef",
)

class ActiveContextTimeToLiveTypeDef(TypedDict):
    timeToLiveInSeconds: NotRequired[int]
    turnsToLive: NotRequired[int]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ButtonTypeDef(TypedDict):
    text: str
    value: str

class DeleteSessionRequestTypeDef(TypedDict):
    botName: str
    botAlias: str
    userId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DialogActionOutputTypeDef = TypedDict(
    "DialogActionOutputTypeDef",
    {
        "type": DialogActionTypeType,
        "intentName": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "slotToElicit": NotRequired[str],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "message": NotRequired[str],
        "messageFormat": NotRequired[MessageFormatTypeType],
    },
)
DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "intentName": NotRequired[str],
        "slots": NotRequired[Mapping[str, str]],
        "slotToElicit": NotRequired[str],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "message": NotRequired[str],
        "messageFormat": NotRequired[MessageFormatTypeType],
    },
)

class GetSessionRequestTypeDef(TypedDict):
    botName: str
    botAlias: str
    userId: str
    checkpointLabelFilter: NotRequired[str]

class IntentSummaryOutputTypeDef(TypedDict):
    dialogActionType: DialogActionTypeType
    intentName: NotRequired[str]
    checkpointLabel: NotRequired[str]
    slots: NotRequired[Dict[str, str]]
    confirmationStatus: NotRequired[ConfirmationStatusType]
    fulfillmentState: NotRequired[FulfillmentStateType]
    slotToElicit: NotRequired[str]

class IntentConfidenceTypeDef(TypedDict):
    score: NotRequired[float]

class IntentSummaryTypeDef(TypedDict):
    dialogActionType: DialogActionTypeType
    intentName: NotRequired[str]
    checkpointLabel: NotRequired[str]
    slots: NotRequired[Mapping[str, str]]
    confirmationStatus: NotRequired[ConfirmationStatusType]
    fulfillmentState: NotRequired[FulfillmentStateType]
    slotToElicit: NotRequired[str]

class SentimentResponseTypeDef(TypedDict):
    sentimentLabel: NotRequired[str]
    sentimentScore: NotRequired[str]

class ActiveContextOutputTypeDef(TypedDict):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    parameters: Dict[str, str]

class ActiveContextTypeDef(TypedDict):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    parameters: Mapping[str, str]

class PostContentRequestTypeDef(TypedDict):
    botName: str
    botAlias: str
    userId: str
    contentType: str
    inputStream: BlobTypeDef
    sessionAttributes: NotRequired[str]
    requestAttributes: NotRequired[str]
    accept: NotRequired[str]
    activeContexts: NotRequired[str]

class GenericAttachmentTypeDef(TypedDict):
    title: NotRequired[str]
    subTitle: NotRequired[str]
    attachmentLinkUrl: NotRequired[str]
    imageUrl: NotRequired[str]
    buttons: NotRequired[List[ButtonTypeDef]]

class DeleteSessionResponseTypeDef(TypedDict):
    botName: str
    botAlias: str
    userId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PostContentResponseTypeDef(TypedDict):
    contentType: str
    intentName: str
    nluIntentConfidence: str
    alternativeIntents: str
    slots: str
    sessionAttributes: str
    sentimentResponse: str
    message: str
    encodedMessage: str
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    inputTranscript: str
    encodedInputTranscript: str
    audioStream: StreamingBody
    botVersion: str
    sessionId: str
    activeContexts: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSessionResponseTypeDef(TypedDict):
    contentType: str
    intentName: str
    slots: str
    sessionAttributes: str
    message: str
    encodedMessage: str
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    audioStream: StreamingBody
    sessionId: str
    activeContexts: str
    ResponseMetadata: ResponseMetadataTypeDef

DialogActionUnionTypeDef = Union[DialogActionTypeDef, DialogActionOutputTypeDef]

class PredictedIntentTypeDef(TypedDict):
    intentName: NotRequired[str]
    nluIntentConfidence: NotRequired[IntentConfidenceTypeDef]
    slots: NotRequired[Dict[str, str]]

IntentSummaryUnionTypeDef = Union[IntentSummaryTypeDef, IntentSummaryOutputTypeDef]

class GetSessionResponseTypeDef(TypedDict):
    recentIntentSummaryView: List[IntentSummaryOutputTypeDef]
    sessionAttributes: Dict[str, str]
    sessionId: str
    dialogAction: DialogActionOutputTypeDef
    activeContexts: List[ActiveContextOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ActiveContextUnionTypeDef = Union[ActiveContextTypeDef, ActiveContextOutputTypeDef]

class ResponseCardTypeDef(TypedDict):
    version: NotRequired[str]
    contentType: NotRequired[Literal["application/vnd.amazonaws.card.generic"]]
    genericAttachments: NotRequired[List[GenericAttachmentTypeDef]]

class PostTextRequestTypeDef(TypedDict):
    botName: str
    botAlias: str
    userId: str
    inputText: str
    sessionAttributes: NotRequired[Mapping[str, str]]
    requestAttributes: NotRequired[Mapping[str, str]]
    activeContexts: NotRequired[Sequence[ActiveContextUnionTypeDef]]

class PutSessionRequestTypeDef(TypedDict):
    botName: str
    botAlias: str
    userId: str
    sessionAttributes: NotRequired[Mapping[str, str]]
    dialogAction: NotRequired[DialogActionUnionTypeDef]
    recentIntentSummaryView: NotRequired[Sequence[IntentSummaryUnionTypeDef]]
    accept: NotRequired[str]
    activeContexts: NotRequired[Sequence[ActiveContextUnionTypeDef]]

class PostTextResponseTypeDef(TypedDict):
    intentName: str
    nluIntentConfidence: IntentConfidenceTypeDef
    alternativeIntents: List[PredictedIntentTypeDef]
    slots: Dict[str, str]
    sessionAttributes: Dict[str, str]
    message: str
    sentimentResponse: SentimentResponseTypeDef
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    responseCard: ResponseCardTypeDef
    sessionId: str
    botVersion: str
    activeContexts: List[ActiveContextOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
