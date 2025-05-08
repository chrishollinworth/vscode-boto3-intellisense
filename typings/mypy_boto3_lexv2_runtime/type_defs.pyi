"""
Type annotations for lexv2-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.type_defs import AccessDeniedExceptionTypeDef

    data: AccessDeniedExceptionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    ConfirmationStateType,
    ConversationModeType,
    DialogActionTypeType,
    InputModeType,
    IntentStateType,
    InterpretationSourceType,
    MessageContentTypeType,
    PlaybackInterruptionReasonType,
    SentimentTypeType,
    ShapeType,
    StyleTypeType,
)

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
    "AccessDeniedExceptionTypeDef",
    "ActiveContextOutputTypeDef",
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ActiveContextUnionTypeDef",
    "AudioInputEventTypeDef",
    "AudioResponseEventTypeDef",
    "BadGatewayExceptionTypeDef",
    "BlobTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "ConfigurationEventTypeDef",
    "ConflictExceptionTypeDef",
    "DTMFInputEventTypeDef",
    "DeleteSessionRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DependencyFailedExceptionTypeDef",
    "DialogActionOutputTypeDef",
    "DialogActionTypeDef",
    "DialogActionUnionTypeDef",
    "DisconnectionEventTypeDef",
    "ElicitSubSlotOutputTypeDef",
    "ElicitSubSlotTypeDef",
    "ElicitSubSlotUnionTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "HeartbeatEventTypeDef",
    "ImageResponseCardOutputTypeDef",
    "ImageResponseCardTypeDef",
    "ImageResponseCardUnionTypeDef",
    "IntentOutputTypeDef",
    "IntentResultEventTypeDef",
    "IntentTypeDef",
    "IntentUnionTypeDef",
    "InternalServerExceptionTypeDef",
    "InterpretationTypeDef",
    "MessageOutputTypeDef",
    "MessageTypeDef",
    "MessageUnionTypeDef",
    "PlaybackCompletionEventTypeDef",
    "PlaybackInterruptionEventTypeDef",
    "PutSessionRequestTypeDef",
    "PutSessionResponseTypeDef",
    "RecognizeTextRequestTypeDef",
    "RecognizeTextResponseTypeDef",
    "RecognizeUtteranceRequestTypeDef",
    "RecognizeUtteranceResponseTypeDef",
    "RecognizedBotMemberTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeHintDetailsOutputTypeDef",
    "RuntimeHintDetailsTypeDef",
    "RuntimeHintDetailsUnionTypeDef",
    "RuntimeHintValueTypeDef",
    "RuntimeHintsOutputTypeDef",
    "RuntimeHintsTypeDef",
    "RuntimeHintsUnionTypeDef",
    "SentimentResponseTypeDef",
    "SentimentScoreTypeDef",
    "SessionStateOutputTypeDef",
    "SessionStateTypeDef",
    "SessionStateUnionTypeDef",
    "SlotOutputTypeDef",
    "SlotTypeDef",
    "SlotUnionTypeDef",
    "StartConversationRequestEventStreamTypeDef",
    "StartConversationRequestTypeDef",
    "StartConversationResponseEventStreamTypeDef",
    "StartConversationResponseTypeDef",
    "TextInputEventTypeDef",
    "TextResponseEventTypeDef",
    "ThrottlingExceptionTypeDef",
    "TranscriptEventTypeDef",
    "ValidationExceptionTypeDef",
    "ValueOutputTypeDef",
    "ValueTypeDef",
    "ValueUnionTypeDef",
)

class AccessDeniedExceptionTypeDef(TypedDict):
    message: str

class ActiveContextTimeToLiveTypeDef(TypedDict):
    timeToLiveInSeconds: int
    turnsToLive: int

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class AudioResponseEventTypeDef(TypedDict):
    audioChunk: NotRequired[bytes]
    contentType: NotRequired[str]
    eventId: NotRequired[str]

class BadGatewayExceptionTypeDef(TypedDict):
    message: str

class ButtonTypeDef(TypedDict):
    text: str
    value: str

class ConfidenceScoreTypeDef(TypedDict):
    score: NotRequired[float]

class ConflictExceptionTypeDef(TypedDict):
    message: str

class DTMFInputEventTypeDef(TypedDict):
    inputCharacter: str
    eventId: NotRequired[str]
    clientTimestampMillis: NotRequired[int]

class DeleteSessionRequestTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DependencyFailedExceptionTypeDef(TypedDict):
    message: str

class ElicitSubSlotOutputTypeDef(TypedDict):
    name: str
    subSlotToElicit: NotRequired[Dict[str, Any]]

class DisconnectionEventTypeDef(TypedDict):
    eventId: NotRequired[str]
    clientTimestampMillis: NotRequired[int]

class ElicitSubSlotTypeDef(TypedDict):
    name: str
    subSlotToElicit: NotRequired[Mapping[str, Any]]

class GetSessionRequestTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str

class HeartbeatEventTypeDef(TypedDict):
    eventId: NotRequired[str]

class RecognizedBotMemberTypeDef(TypedDict):
    botId: str
    botName: NotRequired[str]

class InternalServerExceptionTypeDef(TypedDict):
    message: str

class PlaybackCompletionEventTypeDef(TypedDict):
    eventId: NotRequired[str]
    clientTimestampMillis: NotRequired[int]

class PlaybackInterruptionEventTypeDef(TypedDict):
    eventReason: NotRequired[PlaybackInterruptionReasonType]
    causedByEventId: NotRequired[str]
    eventId: NotRequired[str]

class ResourceNotFoundExceptionTypeDef(TypedDict):
    message: str

class RuntimeHintValueTypeDef(TypedDict):
    phrase: str

class SentimentScoreTypeDef(TypedDict):
    positive: NotRequired[float]
    negative: NotRequired[float]
    neutral: NotRequired[float]
    mixed: NotRequired[float]

class ValueOutputTypeDef(TypedDict):
    interpretedValue: str
    originalValue: NotRequired[str]
    resolvedValues: NotRequired[List[str]]

class TextInputEventTypeDef(TypedDict):
    text: str
    eventId: NotRequired[str]
    clientTimestampMillis: NotRequired[int]

class ThrottlingExceptionTypeDef(TypedDict):
    message: str

class TranscriptEventTypeDef(TypedDict):
    transcript: NotRequired[str]
    eventId: NotRequired[str]

class ValidationExceptionTypeDef(TypedDict):
    message: str

class ValueTypeDef(TypedDict):
    interpretedValue: str
    originalValue: NotRequired[str]
    resolvedValues: NotRequired[Sequence[str]]

class ActiveContextOutputTypeDef(TypedDict):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    contextAttributes: Dict[str, str]

class ActiveContextTypeDef(TypedDict):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    contextAttributes: Mapping[str, str]

class AudioInputEventTypeDef(TypedDict):
    contentType: str
    audioChunk: NotRequired[BlobTypeDef]
    eventId: NotRequired[str]
    clientTimestampMillis: NotRequired[int]

class RecognizeUtteranceRequestTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestContentType: str
    sessionState: NotRequired[str]
    requestAttributes: NotRequired[str]
    responseContentType: NotRequired[str]
    inputStream: NotRequired[BlobTypeDef]

class ImageResponseCardOutputTypeDef(TypedDict):
    title: str
    subtitle: NotRequired[str]
    imageUrl: NotRequired[str]
    buttons: NotRequired[List[ButtonTypeDef]]

class ImageResponseCardTypeDef(TypedDict):
    title: str
    subtitle: NotRequired[str]
    imageUrl: NotRequired[str]
    buttons: NotRequired[Sequence[ButtonTypeDef]]

class DeleteSessionResponseTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSessionResponseTypeDef(TypedDict):
    contentType: str
    messages: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    audioStream: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class RecognizeUtteranceResponseTypeDef(TypedDict):
    inputMode: str
    contentType: str
    messages: str
    interpretations: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    inputTranscript: str
    audioStream: StreamingBody
    recognizedBotMember: str
    ResponseMetadata: ResponseMetadataTypeDef

DialogActionOutputTypeDef = TypedDict(
    "DialogActionOutputTypeDef",
    {
        "type": DialogActionTypeType,
        "slotToElicit": NotRequired[str],
        "slotElicitationStyle": NotRequired[StyleTypeType],
        "subSlotToElicit": NotRequired[ElicitSubSlotOutputTypeDef],
    },
)
ElicitSubSlotUnionTypeDef = Union[ElicitSubSlotTypeDef, ElicitSubSlotOutputTypeDef]

class RuntimeHintDetailsOutputTypeDef(TypedDict):
    runtimeHintValues: NotRequired[List[RuntimeHintValueTypeDef]]
    subSlotHints: NotRequired[Dict[str, Dict[str, Any]]]

class RuntimeHintDetailsTypeDef(TypedDict):
    runtimeHintValues: NotRequired[Sequence[RuntimeHintValueTypeDef]]
    subSlotHints: NotRequired[Mapping[str, Mapping[str, Any]]]

class SentimentResponseTypeDef(TypedDict):
    sentiment: NotRequired[SentimentTypeType]
    sentimentScore: NotRequired[SentimentScoreTypeDef]

class SlotOutputTypeDef(TypedDict):
    value: NotRequired[ValueOutputTypeDef]
    shape: NotRequired[ShapeType]
    values: NotRequired[List[Dict[str, Any]]]
    subSlots: NotRequired[Dict[str, Dict[str, Any]]]

ValueUnionTypeDef = Union[ValueTypeDef, ValueOutputTypeDef]
ActiveContextUnionTypeDef = Union[ActiveContextTypeDef, ActiveContextOutputTypeDef]

class MessageOutputTypeDef(TypedDict):
    contentType: MessageContentTypeType
    content: NotRequired[str]
    imageResponseCard: NotRequired[ImageResponseCardOutputTypeDef]

ImageResponseCardUnionTypeDef = Union[ImageResponseCardTypeDef, ImageResponseCardOutputTypeDef]
DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "slotToElicit": NotRequired[str],
        "slotElicitationStyle": NotRequired[StyleTypeType],
        "subSlotToElicit": NotRequired[ElicitSubSlotUnionTypeDef],
    },
)

class RuntimeHintsOutputTypeDef(TypedDict):
    slotHints: NotRequired[Dict[str, Dict[str, RuntimeHintDetailsOutputTypeDef]]]

RuntimeHintDetailsUnionTypeDef = Union[RuntimeHintDetailsTypeDef, RuntimeHintDetailsOutputTypeDef]

class IntentOutputTypeDef(TypedDict):
    name: str
    slots: NotRequired[Dict[str, SlotOutputTypeDef]]
    state: NotRequired[IntentStateType]
    confirmationState: NotRequired[ConfirmationStateType]

class SlotTypeDef(TypedDict):
    value: NotRequired[ValueUnionTypeDef]
    shape: NotRequired[ShapeType]
    values: NotRequired[Sequence[Mapping[str, Any]]]
    subSlots: NotRequired[Mapping[str, Mapping[str, Any]]]

class TextResponseEventTypeDef(TypedDict):
    messages: NotRequired[List[MessageOutputTypeDef]]
    eventId: NotRequired[str]

class MessageTypeDef(TypedDict):
    contentType: MessageContentTypeType
    content: NotRequired[str]
    imageResponseCard: NotRequired[ImageResponseCardUnionTypeDef]

DialogActionUnionTypeDef = Union[DialogActionTypeDef, DialogActionOutputTypeDef]

class RuntimeHintsTypeDef(TypedDict):
    slotHints: NotRequired[Mapping[str, Mapping[str, RuntimeHintDetailsUnionTypeDef]]]

class InterpretationTypeDef(TypedDict):
    nluConfidence: NotRequired[ConfidenceScoreTypeDef]
    sentimentResponse: NotRequired[SentimentResponseTypeDef]
    intent: NotRequired[IntentOutputTypeDef]
    interpretationSource: NotRequired[InterpretationSourceType]

class SessionStateOutputTypeDef(TypedDict):
    dialogAction: NotRequired[DialogActionOutputTypeDef]
    intent: NotRequired[IntentOutputTypeDef]
    activeContexts: NotRequired[List[ActiveContextOutputTypeDef]]
    sessionAttributes: NotRequired[Dict[str, str]]
    originatingRequestId: NotRequired[str]
    runtimeHints: NotRequired[RuntimeHintsOutputTypeDef]

SlotUnionTypeDef = Union[SlotTypeDef, SlotOutputTypeDef]
MessageUnionTypeDef = Union[MessageTypeDef, MessageOutputTypeDef]
RuntimeHintsUnionTypeDef = Union[RuntimeHintsTypeDef, RuntimeHintsOutputTypeDef]

class GetSessionResponseTypeDef(TypedDict):
    sessionId: str
    messages: List[MessageOutputTypeDef]
    interpretations: List[InterpretationTypeDef]
    sessionState: SessionStateOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntentResultEventTypeDef(TypedDict):
    inputMode: NotRequired[InputModeType]
    interpretations: NotRequired[List[InterpretationTypeDef]]
    sessionState: NotRequired[SessionStateOutputTypeDef]
    requestAttributes: NotRequired[Dict[str, str]]
    sessionId: NotRequired[str]
    eventId: NotRequired[str]
    recognizedBotMember: NotRequired[RecognizedBotMemberTypeDef]

class RecognizeTextResponseTypeDef(TypedDict):
    messages: List[MessageOutputTypeDef]
    sessionState: SessionStateOutputTypeDef
    interpretations: List[InterpretationTypeDef]
    requestAttributes: Dict[str, str]
    sessionId: str
    recognizedBotMember: RecognizedBotMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntentTypeDef(TypedDict):
    name: str
    slots: NotRequired[Mapping[str, SlotUnionTypeDef]]
    state: NotRequired[IntentStateType]
    confirmationState: NotRequired[ConfirmationStateType]

class StartConversationResponseEventStreamTypeDef(TypedDict):
    PlaybackInterruptionEvent: NotRequired[PlaybackInterruptionEventTypeDef]
    TranscriptEvent: NotRequired[TranscriptEventTypeDef]
    IntentResultEvent: NotRequired[IntentResultEventTypeDef]
    TextResponseEvent: NotRequired[TextResponseEventTypeDef]
    AudioResponseEvent: NotRequired[AudioResponseEventTypeDef]
    HeartbeatEvent: NotRequired[HeartbeatEventTypeDef]
    AccessDeniedException: NotRequired[AccessDeniedExceptionTypeDef]
    ResourceNotFoundException: NotRequired[ResourceNotFoundExceptionTypeDef]
    ValidationException: NotRequired[ValidationExceptionTypeDef]
    ThrottlingException: NotRequired[ThrottlingExceptionTypeDef]
    InternalServerException: NotRequired[InternalServerExceptionTypeDef]
    ConflictException: NotRequired[ConflictExceptionTypeDef]
    DependencyFailedException: NotRequired[DependencyFailedExceptionTypeDef]
    BadGatewayException: NotRequired[BadGatewayExceptionTypeDef]

IntentUnionTypeDef = Union[IntentTypeDef, IntentOutputTypeDef]

class StartConversationResponseTypeDef(TypedDict):
    responseEventStream: EventStream[StartConversationResponseEventStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SessionStateTypeDef(TypedDict):
    dialogAction: NotRequired[DialogActionUnionTypeDef]
    intent: NotRequired[IntentUnionTypeDef]
    activeContexts: NotRequired[Sequence[ActiveContextUnionTypeDef]]
    sessionAttributes: NotRequired[Mapping[str, str]]
    originatingRequestId: NotRequired[str]
    runtimeHints: NotRequired[RuntimeHintsUnionTypeDef]

SessionStateUnionTypeDef = Union[SessionStateTypeDef, SessionStateOutputTypeDef]

class ConfigurationEventTypeDef(TypedDict):
    responseContentType: str
    requestAttributes: NotRequired[Mapping[str, str]]
    sessionState: NotRequired[SessionStateUnionTypeDef]
    welcomeMessages: NotRequired[Sequence[MessageUnionTypeDef]]
    disablePlayback: NotRequired[bool]
    eventId: NotRequired[str]
    clientTimestampMillis: NotRequired[int]

class PutSessionRequestTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    sessionState: SessionStateUnionTypeDef
    messages: NotRequired[Sequence[MessageUnionTypeDef]]
    requestAttributes: NotRequired[Mapping[str, str]]
    responseContentType: NotRequired[str]

class RecognizeTextRequestTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    text: str
    sessionState: NotRequired[SessionStateUnionTypeDef]
    requestAttributes: NotRequired[Mapping[str, str]]

class StartConversationRequestEventStreamTypeDef(TypedDict):
    ConfigurationEvent: NotRequired[ConfigurationEventTypeDef]
    AudioInputEvent: NotRequired[AudioInputEventTypeDef]
    DTMFInputEvent: NotRequired[DTMFInputEventTypeDef]
    TextInputEvent: NotRequired[TextInputEventTypeDef]
    PlaybackCompletionEvent: NotRequired[PlaybackCompletionEventTypeDef]
    DisconnectionEvent: NotRequired[DisconnectionEventTypeDef]

class StartConversationRequestTypeDef(TypedDict):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestEventStream: EventStream[StartConversationRequestEventStreamTypeDef]
    conversationMode: NotRequired[ConversationModeType]
