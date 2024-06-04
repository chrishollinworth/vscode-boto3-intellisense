"""
Type annotations for bedrock-agent-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bedrock_agent_runtime.type_defs import AccessDeniedExceptionTypeDef

    data: AccessDeniedExceptionTypeDef = {...}
    ```
"""

import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    CreationModeType,
    ExternalSourceTypeType,
    GuadrailActionType,
    GuardrailActionType,
    GuardrailContentFilterConfidenceType,
    GuardrailContentFilterTypeType,
    GuardrailPiiEntityTypeType,
    GuardrailSensitiveInformationPolicyActionType,
    InvocationTypeType,
    PromptTypeType,
    ResponseStateType,
    RetrieveAndGenerateTypeType,
    SearchTypeType,
    SourceType,
    TypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessDeniedExceptionTypeDef",
    "ActionGroupInvocationInputTypeDef",
    "ActionGroupInvocationOutputTypeDef",
    "ApiInvocationInputTypeDef",
    "ApiParameterTypeDef",
    "ApiRequestBodyTypeDef",
    "ApiResultTypeDef",
    "AttributionTypeDef",
    "BadGatewayExceptionTypeDef",
    "ByteContentDocTypeDef",
    "CitationTypeDef",
    "ConflictExceptionTypeDef",
    "ContentBodyTypeDef",
    "DependencyFailedExceptionTypeDef",
    "ExternalSourceTypeDef",
    "ExternalSourcesGenerationConfigurationTypeDef",
    "ExternalSourcesRetrieveAndGenerateConfigurationTypeDef",
    "FailureTraceTypeDef",
    "FilterAttributeTypeDef",
    "FinalResponseTypeDef",
    "FunctionInvocationInputTypeDef",
    "FunctionParameterTypeDef",
    "FunctionResultTypeDef",
    "GeneratedResponsePartTypeDef",
    "GenerationConfigurationTypeDef",
    "GuardrailAssessmentTypeDef",
    "GuardrailConfigurationTypeDef",
    "GuardrailContentFilterTypeDef",
    "GuardrailContentPolicyAssessmentTypeDef",
    "GuardrailCustomWordTypeDef",
    "GuardrailManagedWordTypeDef",
    "GuardrailPiiEntityFilterTypeDef",
    "GuardrailRegexFilterTypeDef",
    "GuardrailSensitiveInformationPolicyAssessmentTypeDef",
    "GuardrailTopicPolicyAssessmentTypeDef",
    "GuardrailTopicTypeDef",
    "GuardrailTraceTypeDef",
    "GuardrailWordPolicyAssessmentTypeDef",
    "InferenceConfigTypeDef",
    "InferenceConfigurationTypeDef",
    "InternalServerExceptionTypeDef",
    "InvocationInputMemberTypeDef",
    "InvocationInputTypeDef",
    "InvocationResultMemberTypeDef",
    "InvokeAgentRequestRequestTypeDef",
    "InvokeAgentResponseTypeDef",
    "KnowledgeBaseLookupInputTypeDef",
    "KnowledgeBaseLookupOutputTypeDef",
    "KnowledgeBaseQueryTypeDef",
    "KnowledgeBaseRetrievalConfigurationTypeDef",
    "KnowledgeBaseRetrievalResultTypeDef",
    "KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef",
    "KnowledgeBaseVectorSearchConfigurationTypeDef",
    "ModelInvocationInputTypeDef",
    "ObservationTypeDef",
    "OrchestrationTraceTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PayloadPartTypeDef",
    "PostProcessingModelInvocationOutputTypeDef",
    "PostProcessingParsedResponseTypeDef",
    "PostProcessingTraceTypeDef",
    "PreProcessingModelInvocationOutputTypeDef",
    "PreProcessingParsedResponseTypeDef",
    "PreProcessingTraceTypeDef",
    "PromptTemplateTypeDef",
    "PropertyParametersTypeDef",
    "RationaleTypeDef",
    "RepromptResponseTypeDef",
    "RequestBodyTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseStreamTypeDef",
    "RetrievalFilterTypeDef",
    "RetrievalResultContentTypeDef",
    "RetrievalResultLocationTypeDef",
    "RetrievalResultS3LocationTypeDef",
    "RetrieveAndGenerateConfigurationTypeDef",
    "RetrieveAndGenerateInputTypeDef",
    "RetrieveAndGenerateOutputTypeDef",
    "RetrieveAndGenerateRequestRequestTypeDef",
    "RetrieveAndGenerateResponseTypeDef",
    "RetrieveAndGenerateSessionConfigurationTypeDef",
    "RetrieveRequestRequestTypeDef",
    "RetrieveResponseTypeDef",
    "RetrievedReferenceTypeDef",
    "ReturnControlPayloadTypeDef",
    "S3ObjectDocTypeDef",
    "ServiceQuotaExceededExceptionTypeDef",
    "SessionStateTypeDef",
    "SpanTypeDef",
    "TextInferenceConfigTypeDef",
    "TextResponsePartTypeDef",
    "ThrottlingExceptionTypeDef",
    "TracePartTypeDef",
    "TraceTypeDef",
    "ValidationExceptionTypeDef",
)

