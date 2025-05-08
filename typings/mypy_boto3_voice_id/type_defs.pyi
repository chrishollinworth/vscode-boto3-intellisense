"""
Type annotations for voice-id service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_voice_id.type_defs import AssociateFraudsterRequestTypeDef

    data: AssociateFraudsterRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociateFraudsterRequestTypeDef",
    "AssociateFraudsterResponseTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AuthenticationResultTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateWatchlistRequestTypeDef",
    "CreateWatchlistResponseTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteFraudsterRequestTypeDef",
    "DeleteSpeakerRequestTypeDef",
    "DeleteWatchlistRequestTypeDef",
    "DescribeDomainRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeFraudsterRegistrationJobRequestTypeDef",
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    "DescribeFraudsterRequestTypeDef",
    "DescribeFraudsterResponseTypeDef",
    "DescribeSpeakerEnrollmentJobRequestTypeDef",
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    "DescribeSpeakerRequestTypeDef",
    "DescribeSpeakerResponseTypeDef",
    "DescribeWatchlistRequestTypeDef",
    "DescribeWatchlistResponseTypeDef",
    "DisassociateFraudsterRequestTypeDef",
    "DisassociateFraudsterResponseTypeDef",
    "DomainSummaryTypeDef",
    "DomainTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnrollmentConfigOutputTypeDef",
    "EnrollmentConfigTypeDef",
    "EnrollmentConfigUnionTypeDef",
    "EnrollmentJobFraudDetectionConfigOutputTypeDef",
    "EnrollmentJobFraudDetectionConfigTypeDef",
    "EvaluateSessionRequestTypeDef",
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
    "ListDomainsRequestPaginateTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFraudsterRegistrationJobsRequestPaginateTypeDef",
    "ListFraudsterRegistrationJobsRequestTypeDef",
    "ListFraudsterRegistrationJobsResponseTypeDef",
    "ListFraudstersRequestPaginateTypeDef",
    "ListFraudstersRequestTypeDef",
    "ListFraudstersResponseTypeDef",
    "ListSpeakerEnrollmentJobsRequestPaginateTypeDef",
    "ListSpeakerEnrollmentJobsRequestTypeDef",
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    "ListSpeakersRequestPaginateTypeDef",
    "ListSpeakersRequestTypeDef",
    "ListSpeakersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWatchlistsRequestPaginateTypeDef",
    "ListWatchlistsRequestTypeDef",
    "ListWatchlistsResponseTypeDef",
    "OptOutSpeakerRequestTypeDef",
    "OptOutSpeakerResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "RegistrationConfigOutputTypeDef",
    "RegistrationConfigTypeDef",
    "RegistrationConfigUnionTypeDef",
    "ResponseMetadataTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionUpdateDetailsTypeDef",
    "SpeakerEnrollmentJobSummaryTypeDef",
    "SpeakerEnrollmentJobTypeDef",
    "SpeakerSummaryTypeDef",
    "SpeakerTypeDef",
    "StartFraudsterRegistrationJobRequestTypeDef",
    "StartFraudsterRegistrationJobResponseTypeDef",
    "StartSpeakerEnrollmentJobRequestTypeDef",
    "StartSpeakerEnrollmentJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDomainRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateWatchlistRequestTypeDef",
    "UpdateWatchlistResponseTypeDef",
    "VoiceSpoofingRiskTypeDef",
    "WatchlistDetailsTypeDef",
    "WatchlistSummaryTypeDef",
    "WatchlistTypeDef",
)

class AssociateFraudsterRequestTypeDef(TypedDict):
    DomainId: str
    FraudsterId: str
    WatchlistId: str

class FraudsterTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DomainId: NotRequired[str]
    GeneratedFraudsterId: NotRequired[str]
    WatchlistIds: NotRequired[List[str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AuthenticationConfigurationTypeDef(TypedDict):
    AcceptanceThreshold: int

class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    KmsKeyId: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateWatchlistRequestTypeDef(TypedDict):
    DomainId: str
    Name: str
    ClientToken: NotRequired[str]
    Description: NotRequired[str]

class WatchlistTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DefaultWatchlist: NotRequired[bool]
    Description: NotRequired[str]
    DomainId: NotRequired[str]
    Name: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    WatchlistId: NotRequired[str]

class DeleteDomainRequestTypeDef(TypedDict):
    DomainId: str

class DeleteFraudsterRequestTypeDef(TypedDict):
    DomainId: str
    FraudsterId: str

class DeleteSpeakerRequestTypeDef(TypedDict):
    DomainId: str
    SpeakerId: str

class DeleteWatchlistRequestTypeDef(TypedDict):
    DomainId: str
    WatchlistId: str

class DescribeDomainRequestTypeDef(TypedDict):
    DomainId: str

class DescribeFraudsterRegistrationJobRequestTypeDef(TypedDict):
    DomainId: str
    JobId: str

class DescribeFraudsterRequestTypeDef(TypedDict):
    DomainId: str
    FraudsterId: str

class DescribeSpeakerEnrollmentJobRequestTypeDef(TypedDict):
    DomainId: str
    JobId: str

class DescribeSpeakerRequestTypeDef(TypedDict):
    DomainId: str
    SpeakerId: str

class SpeakerTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    CustomerSpeakerId: NotRequired[str]
    DomainId: NotRequired[str]
    GeneratedSpeakerId: NotRequired[str]
    LastAccessedAt: NotRequired[datetime]
    Status: NotRequired[SpeakerStatusType]
    UpdatedAt: NotRequired[datetime]

class DescribeWatchlistRequestTypeDef(TypedDict):
    DomainId: str
    WatchlistId: str

class DisassociateFraudsterRequestTypeDef(TypedDict):
    DomainId: str
    FraudsterId: str
    WatchlistId: str

class ServerSideEncryptionUpdateDetailsTypeDef(TypedDict):
    Message: NotRequired[str]
    OldKmsKeyId: NotRequired[str]
    UpdateStatus: NotRequired[ServerSideEncryptionUpdateStatusType]

class WatchlistDetailsTypeDef(TypedDict):
    DefaultWatchlistId: str

class EnrollmentJobFraudDetectionConfigOutputTypeDef(TypedDict):
    FraudDetectionAction: NotRequired[FraudDetectionActionType]
    RiskThreshold: NotRequired[int]
    WatchlistIds: NotRequired[List[str]]

class EnrollmentJobFraudDetectionConfigTypeDef(TypedDict):
    FraudDetectionAction: NotRequired[FraudDetectionActionType]
    RiskThreshold: NotRequired[int]
    WatchlistIds: NotRequired[Sequence[str]]

class EvaluateSessionRequestTypeDef(TypedDict):
    DomainId: str
    SessionNameOrId: str

class FailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]
    StatusCode: NotRequired[int]

class FraudDetectionConfigurationTypeDef(TypedDict):
    RiskThreshold: NotRequired[int]
    WatchlistId: NotRequired[str]

class KnownFraudsterRiskTypeDef(TypedDict):
    RiskScore: int
    GeneratedFraudsterId: NotRequired[str]

class VoiceSpoofingRiskTypeDef(TypedDict):
    RiskScore: int

class JobProgressTypeDef(TypedDict):
    PercentComplete: NotRequired[int]

class InputDataConfigTypeDef(TypedDict):
    S3Uri: str

class OutputDataConfigTypeDef(TypedDict):
    S3Uri: str
    KmsKeyId: NotRequired[str]

class RegistrationConfigOutputTypeDef(TypedDict):
    DuplicateRegistrationAction: NotRequired[DuplicateRegistrationActionType]
    FraudsterSimilarityThreshold: NotRequired[int]
    WatchlistIds: NotRequired[List[str]]

class FraudsterSummaryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DomainId: NotRequired[str]
    GeneratedFraudsterId: NotRequired[str]
    WatchlistIds: NotRequired[List[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDomainsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListFraudsterRegistrationJobsRequestTypeDef(TypedDict):
    DomainId: str
    JobStatus: NotRequired[FraudsterRegistrationJobStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListFraudstersRequestTypeDef(TypedDict):
    DomainId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    WatchlistId: NotRequired[str]

class ListSpeakerEnrollmentJobsRequestTypeDef(TypedDict):
    DomainId: str
    JobStatus: NotRequired[SpeakerEnrollmentJobStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSpeakersRequestTypeDef(TypedDict):
    DomainId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SpeakerSummaryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    CustomerSpeakerId: NotRequired[str]
    DomainId: NotRequired[str]
    GeneratedSpeakerId: NotRequired[str]
    LastAccessedAt: NotRequired[datetime]
    Status: NotRequired[SpeakerStatusType]
    UpdatedAt: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListWatchlistsRequestTypeDef(TypedDict):
    DomainId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class WatchlistSummaryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DefaultWatchlist: NotRequired[bool]
    Description: NotRequired[str]
    DomainId: NotRequired[str]
    Name: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    WatchlistId: NotRequired[str]

class OptOutSpeakerRequestTypeDef(TypedDict):
    DomainId: str
    SpeakerId: str

class RegistrationConfigTypeDef(TypedDict):
    DuplicateRegistrationAction: NotRequired[DuplicateRegistrationActionType]
    FraudsterSimilarityThreshold: NotRequired[int]
    WatchlistIds: NotRequired[Sequence[str]]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateWatchlistRequestTypeDef(TypedDict):
    DomainId: str
    WatchlistId: str
    Description: NotRequired[str]
    Name: NotRequired[str]

class AssociateFraudsterResponseTypeDef(TypedDict):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFraudsterResponseTypeDef(TypedDict):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFraudsterResponseTypeDef(TypedDict):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class AuthenticationResultTypeDef(TypedDict):
    AudioAggregationEndedAt: NotRequired[datetime]
    AudioAggregationStartedAt: NotRequired[datetime]
    AuthenticationResultId: NotRequired[str]
    Configuration: NotRequired[AuthenticationConfigurationTypeDef]
    CustomerSpeakerId: NotRequired[str]
    Decision: NotRequired[AuthenticationDecisionType]
    GeneratedSpeakerId: NotRequired[str]
    Score: NotRequired[int]

class UpdateDomainRequestTypeDef(TypedDict):
    DomainId: str
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: NotRequired[str]

class CreateDomainRequestTypeDef(TypedDict):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateWatchlistResponseTypeDef(TypedDict):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWatchlistResponseTypeDef(TypedDict):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWatchlistResponseTypeDef(TypedDict):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpeakerResponseTypeDef(TypedDict):
    Speaker: SpeakerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OptOutSpeakerResponseTypeDef(TypedDict):
    Speaker: SpeakerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DomainSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    Description: NotRequired[str]
    DomainId: NotRequired[str]
    DomainStatus: NotRequired[DomainStatusType]
    Name: NotRequired[str]
    ServerSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    ServerSideEncryptionUpdateDetails: NotRequired[ServerSideEncryptionUpdateDetailsTypeDef]
    UpdatedAt: NotRequired[datetime]
    WatchlistDetails: NotRequired[WatchlistDetailsTypeDef]

class DomainTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    Description: NotRequired[str]
    DomainId: NotRequired[str]
    DomainStatus: NotRequired[DomainStatusType]
    Name: NotRequired[str]
    ServerSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    ServerSideEncryptionUpdateDetails: NotRequired[ServerSideEncryptionUpdateDetailsTypeDef]
    UpdatedAt: NotRequired[datetime]
    WatchlistDetails: NotRequired[WatchlistDetailsTypeDef]

class EnrollmentConfigOutputTypeDef(TypedDict):
    ExistingEnrollmentAction: NotRequired[ExistingEnrollmentActionType]
    FraudDetectionConfig: NotRequired[EnrollmentJobFraudDetectionConfigOutputTypeDef]

class EnrollmentConfigTypeDef(TypedDict):
    ExistingEnrollmentAction: NotRequired[ExistingEnrollmentActionType]
    FraudDetectionConfig: NotRequired[EnrollmentJobFraudDetectionConfigTypeDef]

class FraudRiskDetailsTypeDef(TypedDict):
    KnownFraudsterRisk: KnownFraudsterRiskTypeDef
    VoiceSpoofingRisk: VoiceSpoofingRiskTypeDef

class FraudsterRegistrationJobSummaryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DomainId: NotRequired[str]
    EndedAt: NotRequired[datetime]
    FailureDetails: NotRequired[FailureDetailsTypeDef]
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobProgress: NotRequired[JobProgressTypeDef]
    JobStatus: NotRequired[FraudsterRegistrationJobStatusType]

class SpeakerEnrollmentJobSummaryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DomainId: NotRequired[str]
    EndedAt: NotRequired[datetime]
    FailureDetails: NotRequired[FailureDetailsTypeDef]
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobProgress: NotRequired[JobProgressTypeDef]
    JobStatus: NotRequired[SpeakerEnrollmentJobStatusType]

class FraudsterRegistrationJobTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DataAccessRoleArn: NotRequired[str]
    DomainId: NotRequired[str]
    EndedAt: NotRequired[datetime]
    FailureDetails: NotRequired[FailureDetailsTypeDef]
    InputDataConfig: NotRequired[InputDataConfigTypeDef]
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobProgress: NotRequired[JobProgressTypeDef]
    JobStatus: NotRequired[FraudsterRegistrationJobStatusType]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    RegistrationConfig: NotRequired[RegistrationConfigOutputTypeDef]

class ListFraudstersResponseTypeDef(TypedDict):
    FraudsterSummaries: List[FraudsterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDomainsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFraudsterRegistrationJobsRequestPaginateTypeDef(TypedDict):
    DomainId: str
    JobStatus: NotRequired[FraudsterRegistrationJobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFraudstersRequestPaginateTypeDef(TypedDict):
    DomainId: str
    WatchlistId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpeakerEnrollmentJobsRequestPaginateTypeDef(TypedDict):
    DomainId: str
    JobStatus: NotRequired[SpeakerEnrollmentJobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpeakersRequestPaginateTypeDef(TypedDict):
    DomainId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWatchlistsRequestPaginateTypeDef(TypedDict):
    DomainId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpeakersResponseTypeDef(TypedDict):
    SpeakerSummaries: List[SpeakerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWatchlistsResponseTypeDef(TypedDict):
    WatchlistSummaries: List[WatchlistSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

RegistrationConfigUnionTypeDef = Union[RegistrationConfigTypeDef, RegistrationConfigOutputTypeDef]

class ListDomainsResponseTypeDef(TypedDict):
    DomainSummaries: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDomainResponseTypeDef(TypedDict):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResponseTypeDef(TypedDict):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainResponseTypeDef(TypedDict):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpeakerEnrollmentJobTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    DataAccessRoleArn: NotRequired[str]
    DomainId: NotRequired[str]
    EndedAt: NotRequired[datetime]
    EnrollmentConfig: NotRequired[EnrollmentConfigOutputTypeDef]
    FailureDetails: NotRequired[FailureDetailsTypeDef]
    InputDataConfig: NotRequired[InputDataConfigTypeDef]
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobProgress: NotRequired[JobProgressTypeDef]
    JobStatus: NotRequired[SpeakerEnrollmentJobStatusType]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]

EnrollmentConfigUnionTypeDef = Union[EnrollmentConfigTypeDef, EnrollmentConfigOutputTypeDef]

class FraudDetectionResultTypeDef(TypedDict):
    AudioAggregationEndedAt: NotRequired[datetime]
    AudioAggregationStartedAt: NotRequired[datetime]
    Configuration: NotRequired[FraudDetectionConfigurationTypeDef]
    Decision: NotRequired[FraudDetectionDecisionType]
    FraudDetectionResultId: NotRequired[str]
    Reasons: NotRequired[List[FraudDetectionReasonType]]
    RiskDetails: NotRequired[FraudRiskDetailsTypeDef]

class ListFraudsterRegistrationJobsResponseTypeDef(TypedDict):
    JobSummaries: List[FraudsterRegistrationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSpeakerEnrollmentJobsResponseTypeDef(TypedDict):
    JobSummaries: List[SpeakerEnrollmentJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeFraudsterRegistrationJobResponseTypeDef(TypedDict):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartFraudsterRegistrationJobResponseTypeDef(TypedDict):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartFraudsterRegistrationJobRequestTypeDef(TypedDict):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: NotRequired[str]
    JobName: NotRequired[str]
    RegistrationConfig: NotRequired[RegistrationConfigUnionTypeDef]

class DescribeSpeakerEnrollmentJobResponseTypeDef(TypedDict):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerEnrollmentJobResponseTypeDef(TypedDict):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerEnrollmentJobRequestTypeDef(TypedDict):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: NotRequired[str]
    EnrollmentConfig: NotRequired[EnrollmentConfigUnionTypeDef]
    JobName: NotRequired[str]

class EvaluateSessionResponseTypeDef(TypedDict):
    AuthenticationResult: AuthenticationResultTypeDef
    DomainId: str
    FraudDetectionResult: FraudDetectionResultTypeDef
    SessionId: str
    SessionName: str
    StreamingStatus: StreamingStatusType
    ResponseMetadata: ResponseMetadataTypeDef
