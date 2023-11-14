"""
Type annotations for opensearchserverless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opensearchserverless.type_defs import AccessPolicyDetailTypeDef

    data: AccessPolicyDetailTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    CollectionStatusType,
    CollectionTypeType,
    SecurityPolicyTypeType,
    VpcEndpointStatusType,
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
    "AccessPolicyDetailTypeDef",
    "AccessPolicyStatsTypeDef",
    "AccessPolicySummaryTypeDef",
    "AccountSettingsDetailTypeDef",
    "BatchGetCollectionRequestRequestTypeDef",
    "BatchGetCollectionResponseTypeDef",
    "BatchGetEffectiveLifecyclePolicyRequestRequestTypeDef",
    "BatchGetEffectiveLifecyclePolicyResponseTypeDef",
    "BatchGetLifecyclePolicyRequestRequestTypeDef",
    "BatchGetLifecyclePolicyResponseTypeDef",
    "BatchGetVpcEndpointRequestRequestTypeDef",
    "BatchGetVpcEndpointResponseTypeDef",
    "CapacityLimitsTypeDef",
    "CollectionDetailTypeDef",
    "CollectionErrorDetailTypeDef",
    "CollectionFiltersTypeDef",
    "CollectionSummaryTypeDef",
    "CreateAccessPolicyRequestRequestTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateCollectionDetailTypeDef",
    "CreateCollectionRequestRequestTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateLifecyclePolicyRequestRequestTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateSecurityConfigRequestRequestTypeDef",
    "CreateSecurityConfigResponseTypeDef",
    "CreateSecurityPolicyRequestRequestTypeDef",
    "CreateSecurityPolicyResponseTypeDef",
    "CreateVpcEndpointDetailTypeDef",
    "CreateVpcEndpointRequestRequestTypeDef",
    "CreateVpcEndpointResponseTypeDef",
    "DeleteAccessPolicyRequestRequestTypeDef",
    "DeleteCollectionDetailTypeDef",
    "DeleteCollectionRequestRequestTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeleteSecurityConfigRequestRequestTypeDef",
    "DeleteSecurityPolicyRequestRequestTypeDef",
    "DeleteVpcEndpointDetailTypeDef",
    "DeleteVpcEndpointRequestRequestTypeDef",
    "DeleteVpcEndpointResponseTypeDef",
    "EffectiveLifecyclePolicyDetailTypeDef",
    "EffectiveLifecyclePolicyErrorDetailTypeDef",
    "GetAccessPolicyRequestRequestTypeDef",
    "GetAccessPolicyResponseTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetPoliciesStatsResponseTypeDef",
    "GetSecurityConfigRequestRequestTypeDef",
    "GetSecurityConfigResponseTypeDef",
    "GetSecurityPolicyRequestRequestTypeDef",
    "GetSecurityPolicyResponseTypeDef",
    "LifecyclePolicyDetailTypeDef",
    "LifecyclePolicyErrorDetailTypeDef",
    "LifecyclePolicyIdentifierTypeDef",
    "LifecyclePolicyResourceIdentifierTypeDef",
    "LifecyclePolicyStatsTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "ListAccessPoliciesRequestRequestTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListCollectionsRequestRequestTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListLifecyclePoliciesRequestRequestTypeDef",
    "ListLifecyclePoliciesResponseTypeDef",
    "ListSecurityConfigsRequestRequestTypeDef",
    "ListSecurityConfigsResponseTypeDef",
    "ListSecurityPoliciesRequestRequestTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVpcEndpointsRequestRequestTypeDef",
    "ListVpcEndpointsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SamlConfigOptionsTypeDef",
    "SecurityConfigDetailTypeDef",
    "SecurityConfigStatsTypeDef",
    "SecurityConfigSummaryTypeDef",
    "SecurityPolicyDetailTypeDef",
    "SecurityPolicyStatsTypeDef",
    "SecurityPolicySummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessPolicyRequestRequestTypeDef",
    "UpdateAccessPolicyResponseTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateCollectionDetailTypeDef",
    "UpdateCollectionRequestRequestTypeDef",
    "UpdateCollectionResponseTypeDef",
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    "UpdateLifecyclePolicyResponseTypeDef",
    "UpdateSecurityConfigRequestRequestTypeDef",
    "UpdateSecurityConfigResponseTypeDef",
    "UpdateSecurityPolicyRequestRequestTypeDef",
    "UpdateSecurityPolicyResponseTypeDef",
    "UpdateVpcEndpointDetailTypeDef",
    "UpdateVpcEndpointRequestRequestTypeDef",
    "UpdateVpcEndpointResponseTypeDef",
    "VpcEndpointDetailTypeDef",
    "VpcEndpointErrorDetailTypeDef",
    "VpcEndpointFiltersTypeDef",
    "VpcEndpointSummaryTypeDef",
)

AccessPolicyDetailTypeDef = TypedDict(
    "AccessPolicyDetailTypeDef",
    {
        "createdDate": int,
        "description": str,
        "lastModifiedDate": int,
        "name": str,
        "policy": Dict[str, Any],
        "policyVersion": str,
        "type": Literal["data"],
    },
    total=False,
)

AccessPolicyStatsTypeDef = TypedDict(
    "AccessPolicyStatsTypeDef",
    {
        "DataPolicyCount": int,
    },
    total=False,
)

AccessPolicySummaryTypeDef = TypedDict(
    "AccessPolicySummaryTypeDef",
    {
        "createdDate": int,
        "description": str,
        "lastModifiedDate": int,
        "name": str,
        "policyVersion": str,
        "type": Literal["data"],
    },
    total=False,
)

AccountSettingsDetailTypeDef = TypedDict(
    "AccountSettingsDetailTypeDef",
    {
        "capacityLimits": "CapacityLimitsTypeDef",
    },
    total=False,
)

BatchGetCollectionRequestRequestTypeDef = TypedDict(
    "BatchGetCollectionRequestRequestTypeDef",
    {
        "ids": List[str],
        "names": List[str],
    },
    total=False,
)

BatchGetCollectionResponseTypeDef = TypedDict(
    "BatchGetCollectionResponseTypeDef",
    {
        "collectionDetails": List["CollectionDetailTypeDef"],
        "collectionErrorDetails": List["CollectionErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetEffectiveLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "BatchGetEffectiveLifecyclePolicyRequestRequestTypeDef",
    {
        "resourceIdentifiers": List["LifecyclePolicyResourceIdentifierTypeDef"],
    },
)

BatchGetEffectiveLifecyclePolicyResponseTypeDef = TypedDict(
    "BatchGetEffectiveLifecyclePolicyResponseTypeDef",
    {
        "effectiveLifecyclePolicyDetails": List["EffectiveLifecyclePolicyDetailTypeDef"],
        "effectiveLifecyclePolicyErrorDetails": List["EffectiveLifecyclePolicyErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "BatchGetLifecyclePolicyRequestRequestTypeDef",
    {
        "identifiers": List["LifecyclePolicyIdentifierTypeDef"],
    },
)

BatchGetLifecyclePolicyResponseTypeDef = TypedDict(
    "BatchGetLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyDetails": List["LifecyclePolicyDetailTypeDef"],
        "lifecyclePolicyErrorDetails": List["LifecyclePolicyErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetVpcEndpointRequestRequestTypeDef = TypedDict(
    "BatchGetVpcEndpointRequestRequestTypeDef",
    {
        "ids": List[str],
    },
)

BatchGetVpcEndpointResponseTypeDef = TypedDict(
    "BatchGetVpcEndpointResponseTypeDef",
    {
        "vpcEndpointDetails": List["VpcEndpointDetailTypeDef"],
        "vpcEndpointErrorDetails": List["VpcEndpointErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityLimitsTypeDef = TypedDict(
    "CapacityLimitsTypeDef",
    {
        "maxIndexingCapacityInOCU": int,
        "maxSearchCapacityInOCU": int,
    },
    total=False,
)

CollectionDetailTypeDef = TypedDict(
    "CollectionDetailTypeDef",
    {
        "arn": str,
        "collectionEndpoint": str,
        "createdDate": int,
        "dashboardEndpoint": str,
        "description": str,
        "id": str,
        "kmsKeyArn": str,
        "lastModifiedDate": int,
        "name": str,
        "status": CollectionStatusType,
        "type": CollectionTypeType,
    },
    total=False,
)

CollectionErrorDetailTypeDef = TypedDict(
    "CollectionErrorDetailTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "id": str,
        "name": str,
    },
    total=False,
)

CollectionFiltersTypeDef = TypedDict(
    "CollectionFiltersTypeDef",
    {
        "name": str,
        "status": CollectionStatusType,
    },
    total=False,
)

CollectionSummaryTypeDef = TypedDict(
    "CollectionSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": CollectionStatusType,
    },
    total=False,
)

_RequiredCreateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPolicyRequestRequestTypeDef",
    {
        "name": str,
        "policy": str,
        "type": Literal["data"],
    },
)
_OptionalCreateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreateAccessPolicyRequestRequestTypeDef(
    _RequiredCreateAccessPolicyRequestRequestTypeDef,
    _OptionalCreateAccessPolicyRequestRequestTypeDef,
):
    pass

CreateAccessPolicyResponseTypeDef = TypedDict(
    "CreateAccessPolicyResponseTypeDef",
    {
        "accessPolicyDetail": "AccessPolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCollectionDetailTypeDef = TypedDict(
    "CreateCollectionDetailTypeDef",
    {
        "arn": str,
        "createdDate": int,
        "description": str,
        "id": str,
        "kmsKeyArn": str,
        "lastModifiedDate": int,
        "name": str,
        "status": CollectionStatusType,
        "type": CollectionTypeType,
    },
    total=False,
)

_RequiredCreateCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCollectionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCollectionRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": List["TagTypeDef"],
        "type": CollectionTypeType,
    },
    total=False,
)

class CreateCollectionRequestRequestTypeDef(
    _RequiredCreateCollectionRequestRequestTypeDef, _OptionalCreateCollectionRequestRequestTypeDef
):
    pass

CreateCollectionResponseTypeDef = TypedDict(
    "CreateCollectionResponseTypeDef",
    {
        "createCollectionDetail": "CreateCollectionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLifecyclePolicyRequestRequestTypeDef",
    {
        "name": str,
        "policy": str,
        "type": Literal["retention"],
    },
)
_OptionalCreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLifecyclePolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreateLifecyclePolicyRequestRequestTypeDef(
    _RequiredCreateLifecyclePolicyRequestRequestTypeDef,
    _OptionalCreateLifecyclePolicyRequestRequestTypeDef,
):
    pass

CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyDetail": "LifecyclePolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityConfigRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["saml"],
    },
)
_OptionalCreateSecurityConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityConfigRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "samlOptions": "SamlConfigOptionsTypeDef",
    },
    total=False,
)

class CreateSecurityConfigRequestRequestTypeDef(
    _RequiredCreateSecurityConfigRequestRequestTypeDef,
    _OptionalCreateSecurityConfigRequestRequestTypeDef,
):
    pass

CreateSecurityConfigResponseTypeDef = TypedDict(
    "CreateSecurityConfigResponseTypeDef",
    {
        "securityConfigDetail": "SecurityConfigDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityPolicyRequestRequestTypeDef",
    {
        "name": str,
        "policy": str,
        "type": SecurityPolicyTypeType,
    },
)
_OptionalCreateSecurityPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreateSecurityPolicyRequestRequestTypeDef(
    _RequiredCreateSecurityPolicyRequestRequestTypeDef,
    _OptionalCreateSecurityPolicyRequestRequestTypeDef,
):
    pass

CreateSecurityPolicyResponseTypeDef = TypedDict(
    "CreateSecurityPolicyResponseTypeDef",
    {
        "securityPolicyDetail": "SecurityPolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcEndpointDetailTypeDef = TypedDict(
    "CreateVpcEndpointDetailTypeDef",
    {
        "id": str,
        "name": str,
        "status": VpcEndpointStatusType,
    },
    total=False,
)

_RequiredCreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcEndpointRequestRequestTypeDef",
    {
        "name": str,
        "subnetIds": List[str],
        "vpcId": str,
    },
)
_OptionalCreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcEndpointRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityGroupIds": List[str],
    },
    total=False,
)

class CreateVpcEndpointRequestRequestTypeDef(
    _RequiredCreateVpcEndpointRequestRequestTypeDef, _OptionalCreateVpcEndpointRequestRequestTypeDef
):
    pass

CreateVpcEndpointResponseTypeDef = TypedDict(
    "CreateVpcEndpointResponseTypeDef",
    {
        "createVpcEndpointDetail": "CreateVpcEndpointDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAccessPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccessPolicyRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["data"],
    },
)
_OptionalDeleteAccessPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccessPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAccessPolicyRequestRequestTypeDef(
    _RequiredDeleteAccessPolicyRequestRequestTypeDef,
    _OptionalDeleteAccessPolicyRequestRequestTypeDef,
):
    pass

DeleteCollectionDetailTypeDef = TypedDict(
    "DeleteCollectionDetailTypeDef",
    {
        "id": str,
        "name": str,
        "status": CollectionStatusType,
    },
    total=False,
)

_RequiredDeleteCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCollectionRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCollectionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteCollectionRequestRequestTypeDef(
    _RequiredDeleteCollectionRequestRequestTypeDef, _OptionalDeleteCollectionRequestRequestTypeDef
):
    pass

DeleteCollectionResponseTypeDef = TypedDict(
    "DeleteCollectionResponseTypeDef",
    {
        "deleteCollectionDetail": "DeleteCollectionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["retention"],
    },
)
_OptionalDeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteLifecyclePolicyRequestRequestTypeDef(
    _RequiredDeleteLifecyclePolicyRequestRequestTypeDef,
    _OptionalDeleteLifecyclePolicyRequestRequestTypeDef,
):
    pass

_RequiredDeleteSecurityConfigRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSecurityConfigRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteSecurityConfigRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSecurityConfigRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteSecurityConfigRequestRequestTypeDef(
    _RequiredDeleteSecurityConfigRequestRequestTypeDef,
    _OptionalDeleteSecurityConfigRequestRequestTypeDef,
):
    pass

_RequiredDeleteSecurityPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSecurityPolicyRequestRequestTypeDef",
    {
        "name": str,
        "type": SecurityPolicyTypeType,
    },
)
_OptionalDeleteSecurityPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSecurityPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteSecurityPolicyRequestRequestTypeDef(
    _RequiredDeleteSecurityPolicyRequestRequestTypeDef,
    _OptionalDeleteSecurityPolicyRequestRequestTypeDef,
):
    pass

DeleteVpcEndpointDetailTypeDef = TypedDict(
    "DeleteVpcEndpointDetailTypeDef",
    {
        "id": str,
        "name": str,
        "status": VpcEndpointStatusType,
    },
    total=False,
)

_RequiredDeleteVpcEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteVpcEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteVpcEndpointRequestRequestTypeDef(
    _RequiredDeleteVpcEndpointRequestRequestTypeDef, _OptionalDeleteVpcEndpointRequestRequestTypeDef
):
    pass

DeleteVpcEndpointResponseTypeDef = TypedDict(
    "DeleteVpcEndpointResponseTypeDef",
    {
        "deleteVpcEndpointDetail": "DeleteVpcEndpointDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EffectiveLifecyclePolicyDetailTypeDef = TypedDict(
    "EffectiveLifecyclePolicyDetailTypeDef",
    {
        "noMinRetentionPeriod": bool,
        "policyName": str,
        "resource": str,
        "resourceType": Literal["index"],
        "retentionPeriod": str,
        "type": Literal["retention"],
    },
    total=False,
)

EffectiveLifecyclePolicyErrorDetailTypeDef = TypedDict(
    "EffectiveLifecyclePolicyErrorDetailTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "resource": str,
        "type": Literal["retention"],
    },
    total=False,
)

GetAccessPolicyRequestRequestTypeDef = TypedDict(
    "GetAccessPolicyRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["data"],
    },
)

GetAccessPolicyResponseTypeDef = TypedDict(
    "GetAccessPolicyResponseTypeDef",
    {
        "accessPolicyDetail": "AccessPolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "accountSettingsDetail": "AccountSettingsDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPoliciesStatsResponseTypeDef = TypedDict(
    "GetPoliciesStatsResponseTypeDef",
    {
        "AccessPolicyStats": "AccessPolicyStatsTypeDef",
        "LifecyclePolicyStats": "LifecyclePolicyStatsTypeDef",
        "SecurityConfigStats": "SecurityConfigStatsTypeDef",
        "SecurityPolicyStats": "SecurityPolicyStatsTypeDef",
        "TotalPolicyCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSecurityConfigResponseTypeDef = TypedDict(
    "GetSecurityConfigResponseTypeDef",
    {
        "securityConfigDetail": "SecurityConfigDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityPolicyRequestRequestTypeDef = TypedDict(
    "GetSecurityPolicyRequestRequestTypeDef",
    {
        "name": str,
        "type": SecurityPolicyTypeType,
    },
)

GetSecurityPolicyResponseTypeDef = TypedDict(
    "GetSecurityPolicyResponseTypeDef",
    {
        "securityPolicyDetail": "SecurityPolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicyDetailTypeDef = TypedDict(
    "LifecyclePolicyDetailTypeDef",
    {
        "createdDate": int,
        "description": str,
        "lastModifiedDate": int,
        "name": str,
        "policy": Dict[str, Any],
        "policyVersion": str,
        "type": Literal["retention"],
    },
    total=False,
)

LifecyclePolicyErrorDetailTypeDef = TypedDict(
    "LifecyclePolicyErrorDetailTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "name": str,
        "type": Literal["retention"],
    },
    total=False,
)

LifecyclePolicyIdentifierTypeDef = TypedDict(
    "LifecyclePolicyIdentifierTypeDef",
    {
        "name": str,
        "type": Literal["retention"],
    },
)

LifecyclePolicyResourceIdentifierTypeDef = TypedDict(
    "LifecyclePolicyResourceIdentifierTypeDef",
    {
        "resource": str,
        "type": Literal["retention"],
    },
)

LifecyclePolicyStatsTypeDef = TypedDict(
    "LifecyclePolicyStatsTypeDef",
    {
        "RetentionPolicyCount": int,
    },
    total=False,
)

LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "createdDate": int,
        "description": str,
        "lastModifiedDate": int,
        "name": str,
        "policyVersion": str,
        "type": Literal["retention"],
    },
    total=False,
)

_RequiredListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPoliciesRequestRequestTypeDef",
    {
        "type": Literal["data"],
    },
)
_OptionalListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resource": List[str],
    },
    total=False,
)

class ListAccessPoliciesRequestRequestTypeDef(
    _RequiredListAccessPoliciesRequestRequestTypeDef,
    _OptionalListAccessPoliciesRequestRequestTypeDef,
):
    pass

ListAccessPoliciesResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseTypeDef",
    {
        "accessPolicySummaries": List["AccessPolicySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCollectionsRequestRequestTypeDef = TypedDict(
    "ListCollectionsRequestRequestTypeDef",
    {
        "collectionFilters": "CollectionFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCollectionsResponseTypeDef = TypedDict(
    "ListCollectionsResponseTypeDef",
    {
        "collectionSummaries": List["CollectionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLifecyclePoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListLifecyclePoliciesRequestRequestTypeDef",
    {
        "type": Literal["retention"],
    },
)
_OptionalListLifecyclePoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListLifecyclePoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resources": List[str],
    },
    total=False,
)

class ListLifecyclePoliciesRequestRequestTypeDef(
    _RequiredListLifecyclePoliciesRequestRequestTypeDef,
    _OptionalListLifecyclePoliciesRequestRequestTypeDef,
):
    pass

ListLifecyclePoliciesResponseTypeDef = TypedDict(
    "ListLifecyclePoliciesResponseTypeDef",
    {
        "lifecyclePolicySummaries": List["LifecyclePolicySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityConfigsRequestRequestTypeDef",
    {
        "type": Literal["saml"],
    },
)
_OptionalListSecurityConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityConfigsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSecurityConfigsRequestRequestTypeDef(
    _RequiredListSecurityConfigsRequestRequestTypeDef,
    _OptionalListSecurityConfigsRequestRequestTypeDef,
):
    pass

ListSecurityConfigsResponseTypeDef = TypedDict(
    "ListSecurityConfigsResponseTypeDef",
    {
        "nextToken": str,
        "securityConfigSummaries": List["SecurityConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityPoliciesRequestRequestTypeDef",
    {
        "type": SecurityPolicyTypeType,
    },
)
_OptionalListSecurityPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resource": List[str],
    },
    total=False,
)

class ListSecurityPoliciesRequestRequestTypeDef(
    _RequiredListSecurityPoliciesRequestRequestTypeDef,
    _OptionalListSecurityPoliciesRequestRequestTypeDef,
):
    pass

ListSecurityPoliciesResponseTypeDef = TypedDict(
    "ListSecurityPoliciesResponseTypeDef",
    {
        "nextToken": str,
        "securityPolicySummaries": List["SecurityPolicySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVpcEndpointsRequestRequestTypeDef = TypedDict(
    "ListVpcEndpointsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "vpcEndpointFilters": "VpcEndpointFiltersTypeDef",
    },
    total=False,
)

ListVpcEndpointsResponseTypeDef = TypedDict(
    "ListVpcEndpointsResponseTypeDef",
    {
        "nextToken": str,
        "vpcEndpointSummaries": List["VpcEndpointSummaryTypeDef"],
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

_RequiredSamlConfigOptionsTypeDef = TypedDict(
    "_RequiredSamlConfigOptionsTypeDef",
    {
        "metadata": str,
    },
)
_OptionalSamlConfigOptionsTypeDef = TypedDict(
    "_OptionalSamlConfigOptionsTypeDef",
    {
        "groupAttribute": str,
        "sessionTimeout": int,
        "userAttribute": str,
    },
    total=False,
)

class SamlConfigOptionsTypeDef(
    _RequiredSamlConfigOptionsTypeDef, _OptionalSamlConfigOptionsTypeDef
):
    pass

SecurityConfigDetailTypeDef = TypedDict(
    "SecurityConfigDetailTypeDef",
    {
        "configVersion": str,
        "createdDate": int,
        "description": str,
        "id": str,
        "lastModifiedDate": int,
        "samlOptions": "SamlConfigOptionsTypeDef",
        "type": Literal["saml"],
    },
    total=False,
)

SecurityConfigStatsTypeDef = TypedDict(
    "SecurityConfigStatsTypeDef",
    {
        "SamlConfigCount": int,
    },
    total=False,
)

SecurityConfigSummaryTypeDef = TypedDict(
    "SecurityConfigSummaryTypeDef",
    {
        "configVersion": str,
        "createdDate": int,
        "description": str,
        "id": str,
        "lastModifiedDate": int,
        "type": Literal["saml"],
    },
    total=False,
)

SecurityPolicyDetailTypeDef = TypedDict(
    "SecurityPolicyDetailTypeDef",
    {
        "createdDate": int,
        "description": str,
        "lastModifiedDate": int,
        "name": str,
        "policy": Dict[str, Any],
        "policyVersion": str,
        "type": SecurityPolicyTypeType,
    },
    total=False,
)

SecurityPolicyStatsTypeDef = TypedDict(
    "SecurityPolicyStatsTypeDef",
    {
        "EncryptionPolicyCount": int,
        "NetworkPolicyCount": int,
    },
    total=False,
)

SecurityPolicySummaryTypeDef = TypedDict(
    "SecurityPolicySummaryTypeDef",
    {
        "createdDate": int,
        "description": str,
        "lastModifiedDate": int,
        "name": str,
        "policyVersion": str,
        "type": SecurityPolicyTypeType,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessPolicyRequestRequestTypeDef",
    {
        "name": str,
        "policyVersion": str,
        "type": Literal["data"],
    },
)
_OptionalUpdateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "policy": str,
    },
    total=False,
)

class UpdateAccessPolicyRequestRequestTypeDef(
    _RequiredUpdateAccessPolicyRequestRequestTypeDef,
    _OptionalUpdateAccessPolicyRequestRequestTypeDef,
):
    pass

UpdateAccessPolicyResponseTypeDef = TypedDict(
    "UpdateAccessPolicyResponseTypeDef",
    {
        "accessPolicyDetail": "AccessPolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "capacityLimits": "CapacityLimitsTypeDef",
    },
    total=False,
)

UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef",
    {
        "accountSettingsDetail": "AccountSettingsDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCollectionDetailTypeDef = TypedDict(
    "UpdateCollectionDetailTypeDef",
    {
        "arn": str,
        "createdDate": int,
        "description": str,
        "id": str,
        "lastModifiedDate": int,
        "name": str,
        "status": CollectionStatusType,
        "type": CollectionTypeType,
    },
    total=False,
)

_RequiredUpdateCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCollectionRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCollectionRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class UpdateCollectionRequestRequestTypeDef(
    _RequiredUpdateCollectionRequestRequestTypeDef, _OptionalUpdateCollectionRequestRequestTypeDef
):
    pass

UpdateCollectionResponseTypeDef = TypedDict(
    "UpdateCollectionResponseTypeDef",
    {
        "updateCollectionDetail": "UpdateCollectionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "name": str,
        "policyVersion": str,
        "type": Literal["retention"],
    },
)
_OptionalUpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "policy": str,
    },
    total=False,
)

class UpdateLifecyclePolicyRequestRequestTypeDef(
    _RequiredUpdateLifecyclePolicyRequestRequestTypeDef,
    _OptionalUpdateLifecyclePolicyRequestRequestTypeDef,
):
    pass

UpdateLifecyclePolicyResponseTypeDef = TypedDict(
    "UpdateLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyDetail": "LifecyclePolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecurityConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityConfigRequestRequestTypeDef",
    {
        "configVersion": str,
        "id": str,
    },
)
_OptionalUpdateSecurityConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityConfigRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "samlOptions": "SamlConfigOptionsTypeDef",
    },
    total=False,
)

class UpdateSecurityConfigRequestRequestTypeDef(
    _RequiredUpdateSecurityConfigRequestRequestTypeDef,
    _OptionalUpdateSecurityConfigRequestRequestTypeDef,
):
    pass

UpdateSecurityConfigResponseTypeDef = TypedDict(
    "UpdateSecurityConfigResponseTypeDef",
    {
        "securityConfigDetail": "SecurityConfigDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecurityPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityPolicyRequestRequestTypeDef",
    {
        "name": str,
        "policyVersion": str,
        "type": SecurityPolicyTypeType,
    },
)
_OptionalUpdateSecurityPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "policy": str,
    },
    total=False,
)

class UpdateSecurityPolicyRequestRequestTypeDef(
    _RequiredUpdateSecurityPolicyRequestRequestTypeDef,
    _OptionalUpdateSecurityPolicyRequestRequestTypeDef,
):
    pass

UpdateSecurityPolicyResponseTypeDef = TypedDict(
    "UpdateSecurityPolicyResponseTypeDef",
    {
        "securityPolicyDetail": "SecurityPolicyDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVpcEndpointDetailTypeDef = TypedDict(
    "UpdateVpcEndpointDetailTypeDef",
    {
        "id": str,
        "lastModifiedDate": int,
        "name": str,
        "securityGroupIds": List[str],
        "status": VpcEndpointStatusType,
        "subnetIds": List[str],
    },
    total=False,
)

_RequiredUpdateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVpcEndpointRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVpcEndpointRequestRequestTypeDef",
    {
        "addSecurityGroupIds": List[str],
        "addSubnetIds": List[str],
        "clientToken": str,
        "removeSecurityGroupIds": List[str],
        "removeSubnetIds": List[str],
    },
    total=False,
)

class UpdateVpcEndpointRequestRequestTypeDef(
    _RequiredUpdateVpcEndpointRequestRequestTypeDef, _OptionalUpdateVpcEndpointRequestRequestTypeDef
):
    pass

UpdateVpcEndpointResponseTypeDef = TypedDict(
    "UpdateVpcEndpointResponseTypeDef",
    {
        "UpdateVpcEndpointDetail": "UpdateVpcEndpointDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcEndpointDetailTypeDef = TypedDict(
    "VpcEndpointDetailTypeDef",
    {
        "createdDate": int,
        "id": str,
        "name": str,
        "securityGroupIds": List[str],
        "status": VpcEndpointStatusType,
        "subnetIds": List[str],
        "vpcId": str,
    },
    total=False,
)

VpcEndpointErrorDetailTypeDef = TypedDict(
    "VpcEndpointErrorDetailTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "id": str,
    },
    total=False,
)

VpcEndpointFiltersTypeDef = TypedDict(
    "VpcEndpointFiltersTypeDef",
    {
        "status": VpcEndpointStatusType,
    },
    total=False,
)

VpcEndpointSummaryTypeDef = TypedDict(
    "VpcEndpointSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "status": VpcEndpointStatusType,
    },
    total=False,
)
