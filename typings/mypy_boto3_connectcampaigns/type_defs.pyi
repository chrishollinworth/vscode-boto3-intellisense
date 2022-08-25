"""
Type annotations for connectcampaigns service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectcampaigns.type_defs import AnswerMachineDetectionConfigTypeDef

    data: AnswerMachineDetectionConfigTypeDef = {...}
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

AnswerMachineDetectionConfigTypeDef = TypedDict(
    "AnswerMachineDetectionConfigTypeDef",
    {
        "enableAnswerMachineDetection": bool,
    },
)

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
        "arn": str,
        "connectInstanceId": str,
        "id": str,
        "name": str,
    },
)

_RequiredCampaignTypeDef = TypedDict(
    "_RequiredCampaignTypeDef",
    {
        "arn": str,
        "connectInstanceId": str,
        "dialerConfig": "DialerConfigTypeDef",
        "id": str,
        "name": str,
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
        "connectInstanceId": str,
        "dialerConfig": "DialerConfigTypeDef",
        "name": str,
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
        "arn": str,
        "id": str,
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
        "attributes": Dict[str, str],
        "clientToken": str,
        "expirationTime": Union[datetime, str],
        "phoneNumber": str,
    },
)

DialerConfigTypeDef = TypedDict(
    "DialerConfigTypeDef",
    {
        "predictiveDialerConfig": "PredictiveDialerConfigTypeDef",
        "progressiveDialerConfig": "ProgressiveDialerConfigTypeDef",
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
        "failureCode": FailureCodeType,
        "id": str,
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
        "failedRequests": List["FailedCampaignStateResponseTypeDef"],
        "successfulRequests": List["SuccessfulCampaignStateResponseTypeDef"],
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
        "encryptionConfig": "EncryptionConfigTypeDef",
        "serviceLinkedRoleArn": str,
    },
)

InstanceIdFilterTypeDef = TypedDict(
    "InstanceIdFilterTypeDef",
    {
        "operator": Literal["Eq"],
        "value": str,
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
        "filters": "CampaignFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaignSummaryList": List["CampaignSummaryTypeDef"],
        "nextToken": str,
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
        "connectQueueId": str,
    },
)
_OptionalOutboundCallConfigTypeDef = TypedDict(
    "_OptionalOutboundCallConfigTypeDef",
    {
        "answerMachineDetectionConfig": "AnswerMachineDetectionConfigTypeDef",
        "connectSourcePhoneNumber": str,
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

PredictiveDialerConfigTypeDef = TypedDict(
    "PredictiveDialerConfigTypeDef",
    {
        "bandwidthAllocation": float,
    },
)

ProgressiveDialerConfigTypeDef = TypedDict(
    "ProgressiveDialerConfigTypeDef",
    {
        "bandwidthAllocation": float,
    },
)

PutDialRequestBatchRequestRequestTypeDef = TypedDict(
    "PutDialRequestBatchRequestRequestTypeDef",
    {
        "dialRequests": List["DialRequestTypeDef"],
        "id": str,
    },
)

PutDialRequestBatchResponseTypeDef = TypedDict(
    "PutDialRequestBatchResponseTypeDef",
    {
        "failedRequests": List["FailedRequestTypeDef"],
        "successfulRequests": List["SuccessfulRequestTypeDef"],
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
        "dialerConfig": "DialerConfigTypeDef",
        "id": str,
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
        "answerMachineDetectionConfig": "AnswerMachineDetectionConfigTypeDef",
        "connectContactFlowId": str,
        "connectSourcePhoneNumber": str,
    },
    total=False,
)

class UpdateCampaignOutboundCallConfigRequestRequestTypeDef(
    _RequiredUpdateCampaignOutboundCallConfigRequestRequestTypeDef,
    _OptionalUpdateCampaignOutboundCallConfigRequestRequestTypeDef,
):
    pass