AccessDeniedExceptionTypeDef = TypedDict(
    "AccessDeniedExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ActionGroupInvocationInputTypeDef = TypedDict(
    "ActionGroupInvocationInputTypeDef",
    {
        "actionGroupName": str,
        "apiPath": str,
        "function": str,
        "parameters": List["ParameterTypeDef"],
        "requestBody": "RequestBodyTypeDef",
        "verb": str,
    },
    total=False,
)

ActionGroupInvocationOutputTypeDef = TypedDict(
    "ActionGroupInvocationOutputTypeDef",
    {
        "text": str,
    },
    total=False,
)

_RequiredApiInvocationInputTypeDef = TypedDict(
    "_RequiredApiInvocationInputTypeDef",
    {
        "actionGroup": str,
    },
)
_OptionalApiInvocationInputTypeDef = TypedDict(
    "_OptionalApiInvocationInputTypeDef",
    {
        "apiPath": str,
        "httpMethod": str,
        "parameters": List["ApiParameterTypeDef"],
        "requestBody": "ApiRequestBodyTypeDef",
    },
    total=False,
)

class ApiInvocationInputTypeDef(
    _RequiredApiInvocationInputTypeDef, _OptionalApiInvocationInputTypeDef
):
    pass

ApiParameterTypeDef = TypedDict(
    "ApiParameterTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
    },
    total=False,
)

ApiRequestBodyTypeDef = TypedDict(
    "ApiRequestBodyTypeDef",
    {
        "content": Dict[str, "PropertyParametersTypeDef"],
    },
    total=False,
)

_RequiredApiResultTypeDef = TypedDict(
    "_RequiredApiResultTypeDef",
    {
        "actionGroup": str,
    },
)
_OptionalApiResultTypeDef = TypedDict(
    "_OptionalApiResultTypeDef",
    {
        "apiPath": str,
        "httpMethod": str,
        "httpStatusCode": int,
        "responseBody": Dict[str, "ContentBodyTypeDef"],
        "responseState": ResponseStateType,
    },
    total=False,
)

class ApiResultTypeDef(_RequiredApiResultTypeDef, _OptionalApiResultTypeDef):
    pass

AttributionTypeDef = TypedDict(
    "AttributionTypeDef",
    {
        "citations": List["CitationTypeDef"],
    },
    total=False,
)

BadGatewayExceptionTypeDef = TypedDict(
    "BadGatewayExceptionTypeDef",
    {
        "message": str,
        "resourceName": str,
    },
    total=False,
)

ByteContentDocTypeDef = TypedDict(
    "ByteContentDocTypeDef",
    {
        "contentType": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
        "identifier": str,
    },
)

CitationTypeDef = TypedDict(
    "CitationTypeDef",
    {
        "generatedResponsePart": "GeneratedResponsePartTypeDef",
        "retrievedReferences": List["RetrievedReferenceTypeDef"],
    },
    total=False,
)

