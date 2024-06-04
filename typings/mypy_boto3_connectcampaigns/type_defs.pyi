"""
Type annotations for connectcampaigns service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectcampaigns.type_defs import AgentlessDialerConfigTypeDef

    data: AgentlessDialerConfigTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    CampaignStateType,
    FailureCodeType,
    GetCampaignStateBatchFailureCodeType,
    InstanceOnboardingJobFailureCodeType,
    InstanceOnboardingJobStatusCodeType,
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
    "AgentlessDialerConfigTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "CampaignFiltersTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteConnectInstanceConfigRequestRequestTypeDef",
    "DeleteInstanceOnboardingJobRequestRequestTypeDef",
    "DescribeCampaignRequestRequestTypeDef",
    "DescribeCampaignResponseTypeDef",
    "DialRequestTypeDef",
    "DialerConfigTypeDef",
    "EncryptionConfigTypeDef",
    "FailedCampaignStateResponseTypeDef",
    "FailedRequestTypeDef",
    "GetCampaignStateBatchRequestRequestTypeDef",
    "GetCampaignStateBatchResponseTypeDef",
    "GetCampaignStateRequestRequestTypeDef",
    "GetCampaignStateResponseTypeDef",
    "GetConnectInstanceConfigRequestRequestTypeDef",
    "GetConnectInstanceConfigResponseTypeDef",
    "GetInstanceOnboardingJobStatusRequestRequestTypeDef",
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    "InstanceConfigTypeDef",
    "InstanceIdFilterTypeDef",
    "InstanceOnboardingJobStatusTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutboundCallConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PauseCampaignRequestRequestTypeDef",
    "PredictiveDialerConfigTypeDef",
    "ProgressiveDialerConfigTypeDef",
    "PutDialRequestBatchRequestRequestTypeDef",
    "PutDialRequestBatchResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeCampaignRequestRequestTypeDef",
    "StartCampaignRequestRequestTypeDef",
    "StartInstanceOnboardingJobRequestRequestTypeDef",
    "StartInstanceOnboardingJobResponseTypeDef",
    "StopCampaignRequestRequestTypeDef",
    "SuccessfulCampaignStateResponseTypeDef",
    "SuccessfulRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignDialerConfigRequestRequestTypeDef",
    "UpdateCampaignNameRequestRequestTypeDef",
    "UpdateCampaignOutboundCallConfigRequestRequestTypeDef",
)

AgentlessDialerConfigTypeDef = TypedDict(
    "AgentlessDialerConfigTypeDef",
    {
        "dialingCapacity": float,
    },
    total=False,
)

_RequiredAnswerMachineDetectionConfigTypeDef = TypedDict(
    "_RequiredAnswerMachineDetectionConfigTypeDef",
    {
        "enableAnswerMachineDetection": bool,
    },
)
_OptionalAnswerMachineDetectionConfigTypeDef = TypedDict(
    "_OptionalAnswerMachineDetectionConfigTypeDef",
    {
        "awaitAnswerMachinePrompt": bool,
    },
    total=False,
)

class AnswerMachineDetectionConfigTypeDef(
    _RequiredAnswerMachineDetectionConfigTypeDef, _OptionalAnswerMachineDetectionConfigTypeDef
):
    pass

CampaignFiltersTypeDef = TypedDict(
    "CampaignFiltersTypeDef",
    {
        "instanceIdFilter": "InstanceIdFilterTypeDef",
    },
    total=False,
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

_RequiredCampaignTypeDef = TypedDict(
    "_RequiredCampaignTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
        "dialerConfig": "DialerConfigTypeDef",
        "outboundCallConfig": "OutboundCallConfigTypeDef",
    },
)
_OptionalCampaignTypeDef = TypedDict(
    "_OptionalCampaignTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CampaignTypeDef(_RequiredCampaignTypeDef, _OptionalCampaignTypeDef):
    pass

_RequiredCreateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "connectInstanceId": str,
        "dialerConfig": "DialerConfigTypeDef",
        "outboundCallConfig": "OutboundCallConfigTypeDef",
    },
)
_OptionalCreateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCampaignRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateCampaignRequestRequestTypeDef(
    _RequiredCreateCampaignRequestRequestTypeDef, _OptionalCreateCampaignRequestRequestTypeDef
):
    pass

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteConnectInstanceConfigRequestRequestTypeDef = TypedDict(
    "DeleteConnectInstanceConfigRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)

DeleteInstanceOnboardingJobRequestRequestTypeDef = TypedDict(
    "DeleteInstanceOnboardingJobRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)

DescribeCampaignRequestRequestTypeDef = TypedDict(
    "DescribeCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeCampaignResponseTypeDef = TypedDict(
    "DescribeCampaignResponseTypeDef",
    {
        "campaign": "CampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DialRequestTypeDef = TypedDict(
    "DialRequestTypeDef",
    {
        "clientToken": str,
        "phoneNumber": str,
        "expirationTime": Union[datetime, str],
        "attributes": Dict[str, str],
    },
)

DialerConfigTypeDef = TypedDict(
    "DialerConfigTypeDef",
    {
        "progressiveDialerConfig": "ProgressiveDialerConfigTypeDef",
        "predictiveDialerConfig": "PredictiveDialerConfigTypeDef",
        "agentlessDialerConfig": "AgentlessDialerConfigTypeDef",
    },
    total=False,
)

_RequiredEncryptionConfigTypeDef = TypedDict(
    "_RequiredEncryptionConfigTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalEncryptionConfigTypeDef = TypedDict(
    "_OptionalEncryptionConfigTypeDef",
    {
        "encryptionType": Literal["KMS"],
        "keyArn": str,
    },
    total=False,
)

class EncryptionConfigTypeDef(_RequiredEncryptionConfigTypeDef, _OptionalEncryptionConfigTypeDef):
    pass

FailedCampaignStateResponseTypeDef = TypedDict(
    "FailedCampaignStateResponseTypeDef",
    {
        "campaignId": str,
        "failureCode": GetCampaignStateBatchFailureCodeType,
    },
    total=False,
)

FailedRequestTypeDef = TypedDict(
    "FailedRequestTypeDef",
    {
        "clientToken": str,
        "id": str,
        "failureCode": FailureCodeType,
    },
    total=False,
)

GetCampaignStateBatchRequestRequestTypeDef = TypedDict(
    "GetCampaignStateBatchRequestRequestTypeDef",
    {
        "campaignIds": List[str],
    },
)

GetCampaignStateBatchResponseTypeDef = TypedDict(
    "GetCampaignStateBatchResponseTypeDef",
    {
        "successfulRequests": List["SuccessfulCampaignStateResponseTypeDef"],
        "failedRequests": List["FailedCampaignStateResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignStateRequestRequestTypeDef = TypedDict(
    "GetCampaignStateRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetCampaignStateResponseTypeDef = TypedDict(
    "GetCampaignStateResponseTypeDef",
    {
        "state": CampaignStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectInstanceConfigRequestRequestTypeDef = TypedDict(
    "GetConnectInstanceConfigRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)

GetConnectInstanceConfigResponseTypeDef = TypedDict(
    "GetConnectInstanceConfigResponseTypeDef",
    {
        "connectInstanceConfig": "InstanceConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceOnboardingJobStatusRequestRequestTypeDef = TypedDict(
    "GetInstanceOnboardingJobStatusRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)

GetInstanceOnboardingJobStatusResponseTypeDef = TypedDict(
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    {
        "connectInstanceOnboardingJobStatus": "InstanceOnboardingJobStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceConfigTypeDef = TypedDict(
    "InstanceConfigTypeDef",
    {
        "connectInstanceId": str,
        "serviceLinkedRoleArn": str,
        "encryptionConfig": "EncryptionConfigTypeDef",
    },
)

InstanceIdFilterTypeDef = TypedDict(
    "InstanceIdFilterTypeDef",
    {
        "value": str,
        "operator": Literal["Eq"],
    },
)

_RequiredInstanceOnboardingJobStatusTypeDef = TypedDict(
    "_RequiredInstanceOnboardingJobStatusTypeDef",
    {
        "connectInstanceId": str,
        "status": InstanceOnboardingJobStatusCodeType,
    },
)
_OptionalInstanceOnboardingJobStatusTypeDef = TypedDict(
    "_OptionalInstanceOnboardingJobStatusTypeDef",
    {
        "failureCode": InstanceOnboardingJobFailureCodeType,
    },
    total=False,
)

class InstanceOnboardingJobStatusTypeDef(
    _RequiredInstanceOnboardingJobStatusTypeDef, _OptionalInstanceOnboardingJobStatusTypeDef
):
    pass

ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filters": "CampaignFiltersTypeDef",
    },
    total=False,
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "nextToken": str,
        "campaignSummaryList": List["CampaignSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "arn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutboundCallConfigTypeDef = TypedDict(
    "_RequiredOutboundCallConfigTypeDef",
    {
        "connectContactFlowId": str,
    },
)
_OptionalOutboundCallConfigTypeDef = TypedDict(
    "_OptionalOutboundCallConfigTypeDef",
    {
        "connectSourcePhoneNumber": str,
        "connectQueueId": str,
        "answerMachineDetectionConfig": "AnswerMachineDetectionConfigTypeDef",
    },
    total=False,
)

class OutboundCallConfigTypeDef(
    _RequiredOutboundCallConfigTypeDef, _OptionalOutboundCallConfigTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PauseCampaignRequestRequestTypeDef = TypedDict(
    "PauseCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)

_RequiredPredictiveDialerConfigTypeDef = TypedDict(
    "_RequiredPredictiveDialerConfigTypeDef",
    {
        "bandwidthAllocation": float,
    },
)
_OptionalPredictiveDialerConfigTypeDef = TypedDict(
    "_OptionalPredictiveDialerConfigTypeDef",
    {
        "dialingCapacity": float,
    },
    total=False,
)

class PredictiveDialerConfigTypeDef(
    _RequiredPredictiveDialerConfigTypeDef, _OptionalPredictiveDialerConfigTypeDef
):
    pass

_RequiredProgressiveDialerConfigTypeDef = TypedDict(
    "_RequiredProgressiveDialerConfigTypeDef",
    {
        "bandwidthAllocation": float,
    },
)
_OptionalProgressiveDialerConfigTypeDef = TypedDict(
    "_OptionalProgressiveDialerConfigTypeDef",
    {
        "dialingCapacity": float,
    },
    total=False,
)

class ProgressiveDialerConfigTypeDef(
    _RequiredProgressiveDialerConfigTypeDef, _OptionalProgressiveDialerConfigTypeDef
):
    pass

PutDialRequestBatchRequestRequestTypeDef = TypedDict(
    "PutDialRequestBatchRequestRequestTypeDef",
    {
        "id": str,
        "dialRequests": List["DialRequestTypeDef"],
    },
)

PutDialRequestBatchResponseTypeDef = TypedDict(
    "PutDialRequestBatchResponseTypeDef",
    {
        "successfulRequests": List["SuccessfulRequestTypeDef"],
        "failedRequests": List["FailedRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ResumeCampaignRequestRequestTypeDef = TypedDict(
    "ResumeCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)

StartCampaignRequestRequestTypeDef = TypedDict(
    "StartCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)

StartInstanceOnboardingJobRequestRequestTypeDef = TypedDict(
    "StartInstanceOnboardingJobRequestRequestTypeDef",
    {
        "connectInstanceId": str,
        "encryptionConfig": "EncryptionConfigTypeDef",
    },
)

StartInstanceOnboardingJobResponseTypeDef = TypedDict(
    "StartInstanceOnboardingJobResponseTypeDef",
    {
        "connectInstanceOnboardingJobStatus": "InstanceOnboardingJobStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopCampaignRequestRequestTypeDef = TypedDict(
    "StopCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)

SuccessfulCampaignStateResponseTypeDef = TypedDict(
    "SuccessfulCampaignStateResponseTypeDef",
    {
        "campaignId": str,
        "state": CampaignStateType,
    },
    total=False,
)

SuccessfulRequestTypeDef = TypedDict(
    "SuccessfulRequestTypeDef",
    {
        "clientToken": str,
        "id": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tagKeys": List[str],
    },
)

UpdateCampaignDialerConfigRequestRequestTypeDef = TypedDict(
    "UpdateCampaignDialerConfigRequestRequestTypeDef",
    {
        "id": str,
        "dialerConfig": "DialerConfigTypeDef",
    },
)

UpdateCampaignNameRequestRequestTypeDef = TypedDict(
    "UpdateCampaignNameRequestRequestTypeDef",
    {
        "id": str,
        "name": str,
    },
)

_RequiredUpdateCampaignOutboundCallConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCampaignOutboundCallConfigRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateCampaignOutboundCallConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCampaignOutboundCallConfigRequestRequestTypeDef",
    {
        "connectContactFlowId": str,
        "connectSourcePhoneNumber": str,
        "answerMachineDetectionConfig": "AnswerMachineDetectionConfigTypeDef",
    },
    total=False,
)

class UpdateCampaignOutboundCallConfigRequestRequestTypeDef(
    _RequiredUpdateCampaignOutboundCallConfigRequestRequestTypeDef,
    _OptionalUpdateCampaignOutboundCallConfigRequestRequestTypeDef,
):
    pass
