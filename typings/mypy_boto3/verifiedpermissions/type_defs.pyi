"""
Type annotations for verifiedpermissions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_verifiedpermissions.type_defs import ActionIdentifierTypeDef

    data: ActionIdentifierTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import DecisionType, PolicyEffectType, PolicyTypeType, ValidationModeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionIdentifierTypeDef",
    "AttributeValueTypeDef",
    "BatchIsAuthorizedInputItemTypeDef",
    "BatchIsAuthorizedInputRequestTypeDef",
    "BatchIsAuthorizedOutputItemTypeDef",
    "BatchIsAuthorizedOutputTypeDef",
    "BatchIsAuthorizedWithTokenInputItemTypeDef",
    "BatchIsAuthorizedWithTokenInputRequestTypeDef",
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
    "ContextDefinitionTypeDef",
    "CreateIdentitySourceInputRequestTypeDef",
    "CreateIdentitySourceOutputTypeDef",
    "CreatePolicyInputRequestTypeDef",
    "CreatePolicyOutputTypeDef",
    "CreatePolicyStoreInputRequestTypeDef",
    "CreatePolicyStoreOutputTypeDef",
    "CreatePolicyTemplateInputRequestTypeDef",
    "CreatePolicyTemplateOutputTypeDef",
    "DeleteIdentitySourceInputRequestTypeDef",
    "DeletePolicyInputRequestTypeDef",
    "DeletePolicyStoreInputRequestTypeDef",
    "DeletePolicyTemplateInputRequestTypeDef",
    "DeterminingPolicyItemTypeDef",
    "EntitiesDefinitionTypeDef",
    "EntityIdentifierTypeDef",
    "EntityItemTypeDef",
    "EntityReferenceTypeDef",
    "EvaluationErrorItemTypeDef",
    "GetIdentitySourceInputRequestTypeDef",
    "GetIdentitySourceOutputTypeDef",
    "GetPolicyInputRequestTypeDef",
    "GetPolicyOutputTypeDef",
    "GetPolicyStoreInputRequestTypeDef",
    "GetPolicyStoreOutputTypeDef",
    "GetPolicyTemplateInputRequestTypeDef",
    "GetPolicyTemplateOutputTypeDef",
    "GetSchemaInputRequestTypeDef",
    "GetSchemaOutputTypeDef",
    "IdentitySourceDetailsTypeDef",
    "IdentitySourceFilterTypeDef",
    "IdentitySourceItemDetailsTypeDef",
    "IdentitySourceItemTypeDef",
    "IsAuthorizedInputRequestTypeDef",
    "IsAuthorizedOutputTypeDef",
    "IsAuthorizedWithTokenInputRequestTypeDef",
    "IsAuthorizedWithTokenOutputTypeDef",
    "ListIdentitySourcesInputRequestTypeDef",
    "ListIdentitySourcesOutputTypeDef",
    "ListPoliciesInputRequestTypeDef",
    "ListPoliciesOutputTypeDef",
    "ListPolicyStoresInputRequestTypeDef",
    "ListPolicyStoresOutputTypeDef",
    "ListPolicyTemplatesInputRequestTypeDef",
    "ListPolicyTemplatesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDefinitionDetailTypeDef",
    "PolicyDefinitionItemTypeDef",
    "PolicyDefinitionTypeDef",
    "PolicyFilterTypeDef",
    "PolicyItemTypeDef",
    "PolicyStoreItemTypeDef",
    "PolicyTemplateItemTypeDef",
    "PutSchemaInputRequestTypeDef",
    "PutSchemaOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaDefinitionTypeDef",
    "StaticPolicyDefinitionDetailTypeDef",
    "StaticPolicyDefinitionItemTypeDef",
    "StaticPolicyDefinitionTypeDef",
    "TemplateLinkedPolicyDefinitionDetailTypeDef",
    "TemplateLinkedPolicyDefinitionItemTypeDef",
    "TemplateLinkedPolicyDefinitionTypeDef",
    "UpdateCognitoGroupConfigurationTypeDef",
    "UpdateCognitoUserPoolConfigurationTypeDef",
    "UpdateConfigurationTypeDef",
    "UpdateIdentitySourceInputRequestTypeDef",
    "UpdateIdentitySourceOutputTypeDef",
    "UpdatePolicyDefinitionTypeDef",
    "UpdatePolicyInputRequestTypeDef",
    "UpdatePolicyOutputTypeDef",
    "UpdatePolicyStoreInputRequestTypeDef",
    "UpdatePolicyStoreOutputTypeDef",
    "UpdatePolicyTemplateInputRequestTypeDef",
    "UpdatePolicyTemplateOutputTypeDef",
    "UpdateStaticPolicyDefinitionTypeDef",
    "ValidationSettingsTypeDef",
)

ActionIdentifierTypeDef = TypedDict(
    "ActionIdentifierTypeDef",
    {
        "actionType": str,
        "actionId": str,
    },
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "boolean": bool,
        "entityIdentifier": "EntityIdentifierTypeDef",
        "long": int,
        "string": str,
        "set": List[Dict[str, Any]],
        "record": Dict[str, Dict[str, Any]],
    },
    total=False,
)

BatchIsAuthorizedInputItemTypeDef = TypedDict(
    "BatchIsAuthorizedInputItemTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "action": "ActionIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "context": "ContextDefinitionTypeDef",
    },
    total=False,
)

_RequiredBatchIsAuthorizedInputRequestTypeDef = TypedDict(
    "_RequiredBatchIsAuthorizedInputRequestTypeDef",
    {
        "policyStoreId": str,
        "requests": List["BatchIsAuthorizedInputItemTypeDef"],
    },
)
_OptionalBatchIsAuthorizedInputRequestTypeDef = TypedDict(
    "_OptionalBatchIsAuthorizedInputRequestTypeDef",
    {
        "entities": "EntitiesDefinitionTypeDef",
    },
    total=False,
)

class BatchIsAuthorizedInputRequestTypeDef(
    _RequiredBatchIsAuthorizedInputRequestTypeDef, _OptionalBatchIsAuthorizedInputRequestTypeDef
):
    pass

BatchIsAuthorizedOutputItemTypeDef = TypedDict(
    "BatchIsAuthorizedOutputItemTypeDef",
    {
        "request": "BatchIsAuthorizedInputItemTypeDef",
        "decision": DecisionType,
        "determiningPolicies": List["DeterminingPolicyItemTypeDef"],
        "errors": List["EvaluationErrorItemTypeDef"],
    },
)

BatchIsAuthorizedOutputTypeDef = TypedDict(
    "BatchIsAuthorizedOutputTypeDef",
    {
        "results": List["BatchIsAuthorizedOutputItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchIsAuthorizedWithTokenInputItemTypeDef = TypedDict(
    "BatchIsAuthorizedWithTokenInputItemTypeDef",
    {
        "action": "ActionIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "context": "ContextDefinitionTypeDef",
    },
    total=False,
)

_RequiredBatchIsAuthorizedWithTokenInputRequestTypeDef = TypedDict(
    "_RequiredBatchIsAuthorizedWithTokenInputRequestTypeDef",
    {
        "policyStoreId": str,
        "requests": List["BatchIsAuthorizedWithTokenInputItemTypeDef"],
    },
)
_OptionalBatchIsAuthorizedWithTokenInputRequestTypeDef = TypedDict(
    "_OptionalBatchIsAuthorizedWithTokenInputRequestTypeDef",
    {
        "identityToken": str,
        "accessToken": str,
        "entities": "EntitiesDefinitionTypeDef",
    },
    total=False,
)

class BatchIsAuthorizedWithTokenInputRequestTypeDef(
    _RequiredBatchIsAuthorizedWithTokenInputRequestTypeDef,
    _OptionalBatchIsAuthorizedWithTokenInputRequestTypeDef,
):
    pass

BatchIsAuthorizedWithTokenOutputItemTypeDef = TypedDict(
    "BatchIsAuthorizedWithTokenOutputItemTypeDef",
    {
        "request": "BatchIsAuthorizedWithTokenInputItemTypeDef",
        "decision": DecisionType,
        "determiningPolicies": List["DeterminingPolicyItemTypeDef"],
        "errors": List["EvaluationErrorItemTypeDef"],
    },
)

BatchIsAuthorizedWithTokenOutputTypeDef = TypedDict(
    "BatchIsAuthorizedWithTokenOutputTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "results": List["BatchIsAuthorizedWithTokenOutputItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CognitoGroupConfigurationDetailTypeDef = TypedDict(
    "CognitoGroupConfigurationDetailTypeDef",
    {
        "groupEntityType": str,
    },
    total=False,
)

CognitoGroupConfigurationItemTypeDef = TypedDict(
    "CognitoGroupConfigurationItemTypeDef",
    {
        "groupEntityType": str,
    },
    total=False,
)

CognitoGroupConfigurationTypeDef = TypedDict(
    "CognitoGroupConfigurationTypeDef",
    {
        "groupEntityType": str,
    },
)

_RequiredCognitoUserPoolConfigurationDetailTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigurationDetailTypeDef",
    {
        "userPoolArn": str,
        "clientIds": List[str],
        "issuer": str,
    },
)
_OptionalCognitoUserPoolConfigurationDetailTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigurationDetailTypeDef",
    {
        "groupConfiguration": "CognitoGroupConfigurationDetailTypeDef",
    },
    total=False,
)

class CognitoUserPoolConfigurationDetailTypeDef(
    _RequiredCognitoUserPoolConfigurationDetailTypeDef,
    _OptionalCognitoUserPoolConfigurationDetailTypeDef,
):
    pass

_RequiredCognitoUserPoolConfigurationItemTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigurationItemTypeDef",
    {
        "userPoolArn": str,
        "clientIds": List[str],
        "issuer": str,
    },
)
_OptionalCognitoUserPoolConfigurationItemTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigurationItemTypeDef",
    {
        "groupConfiguration": "CognitoGroupConfigurationItemTypeDef",
    },
    total=False,
)

class CognitoUserPoolConfigurationItemTypeDef(
    _RequiredCognitoUserPoolConfigurationItemTypeDef,
    _OptionalCognitoUserPoolConfigurationItemTypeDef,
):
    pass

_RequiredCognitoUserPoolConfigurationTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigurationTypeDef",
    {
        "userPoolArn": str,
    },
)
_OptionalCognitoUserPoolConfigurationTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigurationTypeDef",
    {
        "clientIds": List[str],
        "groupConfiguration": "CognitoGroupConfigurationTypeDef",
    },
    total=False,
)

class CognitoUserPoolConfigurationTypeDef(
    _RequiredCognitoUserPoolConfigurationTypeDef, _OptionalCognitoUserPoolConfigurationTypeDef
):
    pass

ConfigurationDetailTypeDef = TypedDict(
    "ConfigurationDetailTypeDef",
    {
        "cognitoUserPoolConfiguration": "CognitoUserPoolConfigurationDetailTypeDef",
    },
    total=False,
)

ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "cognitoUserPoolConfiguration": "CognitoUserPoolConfigurationItemTypeDef",
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "cognitoUserPoolConfiguration": "CognitoUserPoolConfigurationTypeDef",
    },
    total=False,
)

ContextDefinitionTypeDef = TypedDict(
    "ContextDefinitionTypeDef",
    {
        "contextMap": Dict[str, "AttributeValueTypeDef"],
    },
    total=False,
)

_RequiredCreateIdentitySourceInputRequestTypeDef = TypedDict(
    "_RequiredCreateIdentitySourceInputRequestTypeDef",
    {
        "policyStoreId": str,
        "configuration": "ConfigurationTypeDef",
    },
)
_OptionalCreateIdentitySourceInputRequestTypeDef = TypedDict(
    "_OptionalCreateIdentitySourceInputRequestTypeDef",
    {
        "clientToken": str,
        "principalEntityType": str,
    },
    total=False,
)

class CreateIdentitySourceInputRequestTypeDef(
    _RequiredCreateIdentitySourceInputRequestTypeDef,
    _OptionalCreateIdentitySourceInputRequestTypeDef,
):
    pass

CreateIdentitySourceOutputTypeDef = TypedDict(
    "CreateIdentitySourceOutputTypeDef",
    {
        "createdDate": datetime,
        "identitySourceId": str,
        "lastUpdatedDate": datetime,
        "policyStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyInputRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyInputRequestTypeDef",
    {
        "policyStoreId": str,
        "definition": "PolicyDefinitionTypeDef",
    },
)
_OptionalCreatePolicyInputRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreatePolicyInputRequestTypeDef(
    _RequiredCreatePolicyInputRequestTypeDef, _OptionalCreatePolicyInputRequestTypeDef
):
    pass

CreatePolicyOutputTypeDef = TypedDict(
    "CreatePolicyOutputTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
        "policyType": PolicyTypeType,
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "actions": List["ActionIdentifierTypeDef"],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "effect": PolicyEffectType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyStoreInputRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyStoreInputRequestTypeDef",
    {
        "validationSettings": "ValidationSettingsTypeDef",
    },
)
_OptionalCreatePolicyStoreInputRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyStoreInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreatePolicyStoreInputRequestTypeDef(
    _RequiredCreatePolicyStoreInputRequestTypeDef, _OptionalCreatePolicyStoreInputRequestTypeDef
):
    pass

CreatePolicyStoreOutputTypeDef = TypedDict(
    "CreatePolicyStoreOutputTypeDef",
    {
        "policyStoreId": str,
        "arn": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyTemplateInputRequestTypeDef",
    {
        "policyStoreId": str,
        "statement": str,
    },
)
_OptionalCreatePolicyTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyTemplateInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreatePolicyTemplateInputRequestTypeDef(
    _RequiredCreatePolicyTemplateInputRequestTypeDef,
    _OptionalCreatePolicyTemplateInputRequestTypeDef,
):
    pass

CreatePolicyTemplateOutputTypeDef = TypedDict(
    "CreatePolicyTemplateOutputTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIdentitySourceInputRequestTypeDef = TypedDict(
    "DeleteIdentitySourceInputRequestTypeDef",
    {
        "policyStoreId": str,
        "identitySourceId": str,
    },
)

DeletePolicyInputRequestTypeDef = TypedDict(
    "DeletePolicyInputRequestTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
    },
)

DeletePolicyStoreInputRequestTypeDef = TypedDict(
    "DeletePolicyStoreInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)

DeletePolicyTemplateInputRequestTypeDef = TypedDict(
    "DeletePolicyTemplateInputRequestTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
    },
)

DeterminingPolicyItemTypeDef = TypedDict(
    "DeterminingPolicyItemTypeDef",
    {
        "policyId": str,
    },
)

EntitiesDefinitionTypeDef = TypedDict(
    "EntitiesDefinitionTypeDef",
    {
        "entityList": List["EntityItemTypeDef"],
    },
    total=False,
)

EntityIdentifierTypeDef = TypedDict(
    "EntityIdentifierTypeDef",
    {
        "entityType": str,
        "entityId": str,
    },
)

_RequiredEntityItemTypeDef = TypedDict(
    "_RequiredEntityItemTypeDef",
    {
        "identifier": "EntityIdentifierTypeDef",
    },
)
_OptionalEntityItemTypeDef = TypedDict(
    "_OptionalEntityItemTypeDef",
    {
        "attributes": Dict[str, "AttributeValueTypeDef"],
        "parents": List["EntityIdentifierTypeDef"],
    },
    total=False,
)

class EntityItemTypeDef(_RequiredEntityItemTypeDef, _OptionalEntityItemTypeDef):
    pass

EntityReferenceTypeDef = TypedDict(
    "EntityReferenceTypeDef",
    {
        "unspecified": bool,
        "identifier": "EntityIdentifierTypeDef",
    },
    total=False,
)

EvaluationErrorItemTypeDef = TypedDict(
    "EvaluationErrorItemTypeDef",
    {
        "errorDescription": str,
    },
)

GetIdentitySourceInputRequestTypeDef = TypedDict(
    "GetIdentitySourceInputRequestTypeDef",
    {
        "policyStoreId": str,
        "identitySourceId": str,
    },
)

GetIdentitySourceOutputTypeDef = TypedDict(
    "GetIdentitySourceOutputTypeDef",
    {
        "createdDate": datetime,
        "details": "IdentitySourceDetailsTypeDef",
        "identitySourceId": str,
        "lastUpdatedDate": datetime,
        "policyStoreId": str,
        "principalEntityType": str,
        "configuration": "ConfigurationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyInputRequestTypeDef = TypedDict(
    "GetPolicyInputRequestTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
    },
)

GetPolicyOutputTypeDef = TypedDict(
    "GetPolicyOutputTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
        "policyType": PolicyTypeType,
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "actions": List["ActionIdentifierTypeDef"],
        "definition": "PolicyDefinitionDetailTypeDef",
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "effect": PolicyEffectType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyStoreInputRequestTypeDef = TypedDict(
    "GetPolicyStoreInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)

GetPolicyStoreOutputTypeDef = TypedDict(
    "GetPolicyStoreOutputTypeDef",
    {
        "policyStoreId": str,
        "arn": str,
        "validationSettings": "ValidationSettingsTypeDef",
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyTemplateInputRequestTypeDef = TypedDict(
    "GetPolicyTemplateInputRequestTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
    },
)

GetPolicyTemplateOutputTypeDef = TypedDict(
    "GetPolicyTemplateOutputTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
        "description": str,
        "statement": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaInputRequestTypeDef = TypedDict(
    "GetSchemaInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)

GetSchemaOutputTypeDef = TypedDict(
    "GetSchemaOutputTypeDef",
    {
        "policyStoreId": str,
        "schema": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "namespaces": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentitySourceDetailsTypeDef = TypedDict(
    "IdentitySourceDetailsTypeDef",
    {
        "clientIds": List[str],
        "userPoolArn": str,
        "discoveryUrl": str,
        "openIdIssuer": Literal["COGNITO"],
    },
    total=False,
)

IdentitySourceFilterTypeDef = TypedDict(
    "IdentitySourceFilterTypeDef",
    {
        "principalEntityType": str,
    },
    total=False,
)

IdentitySourceItemDetailsTypeDef = TypedDict(
    "IdentitySourceItemDetailsTypeDef",
    {
        "clientIds": List[str],
        "userPoolArn": str,
        "discoveryUrl": str,
        "openIdIssuer": Literal["COGNITO"],
    },
    total=False,
)

_RequiredIdentitySourceItemTypeDef = TypedDict(
    "_RequiredIdentitySourceItemTypeDef",
    {
        "createdDate": datetime,
        "identitySourceId": str,
        "lastUpdatedDate": datetime,
        "policyStoreId": str,
        "principalEntityType": str,
    },
)
_OptionalIdentitySourceItemTypeDef = TypedDict(
    "_OptionalIdentitySourceItemTypeDef",
    {
        "details": "IdentitySourceItemDetailsTypeDef",
        "configuration": "ConfigurationItemTypeDef",
    },
    total=False,
)

class IdentitySourceItemTypeDef(
    _RequiredIdentitySourceItemTypeDef, _OptionalIdentitySourceItemTypeDef
):
    pass

_RequiredIsAuthorizedInputRequestTypeDef = TypedDict(
    "_RequiredIsAuthorizedInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)
_OptionalIsAuthorizedInputRequestTypeDef = TypedDict(
    "_OptionalIsAuthorizedInputRequestTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "action": "ActionIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "context": "ContextDefinitionTypeDef",
        "entities": "EntitiesDefinitionTypeDef",
    },
    total=False,
)

class IsAuthorizedInputRequestTypeDef(
    _RequiredIsAuthorizedInputRequestTypeDef, _OptionalIsAuthorizedInputRequestTypeDef
):
    pass

IsAuthorizedOutputTypeDef = TypedDict(
    "IsAuthorizedOutputTypeDef",
    {
        "decision": DecisionType,
        "determiningPolicies": List["DeterminingPolicyItemTypeDef"],
        "errors": List["EvaluationErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIsAuthorizedWithTokenInputRequestTypeDef = TypedDict(
    "_RequiredIsAuthorizedWithTokenInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)
_OptionalIsAuthorizedWithTokenInputRequestTypeDef = TypedDict(
    "_OptionalIsAuthorizedWithTokenInputRequestTypeDef",
    {
        "identityToken": str,
        "accessToken": str,
        "action": "ActionIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "context": "ContextDefinitionTypeDef",
        "entities": "EntitiesDefinitionTypeDef",
    },
    total=False,
)

class IsAuthorizedWithTokenInputRequestTypeDef(
    _RequiredIsAuthorizedWithTokenInputRequestTypeDef,
    _OptionalIsAuthorizedWithTokenInputRequestTypeDef,
):
    pass

IsAuthorizedWithTokenOutputTypeDef = TypedDict(
    "IsAuthorizedWithTokenOutputTypeDef",
    {
        "decision": DecisionType,
        "determiningPolicies": List["DeterminingPolicyItemTypeDef"],
        "errors": List["EvaluationErrorItemTypeDef"],
        "principal": "EntityIdentifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentitySourcesInputRequestTypeDef = TypedDict(
    "_RequiredListIdentitySourcesInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)
_OptionalListIdentitySourcesInputRequestTypeDef = TypedDict(
    "_OptionalListIdentitySourcesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["IdentitySourceFilterTypeDef"],
    },
    total=False,
)

class ListIdentitySourcesInputRequestTypeDef(
    _RequiredListIdentitySourcesInputRequestTypeDef, _OptionalListIdentitySourcesInputRequestTypeDef
):
    pass

ListIdentitySourcesOutputTypeDef = TypedDict(
    "ListIdentitySourcesOutputTypeDef",
    {
        "nextToken": str,
        "identitySources": List["IdentitySourceItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPoliciesInputRequestTypeDef = TypedDict(
    "_RequiredListPoliciesInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)
_OptionalListPoliciesInputRequestTypeDef = TypedDict(
    "_OptionalListPoliciesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filter": "PolicyFilterTypeDef",
    },
    total=False,
)

class ListPoliciesInputRequestTypeDef(
    _RequiredListPoliciesInputRequestTypeDef, _OptionalListPoliciesInputRequestTypeDef
):
    pass

ListPoliciesOutputTypeDef = TypedDict(
    "ListPoliciesOutputTypeDef",
    {
        "nextToken": str,
        "policies": List["PolicyItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyStoresInputRequestTypeDef = TypedDict(
    "ListPolicyStoresInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPolicyStoresOutputTypeDef = TypedDict(
    "ListPolicyStoresOutputTypeDef",
    {
        "nextToken": str,
        "policyStores": List["PolicyStoreItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyTemplatesInputRequestTypeDef = TypedDict(
    "_RequiredListPolicyTemplatesInputRequestTypeDef",
    {
        "policyStoreId": str,
    },
)
_OptionalListPolicyTemplatesInputRequestTypeDef = TypedDict(
    "_OptionalListPolicyTemplatesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPolicyTemplatesInputRequestTypeDef(
    _RequiredListPolicyTemplatesInputRequestTypeDef, _OptionalListPolicyTemplatesInputRequestTypeDef
):
    pass

ListPolicyTemplatesOutputTypeDef = TypedDict(
    "ListPolicyTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "policyTemplates": List["PolicyTemplateItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PolicyDefinitionDetailTypeDef = TypedDict(
    "PolicyDefinitionDetailTypeDef",
    {
        "static": "StaticPolicyDefinitionDetailTypeDef",
        "templateLinked": "TemplateLinkedPolicyDefinitionDetailTypeDef",
    },
    total=False,
)

PolicyDefinitionItemTypeDef = TypedDict(
    "PolicyDefinitionItemTypeDef",
    {
        "static": "StaticPolicyDefinitionItemTypeDef",
        "templateLinked": "TemplateLinkedPolicyDefinitionItemTypeDef",
    },
    total=False,
)

PolicyDefinitionTypeDef = TypedDict(
    "PolicyDefinitionTypeDef",
    {
        "static": "StaticPolicyDefinitionTypeDef",
        "templateLinked": "TemplateLinkedPolicyDefinitionTypeDef",
    },
    total=False,
)

PolicyFilterTypeDef = TypedDict(
    "PolicyFilterTypeDef",
    {
        "principal": "EntityReferenceTypeDef",
        "resource": "EntityReferenceTypeDef",
        "policyType": PolicyTypeType,
        "policyTemplateId": str,
    },
    total=False,
)

_RequiredPolicyItemTypeDef = TypedDict(
    "_RequiredPolicyItemTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
        "policyType": PolicyTypeType,
        "definition": "PolicyDefinitionItemTypeDef",
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
)
_OptionalPolicyItemTypeDef = TypedDict(
    "_OptionalPolicyItemTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "actions": List["ActionIdentifierTypeDef"],
        "effect": PolicyEffectType,
    },
    total=False,
)

class PolicyItemTypeDef(_RequiredPolicyItemTypeDef, _OptionalPolicyItemTypeDef):
    pass

_RequiredPolicyStoreItemTypeDef = TypedDict(
    "_RequiredPolicyStoreItemTypeDef",
    {
        "policyStoreId": str,
        "arn": str,
        "createdDate": datetime,
    },
)
_OptionalPolicyStoreItemTypeDef = TypedDict(
    "_OptionalPolicyStoreItemTypeDef",
    {
        "lastUpdatedDate": datetime,
        "description": str,
    },
    total=False,
)

class PolicyStoreItemTypeDef(_RequiredPolicyStoreItemTypeDef, _OptionalPolicyStoreItemTypeDef):
    pass

_RequiredPolicyTemplateItemTypeDef = TypedDict(
    "_RequiredPolicyTemplateItemTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
)
_OptionalPolicyTemplateItemTypeDef = TypedDict(
    "_OptionalPolicyTemplateItemTypeDef",
    {
        "description": str,
    },
    total=False,
)

class PolicyTemplateItemTypeDef(
    _RequiredPolicyTemplateItemTypeDef, _OptionalPolicyTemplateItemTypeDef
):
    pass

PutSchemaInputRequestTypeDef = TypedDict(
    "PutSchemaInputRequestTypeDef",
    {
        "policyStoreId": str,
        "definition": "SchemaDefinitionTypeDef",
    },
)

PutSchemaOutputTypeDef = TypedDict(
    "PutSchemaOutputTypeDef",
    {
        "policyStoreId": str,
        "namespaces": List[str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
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

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "cedarJson": str,
    },
    total=False,
)

_RequiredStaticPolicyDefinitionDetailTypeDef = TypedDict(
    "_RequiredStaticPolicyDefinitionDetailTypeDef",
    {
        "statement": str,
    },
)
_OptionalStaticPolicyDefinitionDetailTypeDef = TypedDict(
    "_OptionalStaticPolicyDefinitionDetailTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StaticPolicyDefinitionDetailTypeDef(
    _RequiredStaticPolicyDefinitionDetailTypeDef, _OptionalStaticPolicyDefinitionDetailTypeDef
):
    pass

StaticPolicyDefinitionItemTypeDef = TypedDict(
    "StaticPolicyDefinitionItemTypeDef",
    {
        "description": str,
    },
    total=False,
)

_RequiredStaticPolicyDefinitionTypeDef = TypedDict(
    "_RequiredStaticPolicyDefinitionTypeDef",
    {
        "statement": str,
    },
)
_OptionalStaticPolicyDefinitionTypeDef = TypedDict(
    "_OptionalStaticPolicyDefinitionTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StaticPolicyDefinitionTypeDef(
    _RequiredStaticPolicyDefinitionTypeDef, _OptionalStaticPolicyDefinitionTypeDef
):
    pass

_RequiredTemplateLinkedPolicyDefinitionDetailTypeDef = TypedDict(
    "_RequiredTemplateLinkedPolicyDefinitionDetailTypeDef",
    {
        "policyTemplateId": str,
    },
)
_OptionalTemplateLinkedPolicyDefinitionDetailTypeDef = TypedDict(
    "_OptionalTemplateLinkedPolicyDefinitionDetailTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
    },
    total=False,
)

class TemplateLinkedPolicyDefinitionDetailTypeDef(
    _RequiredTemplateLinkedPolicyDefinitionDetailTypeDef,
    _OptionalTemplateLinkedPolicyDefinitionDetailTypeDef,
):
    pass

_RequiredTemplateLinkedPolicyDefinitionItemTypeDef = TypedDict(
    "_RequiredTemplateLinkedPolicyDefinitionItemTypeDef",
    {
        "policyTemplateId": str,
    },
)
_OptionalTemplateLinkedPolicyDefinitionItemTypeDef = TypedDict(
    "_OptionalTemplateLinkedPolicyDefinitionItemTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
    },
    total=False,
)

class TemplateLinkedPolicyDefinitionItemTypeDef(
    _RequiredTemplateLinkedPolicyDefinitionItemTypeDef,
    _OptionalTemplateLinkedPolicyDefinitionItemTypeDef,
):
    pass

_RequiredTemplateLinkedPolicyDefinitionTypeDef = TypedDict(
    "_RequiredTemplateLinkedPolicyDefinitionTypeDef",
    {
        "policyTemplateId": str,
    },
)
_OptionalTemplateLinkedPolicyDefinitionTypeDef = TypedDict(
    "_OptionalTemplateLinkedPolicyDefinitionTypeDef",
    {
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
    },
    total=False,
)

class TemplateLinkedPolicyDefinitionTypeDef(
    _RequiredTemplateLinkedPolicyDefinitionTypeDef, _OptionalTemplateLinkedPolicyDefinitionTypeDef
):
    pass

UpdateCognitoGroupConfigurationTypeDef = TypedDict(
    "UpdateCognitoGroupConfigurationTypeDef",
    {
        "groupEntityType": str,
    },
)

_RequiredUpdateCognitoUserPoolConfigurationTypeDef = TypedDict(
    "_RequiredUpdateCognitoUserPoolConfigurationTypeDef",
    {
        "userPoolArn": str,
    },
)
_OptionalUpdateCognitoUserPoolConfigurationTypeDef = TypedDict(
    "_OptionalUpdateCognitoUserPoolConfigurationTypeDef",
    {
        "clientIds": List[str],
        "groupConfiguration": "UpdateCognitoGroupConfigurationTypeDef",
    },
    total=False,
)

class UpdateCognitoUserPoolConfigurationTypeDef(
    _RequiredUpdateCognitoUserPoolConfigurationTypeDef,
    _OptionalUpdateCognitoUserPoolConfigurationTypeDef,
):
    pass

UpdateConfigurationTypeDef = TypedDict(
    "UpdateConfigurationTypeDef",
    {
        "cognitoUserPoolConfiguration": "UpdateCognitoUserPoolConfigurationTypeDef",
    },
    total=False,
)

_RequiredUpdateIdentitySourceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentitySourceInputRequestTypeDef",
    {
        "policyStoreId": str,
        "identitySourceId": str,
        "updateConfiguration": "UpdateConfigurationTypeDef",
    },
)
_OptionalUpdateIdentitySourceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentitySourceInputRequestTypeDef",
    {
        "principalEntityType": str,
    },
    total=False,
)

class UpdateIdentitySourceInputRequestTypeDef(
    _RequiredUpdateIdentitySourceInputRequestTypeDef,
    _OptionalUpdateIdentitySourceInputRequestTypeDef,
):
    pass

UpdateIdentitySourceOutputTypeDef = TypedDict(
    "UpdateIdentitySourceOutputTypeDef",
    {
        "createdDate": datetime,
        "identitySourceId": str,
        "lastUpdatedDate": datetime,
        "policyStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePolicyDefinitionTypeDef = TypedDict(
    "UpdatePolicyDefinitionTypeDef",
    {
        "static": "UpdateStaticPolicyDefinitionTypeDef",
    },
    total=False,
)

UpdatePolicyInputRequestTypeDef = TypedDict(
    "UpdatePolicyInputRequestTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
        "definition": "UpdatePolicyDefinitionTypeDef",
    },
)

UpdatePolicyOutputTypeDef = TypedDict(
    "UpdatePolicyOutputTypeDef",
    {
        "policyStoreId": str,
        "policyId": str,
        "policyType": PolicyTypeType,
        "principal": "EntityIdentifierTypeDef",
        "resource": "EntityIdentifierTypeDef",
        "actions": List["ActionIdentifierTypeDef"],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "effect": PolicyEffectType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePolicyStoreInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePolicyStoreInputRequestTypeDef",
    {
        "policyStoreId": str,
        "validationSettings": "ValidationSettingsTypeDef",
    },
)
_OptionalUpdatePolicyStoreInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePolicyStoreInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdatePolicyStoreInputRequestTypeDef(
    _RequiredUpdatePolicyStoreInputRequestTypeDef, _OptionalUpdatePolicyStoreInputRequestTypeDef
):
    pass

UpdatePolicyStoreOutputTypeDef = TypedDict(
    "UpdatePolicyStoreOutputTypeDef",
    {
        "policyStoreId": str,
        "arn": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePolicyTemplateInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePolicyTemplateInputRequestTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
        "statement": str,
    },
)
_OptionalUpdatePolicyTemplateInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePolicyTemplateInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdatePolicyTemplateInputRequestTypeDef(
    _RequiredUpdatePolicyTemplateInputRequestTypeDef,
    _OptionalUpdatePolicyTemplateInputRequestTypeDef,
):
    pass

UpdatePolicyTemplateOutputTypeDef = TypedDict(
    "UpdatePolicyTemplateOutputTypeDef",
    {
        "policyStoreId": str,
        "policyTemplateId": str,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStaticPolicyDefinitionTypeDef = TypedDict(
    "_RequiredUpdateStaticPolicyDefinitionTypeDef",
    {
        "statement": str,
    },
)
_OptionalUpdateStaticPolicyDefinitionTypeDef = TypedDict(
    "_OptionalUpdateStaticPolicyDefinitionTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateStaticPolicyDefinitionTypeDef(
    _RequiredUpdateStaticPolicyDefinitionTypeDef, _OptionalUpdateStaticPolicyDefinitionTypeDef
):
    pass

ValidationSettingsTypeDef = TypedDict(
    "ValidationSettingsTypeDef",
    {
        "mode": ValidationModeType,
    },
)