ConflictExceptionTypeDef = TypedDict(
    "ConflictExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ContentBodyTypeDef = TypedDict(
    "ContentBodyTypeDef",
    {
        "body": str,
    },
    total=False,
)

DependencyFailedExceptionTypeDef = TypedDict(
    "DependencyFailedExceptionTypeDef",
    {
        "message": str,
        "resourceName": str,
    },
    total=False,
)

_RequiredExternalSourceTypeDef = TypedDict(
    "_RequiredExternalSourceTypeDef",
    {
        "sourceType": ExternalSourceTypeType,
    },
)
_OptionalExternalSourceTypeDef = TypedDict(
    "_OptionalExternalSourceTypeDef",
    {
        "byteContent": "ByteContentDocTypeDef",
        "s3Location": "S3ObjectDocTypeDef",
    },
    total=False,
)

class ExternalSourceTypeDef(_RequiredExternalSourceTypeDef, _OptionalExternalSourceTypeDef):
    pass

ExternalSourcesGenerationConfigurationTypeDef = TypedDict(
    "ExternalSourcesGenerationConfigurationTypeDef",
    {
        "additionalModelRequestFields": Dict[str, Dict[str, Any]],
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "inferenceConfig": "InferenceConfigTypeDef",
        "promptTemplate": "PromptTemplateTypeDef",
    },
    total=False,
)

_RequiredExternalSourcesRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "_RequiredExternalSourcesRetrieveAndGenerateConfigurationTypeDef",
    {
        "modelArn": str,
        "sources": List["ExternalSourceTypeDef"],
    },
)
_OptionalExternalSourcesRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "_OptionalExternalSourcesRetrieveAndGenerateConfigurationTypeDef",
    {
        "generationConfiguration": "ExternalSourcesGenerationConfigurationTypeDef",
    },
    total=False,
)

class ExternalSourcesRetrieveAndGenerateConfigurationTypeDef(
    _RequiredExternalSourcesRetrieveAndGenerateConfigurationTypeDef,
    _OptionalExternalSourcesRetrieveAndGenerateConfigurationTypeDef,
):
    pass

FailureTraceTypeDef = TypedDict(
    "FailureTraceTypeDef",
    {
        "failureReason": str,
        "traceId": str,
    },
    total=False,
)

FilterAttributeTypeDef = TypedDict(
    "FilterAttributeTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)

FinalResponseTypeDef = TypedDict(
    "FinalResponseTypeDef",
    {
        "text": str,
    },
    total=False,
)

_RequiredFunctionInvocationInputTypeDef = TypedDict(
    "_RequiredFunctionInvocationInputTypeDef",
    {
        "actionGroup": str,
    },
)
_OptionalFunctionInvocationInputTypeDef = TypedDict(
    "_OptionalFunctionInvocationInputTypeDef",
    {
        "function": str,
        "parameters": List["FunctionParameterTypeDef"],
    },
    total=False,
)

class FunctionInvocationInputTypeDef(
    _RequiredFunctionInvocationInputTypeDef, _OptionalFunctionInvocationInputTypeDef
):
    pass

FunctionParameterTypeDef = TypedDict(
    "FunctionParameterTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
    },
    total=False,
)

_RequiredFunctionResultTypeDef = TypedDict(
    "_RequiredFunctionResultTypeDef",
    {
        "actionGroup": str,
    },
)
_OptionalFunctionResultTypeDef = TypedDict(
    "_OptionalFunctionResultTypeDef",
    {
        "function": str,
        "responseBody": Dict[str, "ContentBodyTypeDef"],
        "responseState": ResponseStateType,
    },
    total=False,
)

class FunctionResultTypeDef(_RequiredFunctionResultTypeDef, _OptionalFunctionResultTypeDef):
    pass

GeneratedResponsePartTypeDef = TypedDict(
    "GeneratedResponsePartTypeDef",
    {
        "textResponsePart": "TextResponsePartTypeDef",
    },
    total=False,
)

