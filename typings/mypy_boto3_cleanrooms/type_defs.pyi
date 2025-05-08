"""
Type annotations for cleanrooms service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cleanrooms.type_defs import AggregateColumnOutputTypeDef

    data: AggregateColumnOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AdditionalAnalysesType,
    AggregateFunctionNameType,
    AnalysisFormatType,
    AnalysisMethodType,
    AnalysisRuleTypeType,
    AnalysisTemplateValidationStatusType,
    AnalysisTypeType,
    AnalyticsEngineType,
    CollaborationJobLogStatusType,
    CollaborationQueryLogStatusType,
    ConfiguredTableAnalysisRuleTypeType,
    ConfiguredTableAssociationAnalysisRuleTypeType,
    CustomMLMemberAbilityType,
    DifferentialPrivacyAggregationTypeType,
    FilterableMemberStatusType,
    IdNamespaceTypeType,
    JoinOperatorType,
    MemberAbilityType,
    MembershipJobLogStatusType,
    MembershipQueryLogStatusType,
    MembershipStatusType,
    MemberStatusType,
    ParameterTypeType,
    PrivacyBudgetTemplateAutoRefreshType,
    ProtectedJobStatusType,
    ProtectedQueryStatusType,
    ResultFormatType,
    ScalarFunctionsType,
    SchemaStatusReasonCodeType,
    SchemaStatusType,
    SchemaTypeType,
    SelectedAnalysisMethodType,
    WorkerComputeTypeType,
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
    "AggregateColumnOutputTypeDef",
    "AggregateColumnTypeDef",
    "AggregationConstraintTypeDef",
    "AnalysisParameterTypeDef",
    "AnalysisRuleAggregationOutputTypeDef",
    "AnalysisRuleAggregationTypeDef",
    "AnalysisRuleCustomOutputTypeDef",
    "AnalysisRuleCustomTypeDef",
    "AnalysisRuleIdMappingTableTypeDef",
    "AnalysisRuleListOutputTypeDef",
    "AnalysisRuleListTypeDef",
    "AnalysisRulePolicyTypeDef",
    "AnalysisRulePolicyV1TypeDef",
    "AnalysisRuleTypeDef",
    "AnalysisSchemaOutputTypeDef",
    "AnalysisSchemaTypeDef",
    "AnalysisSchemaUnionTypeDef",
    "AnalysisSourceMetadataTypeDef",
    "AnalysisSourceOutputTypeDef",
    "AnalysisSourceTypeDef",
    "AnalysisSourceUnionTypeDef",
    "AnalysisTemplateArtifactMetadataTypeDef",
    "AnalysisTemplateArtifactTypeDef",
    "AnalysisTemplateArtifactsOutputTypeDef",
    "AnalysisTemplateArtifactsTypeDef",
    "AnalysisTemplateSummaryTypeDef",
    "AnalysisTemplateTypeDef",
    "AnalysisTemplateValidationStatusDetailTypeDef",
    "AnalysisTemplateValidationStatusReasonTypeDef",
    "AthenaTableReferenceTypeDef",
    "BatchGetCollaborationAnalysisTemplateErrorTypeDef",
    "BatchGetCollaborationAnalysisTemplateInputTypeDef",
    "BatchGetCollaborationAnalysisTemplateOutputTypeDef",
    "BatchGetSchemaAnalysisRuleErrorTypeDef",
    "BatchGetSchemaAnalysisRuleInputTypeDef",
    "BatchGetSchemaAnalysisRuleOutputTypeDef",
    "BatchGetSchemaErrorTypeDef",
    "BatchGetSchemaInputTypeDef",
    "BatchGetSchemaOutputTypeDef",
    "BilledJobResourceUtilizationTypeDef",
    "BilledResourceUtilizationTypeDef",
    "CollaborationAnalysisTemplateSummaryTypeDef",
    "CollaborationAnalysisTemplateTypeDef",
    "CollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    "CollaborationConfiguredAudienceModelAssociationTypeDef",
    "CollaborationIdNamespaceAssociationSummaryTypeDef",
    "CollaborationIdNamespaceAssociationTypeDef",
    "CollaborationPrivacyBudgetSummaryTypeDef",
    "CollaborationPrivacyBudgetTemplateSummaryTypeDef",
    "CollaborationPrivacyBudgetTemplateTypeDef",
    "CollaborationSummaryTypeDef",
    "CollaborationTypeDef",
    "ColumnTypeDef",
    "ComputeConfigurationTypeDef",
    "ConfigurationDetailsTypeDef",
    "ConfiguredAudienceModelAssociationSummaryTypeDef",
    "ConfiguredAudienceModelAssociationTypeDef",
    "ConfiguredTableAnalysisRulePolicyOutputTypeDef",
    "ConfiguredTableAnalysisRulePolicyTypeDef",
    "ConfiguredTableAnalysisRulePolicyUnionTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1OutputTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    "ConfiguredTableAnalysisRuleTypeDef",
    "ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleAggregationTypeDef",
    "ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleCustomTypeDef",
    "ConfiguredTableAssociationAnalysisRuleListOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleListTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef",
    "ConfiguredTableAssociationAnalysisRuleTypeDef",
    "ConfiguredTableAssociationSummaryTypeDef",
    "ConfiguredTableAssociationTypeDef",
    "ConfiguredTableSummaryTypeDef",
    "ConfiguredTableTypeDef",
    "ConsolidatedPolicyAggregationTypeDef",
    "ConsolidatedPolicyCustomTypeDef",
    "ConsolidatedPolicyListTypeDef",
    "ConsolidatedPolicyTypeDef",
    "ConsolidatedPolicyV1TypeDef",
    "CreateAnalysisTemplateInputTypeDef",
    "CreateAnalysisTemplateOutputTypeDef",
    "CreateCollaborationInputTypeDef",
    "CreateCollaborationOutputTypeDef",
    "CreateConfiguredAudienceModelAssociationInputTypeDef",
    "CreateConfiguredAudienceModelAssociationOutputTypeDef",
    "CreateConfiguredTableAnalysisRuleInputTypeDef",
    "CreateConfiguredTableAnalysisRuleOutputTypeDef",
    "CreateConfiguredTableAssociationAnalysisRuleInputTypeDef",
    "CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    "CreateConfiguredTableAssociationInputTypeDef",
    "CreateConfiguredTableAssociationOutputTypeDef",
    "CreateConfiguredTableInputTypeDef",
    "CreateConfiguredTableOutputTypeDef",
    "CreateIdMappingTableInputTypeDef",
    "CreateIdMappingTableOutputTypeDef",
    "CreateIdNamespaceAssociationInputTypeDef",
    "CreateIdNamespaceAssociationOutputTypeDef",
    "CreateMembershipInputTypeDef",
    "CreateMembershipOutputTypeDef",
    "CreatePrivacyBudgetTemplateInputTypeDef",
    "CreatePrivacyBudgetTemplateOutputTypeDef",
    "DataEncryptionMetadataTypeDef",
    "DeleteAnalysisTemplateInputTypeDef",
    "DeleteCollaborationInputTypeDef",
    "DeleteConfiguredAudienceModelAssociationInputTypeDef",
    "DeleteConfiguredTableAnalysisRuleInputTypeDef",
    "DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef",
    "DeleteConfiguredTableAssociationInputTypeDef",
    "DeleteConfiguredTableInputTypeDef",
    "DeleteIdMappingTableInputTypeDef",
    "DeleteIdNamespaceAssociationInputTypeDef",
    "DeleteMemberInputTypeDef",
    "DeleteMembershipInputTypeDef",
    "DeletePrivacyBudgetTemplateInputTypeDef",
    "DifferentialPrivacyColumnTypeDef",
    "DifferentialPrivacyConfigurationOutputTypeDef",
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
    "DirectAnalysisConfigurationDetailsTypeDef",
    "GetAnalysisTemplateInputTypeDef",
    "GetAnalysisTemplateOutputTypeDef",
    "GetCollaborationAnalysisTemplateInputTypeDef",
    "GetCollaborationAnalysisTemplateOutputTypeDef",
    "GetCollaborationConfiguredAudienceModelAssociationInputTypeDef",
    "GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef",
    "GetCollaborationIdNamespaceAssociationInputTypeDef",
    "GetCollaborationIdNamespaceAssociationOutputTypeDef",
    "GetCollaborationInputTypeDef",
    "GetCollaborationOutputTypeDef",
    "GetCollaborationPrivacyBudgetTemplateInputTypeDef",
    "GetCollaborationPrivacyBudgetTemplateOutputTypeDef",
    "GetConfiguredAudienceModelAssociationInputTypeDef",
    "GetConfiguredAudienceModelAssociationOutputTypeDef",
    "GetConfiguredTableAnalysisRuleInputTypeDef",
    "GetConfiguredTableAnalysisRuleOutputTypeDef",
    "GetConfiguredTableAssociationAnalysisRuleInputTypeDef",
    "GetConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    "GetConfiguredTableAssociationInputTypeDef",
    "GetConfiguredTableAssociationOutputTypeDef",
    "GetConfiguredTableInputTypeDef",
    "GetConfiguredTableOutputTypeDef",
    "GetIdMappingTableInputTypeDef",
    "GetIdMappingTableOutputTypeDef",
    "GetIdNamespaceAssociationInputTypeDef",
    "GetIdNamespaceAssociationOutputTypeDef",
    "GetMembershipInputTypeDef",
    "GetMembershipOutputTypeDef",
    "GetPrivacyBudgetTemplateInputTypeDef",
    "GetPrivacyBudgetTemplateOutputTypeDef",
    "GetProtectedJobInputTypeDef",
    "GetProtectedJobOutputTypeDef",
    "GetProtectedQueryInputTypeDef",
    "GetProtectedQueryOutputTypeDef",
    "GetSchemaAnalysisRuleInputTypeDef",
    "GetSchemaAnalysisRuleOutputTypeDef",
    "GetSchemaInputTypeDef",
    "GetSchemaOutputTypeDef",
    "GlueTableReferenceTypeDef",
    "HashTypeDef",
    "IdMappingConfigTypeDef",
    "IdMappingTableInputReferenceConfigTypeDef",
    "IdMappingTableInputReferencePropertiesTypeDef",
    "IdMappingTableInputSourceTypeDef",
    "IdMappingTableSchemaTypePropertiesTypeDef",
    "IdMappingTableSummaryTypeDef",
    "IdMappingTableTypeDef",
    "IdNamespaceAssociationInputReferenceConfigTypeDef",
    "IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef",
    "IdNamespaceAssociationInputReferencePropertiesTypeDef",
    "IdNamespaceAssociationSummaryTypeDef",
    "IdNamespaceAssociationTypeDef",
    "JobComputePaymentConfigTypeDef",
    "ListAnalysisTemplatesInputPaginateTypeDef",
    "ListAnalysisTemplatesInputTypeDef",
    "ListAnalysisTemplatesOutputTypeDef",
    "ListCollaborationAnalysisTemplatesInputPaginateTypeDef",
    "ListCollaborationAnalysisTemplatesInputTypeDef",
    "ListCollaborationAnalysisTemplatesOutputTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef",
    "ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef",
    "ListCollaborationIdNamespaceAssociationsInputTypeDef",
    "ListCollaborationIdNamespaceAssociationsOutputTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesInputTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesOutputTypeDef",
    "ListCollaborationPrivacyBudgetsInputPaginateTypeDef",
    "ListCollaborationPrivacyBudgetsInputTypeDef",
    "ListCollaborationPrivacyBudgetsOutputTypeDef",
    "ListCollaborationsInputPaginateTypeDef",
    "ListCollaborationsInputTypeDef",
    "ListCollaborationsOutputTypeDef",
    "ListConfiguredAudienceModelAssociationsInputPaginateTypeDef",
    "ListConfiguredAudienceModelAssociationsInputTypeDef",
    "ListConfiguredAudienceModelAssociationsOutputTypeDef",
    "ListConfiguredTableAssociationsInputPaginateTypeDef",
    "ListConfiguredTableAssociationsInputTypeDef",
    "ListConfiguredTableAssociationsOutputTypeDef",
    "ListConfiguredTablesInputPaginateTypeDef",
    "ListConfiguredTablesInputTypeDef",
    "ListConfiguredTablesOutputTypeDef",
    "ListIdMappingTablesInputPaginateTypeDef",
    "ListIdMappingTablesInputTypeDef",
    "ListIdMappingTablesOutputTypeDef",
    "ListIdNamespaceAssociationsInputPaginateTypeDef",
    "ListIdNamespaceAssociationsInputTypeDef",
    "ListIdNamespaceAssociationsOutputTypeDef",
    "ListMembersInputPaginateTypeDef",
    "ListMembersInputTypeDef",
    "ListMembersOutputTypeDef",
    "ListMembershipsInputPaginateTypeDef",
    "ListMembershipsInputTypeDef",
    "ListMembershipsOutputTypeDef",
    "ListPrivacyBudgetTemplatesInputPaginateTypeDef",
    "ListPrivacyBudgetTemplatesInputTypeDef",
    "ListPrivacyBudgetTemplatesOutputTypeDef",
    "ListPrivacyBudgetsInputPaginateTypeDef",
    "ListPrivacyBudgetsInputTypeDef",
    "ListPrivacyBudgetsOutputTypeDef",
    "ListProtectedJobsInputPaginateTypeDef",
    "ListProtectedJobsInputTypeDef",
    "ListProtectedJobsOutputTypeDef",
    "ListProtectedQueriesInputPaginateTypeDef",
    "ListProtectedQueriesInputTypeDef",
    "ListProtectedQueriesOutputTypeDef",
    "ListSchemasInputPaginateTypeDef",
    "ListSchemasInputTypeDef",
    "ListSchemasOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MLMemberAbilitiesOutputTypeDef",
    "MLMemberAbilitiesTypeDef",
    "MLMemberAbilitiesUnionTypeDef",
    "MLPaymentConfigTypeDef",
    "MemberSpecificationTypeDef",
    "MemberSummaryTypeDef",
    "MembershipJobComputePaymentConfigTypeDef",
    "MembershipMLPaymentConfigTypeDef",
    "MembershipModelInferencePaymentConfigTypeDef",
    "MembershipModelTrainingPaymentConfigTypeDef",
    "MembershipPaymentConfigurationTypeDef",
    "MembershipProtectedJobOutputConfigurationTypeDef",
    "MembershipProtectedJobResultConfigurationTypeDef",
    "MembershipProtectedQueryOutputConfigurationTypeDef",
    "MembershipProtectedQueryResultConfigurationTypeDef",
    "MembershipQueryComputePaymentConfigTypeDef",
    "MembershipSummaryTypeDef",
    "MembershipTypeDef",
    "ModelInferencePaymentConfigTypeDef",
    "ModelTrainingPaymentConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PaymentConfigurationTypeDef",
    "PopulateIdMappingTableInputTypeDef",
    "PopulateIdMappingTableOutputTypeDef",
    "PreviewPrivacyImpactInputTypeDef",
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
    "ProtectedJobConfigurationDetailsTypeDef",
    "ProtectedJobDirectAnalysisConfigurationDetailsTypeDef",
    "ProtectedJobErrorTypeDef",
    "ProtectedJobMemberOutputConfigurationInputTypeDef",
    "ProtectedJobMemberOutputConfigurationOutputTypeDef",
    "ProtectedJobOutputConfigurationInputTypeDef",
    "ProtectedJobOutputConfigurationOutputTypeDef",
    "ProtectedJobOutputTypeDef",
    "ProtectedJobParametersTypeDef",
    "ProtectedJobReceiverConfigurationTypeDef",
    "ProtectedJobResultConfigurationInputTypeDef",
    "ProtectedJobResultConfigurationOutputTypeDef",
    "ProtectedJobResultTypeDef",
    "ProtectedJobS3OutputConfigurationInputTypeDef",
    "ProtectedJobS3OutputConfigurationOutputTypeDef",
    "ProtectedJobS3OutputTypeDef",
    "ProtectedJobSingleMemberOutputTypeDef",
    "ProtectedJobStatisticsTypeDef",
    "ProtectedJobSummaryTypeDef",
    "ProtectedJobTypeDef",
    "ProtectedQueryDistributeOutputConfigurationLocationTypeDef",
    "ProtectedQueryDistributeOutputConfigurationOutputTypeDef",
    "ProtectedQueryDistributeOutputConfigurationTypeDef",
    "ProtectedQueryDistributeOutputTypeDef",
    "ProtectedQueryErrorTypeDef",
    "ProtectedQueryMemberOutputConfigurationTypeDef",
    "ProtectedQueryOutputConfigurationOutputTypeDef",
    "ProtectedQueryOutputConfigurationTypeDef",
    "ProtectedQueryOutputTypeDef",
    "ProtectedQueryResultConfigurationOutputTypeDef",
    "ProtectedQueryResultConfigurationTypeDef",
    "ProtectedQueryResultConfigurationUnionTypeDef",
    "ProtectedQueryResultTypeDef",
    "ProtectedQueryS3OutputConfigurationTypeDef",
    "ProtectedQueryS3OutputTypeDef",
    "ProtectedQuerySQLParametersOutputTypeDef",
    "ProtectedQuerySQLParametersTypeDef",
    "ProtectedQuerySQLParametersUnionTypeDef",
    "ProtectedQuerySingleMemberOutputTypeDef",
    "ProtectedQueryStatisticsTypeDef",
    "ProtectedQuerySummaryTypeDef",
    "ProtectedQueryTypeDef",
    "QueryComputePaymentConfigTypeDef",
    "QueryConstraintRequireOverlapTypeDef",
    "QueryConstraintTypeDef",
    "ReceiverConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SchemaAnalysisRuleRequestTypeDef",
    "SchemaStatusDetailTypeDef",
    "SchemaStatusReasonTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaTypeDef",
    "SchemaTypePropertiesTypeDef",
    "SnowflakeTableReferenceOutputTypeDef",
    "SnowflakeTableReferenceTypeDef",
    "SnowflakeTableSchemaOutputTypeDef",
    "SnowflakeTableSchemaTypeDef",
    "SnowflakeTableSchemaV1TypeDef",
    "StartProtectedJobInputTypeDef",
    "StartProtectedJobOutputTypeDef",
    "StartProtectedQueryInputTypeDef",
    "StartProtectedQueryOutputTypeDef",
    "TableReferenceOutputTypeDef",
    "TableReferenceTypeDef",
    "TableReferenceUnionTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateAnalysisTemplateInputTypeDef",
    "UpdateAnalysisTemplateOutputTypeDef",
    "UpdateCollaborationInputTypeDef",
    "UpdateCollaborationOutputTypeDef",
    "UpdateConfiguredAudienceModelAssociationInputTypeDef",
    "UpdateConfiguredAudienceModelAssociationOutputTypeDef",
    "UpdateConfiguredTableAnalysisRuleInputTypeDef",
    "UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    "UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef",
    "UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    "UpdateConfiguredTableAssociationInputTypeDef",
    "UpdateConfiguredTableAssociationOutputTypeDef",
    "UpdateConfiguredTableInputTypeDef",
    "UpdateConfiguredTableOutputTypeDef",
    "UpdateIdMappingTableInputTypeDef",
    "UpdateIdMappingTableOutputTypeDef",
    "UpdateIdNamespaceAssociationInputTypeDef",
    "UpdateIdNamespaceAssociationOutputTypeDef",
    "UpdateMembershipInputTypeDef",
    "UpdateMembershipOutputTypeDef",
    "UpdatePrivacyBudgetTemplateInputTypeDef",
    "UpdatePrivacyBudgetTemplateOutputTypeDef",
    "UpdateProtectedJobInputTypeDef",
    "UpdateProtectedJobOutputTypeDef",
    "UpdateProtectedQueryInputTypeDef",
    "UpdateProtectedQueryOutputTypeDef",
    "WorkerComputeConfigurationTypeDef",
)

class AggregateColumnOutputTypeDef(TypedDict):
    columnNames: List[str]
    function: AggregateFunctionNameType

class AggregateColumnTypeDef(TypedDict):
    columnNames: Sequence[str]
    function: AggregateFunctionNameType

AggregationConstraintTypeDef = TypedDict(
    "AggregationConstraintTypeDef",
    {
        "columnName": str,
        "minimum": int,
        "type": Literal["COUNT_DISTINCT"],
    },
)
AnalysisParameterTypeDef = TypedDict(
    "AnalysisParameterTypeDef",
    {
        "name": str,
        "type": ParameterTypeType,
        "defaultValue": NotRequired[str],
    },
)

class AnalysisRuleListOutputTypeDef(TypedDict):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: NotRequired[List[JoinOperatorType]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]

class AnalysisRuleListTypeDef(TypedDict):
    joinColumns: Sequence[str]
    listColumns: Sequence[str]
    allowedJoinOperators: NotRequired[Sequence[JoinOperatorType]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]

class AnalysisSchemaOutputTypeDef(TypedDict):
    referencedTables: NotRequired[List[str]]

class AnalysisSchemaTypeDef(TypedDict):
    referencedTables: NotRequired[Sequence[str]]

class HashTypeDef(TypedDict):
    sha256: NotRequired[str]

class S3LocationTypeDef(TypedDict):
    bucket: str
    key: str

AnalysisTemplateSummaryTypeDef = TypedDict(
    "AnalysisTemplateSummaryTypeDef",
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
        "description": NotRequired[str],
    },
)

class AnalysisTemplateValidationStatusReasonTypeDef(TypedDict):
    message: str

class AthenaTableReferenceTypeDef(TypedDict):
    workGroup: str
    databaseName: str
    tableName: str
    outputLocation: NotRequired[str]

class BatchGetCollaborationAnalysisTemplateErrorTypeDef(TypedDict):
    arn: str
    code: str
    message: str

class BatchGetCollaborationAnalysisTemplateInputTypeDef(TypedDict):
    collaborationIdentifier: str
    analysisTemplateArns: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

BatchGetSchemaAnalysisRuleErrorTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleErrorTypeDef",
    {
        "name": str,
        "type": AnalysisRuleTypeType,
        "code": str,
        "message": str,
    },
)
SchemaAnalysisRuleRequestTypeDef = TypedDict(
    "SchemaAnalysisRuleRequestTypeDef",
    {
        "name": str,
        "type": AnalysisRuleTypeType,
    },
)

class BatchGetSchemaErrorTypeDef(TypedDict):
    name: str
    code: str
    message: str

class BatchGetSchemaInputTypeDef(TypedDict):
    collaborationIdentifier: str
    names: Sequence[str]

class BilledJobResourceUtilizationTypeDef(TypedDict):
    units: float

class BilledResourceUtilizationTypeDef(TypedDict):
    units: float

CollaborationAnalysisTemplateSummaryTypeDef = TypedDict(
    "CollaborationAnalysisTemplateSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
        "description": NotRequired[str],
    },
)
CollaborationConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "CollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
        "description": NotRequired[str],
    },
)
CollaborationConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "CollaborationConfiguredAudienceModelAssociationTypeDef",
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
        "description": NotRequired[str],
    },
)

class IdNamespaceAssociationInputReferenceConfigTypeDef(TypedDict):
    inputReferenceArn: str
    manageResourcePolicies: bool

class IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef(TypedDict):
    idNamespaceType: IdNamespaceTypeType

class IdMappingConfigTypeDef(TypedDict):
    allowUseAsDimensionColumn: bool

class IdNamespaceAssociationInputReferencePropertiesTypeDef(TypedDict):
    idNamespaceType: IdNamespaceTypeType
    idMappingWorkflowsSupported: List[Dict[str, Any]]

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
CollaborationSummaryTypeDef = TypedDict(
    "CollaborationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "creatorAccountId": str,
        "creatorDisplayName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "memberStatus": MemberStatusType,
        "membershipId": NotRequired[str],
        "membershipArn": NotRequired[str],
        "analyticsEngine": NotRequired[AnalyticsEngineType],
    },
)

class DataEncryptionMetadataTypeDef(TypedDict):
    allowCleartext: bool
    allowDuplicates: bool
    allowJoinsOnColumnsWithDifferentNames: bool
    preserveNulls: bool

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)
WorkerComputeConfigurationTypeDef = TypedDict(
    "WorkerComputeConfigurationTypeDef",
    {
        "type": NotRequired[WorkerComputeTypeType],
        "number": NotRequired[int],
    },
)

class DirectAnalysisConfigurationDetailsTypeDef(TypedDict):
    receiverAccountIds: NotRequired[List[str]]

ConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "ConfiguredAudienceModelAssociationSummaryTypeDef",
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
        "description": NotRequired[str],
    },
)
ConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "ConfiguredAudienceModelAssociationTypeDef",
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
        "description": NotRequired[str],
    },
)

class ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef(TypedDict):
    allowedResultReceivers: NotRequired[List[str]]
    allowedAdditionalAnalyses: NotRequired[List[str]]

class ConfiguredTableAssociationAnalysisRuleAggregationTypeDef(TypedDict):
    allowedResultReceivers: NotRequired[Sequence[str]]
    allowedAdditionalAnalyses: NotRequired[Sequence[str]]

class ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef(TypedDict):
    allowedResultReceivers: NotRequired[List[str]]
    allowedAdditionalAnalyses: NotRequired[List[str]]

class ConfiguredTableAssociationAnalysisRuleCustomTypeDef(TypedDict):
    allowedResultReceivers: NotRequired[Sequence[str]]
    allowedAdditionalAnalyses: NotRequired[Sequence[str]]

class ConfiguredTableAssociationAnalysisRuleListOutputTypeDef(TypedDict):
    allowedResultReceivers: NotRequired[List[str]]
    allowedAdditionalAnalyses: NotRequired[List[str]]

class ConfiguredTableAssociationAnalysisRuleListTypeDef(TypedDict):
    allowedResultReceivers: NotRequired[Sequence[str]]
    allowedAdditionalAnalyses: NotRequired[Sequence[str]]

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
        "analysisRuleTypes": NotRequired[List[ConfiguredTableAssociationAnalysisRuleTypeType]],
    },
)
ConfiguredTableAssociationTypeDef = TypedDict(
    "ConfiguredTableAssociationTypeDef",
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
        "description": NotRequired[str],
        "analysisRuleTypes": NotRequired[List[ConfiguredTableAssociationAnalysisRuleTypeType]],
    },
)
ConfiguredTableSummaryTypeDef = TypedDict(
    "ConfiguredTableSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "analysisRuleTypes": List[ConfiguredTableAnalysisRuleTypeType],
        "analysisMethod": AnalysisMethodType,
        "selectedAnalysisMethods": NotRequired[List[SelectedAnalysisMethodType]],
    },
)

class ConsolidatedPolicyListTypeDef(TypedDict):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: NotRequired[List[JoinOperatorType]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]
    allowedResultReceivers: NotRequired[List[str]]
    allowedAdditionalAnalyses: NotRequired[List[str]]

class CreateConfiguredAudienceModelAssociationInputTypeDef(TypedDict):
    membershipIdentifier: str
    configuredAudienceModelArn: str
    configuredAudienceModelAssociationName: str
    manageResourcePolicies: bool
    tags: NotRequired[Mapping[str, str]]
    description: NotRequired[str]

class CreateConfiguredTableAssociationInputTypeDef(TypedDict):
    name: str
    membershipIdentifier: str
    configuredTableIdentifier: str
    roleArn: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class IdMappingTableInputReferenceConfigTypeDef(TypedDict):
    inputReferenceArn: str
    manageResourcePolicies: bool

class DeleteAnalysisTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    analysisTemplateIdentifier: str

class DeleteCollaborationInputTypeDef(TypedDict):
    collaborationIdentifier: str

class DeleteConfiguredAudienceModelAssociationInputTypeDef(TypedDict):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str

class DeleteConfiguredTableAnalysisRuleInputTypeDef(TypedDict):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType

class DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef(TypedDict):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType

class DeleteConfiguredTableAssociationInputTypeDef(TypedDict):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str

class DeleteConfiguredTableInputTypeDef(TypedDict):
    configuredTableIdentifier: str

class DeleteIdMappingTableInputTypeDef(TypedDict):
    idMappingTableIdentifier: str
    membershipIdentifier: str

class DeleteIdNamespaceAssociationInputTypeDef(TypedDict):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str

class DeleteMemberInputTypeDef(TypedDict):
    collaborationIdentifier: str
    accountId: str

class DeleteMembershipInputTypeDef(TypedDict):
    membershipIdentifier: str

class DeletePrivacyBudgetTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str

class DifferentialPrivacyColumnTypeDef(TypedDict):
    name: str

class DifferentialPrivacySensitivityParametersTypeDef(TypedDict):
    aggregationType: DifferentialPrivacyAggregationTypeType
    aggregationExpression: str
    userContributionLimit: int
    minColumnValue: NotRequired[float]
    maxColumnValue: NotRequired[float]

DifferentialPrivacyPreviewAggregationTypeDef = TypedDict(
    "DifferentialPrivacyPreviewAggregationTypeDef",
    {
        "type": DifferentialPrivacyAggregationTypeType,
        "maxCount": int,
    },
)

class DifferentialPrivacyPreviewParametersInputTypeDef(TypedDict):
    epsilon: int
    usersNoisePerQuery: int

DifferentialPrivacyPrivacyBudgetAggregationTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyBudgetAggregationTypeDef",
    {
        "type": DifferentialPrivacyAggregationTypeType,
        "maxCount": int,
        "remainingCount": int,
    },
)

class DifferentialPrivacyTemplateParametersInputTypeDef(TypedDict):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyTemplateParametersOutputTypeDef(TypedDict):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyTemplateUpdateParametersTypeDef(TypedDict):
    epsilon: NotRequired[int]
    usersNoisePerQuery: NotRequired[int]

class GetAnalysisTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    analysisTemplateIdentifier: str

class GetCollaborationAnalysisTemplateInputTypeDef(TypedDict):
    collaborationIdentifier: str
    analysisTemplateArn: str

class GetCollaborationConfiguredAudienceModelAssociationInputTypeDef(TypedDict):
    collaborationIdentifier: str
    configuredAudienceModelAssociationIdentifier: str

class GetCollaborationIdNamespaceAssociationInputTypeDef(TypedDict):
    collaborationIdentifier: str
    idNamespaceAssociationIdentifier: str

class GetCollaborationInputTypeDef(TypedDict):
    collaborationIdentifier: str

class GetCollaborationPrivacyBudgetTemplateInputTypeDef(TypedDict):
    collaborationIdentifier: str
    privacyBudgetTemplateIdentifier: str

class GetConfiguredAudienceModelAssociationInputTypeDef(TypedDict):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str

class GetConfiguredTableAnalysisRuleInputTypeDef(TypedDict):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType

class GetConfiguredTableAssociationAnalysisRuleInputTypeDef(TypedDict):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType

class GetConfiguredTableAssociationInputTypeDef(TypedDict):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str

class GetConfiguredTableInputTypeDef(TypedDict):
    configuredTableIdentifier: str

class GetIdMappingTableInputTypeDef(TypedDict):
    idMappingTableIdentifier: str
    membershipIdentifier: str

class GetIdNamespaceAssociationInputTypeDef(TypedDict):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str

class GetMembershipInputTypeDef(TypedDict):
    membershipIdentifier: str

class GetPrivacyBudgetTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str

class GetProtectedJobInputTypeDef(TypedDict):
    membershipIdentifier: str
    protectedJobIdentifier: str

class GetProtectedQueryInputTypeDef(TypedDict):
    membershipIdentifier: str
    protectedQueryIdentifier: str

GetSchemaAnalysisRuleInputTypeDef = TypedDict(
    "GetSchemaAnalysisRuleInputTypeDef",
    {
        "collaborationIdentifier": str,
        "name": str,
        "type": AnalysisRuleTypeType,
    },
)

class GetSchemaInputTypeDef(TypedDict):
    collaborationIdentifier: str
    name: str

class GlueTableReferenceTypeDef(TypedDict):
    tableName: str
    databaseName: str

IdMappingTableInputSourceTypeDef = TypedDict(
    "IdMappingTableInputSourceTypeDef",
    {
        "idNamespaceAssociationId": str,
        "type": IdNamespaceTypeType,
    },
)

class JobComputePaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAnalysisTemplatesInputTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationAnalysisTemplatesInputTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationIdNamespaceAssociationsInputTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationPrivacyBudgetTemplatesInputTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationPrivacyBudgetsInputTypeDef(TypedDict):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCollaborationsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    memberStatus: NotRequired[FilterableMemberStatusType]

class ListConfiguredAudienceModelAssociationsInputTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListConfiguredTableAssociationsInputTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListConfiguredTablesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListIdMappingTablesInputTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListIdNamespaceAssociationsInputTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMembersInputTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMembershipsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    status: NotRequired[MembershipStatusType]

class ListPrivacyBudgetTemplatesInputTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

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

class ListPrivacyBudgetsInputTypeDef(TypedDict):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListProtectedJobsInputTypeDef(TypedDict):
    membershipIdentifier: str
    status: NotRequired[ProtectedJobStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListProtectedQueriesInputTypeDef(TypedDict):
    membershipIdentifier: str
    status: NotRequired[ProtectedQueryStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSchemasInputTypeDef(TypedDict):
    collaborationIdentifier: str
    schemaType: NotRequired[SchemaTypeType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "name": str,
        "type": SchemaTypeType,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "collaborationId": str,
        "collaborationArn": str,
        "analysisRuleTypes": List[AnalysisRuleTypeType],
        "analysisMethod": NotRequired[AnalysisMethodType],
        "selectedAnalysisMethods": NotRequired[List[SelectedAnalysisMethodType]],
    },
)

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class MLMemberAbilitiesOutputTypeDef(TypedDict):
    customMLMemberAbilities: List[CustomMLMemberAbilityType]

class MLMemberAbilitiesTypeDef(TypedDict):
    customMLMemberAbilities: Sequence[CustomMLMemberAbilityType]

class ModelInferencePaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class ModelTrainingPaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class MembershipJobComputePaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class MembershipModelInferencePaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class MembershipModelTrainingPaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class MembershipQueryComputePaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class ProtectedJobS3OutputConfigurationInputTypeDef(TypedDict):
    bucket: str
    keyPrefix: NotRequired[str]

class ProtectedQueryS3OutputConfigurationTypeDef(TypedDict):
    resultFormat: ResultFormatType
    bucket: str
    keyPrefix: NotRequired[str]
    singleFileOutput: NotRequired[bool]

class QueryComputePaymentConfigTypeDef(TypedDict):
    isResponsible: bool

class PopulateIdMappingTableInputTypeDef(TypedDict):
    idMappingTableIdentifier: str
    membershipIdentifier: str

class ProtectedJobDirectAnalysisConfigurationDetailsTypeDef(TypedDict):
    receiverAccountIds: NotRequired[List[str]]

class ProtectedJobErrorTypeDef(TypedDict):
    message: str
    code: str

class ProtectedJobMemberOutputConfigurationInputTypeDef(TypedDict):
    accountId: str

class ProtectedJobMemberOutputConfigurationOutputTypeDef(TypedDict):
    accountId: str

class ProtectedJobS3OutputConfigurationOutputTypeDef(TypedDict):
    bucket: str
    keyPrefix: NotRequired[str]

class ProtectedJobS3OutputTypeDef(TypedDict):
    location: str

class ProtectedJobSingleMemberOutputTypeDef(TypedDict):
    accountId: str

class ProtectedJobParametersTypeDef(TypedDict):
    analysisTemplateArn: NotRequired[str]

class ProtectedQueryMemberOutputConfigurationTypeDef(TypedDict):
    accountId: str

class ProtectedQueryS3OutputTypeDef(TypedDict):
    location: str

class ProtectedQuerySingleMemberOutputTypeDef(TypedDict):
    accountId: str

class ProtectedQueryErrorTypeDef(TypedDict):
    message: str
    code: str

class ProtectedQuerySQLParametersOutputTypeDef(TypedDict):
    queryString: NotRequired[str]
    analysisTemplateArn: NotRequired[str]
    parameters: NotRequired[Dict[str, str]]

class ProtectedQuerySQLParametersTypeDef(TypedDict):
    queryString: NotRequired[str]
    analysisTemplateArn: NotRequired[str]
    parameters: NotRequired[Mapping[str, str]]

class QueryConstraintRequireOverlapTypeDef(TypedDict):
    columns: NotRequired[List[str]]

class SchemaStatusReasonTypeDef(TypedDict):
    code: SchemaStatusReasonCodeType
    message: str

class SnowflakeTableSchemaV1TypeDef(TypedDict):
    columnName: str
    columnType: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAnalysisTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    analysisTemplateIdentifier: str
    description: NotRequired[str]

class UpdateCollaborationInputTypeDef(TypedDict):
    collaborationIdentifier: str
    name: NotRequired[str]
    description: NotRequired[str]
    analyticsEngine: NotRequired[AnalyticsEngineType]

class UpdateConfiguredAudienceModelAssociationInputTypeDef(TypedDict):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str
    description: NotRequired[str]
    name: NotRequired[str]

class UpdateConfiguredTableAssociationInputTypeDef(TypedDict):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str
    description: NotRequired[str]
    roleArn: NotRequired[str]

class UpdateConfiguredTableInputTypeDef(TypedDict):
    configuredTableIdentifier: str
    name: NotRequired[str]
    description: NotRequired[str]
    analysisMethod: NotRequired[AnalysisMethodType]
    selectedAnalysisMethods: NotRequired[Sequence[SelectedAnalysisMethodType]]

class UpdateIdMappingTableInputTypeDef(TypedDict):
    idMappingTableIdentifier: str
    membershipIdentifier: str
    description: NotRequired[str]
    kmsKeyArn: NotRequired[str]

class UpdateProtectedJobInputTypeDef(TypedDict):
    membershipIdentifier: str
    protectedJobIdentifier: str
    targetStatus: Literal["CANCELLED"]

class UpdateProtectedQueryInputTypeDef(TypedDict):
    membershipIdentifier: str
    protectedQueryIdentifier: str
    targetStatus: Literal["CANCELLED"]

class AnalysisRuleAggregationOutputTypeDef(TypedDict):
    aggregateColumns: List[AggregateColumnOutputTypeDef]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraintTypeDef]
    joinRequired: NotRequired[Literal["QUERY_RUNNER"]]
    allowedJoinOperators: NotRequired[List[JoinOperatorType]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]

class AnalysisRuleAggregationTypeDef(TypedDict):
    aggregateColumns: Sequence[AggregateColumnTypeDef]
    joinColumns: Sequence[str]
    dimensionColumns: Sequence[str]
    scalarFunctions: Sequence[ScalarFunctionsType]
    outputConstraints: Sequence[AggregationConstraintTypeDef]
    joinRequired: NotRequired[Literal["QUERY_RUNNER"]]
    allowedJoinOperators: NotRequired[Sequence[JoinOperatorType]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]

class ConsolidatedPolicyAggregationTypeDef(TypedDict):
    aggregateColumns: List[AggregateColumnOutputTypeDef]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraintTypeDef]
    joinRequired: NotRequired[Literal["QUERY_RUNNER"]]
    allowedJoinOperators: NotRequired[List[JoinOperatorType]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]
    allowedResultReceivers: NotRequired[List[str]]
    allowedAdditionalAnalyses: NotRequired[List[str]]

AnalysisSchemaUnionTypeDef = Union[AnalysisSchemaTypeDef, AnalysisSchemaOutputTypeDef]

class AnalysisTemplateArtifactMetadataTypeDef(TypedDict):
    entryPointHash: HashTypeDef
    additionalArtifactHashes: NotRequired[List[HashTypeDef]]

class AnalysisTemplateArtifactTypeDef(TypedDict):
    location: S3LocationTypeDef

AnalysisTemplateValidationStatusDetailTypeDef = TypedDict(
    "AnalysisTemplateValidationStatusDetailTypeDef",
    {
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "status": AnalysisTemplateValidationStatusType,
        "reasons": NotRequired[List[AnalysisTemplateValidationStatusReasonTypeDef]],
    },
)

class ListAnalysisTemplatesOutputTypeDef(TypedDict):
    analysisTemplateSummaries: List[AnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PopulateIdMappingTableOutputTypeDef(TypedDict):
    idMappingJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetSchemaAnalysisRuleInputTypeDef(TypedDict):
    collaborationIdentifier: str
    schemaAnalysisRuleRequests: Sequence[SchemaAnalysisRuleRequestTypeDef]

class ProtectedJobStatisticsTypeDef(TypedDict):
    totalDurationInMillis: NotRequired[int]
    billedResourceUtilization: NotRequired[BilledJobResourceUtilizationTypeDef]

class ProtectedQueryStatisticsTypeDef(TypedDict):
    totalDurationInMillis: NotRequired[int]
    billedResourceUtilization: NotRequired[BilledResourceUtilizationTypeDef]

class ListCollaborationAnalysisTemplatesOutputTypeDef(TypedDict):
    collaborationAnalysisTemplateSummaries: List[CollaborationAnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef(TypedDict):
    collaborationConfiguredAudienceModelAssociationSummaries: List[
        CollaborationConfiguredAudienceModelAssociationSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef(TypedDict):
    collaborationConfiguredAudienceModelAssociation: (
        CollaborationConfiguredAudienceModelAssociationTypeDef
    )
    ResponseMetadata: ResponseMetadataTypeDef

CollaborationIdNamespaceAssociationSummaryTypeDef = TypedDict(
    "CollaborationIdNamespaceAssociationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "name": str,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef,
        "description": NotRequired[str],
    },
)
IdNamespaceAssociationSummaryTypeDef = TypedDict(
    "IdNamespaceAssociationSummaryTypeDef",
    {
        "membershipId": str,
        "membershipArn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "name": str,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef,
        "description": NotRequired[str],
    },
)

class CreateIdNamespaceAssociationInputTypeDef(TypedDict):
    membershipIdentifier: str
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfigTypeDef
    name: str
    tags: NotRequired[Mapping[str, str]]
    description: NotRequired[str]
    idMappingConfig: NotRequired[IdMappingConfigTypeDef]

class UpdateIdNamespaceAssociationInputTypeDef(TypedDict):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str
    name: NotRequired[str]
    description: NotRequired[str]
    idMappingConfig: NotRequired[IdMappingConfigTypeDef]

CollaborationIdNamespaceAssociationTypeDef = TypedDict(
    "CollaborationIdNamespaceAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesTypeDef,
        "description": NotRequired[str],
        "idMappingConfig": NotRequired[IdMappingConfigTypeDef],
    },
)
IdNamespaceAssociationTypeDef = TypedDict(
    "IdNamespaceAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesTypeDef,
        "description": NotRequired[str],
        "idMappingConfig": NotRequired[IdMappingConfigTypeDef],
    },
)

class ListCollaborationPrivacyBudgetTemplatesOutputTypeDef(TypedDict):
    collaborationPrivacyBudgetTemplateSummaries: List[
        CollaborationPrivacyBudgetTemplateSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCollaborationsOutputTypeDef(TypedDict):
    collaborationList: List[CollaborationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CollaborationTypeDef = TypedDict(
    "CollaborationTypeDef",
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
        "description": NotRequired[str],
        "membershipId": NotRequired[str],
        "membershipArn": NotRequired[str],
        "dataEncryptionMetadata": NotRequired[DataEncryptionMetadataTypeDef],
        "jobLogStatus": NotRequired[CollaborationJobLogStatusType],
        "analyticsEngine": NotRequired[AnalyticsEngineType],
    },
)

class ComputeConfigurationTypeDef(TypedDict):
    worker: NotRequired[WorkerComputeConfigurationTypeDef]

class ConfigurationDetailsTypeDef(TypedDict):
    directAnalysisConfigurationDetails: NotRequired[DirectAnalysisConfigurationDetailsTypeDef]

class ListConfiguredAudienceModelAssociationsOutputTypeDef(TypedDict):
    configuredAudienceModelAssociationSummaries: List[
        ConfiguredAudienceModelAssociationSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateConfiguredAudienceModelAssociationOutputTypeDef(TypedDict):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredAudienceModelAssociationOutputTypeDef(TypedDict):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelAssociationOutputTypeDef(TypedDict):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef",
    {
        "list": NotRequired[ConfiguredTableAssociationAnalysisRuleListOutputTypeDef],
        "aggregation": NotRequired[ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef],
        "custom": NotRequired[ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef],
    },
)
ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef",
    {
        "list": NotRequired[ConfiguredTableAssociationAnalysisRuleListTypeDef],
        "aggregation": NotRequired[ConfiguredTableAssociationAnalysisRuleAggregationTypeDef],
        "custom": NotRequired[ConfiguredTableAssociationAnalysisRuleCustomTypeDef],
    },
)

class ListConfiguredTableAssociationsOutputTypeDef(TypedDict):
    configuredTableAssociationSummaries: List[ConfiguredTableAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateConfiguredTableAssociationOutputTypeDef(TypedDict):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAssociationOutputTypeDef(TypedDict):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAssociationOutputTypeDef(TypedDict):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfiguredTablesOutputTypeDef(TypedDict):
    configuredTableSummaries: List[ConfiguredTableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateIdMappingTableInputTypeDef(TypedDict):
    membershipIdentifier: str
    name: str
    inputReferenceConfig: IdMappingTableInputReferenceConfigTypeDef
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    kmsKeyArn: NotRequired[str]

IdMappingTableSummaryTypeDef = TypedDict(
    "IdMappingTableSummaryTypeDef",
    {
        "collaborationArn": str,
        "collaborationId": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
        "inputReferenceConfig": IdMappingTableInputReferenceConfigTypeDef,
        "name": str,
        "description": NotRequired[str],
    },
)

class DifferentialPrivacyConfigurationOutputTypeDef(TypedDict):
    columns: List[DifferentialPrivacyColumnTypeDef]

class DifferentialPrivacyConfigurationTypeDef(TypedDict):
    columns: Sequence[DifferentialPrivacyColumnTypeDef]

class DifferentialPrivacyParametersTypeDef(TypedDict):
    sensitivityParameters: List[DifferentialPrivacySensitivityParametersTypeDef]

class DifferentialPrivacyPrivacyImpactTypeDef(TypedDict):
    aggregations: List[DifferentialPrivacyPreviewAggregationTypeDef]

class PreviewPrivacyImpactParametersInputTypeDef(TypedDict):
    differentialPrivacy: NotRequired[DifferentialPrivacyPreviewParametersInputTypeDef]

class DifferentialPrivacyPrivacyBudgetTypeDef(TypedDict):
    aggregations: List[DifferentialPrivacyPrivacyBudgetAggregationTypeDef]
    epsilon: int

class PrivacyBudgetTemplateParametersInputTypeDef(TypedDict):
    differentialPrivacy: NotRequired[DifferentialPrivacyTemplateParametersInputTypeDef]

class PrivacyBudgetTemplateParametersOutputTypeDef(TypedDict):
    differentialPrivacy: NotRequired[DifferentialPrivacyTemplateParametersOutputTypeDef]

class PrivacyBudgetTemplateUpdateParametersTypeDef(TypedDict):
    differentialPrivacy: NotRequired[DifferentialPrivacyTemplateUpdateParametersTypeDef]

class IdMappingTableInputReferencePropertiesTypeDef(TypedDict):
    idMappingTableInputSource: List[IdMappingTableInputSourceTypeDef]

class IdMappingTableSchemaTypePropertiesTypeDef(TypedDict):
    idMappingTableInputSource: List[IdMappingTableInputSourceTypeDef]

class ListAnalysisTemplatesInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationAnalysisTemplatesInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationPrivacyBudgetsInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationsInputPaginateTypeDef(TypedDict):
    memberStatus: NotRequired[FilterableMemberStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfiguredAudienceModelAssociationsInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfiguredTableAssociationsInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfiguredTablesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdMappingTablesInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdNamespaceAssociationsInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembersInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembershipsInputPaginateTypeDef(TypedDict):
    status: NotRequired[MembershipStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPrivacyBudgetTemplatesInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPrivacyBudgetsInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProtectedJobsInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    status: NotRequired[ProtectedJobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProtectedQueriesInputPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    status: NotRequired[ProtectedQueryStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemasInputPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    schemaType: NotRequired[SchemaTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPrivacyBudgetTemplatesOutputTypeDef(TypedDict):
    privacyBudgetTemplateSummaries: List[PrivacyBudgetTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSchemasOutputTypeDef(TypedDict):
    schemaSummaries: List[SchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

MLMemberAbilitiesUnionTypeDef = Union[MLMemberAbilitiesTypeDef, MLMemberAbilitiesOutputTypeDef]

class MLPaymentConfigTypeDef(TypedDict):
    modelTraining: NotRequired[ModelTrainingPaymentConfigTypeDef]
    modelInference: NotRequired[ModelInferencePaymentConfigTypeDef]

class MembershipMLPaymentConfigTypeDef(TypedDict):
    modelTraining: NotRequired[MembershipModelTrainingPaymentConfigTypeDef]
    modelInference: NotRequired[MembershipModelInferencePaymentConfigTypeDef]

class MembershipProtectedJobOutputConfigurationTypeDef(TypedDict):
    s3: NotRequired[ProtectedJobS3OutputConfigurationInputTypeDef]

class MembershipProtectedQueryOutputConfigurationTypeDef(TypedDict):
    s3: NotRequired[ProtectedQueryS3OutputConfigurationTypeDef]

class ProtectedJobConfigurationDetailsTypeDef(TypedDict):
    directAnalysisConfigurationDetails: NotRequired[
        ProtectedJobDirectAnalysisConfigurationDetailsTypeDef
    ]

class ProtectedJobOutputConfigurationInputTypeDef(TypedDict):
    member: NotRequired[ProtectedJobMemberOutputConfigurationInputTypeDef]

class ProtectedJobOutputConfigurationOutputTypeDef(TypedDict):
    s3: NotRequired[ProtectedJobS3OutputConfigurationOutputTypeDef]
    member: NotRequired[ProtectedJobMemberOutputConfigurationOutputTypeDef]

class ProtectedJobOutputTypeDef(TypedDict):
    s3: NotRequired[ProtectedJobS3OutputTypeDef]
    memberList: NotRequired[List[ProtectedJobSingleMemberOutputTypeDef]]

class ProtectedQueryDistributeOutputConfigurationLocationTypeDef(TypedDict):
    s3: NotRequired[ProtectedQueryS3OutputConfigurationTypeDef]
    member: NotRequired[ProtectedQueryMemberOutputConfigurationTypeDef]

class ProtectedQueryDistributeOutputTypeDef(TypedDict):
    s3: NotRequired[ProtectedQueryS3OutputTypeDef]
    memberList: NotRequired[List[ProtectedQuerySingleMemberOutputTypeDef]]

ProtectedQuerySQLParametersUnionTypeDef = Union[
    ProtectedQuerySQLParametersTypeDef, ProtectedQuerySQLParametersOutputTypeDef
]

class QueryConstraintTypeDef(TypedDict):
    requireOverlap: NotRequired[QueryConstraintRequireOverlapTypeDef]

class SchemaStatusDetailTypeDef(TypedDict):
    status: SchemaStatusType
    analysisType: AnalysisTypeType
    reasons: NotRequired[List[SchemaStatusReasonTypeDef]]
    analysisRuleType: NotRequired[AnalysisRuleTypeType]
    configurations: NotRequired[List[Literal["DIFFERENTIAL_PRIVACY"]]]

class SnowflakeTableSchemaOutputTypeDef(TypedDict):
    v1: NotRequired[List[SnowflakeTableSchemaV1TypeDef]]

class SnowflakeTableSchemaTypeDef(TypedDict):
    v1: NotRequired[Sequence[SnowflakeTableSchemaV1TypeDef]]

class AnalysisSourceMetadataTypeDef(TypedDict):
    artifacts: NotRequired[AnalysisTemplateArtifactMetadataTypeDef]

class AnalysisTemplateArtifactsOutputTypeDef(TypedDict):
    entryPoint: AnalysisTemplateArtifactTypeDef
    roleArn: str
    additionalArtifacts: NotRequired[List[AnalysisTemplateArtifactTypeDef]]

class AnalysisTemplateArtifactsTypeDef(TypedDict):
    entryPoint: AnalysisTemplateArtifactTypeDef
    roleArn: str
    additionalArtifacts: NotRequired[Sequence[AnalysisTemplateArtifactTypeDef]]

class ListCollaborationIdNamespaceAssociationsOutputTypeDef(TypedDict):
    collaborationIdNamespaceAssociationSummaries: List[
        CollaborationIdNamespaceAssociationSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListIdNamespaceAssociationsOutputTypeDef(TypedDict):
    idNamespaceAssociationSummaries: List[IdNamespaceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCollaborationIdNamespaceAssociationOutputTypeDef(TypedDict):
    collaborationIdNamespaceAssociation: CollaborationIdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdNamespaceAssociationOutputTypeDef(TypedDict):
    idNamespaceAssociation: IdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdNamespaceAssociationOutputTypeDef(TypedDict):
    idNamespaceAssociation: IdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdNamespaceAssociationOutputTypeDef(TypedDict):
    idNamespaceAssociation: IdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollaborationOutputTypeDef(TypedDict):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationOutputTypeDef(TypedDict):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCollaborationOutputTypeDef(TypedDict):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReceiverConfigurationTypeDef(TypedDict):
    analysisType: AnalysisTypeType
    configurationDetails: NotRequired[ConfigurationDetailsTypeDef]

class ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef(TypedDict):
    v1: NotRequired[ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef]

class ConfiguredTableAssociationAnalysisRulePolicyTypeDef(TypedDict):
    v1: NotRequired[ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef]

class ListIdMappingTablesOutputTypeDef(TypedDict):
    idMappingTableSummaries: List[IdMappingTableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AnalysisRuleCustomOutputTypeDef(TypedDict):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: NotRequired[List[str]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]
    disallowedOutputColumns: NotRequired[List[str]]
    differentialPrivacy: NotRequired[DifferentialPrivacyConfigurationOutputTypeDef]

class ConsolidatedPolicyCustomTypeDef(TypedDict):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: NotRequired[List[str]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]
    disallowedOutputColumns: NotRequired[List[str]]
    differentialPrivacy: NotRequired[DifferentialPrivacyConfigurationOutputTypeDef]
    allowedResultReceivers: NotRequired[List[str]]
    allowedAdditionalAnalyses: NotRequired[List[str]]

class AnalysisRuleCustomTypeDef(TypedDict):
    allowedAnalyses: Sequence[str]
    allowedAnalysisProviders: NotRequired[Sequence[str]]
    additionalAnalyses: NotRequired[AdditionalAnalysesType]
    disallowedOutputColumns: NotRequired[Sequence[str]]
    differentialPrivacy: NotRequired[DifferentialPrivacyConfigurationTypeDef]

class PrivacyImpactTypeDef(TypedDict):
    differentialPrivacy: NotRequired[DifferentialPrivacyPrivacyImpactTypeDef]

class PreviewPrivacyImpactInputTypeDef(TypedDict):
    membershipIdentifier: str
    parameters: PreviewPrivacyImpactParametersInputTypeDef

class PrivacyBudgetTypeDef(TypedDict):
    differentialPrivacy: NotRequired[DifferentialPrivacyPrivacyBudgetTypeDef]

class CreatePrivacyBudgetTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: PrivacyBudgetTemplateParametersInputTypeDef
    tags: NotRequired[Mapping[str, str]]

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
        "parameters": PrivacyBudgetTemplateParametersOutputTypeDef,
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
        "parameters": PrivacyBudgetTemplateParametersOutputTypeDef,
    },
)

class UpdatePrivacyBudgetTemplateInputTypeDef(TypedDict):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: NotRequired[PrivacyBudgetTemplateUpdateParametersTypeDef]

IdMappingTableTypeDef = TypedDict(
    "IdMappingTableTypeDef",
    {
        "id": str,
        "arn": str,
        "inputReferenceConfig": IdMappingTableInputReferenceConfigTypeDef,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "inputReferenceProperties": IdMappingTableInputReferencePropertiesTypeDef,
        "description": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
    },
)

class SchemaTypePropertiesTypeDef(TypedDict):
    idMappingTable: NotRequired[IdMappingTableSchemaTypePropertiesTypeDef]

class PaymentConfigurationTypeDef(TypedDict):
    queryCompute: QueryComputePaymentConfigTypeDef
    machineLearning: NotRequired[MLPaymentConfigTypeDef]
    jobCompute: NotRequired[JobComputePaymentConfigTypeDef]

class MembershipPaymentConfigurationTypeDef(TypedDict):
    queryCompute: MembershipQueryComputePaymentConfigTypeDef
    machineLearning: NotRequired[MembershipMLPaymentConfigTypeDef]
    jobCompute: NotRequired[MembershipJobComputePaymentConfigTypeDef]

class MembershipProtectedJobResultConfigurationTypeDef(TypedDict):
    outputConfiguration: MembershipProtectedJobOutputConfigurationTypeDef
    roleArn: str

class MembershipProtectedQueryResultConfigurationTypeDef(TypedDict):
    outputConfiguration: MembershipProtectedQueryOutputConfigurationTypeDef
    roleArn: NotRequired[str]

class ProtectedJobReceiverConfigurationTypeDef(TypedDict):
    analysisType: Literal["DIRECT_ANALYSIS"]
    configurationDetails: NotRequired[ProtectedJobConfigurationDetailsTypeDef]

class ProtectedJobResultConfigurationInputTypeDef(TypedDict):
    outputConfiguration: ProtectedJobOutputConfigurationInputTypeDef

class ProtectedJobResultConfigurationOutputTypeDef(TypedDict):
    outputConfiguration: ProtectedJobOutputConfigurationOutputTypeDef

class ProtectedJobResultTypeDef(TypedDict):
    output: ProtectedJobOutputTypeDef

class ProtectedQueryDistributeOutputConfigurationOutputTypeDef(TypedDict):
    locations: List[ProtectedQueryDistributeOutputConfigurationLocationTypeDef]

class ProtectedQueryDistributeOutputConfigurationTypeDef(TypedDict):
    locations: Sequence[ProtectedQueryDistributeOutputConfigurationLocationTypeDef]

class ProtectedQueryOutputTypeDef(TypedDict):
    s3: NotRequired[ProtectedQueryS3OutputTypeDef]
    memberList: NotRequired[List[ProtectedQuerySingleMemberOutputTypeDef]]
    distribute: NotRequired[ProtectedQueryDistributeOutputTypeDef]

class AnalysisRuleIdMappingTableTypeDef(TypedDict):
    joinColumns: List[str]
    queryConstraints: List[QueryConstraintTypeDef]
    dimensionColumns: NotRequired[List[str]]

class SnowflakeTableReferenceOutputTypeDef(TypedDict):
    secretArn: str
    accountIdentifier: str
    databaseName: str
    tableName: str
    schemaName: str
    tableSchema: SnowflakeTableSchemaOutputTypeDef

class SnowflakeTableReferenceTypeDef(TypedDict):
    secretArn: str
    accountIdentifier: str
    databaseName: str
    tableName: str
    schemaName: str
    tableSchema: SnowflakeTableSchemaTypeDef

class AnalysisSourceOutputTypeDef(TypedDict):
    text: NotRequired[str]
    artifacts: NotRequired[AnalysisTemplateArtifactsOutputTypeDef]

class AnalysisSourceTypeDef(TypedDict):
    text: NotRequired[str]
    artifacts: NotRequired[AnalysisTemplateArtifactsTypeDef]

ProtectedQuerySummaryTypeDef = TypedDict(
    "ProtectedQuerySummaryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedQueryStatusType,
        "receiverConfigurations": List[ReceiverConfigurationTypeDef],
    },
)
ConfiguredTableAssociationAnalysisRuleTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleTypeDef",
    {
        "membershipIdentifier": str,
        "configuredTableAssociationId": str,
        "configuredTableAssociationArn": str,
        "policy": ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef,
        "type": ConfiguredTableAssociationAnalysisRuleTypeType,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef = Union[
    ConfiguredTableAssociationAnalysisRulePolicyTypeDef,
    ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef,
]
ConfiguredTableAnalysisRulePolicyV1OutputTypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyV1OutputTypeDef",
    {
        "list": NotRequired[AnalysisRuleListOutputTypeDef],
        "aggregation": NotRequired[AnalysisRuleAggregationOutputTypeDef],
        "custom": NotRequired[AnalysisRuleCustomOutputTypeDef],
    },
)
ConsolidatedPolicyV1TypeDef = TypedDict(
    "ConsolidatedPolicyV1TypeDef",
    {
        "list": NotRequired[ConsolidatedPolicyListTypeDef],
        "aggregation": NotRequired[ConsolidatedPolicyAggregationTypeDef],
        "custom": NotRequired[ConsolidatedPolicyCustomTypeDef],
    },
)
ConfiguredTableAnalysisRulePolicyV1TypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    {
        "list": NotRequired[AnalysisRuleListTypeDef],
        "aggregation": NotRequired[AnalysisRuleAggregationTypeDef],
        "custom": NotRequired[AnalysisRuleCustomTypeDef],
    },
)

class PreviewPrivacyImpactOutputTypeDef(TypedDict):
    privacyImpact: PrivacyImpactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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
        "budget": PrivacyBudgetTypeDef,
    },
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
        "budget": PrivacyBudgetTypeDef,
    },
)

class GetCollaborationPrivacyBudgetTemplateOutputTypeDef(TypedDict):
    collaborationPrivacyBudgetTemplate: CollaborationPrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivacyBudgetTemplateOutputTypeDef(TypedDict):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrivacyBudgetTemplateOutputTypeDef(TypedDict):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivacyBudgetTemplateOutputTypeDef(TypedDict):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdMappingTableOutputTypeDef(TypedDict):
    idMappingTable: IdMappingTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdMappingTableOutputTypeDef(TypedDict):
    idMappingTable: IdMappingTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdMappingTableOutputTypeDef(TypedDict):
    idMappingTable: IdMappingTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "columns": List[ColumnTypeDef],
        "partitionKeys": List[ColumnTypeDef],
        "analysisRuleTypes": List[AnalysisRuleTypeType],
        "creatorAccountId": str,
        "name": str,
        "collaborationId": str,
        "collaborationArn": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
        "type": SchemaTypeType,
        "schemaStatusDetails": List[SchemaStatusDetailTypeDef],
        "analysisMethod": NotRequired[AnalysisMethodType],
        "selectedAnalysisMethods": NotRequired[List[SelectedAnalysisMethodType]],
        "schemaTypeProperties": NotRequired[SchemaTypePropertiesTypeDef],
    },
)

class MemberSpecificationTypeDef(TypedDict):
    accountId: str
    memberAbilities: Sequence[MemberAbilityType]
    displayName: str
    mlMemberAbilities: NotRequired[MLMemberAbilitiesUnionTypeDef]
    paymentConfiguration: NotRequired[PaymentConfigurationTypeDef]

class MemberSummaryTypeDef(TypedDict):
    accountId: str
    status: MemberStatusType
    displayName: str
    abilities: List[MemberAbilityType]
    createTime: datetime
    updateTime: datetime
    paymentConfiguration: PaymentConfigurationTypeDef
    mlAbilities: NotRequired[MLMemberAbilitiesOutputTypeDef]
    membershipId: NotRequired[str]
    membershipArn: NotRequired[str]

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
        "paymentConfiguration": MembershipPaymentConfigurationTypeDef,
        "mlMemberAbilities": NotRequired[MLMemberAbilitiesOutputTypeDef],
    },
)

class CreateMembershipInputTypeDef(TypedDict):
    collaborationIdentifier: str
    queryLogStatus: MembershipQueryLogStatusType
    jobLogStatus: NotRequired[MembershipJobLogStatusType]
    tags: NotRequired[Mapping[str, str]]
    defaultResultConfiguration: NotRequired[MembershipProtectedQueryResultConfigurationTypeDef]
    defaultJobResultConfiguration: NotRequired[MembershipProtectedJobResultConfigurationTypeDef]
    paymentConfiguration: NotRequired[MembershipPaymentConfigurationTypeDef]

MembershipTypeDef = TypedDict(
    "MembershipTypeDef",
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
        "paymentConfiguration": MembershipPaymentConfigurationTypeDef,
        "mlMemberAbilities": NotRequired[MLMemberAbilitiesOutputTypeDef],
        "jobLogStatus": NotRequired[MembershipJobLogStatusType],
        "defaultResultConfiguration": NotRequired[
            MembershipProtectedQueryResultConfigurationTypeDef
        ],
        "defaultJobResultConfiguration": NotRequired[
            MembershipProtectedJobResultConfigurationTypeDef
        ],
    },
)

class UpdateMembershipInputTypeDef(TypedDict):
    membershipIdentifier: str
    queryLogStatus: NotRequired[MembershipQueryLogStatusType]
    jobLogStatus: NotRequired[MembershipJobLogStatusType]
    defaultResultConfiguration: NotRequired[MembershipProtectedQueryResultConfigurationTypeDef]
    defaultJobResultConfiguration: NotRequired[MembershipProtectedJobResultConfigurationTypeDef]

ProtectedJobSummaryTypeDef = TypedDict(
    "ProtectedJobSummaryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedJobStatusType,
        "receiverConfigurations": List[ProtectedJobReceiverConfigurationTypeDef],
    },
)
StartProtectedJobInputTypeDef = TypedDict(
    "StartProtectedJobInputTypeDef",
    {
        "type": Literal["PYSPARK"],
        "membershipIdentifier": str,
        "jobParameters": ProtectedJobParametersTypeDef,
        "resultConfiguration": NotRequired[ProtectedJobResultConfigurationInputTypeDef],
    },
)
ProtectedJobTypeDef = TypedDict(
    "ProtectedJobTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedJobStatusType,
        "jobParameters": NotRequired[ProtectedJobParametersTypeDef],
        "resultConfiguration": NotRequired[ProtectedJobResultConfigurationOutputTypeDef],
        "statistics": NotRequired[ProtectedJobStatisticsTypeDef],
        "result": NotRequired[ProtectedJobResultTypeDef],
        "error": NotRequired[ProtectedJobErrorTypeDef],
    },
)

class ProtectedQueryOutputConfigurationOutputTypeDef(TypedDict):
    s3: NotRequired[ProtectedQueryS3OutputConfigurationTypeDef]
    member: NotRequired[ProtectedQueryMemberOutputConfigurationTypeDef]
    distribute: NotRequired[ProtectedQueryDistributeOutputConfigurationOutputTypeDef]

class ProtectedQueryOutputConfigurationTypeDef(TypedDict):
    s3: NotRequired[ProtectedQueryS3OutputConfigurationTypeDef]
    member: NotRequired[ProtectedQueryMemberOutputConfigurationTypeDef]
    distribute: NotRequired[ProtectedQueryDistributeOutputConfigurationTypeDef]

class ProtectedQueryResultTypeDef(TypedDict):
    output: ProtectedQueryOutputTypeDef

AnalysisRulePolicyV1TypeDef = TypedDict(
    "AnalysisRulePolicyV1TypeDef",
    {
        "list": NotRequired[AnalysisRuleListOutputTypeDef],
        "aggregation": NotRequired[AnalysisRuleAggregationOutputTypeDef],
        "custom": NotRequired[AnalysisRuleCustomOutputTypeDef],
        "idMappingTable": NotRequired[AnalysisRuleIdMappingTableTypeDef],
    },
)

class TableReferenceOutputTypeDef(TypedDict):
    glue: NotRequired[GlueTableReferenceTypeDef]
    snowflake: NotRequired[SnowflakeTableReferenceOutputTypeDef]
    athena: NotRequired[AthenaTableReferenceTypeDef]

class TableReferenceTypeDef(TypedDict):
    glue: NotRequired[GlueTableReferenceTypeDef]
    snowflake: NotRequired[SnowflakeTableReferenceTypeDef]
    athena: NotRequired[AthenaTableReferenceTypeDef]

AnalysisTemplateTypeDef = TypedDict(
    "AnalysisTemplateTypeDef",
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
        "schema": AnalysisSchemaOutputTypeDef,
        "format": AnalysisFormatType,
        "source": AnalysisSourceOutputTypeDef,
        "description": NotRequired[str],
        "sourceMetadata": NotRequired[AnalysisSourceMetadataTypeDef],
        "analysisParameters": NotRequired[List[AnalysisParameterTypeDef]],
        "validations": NotRequired[List[AnalysisTemplateValidationStatusDetailTypeDef]],
    },
)
CollaborationAnalysisTemplateTypeDef = TypedDict(
    "CollaborationAnalysisTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "schema": AnalysisSchemaOutputTypeDef,
        "format": AnalysisFormatType,
        "description": NotRequired[str],
        "source": NotRequired[AnalysisSourceOutputTypeDef],
        "sourceMetadata": NotRequired[AnalysisSourceMetadataTypeDef],
        "analysisParameters": NotRequired[List[AnalysisParameterTypeDef]],
        "validations": NotRequired[List[AnalysisTemplateValidationStatusDetailTypeDef]],
    },
)
AnalysisSourceUnionTypeDef = Union[AnalysisSourceTypeDef, AnalysisSourceOutputTypeDef]

class ListProtectedQueriesOutputTypeDef(TypedDict):
    protectedQueries: List[ProtectedQuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: ConfiguredTableAssociationAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAssociationAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: ConfiguredTableAssociationAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: ConfiguredTableAssociationAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableAssociationAnalysisRuleInputTypeDef(TypedDict):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef

class UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef(TypedDict):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef

class ConfiguredTableAnalysisRulePolicyOutputTypeDef(TypedDict):
    v1: NotRequired[ConfiguredTableAnalysisRulePolicyV1OutputTypeDef]

class ConsolidatedPolicyTypeDef(TypedDict):
    v1: NotRequired[ConsolidatedPolicyV1TypeDef]

class ConfiguredTableAnalysisRulePolicyTypeDef(TypedDict):
    v1: NotRequired[ConfiguredTableAnalysisRulePolicyV1TypeDef]

class ListCollaborationPrivacyBudgetsOutputTypeDef(TypedDict):
    collaborationPrivacyBudgetSummaries: List[CollaborationPrivacyBudgetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPrivacyBudgetsOutputTypeDef(TypedDict):
    privacyBudgetSummaries: List[PrivacyBudgetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchGetSchemaOutputTypeDef(TypedDict):
    schemas: List[SchemaTypeDef]
    errors: List[BatchGetSchemaErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaOutputTypeDef(TypedDict):
    schema: SchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollaborationInputTypeDef(TypedDict):
    members: Sequence[MemberSpecificationTypeDef]
    name: str
    description: str
    creatorMemberAbilities: Sequence[MemberAbilityType]
    creatorDisplayName: str
    queryLogStatus: CollaborationQueryLogStatusType
    creatorMLMemberAbilities: NotRequired[MLMemberAbilitiesUnionTypeDef]
    dataEncryptionMetadata: NotRequired[DataEncryptionMetadataTypeDef]
    jobLogStatus: NotRequired[CollaborationJobLogStatusType]
    tags: NotRequired[Mapping[str, str]]
    creatorPaymentConfiguration: NotRequired[PaymentConfigurationTypeDef]
    analyticsEngine: NotRequired[AnalyticsEngineType]

class ListMembersOutputTypeDef(TypedDict):
    memberSummaries: List[MemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMembershipsOutputTypeDef(TypedDict):
    membershipSummaries: List[MembershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateMembershipOutputTypeDef(TypedDict):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembershipOutputTypeDef(TypedDict):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMembershipOutputTypeDef(TypedDict):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectedJobsOutputTypeDef(TypedDict):
    protectedJobs: List[ProtectedJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetProtectedJobOutputTypeDef(TypedDict):
    protectedJob: ProtectedJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartProtectedJobOutputTypeDef(TypedDict):
    protectedJob: ProtectedJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectedJobOutputTypeDef(TypedDict):
    protectedJob: ProtectedJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectedQueryResultConfigurationOutputTypeDef(TypedDict):
    outputConfiguration: ProtectedQueryOutputConfigurationOutputTypeDef

class ProtectedQueryResultConfigurationTypeDef(TypedDict):
    outputConfiguration: ProtectedQueryOutputConfigurationTypeDef

class AnalysisRulePolicyTypeDef(TypedDict):
    v1: NotRequired[AnalysisRulePolicyV1TypeDef]

ConfiguredTableTypeDef = TypedDict(
    "ConfiguredTableTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "tableReference": TableReferenceOutputTypeDef,
        "createTime": datetime,
        "updateTime": datetime,
        "analysisRuleTypes": List[ConfiguredTableAnalysisRuleTypeType],
        "analysisMethod": AnalysisMethodType,
        "allowedColumns": List[str],
        "description": NotRequired[str],
        "selectedAnalysisMethods": NotRequired[List[SelectedAnalysisMethodType]],
    },
)
TableReferenceUnionTypeDef = Union[TableReferenceTypeDef, TableReferenceOutputTypeDef]

class CreateAnalysisTemplateOutputTypeDef(TypedDict):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalysisTemplateOutputTypeDef(TypedDict):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnalysisTemplateOutputTypeDef(TypedDict):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetCollaborationAnalysisTemplateOutputTypeDef(TypedDict):
    collaborationAnalysisTemplates: List[CollaborationAnalysisTemplateTypeDef]
    errors: List[BatchGetCollaborationAnalysisTemplateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationAnalysisTemplateOutputTypeDef(TypedDict):
    collaborationAnalysisTemplate: CollaborationAnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateAnalysisTemplateInputTypeDef = TypedDict(
    "CreateAnalysisTemplateInputTypeDef",
    {
        "membershipIdentifier": str,
        "name": str,
        "format": AnalysisFormatType,
        "source": AnalysisSourceUnionTypeDef,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "analysisParameters": NotRequired[Sequence[AnalysisParameterTypeDef]],
        "schema": NotRequired[AnalysisSchemaUnionTypeDef],
    },
)
ConfiguredTableAnalysisRuleTypeDef = TypedDict(
    "ConfiguredTableAnalysisRuleTypeDef",
    {
        "configuredTableId": str,
        "configuredTableArn": str,
        "policy": ConfiguredTableAnalysisRulePolicyOutputTypeDef,
        "type": ConfiguredTableAnalysisRuleTypeType,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
ConfiguredTableAnalysisRulePolicyUnionTypeDef = Union[
    ConfiguredTableAnalysisRulePolicyTypeDef, ConfiguredTableAnalysisRulePolicyOutputTypeDef
]
ProtectedQueryTypeDef = TypedDict(
    "ProtectedQueryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedQueryStatusType,
        "sqlParameters": NotRequired[ProtectedQuerySQLParametersOutputTypeDef],
        "resultConfiguration": NotRequired[ProtectedQueryResultConfigurationOutputTypeDef],
        "statistics": NotRequired[ProtectedQueryStatisticsTypeDef],
        "result": NotRequired[ProtectedQueryResultTypeDef],
        "error": NotRequired[ProtectedQueryErrorTypeDef],
        "differentialPrivacy": NotRequired[DifferentialPrivacyParametersTypeDef],
        "computeConfiguration": NotRequired[ComputeConfigurationTypeDef],
    },
)
ProtectedQueryResultConfigurationUnionTypeDef = Union[
    ProtectedQueryResultConfigurationTypeDef, ProtectedQueryResultConfigurationOutputTypeDef
]
AnalysisRuleTypeDef = TypedDict(
    "AnalysisRuleTypeDef",
    {
        "collaborationId": str,
        "type": AnalysisRuleTypeType,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "policy": AnalysisRulePolicyTypeDef,
        "collaborationPolicy": NotRequired[
            ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef
        ],
        "consolidatedPolicy": NotRequired[ConsolidatedPolicyTypeDef],
    },
)

class CreateConfiguredTableOutputTypeDef(TypedDict):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableOutputTypeDef(TypedDict):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableOutputTypeDef(TypedDict):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableInputTypeDef(TypedDict):
    name: str
    tableReference: TableReferenceUnionTypeDef
    allowedColumns: Sequence[str]
    analysisMethod: AnalysisMethodType
    description: NotRequired[str]
    selectedAnalysisMethods: NotRequired[Sequence[SelectedAnalysisMethodType]]
    tags: NotRequired[Mapping[str, str]]

class CreateConfiguredTableAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableAnalysisRuleInputTypeDef(TypedDict):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnionTypeDef

class UpdateConfiguredTableAnalysisRuleInputTypeDef(TypedDict):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnionTypeDef

class GetProtectedQueryOutputTypeDef(TypedDict):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartProtectedQueryOutputTypeDef(TypedDict):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectedQueryOutputTypeDef(TypedDict):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

StartProtectedQueryInputTypeDef = TypedDict(
    "StartProtectedQueryInputTypeDef",
    {
        "type": Literal["SQL"],
        "membershipIdentifier": str,
        "sqlParameters": ProtectedQuerySQLParametersUnionTypeDef,
        "resultConfiguration": NotRequired[ProtectedQueryResultConfigurationUnionTypeDef],
        "computeConfiguration": NotRequired[ComputeConfigurationTypeDef],
    },
)

class BatchGetSchemaAnalysisRuleOutputTypeDef(TypedDict):
    analysisRules: List[AnalysisRuleTypeDef]
    errors: List[BatchGetSchemaAnalysisRuleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaAnalysisRuleOutputTypeDef(TypedDict):
    analysisRule: AnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
