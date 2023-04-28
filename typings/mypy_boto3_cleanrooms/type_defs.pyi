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
    CollaborationQueryLogStatusType,
    ConfiguredTableAnalysisRuleTypeType,
    FilterableMemberStatusType,
    MemberAbilityType,
    MembershipQueryLogStatusType,
    MembershipStatusType,
    MemberStatusType,
    ProtectedQueryStatusType,
    ResultFormatType,
    ScalarFunctionsType,
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
    "AnalysisRuleAggregationTypeDef",
    "AnalysisRuleListTypeDef",
    "AnalysisRulePolicyTypeDef",
    "AnalysisRulePolicyV1TypeDef",
    "AnalysisRuleTypeDef",
    "BatchGetSchemaErrorTypeDef",
    "BatchGetSchemaInputRequestTypeDef",
    "BatchGetSchemaOutputTypeDef",
    "CollaborationSummaryTypeDef",
    "CollaborationTypeDef",
    "ColumnTypeDef",
    "ConfiguredTableAnalysisRulePolicyTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    "ConfiguredTableAnalysisRuleTypeDef",
    "ConfiguredTableAssociationSummaryTypeDef",
    "ConfiguredTableAssociationTypeDef",
    "ConfiguredTableSummaryTypeDef",
    "ConfiguredTableTypeDef",
    "CreateCollaborationInputRequestTypeDef",
    "CreateCollaborationOutputTypeDef",
    "CreateConfiguredTableAnalysisRuleInputRequestTypeDef",
    "CreateConfiguredTableAnalysisRuleOutputTypeDef",
    "CreateConfiguredTableAssociationInputRequestTypeDef",
    "CreateConfiguredTableAssociationOutputTypeDef",
    "CreateConfiguredTableInputRequestTypeDef",
    "CreateConfiguredTableOutputTypeDef",
    "CreateMembershipInputRequestTypeDef",
    "CreateMembershipOutputTypeDef",
    "DataEncryptionMetadataTypeDef",
    "DeleteCollaborationInputRequestTypeDef",
    "DeleteConfiguredTableAnalysisRuleInputRequestTypeDef",
    "DeleteConfiguredTableAssociationInputRequestTypeDef",
    "DeleteConfiguredTableInputRequestTypeDef",
    "DeleteMemberInputRequestTypeDef",
    "DeleteMembershipInputRequestTypeDef",
    "GetCollaborationInputRequestTypeDef",
    "GetCollaborationOutputTypeDef",
    "GetConfiguredTableAnalysisRuleInputRequestTypeDef",
    "GetConfiguredTableAnalysisRuleOutputTypeDef",
    "GetConfiguredTableAssociationInputRequestTypeDef",
    "GetConfiguredTableAssociationOutputTypeDef",
    "GetConfiguredTableInputRequestTypeDef",
    "GetConfiguredTableOutputTypeDef",
    "GetMembershipInputRequestTypeDef",
    "GetMembershipOutputTypeDef",
    "GetProtectedQueryInputRequestTypeDef",
    "GetProtectedQueryOutputTypeDef",
    "GetSchemaAnalysisRuleInputRequestTypeDef",
    "GetSchemaAnalysisRuleOutputTypeDef",
    "GetSchemaInputRequestTypeDef",
    "GetSchemaOutputTypeDef",
    "GlueTableReferenceTypeDef",
    "ListCollaborationsInputRequestTypeDef",
    "ListCollaborationsOutputTypeDef",
    "ListConfiguredTableAssociationsInputRequestTypeDef",
    "ListConfiguredTableAssociationsOutputTypeDef",
    "ListConfiguredTablesInputRequestTypeDef",
    "ListConfiguredTablesOutputTypeDef",
    "ListMembersInputRequestTypeDef",
    "ListMembersOutputTypeDef",
    "ListMembershipsInputRequestTypeDef",
    "ListMembershipsOutputTypeDef",
    "ListProtectedQueriesInputRequestTypeDef",
    "ListProtectedQueriesOutputTypeDef",
    "ListSchemasInputRequestTypeDef",
    "ListSchemasOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MemberSpecificationTypeDef",
    "MemberSummaryTypeDef",
    "MembershipSummaryTypeDef",
    "MembershipTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectedQueryErrorTypeDef",
    "ProtectedQueryOutputConfigurationTypeDef",
    "ProtectedQueryOutputTypeDef",
    "ProtectedQueryResultConfigurationTypeDef",
    "ProtectedQueryResultTypeDef",
    "ProtectedQueryS3OutputConfigurationTypeDef",
    "ProtectedQueryS3OutputTypeDef",
    "ProtectedQuerySQLParametersTypeDef",
    "ProtectedQueryStatisticsTypeDef",
    "ProtectedQuerySummaryTypeDef",
    "ProtectedQueryTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaTypeDef",
    "StartProtectedQueryInputRequestTypeDef",
    "StartProtectedQueryOutputTypeDef",
    "TableReferenceTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateCollaborationInputRequestTypeDef",
    "UpdateCollaborationOutputTypeDef",
    "UpdateConfiguredTableAnalysisRuleInputRequestTypeDef",
    "UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    "UpdateConfiguredTableAssociationInputRequestTypeDef",
    "UpdateConfiguredTableAssociationOutputTypeDef",
    "UpdateConfiguredTableInputRequestTypeDef",
    "UpdateConfiguredTableOutputTypeDef",
    "UpdateMembershipInputRequestTypeDef",
    "UpdateMembershipOutputTypeDef",
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
    },
    total=False,
)