GenerationConfigurationTypeDef = TypedDict(
    "GenerationConfigurationTypeDef",
    {
        "additionalModelRequestFields": Dict[str, Dict[str, Any]],
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "inferenceConfig": "InferenceConfigTypeDef",
        "promptTemplate": "PromptTemplateTypeDef",
    },
    total=False,
)

GuardrailAssessmentTypeDef = TypedDict(
    "GuardrailAssessmentTypeDef",
    {
        "contentPolicy": "GuardrailContentPolicyAssessmentTypeDef",
        "sensitiveInformationPolicy": "GuardrailSensitiveInformationPolicyAssessmentTypeDef",
        "topicPolicy": "GuardrailTopicPolicyAssessmentTypeDef",
        "wordPolicy": "GuardrailWordPolicyAssessmentTypeDef",
    },
    total=False,
)

GuardrailConfigurationTypeDef = TypedDict(
    "GuardrailConfigurationTypeDef",
    {
        "guardrailId": str,
        "guardrailVersion": str,
    },
)

GuardrailContentFilterTypeDef = TypedDict(
    "GuardrailContentFilterTypeDef",
    {
        "action": Literal["BLOCKED"],
        "confidence": GuardrailContentFilterConfidenceType,
        "type": GuardrailContentFilterTypeType,
    },
    total=False,
)

GuardrailContentPolicyAssessmentTypeDef = TypedDict(
    "GuardrailContentPolicyAssessmentTypeDef",
    {
        "filters": List["GuardrailContentFilterTypeDef"],
    },
    total=False,
)

GuardrailCustomWordTypeDef = TypedDict(
    "GuardrailCustomWordTypeDef",
    {
        "action": Literal["BLOCKED"],
        "match": str,
    },
    total=False,
)

GuardrailManagedWordTypeDef = TypedDict(
    "GuardrailManagedWordTypeDef",
    {
        "action": Literal["BLOCKED"],
        "match": str,
        "type": Literal["PROFANITY"],
    },
    total=False,
)

GuardrailPiiEntityFilterTypeDef = TypedDict(
    "GuardrailPiiEntityFilterTypeDef",
    {
        "action": GuardrailSensitiveInformationPolicyActionType,
        "match": str,
        "type": GuardrailPiiEntityTypeType,
    },
    total=False,
)

GuardrailRegexFilterTypeDef = TypedDict(
    "GuardrailRegexFilterTypeDef",
    {
        "action": GuardrailSensitiveInformationPolicyActionType,
        "match": str,
        "name": str,
        "regex": str,
    },
    total=False,
)

GuardrailSensitiveInformationPolicyAssessmentTypeDef = TypedDict(
    "GuardrailSensitiveInformationPolicyAssessmentTypeDef",
    {
        "piiEntities": List["GuardrailPiiEntityFilterTypeDef"],
        "regexes": List["GuardrailRegexFilterTypeDef"],
    },
    total=False,
)

GuardrailTopicPolicyAssessmentTypeDef = TypedDict(
    "GuardrailTopicPolicyAssessmentTypeDef",
    {
        "topics": List["GuardrailTopicTypeDef"],
    },
    total=False,
)

GuardrailTopicTypeDef = TypedDict(
    "GuardrailTopicTypeDef",
    {
        "action": Literal["BLOCKED"],
        "name": str,
        "type": Literal["DENY"],
    },
    total=False,
)

GuardrailTraceTypeDef = TypedDict(
    "GuardrailTraceTypeDef",
    {
        "action": GuardrailActionType,
        "inputAssessments": List["GuardrailAssessmentTypeDef"],
        "outputAssessments": List["GuardrailAssessmentTypeDef"],
        "traceId": str,
    },
    total=False,
)

GuardrailWordPolicyAssessmentTypeDef = TypedDict(
    "GuardrailWordPolicyAssessmentTypeDef",
    {
        "customWords": List["GuardrailCustomWordTypeDef"],
        "managedWordLists": List["GuardrailManagedWordTypeDef"],
    },
    total=False,
)

InferenceConfigTypeDef = TypedDict(
    "InferenceConfigTypeDef",
    {
        "textInferenceConfig": "TextInferenceConfigTypeDef",
    },
    total=False,
)

