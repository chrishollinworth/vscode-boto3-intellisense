"""
Type annotations for voice-id service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/type_defs.html)

Usage::

    ```python
    from mypy_boto3_voice_id.type_defs import AssociateFraudsterRequestRequestTypeDef

    data: AssociateFraudsterRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AuthenticationDecisionType,
    DomainStatusType,
    DuplicateRegistrationActionType,
    ExistingEnrollmentActionType,
    FraudDetectionActionType,
    FraudDetectionDecisionType,
    FraudDetectionReasonType,
    FraudsterRegistrationJobStatusType,
    ServerSideEncryptionUpdateStatusType,
    SpeakerEnrollmentJobStatusType,
    SpeakerStatusType,
    StreamingStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateFraudsterRequestRequestTypeDef",
    "AssociateFraudsterResponseTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AuthenticationResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateWatchlistRequestRequestTypeDef",
    "CreateWatchlistResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteFraudsterRequestRequestTypeDef",
    "DeleteSpeakerRequestRequestTypeDef",
    "DeleteWatchlistRequestRequestTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeFraudsterRegistrationJobRequestRequestTypeDef",
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    "DescribeFraudsterRequestRequestTypeDef",
    "DescribeFraudsterResponseTypeDef",
    "DescribeSpeakerEnrollmentJobRequestRequestTypeDef",
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    "DescribeSpeakerRequestRequestTypeDef",
    "DescribeSpeakerResponseTypeDef",
    "DescribeWatchlistRequestRequestTypeDef",
    "DescribeWatchlistResponseTypeDef",
    "DisassociateFraudsterRequestRequestTypeDef",
    "DisassociateFraudsterResponseTypeDef",
    "DomainSummaryTypeDef",
    "DomainTypeDef",
    "EnrollmentConfigTypeDef",
    "EnrollmentJobFraudDetectionConfigTypeDef",
    "EvaluateSessionRequestRequestTypeDef",
    "EvaluateSessionResponseTypeDef",
    "FailureDetailsTypeDef",
    "FraudDetectionConfigurationTypeDef",
    "FraudDetectionResultTypeDef",
    "FraudRiskDetailsTypeDef",
    "FraudsterRegistrationJobSummaryTypeDef",
    "FraudsterRegistrationJobTypeDef",
    "FraudsterSummaryTypeDef",
    "FraudsterTypeDef",
    "InputDataConfigTypeDef",
    "JobProgressTypeDef",
    "KnownFraudsterRiskTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFraudsterRegistrationJobsRequestRequestTypeDef",
    "ListFraudsterRegistrationJobsResponseTypeDef",
    "ListFraudstersRequestRequestTypeDef",
    "ListFraudstersResponseTypeDef",
    "ListSpeakerEnrollmentJobsRequestRequestTypeDef",
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    "ListSpeakersRequestRequestTypeDef",
    "ListSpeakersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWatchlistsRequestRequestTypeDef",
    "ListWatchlistsResponseTypeDef",
    "OptOutSpeakerRequestRequestTypeDef",
    "OptOutSpeakerResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "RegistrationConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionUpdateDetailsTypeDef",
    "SpeakerEnrollmentJobSummaryTypeDef",
    "SpeakerEnrollmentJobTypeDef",
    "SpeakerSummaryTypeDef",
    "SpeakerTypeDef",
    "StartFraudsterRegistrationJobRequestRequestTypeDef",
    "StartFraudsterRegistrationJobResponseTypeDef",
    "StartSpeakerEnrollmentJobRequestRequestTypeDef",
    "StartSpeakerEnrollmentJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateWatchlistRequestRequestTypeDef",
    "UpdateWatchlistResponseTypeDef",
    "VoiceSpoofingRiskTypeDef",
    "WatchlistDetailsTypeDef",
    "WatchlistSummaryTypeDef",
    "WatchlistTypeDef",
)

AssociateFraudsterRequestRequestTypeDef = TypedDict(
    "AssociateFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
        "WatchlistId": str,
    },
)

AssociateFraudsterResponseTypeDef = TypedDict(
    "AssociateFraudsterResponseTypeDef",
    {
        "Fraudster": "FraudsterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "AcceptanceThreshold": int,
    },
)

AuthenticationResultTypeDef = TypedDict(
    "AuthenticationResultTypeDef",
    {
        "AudioAggregationEndedAt": datetime,
        "AudioAggregationStartedAt": datetime,
        "AuthenticationResultId": str,
        "Configuration": "AuthenticationConfigurationTypeDef",
        "CustomerSpeakerId": str,
        "Decision": AuthenticationDecisionType,
        "GeneratedSpeakerId": str,
        "Score": int,
    },
    total=False,
)

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "Name": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "Domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWatchlistRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "Name": str,
    },
)
_OptionalCreateWatchlistRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWatchlistRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
    },
    total=False,
)

class CreateWatchlistRequestRequestTypeDef(
    _RequiredCreateWatchlistRequestRequestTypeDef, _OptionalCreateWatchlistRequestRequestTypeDef
):
    pass

CreateWatchlistResponseTypeDef = TypedDict(
    "CreateWatchlistResponseTypeDef",
    {
        "Watchlist": "WatchlistTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

DeleteFraudsterRequestRequestTypeDef = TypedDict(
    "DeleteFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
    },
)

DeleteSpeakerRequestRequestTypeDef = TypedDict(
    "DeleteSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)

DeleteWatchlistRequestRequestTypeDef = TypedDict(
    "DeleteWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "WatchlistId": str,
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "Domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "DescribeFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobId": str,
    },
)

DescribeFraudsterRegistrationJobResponseTypeDef = TypedDict(
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    {
        "Job": "FraudsterRegistrationJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFraudsterRequestRequestTypeDef = TypedDict(
    "DescribeFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
    },
)

DescribeFraudsterResponseTypeDef = TypedDict(
    "DescribeFraudsterResponseTypeDef",
    {
        "Fraudster": "FraudsterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "DescribeSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobId": str,
    },
)

DescribeSpeakerEnrollmentJobResponseTypeDef = TypedDict(
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    {
        "Job": "SpeakerEnrollmentJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpeakerRequestRequestTypeDef = TypedDict(
    "DescribeSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)

DescribeSpeakerResponseTypeDef = TypedDict(
    "DescribeSpeakerResponseTypeDef",
    {
        "Speaker": "SpeakerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWatchlistRequestRequestTypeDef = TypedDict(
    "DescribeWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "WatchlistId": str,
    },
)

DescribeWatchlistResponseTypeDef = TypedDict(
    "DescribeWatchlistResponseTypeDef",
    {
        "Watchlist": "WatchlistTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateFraudsterRequestRequestTypeDef = TypedDict(
    "DisassociateFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
        "WatchlistId": str,
    },
)

DisassociateFraudsterResponseTypeDef = TypedDict(
    "DisassociateFraudsterResponseTypeDef",
    {
        "Fraudster": "FraudsterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "DomainId": str,
        "DomainStatus": DomainStatusType,
        "Name": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ServerSideEncryptionUpdateDetails": "ServerSideEncryptionUpdateDetailsTypeDef",
        "UpdatedAt": datetime,
        "WatchlistDetails": "WatchlistDetailsTypeDef",
    },
    total=False,
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "DomainId": str,
        "DomainStatus": DomainStatusType,
        "Name": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ServerSideEncryptionUpdateDetails": "ServerSideEncryptionUpdateDetailsTypeDef",
        "UpdatedAt": datetime,
        "WatchlistDetails": "WatchlistDetailsTypeDef",
    },
    total=False,
)

EnrollmentConfigTypeDef = TypedDict(
    "EnrollmentConfigTypeDef",
    {
        "ExistingEnrollmentAction": ExistingEnrollmentActionType,
        "FraudDetectionConfig": "EnrollmentJobFraudDetectionConfigTypeDef",
    },
    total=False,
)

EnrollmentJobFraudDetectionConfigTypeDef = TypedDict(
    "EnrollmentJobFraudDetectionConfigTypeDef",
    {
        "FraudDetectionAction": FraudDetectionActionType,
        "RiskThreshold": int,
        "WatchlistIds": List[str],
    },
    total=False,
)

EvaluateSessionRequestRequestTypeDef = TypedDict(
    "EvaluateSessionRequestRequestTypeDef",
    {
        "DomainId": str,
        "SessionNameOrId": str,
    },
)

EvaluateSessionResponseTypeDef = TypedDict(
    "EvaluateSessionResponseTypeDef",
    {
        "AuthenticationResult": "AuthenticationResultTypeDef",
        "DomainId": str,
        "FraudDetectionResult": "FraudDetectionResultTypeDef",
        "SessionId": str,
        "SessionName": str,
        "StreamingStatus": StreamingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Message": str,
        "StatusCode": int,
    },
    total=False,
)

FraudDetectionConfigurationTypeDef = TypedDict(
    "FraudDetectionConfigurationTypeDef",
    {
        "RiskThreshold": int,
        "WatchlistId": str,
    },
    total=False,
)

FraudDetectionResultTypeDef = TypedDict(
    "FraudDetectionResultTypeDef",
    {
        "AudioAggregationEndedAt": datetime,
        "AudioAggregationStartedAt": datetime,
        "Configuration": "FraudDetectionConfigurationTypeDef",
        "Decision": FraudDetectionDecisionType,
        "FraudDetectionResultId": str,
        "Reasons": List[FraudDetectionReasonType],
        "RiskDetails": "FraudRiskDetailsTypeDef",
    },
    total=False,
)

FraudRiskDetailsTypeDef = TypedDict(
    "FraudRiskDetailsTypeDef",
    {
        "KnownFraudsterRisk": "KnownFraudsterRiskTypeDef",
        "VoiceSpoofingRisk": "VoiceSpoofingRiskTypeDef",
    },
)

FraudsterRegistrationJobSummaryTypeDef = TypedDict(
    "FraudsterRegistrationJobSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "DomainId": str,
        "EndedAt": datetime,
        "FailureDetails": "FailureDetailsTypeDef",
        "JobId": str,
        "JobName": str,
        "JobProgress": "JobProgressTypeDef",
        "JobStatus": FraudsterRegistrationJobStatusType,
    },
    total=False,
)

FraudsterRegistrationJobTypeDef = TypedDict(
    "FraudsterRegistrationJobTypeDef",
    {
        "CreatedAt": datetime,
        "DataAccessRoleArn": str,
        "DomainId": str,
        "EndedAt": datetime,
        "FailureDetails": "FailureDetailsTypeDef",
        "InputDataConfig": "InputDataConfigTypeDef",
        "JobId": str,
        "JobName": str,
        "JobProgress": "JobProgressTypeDef",
        "JobStatus": FraudsterRegistrationJobStatusType,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "RegistrationConfig": "RegistrationConfigTypeDef",
    },
    total=False,
)

FraudsterSummaryTypeDef = TypedDict(
    "FraudsterSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "DomainId": str,
        "GeneratedFraudsterId": str,
        "WatchlistIds": List[str],
    },
    total=False,
)

FraudsterTypeDef = TypedDict(
    "FraudsterTypeDef",
    {
        "CreatedAt": datetime,
        "DomainId": str,
        "GeneratedFraudsterId": str,
        "WatchlistIds": List[str],
    },
    total=False,
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)

JobProgressTypeDef = TypedDict(
    "JobProgressTypeDef",
    {
        "PercentComplete": int,
    },
    total=False,
)

_RequiredKnownFraudsterRiskTypeDef = TypedDict(
    "_RequiredKnownFraudsterRiskTypeDef",
    {
        "RiskScore": int,
    },
)
_OptionalKnownFraudsterRiskTypeDef = TypedDict(
    "_OptionalKnownFraudsterRiskTypeDef",
    {
        "GeneratedFraudsterId": str,
    },
    total=False,
)

class KnownFraudsterRiskTypeDef(
    _RequiredKnownFraudsterRiskTypeDef, _OptionalKnownFraudsterRiskTypeDef
):
    pass

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "DomainSummaries": List["DomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFraudsterRegistrationJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListFraudsterRegistrationJobsRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalListFraudsterRegistrationJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListFraudsterRegistrationJobsRequestRequestTypeDef",
    {
        "JobStatus": FraudsterRegistrationJobStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListFraudsterRegistrationJobsRequestRequestTypeDef(
    _RequiredListFraudsterRegistrationJobsRequestRequestTypeDef,
    _OptionalListFraudsterRegistrationJobsRequestRequestTypeDef,
):
    pass

ListFraudsterRegistrationJobsResponseTypeDef = TypedDict(
    "ListFraudsterRegistrationJobsResponseTypeDef",
    {
        "JobSummaries": List["FraudsterRegistrationJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFraudstersRequestRequestTypeDef = TypedDict(
    "_RequiredListFraudstersRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalListFraudstersRequestRequestTypeDef = TypedDict(
    "_OptionalListFraudstersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "WatchlistId": str,
    },
    total=False,
)

class ListFraudstersRequestRequestTypeDef(
    _RequiredListFraudstersRequestRequestTypeDef, _OptionalListFraudstersRequestRequestTypeDef
):
    pass

ListFraudstersResponseTypeDef = TypedDict(
    "ListFraudstersResponseTypeDef",
    {
        "FraudsterSummaries": List["FraudsterSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSpeakerEnrollmentJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListSpeakerEnrollmentJobsRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalListSpeakerEnrollmentJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListSpeakerEnrollmentJobsRequestRequestTypeDef",
    {
        "JobStatus": SpeakerEnrollmentJobStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSpeakerEnrollmentJobsRequestRequestTypeDef(
    _RequiredListSpeakerEnrollmentJobsRequestRequestTypeDef,
    _OptionalListSpeakerEnrollmentJobsRequestRequestTypeDef,
):
    pass

ListSpeakerEnrollmentJobsResponseTypeDef = TypedDict(
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    {
        "JobSummaries": List["SpeakerEnrollmentJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSpeakersRequestRequestTypeDef = TypedDict(
    "_RequiredListSpeakersRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalListSpeakersRequestRequestTypeDef = TypedDict(
    "_OptionalListSpeakersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSpeakersRequestRequestTypeDef(
    _RequiredListSpeakersRequestRequestTypeDef, _OptionalListSpeakersRequestRequestTypeDef
):
    pass

ListSpeakersResponseTypeDef = TypedDict(
    "ListSpeakersResponseTypeDef",
    {
        "NextToken": str,
        "SpeakerSummaries": List["SpeakerSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWatchlistsRequestRequestTypeDef = TypedDict(
    "_RequiredListWatchlistsRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalListWatchlistsRequestRequestTypeDef = TypedDict(
    "_OptionalListWatchlistsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListWatchlistsRequestRequestTypeDef(
    _RequiredListWatchlistsRequestRequestTypeDef, _OptionalListWatchlistsRequestRequestTypeDef
):
    pass

ListWatchlistsResponseTypeDef = TypedDict(
    "ListWatchlistsResponseTypeDef",
    {
        "NextToken": str,
        "WatchlistSummaries": List["WatchlistSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptOutSpeakerRequestRequestTypeDef = TypedDict(
    "OptOutSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)

OptOutSpeakerResponseTypeDef = TypedDict(
    "OptOutSpeakerResponseTypeDef",
    {
        "Speaker": "SpeakerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
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

RegistrationConfigTypeDef = TypedDict(
    "RegistrationConfigTypeDef",
    {
        "DuplicateRegistrationAction": DuplicateRegistrationActionType,
        "FraudsterSimilarityThreshold": int,
        "WatchlistIds": List[str],
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

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
)

ServerSideEncryptionUpdateDetailsTypeDef = TypedDict(
    "ServerSideEncryptionUpdateDetailsTypeDef",
    {
        "Message": str,
        "OldKmsKeyId": str,
        "UpdateStatus": ServerSideEncryptionUpdateStatusType,
    },
    total=False,
)

SpeakerEnrollmentJobSummaryTypeDef = TypedDict(
    "SpeakerEnrollmentJobSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "DomainId": str,
        "EndedAt": datetime,
        "FailureDetails": "FailureDetailsTypeDef",
        "JobId": str,
        "JobName": str,
        "JobProgress": "JobProgressTypeDef",
        "JobStatus": SpeakerEnrollmentJobStatusType,
    },
    total=False,
)

SpeakerEnrollmentJobTypeDef = TypedDict(
    "SpeakerEnrollmentJobTypeDef",
    {
        "CreatedAt": datetime,
        "DataAccessRoleArn": str,
        "DomainId": str,
        "EndedAt": datetime,
        "EnrollmentConfig": "EnrollmentConfigTypeDef",
        "FailureDetails": "FailureDetailsTypeDef",
        "InputDataConfig": "InputDataConfigTypeDef",
        "JobId": str,
        "JobName": str,
        "JobProgress": "JobProgressTypeDef",
        "JobStatus": SpeakerEnrollmentJobStatusType,
        "OutputDataConfig": "OutputDataConfigTypeDef",
    },
    total=False,
)

SpeakerSummaryTypeDef = TypedDict(
    "SpeakerSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "CustomerSpeakerId": str,
        "DomainId": str,
        "GeneratedSpeakerId": str,
        "LastAccessedAt": datetime,
        "Status": SpeakerStatusType,
        "UpdatedAt": datetime,
    },
    total=False,
)

SpeakerTypeDef = TypedDict(
    "SpeakerTypeDef",
    {
        "CreatedAt": datetime,
        "CustomerSpeakerId": str,
        "DomainId": str,
        "GeneratedSpeakerId": str,
        "LastAccessedAt": datetime,
        "Status": SpeakerStatusType,
        "UpdatedAt": datetime,
    },
    total=False,
)

_RequiredStartFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "DataAccessRoleArn": str,
        "DomainId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
    },
)
_OptionalStartFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "JobName": str,
        "RegistrationConfig": "RegistrationConfigTypeDef",
    },
    total=False,
)

class StartFraudsterRegistrationJobRequestRequestTypeDef(
    _RequiredStartFraudsterRegistrationJobRequestRequestTypeDef,
    _OptionalStartFraudsterRegistrationJobRequestRequestTypeDef,
):
    pass

StartFraudsterRegistrationJobResponseTypeDef = TypedDict(
    "StartFraudsterRegistrationJobResponseTypeDef",
    {
        "Job": "FraudsterRegistrationJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "DataAccessRoleArn": str,
        "DomainId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
    },
)
_OptionalStartSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "EnrollmentConfig": "EnrollmentConfigTypeDef",
        "JobName": str,
    },
    total=False,
)

class StartSpeakerEnrollmentJobRequestRequestTypeDef(
    _RequiredStartSpeakerEnrollmentJobRequestRequestTypeDef,
    _OptionalStartSpeakerEnrollmentJobRequestRequestTypeDef,
):
    pass

StartSpeakerEnrollmentJobResponseTypeDef = TypedDict(
    "StartSpeakerEnrollmentJobResponseTypeDef",
    {
        "Job": "SpeakerEnrollmentJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainRequestRequestTypeDef",
    {
        "DomainId": str,
        "Name": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
    },
)
_OptionalUpdateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateDomainRequestRequestTypeDef(
    _RequiredUpdateDomainRequestRequestTypeDef, _OptionalUpdateDomainRequestRequestTypeDef
):
    pass

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "Domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWatchlistRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "WatchlistId": str,
    },
)
_OptionalUpdateWatchlistRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWatchlistRequestRequestTypeDef",
    {
        "Description": str,
        "Name": str,
    },
    total=False,
)

class UpdateWatchlistRequestRequestTypeDef(
    _RequiredUpdateWatchlistRequestRequestTypeDef, _OptionalUpdateWatchlistRequestRequestTypeDef
):
    pass

UpdateWatchlistResponseTypeDef = TypedDict(
    "UpdateWatchlistResponseTypeDef",
    {
        "Watchlist": "WatchlistTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceSpoofingRiskTypeDef = TypedDict(
    "VoiceSpoofingRiskTypeDef",
    {
        "RiskScore": int,
    },
)

WatchlistDetailsTypeDef = TypedDict(
    "WatchlistDetailsTypeDef",
    {
        "DefaultWatchlistId": str,
    },
)

WatchlistSummaryTypeDef = TypedDict(
    "WatchlistSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "DefaultWatchlist": bool,
        "Description": str,
        "DomainId": str,
        "Name": str,
        "UpdatedAt": datetime,
        "WatchlistId": str,
    },
    total=False,
)

WatchlistTypeDef = TypedDict(
    "WatchlistTypeDef",
    {
        "CreatedAt": datetime,
        "DefaultWatchlist": bool,
        "Description": str,
        "DomainId": str,
        "Name": str,
        "UpdatedAt": datetime,
        "WatchlistId": str,
    },
    total=False,
)