class AnalysisRuleAggregationTypeDef(
    _RequiredAnalysisRuleAggregationTypeDef, _OptionalAnalysisRuleAggregationTypeDef
):
    pass

AnalysisRuleListTypeDef = TypedDict(
    "AnalysisRuleListTypeDef",
    {
        "joinColumns": List[str],
        "listColumns": List[str],
    },
)

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

DataEncryptionMetadataTypeDef = TypedDict(
    "DataEncryptionMetadataTypeDef",
    {
        "allowCleartext": bool,
        "allowDuplicates": bool,
        "allowJoinsOnColumnsWithDifferentNames": bool,
        "preserveNulls": bool,
    },
)

DeleteCollaborationInputRequestTypeDef = TypedDict(
    "DeleteCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
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

MemberSpecificationTypeDef = TypedDict(
    "MemberSpecificationTypeDef",
    {
        "accountId": str,
        "memberAbilities": List[MemberAbilityType],
        "displayName": str,
    },
)

_RequiredMemberSummaryTypeDef = TypedDict(
    "_RequiredMemberSummaryTypeDef",
    {
        "accountId": str,
        "status": MemberStatusType,
        "displayName": str,
        "abilities": List[MemberAbilityType],
        "createTime": datetime,
        "updateTime": datetime,
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
    },
)

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
        "sqlParameters": "ProtectedQuerySQLParametersTypeDef",
        "status": ProtectedQueryStatusType,
        "resultConfiguration": "ProtectedQueryResultConfigurationTypeDef",
    },
)
_OptionalProtectedQueryTypeDef = TypedDict(
    "_OptionalProtectedQueryTypeDef",
    {
        "statistics": "ProtectedQueryStatisticsTypeDef",
        "result": "ProtectedQueryResultTypeDef",
        "error": "ProtectedQueryErrorTypeDef",
    },
    total=False,
)

class ProtectedQueryTypeDef(_RequiredProtectedQueryTypeDef, _OptionalProtectedQueryTypeDef):
    pass

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

StartProtectedQueryInputRequestTypeDef = TypedDict(
    "StartProtectedQueryInputRequestTypeDef",
    {
        "type": Literal["SQL"],
        "membershipIdentifier": str,
        "sqlParameters": "ProtectedQuerySQLParametersTypeDef",
        "resultConfiguration": "ProtectedQueryResultConfigurationTypeDef",
    },
)

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