InferenceConfigurationTypeDef = TypedDict(
    "InferenceConfigurationTypeDef",
    {
        "maximumLength": int,
        "stopSequences": List[str],
        "temperature": float,
        "topK": int,
        "topP": float,
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

InvocationInputMemberTypeDef = TypedDict(
    "InvocationInputMemberTypeDef",
    {
        "apiInvocationInput": "ApiInvocationInputTypeDef",
        "functionInvocationInput": "FunctionInvocationInputTypeDef",
    },
    total=False,
)

InvocationInputTypeDef = TypedDict(
    "InvocationInputTypeDef",
    {
        "actionGroupInvocationInput": "ActionGroupInvocationInputTypeDef",
        "invocationType": InvocationTypeType,
        "knowledgeBaseLookupInput": "KnowledgeBaseLookupInputTypeDef",
        "traceId": str,
    },
    total=False,
)

InvocationResultMemberTypeDef = TypedDict(
    "InvocationResultMemberTypeDef",
    {
        "apiResult": "ApiResultTypeDef",
        "functionResult": "FunctionResultTypeDef",
    },
    total=False,
)

_RequiredInvokeAgentRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeAgentRequestRequestTypeDef",
    {
        "agentAliasId": str,
        "agentId": str,
        "sessionId": str,
    },
)
_OptionalInvokeAgentRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeAgentRequestRequestTypeDef",
    {
        "enableTrace": bool,
        "endSession": bool,
        "inputText": str,
        "sessionState": "SessionStateTypeDef",
    },
    total=False,
)

class InvokeAgentRequestRequestTypeDef(
    _RequiredInvokeAgentRequestRequestTypeDef, _OptionalInvokeAgentRequestRequestTypeDef
):
    pass

InvokeAgentResponseTypeDef = TypedDict(
    "InvokeAgentResponseTypeDef",
    {
        "completion": "ResponseStreamTypeDef",
        "contentType": str,
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KnowledgeBaseLookupInputTypeDef = TypedDict(
    "KnowledgeBaseLookupInputTypeDef",
    {
        "knowledgeBaseId": str,
        "text": str,
    },
    total=False,
)

KnowledgeBaseLookupOutputTypeDef = TypedDict(
    "KnowledgeBaseLookupOutputTypeDef",
    {
        "retrievedReferences": List["RetrievedReferenceTypeDef"],
    },
    total=False,
)

KnowledgeBaseQueryTypeDef = TypedDict(
    "KnowledgeBaseQueryTypeDef",
    {
        "text": str,
    },
)

KnowledgeBaseRetrievalConfigurationTypeDef = TypedDict(
    "KnowledgeBaseRetrievalConfigurationTypeDef",
    {
        "vectorSearchConfiguration": "KnowledgeBaseVectorSearchConfigurationTypeDef",
    },
)

_RequiredKnowledgeBaseRetrievalResultTypeDef = TypedDict(
    "_RequiredKnowledgeBaseRetrievalResultTypeDef",
    {
        "content": "RetrievalResultContentTypeDef",
    },
)
_OptionalKnowledgeBaseRetrievalResultTypeDef = TypedDict(
    "_OptionalKnowledgeBaseRetrievalResultTypeDef",
    {
        "location": "RetrievalResultLocationTypeDef",
        "metadata": Dict[str, Dict[str, Any]],
        "score": float,
    },
    total=False,
)

class KnowledgeBaseRetrievalResultTypeDef(
    _RequiredKnowledgeBaseRetrievalResultTypeDef, _OptionalKnowledgeBaseRetrievalResultTypeDef
):
    pass

_RequiredKnowledgeBaseRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "_RequiredKnowledgeBaseRetrieveAndGenerateConfigurationTypeDef",
    {
        "knowledgeBaseId": str,
        "modelArn": str,
    },
)
_OptionalKnowledgeBaseRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "_OptionalKnowledgeBaseRetrieveAndGenerateConfigurationTypeDef",
    {
        "generationConfiguration": "GenerationConfigurationTypeDef",
        "retrievalConfiguration": "KnowledgeBaseRetrievalConfigurationTypeDef",
    },
    total=False,
)

class KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef(
    _RequiredKnowledgeBaseRetrieveAndGenerateConfigurationTypeDef,
    _OptionalKnowledgeBaseRetrieveAndGenerateConfigurationTypeDef,
):
    pass

KnowledgeBaseVectorSearchConfigurationTypeDef = TypedDict(
    "KnowledgeBaseVectorSearchConfigurationTypeDef",
    {
        "filter": "RetrievalFilterTypeDef",
        "numberOfResults": int,
        "overrideSearchType": SearchTypeType,
    },
    total=False,
)

ModelInvocationInputTypeDef = TypedDict(
    "ModelInvocationInputTypeDef",
    {
        "inferenceConfiguration": "InferenceConfigurationTypeDef",
        "overrideLambda": str,
        "parserMode": CreationModeType,
        "promptCreationMode": CreationModeType,
        "text": str,
        "traceId": str,
        "type": PromptTypeType,
    },
    total=False,
)

ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "actionGroupInvocationOutput": "ActionGroupInvocationOutputTypeDef",
        "finalResponse": "FinalResponseTypeDef",
        "knowledgeBaseLookupOutput": "KnowledgeBaseLookupOutputTypeDef",
        "repromptResponse": "RepromptResponseTypeDef",
        "traceId": str,
        "type": TypeType,
    },
    total=False,
)

OrchestrationTraceTypeDef = TypedDict(
    "OrchestrationTraceTypeDef",
    {
        "invocationInput": "InvocationInputTypeDef",
        "modelInvocationInput": "ModelInvocationInputTypeDef",
        "observation": "ObservationTypeDef",
        "rationale": "RationaleTypeDef",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
    },
    total=False,
)

PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "attribution": "AttributionTypeDef",
        "bytes": bytes,
    },
    total=False,
)

PostProcessingModelInvocationOutputTypeDef = TypedDict(
    "PostProcessingModelInvocationOutputTypeDef",
    {
        "parsedResponse": "PostProcessingParsedResponseTypeDef",
        "traceId": str,
    },
    total=False,
)

PostProcessingParsedResponseTypeDef = TypedDict(
    "PostProcessingParsedResponseTypeDef",
    {
        "text": str,
    },
    total=False,
)

PostProcessingTraceTypeDef = TypedDict(
    "PostProcessingTraceTypeDef",
    {
        "modelInvocationInput": "ModelInvocationInputTypeDef",
        "modelInvocationOutput": "PostProcessingModelInvocationOutputTypeDef",
    },
    total=False,
)

PreProcessingModelInvocationOutputTypeDef = TypedDict(
    "PreProcessingModelInvocationOutputTypeDef",
    {
        "parsedResponse": "PreProcessingParsedResponseTypeDef",
        "traceId": str,
    },
    total=False,
)

PreProcessingParsedResponseTypeDef = TypedDict(
    "PreProcessingParsedResponseTypeDef",
    {
        "isValid": bool,
        "rationale": str,
    },
    total=False,
)

PreProcessingTraceTypeDef = TypedDict(
    "PreProcessingTraceTypeDef",
    {
        "modelInvocationInput": "ModelInvocationInputTypeDef",
        "modelInvocationOutput": "PreProcessingModelInvocationOutputTypeDef",
    },
    total=False,
)

PromptTemplateTypeDef = TypedDict(
    "PromptTemplateTypeDef",
    {
        "textPromptTemplate": str,
    },
    total=False,
)

PropertyParametersTypeDef = TypedDict(
    "PropertyParametersTypeDef",
    {
        "properties": List["ParameterTypeDef"],
    },
    total=False,
)

RationaleTypeDef = TypedDict(
    "RationaleTypeDef",
    {
        "text": str,
        "traceId": str,
    },
    total=False,
)

RepromptResponseTypeDef = TypedDict(
    "RepromptResponseTypeDef",
    {
        "source": SourceType,
        "text": str,
    },
    total=False,
)

