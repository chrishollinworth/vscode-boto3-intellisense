"""
Type annotations for cleanrooms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cleanrooms.type_defs import AggregateColumnTypeDef

    data: AggregateColumnTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AggregateFunctionNameType,
    AnalysisRuleTypeType,
    AnalysisTemplateValidationStatusType,
    CollaborationQueryLogStatusType,
    ConfiguredTableAnalysisRuleTypeType,
    DifferentialPrivacyAggregationTypeType,
    FilterableMemberStatusType,
    JoinOperatorType,
    MemberAbilityType,
    MembershipQueryLogStatusType,
    MembershipStatusType,
    MemberStatusType,
    ParameterTypeType,
    PrivacyBudgetTemplateAutoRefreshType,
    ProtectedQueryStatusType,
    ResultFormatType,
    ScalarFunctionsType,
    SchemaStatusReasonCodeType,
    SchemaStatusType,
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
    "AggregateColumnTypeDef",
    "AggregationConstraintTypeDef",
    "AnalysisParameterTypeDef",
    "AnalysisRuleAggregationTypeDef",
    "AnalysisRuleCustomTypeDef",
    "AnalysisRuleListTypeDef",
    "AnalysisRulePolicyTypeDef",
    "AnalysisRulePolicyV1TypeDef",
    "AnalysisRuleTypeDef",
    "AnalysisSchemaTypeDef",
    "AnalysisSourceTypeDef",
    "AnalysisTemplateSummaryTypeDef",
    "AnalysisTemplateTypeDef",
    "AnalysisTemplateValidationStatusDetailTypeDef",
    "AnalysisTemplateValidationStatusReasonTypeDef",
    "BatchGetCollaborationAnalysisTemplateErrorTypeDef",
    "BatchGetCollaborationAnalysisTemplateInputRequestTypeDef",
    "BatchGetCollaborationAnalysisTemplateOutputTypeDef",
    "BatchGetSchemaAnalysisRuleErrorTypeDef",
    "BatchGetSchemaAnalysisRuleInputRequestTypeDef",
    "BatchGetSchemaAnalysisRuleOutputTypeDef",
    "BatchGetSchemaErrorTypeDef",
    "BatchGetSchemaInputRequestTypeDef",
    "BatchGetSchemaOutputTypeDef",
    "CollaborationAnalysisTemplateSummaryTypeDef",
    "CollaborationAnalysisTemplateTypeDef",
    "CollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    "CollaborationConfiguredAudienceModelAssociationTypeDef",
    "CollaborationPrivacyBudgetSummaryTypeDef",
    "CollaborationPrivacyBudgetTemplateSummaryTypeDef",
    "CollaborationPrivacyBudgetTemplateTypeDef",
    "CollaborationSummaryTypeDef",
    "CollaborationTypeDef",
    "ColumnTypeDef",
    "ConfiguredAudienceModelAssociationSummaryTypeDef",
    "ConfiguredAudienceModelAssociationTypeDef",
    "ConfiguredTableAnalysisRulePolicyTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    "ConfiguredTableAnalysisRuleTypeDef",
    "ConfiguredTableAssociationSummaryTypeDef",
    "ConfiguredTableAssociationTypeDef",
    "ConfiguredTableSummaryTypeDef",
    "ConfiguredTableTypeDef",
    "CreateAnalysisTemplateInputRequestTypeDef",
    "CreateAnalysisTemplateOutputTypeDef",
    "CreateCollaborationInputRequestTypeDef",
    "CreateCollaborationOutputTypeDef",
    "CreateConfiguredAudienceModelAssociationInputRequestTypeDef",
    "CreateConfiguredAudienceModelAssociationOutputTypeDef",
    "CreateConfiguredTableAnalysisRuleInputRequestTypeDef",
    "CreateConfiguredTableAnalysisRuleOutputTypeDef",
    "CreateConfiguredTableAssociationInputRequestTypeDef",
    "CreateConfiguredTableAssociationOutputTypeDef",
    "CreateConfiguredTableInputRequestTypeDef",
    "CreateConfiguredTableOutputTypeDef",
    "CreateMembershipInputRequestTypeDef",
    "CreateMembershipOutputTypeDef",
    "CreatePrivacyBudgetTemplateInputRequestTypeDef",
    "CreatePrivacyBudgetTemplateOutputTypeDef",
    "DataEncryptionMetadataTypeDef",
    "DeleteAnalysisTemplateInputRequestTypeDef",
    "DeleteCollaborationInputRequestTypeDef",
    "DeleteConfiguredAudienceModelAssociationInputRequestTypeDef",
    "DeleteConfiguredTableAnalysisRuleInputRequestTypeDef",
    "DeleteConfiguredTableAssociationInputRequestTypeDef",
    "DeleteConfiguredTableInputRequestTypeDef",
    "DeleteMemberInputRequestTypeDef",
    "DeleteMembershipInputRequestTypeDef",
    "DeletePrivacyBudgetTemplateInputRequestTypeDef",
    "DifferentialPrivacyColumnTypeDef",
    "DifferentialPrivacyConfigurationTypeDef",
    "DifferentialPrivacyParametersTypeDef",
    "DifferentialPrivacyPreviewAggregationTypeDef",
    "DifferentialPrivacyPreviewParametersInputTypeDef",
    "DifferentialPrivacyPrivacyBudgetAggregationTypeDef",
    "DifferentialPrivacyPrivacyBudgetTypeDef",
    "DifferentialPrivacyPrivacyImpactTypeDef",
    "DifferentialPrivacySensitivityParametersTypeDef",
    "DifferentialPrivacyTemplateParametersInputTypeDef",
    "DifferentialPrivacyTemplateParametersOutputTypeDef",
    "DifferentialPrivacyTemplateUpdateParametersTypeDef",
    "GetAnalysisTemplateInputRequestTypeDef",
    "GetAnalysisTemplateOutputTypeDef",
    "GetCollaborationAnalysisTemplateInputRequestTypeDef",
    "GetCollaborationAnalysisTemplateOutputTypeDef",
    "GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef",
    "GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef",
    "GetCollaborationInputRequestTypeDef",
    "GetCollaborationOutputTypeDef",
    "GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef",
    "GetCollaborationPrivacyBudgetTemplateOutputTypeDef",
    "GetConfiguredAudienceModelAssociationInputRequestTypeDef",
    "GetConfiguredAudienceModelAssociationOutputTypeDef",
    "GetConfiguredTableAnalysisRuleInputRequestTypeDef",
    "GetConfiguredTableAnalysisRuleOutputTypeDef",
    "GetConfiguredTableAssociationInputRequestTypeDef",
    "GetConfiguredTableAssociationOutputTypeDef",
    "GetConfiguredTableInputRequestTypeDef",
    "GetConfiguredTableOutputTypeDef",
    "GetMembershipInputRequestTypeDef",
    "GetMembershipOutputTypeDef",
    "GetPrivacyBudgetTemplateInputRequestTypeDef",
    "GetPrivacyBudgetTemplateOutputTypeDef",
    "GetProtectedQueryInputRequestTypeDef",
    "GetProtectedQueryOutputTypeDef",
    "GetSchemaAnalysisRuleInputRequestTypeDef",
    "GetSchemaAnalysisRuleOutputTypeDef",
    "GetSchemaInputRequestTypeDef",
    "GetSchemaOutputTypeDef",
    "GlueTableReferenceTypeDef",
    "ListAnalysisTemplatesInputRequestTypeDef",
    "ListAnalysisTemplatesOutputTypeDef",
    "ListCollaborationAnalysisTemplatesInputRequestTypeDef",
    "ListCollaborationAnalysisTemplatesOutputTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesOutputTypeDef",
    "ListCollaborationPrivacyBudgetsInputRequestTypeDef",
    "ListCollaborationPrivacyBudgetsOutputTypeDef",
    "ListCollaborationsInputRequestTypeDef",
    "ListCollaborationsOutputTypeDef",
    "ListConfiguredAudienceModelAssociationsInputRequestTypeDef",
    "ListConfiguredAudienceModelAssociationsOutputTypeDef",
    "ListConfiguredTableAssociationsInputRequestTypeDef",
    "ListConfiguredTableAssociationsOutputTypeDef",
    "ListConfiguredTablesInputRequestTypeDef",
    "ListConfiguredTablesOutputTypeDef",
    "ListMembersInputRequestTypeDef",
    "ListMembersOutputTypeDef",
    "ListMembershipsInputRequestTypeDef",
    "ListMembershipsOutputTypeDef",
    "ListPrivacyBudgetTemplatesInputRequestTypeDef",
    "ListPrivacyBudgetTemplatesOutputTypeDef",
    "ListPrivacyBudgetsInputRequestTypeDef",
    "ListPrivacyBudgetsOutputTypeDef",
    "ListProtectedQueriesInputRequestTypeDef",
    "ListProtectedQueriesOutputTypeDef",
    "ListSchemasInputRequestTypeDef",
    "ListSchemasOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MemberSpecificationTypeDef",
    "MemberSummaryTypeDef",
    "MembershipPaymentConfigurationTypeDef",
    "MembershipProtectedQueryOutputConfigurationTypeDef",
    "MembershipProtectedQueryResultConfigurationTypeDef",
    "MembershipQueryComputePaymentConfigTypeDef",
    "MembershipSummaryTypeDef",
    "MembershipTypeDef",
    "PaginatorConfigTypeDef",
    "PaymentConfigurationTypeDef",
    "PreviewPrivacyImpactInputRequestTypeDef",
    "PreviewPrivacyImpactOutputTypeDef",
    "PreviewPrivacyImpactParametersInputTypeDef",
    "PrivacyBudgetSummaryTypeDef",
    "PrivacyBudgetTemplateParametersInputTypeDef",
    "PrivacyBudgetTemplateParametersOutputTypeDef",
    "PrivacyBudgetTemplateSummaryTypeDef",
    "PrivacyBudgetTemplateTypeDef",
    "PrivacyBudgetTemplateUpdateParametersTypeDef",
    "PrivacyBudgetTypeDef",
    "PrivacyImpactTypeDef",
    "ProtectedQueryErrorTypeDef",
    "ProtectedQueryOutputConfigurationTypeDef",
    "ProtectedQueryOutputTypeDef",
    "ProtectedQueryResultConfigurationTypeDef",
    "ProtectedQueryResultTypeDef",
    "ProtectedQueryS3OutputConfigurationTypeDef",
    "ProtectedQueryS3OutputTypeDef",
    "ProtectedQuerySQLParametersTypeDef",
    "ProtectedQuerySingleMemberOutputTypeDef",
    "ProtectedQueryStatisticsTypeDef",
    "ProtectedQuerySummaryTypeDef",
    "ProtectedQueryTypeDef",
    "QueryComputePaymentConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaAnalysisRuleRequestTypeDef",
    "SchemaStatusDetailTypeDef",
    "SchemaStatusReasonTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaTypeDef",
    "StartProtectedQueryInputRequestTypeDef",
    "StartProtectedQueryOutputTypeDef",
    "TableReferenceTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAnalysisTemplateInputRequestTypeDef",
    "UpdateAnalysisTemplateOutputTypeDef",
    "UpdateCollaborationInputRequestTypeDef",
    "UpdateCollaborationOutputTypeDef",
    "UpdateConfiguredAudienceModelAssociationInputRequestTypeDef",
    "UpdateConfiguredAudienceModelAssociationOutputTypeDef",
    "UpdateConfiguredTableAnalysisRuleInputRequestTypeDef",
    "UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    "UpdateConfiguredTableAssociationInputRequestTypeDef",
    "UpdateConfiguredTableAssociationOutputTypeDef",
    "UpdateConfiguredTableInputRequestTypeDef",
    "UpdateConfiguredTableOutputTypeDef",
    "UpdateMembershipInputRequestTypeDef",
    "UpdateMembershipOutputTypeDef",
    "UpdatePrivacyBudgetTemplateInputRequestTypeDef",
    "UpdatePrivacyBudgetTemplateOutputTypeDef",
    "UpdateProtectedQueryInputRequestTypeDef",
    "UpdateProtectedQueryOutputTypeDef",
)

AggregateColumnTypeDef = TypedDict(
    "AggregateColumnTypeDef",
    {
        "columnNames": List[str],
        "function": AggregateFunctionNameType,
    },
)

AggregationConstraintTypeDef = TypedDict(
    "AggregationConstraintTypeDef",
    {
        "columnName": str,
        "minimum": int,
        "type": Literal["COUNT_DISTINCT"],
    },
)

_RequiredAnalysisParameterTypeDef = TypedDict(
    "_RequiredAnalysisParameterTypeDef",
    {
        "name": str,
        "type": ParameterTypeType,
    },
)
_OptionalAnalysisParameterTypeDef = TypedDict(
    "_OptionalAnalysisParameterTypeDef",
    {
        "defaultValue": str,
    },
    total=False,
)

class AnalysisParameterTypeDef(
    _RequiredAnalysisParameterTypeDef, _OptionalAnalysisParameterTypeDef
):
    pass

_RequiredAnalysisRuleAggregationTypeDef = TypedDict(
    "_RequiredAnalysisRuleAggregationTypeDef",
    {
        "aggregateColumns": List["AggregateColumnTypeDef"],
        "joinColumns": List[str],
        "dimensionColumns": List[str],
        "scalarFunctions": List[ScalarFunctionsType],
        "outputConstraints": List["AggregationConstraintTypeDef"],
    },
)
_OptionalAnalysisRuleAggregationTypeDef = TypedDict(
    "_OptionalAnalysisRuleAggregationTypeDef",
    {
        "joinRequired": Literal["QUERY_RUNNER"],
        "allowedJoinOperators": List[JoinOperatorType],
    },
    total=False,
)

class AnalysisRuleAggregationTypeDef(
    _RequiredAnalysisRuleAggregationTypeDef, _OptionalAnalysisRuleAggregationTypeDef
):
    pass

_RequiredAnalysisRuleCustomTypeDef = TypedDict(
    "_RequiredAnalysisRuleCustomTypeDef",
    {
        "allowedAnalyses": List[str],
    },
)
_OptionalAnalysisRuleCustomTypeDef = TypedDict(
    "_OptionalAnalysisRuleCustomTypeDef",
    {
        "allowedAnalysisProviders": List[str],
        "differentialPrivacy": "DifferentialPrivacyConfigurationTypeDef",
    },
    total=False,
)

class AnalysisRuleCustomTypeDef(
    _RequiredAnalysisRuleCustomTypeDef, _OptionalAnalysisRuleCustomTypeDef
):
    pass

_RequiredAnalysisRuleListTypeDef = TypedDict(
    "_RequiredAnalysisRuleListTypeDef",
    {
        "joinColumns": List[str],
        "listColumns": List[str],
    },
)
_OptionalAnalysisRuleListTypeDef = TypedDict(
    "_OptionalAnalysisRuleListTypeDef",
    {
        "allowedJoinOperators": List[JoinOperatorType],
    },
    total=False,
)

class AnalysisRuleListTypeDef(_RequiredAnalysisRuleListTypeDef, _OptionalAnalysisRuleListTypeDef):
    pass

AnalysisRulePolicyTypeDef = TypedDict(
    "AnalysisRulePolicyTypeDef",
    {
        "v1": "AnalysisRulePolicyV1TypeDef",
    },
    total=False,
)

AnalysisRulePolicyV1TypeDef = TypedDict(
    "AnalysisRulePolicyV1TypeDef",
    {
        "list": "AnalysisRuleListTypeDef",
        "aggregation": "AnalysisRuleAggregationTypeDef",
        "custom": "AnalysisRuleCustomTypeDef",
    },
    total=False,
)

AnalysisRuleTypeDef = TypedDict(
    "AnalysisRuleTypeDef",
    {
        "collaborationId": str,
        "type": AnalysisRuleTypeType,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "policy": "AnalysisRulePolicyTypeDef",
    },
)

AnalysisSchemaTypeDef = TypedDict(
    "AnalysisSchemaTypeDef",
    {
        "referencedTables": List[str],
    },
    total=False,
)

AnalysisSourceTypeDef = TypedDict(
    "AnalysisSourceTypeDef",
    {
        "text": str,
    },
    total=False,
)

_RequiredAnalysisTemplateSummaryTypeDef = TypedDict(
    "_RequiredAnalysisTemplateSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "membershipArn": str,
        "membershipId": str,
        "collaborationArn": str,
        "collaborationId": str,
    },
)
_OptionalAnalysisTemplateSummaryTypeDef = TypedDict(
    "_OptionalAnalysisTemplateSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class AnalysisTemplateSummaryTypeDef(
    _RequiredAnalysisTemplateSummaryTypeDef, _OptionalAnalysisTemplateSummaryTypeDef
):
    pass

_RequiredAnalysisTemplateTypeDef = TypedDict(
    "_RequiredAnalysisTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "membershipId": str,
        "membershipArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "schema": "AnalysisSchemaTypeDef",
        "format": Literal["SQL"],
        "source": "AnalysisSourceTypeDef",
    },
)
_OptionalAnalysisTemplateTypeDef = TypedDict(
    "_OptionalAnalysisTemplateTypeDef",
    {
        "description": str,
        "analysisParameters": List["AnalysisParameterTypeDef"],
        "validations": List["AnalysisTemplateValidationStatusDetailTypeDef"],
    },
    total=False,
)

class AnalysisTemplateTypeDef(_RequiredAnalysisTemplateTypeDef, _OptionalAnalysisTemplateTypeDef):
    pass

_RequiredAnalysisTemplateValidationStatusDetailTypeDef = TypedDict(
    "_RequiredAnalysisTemplateValidationStatusDetailTypeDef",
    {
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "status": AnalysisTemplateValidationStatusType,
    },
)
_OptionalAnalysisTemplateValidationStatusDetailTypeDef = TypedDict(
    "_OptionalAnalysisTemplateValidationStatusDetailTypeDef",
    {
        "reasons": List["AnalysisTemplateValidationStatusReasonTypeDef"],
    },
    total=False,
)

class AnalysisTemplateValidationStatusDetailTypeDef(
    _RequiredAnalysisTemplateValidationStatusDetailTypeDef,
    _OptionalAnalysisTemplateValidationStatusDetailTypeDef,
):
    pass

AnalysisTemplateValidationStatusReasonTypeDef = TypedDict(
    "AnalysisTemplateValidationStatusReasonTypeDef",
    {
        "message": str,
    },
)

BatchGetCollaborationAnalysisTemplateErrorTypeDef = TypedDict(
    "BatchGetCollaborationAnalysisTemplateErrorTypeDef",
    {
        "arn": str,
        "code": str,
        "message": str,
    },
)

BatchGetCollaborationAnalysisTemplateInputRequestTypeDef = TypedDict(
    "BatchGetCollaborationAnalysisTemplateInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "analysisTemplateArns": List[str],
    },
)

BatchGetCollaborationAnalysisTemplateOutputTypeDef = TypedDict(
    "BatchGetCollaborationAnalysisTemplateOutputTypeDef",
    {
        "collaborationAnalysisTemplates": List["CollaborationAnalysisTemplateTypeDef"],
        "errors": List["BatchGetCollaborationAnalysisTemplateErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetSchemaAnalysisRuleErrorTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleErrorTypeDef",
    {
        "name": str,
        "type": AnalysisRuleTypeType,
        "code": str,
        "message": str,
    },
)

BatchGetSchemaAnalysisRuleInputRequestTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "schemaAnalysisRuleRequests": List["SchemaAnalysisRuleRequestTypeDef"],
    },
)

BatchGetSchemaAnalysisRuleOutputTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleOutputTypeDef",
    {
        "analysisRules": List["AnalysisRuleTypeDef"],
        "errors": List["BatchGetSchemaAnalysisRuleErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetSchemaErrorTypeDef = TypedDict(
    "BatchGetSchemaErrorTypeDef",
    {
        "name": str,
        "code": str,
        "message": str,
    },
)

BatchGetSchemaInputRequestTypeDef = TypedDict(
    "BatchGetSchemaInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "names": List[str],
    },
)

BatchGetSchemaOutputTypeDef = TypedDict(
    "BatchGetSchemaOutputTypeDef",
    {
        "schemas": List["SchemaTypeDef"],
        "errors": List["BatchGetSchemaErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCollaborationAnalysisTemplateSummaryTypeDef = TypedDict(
    "_RequiredCollaborationAnalysisTemplateSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
    },
)
_OptionalCollaborationAnalysisTemplateSummaryTypeDef = TypedDict(
    "_OptionalCollaborationAnalysisTemplateSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CollaborationAnalysisTemplateSummaryTypeDef(
    _RequiredCollaborationAnalysisTemplateSummaryTypeDef,
    _OptionalCollaborationAnalysisTemplateSummaryTypeDef,
):
    pass

_RequiredCollaborationAnalysisTemplateTypeDef = TypedDict(
    "_RequiredCollaborationAnalysisTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "schema": "AnalysisSchemaTypeDef",
        "format": Literal["SQL"],
        "source": "AnalysisSourceTypeDef",
    },
)
_OptionalCollaborationAnalysisTemplateTypeDef = TypedDict(
    "_OptionalCollaborationAnalysisTemplateTypeDef",
    {
        "description": str,
        "analysisParameters": List["AnalysisParameterTypeDef"],
        "validations": List["AnalysisTemplateValidationStatusDetailTypeDef"],
    },
    total=False,
)

class CollaborationAnalysisTemplateTypeDef(
    _RequiredCollaborationAnalysisTemplateTypeDef, _OptionalCollaborationAnalysisTemplateTypeDef
):
    pass

_RequiredCollaborationConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "_RequiredCollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
    },
)
_OptionalCollaborationConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "_OptionalCollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CollaborationConfiguredAudienceModelAssociationSummaryTypeDef(
    _RequiredCollaborationConfiguredAudienceModelAssociationSummaryTypeDef,
    _OptionalCollaborationConfiguredAudienceModelAssociationSummaryTypeDef,
):
    pass

_RequiredCollaborationConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "_RequiredCollaborationConfiguredAudienceModelAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "configuredAudienceModelArn": str,
        "name": str,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalCollaborationConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "_OptionalCollaborationConfiguredAudienceModelAssociationTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CollaborationConfiguredAudienceModelAssociationTypeDef(
    _RequiredCollaborationConfiguredAudienceModelAssociationTypeDef,
    _OptionalCollaborationConfiguredAudienceModelAssociationTypeDef,
):
    pass

CollaborationPrivacyBudgetSummaryTypeDef = TypedDict(
    "CollaborationPrivacyBudgetSummaryTypeDef",
    {
        "id": str,
        "privacyBudgetTemplateId": str,
        "privacyBudgetTemplateArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
        "budget": "PrivacyBudgetTypeDef",
    },
)

CollaborationPrivacyBudgetTemplateSummaryTypeDef = TypedDict(
    "CollaborationPrivacyBudgetTemplateSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
    },
)

CollaborationPrivacyBudgetTemplateTypeDef = TypedDict(
    "CollaborationPrivacyBudgetTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "autoRefresh": PrivacyBudgetTemplateAutoRefreshType,
        "parameters": "PrivacyBudgetTemplateParametersOutputTypeDef",
    },
)

_RequiredCollaborationSummaryTypeDef = TypedDict(
    "_RequiredCollaborationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "creatorAccountId": str,
        "creatorDisplayName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "memberStatus": MemberStatusType,
    },
)
_OptionalCollaborationSummaryTypeDef = TypedDict(
    "_OptionalCollaborationSummaryTypeDef",
    {
        "membershipId": str,
        "membershipArn": str,
    },
    total=False,
)

class CollaborationSummaryTypeDef(
    _RequiredCollaborationSummaryTypeDef, _OptionalCollaborationSummaryTypeDef
):
    pass

_RequiredCollaborationTypeDef = TypedDict(
    "_RequiredCollaborationTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "creatorAccountId": str,
        "creatorDisplayName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "memberStatus": MemberStatusType,
        "queryLogStatus": CollaborationQueryLogStatusType,
    },
)
_OptionalCollaborationTypeDef = TypedDict(
    "_OptionalCollaborationTypeDef",
    {
        "description": str,
        "membershipId": str,
        "membershipArn": str,
        "dataEncryptionMetadata": "DataEncryptionMetadataTypeDef",
    },
    total=False,
)

class CollaborationTypeDef(_RequiredCollaborationTypeDef, _OptionalCollaborationTypeDef):
    pass

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)

_RequiredConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "_RequiredConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "membershipId": str,
        "membershipArn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
        "name": str,
        "configuredAudienceModelArn": str,
    },
)
_OptionalConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "_OptionalConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ConfiguredAudienceModelAssociationSummaryTypeDef(
    _RequiredConfiguredAudienceModelAssociationSummaryTypeDef,
    _OptionalConfiguredAudienceModelAssociationSummaryTypeDef,
):
    pass

_RequiredConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "_RequiredConfiguredAudienceModelAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "configuredAudienceModelArn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "manageResourcePolicies": bool,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "_OptionalConfiguredAudienceModelAssociationTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ConfiguredAudienceModelAssociationTypeDef(
    _RequiredConfiguredAudienceModelAssociationTypeDef,
    _OptionalConfiguredAudienceModelAssociationTypeDef,
):
    pass

ConfiguredTableAnalysisRulePolicyTypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyTypeDef",
    {
        "v1": "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    },
    total=False,
)

ConfiguredTableAnalysisRulePolicyV1TypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    {
        "list": "AnalysisRuleListTypeDef",
        "aggregation": "AnalysisRuleAggregationTypeDef",
        "custom": "AnalysisRuleCustomTypeDef",
    },
    total=False,
)

ConfiguredTableAnalysisRuleTypeDef = TypedDict(
    "ConfiguredTableAnalysisRuleTypeDef",
    {
        "configuredTableId": str,
        "configuredTableArn": str,
        "policy": "ConfiguredTableAnalysisRulePolicyTypeDef",
        "type": ConfiguredTableAnalysisRuleTypeType,
        "createTime": datetime,
        "updateTime": datetime,
    },
)

ConfiguredTableAssociationSummaryTypeDef = TypedDict(
    "ConfiguredTableAssociationSummaryTypeDef",
    {
        "configuredTableId": str,
        "membershipId": str,
        "membershipArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
    },
)

_RequiredConfiguredTableAssociationTypeDef = TypedDict(
    "_RequiredConfiguredTableAssociationTypeDef",
    {
        "arn": str,
        "id": str,
        "configuredTableId": str,
        "configuredTableArn": str,
        "membershipId": str,
        "membershipArn": str,
        "roleArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalConfiguredTableAssociationTypeDef = TypedDict(
    "_OptionalConfiguredTableAssociationTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ConfiguredTableAssociationTypeDef(
    _RequiredConfiguredTableAssociationTypeDef, _OptionalConfiguredTableAssociationTypeDef
):
    pass

ConfiguredTableSummaryTypeDef = TypedDict(
    "ConfiguredTableSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "analysisRuleTypes": List[ConfiguredTableAnalysisRuleTypeType],
        "analysisMethod": Literal["DIRECT_QUERY"],
    },
)

_RequiredConfiguredTableTypeDef = TypedDict(
    "_RequiredConfiguredTableTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "tableReference": "TableReferenceTypeDef",
        "createTime": datetime,
        "updateTime": datetime,
        "analysisRuleTypes": List[ConfiguredTableAnalysisRuleTypeType],
        "analysisMethod": Literal["DIRECT_QUERY"],
        "allowedColumns": List[str],
    },
)
_OptionalConfiguredTableTypeDef = TypedDict(
    "_OptionalConfiguredTableTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ConfiguredTableTypeDef(_RequiredConfiguredTableTypeDef, _OptionalConfiguredTableTypeDef):
    pass

_RequiredCreateAnalysisTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreateAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "name": str,
        "format": Literal["SQL"],
        "source": "AnalysisSourceTypeDef",
    },
)
_OptionalCreateAnalysisTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreateAnalysisTemplateInputRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
        "analysisParameters": List["AnalysisParameterTypeDef"],
    },
    total=False,
)

class CreateAnalysisTemplateInputRequestTypeDef(
    _RequiredCreateAnalysisTemplateInputRequestTypeDef,
    _OptionalCreateAnalysisTemplateInputRequestTypeDef,
):
    pass

CreateAnalysisTemplateOutputTypeDef = TypedDict(
    "CreateAnalysisTemplateOutputTypeDef",
    {
        "analysisTemplate": "AnalysisTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCollaborationInputRequestTypeDef = TypedDict(
    "_RequiredCreateCollaborationInputRequestTypeDef",
    {
        "members": List["MemberSpecificationTypeDef"],
        "name": str,
        "description": str,
        "creatorMemberAbilities": List[MemberAbilityType],
        "creatorDisplayName": str,
        "queryLogStatus": CollaborationQueryLogStatusType,
    },
)
_OptionalCreateCollaborationInputRequestTypeDef = TypedDict(
    "_OptionalCreateCollaborationInputRequestTypeDef",
    {
        "dataEncryptionMetadata": "DataEncryptionMetadataTypeDef",
        "tags": Dict[str, str],
        "creatorPaymentConfiguration": "PaymentConfigurationTypeDef",
    },
    total=False,
)

class CreateCollaborationInputRequestTypeDef(
    _RequiredCreateCollaborationInputRequestTypeDef, _OptionalCreateCollaborationInputRequestTypeDef
):
    pass

CreateCollaborationOutputTypeDef = TypedDict(
    "CreateCollaborationOutputTypeDef",
    {
        "collaboration": "CollaborationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "_RequiredCreateConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "configuredAudienceModelArn": str,
        "configuredAudienceModelAssociationName": str,
        "manageResourcePolicies": bool,
    },
)
_OptionalCreateConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "_OptionalCreateConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "tags": Dict[str, str],
        "description": str,
    },
    total=False,
)

class CreateConfiguredAudienceModelAssociationInputRequestTypeDef(
    _RequiredCreateConfiguredAudienceModelAssociationInputRequestTypeDef,
    _OptionalCreateConfiguredAudienceModelAssociationInputRequestTypeDef,
):
    pass

CreateConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "CreateConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "configuredAudienceModelAssociation": "ConfiguredAudienceModelAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "CreateConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
        "analysisRulePolicy": "ConfiguredTableAnalysisRulePolicyTypeDef",
    },
)

CreateConfiguredTableAnalysisRuleOutputTypeDef = TypedDict(
    "CreateConfiguredTableAnalysisRuleOutputTypeDef",
    {
        "analysisRule": "ConfiguredTableAnalysisRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "_RequiredCreateConfiguredTableAssociationInputRequestTypeDef",
    {
        "name": str,
        "membershipIdentifier": str,
        "configuredTableIdentifier": str,
        "roleArn": str,
    },
)
_OptionalCreateConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "_OptionalCreateConfiguredTableAssociationInputRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateConfiguredTableAssociationInputRequestTypeDef(
    _RequiredCreateConfiguredTableAssociationInputRequestTypeDef,
    _OptionalCreateConfiguredTableAssociationInputRequestTypeDef,
):
    pass

CreateConfiguredTableAssociationOutputTypeDef = TypedDict(
    "CreateConfiguredTableAssociationOutputTypeDef",
    {
        "configuredTableAssociation": "ConfiguredTableAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfiguredTableInputRequestTypeDef = TypedDict(
    "_RequiredCreateConfiguredTableInputRequestTypeDef",
    {
        "name": str,
        "tableReference": "TableReferenceTypeDef",
        "allowedColumns": List[str],
        "analysisMethod": Literal["DIRECT_QUERY"],
    },
)
_OptionalCreateConfiguredTableInputRequestTypeDef = TypedDict(
    "_OptionalCreateConfiguredTableInputRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateConfiguredTableInputRequestTypeDef(
    _RequiredCreateConfiguredTableInputRequestTypeDef,
    _OptionalCreateConfiguredTableInputRequestTypeDef,
):
    pass

CreateConfiguredTableOutputTypeDef = TypedDict(
    "CreateConfiguredTableOutputTypeDef",
    {
        "configuredTable": "ConfiguredTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMembershipInputRequestTypeDef = TypedDict(
    "_RequiredCreateMembershipInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "queryLogStatus": MembershipQueryLogStatusType,
    },
)
_OptionalCreateMembershipInputRequestTypeDef = TypedDict(
    "_OptionalCreateMembershipInputRequestTypeDef",
    {
        "tags": Dict[str, str],
        "defaultResultConfiguration": "MembershipProtectedQueryResultConfigurationTypeDef",
        "paymentConfiguration": "MembershipPaymentConfigurationTypeDef",
    },
    total=False,
)

class CreateMembershipInputRequestTypeDef(
    _RequiredCreateMembershipInputRequestTypeDef, _OptionalCreateMembershipInputRequestTypeDef
):
    pass

CreateMembershipOutputTypeDef = TypedDict(
    "CreateMembershipOutputTypeDef",
    {
        "membership": "MembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreatePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "autoRefresh": PrivacyBudgetTemplateAutoRefreshType,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "parameters": "PrivacyBudgetTemplateParametersInputTypeDef",
    },
)
_OptionalCreatePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreatePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreatePrivacyBudgetTemplateInputRequestTypeDef(
    _RequiredCreatePrivacyBudgetTemplateInputRequestTypeDef,
    _OptionalCreatePrivacyBudgetTemplateInputRequestTypeDef,
):
    pass

CreatePrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "CreatePrivacyBudgetTemplateOutputTypeDef",
    {
        "privacyBudgetTemplate": "PrivacyBudgetTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataEncryptionMetadataTypeDef = TypedDict(
    "DataEncryptionMetadataTypeDef",
    {
        "allowCleartext": bool,
        "allowDuplicates": bool,
        "allowJoinsOnColumnsWithDifferentNames": bool,
        "preserveNulls": bool,
    },
)

DeleteAnalysisTemplateInputRequestTypeDef = TypedDict(
    "DeleteAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "analysisTemplateIdentifier": str,
    },
)

DeleteCollaborationInputRequestTypeDef = TypedDict(
    "DeleteCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)

DeleteConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "configuredAudienceModelAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)

DeleteConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
    },
)

DeleteConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableAssociationInputRequestTypeDef",
    {
        "configuredTableAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)

DeleteConfiguredTableInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
    },
)

DeleteMemberInputRequestTypeDef = TypedDict(
    "DeleteMemberInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "accountId": str,
    },
)

DeleteMembershipInputRequestTypeDef = TypedDict(
    "DeleteMembershipInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)

DeletePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "DeletePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
    },
)

DifferentialPrivacyColumnTypeDef = TypedDict(
    "DifferentialPrivacyColumnTypeDef",
    {
        "name": str,
    },
)

DifferentialPrivacyConfigurationTypeDef = TypedDict(
    "DifferentialPrivacyConfigurationTypeDef",
    {
        "columns": List["DifferentialPrivacyColumnTypeDef"],
    },
)

DifferentialPrivacyParametersTypeDef = TypedDict(
    "DifferentialPrivacyParametersTypeDef",
    {
        "sensitivityParameters": List["DifferentialPrivacySensitivityParametersTypeDef"],
    },
)

DifferentialPrivacyPreviewAggregationTypeDef = TypedDict(
    "DifferentialPrivacyPreviewAggregationTypeDef",
    {
        "type": DifferentialPrivacyAggregationTypeType,
        "maxCount": int,
    },
)

DifferentialPrivacyPreviewParametersInputTypeDef = TypedDict(
    "DifferentialPrivacyPreviewParametersInputTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
)

DifferentialPrivacyPrivacyBudgetAggregationTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyBudgetAggregationTypeDef",
    {
        "type": DifferentialPrivacyAggregationTypeType,
        "maxCount": int,
        "remainingCount": int,
    },
)

DifferentialPrivacyPrivacyBudgetTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyBudgetTypeDef",
    {
        "aggregations": List["DifferentialPrivacyPrivacyBudgetAggregationTypeDef"],
        "epsilon": int,
    },
)

DifferentialPrivacyPrivacyImpactTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyImpactTypeDef",
    {
        "aggregations": List["DifferentialPrivacyPreviewAggregationTypeDef"],
    },
)

_RequiredDifferentialPrivacySensitivityParametersTypeDef = TypedDict(
    "_RequiredDifferentialPrivacySensitivityParametersTypeDef",
    {
        "aggregationType": DifferentialPrivacyAggregationTypeType,
        "aggregationExpression": str,
        "userContributionLimit": int,
    },
)
_OptionalDifferentialPrivacySensitivityParametersTypeDef = TypedDict(
    "_OptionalDifferentialPrivacySensitivityParametersTypeDef",
    {
        "minColumnValue": float,
        "maxColumnValue": float,
    },
    total=False,
)

class DifferentialPrivacySensitivityParametersTypeDef(
    _RequiredDifferentialPrivacySensitivityParametersTypeDef,
    _OptionalDifferentialPrivacySensitivityParametersTypeDef,
):
    pass

DifferentialPrivacyTemplateParametersInputTypeDef = TypedDict(
    "DifferentialPrivacyTemplateParametersInputTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
)

DifferentialPrivacyTemplateParametersOutputTypeDef = TypedDict(
    "DifferentialPrivacyTemplateParametersOutputTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
)

DifferentialPrivacyTemplateUpdateParametersTypeDef = TypedDict(
    "DifferentialPrivacyTemplateUpdateParametersTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
    total=False,
)

GetAnalysisTemplateInputRequestTypeDef = TypedDict(
    "GetAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "analysisTemplateIdentifier": str,
    },
)

GetAnalysisTemplateOutputTypeDef = TypedDict(
    "GetAnalysisTemplateOutputTypeDef",
    {
        "analysisTemplate": "AnalysisTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCollaborationAnalysisTemplateInputRequestTypeDef = TypedDict(
    "GetCollaborationAnalysisTemplateInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "analysisTemplateArn": str,
    },
)

GetCollaborationAnalysisTemplateOutputTypeDef = TypedDict(
    "GetCollaborationAnalysisTemplateOutputTypeDef",
    {
        "collaborationAnalysisTemplate": "CollaborationAnalysisTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "configuredAudienceModelAssociationIdentifier": str,
    },
)

GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "collaborationConfiguredAudienceModelAssociation": "CollaborationConfiguredAudienceModelAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCollaborationInputRequestTypeDef = TypedDict(
    "GetCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)

GetCollaborationOutputTypeDef = TypedDict(
    "GetCollaborationOutputTypeDef",
    {
        "collaboration": "CollaborationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
    },
)

GetCollaborationPrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "GetCollaborationPrivacyBudgetTemplateOutputTypeDef",
    {
        "collaborationPrivacyBudgetTemplate": "CollaborationPrivacyBudgetTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "configuredAudienceModelAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)

GetConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "GetConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "configuredAudienceModelAssociation": "ConfiguredAudienceModelAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "GetConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
    },
)

GetConfiguredTableAnalysisRuleOutputTypeDef = TypedDict(
    "GetConfiguredTableAnalysisRuleOutputTypeDef",
    {
        "analysisRule": "ConfiguredTableAnalysisRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "GetConfiguredTableAssociationInputRequestTypeDef",
    {
        "configuredTableAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)

GetConfiguredTableAssociationOutputTypeDef = TypedDict(
    "GetConfiguredTableAssociationOutputTypeDef",
    {
        "configuredTableAssociation": "ConfiguredTableAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfiguredTableInputRequestTypeDef = TypedDict(
    "GetConfiguredTableInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
    },
)

GetConfiguredTableOutputTypeDef = TypedDict(
    "GetConfiguredTableOutputTypeDef",
    {
        "configuredTable": "ConfiguredTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembershipInputRequestTypeDef = TypedDict(
    "GetMembershipInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)

GetMembershipOutputTypeDef = TypedDict(
    "GetMembershipOutputTypeDef",
    {
        "membership": "MembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "GetPrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
    },
)

GetPrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "GetPrivacyBudgetTemplateOutputTypeDef",
    {
        "privacyBudgetTemplate": "PrivacyBudgetTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProtectedQueryInputRequestTypeDef = TypedDict(
    "GetProtectedQueryInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "protectedQueryIdentifier": str,
    },
)

GetProtectedQueryOutputTypeDef = TypedDict(
    "GetProtectedQueryOutputTypeDef",
    {
        "protectedQuery": "ProtectedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaAnalysisRuleInputRequestTypeDef = TypedDict(
    "GetSchemaAnalysisRuleInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "name": str,
        "type": AnalysisRuleTypeType,
    },
)

GetSchemaAnalysisRuleOutputTypeDef = TypedDict(
    "GetSchemaAnalysisRuleOutputTypeDef",
    {
        "analysisRule": "AnalysisRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaInputRequestTypeDef = TypedDict(
    "GetSchemaInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "name": str,
    },
)

GetSchemaOutputTypeDef = TypedDict(
    "GetSchemaOutputTypeDef",
    {
        "schema": "SchemaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlueTableReferenceTypeDef = TypedDict(
    "GlueTableReferenceTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)

_RequiredListAnalysisTemplatesInputRequestTypeDef = TypedDict(
    "_RequiredListAnalysisTemplatesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
_OptionalListAnalysisTemplatesInputRequestTypeDef = TypedDict(
    "_OptionalListAnalysisTemplatesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAnalysisTemplatesInputRequestTypeDef(
    _RequiredListAnalysisTemplatesInputRequestTypeDef,
    _OptionalListAnalysisTemplatesInputRequestTypeDef,
):
    pass

ListAnalysisTemplatesOutputTypeDef = TypedDict(
    "ListAnalysisTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "analysisTemplateSummaries": List["AnalysisTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCollaborationAnalysisTemplatesInputRequestTypeDef = TypedDict(
    "_RequiredListCollaborationAnalysisTemplatesInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
_OptionalListCollaborationAnalysisTemplatesInputRequestTypeDef = TypedDict(
    "_OptionalListCollaborationAnalysisTemplatesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListCollaborationAnalysisTemplatesInputRequestTypeDef(
    _RequiredListCollaborationAnalysisTemplatesInputRequestTypeDef,
    _OptionalListCollaborationAnalysisTemplatesInputRequestTypeDef,
):
    pass

ListCollaborationAnalysisTemplatesOutputTypeDef = TypedDict(
    "ListCollaborationAnalysisTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "collaborationAnalysisTemplateSummaries": List[
            "CollaborationAnalysisTemplateSummaryTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef = TypedDict(
    "_RequiredListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
_OptionalListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef = TypedDict(
    "_OptionalListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef(
    _RequiredListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef,
    _OptionalListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef,
):
    pass

ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef = TypedDict(
    "ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef",
    {
        "collaborationConfiguredAudienceModelAssociationSummaries": List[
            "CollaborationConfiguredAudienceModelAssociationSummaryTypeDef"
        ],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef = TypedDict(
    "_RequiredListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
_OptionalListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef = TypedDict(
    "_OptionalListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef(
    _RequiredListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef,
    _OptionalListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef,
):
    pass

ListCollaborationPrivacyBudgetTemplatesOutputTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "collaborationPrivacyBudgetTemplateSummaries": List[
            "CollaborationPrivacyBudgetTemplateSummaryTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCollaborationPrivacyBudgetsInputRequestTypeDef = TypedDict(
    "_RequiredListCollaborationPrivacyBudgetsInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
    },
)
_OptionalListCollaborationPrivacyBudgetsInputRequestTypeDef = TypedDict(
    "_OptionalListCollaborationPrivacyBudgetsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListCollaborationPrivacyBudgetsInputRequestTypeDef(
    _RequiredListCollaborationPrivacyBudgetsInputRequestTypeDef,
    _OptionalListCollaborationPrivacyBudgetsInputRequestTypeDef,
):
    pass

ListCollaborationPrivacyBudgetsOutputTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetsOutputTypeDef",
    {
        "collaborationPrivacyBudgetSummaries": List["CollaborationPrivacyBudgetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCollaborationsInputRequestTypeDef = TypedDict(
    "ListCollaborationsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "memberStatus": FilterableMemberStatusType,
    },
    total=False,
)

ListCollaborationsOutputTypeDef = TypedDict(
    "ListCollaborationsOutputTypeDef",
    {
        "nextToken": str,
        "collaborationList": List["CollaborationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfiguredAudienceModelAssociationsInputRequestTypeDef = TypedDict(
    "_RequiredListConfiguredAudienceModelAssociationsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
_OptionalListConfiguredAudienceModelAssociationsInputRequestTypeDef = TypedDict(
    "_OptionalListConfiguredAudienceModelAssociationsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListConfiguredAudienceModelAssociationsInputRequestTypeDef(
    _RequiredListConfiguredAudienceModelAssociationsInputRequestTypeDef,
    _OptionalListConfiguredAudienceModelAssociationsInputRequestTypeDef,
):
    pass

ListConfiguredAudienceModelAssociationsOutputTypeDef = TypedDict(
    "ListConfiguredAudienceModelAssociationsOutputTypeDef",
    {
        "configuredAudienceModelAssociationSummaries": List[
            "ConfiguredAudienceModelAssociationSummaryTypeDef"
        ],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfiguredTableAssociationsInputRequestTypeDef = TypedDict(
    "_RequiredListConfiguredTableAssociationsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
_OptionalListConfiguredTableAssociationsInputRequestTypeDef = TypedDict(
    "_OptionalListConfiguredTableAssociationsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListConfiguredTableAssociationsInputRequestTypeDef(
    _RequiredListConfiguredTableAssociationsInputRequestTypeDef,
    _OptionalListConfiguredTableAssociationsInputRequestTypeDef,
):
    pass

ListConfiguredTableAssociationsOutputTypeDef = TypedDict(
    "ListConfiguredTableAssociationsOutputTypeDef",
    {
        "configuredTableAssociationSummaries": List["ConfiguredTableAssociationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfiguredTablesInputRequestTypeDef = TypedDict(
    "ListConfiguredTablesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListConfiguredTablesOutputTypeDef = TypedDict(
    "ListConfiguredTablesOutputTypeDef",
    {
        "configuredTableSummaries": List["ConfiguredTableSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersInputRequestTypeDef = TypedDict(
    "_RequiredListMembersInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
_OptionalListMembersInputRequestTypeDef = TypedDict(
    "_OptionalListMembersInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListMembersInputRequestTypeDef(
    _RequiredListMembersInputRequestTypeDef, _OptionalListMembersInputRequestTypeDef
):
    pass

ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {
        "nextToken": str,
        "memberSummaries": List["MemberSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembershipsInputRequestTypeDef = TypedDict(
    "ListMembershipsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": MembershipStatusType,
    },
    total=False,
)

ListMembershipsOutputTypeDef = TypedDict(
    "ListMembershipsOutputTypeDef",
    {
        "nextToken": str,
        "membershipSummaries": List["MembershipSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrivacyBudgetTemplatesInputRequestTypeDef = TypedDict(
    "_RequiredListPrivacyBudgetTemplatesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
_OptionalListPrivacyBudgetTemplatesInputRequestTypeDef = TypedDict(
    "_OptionalListPrivacyBudgetTemplatesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPrivacyBudgetTemplatesInputRequestTypeDef(
    _RequiredListPrivacyBudgetTemplatesInputRequestTypeDef,
    _OptionalListPrivacyBudgetTemplatesInputRequestTypeDef,
):
    pass

ListPrivacyBudgetTemplatesOutputTypeDef = TypedDict(
    "ListPrivacyBudgetTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "privacyBudgetTemplateSummaries": List["PrivacyBudgetTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrivacyBudgetsInputRequestTypeDef = TypedDict(
    "_RequiredListPrivacyBudgetsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
    },
)
_OptionalListPrivacyBudgetsInputRequestTypeDef = TypedDict(
    "_OptionalListPrivacyBudgetsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPrivacyBudgetsInputRequestTypeDef(
    _RequiredListPrivacyBudgetsInputRequestTypeDef, _OptionalListPrivacyBudgetsInputRequestTypeDef
):
    pass

ListPrivacyBudgetsOutputTypeDef = TypedDict(
    "ListPrivacyBudgetsOutputTypeDef",
    {
        "privacyBudgetSummaries": List["PrivacyBudgetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProtectedQueriesInputRequestTypeDef = TypedDict(
    "_RequiredListProtectedQueriesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
_OptionalListProtectedQueriesInputRequestTypeDef = TypedDict(
    "_OptionalListProtectedQueriesInputRequestTypeDef",
    {
        "status": ProtectedQueryStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListProtectedQueriesInputRequestTypeDef(
    _RequiredListProtectedQueriesInputRequestTypeDef,
    _OptionalListProtectedQueriesInputRequestTypeDef,
):
    pass

ListProtectedQueriesOutputTypeDef = TypedDict(
    "ListProtectedQueriesOutputTypeDef",
    {
        "nextToken": str,
        "protectedQueries": List["ProtectedQuerySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemasInputRequestTypeDef = TypedDict(
    "_RequiredListSchemasInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
_OptionalListSchemasInputRequestTypeDef = TypedDict(
    "_OptionalListSchemasInputRequestTypeDef",
    {
        "schemaType": Literal["TABLE"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSchemasInputRequestTypeDef(
    _RequiredListSchemasInputRequestTypeDef, _OptionalListSchemasInputRequestTypeDef
):
    pass

ListSchemasOutputTypeDef = TypedDict(
    "ListSchemasOutputTypeDef",
    {
        "schemaSummaries": List["SchemaSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMemberSpecificationTypeDef = TypedDict(
    "_RequiredMemberSpecificationTypeDef",
    {
        "accountId": str,
        "memberAbilities": List[MemberAbilityType],
        "displayName": str,
    },
)
_OptionalMemberSpecificationTypeDef = TypedDict(
    "_OptionalMemberSpecificationTypeDef",
    {
        "paymentConfiguration": "PaymentConfigurationTypeDef",
    },
    total=False,
)

class MemberSpecificationTypeDef(
    _RequiredMemberSpecificationTypeDef, _OptionalMemberSpecificationTypeDef
):
    pass

_RequiredMemberSummaryTypeDef = TypedDict(
    "_RequiredMemberSummaryTypeDef",
    {
        "accountId": str,
        "status": MemberStatusType,
        "displayName": str,
        "abilities": List[MemberAbilityType],
        "createTime": datetime,
        "updateTime": datetime,
        "paymentConfiguration": "PaymentConfigurationTypeDef",
    },
)
_OptionalMemberSummaryTypeDef = TypedDict(
    "_OptionalMemberSummaryTypeDef",
    {
        "membershipId": str,
        "membershipArn": str,
    },
    total=False,
)

class MemberSummaryTypeDef(_RequiredMemberSummaryTypeDef, _OptionalMemberSummaryTypeDef):
    pass

MembershipPaymentConfigurationTypeDef = TypedDict(
    "MembershipPaymentConfigurationTypeDef",
    {
        "queryCompute": "MembershipQueryComputePaymentConfigTypeDef",
    },
)

MembershipProtectedQueryOutputConfigurationTypeDef = TypedDict(
    "MembershipProtectedQueryOutputConfigurationTypeDef",
    {
        "s3": "ProtectedQueryS3OutputConfigurationTypeDef",
    },
    total=False,
)

_RequiredMembershipProtectedQueryResultConfigurationTypeDef = TypedDict(
    "_RequiredMembershipProtectedQueryResultConfigurationTypeDef",
    {
        "outputConfiguration": "MembershipProtectedQueryOutputConfigurationTypeDef",
    },
)
_OptionalMembershipProtectedQueryResultConfigurationTypeDef = TypedDict(
    "_OptionalMembershipProtectedQueryResultConfigurationTypeDef",
    {
        "roleArn": str,
    },
    total=False,
)

class MembershipProtectedQueryResultConfigurationTypeDef(
    _RequiredMembershipProtectedQueryResultConfigurationTypeDef,
    _OptionalMembershipProtectedQueryResultConfigurationTypeDef,
):
    pass

MembershipQueryComputePaymentConfigTypeDef = TypedDict(
    "MembershipQueryComputePaymentConfigTypeDef",
    {
        "isResponsible": bool,
    },
)

MembershipSummaryTypeDef = TypedDict(
    "MembershipSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "collaborationCreatorAccountId": str,
        "collaborationCreatorDisplayName": str,
        "collaborationName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "status": MembershipStatusType,
        "memberAbilities": List[MemberAbilityType],
        "paymentConfiguration": "MembershipPaymentConfigurationTypeDef",
    },
)

_RequiredMembershipTypeDef = TypedDict(
    "_RequiredMembershipTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "collaborationCreatorAccountId": str,
        "collaborationCreatorDisplayName": str,
        "collaborationName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "status": MembershipStatusType,
        "memberAbilities": List[MemberAbilityType],
        "queryLogStatus": MembershipQueryLogStatusType,
        "paymentConfiguration": "MembershipPaymentConfigurationTypeDef",
    },
)
_OptionalMembershipTypeDef = TypedDict(
    "_OptionalMembershipTypeDef",
    {
        "defaultResultConfiguration": "MembershipProtectedQueryResultConfigurationTypeDef",
    },
    total=False,
)

class MembershipTypeDef(_RequiredMembershipTypeDef, _OptionalMembershipTypeDef):
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

PaymentConfigurationTypeDef = TypedDict(
    "PaymentConfigurationTypeDef",
    {
        "queryCompute": "QueryComputePaymentConfigTypeDef",
    },
)

PreviewPrivacyImpactInputRequestTypeDef = TypedDict(
    "PreviewPrivacyImpactInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "parameters": "PreviewPrivacyImpactParametersInputTypeDef",
    },
)

PreviewPrivacyImpactOutputTypeDef = TypedDict(
    "PreviewPrivacyImpactOutputTypeDef",
    {
        "privacyImpact": "PrivacyImpactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PreviewPrivacyImpactParametersInputTypeDef = TypedDict(
    "PreviewPrivacyImpactParametersInputTypeDef",
    {
        "differentialPrivacy": "DifferentialPrivacyPreviewParametersInputTypeDef",
    },
    total=False,
)

PrivacyBudgetSummaryTypeDef = TypedDict(
    "PrivacyBudgetSummaryTypeDef",
    {
        "id": str,
        "privacyBudgetTemplateId": str,
        "privacyBudgetTemplateArn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
        "budget": "PrivacyBudgetTypeDef",
    },
)

PrivacyBudgetTemplateParametersInputTypeDef = TypedDict(
    "PrivacyBudgetTemplateParametersInputTypeDef",
    {
        "differentialPrivacy": "DifferentialPrivacyTemplateParametersInputTypeDef",
    },
    total=False,
)

PrivacyBudgetTemplateParametersOutputTypeDef = TypedDict(
    "PrivacyBudgetTemplateParametersOutputTypeDef",
    {
        "differentialPrivacy": "DifferentialPrivacyTemplateParametersOutputTypeDef",
    },
    total=False,
)

PrivacyBudgetTemplateSummaryTypeDef = TypedDict(
    "PrivacyBudgetTemplateSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
    },
)

PrivacyBudgetTemplateTypeDef = TypedDict(
    "PrivacyBudgetTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "createTime": datetime,
        "updateTime": datetime,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "autoRefresh": PrivacyBudgetTemplateAutoRefreshType,
        "parameters": "PrivacyBudgetTemplateParametersOutputTypeDef",
    },
)

PrivacyBudgetTemplateUpdateParametersTypeDef = TypedDict(
    "PrivacyBudgetTemplateUpdateParametersTypeDef",
    {
        "differentialPrivacy": "DifferentialPrivacyTemplateUpdateParametersTypeDef",
    },
    total=False,
)

PrivacyBudgetTypeDef = TypedDict(
    "PrivacyBudgetTypeDef",
    {
        "differentialPrivacy": "DifferentialPrivacyPrivacyBudgetTypeDef",
    },
    total=False,
)

PrivacyImpactTypeDef = TypedDict(
    "PrivacyImpactTypeDef",
    {
        "differentialPrivacy": "DifferentialPrivacyPrivacyImpactTypeDef",
    },
    total=False,
)

ProtectedQueryErrorTypeDef = TypedDict(
    "ProtectedQueryErrorTypeDef",
    {
        "message": str,
        "code": str,
    },
)

ProtectedQueryOutputConfigurationTypeDef = TypedDict(
    "ProtectedQueryOutputConfigurationTypeDef",
    {
        "s3": "ProtectedQueryS3OutputConfigurationTypeDef",
    },
    total=False,
)

ProtectedQueryOutputTypeDef = TypedDict(
    "ProtectedQueryOutputTypeDef",
    {
        "s3": "ProtectedQueryS3OutputTypeDef",
        "memberList": List["ProtectedQuerySingleMemberOutputTypeDef"],
    },
    total=False,
)

ProtectedQueryResultConfigurationTypeDef = TypedDict(
    "ProtectedQueryResultConfigurationTypeDef",
    {
        "outputConfiguration": "ProtectedQueryOutputConfigurationTypeDef",
    },
)

ProtectedQueryResultTypeDef = TypedDict(
    "ProtectedQueryResultTypeDef",
    {
        "output": "ProtectedQueryOutputTypeDef",
    },
)

_RequiredProtectedQueryS3OutputConfigurationTypeDef = TypedDict(
    "_RequiredProtectedQueryS3OutputConfigurationTypeDef",
    {
        "resultFormat": ResultFormatType,
        "bucket": str,
    },
)
_OptionalProtectedQueryS3OutputConfigurationTypeDef = TypedDict(
    "_OptionalProtectedQueryS3OutputConfigurationTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class ProtectedQueryS3OutputConfigurationTypeDef(
    _RequiredProtectedQueryS3OutputConfigurationTypeDef,
    _OptionalProtectedQueryS3OutputConfigurationTypeDef,
):
    pass

ProtectedQueryS3OutputTypeDef = TypedDict(
    "ProtectedQueryS3OutputTypeDef",
    {
        "location": str,
    },
)

ProtectedQuerySQLParametersTypeDef = TypedDict(
    "ProtectedQuerySQLParametersTypeDef",
    {
        "queryString": str,
        "analysisTemplateArn": str,
        "parameters": Dict[str, str],
    },
    total=False,
)

ProtectedQuerySingleMemberOutputTypeDef = TypedDict(
    "ProtectedQuerySingleMemberOutputTypeDef",
    {
        "accountId": str,
    },
)

ProtectedQueryStatisticsTypeDef = TypedDict(
    "ProtectedQueryStatisticsTypeDef",
    {
        "totalDurationInMillis": int,
    },
    total=False,
)

ProtectedQuerySummaryTypeDef = TypedDict(
    "ProtectedQuerySummaryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedQueryStatusType,
    },
)

_RequiredProtectedQueryTypeDef = TypedDict(
    "_RequiredProtectedQueryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedQueryStatusType,
    },
)
_OptionalProtectedQueryTypeDef = TypedDict(
    "_OptionalProtectedQueryTypeDef",
    {
        "sqlParameters": "ProtectedQuerySQLParametersTypeDef",
        "resultConfiguration": "ProtectedQueryResultConfigurationTypeDef",
        "statistics": "ProtectedQueryStatisticsTypeDef",
        "result": "ProtectedQueryResultTypeDef",
        "error": "ProtectedQueryErrorTypeDef",
        "differentialPrivacy": "DifferentialPrivacyParametersTypeDef",
    },
    total=False,
)

class ProtectedQueryTypeDef(_RequiredProtectedQueryTypeDef, _OptionalProtectedQueryTypeDef):
    pass

QueryComputePaymentConfigTypeDef = TypedDict(
    "QueryComputePaymentConfigTypeDef",
    {
        "isResponsible": bool,
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

SchemaAnalysisRuleRequestTypeDef = TypedDict(
    "SchemaAnalysisRuleRequestTypeDef",
    {
        "name": str,
        "type": AnalysisRuleTypeType,
    },
)

_RequiredSchemaStatusDetailTypeDef = TypedDict(
    "_RequiredSchemaStatusDetailTypeDef",
    {
        "status": SchemaStatusType,
    },
)
_OptionalSchemaStatusDetailTypeDef = TypedDict(
    "_OptionalSchemaStatusDetailTypeDef",
    {
        "reasons": List["SchemaStatusReasonTypeDef"],
        "analysisRuleType": AnalysisRuleTypeType,
        "configurations": List[Literal["DIFFERENTIAL_PRIVACY"]],
    },
    total=False,
)

class SchemaStatusDetailTypeDef(
    _RequiredSchemaStatusDetailTypeDef, _OptionalSchemaStatusDetailTypeDef
):
    pass

SchemaStatusReasonTypeDef = TypedDict(
    "SchemaStatusReasonTypeDef",
    {
        "code": SchemaStatusReasonCodeType,
        "message": str,
    },
)

_RequiredSchemaSummaryTypeDef = TypedDict(
    "_RequiredSchemaSummaryTypeDef",
    {
        "name": str,
        "type": Literal["TABLE"],
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "collaborationId": str,
        "collaborationArn": str,
        "analysisRuleTypes": List[AnalysisRuleTypeType],
    },
)
_OptionalSchemaSummaryTypeDef = TypedDict(
    "_OptionalSchemaSummaryTypeDef",
    {
        "analysisMethod": Literal["DIRECT_QUERY"],
    },
    total=False,
)

class SchemaSummaryTypeDef(_RequiredSchemaSummaryTypeDef, _OptionalSchemaSummaryTypeDef):
    pass

_RequiredSchemaTypeDef = TypedDict(
    "_RequiredSchemaTypeDef",
    {
        "columns": List["ColumnTypeDef"],
        "partitionKeys": List["ColumnTypeDef"],
        "analysisRuleTypes": List[AnalysisRuleTypeType],
        "creatorAccountId": str,
        "name": str,
        "collaborationId": str,
        "collaborationArn": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
        "type": Literal["TABLE"],
        "schemaStatusDetails": List["SchemaStatusDetailTypeDef"],
    },
)
_OptionalSchemaTypeDef = TypedDict(
    "_OptionalSchemaTypeDef",
    {
        "analysisMethod": Literal["DIRECT_QUERY"],
    },
    total=False,
)

class SchemaTypeDef(_RequiredSchemaTypeDef, _OptionalSchemaTypeDef):
    pass

_RequiredStartProtectedQueryInputRequestTypeDef = TypedDict(
    "_RequiredStartProtectedQueryInputRequestTypeDef",
    {
        "type": Literal["SQL"],
        "membershipIdentifier": str,
        "sqlParameters": "ProtectedQuerySQLParametersTypeDef",
    },
)
_OptionalStartProtectedQueryInputRequestTypeDef = TypedDict(
    "_OptionalStartProtectedQueryInputRequestTypeDef",
    {
        "resultConfiguration": "ProtectedQueryResultConfigurationTypeDef",
    },
    total=False,
)

class StartProtectedQueryInputRequestTypeDef(
    _RequiredStartProtectedQueryInputRequestTypeDef, _OptionalStartProtectedQueryInputRequestTypeDef
):
    pass

StartProtectedQueryOutputTypeDef = TypedDict(
    "StartProtectedQueryOutputTypeDef",
    {
        "protectedQuery": "ProtectedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableReferenceTypeDef = TypedDict(
    "TableReferenceTypeDef",
    {
        "glue": "GlueTableReferenceTypeDef",
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAnalysisTemplateInputRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "analysisTemplateIdentifier": str,
    },
)
_OptionalUpdateAnalysisTemplateInputRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisTemplateInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateAnalysisTemplateInputRequestTypeDef(
    _RequiredUpdateAnalysisTemplateInputRequestTypeDef,
    _OptionalUpdateAnalysisTemplateInputRequestTypeDef,
):
    pass

UpdateAnalysisTemplateOutputTypeDef = TypedDict(
    "UpdateAnalysisTemplateOutputTypeDef",
    {
        "analysisTemplate": "AnalysisTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCollaborationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
_OptionalUpdateCollaborationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateCollaborationInputRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateCollaborationInputRequestTypeDef(
    _RequiredUpdateCollaborationInputRequestTypeDef, _OptionalUpdateCollaborationInputRequestTypeDef
):
    pass

UpdateCollaborationOutputTypeDef = TypedDict(
    "UpdateCollaborationOutputTypeDef",
    {
        "collaboration": "CollaborationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "configuredAudienceModelAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
_OptionalUpdateConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "description": str,
        "name": str,
    },
    total=False,
)

class UpdateConfiguredAudienceModelAssociationInputRequestTypeDef(
    _RequiredUpdateConfiguredAudienceModelAssociationInputRequestTypeDef,
    _OptionalUpdateConfiguredAudienceModelAssociationInputRequestTypeDef,
):
    pass

UpdateConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "configuredAudienceModelAssociation": "ConfiguredAudienceModelAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "UpdateConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
        "analysisRulePolicy": "ConfiguredTableAnalysisRulePolicyTypeDef",
    },
)

UpdateConfiguredTableAnalysisRuleOutputTypeDef = TypedDict(
    "UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    {
        "analysisRule": "ConfiguredTableAnalysisRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateConfiguredTableAssociationInputRequestTypeDef",
    {
        "configuredTableAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
_OptionalUpdateConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateConfiguredTableAssociationInputRequestTypeDef",
    {
        "description": str,
        "roleArn": str,
    },
    total=False,
)

class UpdateConfiguredTableAssociationInputRequestTypeDef(
    _RequiredUpdateConfiguredTableAssociationInputRequestTypeDef,
    _OptionalUpdateConfiguredTableAssociationInputRequestTypeDef,
):
    pass

UpdateConfiguredTableAssociationOutputTypeDef = TypedDict(
    "UpdateConfiguredTableAssociationOutputTypeDef",
    {
        "configuredTableAssociation": "ConfiguredTableAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfiguredTableInputRequestTypeDef = TypedDict(
    "_RequiredUpdateConfiguredTableInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
    },
)
_OptionalUpdateConfiguredTableInputRequestTypeDef = TypedDict(
    "_OptionalUpdateConfiguredTableInputRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateConfiguredTableInputRequestTypeDef(
    _RequiredUpdateConfiguredTableInputRequestTypeDef,
    _OptionalUpdateConfiguredTableInputRequestTypeDef,
):
    pass

UpdateConfiguredTableOutputTypeDef = TypedDict(
    "UpdateConfiguredTableOutputTypeDef",
    {
        "configuredTable": "ConfiguredTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMembershipInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMembershipInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
_OptionalUpdateMembershipInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMembershipInputRequestTypeDef",
    {
        "queryLogStatus": MembershipQueryLogStatusType,
        "defaultResultConfiguration": "MembershipProtectedQueryResultConfigurationTypeDef",
    },
    total=False,
)

class UpdateMembershipInputRequestTypeDef(
    _RequiredUpdateMembershipInputRequestTypeDef, _OptionalUpdateMembershipInputRequestTypeDef
):
    pass

UpdateMembershipOutputTypeDef = TypedDict(
    "UpdateMembershipOutputTypeDef",
    {
        "membership": "MembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
    },
)
_OptionalUpdatePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "parameters": "PrivacyBudgetTemplateUpdateParametersTypeDef",
    },
    total=False,
)

class UpdatePrivacyBudgetTemplateInputRequestTypeDef(
    _RequiredUpdatePrivacyBudgetTemplateInputRequestTypeDef,
    _OptionalUpdatePrivacyBudgetTemplateInputRequestTypeDef,
):
    pass

UpdatePrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "UpdatePrivacyBudgetTemplateOutputTypeDef",
    {
        "privacyBudgetTemplate": "PrivacyBudgetTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProtectedQueryInputRequestTypeDef = TypedDict(
    "UpdateProtectedQueryInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "protectedQueryIdentifier": str,
        "targetStatus": Literal["CANCELLED"],
    },
)

UpdateProtectedQueryOutputTypeDef = TypedDict(
    "UpdateProtectedQueryOutputTypeDef",
    {
        "protectedQuery": "ProtectedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
