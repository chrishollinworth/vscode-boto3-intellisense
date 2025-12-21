"""
Type annotations for mpa service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mpa.type_defs import MofNApprovalStrategyTypeDef

    data: MofNApprovalStrategyTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ApprovalTeamStatusCodeType,
    ApprovalTeamStatusType,
    FilterFieldType,
    IdentitySourceStatusCodeType,
    IdentitySourceStatusType,
    IdentityStatusType,
    OperatorType,
    PolicyStatusType,
    PolicyTypeType,
    SessionExecutionStatusType,
    SessionResponseType,
    SessionStatusCodeType,
    SessionStatusType,
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
    "ApprovalStrategyResponseTypeDef",
    "ApprovalStrategyTypeDef",
    "ApprovalTeamRequestApproverTypeDef",
    "CancelSessionRequestTypeDef",
    "CreateApprovalTeamRequestTypeDef",
    "CreateApprovalTeamResponseTypeDef",
    "CreateIdentitySourceRequestTypeDef",
    "CreateIdentitySourceResponseTypeDef",
    "DeleteIdentitySourceRequestTypeDef",
    "DeleteInactiveApprovalTeamVersionRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FilterTypeDef",
    "GetApprovalTeamRequestTypeDef",
    "GetApprovalTeamResponseApproverTypeDef",
    "GetApprovalTeamResponseTypeDef",
    "GetIdentitySourceRequestTypeDef",
    "GetIdentitySourceResponseTypeDef",
    "GetPolicyVersionRequestTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseApproverResponseTypeDef",
    "GetSessionResponseTypeDef",
    "IamIdentityCenterForGetTypeDef",
    "IamIdentityCenterForListTypeDef",
    "IamIdentityCenterTypeDef",
    "IdentitySourceForListTypeDef",
    "IdentitySourceParametersForGetTypeDef",
    "IdentitySourceParametersForListTypeDef",
    "IdentitySourceParametersTypeDef",
    "ListApprovalTeamsRequestPaginateTypeDef",
    "ListApprovalTeamsRequestTypeDef",
    "ListApprovalTeamsResponseApprovalTeamTypeDef",
    "ListApprovalTeamsResponseTypeDef",
    "ListIdentitySourcesRequestPaginateTypeDef",
    "ListIdentitySourcesRequestTypeDef",
    "ListIdentitySourcesResponseTypeDef",
    "ListPoliciesRequestPaginateTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyVersionsRequestPaginateTypeDef",
    "ListPolicyVersionsRequestTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListResourcePoliciesRequestPaginateTypeDef",
    "ListResourcePoliciesRequestTypeDef",
    "ListResourcePoliciesResponseResourcePolicyTypeDef",
    "ListResourcePoliciesResponseTypeDef",
    "ListSessionsRequestPaginateTypeDef",
    "ListSessionsRequestTypeDef",
    "ListSessionsResponseSessionTypeDef",
    "ListSessionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MofNApprovalStrategyTypeDef",
    "PaginatorConfigTypeDef",
    "PendingUpdateTypeDef",
    "PolicyReferenceTypeDef",
    "PolicyTypeDef",
    "PolicyVersionSummaryTypeDef",
    "PolicyVersionTypeDef",
    "ResponseMetadataTypeDef",
    "StartActiveApprovalTeamDeletionRequestTypeDef",
    "StartActiveApprovalTeamDeletionResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApprovalTeamRequestTypeDef",
    "UpdateApprovalTeamResponseTypeDef",
)

class MofNApprovalStrategyTypeDef(TypedDict):
    MinApprovalsRequired: int

class ApprovalTeamRequestApproverTypeDef(TypedDict):
    PrimaryIdentityId: str
    PrimaryIdentitySourceArn: str

class CancelSessionRequestTypeDef(TypedDict):
    SessionArn: str

class PolicyReferenceTypeDef(TypedDict):
    PolicyArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteIdentitySourceRequestTypeDef(TypedDict):
    IdentitySourceArn: str

class DeleteInactiveApprovalTeamVersionRequestTypeDef(TypedDict):
    Arn: str
    VersionId: str

class FilterTypeDef(TypedDict):
    FieldName: NotRequired[FilterFieldType]
    Operator: NotRequired[OperatorType]
    Value: NotRequired[str]

class GetApprovalTeamRequestTypeDef(TypedDict):
    Arn: str

class GetApprovalTeamResponseApproverTypeDef(TypedDict):
    ApproverId: NotRequired[str]
    ResponseTime: NotRequired[datetime]
    PrimaryIdentityId: NotRequired[str]
    PrimaryIdentitySourceArn: NotRequired[str]
    PrimaryIdentityStatus: NotRequired[IdentityStatusType]

class GetIdentitySourceRequestTypeDef(TypedDict):
    IdentitySourceArn: str

class GetPolicyVersionRequestTypeDef(TypedDict):
    PolicyVersionArn: str

class PolicyVersionTypeDef(TypedDict):
    Arn: str
    PolicyArn: str
    VersionId: int
    PolicyType: PolicyTypeType
    IsDefault: bool
    Name: str
    Status: PolicyStatusType
    CreationTime: datetime
    LastUpdatedTime: datetime
    Document: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    PolicyName: str
    PolicyType: PolicyTypeType

class GetSessionRequestTypeDef(TypedDict):
    SessionArn: str

class GetSessionResponseApproverResponseTypeDef(TypedDict):
    ApproverId: NotRequired[str]
    IdentitySourceArn: NotRequired[str]
    IdentityId: NotRequired[str]
    Response: NotRequired[SessionResponseType]
    ResponseTime: NotRequired[datetime]

class IamIdentityCenterForGetTypeDef(TypedDict):
    InstanceArn: NotRequired[str]
    ApprovalPortalUrl: NotRequired[str]
    Region: NotRequired[str]

class IamIdentityCenterForListTypeDef(TypedDict):
    InstanceArn: NotRequired[str]
    ApprovalPortalUrl: NotRequired[str]
    Region: NotRequired[str]

class IamIdentityCenterTypeDef(TypedDict):
    InstanceArn: str
    Region: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApprovalTeamsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListIdentitySourcesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPoliciesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PolicyTypeDef(TypedDict):
    Arn: str
    DefaultVersion: int
    PolicyType: PolicyTypeType
    Name: str

class ListPolicyVersionsRequestTypeDef(TypedDict):
    PolicyArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PolicyVersionSummaryTypeDef(TypedDict):
    Arn: str
    PolicyArn: str
    VersionId: int
    PolicyType: PolicyTypeType
    IsDefault: bool
    Name: str
    Status: PolicyStatusType
    CreationTime: datetime
    LastUpdatedTime: datetime

class ListResourcePoliciesRequestTypeDef(TypedDict):
    ResourceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListResourcePoliciesResponseResourcePolicyTypeDef(TypedDict):
    PolicyArn: NotRequired[str]
    PolicyType: NotRequired[PolicyTypeType]
    PolicyName: NotRequired[str]

class ListSessionsResponseSessionTypeDef(TypedDict):
    SessionArn: NotRequired[str]
    ApprovalTeamName: NotRequired[str]
    ApprovalTeamArn: NotRequired[str]
    InitiationTime: NotRequired[datetime]
    ExpirationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    Description: NotRequired[str]
    ActionName: NotRequired[str]
    ProtectedResourceArn: NotRequired[str]
    RequesterServicePrincipal: NotRequired[str]
    RequesterPrincipalArn: NotRequired[str]
    RequesterRegion: NotRequired[str]
    RequesterAccountId: NotRequired[str]
    Status: NotRequired[SessionStatusType]
    StatusCode: NotRequired[SessionStatusCodeType]
    StatusMessage: NotRequired[str]
    ActionCompletionStrategy: NotRequired[Literal["AUTO_COMPLETION_UPON_APPROVAL"]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class StartActiveApprovalTeamDeletionRequestTypeDef(TypedDict):
    Arn: str
    PendingWindowDays: NotRequired[int]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ApprovalStrategyResponseTypeDef(TypedDict):
    MofN: NotRequired[MofNApprovalStrategyTypeDef]

class ApprovalStrategyTypeDef(TypedDict):
    MofN: NotRequired[MofNApprovalStrategyTypeDef]

class CreateApprovalTeamResponseTypeDef(TypedDict):
    CreationTime: datetime
    Arn: str
    Name: str
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdentitySourceResponseTypeDef(TypedDict):
    IdentitySourceType: Literal["IAM_IDENTITY_CENTER"]
    IdentitySourceArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    ResourceArn: str
    PolicyType: PolicyTypeType
    PolicyVersionArn: str
    PolicyName: str
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartActiveApprovalTeamDeletionResponseTypeDef(TypedDict):
    DeletionCompletionTime: datetime
    DeletionStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApprovalTeamResponseTypeDef(TypedDict):
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsRequestTypeDef(TypedDict):
    ApprovalTeamArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class GetPolicyVersionResponseTypeDef(TypedDict):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IdentitySourceParametersForGetTypeDef(TypedDict):
    IamIdentityCenter: NotRequired[IamIdentityCenterForGetTypeDef]

class IdentitySourceParametersForListTypeDef(TypedDict):
    IamIdentityCenter: NotRequired[IamIdentityCenterForListTypeDef]

class IdentitySourceParametersTypeDef(TypedDict):
    IamIdentityCenter: NotRequired[IamIdentityCenterTypeDef]

class ListApprovalTeamsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdentitySourcesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyVersionsRequestPaginateTypeDef(TypedDict):
    PolicyArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourcePoliciesRequestPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsRequestPaginateTypeDef(TypedDict):
    ApprovalTeamArn: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoliciesResponseTypeDef(TypedDict):
    Policies: List[PolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPolicyVersionsResponseTypeDef(TypedDict):
    PolicyVersions: List[PolicyVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourcePoliciesResponseTypeDef(TypedDict):
    ResourcePolicies: List[ListResourcePoliciesResponseResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSessionsResponseTypeDef(TypedDict):
    Sessions: List[ListSessionsResponseSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetSessionResponseTypeDef(TypedDict):
    SessionArn: str
    ApprovalTeamArn: str
    ApprovalTeamName: str
    ProtectedResourceArn: str
    ApprovalStrategy: ApprovalStrategyResponseTypeDef
    NumberOfApprovers: int
    InitiationTime: datetime
    ExpirationTime: datetime
    CompletionTime: datetime
    Description: str
    Metadata: Dict[str, str]
    Status: SessionStatusType
    StatusCode: SessionStatusCodeType
    StatusMessage: str
    ExecutionStatus: SessionExecutionStatusType
    ActionName: str
    RequesterServicePrincipal: str
    RequesterPrincipalArn: str
    RequesterAccountId: str
    RequesterRegion: str
    RequesterComment: str
    ActionCompletionStrategy: Literal["AUTO_COMPLETION_UPON_APPROVAL"]
    ApproverResponses: List[GetSessionResponseApproverResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApprovalTeamsResponseApprovalTeamTypeDef(TypedDict):
    CreationTime: NotRequired[datetime]
    ApprovalStrategy: NotRequired[ApprovalStrategyResponseTypeDef]
    NumberOfApprovers: NotRequired[int]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[ApprovalTeamStatusType]
    StatusCode: NotRequired[ApprovalTeamStatusCodeType]
    StatusMessage: NotRequired[str]

class PendingUpdateTypeDef(TypedDict):
    VersionId: NotRequired[str]
    Description: NotRequired[str]
    ApprovalStrategy: NotRequired[ApprovalStrategyResponseTypeDef]
    NumberOfApprovers: NotRequired[int]
    Status: NotRequired[ApprovalTeamStatusType]
    StatusCode: NotRequired[ApprovalTeamStatusCodeType]
    StatusMessage: NotRequired[str]
    Approvers: NotRequired[List[GetApprovalTeamResponseApproverTypeDef]]
    UpdateInitiationTime: NotRequired[datetime]

class CreateApprovalTeamRequestTypeDef(TypedDict):
    ApprovalStrategy: ApprovalStrategyTypeDef
    Approvers: Sequence[ApprovalTeamRequestApproverTypeDef]
    Description: str
    Policies: Sequence[PolicyReferenceTypeDef]
    Name: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateApprovalTeamRequestTypeDef(TypedDict):
    Arn: str
    ApprovalStrategy: NotRequired[ApprovalStrategyTypeDef]
    Approvers: NotRequired[Sequence[ApprovalTeamRequestApproverTypeDef]]
    Description: NotRequired[str]

class GetIdentitySourceResponseTypeDef(TypedDict):
    IdentitySourceType: Literal["IAM_IDENTITY_CENTER"]
    IdentitySourceParameters: IdentitySourceParametersForGetTypeDef
    IdentitySourceArn: str
    CreationTime: datetime
    Status: IdentitySourceStatusType
    StatusCode: IdentitySourceStatusCodeType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class IdentitySourceForListTypeDef(TypedDict):
    IdentitySourceType: NotRequired[Literal["IAM_IDENTITY_CENTER"]]
    IdentitySourceParameters: NotRequired[IdentitySourceParametersForListTypeDef]
    IdentitySourceArn: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Status: NotRequired[IdentitySourceStatusType]
    StatusCode: NotRequired[IdentitySourceStatusCodeType]
    StatusMessage: NotRequired[str]

class CreateIdentitySourceRequestTypeDef(TypedDict):
    IdentitySourceParameters: IdentitySourceParametersTypeDef
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ListApprovalTeamsResponseTypeDef(TypedDict):
    ApprovalTeams: List[ListApprovalTeamsResponseApprovalTeamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetApprovalTeamResponseTypeDef(TypedDict):
    CreationTime: datetime
    ApprovalStrategy: ApprovalStrategyResponseTypeDef
    NumberOfApprovers: int
    Approvers: List[GetApprovalTeamResponseApproverTypeDef]
    Arn: str
    Description: str
    Name: str
    Status: ApprovalTeamStatusType
    StatusCode: ApprovalTeamStatusCodeType
    StatusMessage: str
    UpdateSessionArn: str
    VersionId: str
    Policies: List[PolicyReferenceTypeDef]
    LastUpdateTime: datetime
    PendingUpdate: PendingUpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentitySourcesResponseTypeDef(TypedDict):
    IdentitySources: List[IdentitySourceForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