RequestBodyTypeDef = TypedDict(
    "RequestBodyTypeDef",
    {
        "content": Dict[str, List["ParameterTypeDef"]],
    },
    total=False,
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": str,
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
        "accessDeniedException": "AccessDeniedExceptionTypeDef",
        "badGatewayException": "BadGatewayExceptionTypeDef",
        "chunk": "PayloadPartTypeDef",
        "conflictException": "ConflictExceptionTypeDef",
        "dependencyFailedException": "DependencyFailedExceptionTypeDef",
        "internalServerException": "InternalServerExceptionTypeDef",
        "resourceNotFoundException": "ResourceNotFoundExceptionTypeDef",
        "returnControl": "ReturnControlPayloadTypeDef",
        "serviceQuotaExceededException": "ServiceQuotaExceededExceptionTypeDef",
        "throttlingException": "ThrottlingExceptionTypeDef",
        "trace": "TracePartTypeDef",
        "validationException": "ValidationExceptionTypeDef",
    },
    total=False,
)

RetrievalFilterTypeDef = TypedDict(
    "RetrievalFilterTypeDef",
    {
        "andAll": List[Dict[str, Any]],
        "equals": "FilterAttributeTypeDef",
        "greaterThan": "FilterAttributeTypeDef",
        "greaterThanOrEquals": "FilterAttributeTypeDef",
        "in": "FilterAttributeTypeDef",
        "lessThan": "FilterAttributeTypeDef",
        "lessThanOrEquals": "FilterAttributeTypeDef",
        "listContains": "FilterAttributeTypeDef",
        "notEquals": "FilterAttributeTypeDef",
        "notIn": "FilterAttributeTypeDef",
        "orAll": List[Dict[str, Any]],
        "startsWith": "FilterAttributeTypeDef",
        "stringContains": "FilterAttributeTypeDef",
    },
    total=False,
)

RetrievalResultContentTypeDef = TypedDict(
    "RetrievalResultContentTypeDef",
    {
        "text": str,
    },
)

_RequiredRetrievalResultLocationTypeDef = TypedDict(
    "_RequiredRetrievalResultLocationTypeDef",
    {
        "type": Literal["S3"],
    },
)
_OptionalRetrievalResultLocationTypeDef = TypedDict(
    "_OptionalRetrievalResultLocationTypeDef",
    {
        "s3Location": "RetrievalResultS3LocationTypeDef",
    },
    total=False,
)

class RetrievalResultLocationTypeDef(
    _RequiredRetrievalResultLocationTypeDef, _OptionalRetrievalResultLocationTypeDef
):
    pass

RetrievalResultS3LocationTypeDef = TypedDict(
    "RetrievalResultS3LocationTypeDef",
    {
        "uri": str,
    },
    total=False,
)

_RequiredRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "_RequiredRetrieveAndGenerateConfigurationTypeDef",
    {
        "type": RetrieveAndGenerateTypeType,
    },
)
_OptionalRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "_OptionalRetrieveAndGenerateConfigurationTypeDef",
    {
        "externalSourcesConfiguration": "ExternalSourcesRetrieveAndGenerateConfigurationTypeDef",
        "knowledgeBaseConfiguration": "KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef",
    },
    total=False,
)

class RetrieveAndGenerateConfigurationTypeDef(
    _RequiredRetrieveAndGenerateConfigurationTypeDef,
    _OptionalRetrieveAndGenerateConfigurationTypeDef,
):
    pass

RetrieveAndGenerateInputTypeDef = TypedDict(
    "RetrieveAndGenerateInputTypeDef",
    {
        "text": str,
    },
)

RetrieveAndGenerateOutputTypeDef = TypedDict(
    "RetrieveAndGenerateOutputTypeDef",
    {
        "text": str,
    },
)

_RequiredRetrieveAndGenerateRequestRequestTypeDef = TypedDict(
    "_RequiredRetrieveAndGenerateRequestRequestTypeDef",
    {
        "input": "RetrieveAndGenerateInputTypeDef",
    },
)
_OptionalRetrieveAndGenerateRequestRequestTypeDef = TypedDict(
    "_OptionalRetrieveAndGenerateRequestRequestTypeDef",
    {
        "retrieveAndGenerateConfiguration": "RetrieveAndGenerateConfigurationTypeDef",
        "sessionConfiguration": "RetrieveAndGenerateSessionConfigurationTypeDef",
        "sessionId": str,
    },
    total=False,
)

