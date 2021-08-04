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
    "AuthenticationTypeType",
    "AuthorizationTypeType",
    "ConflictDetectionTypeType",
    "ConflictHandlerTypeType",
    "DataSourceTypeType",
    "DefaultActionType",
    "FieldLogLevelType",
    "ListApiKeysPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListFunctionsPaginatorName",
    "ListGraphqlApisPaginatorName",
    "ListResolversByFunctionPaginatorName",
    "ListResolversPaginatorName",
    "ListTypesPaginatorName",
    "OutputTypeType",
    "RelationalDatabaseSourceTypeType",
    "ResolverKindType",
    "SchemaStatusType",
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
AuthenticationTypeType = Literal[
    "AMAZON_COGNITO_USER_POOLS", "API_KEY", "AWS_IAM", "AWS_LAMBDA", "OPENID_CONNECT"
]
AuthorizationTypeType = Literal["AWS_IAM"]
ConflictDetectionTypeType = Literal["NONE", "VERSION"]
ConflictHandlerTypeType = Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
DataSourceTypeType = Literal[
    "AMAZON_DYNAMODB", "AMAZON_ELASTICSEARCH", "AWS_LAMBDA", "HTTP", "NONE", "RELATIONAL_DATABASE"
]
DefaultActionType = Literal["ALLOW", "DENY"]
FieldLogLevelType = Literal["ALL", "ERROR", "NONE"]
ListApiKeysPaginatorName = Literal["list_api_keys"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListFunctionsPaginatorName = Literal["list_functions"]
ListGraphqlApisPaginatorName = Literal["list_graphql_apis"]
ListResolversByFunctionPaginatorName = Literal["list_resolvers_by_function"]
ListResolversPaginatorName = Literal["list_resolvers"]
ListTypesPaginatorName = Literal["list_types"]
OutputTypeType = Literal["JSON", "SDL"]
RelationalDatabaseSourceTypeType = Literal["RDS_HTTP_ENDPOINT"]
ResolverKindType = Literal["PIPELINE", "UNIT"]
SchemaStatusType = Literal[
    "ACTIVE", "DELETING", "FAILED", "NOT_APPLICABLE", "PROCESSING", "SUCCESS"
]
TypeDefinitionFormatType = Literal["JSON", "SDL"]
