"""
Type annotations for cleanrooms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/literals.html)

Usage::

    ```python
    from mypy_boto3_cleanrooms.literals import AggregateFunctionNameType

    data: AggregateFunctionNameType = "AVG"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregateFunctionNameType",
    "AggregationTypeType",
    "AnalysisFormatType",
    "AnalysisMethodType",
    "AnalysisRuleTypeType",
    "AnalysisTemplateValidationStatusType",
    "AnalysisTemplateValidationTypeType",
    "CollaborationQueryLogStatusType",
    "ConfiguredTableAnalysisRuleTypeType",
    "DifferentialPrivacyAggregationTypeType",
    "FilterableMemberStatusType",
    "JoinOperatorType",
    "JoinRequiredOptionType",
    "ListAnalysisTemplatesPaginatorName",
    "ListCollaborationAnalysisTemplatesPaginatorName",
    "ListCollaborationConfiguredAudienceModelAssociationsPaginatorName",
    "ListCollaborationPrivacyBudgetTemplatesPaginatorName",
    "ListCollaborationPrivacyBudgetsPaginatorName",
    "ListCollaborationsPaginatorName",
    "ListConfiguredAudienceModelAssociationsPaginatorName",
    "ListConfiguredTableAssociationsPaginatorName",
    "ListConfiguredTablesPaginatorName",
    "ListMembersPaginatorName",
    "ListMembershipsPaginatorName",
    "ListPrivacyBudgetTemplatesPaginatorName",
    "ListPrivacyBudgetsPaginatorName",
    "ListProtectedQueriesPaginatorName",
    "ListSchemasPaginatorName",
    "MemberAbilityType",
    "MemberStatusType",
    "MembershipQueryLogStatusType",
    "MembershipStatusType",
    "ParameterTypeType",
    "PrivacyBudgetTemplateAutoRefreshType",
    "PrivacyBudgetTypeType",
    "ProtectedQueryStatusType",
    "ProtectedQueryTypeType",
    "ResultFormatType",
    "ScalarFunctionsType",
    "SchemaConfigurationType",
    "SchemaStatusReasonCodeType",
    "SchemaStatusType",
    "SchemaTypeType",
    "TargetProtectedQueryStatusType",
)

AggregateFunctionNameType = Literal["AVG", "COUNT", "COUNT_DISTINCT", "SUM", "SUM_DISTINCT"]
AggregationTypeType = Literal["COUNT_DISTINCT"]
AnalysisFormatType = Literal["SQL"]
AnalysisMethodType = Literal["DIRECT_QUERY"]
AnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "LIST"]
AnalysisTemplateValidationStatusType = Literal["INVALID", "UNABLE_TO_VALIDATE", "VALID"]
AnalysisTemplateValidationTypeType = Literal["DIFFERENTIAL_PRIVACY"]
CollaborationQueryLogStatusType = Literal["DISABLED", "ENABLED"]
ConfiguredTableAnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "LIST"]
DifferentialPrivacyAggregationTypeType = Literal["AVG", "COUNT", "COUNT_DISTINCT", "STDDEV", "SUM"]
FilterableMemberStatusType = Literal["ACTIVE", "INVITED"]
JoinOperatorType = Literal["AND", "OR"]
JoinRequiredOptionType = Literal["QUERY_RUNNER"]
ListAnalysisTemplatesPaginatorName = Literal["list_analysis_templates"]
ListCollaborationAnalysisTemplatesPaginatorName = Literal["list_collaboration_analysis_templates"]
ListCollaborationConfiguredAudienceModelAssociationsPaginatorName = Literal[
    "list_collaboration_configured_audience_model_associations"
]
ListCollaborationPrivacyBudgetTemplatesPaginatorName = Literal[
    "list_collaboration_privacy_budget_templates"
]
ListCollaborationPrivacyBudgetsPaginatorName = Literal["list_collaboration_privacy_budgets"]
ListCollaborationsPaginatorName = Literal["list_collaborations"]
ListConfiguredAudienceModelAssociationsPaginatorName = Literal[
    "list_configured_audience_model_associations"
]
ListConfiguredTableAssociationsPaginatorName = Literal["list_configured_table_associations"]
ListConfiguredTablesPaginatorName = Literal["list_configured_tables"]
ListMembersPaginatorName = Literal["list_members"]
ListMembershipsPaginatorName = Literal["list_memberships"]
ListPrivacyBudgetTemplatesPaginatorName = Literal["list_privacy_budget_templates"]
ListPrivacyBudgetsPaginatorName = Literal["list_privacy_budgets"]
ListProtectedQueriesPaginatorName = Literal["list_protected_queries"]
ListSchemasPaginatorName = Literal["list_schemas"]
MemberAbilityType = Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]
MemberStatusType = Literal["ACTIVE", "INVITED", "LEFT", "REMOVED"]
MembershipQueryLogStatusType = Literal["DISABLED", "ENABLED"]
MembershipStatusType = Literal["ACTIVE", "COLLABORATION_DELETED", "REMOVED"]
ParameterTypeType = Literal[
    "BIGINT",
    "BOOLEAN",
    "CHAR",
    "DATE",
    "DECIMAL",
    "DOUBLE_PRECISION",
    "INTEGER",
    "REAL",
    "SMALLINT",
    "TIME",
    "TIMESTAMP",
    "TIMESTAMPTZ",
    "TIMETZ",
    "VARBYTE",
    "VARCHAR",
]
PrivacyBudgetTemplateAutoRefreshType = Literal["CALENDAR_MONTH", "NONE"]
PrivacyBudgetTypeType = Literal["DIFFERENTIAL_PRIVACY"]
ProtectedQueryStatusType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "STARTED", "SUBMITTED", "SUCCESS", "TIMED_OUT"
]
ProtectedQueryTypeType = Literal["SQL"]
ResultFormatType = Literal["CSV", "PARQUET"]
ScalarFunctionsType = Literal[
    "ABS",
    "CAST",
    "CEILING",
    "COALESCE",
    "CONVERT",
    "CURRENT_DATE",
    "DATEADD",
    "EXTRACT",
    "FLOOR",
    "GETDATE",
    "LN",
    "LOG",
    "LOWER",
    "ROUND",
    "RTRIM",
    "SQRT",
    "SUBSTRING",
    "TO_CHAR",
    "TO_DATE",
    "TO_NUMBER",
    "TO_TIMESTAMP",
    "TRIM",
    "TRUNC",
    "UPPER",
]
SchemaConfigurationType = Literal["DIFFERENTIAL_PRIVACY"]
SchemaStatusReasonCodeType = Literal[
    "ANALYSIS_PROVIDERS_NOT_CONFIGURED",
    "ANALYSIS_RULE_MISSING",
    "ANALYSIS_TEMPLATES_NOT_CONFIGURED",
    "DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED",
]
SchemaStatusType = Literal["NOT_READY", "READY"]
SchemaTypeType = Literal["TABLE"]
TargetProtectedQueryStatusType = Literal["CANCELLED"]
