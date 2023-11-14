"""
Type annotations for appsync service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/literals.html)

Usage::

    ```python
    from mypy_boto3_appsync.literals import ApiCacheStatusType

    data: ApiCacheStatusType = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApiCacheStatusType",
    "ApiCacheTypeType",
    "ApiCachingBehaviorType",
    "AssociationStatusType",
    "AuthenticationTypeType",
    "AuthorizationTypeType",
    "ConflictDetectionTypeType",
    "ConflictHandlerTypeType",
    "DataSourceTypeType",
    "DefaultActionType",
    "FieldLogLevelType",
    "GraphQLApiTypeType",
    "GraphQLApiVisibilityType",
    "ListApiKeysPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListFunctionsPaginatorName",
    "ListGraphqlApisPaginatorName",
    "ListResolversByFunctionPaginatorName",
    "ListResolversPaginatorName",
    "ListTypesPaginatorName",
    "MergeTypeType",
    "OutputTypeType",
    "OwnershipType",
    "RelationalDatabaseSourceTypeType",
    "ResolverKindType",
    "RuntimeNameType",
    "SchemaStatusType",
    "SourceApiAssociationStatusType",
    "TypeDefinitionFormatType",
)

ApiCacheStatusType = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED", "MODIFYING"]
ApiCacheTypeType = Literal[
    "LARGE",
    "LARGE_12X",
    "LARGE_2X",
    "LARGE_4X",
    "LARGE_8X",
    "MEDIUM",
    "R4_2XLARGE",
    "R4_4XLARGE",
    "R4_8XLARGE",
    "R4_LARGE",
    "R4_XLARGE",
    "SMALL",
    "T2_MEDIUM",
    "T2_SMALL",
    "XLARGE",
]
ApiCachingBehaviorType = Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"]
AssociationStatusType = Literal["FAILED", "PROCESSING", "SUCCESS"]
AuthenticationTypeType = Literal[
    "AMAZON_COGNITO_USER_POOLS", "API_KEY", "AWS_IAM", "AWS_LAMBDA", "OPENID_CONNECT"
]
AuthorizationTypeType = Literal["AWS_IAM"]
ConflictDetectionTypeType = Literal["NONE", "VERSION"]
ConflictHandlerTypeType = Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
DataSourceTypeType = Literal[
    "AMAZON_DYNAMODB",
    "AMAZON_ELASTICSEARCH",
    "AMAZON_EVENTBRIDGE",
    "AMAZON_OPENSEARCH_SERVICE",
    "AWS_LAMBDA",
    "HTTP",
    "NONE",
    "RELATIONAL_DATABASE",
]
DefaultActionType = Literal["ALLOW", "DENY"]
FieldLogLevelType = Literal["ALL", "ERROR", "NONE"]
GraphQLApiTypeType = Literal["GRAPHQL", "MERGED"]
GraphQLApiVisibilityType = Literal["GLOBAL", "PRIVATE"]
ListApiKeysPaginatorName = Literal["list_api_keys"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListFunctionsPaginatorName = Literal["list_functions"]
ListGraphqlApisPaginatorName = Literal["list_graphql_apis"]
ListResolversByFunctionPaginatorName = Literal["list_resolvers_by_function"]
ListResolversPaginatorName = Literal["list_resolvers"]
ListTypesPaginatorName = Literal["list_types"]
MergeTypeType = Literal["AUTO_MERGE", "MANUAL_MERGE"]
OutputTypeType = Literal["JSON", "SDL"]
OwnershipType = Literal["CURRENT_ACCOUNT", "OTHER_ACCOUNTS"]
RelationalDatabaseSourceTypeType = Literal["RDS_HTTP_ENDPOINT"]
ResolverKindType = Literal["PIPELINE", "UNIT"]
RuntimeNameType = Literal["APPSYNC_JS"]
SchemaStatusType = Literal[
    "ACTIVE", "DELETING", "FAILED", "NOT_APPLICABLE", "PROCESSING", "SUCCESS"
]
SourceApiAssociationStatusType = Literal[
    "AUTO_MERGE_SCHEDULE_FAILED",
    "DELETION_FAILED",
    "DELETION_IN_PROGRESS",
    "DELETION_SCHEDULED",
    "MERGE_FAILED",
    "MERGE_IN_PROGRESS",
    "MERGE_SCHEDULED",
    "MERGE_SUCCESS",
]
TypeDefinitionFormatType = Literal["JSON", "SDL"]
