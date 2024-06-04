"""
Type annotations for appflow service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/literals.html)

Usage::

    ```python
    from mypy_boto3_appflow.literals import AggregationTypeType

    data: AggregationTypeType = "None"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregationTypeType",
    "AmplitudeConnectorOperatorType",
    "AuthenticationTypeType",
    "CatalogTypeType",
    "ConnectionModeType",
    "ConnectorProvisioningTypeType",
    "ConnectorTypeType",
    "DataPullModeType",
    "DataTransferApiTypeType",
    "DatadogConnectorOperatorType",
    "DynatraceConnectorOperatorType",
    "ExecutionStatusType",
    "FileTypeType",
    "FlowStatusType",
    "GoogleAnalyticsConnectorOperatorType",
    "InforNexusConnectorOperatorType",
    "MarketoConnectorOperatorType",
    "OAuth2CustomPropTypeType",
    "OAuth2GrantTypeType",
    "OperatorPropertiesKeysType",
    "OperatorType",
    "OperatorsType",
    "PardotConnectorOperatorType",
    "PathPrefixType",
    "PrefixFormatType",
    "PrefixTypeType",
    "PrivateConnectionProvisioningFailureCauseType",
    "PrivateConnectionProvisioningStatusType",
    "S3ConnectorOperatorType",
    "S3InputFileTypeType",
    "SAPODataConnectorOperatorType",
    "SalesforceConnectorOperatorType",
    "SalesforceDataTransferApiType",
    "ScheduleFrequencyTypeType",
    "ServiceNowConnectorOperatorType",
    "SingularConnectorOperatorType",
    "SlackConnectorOperatorType",
    "SupportedDataTransferTypeType",
    "TaskTypeType",
    "TrendmicroConnectorOperatorType",
    "TriggerTypeType",
    "VeevaConnectorOperatorType",
    "WriteOperationTypeType",
    "ZendeskConnectorOperatorType",
)

AggregationTypeType = Literal["None", "SingleFile"]
AmplitudeConnectorOperatorType = Literal["BETWEEN"]
AuthenticationTypeType = Literal["APIKEY", "BASIC", "CUSTOM", "OAUTH2"]
CatalogTypeType = Literal["GLUE"]
ConnectionModeType = Literal["Private", "Public"]
ConnectorProvisioningTypeType = Literal["LAMBDA"]
ConnectorTypeType = Literal[
    "Amplitude",
    "CustomConnector",
    "CustomerProfiles",
    "Datadog",
    "Dynatrace",
    "EventBridge",
    "Googleanalytics",
    "Honeycode",
    "Infornexus",
    "LookoutMetrics",
    "Marketo",
    "Pardot",
    "Redshift",
    "S3",
    "SAPOData",
    "Salesforce",
    "Servicenow",
    "Singular",
    "Slack",
    "Snowflake",
    "Trendmicro",
    "Upsolver",
    "Veeva",
    "Zendesk",
]
DataPullModeType = Literal["Complete", "Incremental"]
DataTransferApiTypeType = Literal["ASYNC", "AUTOMATIC", "SYNC"]
DatadogConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
DynatraceConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
ExecutionStatusType = Literal["CancelStarted", "Canceled", "Error", "InProgress", "Successful"]
FileTypeType = Literal["CSV", "JSON", "PARQUET"]
FlowStatusType = Literal["Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"]
GoogleAnalyticsConnectorOperatorType = Literal["BETWEEN", "PROJECTION"]
InforNexusConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
MarketoConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "GREATER_THAN",
    "LESS_THAN",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
OAuth2CustomPropTypeType = Literal["AUTH_URL", "TOKEN_URL"]
OAuth2GrantTypeType = Literal["AUTHORIZATION_CODE", "CLIENT_CREDENTIALS", "JWT_BEARER"]
OperatorPropertiesKeysType = Literal[
    "CONCAT_FORMAT",
    "DATA_TYPE",
    "DESTINATION_DATA_TYPE",
    "EXCLUDE_SOURCE_FIELDS_LIST",
    "INCLUDE_NEW_FIELDS",
    "LOWER_BOUND",
    "MASK_LENGTH",
    "MASK_VALUE",
    "MATH_OPERATION_FIELDS_ORDER",
    "ORDERED_PARTITION_KEYS_LIST",
    "SOURCE_DATA_TYPE",
    "SUBFIELD_CATEGORY_MAP",
    "TRUNCATE_LENGTH",
    "UPPER_BOUND",
    "VALIDATION_ACTION",
    "VALUE",
    "VALUES",
]
OperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
OperatorsType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
PardotConnectorOperatorType = Literal[
    "ADDITION",
    "DIVISION",
    "EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
PathPrefixType = Literal["EXECUTION_ID", "SCHEMA_VERSION"]
PrefixFormatType = Literal["DAY", "HOUR", "MINUTE", "MONTH", "YEAR"]
PrefixTypeType = Literal["FILENAME", "PATH", "PATH_AND_FILENAME"]
PrivateConnectionProvisioningFailureCauseType = Literal[
    "ACCESS_DENIED", "CONNECTOR_AUTHENTICATION", "CONNECTOR_SERVER", "INTERNAL_SERVER", "VALIDATION"
]
PrivateConnectionProvisioningStatusType = Literal["CREATED", "FAILED", "PENDING"]
S3ConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
S3InputFileTypeType = Literal["CSV", "JSON"]
SAPODataConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SalesforceConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SalesforceDataTransferApiType = Literal["AUTOMATIC", "BULKV2", "REST_SYNC"]
ScheduleFrequencyTypeType = Literal["BYMINUTE", "DAILY", "HOURLY", "MONTHLY", "ONCE", "WEEKLY"]
ServiceNowConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SingularConnectorOperatorType = Literal[
    "ADDITION",
    "DIVISION",
    "EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SlackConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SupportedDataTransferTypeType = Literal["FILE", "RECORD"]
TaskTypeType = Literal[
    "Arithmetic",
    "Filter",
    "Map",
    "Map_all",
    "Mask",
    "Merge",
    "Partition",
    "Passthrough",
    "Truncate",
    "Validate",
]
TrendmicroConnectorOperatorType = Literal[
    "ADDITION",
    "DIVISION",
    "EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
TriggerTypeType = Literal["Event", "OnDemand", "Scheduled"]
VeevaConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
WriteOperationTypeType = Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]
ZendeskConnectorOperatorType = Literal[
    "ADDITION",
    "DIVISION",
    "GREATER_THAN",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
