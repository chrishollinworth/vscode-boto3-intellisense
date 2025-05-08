"""
Type annotations for opensearchserverless service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_opensearchserverless.type_defs import AccessPolicyDetailTypeDef

    data: AccessPolicyDetailTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from .literals import (
    CollectionStatusType,
    CollectionTypeType,
    IamIdentityCenterGroupAttributeType,
    IamIdentityCenterUserAttributeType,
    SecurityConfigTypeType,
    SecurityPolicyTypeType,
    StandbyReplicasType,
    VpcEndpointStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessPolicyDetailTypeDef",
    "AccessPolicyStatsTypeDef",
    "AccessPolicySummaryTypeDef",
    "AccountSettingsDetailTypeDef",
    "BatchGetCollectionRequestTypeDef",
    "BatchGetCollectionResponseTypeDef",
    "BatchGetEffectiveLifecyclePolicyRequestTypeDef",
    "BatchGetEffectiveLifecyclePolicyResponseTypeDef",
    "BatchGetLifecyclePolicyRequestTypeDef",
    "BatchGetLifecyclePolicyResponseTypeDef",
    "BatchGetVpcEndpointRequestTypeDef",
    "BatchGetVpcEndpointResponseTypeDef",
    "CapacityLimitsTypeDef",
    "CollectionDetailTypeDef",
    "CollectionErrorDetailTypeDef",
    "CollectionFiltersTypeDef",
    "CollectionSummaryTypeDef",
    "CreateAccessPolicyRequestTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateCollectionDetailTypeDef",
    "CreateCollectionRequestTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateIamIdentityCenterConfigOptionsTypeDef",
    "CreateLifecyclePolicyRequestTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateSecurityConfigRequestTypeDef",
    "CreateSecurityConfigResponseTypeDef",
    "CreateSecurityPolicyRequestTypeDef",
    "CreateSecurityPolicyResponseTypeDef",
    "CreateVpcEndpointDetailTypeDef",
    "CreateVpcEndpointRequestTypeDef",
    "CreateVpcEndpointResponseTypeDef",
    "DeleteAccessPolicyRequestTypeDef",
    "DeleteCollectionDetailTypeDef",
    "DeleteCollectionRequestTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteLifecyclePolicyRequestTypeDef",
    "DeleteSecurityConfigRequestTypeDef",
    "DeleteSecurityPolicyRequestTypeDef",
    "DeleteVpcEndpointDetailTypeDef",
    "DeleteVpcEndpointRequestTypeDef",
    "DeleteVpcEndpointResponseTypeDef",
    "EffectiveLifecyclePolicyDetailTypeDef",
    "EffectiveLifecyclePolicyErrorDetailTypeDef",
    "GetAccessPolicyRequestTypeDef",
    "GetAccessPolicyResponseTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetPoliciesStatsResponseTypeDef",
    "GetSecurityConfigRequestTypeDef",
    "GetSecurityConfigResponseTypeDef",
    "GetSecurityPolicyRequestTypeDef",
    "GetSecurityPolicyResponseTypeDef",
    "IamIdentityCenterConfigOptionsTypeDef",
    "LifecyclePolicyDetailTypeDef",
    "LifecyclePolicyErrorDetailTypeDef",
    "LifecyclePolicyIdentifierTypeDef",
    "LifecyclePolicyResourceIdentifierTypeDef",
    "LifecyclePolicyStatsTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "ListAccessPoliciesRequestTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListCollectionsRequestTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListLifecyclePoliciesRequestTypeDef",
    "ListLifecyclePoliciesResponseTypeDef",
    "ListSecurityConfigsRequestTypeDef",
    "ListSecurityConfigsResponseTypeDef",
    "ListSecurityPoliciesRequestTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVpcEndpointsRequestTypeDef",
    "ListVpcEndpointsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SamlConfigOptionsTypeDef",
    "SecurityConfigDetailTypeDef",
    "SecurityConfigStatsTypeDef",
    "SecurityConfigSummaryTypeDef",
    "SecurityPolicyDetailTypeDef",
    "SecurityPolicyStatsTypeDef",
    "SecurityPolicySummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessPolicyRequestTypeDef",
    "UpdateAccessPolicyResponseTypeDef",
    "UpdateAccountSettingsRequestTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateCollectionDetailTypeDef",
    "UpdateCollectionRequestTypeDef",
    "UpdateCollectionResponseTypeDef",
    "UpdateIamIdentityCenterConfigOptionsTypeDef",
    "UpdateLifecyclePolicyRequestTypeDef",
    "UpdateLifecyclePolicyResponseTypeDef",
    "UpdateSecurityConfigRequestTypeDef",
    "UpdateSecurityConfigResponseTypeDef",
    "UpdateSecurityPolicyRequestTypeDef",
    "UpdateSecurityPolicyResponseTypeDef",
    "UpdateVpcEndpointDetailTypeDef",
    "UpdateVpcEndpointRequestTypeDef",
    "UpdateVpcEndpointResponseTypeDef",
    "VpcEndpointDetailTypeDef",
    "VpcEndpointErrorDetailTypeDef",
    "VpcEndpointFiltersTypeDef",
    "VpcEndpointSummaryTypeDef",
)

AccessPolicyDetailTypeDef = TypedDict(
    "AccessPolicyDetailTypeDef",
    {
        "type": NotRequired[Literal["data"]],
        "name": NotRequired[str],
        "policyVersion": NotRequired[str],
        "description": NotRequired[str],
        "policy": NotRequired[Dict[str, Any]],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)

class AccessPolicyStatsTypeDef(TypedDict):
    DataPolicyCount: NotRequired[int]

AccessPolicySummaryTypeDef = TypedDict(
    "AccessPolicySummaryTypeDef",
    {
        "type": NotRequired[Literal["data"]],
        "name": NotRequired[str],
        "policyVersion": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)

class CapacityLimitsTypeDef(TypedDict):
    maxIndexingCapacityInOCU: NotRequired[int]
    maxSearchCapacityInOCU: NotRequired[int]

class BatchGetCollectionRequestTypeDef(TypedDict):
    ids: NotRequired[Sequence[str]]
    names: NotRequired[Sequence[str]]

CollectionDetailTypeDef = TypedDict(
    "CollectionDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CollectionStatusType],
        "type": NotRequired[CollectionTypeType],
        "description": NotRequired[str],
        "arn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "standbyReplicas": NotRequired[StandbyReplicasType],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
        "collectionEndpoint": NotRequired[str],
        "dashboardEndpoint": NotRequired[str],
        "failureCode": NotRequired[str],
        "failureMessage": NotRequired[str],
    },
)
CollectionErrorDetailTypeDef = TypedDict(
    "CollectionErrorDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

LifecyclePolicyResourceIdentifierTypeDef = TypedDict(
    "LifecyclePolicyResourceIdentifierTypeDef",
    {
        "type": Literal["retention"],
        "resource": str,
    },
)
EffectiveLifecyclePolicyDetailTypeDef = TypedDict(
    "EffectiveLifecyclePolicyDetailTypeDef",
    {
        "type": NotRequired[Literal["retention"]],
        "resource": NotRequired[str],
        "policyName": NotRequired[str],
        "resourceType": NotRequired[Literal["index"]],
        "retentionPeriod": NotRequired[str],
        "noMinRetentionPeriod": NotRequired[bool],
    },
)
EffectiveLifecyclePolicyErrorDetailTypeDef = TypedDict(
    "EffectiveLifecyclePolicyErrorDetailTypeDef",
    {
        "type": NotRequired[Literal["retention"]],
        "resource": NotRequired[str],
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[str],
    },
)
LifecyclePolicyIdentifierTypeDef = TypedDict(
    "LifecyclePolicyIdentifierTypeDef",
    {
        "type": Literal["retention"],
        "name": str,
    },
)
LifecyclePolicyDetailTypeDef = TypedDict(
    "LifecyclePolicyDetailTypeDef",
    {
        "type": NotRequired[Literal["retention"]],
        "name": NotRequired[str],
        "policyVersion": NotRequired[str],
        "description": NotRequired[str],
        "policy": NotRequired[Dict[str, Any]],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)
LifecyclePolicyErrorDetailTypeDef = TypedDict(
    "LifecyclePolicyErrorDetailTypeDef",
    {
        "type": NotRequired[Literal["retention"]],
        "name": NotRequired[str],
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[str],
    },
)

class BatchGetVpcEndpointRequestTypeDef(TypedDict):
    ids: Sequence[str]

VpcEndpointDetailTypeDef = TypedDict(
    "VpcEndpointDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "vpcId": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "status": NotRequired[VpcEndpointStatusType],
        "createdDate": NotRequired[int],
        "failureCode": NotRequired[str],
        "failureMessage": NotRequired[str],
    },
)
VpcEndpointErrorDetailTypeDef = TypedDict(
    "VpcEndpointErrorDetailTypeDef",
    {
        "id": NotRequired[str],
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[str],
    },
)

class CollectionFiltersTypeDef(TypedDict):
    name: NotRequired[str]
    status: NotRequired[CollectionStatusType]

CollectionSummaryTypeDef = TypedDict(
    "CollectionSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CollectionStatusType],
        "arn": NotRequired[str],
    },
)
CreateAccessPolicyRequestTypeDef = TypedDict(
    "CreateAccessPolicyRequestTypeDef",
    {
        "type": Literal["data"],
        "name": str,
        "policy": str,
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
CreateCollectionDetailTypeDef = TypedDict(
    "CreateCollectionDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CollectionStatusType],
        "type": NotRequired[CollectionTypeType],
        "description": NotRequired[str],
        "arn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "standbyReplicas": NotRequired[StandbyReplicasType],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)

class TagTypeDef(TypedDict):
    key: str
    value: str

class CreateIamIdentityCenterConfigOptionsTypeDef(TypedDict):
    instanceArn: str
    userAttribute: NotRequired[IamIdentityCenterUserAttributeType]
    groupAttribute: NotRequired[IamIdentityCenterGroupAttributeType]

CreateLifecyclePolicyRequestTypeDef = TypedDict(
    "CreateLifecyclePolicyRequestTypeDef",
    {
        "type": Literal["retention"],
        "name": str,
        "policy": str,
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

class SamlConfigOptionsTypeDef(TypedDict):
    metadata: str
    userAttribute: NotRequired[str]
    groupAttribute: NotRequired[str]
    openSearchServerlessEntityId: NotRequired[str]
    sessionTimeout: NotRequired[int]

CreateSecurityPolicyRequestTypeDef = TypedDict(
    "CreateSecurityPolicyRequestTypeDef",
    {
        "type": SecurityPolicyTypeType,
        "name": str,
        "policy": str,
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
SecurityPolicyDetailTypeDef = TypedDict(
    "SecurityPolicyDetailTypeDef",
    {
        "type": NotRequired[SecurityPolicyTypeType],
        "name": NotRequired[str],
        "policyVersion": NotRequired[str],
        "description": NotRequired[str],
        "policy": NotRequired[Dict[str, Any]],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)
CreateVpcEndpointDetailTypeDef = TypedDict(
    "CreateVpcEndpointDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[VpcEndpointStatusType],
    },
)

class CreateVpcEndpointRequestTypeDef(TypedDict):
    name: str
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]

DeleteAccessPolicyRequestTypeDef = TypedDict(
    "DeleteAccessPolicyRequestTypeDef",
    {
        "type": Literal["data"],
        "name": str,
        "clientToken": NotRequired[str],
    },
)
DeleteCollectionDetailTypeDef = TypedDict(
    "DeleteCollectionDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CollectionStatusType],
    },
)
DeleteCollectionRequestTypeDef = TypedDict(
    "DeleteCollectionRequestTypeDef",
    {
        "id": str,
        "clientToken": NotRequired[str],
    },
)
DeleteLifecyclePolicyRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestTypeDef",
    {
        "type": Literal["retention"],
        "name": str,
        "clientToken": NotRequired[str],
    },
)
DeleteSecurityConfigRequestTypeDef = TypedDict(
    "DeleteSecurityConfigRequestTypeDef",
    {
        "id": str,
        "clientToken": NotRequired[str],
    },
)
DeleteSecurityPolicyRequestTypeDef = TypedDict(
    "DeleteSecurityPolicyRequestTypeDef",
    {
        "type": SecurityPolicyTypeType,
        "name": str,
        "clientToken": NotRequired[str],
    },
)
DeleteVpcEndpointDetailTypeDef = TypedDict(
    "DeleteVpcEndpointDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[VpcEndpointStatusType],
    },
)
DeleteVpcEndpointRequestTypeDef = TypedDict(
    "DeleteVpcEndpointRequestTypeDef",
    {
        "id": str,
        "clientToken": NotRequired[str],
    },
)
GetAccessPolicyRequestTypeDef = TypedDict(
    "GetAccessPolicyRequestTypeDef",
    {
        "type": Literal["data"],
        "name": str,
    },
)

class LifecyclePolicyStatsTypeDef(TypedDict):
    RetentionPolicyCount: NotRequired[int]

class SecurityConfigStatsTypeDef(TypedDict):
    SamlConfigCount: NotRequired[int]

class SecurityPolicyStatsTypeDef(TypedDict):
    EncryptionPolicyCount: NotRequired[int]
    NetworkPolicyCount: NotRequired[int]

GetSecurityConfigRequestTypeDef = TypedDict(
    "GetSecurityConfigRequestTypeDef",
    {
        "id": str,
    },
)
GetSecurityPolicyRequestTypeDef = TypedDict(
    "GetSecurityPolicyRequestTypeDef",
    {
        "type": SecurityPolicyTypeType,
        "name": str,
    },
)

class IamIdentityCenterConfigOptionsTypeDef(TypedDict):
    instanceArn: NotRequired[str]
    applicationArn: NotRequired[str]
    applicationName: NotRequired[str]
    applicationDescription: NotRequired[str]
    userAttribute: NotRequired[IamIdentityCenterUserAttributeType]
    groupAttribute: NotRequired[IamIdentityCenterGroupAttributeType]

LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "type": NotRequired[Literal["retention"]],
        "name": NotRequired[str],
        "policyVersion": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)
ListAccessPoliciesRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestTypeDef",
    {
        "type": Literal["data"],
        "resource": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListLifecyclePoliciesRequestTypeDef = TypedDict(
    "ListLifecyclePoliciesRequestTypeDef",
    {
        "type": Literal["retention"],
        "resources": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSecurityConfigsRequestTypeDef = TypedDict(
    "ListSecurityConfigsRequestTypeDef",
    {
        "type": SecurityConfigTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SecurityConfigSummaryTypeDef = TypedDict(
    "SecurityConfigSummaryTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[SecurityConfigTypeType],
        "configVersion": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)
ListSecurityPoliciesRequestTypeDef = TypedDict(
    "ListSecurityPoliciesRequestTypeDef",
    {
        "type": SecurityPolicyTypeType,
        "resource": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SecurityPolicySummaryTypeDef = TypedDict(
    "SecurityPolicySummaryTypeDef",
    {
        "type": NotRequired[SecurityPolicyTypeType],
        "name": NotRequired[str],
        "policyVersion": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class VpcEndpointFiltersTypeDef(TypedDict):
    status: NotRequired[VpcEndpointStatusType]

VpcEndpointSummaryTypeDef = TypedDict(
    "VpcEndpointSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[VpcEndpointStatusType],
    },
)

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateAccessPolicyRequestTypeDef = TypedDict(
    "UpdateAccessPolicyRequestTypeDef",
    {
        "type": Literal["data"],
        "name": str,
        "policyVersion": str,
        "description": NotRequired[str],
        "policy": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateCollectionDetailTypeDef = TypedDict(
    "UpdateCollectionDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CollectionStatusType],
        "type": NotRequired[CollectionTypeType],
        "description": NotRequired[str],
        "arn": NotRequired[str],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)
UpdateCollectionRequestTypeDef = TypedDict(
    "UpdateCollectionRequestTypeDef",
    {
        "id": str,
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

class UpdateIamIdentityCenterConfigOptionsTypeDef(TypedDict):
    userAttribute: NotRequired[IamIdentityCenterUserAttributeType]
    groupAttribute: NotRequired[IamIdentityCenterGroupAttributeType]

UpdateLifecyclePolicyRequestTypeDef = TypedDict(
    "UpdateLifecyclePolicyRequestTypeDef",
    {
        "type": Literal["retention"],
        "name": str,
        "policyVersion": str,
        "description": NotRequired[str],
        "policy": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateSecurityPolicyRequestTypeDef = TypedDict(
    "UpdateSecurityPolicyRequestTypeDef",
    {
        "type": SecurityPolicyTypeType,
        "name": str,
        "policyVersion": str,
        "description": NotRequired[str],
        "policy": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateVpcEndpointDetailTypeDef = TypedDict(
    "UpdateVpcEndpointDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[VpcEndpointStatusType],
        "subnetIds": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "lastModifiedDate": NotRequired[int],
    },
)
UpdateVpcEndpointRequestTypeDef = TypedDict(
    "UpdateVpcEndpointRequestTypeDef",
    {
        "id": str,
        "addSubnetIds": NotRequired[Sequence[str]],
        "removeSubnetIds": NotRequired[Sequence[str]],
        "addSecurityGroupIds": NotRequired[Sequence[str]],
        "removeSecurityGroupIds": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)

class AccountSettingsDetailTypeDef(TypedDict):
    capacityLimits: NotRequired[CapacityLimitsTypeDef]

class UpdateAccountSettingsRequestTypeDef(TypedDict):
    capacityLimits: NotRequired[CapacityLimitsTypeDef]

class BatchGetCollectionResponseTypeDef(TypedDict):
    collectionDetails: List[CollectionDetailTypeDef]
    collectionErrorDetails: List[CollectionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPolicyResponseTypeDef(TypedDict):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPolicyResponseTypeDef(TypedDict):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(TypedDict):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateAccessPolicyResponseTypeDef(TypedDict):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetEffectiveLifecyclePolicyRequestTypeDef(TypedDict):
    resourceIdentifiers: Sequence[LifecyclePolicyResourceIdentifierTypeDef]

class BatchGetEffectiveLifecyclePolicyResponseTypeDef(TypedDict):
    effectiveLifecyclePolicyDetails: List[EffectiveLifecyclePolicyDetailTypeDef]
    effectiveLifecyclePolicyErrorDetails: List[EffectiveLifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetLifecyclePolicyRequestTypeDef(TypedDict):
    identifiers: Sequence[LifecyclePolicyIdentifierTypeDef]

class CreateLifecyclePolicyResponseTypeDef(TypedDict):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLifecyclePolicyResponseTypeDef(TypedDict):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetLifecyclePolicyResponseTypeDef(TypedDict):
    lifecyclePolicyDetails: List[LifecyclePolicyDetailTypeDef]
    lifecyclePolicyErrorDetails: List[LifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetVpcEndpointResponseTypeDef(TypedDict):
    vpcEndpointDetails: List[VpcEndpointDetailTypeDef]
    vpcEndpointErrorDetails: List[VpcEndpointErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollectionsRequestTypeDef(TypedDict):
    collectionFilters: NotRequired[CollectionFiltersTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollectionsResponseTypeDef(TypedDict):
    collectionSummaries: List[CollectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateCollectionResponseTypeDef(TypedDict):
    createCollectionDetail: CreateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateCollectionRequestTypeDef = TypedDict(
    "CreateCollectionRequestTypeDef",
    {
        "name": str,
        "type": NotRequired[CollectionTypeType],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "standbyReplicas": NotRequired[StandbyReplicasType],
        "clientToken": NotRequired[str],
    },
)

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

CreateSecurityConfigRequestTypeDef = TypedDict(
    "CreateSecurityConfigRequestTypeDef",
    {
        "type": SecurityConfigTypeType,
        "name": str,
        "description": NotRequired[str],
        "samlOptions": NotRequired[SamlConfigOptionsTypeDef],
        "iamIdentityCenterOptions": NotRequired[CreateIamIdentityCenterConfigOptionsTypeDef],
        "clientToken": NotRequired[str],
    },
)

class CreateSecurityPolicyResponseTypeDef(TypedDict):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityPolicyResponseTypeDef(TypedDict):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityPolicyResponseTypeDef(TypedDict):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcEndpointResponseTypeDef(TypedDict):
    createVpcEndpointDetail: CreateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCollectionResponseTypeDef(TypedDict):
    deleteCollectionDetail: DeleteCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointResponseTypeDef(TypedDict):
    deleteVpcEndpointDetail: DeleteVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPoliciesStatsResponseTypeDef(TypedDict):
    AccessPolicyStats: AccessPolicyStatsTypeDef
    SecurityPolicyStats: SecurityPolicyStatsTypeDef
    SecurityConfigStats: SecurityConfigStatsTypeDef
    LifecyclePolicyStats: LifecyclePolicyStatsTypeDef
    TotalPolicyCount: int
    ResponseMetadata: ResponseMetadataTypeDef

SecurityConfigDetailTypeDef = TypedDict(
    "SecurityConfigDetailTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[SecurityConfigTypeType],
        "configVersion": NotRequired[str],
        "description": NotRequired[str],
        "samlOptions": NotRequired[SamlConfigOptionsTypeDef],
        "iamIdentityCenterOptions": NotRequired[IamIdentityCenterConfigOptionsTypeDef],
        "createdDate": NotRequired[int],
        "lastModifiedDate": NotRequired[int],
    },
)

class ListLifecyclePoliciesResponseTypeDef(TypedDict):
    lifecyclePolicySummaries: List[LifecyclePolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSecurityConfigsResponseTypeDef(TypedDict):
    securityConfigSummaries: List[SecurityConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSecurityPoliciesResponseTypeDef(TypedDict):
    securityPolicySummaries: List[SecurityPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVpcEndpointsRequestTypeDef(TypedDict):
    vpcEndpointFilters: NotRequired[VpcEndpointFiltersTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListVpcEndpointsResponseTypeDef(TypedDict):
    vpcEndpointSummaries: List[VpcEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateCollectionResponseTypeDef(TypedDict):
    updateCollectionDetail: UpdateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

UpdateSecurityConfigRequestTypeDef = TypedDict(
    "UpdateSecurityConfigRequestTypeDef",
    {
        "id": str,
        "configVersion": str,
        "description": NotRequired[str],
        "samlOptions": NotRequired[SamlConfigOptionsTypeDef],
        "iamIdentityCenterOptionsUpdates": NotRequired[UpdateIamIdentityCenterConfigOptionsTypeDef],
        "clientToken": NotRequired[str],
    },
)

class UpdateVpcEndpointResponseTypeDef(TypedDict):
    UpdateVpcEndpointDetail: UpdateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(TypedDict):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(TypedDict):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigResponseTypeDef(TypedDict):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityConfigResponseTypeDef(TypedDict):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityConfigResponseTypeDef(TypedDict):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