class RetrieveAndGenerateRequestRequestTypeDef(
    _RequiredRetrieveAndGenerateRequestRequestTypeDef,
    _OptionalRetrieveAndGenerateRequestRequestTypeDef,
):
    pass

RetrieveAndGenerateResponseTypeDef = TypedDict(
    "RetrieveAndGenerateResponseTypeDef",
    {
        "citations": List["CitationTypeDef"],
        "guardrailAction": GuadrailActionType,
        "output": "RetrieveAndGenerateOutputTypeDef",
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetrieveAndGenerateSessionConfigurationTypeDef = TypedDict(
    "RetrieveAndGenerateSessionConfigurationTypeDef",
    {
        "kmsKeyArn": str,
    },
)

_RequiredRetrieveRequestRequestTypeDef = TypedDict(
    "_RequiredRetrieveRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "retrievalQuery": "KnowledgeBaseQueryTypeDef",
    },
)
_OptionalRetrieveRequestRequestTypeDef = TypedDict(
    "_OptionalRetrieveRequestRequestTypeDef",
    {
        "nextToken": str,
        "retrievalConfiguration": "KnowledgeBaseRetrievalConfigurationTypeDef",
    },
    total=False,
)

class RetrieveRequestRequestTypeDef(
    _RequiredRetrieveRequestRequestTypeDef, _OptionalRetrieveRequestRequestTypeDef
):
    pass

RetrieveResponseTypeDef = TypedDict(
    "RetrieveResponseTypeDef",
    {
        "nextToken": str,
        "retrievalResults": List["KnowledgeBaseRetrievalResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetrievedReferenceTypeDef = TypedDict(
    "RetrievedReferenceTypeDef",
    {
        "content": "RetrievalResultContentTypeDef",
        "location": "RetrievalResultLocationTypeDef",
        "metadata": Dict[str, Dict[str, Any]],
    },
    total=False,
)

ReturnControlPayloadTypeDef = TypedDict(
    "ReturnControlPayloadTypeDef",
    {
        "invocationId": str,
        "invocationInputs": List["InvocationInputMemberTypeDef"],
    },
    total=False,
)

S3ObjectDocTypeDef = TypedDict(
    "S3ObjectDocTypeDef",
    {
        "uri": str,
    },
)

ServiceQuotaExceededExceptionTypeDef = TypedDict(
    "ServiceQuotaExceededExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "invocationId": str,
        "promptSessionAttributes": Dict[str, str],
        "returnControlInvocationResults": List["InvocationResultMemberTypeDef"],
        "sessionAttributes": Dict[str, str],
    },
    total=False,
)

SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "end": int,
        "start": int,
    },
    total=False,
)

TextInferenceConfigTypeDef = TypedDict(
    "TextInferenceConfigTypeDef",
    {
        "maxTokens": int,
        "stopSequences": List[str],
        "temperature": float,
        "topP": float,
    },
    total=False,
)

TextResponsePartTypeDef = TypedDict(
    "TextResponsePartTypeDef",
    {
        "span": "SpanTypeDef",
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

TracePartTypeDef = TypedDict(
    "TracePartTypeDef",
    {
        "agentAliasId": str,
        "agentId": str,
        "agentVersion": str,
        "sessionId": str,
        "trace": "TraceTypeDef",
    },
    total=False,
)

TraceTypeDef = TypedDict(
    "TraceTypeDef",
    {
        "failureTrace": "FailureTraceTypeDef",
        "guardrailTrace": "GuardrailTraceTypeDef",
        "orchestrationTrace": "OrchestrationTraceTypeDef",
        "postProcessingTrace": "PostProcessingTraceTypeDef",
        "preProcessingTrace": "PreProcessingTraceTypeDef",
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
