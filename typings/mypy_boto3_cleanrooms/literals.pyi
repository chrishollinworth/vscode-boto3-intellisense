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
    "CollaborationQueryLogStatusType",
    "ConfiguredTableAnalysisRuleTypeType",
    "FilterableMemberStatusType",
    "JoinOperatorType",
    "JoinRequiredOptionType",
    "ListAnalysisTemplatesPaginatorName",
    "ListCollaborationAnalysisTemplatesPaginatorName",
    "ListCollaborationsPaginatorName",
    "ListConfiguredTableAssociationsPaginatorName",
    "ListConfiguredTablesPaginatorName",
    "ListMembersPaginatorName",
    "ListMembershipsPaginatorName",
    "ListProtectedQueriesPaginatorName",
    "ListSchemasPaginatorName",
    "MemberAbilityType",
    "MemberStatusType",
    "MembershipQueryLogStatusType",
    "MembershipStatusType",
    "ParameterTypeType",
    "ProtectedQueryStatusType",
    "ProtectedQueryTypeType",
    "ResultFormatType",
    "ScalarFunctionsType",
    "SchemaTypeType",
    "TargetProtectedQueryStatusType",
)

AggregateFunctionNameType = Literal["AVG", "COUNT", "COUNT_DISTINCT", "SUM", "SUM_DISTINCT"]
AggregationTypeType = Literal["COUNT_DISTINCT"]
AnalysisFormatType = Literal["SQL"]
AnalysisMethodType = Literal["DIRECT_QUERY"]
AnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "LIST"]
CollaborationQueryLogStatusType = Literal["DISABLED", "ENABLED"]
ConfiguredTableAnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "LIST"]
FilterableMemberStatusType = Literal["ACTIVE", "INVITED"]
JoinOperatorType = Literal["AND", "OR"]
JoinRequiredOptionType = Literal["QUERY_RUNNER"]
ListAnalysisTemplatesPaginatorName = Literal["list_analysis_templates"]
ListCollaborationAnalysisTemplatesPaginatorName = Literal["list_collaboration_analysis_templates"]
ListCollaborationsPaginatorName = Literal["list_collaborations"]
ListConfiguredTableAssociationsPaginatorName = Literal["list_configured_table_associations"]
ListConfiguredTablesPaginatorName = Literal["list_configured_tables"]
ListMembersPaginatorName = Literal["list_members"]
ListMembershipsPaginatorName = Literal["list_memberships"]
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
    "FLOOR",
    "LN",
    "LOG",
    "LOWER",
    "ROUND",
    "RTRIM",
    "SQRT",
    "TRUNC",
    "UPPER",
]
SchemaTypeType = Literal["TABLE"]
TargetProtectedQueryStatusType = Literal["CANCELLED"]
