"""
Type annotations for connectcampaigns service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_connectcampaigns.type_defs import AgentlessDialerConfigTypeDef

    data: AgentlessDialerConfigTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CampaignStateType,
    FailureCodeType,
    GetCampaignStateBatchFailureCodeType,
    InstanceOnboardingJobFailureCodeType,
    InstanceOnboardingJobStatusCodeType,
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
    "AgentlessDialerConfigTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "CampaignFiltersTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CreateCampaignRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "DeleteCampaignRequestTypeDef",
    "DeleteConnectInstanceConfigRequestTypeDef",
    "DeleteInstanceOnboardingJobRequestTypeDef",
    "DescribeCampaignRequestTypeDef",
    "DescribeCampaignResponseTypeDef",
    "DialRequestTypeDef",
    "DialerConfigTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigTypeDef",
    "FailedCampaignStateResponseTypeDef",
    "FailedRequestTypeDef",
    "GetCampaignStateBatchRequestTypeDef",
    "GetCampaignStateBatchResponseTypeDef",
    "GetCampaignStateRequestTypeDef",
    "GetCampaignStateResponseTypeDef",
    "GetConnectInstanceConfigRequestTypeDef",
    "GetConnectInstanceConfigResponseTypeDef",
    "GetInstanceOnboardingJobStatusRequestTypeDef",
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    "InstanceConfigTypeDef",
    "InstanceIdFilterTypeDef",
    "InstanceOnboardingJobStatusTypeDef",
    "ListCampaignsRequestPaginateTypeDef",
    "ListCampaignsRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutboundCallConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PauseCampaignRequestTypeDef",
    "PredictiveDialerConfigTypeDef",
    "ProgressiveDialerConfigTypeDef",
    "PutDialRequestBatchRequestTypeDef",
    "PutDialRequestBatchResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeCampaignRequestTypeDef",
    "StartCampaignRequestTypeDef",
    "StartInstanceOnboardingJobRequestTypeDef",
    "StartInstanceOnboardingJobResponseTypeDef",
    "StopCampaignRequestTypeDef",
    "SuccessfulCampaignStateResponseTypeDef",
    "SuccessfulRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCampaignDialerConfigRequestTypeDef",
    "UpdateCampaignNameRequestTypeDef",
    "UpdateCampaignOutboundCallConfigRequestTypeDef",
)

class AgentlessDialerConfigTypeDef(TypedDict):
    dialingCapacity: NotRequired[float]

class AnswerMachineDetectionConfigTypeDef(TypedDict):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: NotRequired[bool]

InstanceIdFilterTypeDef = TypedDict(
    "InstanceIdFilterTypeDef",
    {
        "value": str,
        "operator": Literal["Eq"],
    },
)
CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DeleteCampaignRequestTypeDef = TypedDict(
    "DeleteCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteConnectInstanceConfigRequestTypeDef(TypedDict):
    connectInstanceId: str

class DeleteInstanceOnboardingJobRequestTypeDef(TypedDict):
    connectInstanceId: str

DescribeCampaignRequestTypeDef = TypedDict(
    "DescribeCampaignRequestTypeDef",
    {
        "id": str,
    },
)
TimestampTypeDef = Union[datetime, str]

class PredictiveDialerConfigTypeDef(TypedDict):
    bandwidthAllocation: float
    dialingCapacity: NotRequired[float]

class ProgressiveDialerConfigTypeDef(TypedDict):
    bandwidthAllocation: float
    dialingCapacity: NotRequired[float]

class EncryptionConfigTypeDef(TypedDict):
    enabled: bool
    encryptionType: NotRequired[Literal["KMS"]]
    keyArn: NotRequired[str]

class FailedCampaignStateResponseTypeDef(TypedDict):
    campaignId: NotRequired[str]
    failureCode: NotRequired[GetCampaignStateBatchFailureCodeType]

FailedRequestTypeDef = TypedDict(
    "FailedRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
        "failureCode": NotRequired[FailureCodeType],
    },
)

class GetCampaignStateBatchRequestTypeDef(TypedDict):
    campaignIds: Sequence[str]

class SuccessfulCampaignStateResponseTypeDef(TypedDict):
    campaignId: NotRequired[str]
    state: NotRequired[CampaignStateType]

GetCampaignStateRequestTypeDef = TypedDict(
    "GetCampaignStateRequestTypeDef",
    {
        "id": str,
    },
)

class GetConnectInstanceConfigRequestTypeDef(TypedDict):
    connectInstanceId: str

class GetInstanceOnboardingJobStatusRequestTypeDef(TypedDict):
    connectInstanceId: str

class InstanceOnboardingJobStatusTypeDef(TypedDict):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: NotRequired[InstanceOnboardingJobFailureCodeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    arn: str

PauseCampaignRequestTypeDef = TypedDict(
    "PauseCampaignRequestTypeDef",
    {
        "id": str,
    },
)
SuccessfulRequestTypeDef = TypedDict(
    "SuccessfulRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
    },
)
ResumeCampaignRequestTypeDef = TypedDict(
    "ResumeCampaignRequestTypeDef",
    {
        "id": str,
    },
)
StartCampaignRequestTypeDef = TypedDict(
    "StartCampaignRequestTypeDef",
    {
        "id": str,
    },
)
StopCampaignRequestTypeDef = TypedDict(
    "StopCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class TagResourceRequestTypeDef(TypedDict):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    arn: str
    tagKeys: Sequence[str]

UpdateCampaignNameRequestTypeDef = TypedDict(
    "UpdateCampaignNameRequestTypeDef",
    {
        "id": str,
        "name": str,
    },
)

class OutboundCallConfigTypeDef(TypedDict):
    connectContactFlowId: str
    connectSourcePhoneNumber: NotRequired[str]
    connectQueueId: NotRequired[str]
    answerMachineDetectionConfig: NotRequired[AnswerMachineDetectionConfigTypeDef]

UpdateCampaignOutboundCallConfigRequestTypeDef = TypedDict(
    "UpdateCampaignOutboundCallConfigRequestTypeDef",
    {
        "id": str,
        "connectContactFlowId": NotRequired[str],
        "connectSourcePhoneNumber": NotRequired[str],
        "answerMachineDetectionConfig": NotRequired[AnswerMachineDetectionConfigTypeDef],
    },
)

class CampaignFiltersTypeDef(TypedDict):
    instanceIdFilter: NotRequired[InstanceIdFilterTypeDef]

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignStateResponseTypeDef(TypedDict):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsResponseTypeDef(TypedDict):
    campaignSummaryList: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DialRequestTypeDef(TypedDict):
    clientToken: str
    phoneNumber: str
    expirationTime: TimestampTypeDef
    attributes: Mapping[str, str]

class DialerConfigTypeDef(TypedDict):
    progressiveDialerConfig: NotRequired[ProgressiveDialerConfigTypeDef]
    predictiveDialerConfig: NotRequired[PredictiveDialerConfigTypeDef]
    agentlessDialerConfig: NotRequired[AgentlessDialerConfigTypeDef]

class InstanceConfigTypeDef(TypedDict):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfigTypeDef

class StartInstanceOnboardingJobRequestTypeDef(TypedDict):
    connectInstanceId: str
    encryptionConfig: EncryptionConfigTypeDef

class GetCampaignStateBatchResponseTypeDef(TypedDict):
    successfulRequests: List[SuccessfulCampaignStateResponseTypeDef]
    failedRequests: List[FailedCampaignStateResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceOnboardingJobStatusResponseTypeDef(TypedDict):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceOnboardingJobResponseTypeDef(TypedDict):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDialRequestBatchResponseTypeDef(TypedDict):
    successfulRequests: List[SuccessfulRequestTypeDef]
    failedRequests: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[CampaignFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCampaignsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[CampaignFiltersTypeDef]

PutDialRequestBatchRequestTypeDef = TypedDict(
    "PutDialRequestBatchRequestTypeDef",
    {
        "id": str,
        "dialRequests": Sequence[DialRequestTypeDef],
    },
)
CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
        "dialerConfig": DialerConfigTypeDef,
        "outboundCallConfig": OutboundCallConfigTypeDef,
        "tags": NotRequired[Dict[str, str]],
    },
)

class CreateCampaignRequestTypeDef(TypedDict):
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfigTypeDef
    outboundCallConfig: OutboundCallConfigTypeDef
    tags: NotRequired[Mapping[str, str]]

UpdateCampaignDialerConfigRequestTypeDef = TypedDict(
    "UpdateCampaignDialerConfigRequestTypeDef",
    {
        "id": str,
        "dialerConfig": DialerConfigTypeDef,
    },
)

class GetConnectInstanceConfigResponseTypeDef(TypedDict):
    connectInstanceConfig: InstanceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCampaignResponseTypeDef(TypedDict):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
