"""
Type annotations for bedrock-agentcore service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bedrock_agentcore.type_defs import AccessDeniedExceptionTypeDef

    data: AccessDeniedExceptionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    AutomationStreamStatusType,
    BrowserSessionStatusType,
    CodeInterpreterSessionStatusType,
    ContentBlockTypeType,
    MemoryRecordStatusType,
    Oauth2FlowTypeType,
    OperatorTypeType,
    ProgrammingLanguageType,
    ResourceContentTypeType,
    RoleType,
    SessionStatusType,
    TaskStatusType,
    ToolNameType,
    ValidationExceptionReasonType,
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
    "AccessDeniedExceptionTypeDef",
    "ActorSummaryTypeDef",
    "AutomationStreamTypeDef",
    "AutomationStreamUpdateTypeDef",
    "BatchCreateMemoryRecordsInputTypeDef",
    "BatchCreateMemoryRecordsOutputTypeDef",
    "BatchDeleteMemoryRecordsInputTypeDef",
    "BatchDeleteMemoryRecordsOutputTypeDef",
    "BatchUpdateMemoryRecordsInputTypeDef",
    "BatchUpdateMemoryRecordsOutputTypeDef",
    "BlobTypeDef",
    "BranchFilterTypeDef",
    "BranchTypeDef",
    "BrowserSessionStreamTypeDef",
    "BrowserSessionSummaryTypeDef",
    "CodeInterpreterResultTypeDef",
    "CodeInterpreterSessionSummaryTypeDef",
    "CodeInterpreterStreamOutputTypeDef",
    "CompleteResourceTokenAuthRequestTypeDef",
    "ConflictExceptionTypeDef",
    "ContentBlockTypeDef",
    "ContentTypeDef",
    "ContextTypeDef",
    "ConversationalTypeDef",
    "CreateEventInputTypeDef",
    "CreateEventOutputTypeDef",
    "DeleteEventInputTypeDef",
    "DeleteEventOutputTypeDef",
    "DeleteMemoryRecordInputTypeDef",
    "DeleteMemoryRecordOutputTypeDef",
    "EvaluateRequestTypeDef",
    "EvaluateResponseTypeDef",
    "EvaluationInputTypeDef",
    "EvaluationResultContentTypeDef",
    "EvaluationTargetTypeDef",
    "EventMetadataFilterExpressionTypeDef",
    "EventTypeDef",
    "ExtractionJobFilterInputTypeDef",
    "ExtractionJobMessagesTypeDef",
    "ExtractionJobMetadataTypeDef",
    "ExtractionJobTypeDef",
    "FilterInputTypeDef",
    "GetAgentCardRequestTypeDef",
    "GetAgentCardResponseTypeDef",
    "GetBrowserSessionRequestTypeDef",
    "GetBrowserSessionResponseTypeDef",
    "GetCodeInterpreterSessionRequestTypeDef",
    "GetCodeInterpreterSessionResponseTypeDef",
    "GetEventInputTypeDef",
    "GetEventOutputTypeDef",
    "GetMemoryRecordInputTypeDef",
    "GetMemoryRecordOutputTypeDef",
    "GetResourceApiKeyRequestTypeDef",
    "GetResourceApiKeyResponseTypeDef",
    "GetResourceOauth2TokenRequestTypeDef",
    "GetResourceOauth2TokenResponseTypeDef",
    "GetWorkloadAccessTokenForJWTRequestTypeDef",
    "GetWorkloadAccessTokenForJWTResponseTypeDef",
    "GetWorkloadAccessTokenForUserIdRequestTypeDef",
    "GetWorkloadAccessTokenForUserIdResponseTypeDef",
    "GetWorkloadAccessTokenRequestTypeDef",
    "GetWorkloadAccessTokenResponseTypeDef",
    "InputContentBlockTypeDef",
    "InternalServerExceptionTypeDef",
    "InvokeAgentRuntimeRequestTypeDef",
    "InvokeAgentRuntimeResponseTypeDef",
    "InvokeCodeInterpreterRequestTypeDef",
    "InvokeCodeInterpreterResponseTypeDef",
    "LeftExpressionTypeDef",
    "ListActorsInputPaginateTypeDef",
    "ListActorsInputTypeDef",
    "ListActorsOutputTypeDef",
    "ListBrowserSessionsRequestTypeDef",
    "ListBrowserSessionsResponseTypeDef",
    "ListCodeInterpreterSessionsRequestTypeDef",
    "ListCodeInterpreterSessionsResponseTypeDef",
    "ListEventsInputPaginateTypeDef",
    "ListEventsInputTypeDef",
    "ListEventsOutputTypeDef",
    "ListMemoryExtractionJobsInputPaginateTypeDef",
    "ListMemoryExtractionJobsInputTypeDef",
    "ListMemoryExtractionJobsOutputTypeDef",
    "ListMemoryRecordsInputPaginateTypeDef",
    "ListMemoryRecordsInputTypeDef",
    "ListMemoryRecordsOutputTypeDef",
    "ListSessionsInputPaginateTypeDef",
    "ListSessionsInputTypeDef",
    "ListSessionsOutputTypeDef",
    "LiveViewStreamTypeDef",
    "MemoryContentTypeDef",
    "MemoryMetadataFilterExpressionTypeDef",
    "MemoryRecordCreateInputTypeDef",
    "MemoryRecordDeleteInputTypeDef",
    "MemoryRecordOutputTypeDef",
    "MemoryRecordSummaryTypeDef",
    "MemoryRecordTypeDef",
    "MemoryRecordUpdateInputTypeDef",
    "MessageMetadataTypeDef",
    "MetadataValueTypeDef",
    "PaginatorConfigTypeDef",
    "PayloadTypeOutputTypeDef",
    "PayloadTypeTypeDef",
    "PayloadTypeUnionTypeDef",
    "ResourceContentTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveMemoryRecordsInputPaginateTypeDef",
    "RetrieveMemoryRecordsInputTypeDef",
    "RetrieveMemoryRecordsOutputTypeDef",
    "RightExpressionTypeDef",
    "SearchCriteriaTypeDef",
    "ServiceQuotaExceededExceptionTypeDef",
    "SessionSummaryTypeDef",
    "SpanContextTypeDef",
    "StartBrowserSessionRequestTypeDef",
    "StartBrowserSessionResponseTypeDef",
    "StartCodeInterpreterSessionRequestTypeDef",
    "StartCodeInterpreterSessionResponseTypeDef",
    "StartMemoryExtractionJobInputTypeDef",
    "StartMemoryExtractionJobOutputTypeDef",
    "StopBrowserSessionRequestTypeDef",
    "StopBrowserSessionResponseTypeDef",
    "StopCodeInterpreterSessionRequestTypeDef",
    "StopCodeInterpreterSessionResponseTypeDef",
    "StopRuntimeSessionRequestTypeDef",
    "StopRuntimeSessionResponseTypeDef",
    "StreamUpdateTypeDef",
    "ThrottlingExceptionTypeDef",
    "TimestampTypeDef",
    "TokenUsageTypeDef",
    "ToolArgumentsTypeDef",
    "ToolResultStructuredContentTypeDef",
    "UpdateBrowserStreamRequestTypeDef",
    "UpdateBrowserStreamResponseTypeDef",
    "UserIdentifierTypeDef",
    "ValidationExceptionFieldTypeDef",
    "ValidationExceptionTypeDef",
    "ViewPortTypeDef",
)

class AccessDeniedExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class ActorSummaryTypeDef(TypedDict):
    actorId: str

class AutomationStreamTypeDef(TypedDict):
    streamEndpoint: str
    streamStatus: AutomationStreamStatusType

class AutomationStreamUpdateTypeDef(TypedDict):
    streamStatus: NotRequired[AutomationStreamStatusType]

class MemoryRecordOutputTypeDef(TypedDict):
    memoryRecordId: str
    status: MemoryRecordStatusType
    requestIdentifier: NotRequired[str]
    errorCode: NotRequired[int]
    errorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class MemoryRecordDeleteInputTypeDef(TypedDict):
    memoryRecordId: str

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BranchFilterTypeDef(TypedDict):
    name: str
    includeParentBranches: NotRequired[bool]

class BranchTypeDef(TypedDict):
    name: str
    rootEventId: NotRequired[str]

class LiveViewStreamTypeDef(TypedDict):
    streamEndpoint: NotRequired[str]

class BrowserSessionSummaryTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    status: BrowserSessionStatusType
    createdAt: datetime
    name: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]

class ToolResultStructuredContentTypeDef(TypedDict):
    taskId: NotRequired[str]
    taskStatus: NotRequired[TaskStatusType]
    stdout: NotRequired[str]
    stderr: NotRequired[str]
    exitCode: NotRequired[int]
    executionTime: NotRequired[float]

class CodeInterpreterSessionSummaryTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    sessionId: str
    status: CodeInterpreterSessionStatusType
    createdAt: datetime
    name: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]

class ConflictExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class InternalServerExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class ResourceNotFoundExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class ServiceQuotaExceededExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class ThrottlingExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class UserIdentifierTypeDef(TypedDict):
    userToken: NotRequired[str]
    userId: NotRequired[str]

ResourceContentTypeDef = TypedDict(
    "ResourceContentTypeDef",
    {
        "type": ResourceContentTypeType,
        "uri": NotRequired[str],
        "mimeType": NotRequired[str],
        "text": NotRequired[str],
        "blob": NotRequired[bytes],
    },
)

class ContentTypeDef(TypedDict):
    text: NotRequired[str]

class SpanContextTypeDef(TypedDict):
    sessionId: str
    traceId: NotRequired[str]
    spanId: NotRequired[str]

class MetadataValueTypeDef(TypedDict):
    stringValue: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DeleteEventInputTypeDef(TypedDict):
    memoryId: str
    sessionId: str
    eventId: str
    actorId: str

class DeleteMemoryRecordInputTypeDef(TypedDict):
    memoryId: str
    memoryRecordId: str

class EvaluationInputTypeDef(TypedDict):
    sessionSpans: NotRequired[Sequence[Mapping[str, Any]]]

class EvaluationTargetTypeDef(TypedDict):
    spanIds: NotRequired[Sequence[str]]
    traceIds: NotRequired[Sequence[str]]

class TokenUsageTypeDef(TypedDict):
    inputTokens: NotRequired[int]
    outputTokens: NotRequired[int]
    totalTokens: NotRequired[int]

class LeftExpressionTypeDef(TypedDict):
    metadataKey: NotRequired[str]

class ExtractionJobFilterInputTypeDef(TypedDict):
    strategyId: NotRequired[str]
    sessionId: NotRequired[str]
    actorId: NotRequired[str]
    status: NotRequired[Literal["FAILED"]]

class MessageMetadataTypeDef(TypedDict):
    eventId: str
    messageIndex: int

class ExtractionJobTypeDef(TypedDict):
    jobId: str

class GetAgentCardRequestTypeDef(TypedDict):
    agentRuntimeArn: str
    runtimeSessionId: NotRequired[str]
    qualifier: NotRequired[str]

class GetBrowserSessionRequestTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str

class ViewPortTypeDef(TypedDict):
    width: int
    height: int

class GetCodeInterpreterSessionRequestTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    sessionId: str

class GetEventInputTypeDef(TypedDict):
    memoryId: str
    sessionId: str
    actorId: str
    eventId: str

class GetMemoryRecordInputTypeDef(TypedDict):
    memoryId: str
    memoryRecordId: str

class GetResourceApiKeyRequestTypeDef(TypedDict):
    workloadIdentityToken: str
    resourceCredentialProviderName: str

class GetResourceOauth2TokenRequestTypeDef(TypedDict):
    workloadIdentityToken: str
    resourceCredentialProviderName: str
    scopes: Sequence[str]
    oauth2Flow: Oauth2FlowTypeType
    sessionUri: NotRequired[str]
    resourceOauth2ReturnUrl: NotRequired[str]
    forceAuthentication: NotRequired[bool]
    customParameters: NotRequired[Mapping[str, str]]
    customState: NotRequired[str]

class GetWorkloadAccessTokenForJWTRequestTypeDef(TypedDict):
    workloadName: str
    userToken: str

class GetWorkloadAccessTokenForUserIdRequestTypeDef(TypedDict):
    workloadName: str
    userId: str

class GetWorkloadAccessTokenRequestTypeDef(TypedDict):
    workloadName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListActorsInputTypeDef(TypedDict):
    memoryId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListBrowserSessionsRequestTypeDef(TypedDict):
    browserIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[BrowserSessionStatusType]

class ListCodeInterpreterSessionsRequestTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[CodeInterpreterSessionStatusType]

class ListMemoryRecordsInputTypeDef(TypedDict):
    memoryId: str
    namespace: str
    memoryStrategyId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSessionsInputTypeDef(TypedDict):
    memoryId: str
    actorId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SessionSummaryTypeDef(TypedDict):
    sessionId: str
    actorId: str
    createdAt: datetime

class MemoryContentTypeDef(TypedDict):
    text: NotRequired[str]

class StartCodeInterpreterSessionRequestTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    traceId: NotRequired[str]
    traceParent: NotRequired[str]
    name: NotRequired[str]
    sessionTimeoutSeconds: NotRequired[int]
    clientToken: NotRequired[str]

class StopBrowserSessionRequestTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    traceId: NotRequired[str]
    traceParent: NotRequired[str]
    clientToken: NotRequired[str]

class StopCodeInterpreterSessionRequestTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    sessionId: str
    traceId: NotRequired[str]
    traceParent: NotRequired[str]
    clientToken: NotRequired[str]

class StopRuntimeSessionRequestTypeDef(TypedDict):
    runtimeSessionId: str
    agentRuntimeArn: str
    qualifier: NotRequired[str]
    clientToken: NotRequired[str]

class ValidationExceptionFieldTypeDef(TypedDict):
    name: str
    message: str

class StreamUpdateTypeDef(TypedDict):
    automationStreamUpdate: NotRequired[AutomationStreamUpdateTypeDef]

class BatchCreateMemoryRecordsOutputTypeDef(TypedDict):
    successfulRecords: List[MemoryRecordOutputTypeDef]
    failedRecords: List[MemoryRecordOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteMemoryRecordsOutputTypeDef(TypedDict):
    successfulRecords: List[MemoryRecordOutputTypeDef]
    failedRecords: List[MemoryRecordOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateMemoryRecordsOutputTypeDef(TypedDict):
    successfulRecords: List[MemoryRecordOutputTypeDef]
    failedRecords: List[MemoryRecordOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventOutputTypeDef(TypedDict):
    eventId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMemoryRecordOutputTypeDef(TypedDict):
    memoryRecordId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentCardResponseTypeDef(TypedDict):
    runtimeSessionId: str
    agentCard: Dict[str, Any]
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetCodeInterpreterSessionResponseTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    sessionId: str
    name: str
    createdAt: datetime
    sessionTimeoutSeconds: int
    status: CodeInterpreterSessionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceApiKeyResponseTypeDef(TypedDict):
    apiKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceOauth2TokenResponseTypeDef(TypedDict):
    authorizationUrl: str
    accessToken: str
    sessionUri: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkloadAccessTokenForJWTResponseTypeDef(TypedDict):
    workloadAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkloadAccessTokenForUserIdResponseTypeDef(TypedDict):
    workloadAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkloadAccessTokenResponseTypeDef(TypedDict):
    workloadAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeAgentRuntimeResponseTypeDef(TypedDict):
    runtimeSessionId: str
    mcpSessionId: str
    mcpProtocolVersion: str
    traceId: str
    traceParent: str
    traceState: str
    baggage: str
    contentType: str
    response: StreamingBody
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListActorsOutputTypeDef(TypedDict):
    actorSummaries: List[ActorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartCodeInterpreterSessionResponseTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    sessionId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartMemoryExtractionJobOutputTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopBrowserSessionResponseTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopCodeInterpreterSessionResponseTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    sessionId: str
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopRuntimeSessionResponseTypeDef(TypedDict):
    runtimeSessionId: str
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteMemoryRecordsInputTypeDef(TypedDict):
    memoryId: str
    records: Sequence[MemoryRecordDeleteInputTypeDef]

class InputContentBlockTypeDef(TypedDict):
    path: str
    text: NotRequired[str]
    blob: NotRequired[BlobTypeDef]

class InvokeAgentRuntimeRequestTypeDef(TypedDict):
    agentRuntimeArn: str
    payload: BlobTypeDef
    contentType: NotRequired[str]
    accept: NotRequired[str]
    mcpSessionId: NotRequired[str]
    runtimeSessionId: NotRequired[str]
    mcpProtocolVersion: NotRequired[str]
    runtimeUserId: NotRequired[str]
    traceId: NotRequired[str]
    traceParent: NotRequired[str]
    traceState: NotRequired[str]
    baggage: NotRequired[str]
    qualifier: NotRequired[str]
    accountId: NotRequired[str]

class BrowserSessionStreamTypeDef(TypedDict):
    automationStream: AutomationStreamTypeDef
    liveViewStream: NotRequired[LiveViewStreamTypeDef]

class ListBrowserSessionsResponseTypeDef(TypedDict):
    items: List[BrowserSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCodeInterpreterSessionsResponseTypeDef(TypedDict):
    items: List[CodeInterpreterSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CompleteResourceTokenAuthRequestTypeDef(TypedDict):
    userIdentifier: UserIdentifierTypeDef
    sessionUri: str

ContentBlockTypeDef = TypedDict(
    "ContentBlockTypeDef",
    {
        "type": ContentBlockTypeType,
        "text": NotRequired[str],
        "data": NotRequired[bytes],
        "mimeType": NotRequired[str],
        "uri": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "size": NotRequired[int],
        "resource": NotRequired[ResourceContentTypeDef],
    },
)

class ConversationalTypeDef(TypedDict):
    content: ContentTypeDef
    role: RoleType

class ContextTypeDef(TypedDict):
    spanContext: NotRequired[SpanContextTypeDef]

class RightExpressionTypeDef(TypedDict):
    metadataValue: NotRequired[MetadataValueTypeDef]

class EvaluateRequestTypeDef(TypedDict):
    evaluatorId: str
    evaluationInput: EvaluationInputTypeDef
    evaluationTarget: NotRequired[EvaluationTargetTypeDef]

ListMemoryExtractionJobsInputTypeDef = TypedDict(
    "ListMemoryExtractionJobsInputTypeDef",
    {
        "memoryId": str,
        "maxResults": NotRequired[int],
        "filter": NotRequired[ExtractionJobFilterInputTypeDef],
        "nextToken": NotRequired[str],
    },
)

class ExtractionJobMessagesTypeDef(TypedDict):
    messagesList: NotRequired[List[MessageMetadataTypeDef]]

class StartMemoryExtractionJobInputTypeDef(TypedDict):
    memoryId: str
    extractionJob: ExtractionJobTypeDef
    clientToken: NotRequired[str]

class StartBrowserSessionRequestTypeDef(TypedDict):
    browserIdentifier: str
    traceId: NotRequired[str]
    traceParent: NotRequired[str]
    name: NotRequired[str]
    sessionTimeoutSeconds: NotRequired[int]
    viewPort: NotRequired[ViewPortTypeDef]
    clientToken: NotRequired[str]

class ListActorsInputPaginateTypeDef(TypedDict):
    memoryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListMemoryExtractionJobsInputPaginateTypeDef = TypedDict(
    "ListMemoryExtractionJobsInputPaginateTypeDef",
    {
        "memoryId": str,
        "filter": NotRequired[ExtractionJobFilterInputTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListMemoryRecordsInputPaginateTypeDef(TypedDict):
    memoryId: str
    namespace: str
    memoryStrategyId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsInputPaginateTypeDef(TypedDict):
    memoryId: str
    actorId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsOutputTypeDef(TypedDict):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class MemoryRecordCreateInputTypeDef(TypedDict):
    requestIdentifier: str
    namespaces: Sequence[str]
    content: MemoryContentTypeDef
    timestamp: TimestampTypeDef
    memoryStrategyId: NotRequired[str]

class MemoryRecordSummaryTypeDef(TypedDict):
    memoryRecordId: str
    content: MemoryContentTypeDef
    memoryStrategyId: str
    namespaces: List[str]
    createdAt: datetime
    score: NotRequired[float]
    metadata: NotRequired[Dict[str, MetadataValueTypeDef]]

class MemoryRecordTypeDef(TypedDict):
    memoryRecordId: str
    content: MemoryContentTypeDef
    memoryStrategyId: str
    namespaces: List[str]
    createdAt: datetime
    metadata: NotRequired[Dict[str, MetadataValueTypeDef]]

class MemoryRecordUpdateInputTypeDef(TypedDict):
    memoryRecordId: str
    timestamp: TimestampTypeDef
    content: NotRequired[MemoryContentTypeDef]
    namespaces: NotRequired[Sequence[str]]
    memoryStrategyId: NotRequired[str]

class ValidationExceptionTypeDef(TypedDict):
    message: str
    reason: ValidationExceptionReasonType
    fieldList: NotRequired[List[ValidationExceptionFieldTypeDef]]

class UpdateBrowserStreamRequestTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    streamUpdate: StreamUpdateTypeDef
    clientToken: NotRequired[str]

class ToolArgumentsTypeDef(TypedDict):
    code: NotRequired[str]
    language: NotRequired[ProgrammingLanguageType]
    clearContext: NotRequired[bool]
    command: NotRequired[str]
    path: NotRequired[str]
    paths: NotRequired[Sequence[str]]
    content: NotRequired[Sequence[InputContentBlockTypeDef]]
    directoryPath: NotRequired[str]
    taskId: NotRequired[str]

class GetBrowserSessionResponseTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    name: str
    createdAt: datetime
    viewPort: ViewPortTypeDef
    sessionTimeoutSeconds: int
    status: BrowserSessionStatusType
    streams: BrowserSessionStreamTypeDef
    sessionReplayArtifact: str
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartBrowserSessionResponseTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    createdAt: datetime
    streams: BrowserSessionStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrowserStreamResponseTypeDef(TypedDict):
    browserIdentifier: str
    sessionId: str
    streams: BrowserSessionStreamTypeDef
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CodeInterpreterResultTypeDef(TypedDict):
    content: List[ContentBlockTypeDef]
    structuredContent: NotRequired[ToolResultStructuredContentTypeDef]
    isError: NotRequired[bool]

class PayloadTypeOutputTypeDef(TypedDict):
    conversational: NotRequired[ConversationalTypeDef]
    blob: NotRequired[Dict[str, Any]]

class PayloadTypeTypeDef(TypedDict):
    conversational: NotRequired[ConversationalTypeDef]
    blob: NotRequired[Mapping[str, Any]]

class EvaluationResultContentTypeDef(TypedDict):
    evaluatorArn: str
    evaluatorId: str
    evaluatorName: str
    context: ContextTypeDef
    explanation: NotRequired[str]
    value: NotRequired[float]
    label: NotRequired[str]
    tokenUsage: NotRequired[TokenUsageTypeDef]
    errorMessage: NotRequired[str]
    errorCode: NotRequired[str]

EventMetadataFilterExpressionTypeDef = TypedDict(
    "EventMetadataFilterExpressionTypeDef",
    {
        "left": LeftExpressionTypeDef,
        "operator": OperatorTypeType,
        "right": NotRequired[RightExpressionTypeDef],
    },
)
MemoryMetadataFilterExpressionTypeDef = TypedDict(
    "MemoryMetadataFilterExpressionTypeDef",
    {
        "left": LeftExpressionTypeDef,
        "operator": OperatorTypeType,
        "right": NotRequired[RightExpressionTypeDef],
    },
)

class ExtractionJobMetadataTypeDef(TypedDict):
    jobID: str
    messages: ExtractionJobMessagesTypeDef
    status: NotRequired[Literal["FAILED"]]
    failureReason: NotRequired[str]
    strategyId: NotRequired[str]
    sessionId: NotRequired[str]
    actorId: NotRequired[str]

class BatchCreateMemoryRecordsInputTypeDef(TypedDict):
    memoryId: str
    records: Sequence[MemoryRecordCreateInputTypeDef]
    clientToken: NotRequired[str]

class ListMemoryRecordsOutputTypeDef(TypedDict):
    memoryRecordSummaries: List[MemoryRecordSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RetrieveMemoryRecordsOutputTypeDef(TypedDict):
    memoryRecordSummaries: List[MemoryRecordSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetMemoryRecordOutputTypeDef(TypedDict):
    memoryRecord: MemoryRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateMemoryRecordsInputTypeDef(TypedDict):
    memoryId: str
    records: Sequence[MemoryRecordUpdateInputTypeDef]

class InvokeCodeInterpreterRequestTypeDef(TypedDict):
    codeInterpreterIdentifier: str
    name: ToolNameType
    sessionId: NotRequired[str]
    traceId: NotRequired[str]
    traceParent: NotRequired[str]
    arguments: NotRequired[ToolArgumentsTypeDef]

class CodeInterpreterStreamOutputTypeDef(TypedDict):
    result: NotRequired[CodeInterpreterResultTypeDef]
    accessDeniedException: NotRequired[AccessDeniedExceptionTypeDef]
    conflictException: NotRequired[ConflictExceptionTypeDef]
    internalServerException: NotRequired[InternalServerExceptionTypeDef]
    resourceNotFoundException: NotRequired[ResourceNotFoundExceptionTypeDef]
    serviceQuotaExceededException: NotRequired[ServiceQuotaExceededExceptionTypeDef]
    throttlingException: NotRequired[ThrottlingExceptionTypeDef]
    validationException: NotRequired[ValidationExceptionTypeDef]

class EventTypeDef(TypedDict):
    memoryId: str
    actorId: str
    sessionId: str
    eventId: str
    eventTimestamp: datetime
    payload: List[PayloadTypeOutputTypeDef]
    branch: NotRequired[BranchTypeDef]
    metadata: NotRequired[Dict[str, MetadataValueTypeDef]]

PayloadTypeUnionTypeDef = Union[PayloadTypeTypeDef, PayloadTypeOutputTypeDef]

class EvaluateResponseTypeDef(TypedDict):
    evaluationResults: List[EvaluationResultContentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterInputTypeDef(TypedDict):
    branch: NotRequired[BranchFilterTypeDef]
    eventMetadata: NotRequired[Sequence[EventMetadataFilterExpressionTypeDef]]

class SearchCriteriaTypeDef(TypedDict):
    searchQuery: str
    memoryStrategyId: NotRequired[str]
    topK: NotRequired[int]
    metadataFilters: NotRequired[Sequence[MemoryMetadataFilterExpressionTypeDef]]

class ListMemoryExtractionJobsOutputTypeDef(TypedDict):
    jobs: List[ExtractionJobMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class InvokeCodeInterpreterResponseTypeDef(TypedDict):
    sessionId: str
    stream: EventStream[CodeInterpreterStreamOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventOutputTypeDef(TypedDict):
    event: EventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventOutputTypeDef(TypedDict):
    event: EventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventsOutputTypeDef(TypedDict):
    events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateEventInputTypeDef(TypedDict):
    memoryId: str
    actorId: str
    eventTimestamp: TimestampTypeDef
    payload: Sequence[PayloadTypeUnionTypeDef]
    sessionId: NotRequired[str]
    branch: NotRequired[BranchTypeDef]
    clientToken: NotRequired[str]
    metadata: NotRequired[Mapping[str, MetadataValueTypeDef]]

ListEventsInputPaginateTypeDef = TypedDict(
    "ListEventsInputPaginateTypeDef",
    {
        "memoryId": str,
        "sessionId": str,
        "actorId": str,
        "includePayloads": NotRequired[bool],
        "filter": NotRequired[FilterInputTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventsInputTypeDef = TypedDict(
    "ListEventsInputTypeDef",
    {
        "memoryId": str,
        "sessionId": str,
        "actorId": str,
        "includePayloads": NotRequired[bool],
        "filter": NotRequired[FilterInputTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class RetrieveMemoryRecordsInputPaginateTypeDef(TypedDict):
    memoryId: str
    namespace: str
    searchCriteria: SearchCriteriaTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class RetrieveMemoryRecordsInputTypeDef(TypedDict):
    memoryId: str
    namespace: str
    searchCriteria: SearchCriteriaTypeDef
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
