"""
Type annotations for verifiedpermissions service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_verifiedpermissions.type_defs import ActionIdentifierTypeDef

    data: ActionIdentifierTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    BatchGetPolicyErrorCodeType,
    CedarVersionType,
    DecisionType,
    DeletionProtectionType,
    PolicyEffectType,
    PolicyTypeType,
    ValidationModeType,
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
    "ActionIdentifierTypeDef",
    "AttributeValueOutputTypeDef",
    "AttributeValueTypeDef",
    "AttributeValueUnionTypeDef",
    "BatchGetPolicyErrorItemTypeDef",
    "BatchGetPolicyInputItemTypeDef",
    "BatchGetPolicyInputTypeDef",
    "BatchGetPolicyOutputItemTypeDef",
    "BatchGetPolicyOutputTypeDef",
    "BatchIsAuthorizedInputItemOutputTypeDef",
    "BatchIsAuthorizedInputItemTypeDef",
    "BatchIsAuthorizedInputItemUnionTypeDef",
    "BatchIsAuthorizedInputTypeDef",
    "BatchIsAuthorizedOutputItemTypeDef",
    "BatchIsAuthorizedOutputTypeDef",
    "BatchIsAuthorizedWithTokenInputItemOutputTypeDef",
    "BatchIsAuthorizedWithTokenInputItemTypeDef",
    "BatchIsAuthorizedWithTokenInputItemUnionTypeDef",
    "BatchIsAuthorizedWithTokenInputTypeDef",
    "BatchIsAuthorizedWithTokenOutputItemTypeDef",
    "BatchIsAuthorizedWithTokenOutputTypeDef",
    "CognitoGroupConfigurationDetailTypeDef",
    "CognitoGroupConfigurationItemTypeDef",
    "CognitoGroupConfigurationTypeDef",
    "CognitoUserPoolConfigurationDetailTypeDef",
    "CognitoUserPoolConfigurationItemTypeDef",
    "CognitoUserPoolConfigurationTypeDef",
    "ConfigurationDetailTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationTypeDef",
    "ContextDefinitionOutputTypeDef",
    "ContextDefinitionTypeDef",
    "ContextDefinitionUnionTypeDef",
    "CreateIdentitySourceInputTypeDef",
    "CreateIdentitySourceOutputTypeDef",
    "CreatePolicyInputTypeDef",
    "CreatePolicyOutputTypeDef",
    "CreatePolicyStoreInputTypeDef",
    "CreatePolicyStoreOutputTypeDef",
    "CreatePolicyTemplateInputTypeDef",
    "CreatePolicyTemplateOutputTypeDef",
    "DeleteIdentitySourceInputTypeDef",
    "DeletePolicyInputTypeDef",
    "DeletePolicyStoreInputTypeDef",
    "DeletePolicyTemplateInputTypeDef",
    "DeterminingPolicyItemTypeDef",
    "EntitiesDefinitionTypeDef",
    "EntityIdentifierTypeDef",
    "EntityItemTypeDef",
    "EntityReferenceTypeDef",
    "EvaluationErrorItemTypeDef",
    "GetIdentitySourceInputTypeDef",
    "GetIdentitySourceOutputTypeDef",
    "GetPolicyInputTypeDef",
    "GetPolicyOutputTypeDef",
    "GetPolicyStoreInputTypeDef",
    "GetPolicyStoreOutputTypeDef",
    "GetPolicyTemplateInputTypeDef",
    "GetPolicyTemplateOutputTypeDef",
    "GetSchemaInputTypeDef",
    "GetSchemaOutputTypeDef",
    "IdentitySourceDetailsTypeDef",
    "IdentitySourceFilterTypeDef",
    "IdentitySourceItemDetailsTypeDef",
    "IdentitySourceItemTypeDef",
    "IsAuthorizedInputTypeDef",
    "IsAuthorizedOutputTypeDef",
    "IsAuthorizedWithTokenInputTypeDef",
    "IsAuthorizedWithTokenOutputTypeDef",
    "ListIdentitySourcesInputPaginateTypeDef",
    "ListIdentitySourcesInputTypeDef",
    "ListIdentitySourcesOutputTypeDef",
    "ListPoliciesInputPaginateTypeDef",
    "ListPoliciesInputTypeDef",
    "ListPoliciesOutputTypeDef",
    "ListPolicyStoresInputPaginateTypeDef",
    "ListPolicyStoresInputTypeDef",
    "ListPolicyStoresOutputTypeDef",
    "ListPolicyTemplatesInputPaginateTypeDef",
    "ListPolicyTemplatesInputTypeDef",
    "ListPolicyTemplatesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "OpenIdConnectAccessTokenConfigurationDetailTypeDef",
    "OpenIdConnectAccessTokenConfigurationItemTypeDef",
    "OpenIdConnectAccessTokenConfigurationTypeDef",
    "OpenIdConnectConfigurationDetailTypeDef",
    "OpenIdConnectConfigurationItemTypeDef",
    "OpenIdConnectConfigurationTypeDef",
    "OpenIdConnectGroupConfigurationDetailTypeDef",
    "OpenIdConnectGroupConfigurationItemTypeDef",
    "OpenIdConnectGroupConfigurationTypeDef",
    "OpenIdConnectIdentityTokenConfigurationDetailTypeDef",
    "OpenIdConnectIdentityTokenConfigurationItemTypeDef",
    "OpenIdConnectIdentityTokenConfigurationTypeDef",
    "OpenIdConnectTokenSelectionDetailTypeDef",
    "OpenIdConnectTokenSelectionItemTypeDef",
    "OpenIdConnectTokenSelectionTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDefinitionDetailTypeDef",
    "PolicyDefinitionItemTypeDef",
    "PolicyDefinitionTypeDef",
    "PolicyFilterTypeDef",
    "PolicyItemTypeDef",
    "PolicyStoreItemTypeDef",
    "PolicyTemplateItemTypeDef",
    "PutSchemaInputTypeDef",
    "PutSchemaOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaDefinitionTypeDef",
    "StaticPolicyDefinitionDetailTypeDef",
    "StaticPolicyDefinitionItemTypeDef",
    "StaticPolicyDefinitionTypeDef",
    "TagResourceInputTypeDef",
    "TemplateLinkedPolicyDefinitionDetailTypeDef",
    "TemplateLinkedPolicyDefinitionItemTypeDef",
    "TemplateLinkedPolicyDefinitionTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateCognitoGroupConfigurationTypeDef",
    "UpdateCognitoUserPoolConfigurationTypeDef",
    "UpdateConfigurationTypeDef",
    "UpdateIdentitySourceInputTypeDef",
    "UpdateIdentitySourceOutputTypeDef",
    "UpdateOpenIdConnectAccessTokenConfigurationTypeDef",
    "UpdateOpenIdConnectConfigurationTypeDef",
    "UpdateOpenIdConnectGroupConfigurationTypeDef",
    "UpdateOpenIdConnectIdentityTokenConfigurationTypeDef",
    "UpdateOpenIdConnectTokenSelectionTypeDef",
    "UpdatePolicyDefinitionTypeDef",
    "UpdatePolicyInputTypeDef",
    "UpdatePolicyOutputTypeDef",
    "UpdatePolicyStoreInputTypeDef",
    "UpdatePolicyStoreOutputTypeDef",
    "UpdatePolicyTemplateInputTypeDef",
    "UpdatePolicyTemplateOutputTypeDef",
    "UpdateStaticPolicyDefinitionTypeDef",
    "ValidationSettingsTypeDef",
)

class ActionIdentifierTypeDef(TypedDict):
    actionType: str
    actionId: str

class EntityIdentifierTypeDef(TypedDict):
    entityType: str
    entityId: str

class BatchGetPolicyErrorItemTypeDef(TypedDict):
    code: BatchGetPolicyErrorCodeType
    policyStoreId: str
    policyId: str
    message: str

class BatchGetPolicyInputItemTypeDef(TypedDict):
    policyStoreId: str
    policyId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeterminingPolicyItemTypeDef(TypedDict):
    policyId: str

class EvaluationErrorItemTypeDef(TypedDict):
    errorDescription: str

class CognitoGroupConfigurationDetailTypeDef(TypedDict):
    groupEntityType: NotRequired[str]

class CognitoGroupConfigurationItemTypeDef(TypedDict):
    groupEntityType: NotRequired[str]

class CognitoGroupConfigurationTypeDef(TypedDict):
    groupEntityType: str

class ValidationSettingsTypeDef(TypedDict):
    mode: ValidationModeType

class CreatePolicyTemplateInputTypeDef(TypedDict):
    policyStoreId: str
    statement: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class DeleteIdentitySourceInputTypeDef(TypedDict):
    policyStoreId: str
    identitySourceId: str

class DeletePolicyInputTypeDef(TypedDict):
    policyStoreId: str
    policyId: str

class DeletePolicyStoreInputTypeDef(TypedDict):
    policyStoreId: str

class DeletePolicyTemplateInputTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str

class GetIdentitySourceInputTypeDef(TypedDict):
    policyStoreId: str
    identitySourceId: str

class IdentitySourceDetailsTypeDef(TypedDict):
    clientIds: NotRequired[List[str]]
    userPoolArn: NotRequired[str]
    discoveryUrl: NotRequired[str]
    openIdIssuer: NotRequired[Literal["COGNITO"]]

class GetPolicyInputTypeDef(TypedDict):
    policyStoreId: str
    policyId: str

class GetPolicyStoreInputTypeDef(TypedDict):
    policyStoreId: str
    tags: NotRequired[bool]

class GetPolicyTemplateInputTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str

class GetSchemaInputTypeDef(TypedDict):
    policyStoreId: str

class IdentitySourceFilterTypeDef(TypedDict):
    principalEntityType: NotRequired[str]

class IdentitySourceItemDetailsTypeDef(TypedDict):
    clientIds: NotRequired[List[str]]
    userPoolArn: NotRequired[str]
    discoveryUrl: NotRequired[str]
    openIdIssuer: NotRequired[Literal["COGNITO"]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListPolicyStoresInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PolicyStoreItemTypeDef(TypedDict):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: NotRequired[datetime]
    description: NotRequired[str]

class ListPolicyTemplatesInputTypeDef(TypedDict):
    policyStoreId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PolicyTemplateItemTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    description: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class OpenIdConnectAccessTokenConfigurationDetailTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    audiences: NotRequired[List[str]]

class OpenIdConnectAccessTokenConfigurationItemTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    audiences: NotRequired[List[str]]

class OpenIdConnectAccessTokenConfigurationTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    audiences: NotRequired[Sequence[str]]

class OpenIdConnectGroupConfigurationDetailTypeDef(TypedDict):
    groupClaim: str
    groupEntityType: str

class OpenIdConnectGroupConfigurationItemTypeDef(TypedDict):
    groupClaim: str
    groupEntityType: str

class OpenIdConnectGroupConfigurationTypeDef(TypedDict):
    groupClaim: str
    groupEntityType: str

class OpenIdConnectIdentityTokenConfigurationDetailTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    clientIds: NotRequired[List[str]]

class OpenIdConnectIdentityTokenConfigurationItemTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    clientIds: NotRequired[List[str]]

class OpenIdConnectIdentityTokenConfigurationTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    clientIds: NotRequired[Sequence[str]]

class StaticPolicyDefinitionDetailTypeDef(TypedDict):
    statement: str
    description: NotRequired[str]

class StaticPolicyDefinitionItemTypeDef(TypedDict):
    description: NotRequired[str]

class StaticPolicyDefinitionTypeDef(TypedDict):
    statement: str
    description: NotRequired[str]

class SchemaDefinitionTypeDef(TypedDict):
    cedarJson: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateCognitoGroupConfigurationTypeDef(TypedDict):
    groupEntityType: str

class UpdateOpenIdConnectAccessTokenConfigurationTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    audiences: NotRequired[Sequence[str]]

class UpdateOpenIdConnectGroupConfigurationTypeDef(TypedDict):
    groupClaim: str
    groupEntityType: str

class UpdateOpenIdConnectIdentityTokenConfigurationTypeDef(TypedDict):
    principalIdClaim: NotRequired[str]
    clientIds: NotRequired[Sequence[str]]

class UpdateStaticPolicyDefinitionTypeDef(TypedDict):
    statement: str
    description: NotRequired[str]

class UpdatePolicyTemplateInputTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str
    statement: str
    description: NotRequired[str]

AttributeValueOutputTypeDef = TypedDict(
    "AttributeValueOutputTypeDef",
    {
        "boolean": NotRequired[bool],
        "entityIdentifier": NotRequired[EntityIdentifierTypeDef],
        "long": NotRequired[int],
        "string": NotRequired[str],
        "set": NotRequired[List[Dict[str, Any]]],
        "record": NotRequired[Dict[str, Dict[str, Any]]],
        "ipaddr": NotRequired[str],
        "decimal": NotRequired[str],
    },
)
AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "boolean": NotRequired[bool],
        "entityIdentifier": NotRequired[EntityIdentifierTypeDef],
        "long": NotRequired[int],
        "string": NotRequired[str],
        "set": NotRequired[Sequence[Mapping[str, Any]]],
        "record": NotRequired[Mapping[str, Mapping[str, Any]]],
        "ipaddr": NotRequired[str],
        "decimal": NotRequired[str],
    },
)

class EntityReferenceTypeDef(TypedDict):
    unspecified: NotRequired[bool]
    identifier: NotRequired[EntityIdentifierTypeDef]

class TemplateLinkedPolicyDefinitionDetailTypeDef(TypedDict):
    policyTemplateId: str
    principal: NotRequired[EntityIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]

class TemplateLinkedPolicyDefinitionItemTypeDef(TypedDict):
    policyTemplateId: str
    principal: NotRequired[EntityIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]

class TemplateLinkedPolicyDefinitionTypeDef(TypedDict):
    policyTemplateId: str
    principal: NotRequired[EntityIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]

class BatchGetPolicyInputTypeDef(TypedDict):
    requests: Sequence[BatchGetPolicyInputItemTypeDef]

class CreateIdentitySourceOutputTypeDef(TypedDict):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyOutputTypeDef(TypedDict):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifierTypeDef
    resource: EntityIdentifierTypeDef
    actions: List[ActionIdentifierTypeDef]
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyStoreOutputTypeDef(TypedDict):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyTemplateOutputTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyTemplateOutputTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str
    description: str
    statement: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaOutputTypeDef(TypedDict):
    policyStoreId: str
    schema: str
    createdDate: datetime
    lastUpdatedDate: datetime
    namespaces: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSchemaOutputTypeDef(TypedDict):
    policyStoreId: str
    namespaces: List[str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentitySourceOutputTypeDef(TypedDict):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyOutputTypeDef(TypedDict):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifierTypeDef
    resource: EntityIdentifierTypeDef
    actions: List[ActionIdentifierTypeDef]
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyStoreOutputTypeDef(TypedDict):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyTemplateOutputTypeDef(TypedDict):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class IsAuthorizedOutputTypeDef(TypedDict):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IsAuthorizedWithTokenOutputTypeDef(TypedDict):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]
    principal: EntityIdentifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CognitoUserPoolConfigurationDetailTypeDef(TypedDict):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: NotRequired[CognitoGroupConfigurationDetailTypeDef]

class CognitoUserPoolConfigurationItemTypeDef(TypedDict):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: NotRequired[CognitoGroupConfigurationItemTypeDef]

class CognitoUserPoolConfigurationTypeDef(TypedDict):
    userPoolArn: str
    clientIds: NotRequired[Sequence[str]]
    groupConfiguration: NotRequired[CognitoGroupConfigurationTypeDef]

class CreatePolicyStoreInputTypeDef(TypedDict):
    validationSettings: ValidationSettingsTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]
    deletionProtection: NotRequired[DeletionProtectionType]
    tags: NotRequired[Mapping[str, str]]

class GetPolicyStoreOutputTypeDef(TypedDict):
    policyStoreId: str
    arn: str
    validationSettings: ValidationSettingsTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    description: str
    deletionProtection: DeletionProtectionType
    cedarVersion: CedarVersionType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyStoreInputTypeDef(TypedDict):
    policyStoreId: str
    validationSettings: ValidationSettingsTypeDef
    deletionProtection: NotRequired[DeletionProtectionType]
    description: NotRequired[str]

class ListIdentitySourcesInputTypeDef(TypedDict):
    policyStoreId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[IdentitySourceFilterTypeDef]]

class ListIdentitySourcesInputPaginateTypeDef(TypedDict):
    policyStoreId: str
    filters: NotRequired[Sequence[IdentitySourceFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyStoresInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyTemplatesInputPaginateTypeDef(TypedDict):
    policyStoreId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyStoresOutputTypeDef(TypedDict):
    policyStores: List[PolicyStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPolicyTemplatesOutputTypeDef(TypedDict):
    policyTemplates: List[PolicyTemplateItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class OpenIdConnectTokenSelectionDetailTypeDef(TypedDict):
    accessTokenOnly: NotRequired[OpenIdConnectAccessTokenConfigurationDetailTypeDef]
    identityTokenOnly: NotRequired[OpenIdConnectIdentityTokenConfigurationDetailTypeDef]

class OpenIdConnectTokenSelectionItemTypeDef(TypedDict):
    accessTokenOnly: NotRequired[OpenIdConnectAccessTokenConfigurationItemTypeDef]
    identityTokenOnly: NotRequired[OpenIdConnectIdentityTokenConfigurationItemTypeDef]

class OpenIdConnectTokenSelectionTypeDef(TypedDict):
    accessTokenOnly: NotRequired[OpenIdConnectAccessTokenConfigurationTypeDef]
    identityTokenOnly: NotRequired[OpenIdConnectIdentityTokenConfigurationTypeDef]

class PutSchemaInputTypeDef(TypedDict):
    policyStoreId: str
    definition: SchemaDefinitionTypeDef

class UpdateCognitoUserPoolConfigurationTypeDef(TypedDict):
    userPoolArn: str
    clientIds: NotRequired[Sequence[str]]
    groupConfiguration: NotRequired[UpdateCognitoGroupConfigurationTypeDef]

class UpdateOpenIdConnectTokenSelectionTypeDef(TypedDict):
    accessTokenOnly: NotRequired[UpdateOpenIdConnectAccessTokenConfigurationTypeDef]
    identityTokenOnly: NotRequired[UpdateOpenIdConnectIdentityTokenConfigurationTypeDef]

class UpdatePolicyDefinitionTypeDef(TypedDict):
    static: NotRequired[UpdateStaticPolicyDefinitionTypeDef]

class ContextDefinitionOutputTypeDef(TypedDict):
    contextMap: NotRequired[Dict[str, AttributeValueOutputTypeDef]]
    cedarJson: NotRequired[str]

AttributeValueUnionTypeDef = Union[AttributeValueTypeDef, AttributeValueOutputTypeDef]

class PolicyFilterTypeDef(TypedDict):
    principal: NotRequired[EntityReferenceTypeDef]
    resource: NotRequired[EntityReferenceTypeDef]
    policyType: NotRequired[PolicyTypeType]
    policyTemplateId: NotRequired[str]

class PolicyDefinitionDetailTypeDef(TypedDict):
    static: NotRequired[StaticPolicyDefinitionDetailTypeDef]
    templateLinked: NotRequired[TemplateLinkedPolicyDefinitionDetailTypeDef]

class PolicyDefinitionItemTypeDef(TypedDict):
    static: NotRequired[StaticPolicyDefinitionItemTypeDef]
    templateLinked: NotRequired[TemplateLinkedPolicyDefinitionItemTypeDef]

class PolicyDefinitionTypeDef(TypedDict):
    static: NotRequired[StaticPolicyDefinitionTypeDef]
    templateLinked: NotRequired[TemplateLinkedPolicyDefinitionTypeDef]

class OpenIdConnectConfigurationDetailTypeDef(TypedDict):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionDetailTypeDef
    entityIdPrefix: NotRequired[str]
    groupConfiguration: NotRequired[OpenIdConnectGroupConfigurationDetailTypeDef]

class OpenIdConnectConfigurationItemTypeDef(TypedDict):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionItemTypeDef
    entityIdPrefix: NotRequired[str]
    groupConfiguration: NotRequired[OpenIdConnectGroupConfigurationItemTypeDef]

class OpenIdConnectConfigurationTypeDef(TypedDict):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionTypeDef
    entityIdPrefix: NotRequired[str]
    groupConfiguration: NotRequired[OpenIdConnectGroupConfigurationTypeDef]

class UpdateOpenIdConnectConfigurationTypeDef(TypedDict):
    issuer: str
    tokenSelection: UpdateOpenIdConnectTokenSelectionTypeDef
    entityIdPrefix: NotRequired[str]
    groupConfiguration: NotRequired[UpdateOpenIdConnectGroupConfigurationTypeDef]

class UpdatePolicyInputTypeDef(TypedDict):
    policyStoreId: str
    policyId: str
    definition: UpdatePolicyDefinitionTypeDef

class BatchIsAuthorizedInputItemOutputTypeDef(TypedDict):
    principal: NotRequired[EntityIdentifierTypeDef]
    action: NotRequired[ActionIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    context: NotRequired[ContextDefinitionOutputTypeDef]

class BatchIsAuthorizedWithTokenInputItemOutputTypeDef(TypedDict):
    action: NotRequired[ActionIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    context: NotRequired[ContextDefinitionOutputTypeDef]

class ContextDefinitionTypeDef(TypedDict):
    contextMap: NotRequired[Mapping[str, AttributeValueUnionTypeDef]]
    cedarJson: NotRequired[str]

class EntityItemTypeDef(TypedDict):
    identifier: EntityIdentifierTypeDef
    attributes: NotRequired[Mapping[str, AttributeValueUnionTypeDef]]
    parents: NotRequired[Sequence[EntityIdentifierTypeDef]]

ListPoliciesInputPaginateTypeDef = TypedDict(
    "ListPoliciesInputPaginateTypeDef",
    {
        "policyStoreId": str,
        "filter": NotRequired[PolicyFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesInputTypeDef = TypedDict(
    "ListPoliciesInputTypeDef",
    {
        "policyStoreId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[PolicyFilterTypeDef],
    },
)

class BatchGetPolicyOutputItemTypeDef(TypedDict):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    definition: PolicyDefinitionDetailTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime

class GetPolicyOutputTypeDef(TypedDict):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifierTypeDef
    resource: EntityIdentifierTypeDef
    actions: List[ActionIdentifierTypeDef]
    definition: PolicyDefinitionDetailTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyItemTypeDef(TypedDict):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    definition: PolicyDefinitionItemTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    principal: NotRequired[EntityIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    actions: NotRequired[List[ActionIdentifierTypeDef]]
    effect: NotRequired[PolicyEffectType]

class CreatePolicyInputTypeDef(TypedDict):
    policyStoreId: str
    definition: PolicyDefinitionTypeDef
    clientToken: NotRequired[str]

class ConfigurationDetailTypeDef(TypedDict):
    cognitoUserPoolConfiguration: NotRequired[CognitoUserPoolConfigurationDetailTypeDef]
    openIdConnectConfiguration: NotRequired[OpenIdConnectConfigurationDetailTypeDef]

class ConfigurationItemTypeDef(TypedDict):
    cognitoUserPoolConfiguration: NotRequired[CognitoUserPoolConfigurationItemTypeDef]
    openIdConnectConfiguration: NotRequired[OpenIdConnectConfigurationItemTypeDef]

class ConfigurationTypeDef(TypedDict):
    cognitoUserPoolConfiguration: NotRequired[CognitoUserPoolConfigurationTypeDef]
    openIdConnectConfiguration: NotRequired[OpenIdConnectConfigurationTypeDef]

class UpdateConfigurationTypeDef(TypedDict):
    cognitoUserPoolConfiguration: NotRequired[UpdateCognitoUserPoolConfigurationTypeDef]
    openIdConnectConfiguration: NotRequired[UpdateOpenIdConnectConfigurationTypeDef]

class BatchIsAuthorizedOutputItemTypeDef(TypedDict):
    request: BatchIsAuthorizedInputItemOutputTypeDef
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]

class BatchIsAuthorizedWithTokenOutputItemTypeDef(TypedDict):
    request: BatchIsAuthorizedWithTokenInputItemOutputTypeDef
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]

ContextDefinitionUnionTypeDef = Union[ContextDefinitionTypeDef, ContextDefinitionOutputTypeDef]

class EntitiesDefinitionTypeDef(TypedDict):
    entityList: NotRequired[Sequence[EntityItemTypeDef]]
    cedarJson: NotRequired[str]

class BatchGetPolicyOutputTypeDef(TypedDict):
    results: List[BatchGetPolicyOutputItemTypeDef]
    errors: List[BatchGetPolicyErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesOutputTypeDef(TypedDict):
    policies: List[PolicyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetIdentitySourceOutputTypeDef(TypedDict):
    createdDate: datetime
    details: IdentitySourceDetailsTypeDef
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    configuration: ConfigurationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IdentitySourceItemTypeDef(TypedDict):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    details: NotRequired[IdentitySourceItemDetailsTypeDef]
    configuration: NotRequired[ConfigurationItemTypeDef]

class CreateIdentitySourceInputTypeDef(TypedDict):
    policyStoreId: str
    configuration: ConfigurationTypeDef
    clientToken: NotRequired[str]
    principalEntityType: NotRequired[str]

class UpdateIdentitySourceInputTypeDef(TypedDict):
    policyStoreId: str
    identitySourceId: str
    updateConfiguration: UpdateConfigurationTypeDef
    principalEntityType: NotRequired[str]

class BatchIsAuthorizedOutputTypeDef(TypedDict):
    results: List[BatchIsAuthorizedOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchIsAuthorizedWithTokenOutputTypeDef(TypedDict):
    principal: EntityIdentifierTypeDef
    results: List[BatchIsAuthorizedWithTokenOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchIsAuthorizedInputItemTypeDef(TypedDict):
    principal: NotRequired[EntityIdentifierTypeDef]
    action: NotRequired[ActionIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    context: NotRequired[ContextDefinitionUnionTypeDef]

class BatchIsAuthorizedWithTokenInputItemTypeDef(TypedDict):
    action: NotRequired[ActionIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    context: NotRequired[ContextDefinitionUnionTypeDef]

class IsAuthorizedInputTypeDef(TypedDict):
    policyStoreId: str
    principal: NotRequired[EntityIdentifierTypeDef]
    action: NotRequired[ActionIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    context: NotRequired[ContextDefinitionUnionTypeDef]
    entities: NotRequired[EntitiesDefinitionTypeDef]

class IsAuthorizedWithTokenInputTypeDef(TypedDict):
    policyStoreId: str
    identityToken: NotRequired[str]
    accessToken: NotRequired[str]
    action: NotRequired[ActionIdentifierTypeDef]
    resource: NotRequired[EntityIdentifierTypeDef]
    context: NotRequired[ContextDefinitionUnionTypeDef]
    entities: NotRequired[EntitiesDefinitionTypeDef]

class ListIdentitySourcesOutputTypeDef(TypedDict):
    identitySources: List[IdentitySourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

BatchIsAuthorizedInputItemUnionTypeDef = Union[
    BatchIsAuthorizedInputItemTypeDef, BatchIsAuthorizedInputItemOutputTypeDef
]
BatchIsAuthorizedWithTokenInputItemUnionTypeDef = Union[
    BatchIsAuthorizedWithTokenInputItemTypeDef, BatchIsAuthorizedWithTokenInputItemOutputTypeDef
]

class BatchIsAuthorizedInputTypeDef(TypedDict):
    policyStoreId: str
    requests: Sequence[BatchIsAuthorizedInputItemUnionTypeDef]
    entities: NotRequired[EntitiesDefinitionTypeDef]

class BatchIsAuthorizedWithTokenInputTypeDef(TypedDict):
    policyStoreId: str
    requests: Sequence[BatchIsAuthorizedWithTokenInputItemUnionTypeDef]
    identityToken: NotRequired[str]
    accessToken: NotRequired[str]
    entities: NotRequired[EntitiesDefinitionTypeDef]
