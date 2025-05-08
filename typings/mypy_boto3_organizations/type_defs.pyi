"""
Type annotations for organizations service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_organizations.type_defs import AcceptHandshakeRequestTypeDef

    data: AcceptHandshakeRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import (
    AccountJoinedMethodType,
    AccountStatusType,
    ActionTypeType,
    ChildTypeType,
    CreateAccountFailureReasonType,
    CreateAccountStateType,
    EffectivePolicyTypeType,
    HandshakePartyTypeType,
    HandshakeResourceTypeType,
    HandshakeStateType,
    IAMUserAccessToBillingType,
    OrganizationFeatureSetType,
    ParentTypeType,
    PolicyTypeStatusType,
    PolicyTypeType,
    TargetTypeType,
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
    "AcceptHandshakeRequestTypeDef",
    "AcceptHandshakeResponseTypeDef",
    "AccountTypeDef",
    "AttachPolicyRequestTypeDef",
    "CancelHandshakeRequestTypeDef",
    "CancelHandshakeResponseTypeDef",
    "ChildTypeDef",
    "CloseAccountRequestTypeDef",
    "CreateAccountRequestTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAccountStatusTypeDef",
    "CreateGovCloudAccountRequestTypeDef",
    "CreateGovCloudAccountResponseTypeDef",
    "CreateOrganizationRequestTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateOrganizationalUnitRequestTypeDef",
    "CreateOrganizationalUnitResponseTypeDef",
    "CreatePolicyRequestTypeDef",
    "CreatePolicyResponseTypeDef",
    "DeclineHandshakeRequestTypeDef",
    "DeclineHandshakeResponseTypeDef",
    "DelegatedAdministratorTypeDef",
    "DelegatedServiceTypeDef",
    "DeleteOrganizationalUnitRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeregisterDelegatedAdministratorRequestTypeDef",
    "DescribeAccountRequestTypeDef",
    "DescribeAccountResponseTypeDef",
    "DescribeCreateAccountStatusRequestTypeDef",
    "DescribeCreateAccountStatusResponseTypeDef",
    "DescribeEffectivePolicyRequestTypeDef",
    "DescribeEffectivePolicyResponseTypeDef",
    "DescribeHandshakeRequestTypeDef",
    "DescribeHandshakeResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeOrganizationalUnitRequestTypeDef",
    "DescribeOrganizationalUnitResponseTypeDef",
    "DescribePolicyRequestTypeDef",
    "DescribePolicyResponseTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DetachPolicyRequestTypeDef",
    "DisableAWSServiceAccessRequestTypeDef",
    "DisablePolicyTypeRequestTypeDef",
    "DisablePolicyTypeResponseTypeDef",
    "EffectivePolicyTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableAWSServiceAccessRequestTypeDef",
    "EnableAllFeaturesResponseTypeDef",
    "EnablePolicyTypeRequestTypeDef",
    "EnablePolicyTypeResponseTypeDef",
    "EnabledServicePrincipalTypeDef",
    "HandshakeFilterTypeDef",
    "HandshakePaginatorTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeResourcePaginatorTypeDef",
    "HandshakeResourceTypeDef",
    "HandshakeTypeDef",
    "InviteAccountToOrganizationRequestTypeDef",
    "InviteAccountToOrganizationResponseTypeDef",
    "ListAWSServiceAccessForOrganizationRequestPaginateTypeDef",
    "ListAWSServiceAccessForOrganizationRequestTypeDef",
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    "ListAccountsForParentRequestPaginateTypeDef",
    "ListAccountsForParentRequestTypeDef",
    "ListAccountsForParentResponseTypeDef",
    "ListAccountsRequestPaginateTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "ListChildrenRequestPaginateTypeDef",
    "ListChildrenRequestTypeDef",
    "ListChildrenResponseTypeDef",
    "ListCreateAccountStatusRequestPaginateTypeDef",
    "ListCreateAccountStatusRequestTypeDef",
    "ListCreateAccountStatusResponseTypeDef",
    "ListDelegatedAdministratorsRequestPaginateTypeDef",
    "ListDelegatedAdministratorsRequestTypeDef",
    "ListDelegatedAdministratorsResponseTypeDef",
    "ListDelegatedServicesForAccountRequestPaginateTypeDef",
    "ListDelegatedServicesForAccountRequestTypeDef",
    "ListDelegatedServicesForAccountResponseTypeDef",
    "ListHandshakesForAccountRequestPaginateTypeDef",
    "ListHandshakesForAccountRequestTypeDef",
    "ListHandshakesForAccountResponsePaginatorTypeDef",
    "ListHandshakesForAccountResponseTypeDef",
    "ListHandshakesForOrganizationRequestPaginateTypeDef",
    "ListHandshakesForOrganizationRequestTypeDef",
    "ListHandshakesForOrganizationResponsePaginatorTypeDef",
    "ListHandshakesForOrganizationResponseTypeDef",
    "ListOrganizationalUnitsForParentRequestPaginateTypeDef",
    "ListOrganizationalUnitsForParentRequestTypeDef",
    "ListOrganizationalUnitsForParentResponseTypeDef",
    "ListParentsRequestPaginateTypeDef",
    "ListParentsRequestTypeDef",
    "ListParentsResponseTypeDef",
    "ListPoliciesForTargetRequestPaginateTypeDef",
    "ListPoliciesForTargetRequestTypeDef",
    "ListPoliciesForTargetResponseTypeDef",
    "ListPoliciesRequestPaginateTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListRootsRequestPaginateTypeDef",
    "ListRootsRequestTypeDef",
    "ListRootsResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsForPolicyRequestPaginateTypeDef",
    "ListTargetsForPolicyRequestTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "MoveAccountRequestTypeDef",
    "OrganizationTypeDef",
    "OrganizationalUnitTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTargetSummaryTypeDef",
    "PolicyTypeDef",
    "PolicyTypeSummaryTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegisterDelegatedAdministratorRequestTypeDef",
    "RemoveAccountFromOrganizationRequestTypeDef",
    "ResourcePolicySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "RootTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateOrganizationalUnitRequestTypeDef",
    "UpdateOrganizationalUnitResponseTypeDef",
    "UpdatePolicyRequestTypeDef",
    "UpdatePolicyResponseTypeDef",
)

class AcceptHandshakeRequestTypeDef(TypedDict):
    HandshakeId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AccountTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Email: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[AccountStatusType]
    JoinedMethod: NotRequired[AccountJoinedMethodType]
    JoinedTimestamp: NotRequired[datetime]

class AttachPolicyRequestTypeDef(TypedDict):
    PolicyId: str
    TargetId: str

class CancelHandshakeRequestTypeDef(TypedDict):
    HandshakeId: str

ChildTypeDef = TypedDict(
    "ChildTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ChildTypeType],
    },
)

class CloseAccountRequestTypeDef(TypedDict):
    AccountId: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateAccountStatusTypeDef(TypedDict):
    Id: NotRequired[str]
    AccountName: NotRequired[str]
    State: NotRequired[CreateAccountStateType]
    RequestedTimestamp: NotRequired[datetime]
    CompletedTimestamp: NotRequired[datetime]
    AccountId: NotRequired[str]
    GovCloudAccountId: NotRequired[str]
    FailureReason: NotRequired[CreateAccountFailureReasonType]

class CreateOrganizationRequestTypeDef(TypedDict):
    FeatureSet: NotRequired[OrganizationFeatureSetType]

class OrganizationalUnitTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]

class DeclineHandshakeRequestTypeDef(TypedDict):
    HandshakeId: str

class DelegatedAdministratorTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Email: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[AccountStatusType]
    JoinedMethod: NotRequired[AccountJoinedMethodType]
    JoinedTimestamp: NotRequired[datetime]
    DelegationEnabledDate: NotRequired[datetime]

class DelegatedServiceTypeDef(TypedDict):
    ServicePrincipal: NotRequired[str]
    DelegationEnabledDate: NotRequired[datetime]

class DeleteOrganizationalUnitRequestTypeDef(TypedDict):
    OrganizationalUnitId: str

class DeletePolicyRequestTypeDef(TypedDict):
    PolicyId: str

class DeregisterDelegatedAdministratorRequestTypeDef(TypedDict):
    AccountId: str
    ServicePrincipal: str

class DescribeAccountRequestTypeDef(TypedDict):
    AccountId: str

class DescribeCreateAccountStatusRequestTypeDef(TypedDict):
    CreateAccountRequestId: str

class DescribeEffectivePolicyRequestTypeDef(TypedDict):
    PolicyType: EffectivePolicyTypeType
    TargetId: NotRequired[str]

class EffectivePolicyTypeDef(TypedDict):
    PolicyContent: NotRequired[str]
    LastUpdatedTimestamp: NotRequired[datetime]
    TargetId: NotRequired[str]
    PolicyType: NotRequired[EffectivePolicyTypeType]

class DescribeHandshakeRequestTypeDef(TypedDict):
    HandshakeId: str

class DescribeOrganizationalUnitRequestTypeDef(TypedDict):
    OrganizationalUnitId: str

class DescribePolicyRequestTypeDef(TypedDict):
    PolicyId: str

class DetachPolicyRequestTypeDef(TypedDict):
    PolicyId: str
    TargetId: str

class DisableAWSServiceAccessRequestTypeDef(TypedDict):
    ServicePrincipal: str

class DisablePolicyTypeRequestTypeDef(TypedDict):
    RootId: str
    PolicyType: PolicyTypeType

class EnableAWSServiceAccessRequestTypeDef(TypedDict):
    ServicePrincipal: str

class EnablePolicyTypeRequestTypeDef(TypedDict):
    RootId: str
    PolicyType: PolicyTypeType

class EnabledServicePrincipalTypeDef(TypedDict):
    ServicePrincipal: NotRequired[str]
    DateEnabled: NotRequired[datetime]

class HandshakeFilterTypeDef(TypedDict):
    ActionType: NotRequired[ActionTypeType]
    ParentHandshakeId: NotRequired[str]

HandshakePartyTypeDef = TypedDict(
    "HandshakePartyTypeDef",
    {
        "Id": str,
        "Type": HandshakePartyTypeType,
    },
)
HandshakeResourcePaginatorTypeDef = TypedDict(
    "HandshakeResourcePaginatorTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[HandshakeResourceTypeType],
        "Resources": NotRequired[List[Dict[str, Any]]],
    },
)
HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[HandshakeResourceTypeType],
        "Resources": NotRequired[List[Dict[str, Any]]],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAWSServiceAccessForOrganizationRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAccountsForParentRequestTypeDef(TypedDict):
    ParentId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAccountsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListChildrenRequestTypeDef(TypedDict):
    ParentId: str
    ChildType: ChildTypeType
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCreateAccountStatusRequestTypeDef(TypedDict):
    States: NotRequired[Sequence[CreateAccountStateType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDelegatedAdministratorsRequestTypeDef(TypedDict):
    ServicePrincipal: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDelegatedServicesForAccountRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListOrganizationalUnitsForParentRequestTypeDef(TypedDict):
    ParentId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListParentsRequestTypeDef(TypedDict):
    ChildId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ParentTypeType],
    },
)

class ListPoliciesForTargetRequestTypeDef(TypedDict):
    TargetId: str
    Filter: PolicyTypeType
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[PolicyTypeType],
        "AwsManaged": NotRequired[bool],
    },
)

class ListPoliciesRequestTypeDef(TypedDict):
    Filter: PolicyTypeType
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRootsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceId: str
    NextToken: NotRequired[str]

class ListTargetsForPolicyRequestTypeDef(TypedDict):
    PolicyId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

PolicyTargetSummaryTypeDef = TypedDict(
    "PolicyTargetSummaryTypeDef",
    {
        "TargetId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[TargetTypeType],
    },
)

class MoveAccountRequestTypeDef(TypedDict):
    AccountId: str
    SourceParentId: str
    DestinationParentId: str

PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef",
    {
        "Type": NotRequired[PolicyTypeType],
        "Status": NotRequired[PolicyTypeStatusType],
    },
)

class RegisterDelegatedAdministratorRequestTypeDef(TypedDict):
    AccountId: str
    ServicePrincipal: str

class RemoveAccountFromOrganizationRequestTypeDef(TypedDict):
    AccountId: str

class ResourcePolicySummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceId: str
    TagKeys: Sequence[str]

class UpdateOrganizationalUnitRequestTypeDef(TypedDict):
    OrganizationalUnitId: str
    Name: NotRequired[str]

class UpdatePolicyRequestTypeDef(TypedDict):
    PolicyId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    Content: NotRequired[str]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountResponseTypeDef(TypedDict):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsForParentResponseTypeDef(TypedDict):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAccountsResponseTypeDef(TypedDict):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListChildrenResponseTypeDef(TypedDict):
    Children: List[ChildTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateAccountRequestTypeDef(TypedDict):
    Email: str
    AccountName: str
    RoleName: NotRequired[str]
    IamUserAccessToBilling: NotRequired[IAMUserAccessToBillingType]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateGovCloudAccountRequestTypeDef(TypedDict):
    Email: str
    AccountName: str
    RoleName: NotRequired[str]
    IamUserAccessToBilling: NotRequired[IAMUserAccessToBillingType]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateOrganizationalUnitRequestTypeDef(TypedDict):
    ParentId: str
    Name: str
    Tags: NotRequired[Sequence[TagTypeDef]]

CreatePolicyRequestTypeDef = TypedDict(
    "CreatePolicyRequestTypeDef",
    {
        "Content": str,
        "Description": str,
        "Name": str,
        "Type": PolicyTypeType,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    Content: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateAccountResponseTypeDef(TypedDict):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGovCloudAccountResponseTypeDef(TypedDict):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCreateAccountStatusResponseTypeDef(TypedDict):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCreateAccountStatusResponseTypeDef(TypedDict):
    CreateAccountStatuses: List[CreateAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateOrganizationalUnitResponseTypeDef(TypedDict):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationalUnitResponseTypeDef(TypedDict):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationalUnitsForParentResponseTypeDef(TypedDict):
    OrganizationalUnits: List[OrganizationalUnitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateOrganizationalUnitResponseTypeDef(TypedDict):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDelegatedAdministratorsResponseTypeDef(TypedDict):
    DelegatedAdministrators: List[DelegatedAdministratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDelegatedServicesForAccountResponseTypeDef(TypedDict):
    DelegatedServices: List[DelegatedServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEffectivePolicyResponseTypeDef(TypedDict):
    EffectivePolicy: EffectivePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSServiceAccessForOrganizationResponseTypeDef(TypedDict):
    EnabledServicePrincipals: List[EnabledServicePrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListHandshakesForAccountRequestTypeDef(TypedDict):
    Filter: NotRequired[HandshakeFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListHandshakesForOrganizationRequestTypeDef(TypedDict):
    Filter: NotRequired[HandshakeFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class InviteAccountToOrganizationRequestTypeDef(TypedDict):
    Target: HandshakePartyTypeDef
    Notes: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class HandshakePaginatorTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Parties: NotRequired[List[HandshakePartyTypeDef]]
    State: NotRequired[HandshakeStateType]
    RequestedTimestamp: NotRequired[datetime]
    ExpirationTimestamp: NotRequired[datetime]
    Action: NotRequired[ActionTypeType]
    Resources: NotRequired[List[HandshakeResourcePaginatorTypeDef]]

class HandshakeTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Parties: NotRequired[List[HandshakePartyTypeDef]]
    State: NotRequired[HandshakeStateType]
    RequestedTimestamp: NotRequired[datetime]
    ExpirationTimestamp: NotRequired[datetime]
    Action: NotRequired[ActionTypeType]
    Resources: NotRequired[List[HandshakeResourceTypeDef]]

class ListAWSServiceAccessForOrganizationRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccountsForParentRequestPaginateTypeDef(TypedDict):
    ParentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListChildrenRequestPaginateTypeDef(TypedDict):
    ParentId: str
    ChildType: ChildTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCreateAccountStatusRequestPaginateTypeDef(TypedDict):
    States: NotRequired[Sequence[CreateAccountStateType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDelegatedAdministratorsRequestPaginateTypeDef(TypedDict):
    ServicePrincipal: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDelegatedServicesForAccountRequestPaginateTypeDef(TypedDict):
    AccountId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHandshakesForAccountRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[HandshakeFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHandshakesForOrganizationRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[HandshakeFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationalUnitsForParentRequestPaginateTypeDef(TypedDict):
    ParentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListParentsRequestPaginateTypeDef(TypedDict):
    ChildId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoliciesForTargetRequestPaginateTypeDef(TypedDict):
    TargetId: str
    Filter: PolicyTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoliciesRequestPaginateTypeDef(TypedDict):
    Filter: PolicyTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRootsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTargetsForPolicyRequestPaginateTypeDef(TypedDict):
    PolicyId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListParentsResponseTypeDef(TypedDict):
    Parents: List[ParentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPoliciesForTargetResponseTypeDef(TypedDict):
    Policies: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPoliciesResponseTypeDef(TypedDict):
    Policies: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PolicyTypeDef(TypedDict):
    PolicySummary: NotRequired[PolicySummaryTypeDef]
    Content: NotRequired[str]

class ListTargetsForPolicyResponseTypeDef(TypedDict):
    Targets: List[PolicyTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OrganizationTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    FeatureSet: NotRequired[OrganizationFeatureSetType]
    MasterAccountArn: NotRequired[str]
    MasterAccountId: NotRequired[str]
    MasterAccountEmail: NotRequired[str]
    AvailablePolicyTypes: NotRequired[List[PolicyTypeSummaryTypeDef]]

class RootTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    PolicyTypes: NotRequired[List[PolicyTypeSummaryTypeDef]]

class ResourcePolicyTypeDef(TypedDict):
    ResourcePolicySummary: NotRequired[ResourcePolicySummaryTypeDef]
    Content: NotRequired[str]

class ListHandshakesForAccountResponsePaginatorTypeDef(TypedDict):
    Handshakes: List[HandshakePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListHandshakesForOrganizationResponsePaginatorTypeDef(TypedDict):
    Handshakes: List[HandshakePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AcceptHandshakeResponseTypeDef(TypedDict):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelHandshakeResponseTypeDef(TypedDict):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineHandshakeResponseTypeDef(TypedDict):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHandshakeResponseTypeDef(TypedDict):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAllFeaturesResponseTypeDef(TypedDict):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InviteAccountToOrganizationResponseTypeDef(TypedDict):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHandshakesForAccountResponseTypeDef(TypedDict):
    Handshakes: List[HandshakeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListHandshakesForOrganizationResponseTypeDef(TypedDict):
    Handshakes: List[HandshakeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreatePolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOrganizationResponseTypeDef(TypedDict):
    Organization: OrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationResponseTypeDef(TypedDict):
    Organization: OrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisablePolicyTypeResponseTypeDef(TypedDict):
    Root: RootTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnablePolicyTypeResponseTypeDef(TypedDict):
    Root: RootTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRootsResponseTypeDef(TypedDict):
    Roots: List[RootTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeResourcePolicyResponseTypeDef(TypedDict):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
