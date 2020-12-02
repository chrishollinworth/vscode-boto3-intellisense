"""
Main interface for appflow service type definitions.

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef

    data: AggregationConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorEntityFieldTypeDef",
    "ConnectorEntityTypeDef",
    "ConnectorMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "ConnectorProfileTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DestinationConnectorPropertiesTypeDef",
    "DestinationFieldPropertiesTypeDef",
    "DestinationFlowConfigTypeDef",
    "DynatraceConnectorProfileCredentialsTypeDef",
    "DynatraceConnectorProfilePropertiesTypeDef",
    "DynatraceSourcePropertiesTypeDef",
    "ErrorHandlingConfigTypeDef",
    "ErrorInfoTypeDef",
    "EventBridgeDestinationPropertiesTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionRecordTypeDef",
    "ExecutionResultTypeDef",
    "FieldTypeDetailsTypeDef",
    "FlowDefinitionTypeDef",
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    "GoogleAnalyticsMetadataTypeDef",
    "GoogleAnalyticsSourcePropertiesTypeDef",
    "IncrementalPullConfigTypeDef",
    "InforNexusConnectorProfileCredentialsTypeDef",
    "InforNexusConnectorProfilePropertiesTypeDef",
    "InforNexusSourcePropertiesTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "PrefixConfigTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "S3DestinationPropertiesTypeDef",
    "S3OutputFormatConfigTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceConnectorProfileCredentialsTypeDef",
    "SalesforceConnectorProfilePropertiesTypeDef",
    "SalesforceDestinationPropertiesTypeDef",
    "SalesforceMetadataTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "ServiceNowConnectorProfileCredentialsTypeDef",
    "ServiceNowConnectorProfilePropertiesTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SingularConnectorProfileCredentialsTypeDef",
    "SingularSourcePropertiesTypeDef",
    "SlackConnectorProfileCredentialsTypeDef",
    "SlackConnectorProfilePropertiesTypeDef",
    "SlackMetadataTypeDef",
    "SlackSourcePropertiesTypeDef",
    "SnowflakeConnectorProfileCredentialsTypeDef",
    "SnowflakeConnectorProfilePropertiesTypeDef",
    "SnowflakeDestinationPropertiesTypeDef",
    "SnowflakeMetadataTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFieldPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "TaskTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "ZendeskMetadataTypeDef",
    "ZendeskSourcePropertiesTypeDef",
    "ConnectorProfileConfigTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowResponseTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "DescribeFlowResponseTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateFlowResponseTypeDef",
)

AggregationConfigTypeDef = TypedDict(
    "AggregationConfigTypeDef", {"aggregationType": Literal["None", "SingleFile"]}, total=False
)

AmplitudeConnectorProfileCredentialsTypeDef = TypedDict(
    "AmplitudeConnectorProfileCredentialsTypeDef", {"apiKey": str, "secretKey": str}
)

AmplitudeSourcePropertiesTypeDef = TypedDict("AmplitudeSourcePropertiesTypeDef", {"object": str})

ConnectorConfigurationTypeDef = TypedDict(
    "ConnectorConfigurationTypeDef",
    {
        "canUseAsSource": bool,
        "canUseAsDestination": bool,
        "supportedDestinationConnectors": List[
            Literal[
                "Salesforce",
                "Singular",
                "Slack",
                "Redshift",
                "S3",
                "Marketo",
                "Googleanalytics",
                "Zendesk",
                "Servicenow",
                "Datadog",
                "Trendmicro",
                "Snowflake",
                "Dynatrace",
                "Infornexus",
                "Amplitude",
                "Veeva",
                "EventBridge",
                "Upsolver",
            ]
        ],
        "supportedSchedulingFrequencies": List[
            Literal["BYMINUTE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ONCE"]
        ],
        "isPrivateLinkEnabled": bool,
        "isPrivateLinkEndpointUrlRequired": bool,
        "supportedTriggerTypes": List[Literal["Scheduled", "Event", "OnDemand"]],
        "connectorMetadata": "ConnectorMetadataTypeDef",
    },
    total=False,
)

_RequiredConnectorEntityFieldTypeDef = TypedDict(
    "_RequiredConnectorEntityFieldTypeDef", {"identifier": str}
)
_OptionalConnectorEntityFieldTypeDef = TypedDict(
    "_OptionalConnectorEntityFieldTypeDef",
    {
        "label": str,
        "supportedFieldTypeDetails": "SupportedFieldTypeDetailsTypeDef",
        "description": str,
        "sourceProperties": "SourceFieldPropertiesTypeDef",
        "destinationProperties": "DestinationFieldPropertiesTypeDef",
    },
    total=False,
)


class ConnectorEntityFieldTypeDef(
    _RequiredConnectorEntityFieldTypeDef, _OptionalConnectorEntityFieldTypeDef
):
    pass


_RequiredConnectorEntityTypeDef = TypedDict("_RequiredConnectorEntityTypeDef", {"name": str})
_OptionalConnectorEntityTypeDef = TypedDict(
    "_OptionalConnectorEntityTypeDef", {"label": str, "hasNestedEntities": bool}, total=False
)


class ConnectorEntityTypeDef(_RequiredConnectorEntityTypeDef, _OptionalConnectorEntityTypeDef):
    pass


ConnectorMetadataTypeDef = TypedDict(
    "ConnectorMetadataTypeDef",
    {
        "Amplitude": Dict[str, Any],
        "Datadog": Dict[str, Any],
        "Dynatrace": Dict[str, Any],
        "GoogleAnalytics": "GoogleAnalyticsMetadataTypeDef",
        "InforNexus": Dict[str, Any],
        "Marketo": Dict[str, Any],
        "Redshift": Dict[str, Any],
        "S3": Dict[str, Any],
        "Salesforce": "SalesforceMetadataTypeDef",
        "ServiceNow": Dict[str, Any],
        "Singular": Dict[str, Any],
        "Slack": "SlackMetadataTypeDef",
        "Snowflake": "SnowflakeMetadataTypeDef",
        "Trendmicro": Dict[str, Any],
        "Veeva": Dict[str, Any],
        "Zendesk": "ZendeskMetadataTypeDef",
        "EventBridge": Dict[str, Any],
        "Upsolver": Dict[str, Any],
    },
    total=False,
)

ConnectorOAuthRequestTypeDef = TypedDict(
    "ConnectorOAuthRequestTypeDef", {"authCode": str, "redirectUri": str}, total=False
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Amplitude": Literal["BETWEEN"],
        "Datadog": Literal[
            "PROJECTION",
            "BETWEEN",
            "EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Dynatrace": Literal[
            "PROJECTION",
            "BETWEEN",
            "EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "GoogleAnalytics": Literal["PROJECTION", "BETWEEN"],
        "InforNexus": Literal[
            "PROJECTION",
            "BETWEEN",
            "EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Marketo": Literal[
            "PROJECTION",
            "LESS_THAN",
            "GREATER_THAN",
            "BETWEEN",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "S3": Literal[
            "PROJECTION",
            "LESS_THAN",
            "GREATER_THAN",
            "BETWEEN",
            "LESS_THAN_OR_EQUAL_TO",
            "GREATER_THAN_OR_EQUAL_TO",
            "EQUAL_TO",
            "NOT_EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Salesforce": Literal[
            "PROJECTION",
            "LESS_THAN",
            "CONTAINS",
            "GREATER_THAN",
            "BETWEEN",
            "LESS_THAN_OR_EQUAL_TO",
            "GREATER_THAN_OR_EQUAL_TO",
            "EQUAL_TO",
            "NOT_EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "ServiceNow": Literal[
            "PROJECTION",
            "CONTAINS",
            "LESS_THAN",
            "GREATER_THAN",
            "BETWEEN",
            "LESS_THAN_OR_EQUAL_TO",
            "GREATER_THAN_OR_EQUAL_TO",
            "EQUAL_TO",
            "NOT_EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Singular": Literal[
            "PROJECTION",
            "EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Slack": Literal[
            "PROJECTION",
            "LESS_THAN",
            "GREATER_THAN",
            "BETWEEN",
            "LESS_THAN_OR_EQUAL_TO",
            "GREATER_THAN_OR_EQUAL_TO",
            "EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Trendmicro": Literal[
            "PROJECTION",
            "EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Veeva": Literal[
            "PROJECTION",
            "LESS_THAN",
            "GREATER_THAN",
            "CONTAINS",
            "BETWEEN",
            "LESS_THAN_OR_EQUAL_TO",
            "GREATER_THAN_OR_EQUAL_TO",
            "EQUAL_TO",
            "NOT_EQUAL_TO",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
        "Zendesk": Literal[
            "PROJECTION",
            "GREATER_THAN",
            "ADDITION",
            "MULTIPLICATION",
            "DIVISION",
            "SUBTRACTION",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NUMERIC",
            "NO_OP",
        ],
    },
    total=False,
)

ConnectorProfileCredentialsTypeDef = TypedDict(
    "ConnectorProfileCredentialsTypeDef",
    {
        "Amplitude": "AmplitudeConnectorProfileCredentialsTypeDef",
        "Datadog": "DatadogConnectorProfileCredentialsTypeDef",
        "Dynatrace": "DynatraceConnectorProfileCredentialsTypeDef",
        "GoogleAnalytics": "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
        "InforNexus": "InforNexusConnectorProfileCredentialsTypeDef",
        "Marketo": "MarketoConnectorProfileCredentialsTypeDef",
        "Redshift": "RedshiftConnectorProfileCredentialsTypeDef",
        "Salesforce": "SalesforceConnectorProfileCredentialsTypeDef",
        "ServiceNow": "ServiceNowConnectorProfileCredentialsTypeDef",
        "Singular": "SingularConnectorProfileCredentialsTypeDef",
        "Slack": "SlackConnectorProfileCredentialsTypeDef",
        "Snowflake": "SnowflakeConnectorProfileCredentialsTypeDef",
        "Trendmicro": "TrendmicroConnectorProfileCredentialsTypeDef",
        "Veeva": "VeevaConnectorProfileCredentialsTypeDef",
        "Zendesk": "ZendeskConnectorProfileCredentialsTypeDef",
    },
    total=False,
)

ConnectorProfilePropertiesTypeDef = TypedDict(
    "ConnectorProfilePropertiesTypeDef",
    {
        "Amplitude": Dict[str, Any],
        "Datadog": "DatadogConnectorProfilePropertiesTypeDef",
        "Dynatrace": "DynatraceConnectorProfilePropertiesTypeDef",
        "GoogleAnalytics": Dict[str, Any],
        "InforNexus": "InforNexusConnectorProfilePropertiesTypeDef",
        "Marketo": "MarketoConnectorProfilePropertiesTypeDef",
        "Redshift": "RedshiftConnectorProfilePropertiesTypeDef",
        "Salesforce": "SalesforceConnectorProfilePropertiesTypeDef",
        "ServiceNow": "ServiceNowConnectorProfilePropertiesTypeDef",
        "Singular": Dict[str, Any],
        "Slack": "SlackConnectorProfilePropertiesTypeDef",
        "Snowflake": "SnowflakeConnectorProfilePropertiesTypeDef",
        "Trendmicro": Dict[str, Any],
        "Veeva": "VeevaConnectorProfilePropertiesTypeDef",
        "Zendesk": "ZendeskConnectorProfilePropertiesTypeDef",
    },
    total=False,
)

ConnectorProfileTypeDef = TypedDict(
    "ConnectorProfileTypeDef",
    {
        "connectorProfileArn": str,
        "connectorProfileName": str,
        "connectorType": Literal[
            "Salesforce",
            "Singular",
            "Slack",
            "Redshift",
            "S3",
            "Marketo",
            "Googleanalytics",
            "Zendesk",
            "Servicenow",
            "Datadog",
            "Trendmicro",
            "Snowflake",
            "Dynatrace",
            "Infornexus",
            "Amplitude",
            "Veeva",
            "EventBridge",
            "Upsolver",
        ],
        "connectionMode": Literal["Public", "Private"],
        "credentialsArn": str,
        "connectorProfileProperties": "ConnectorProfilePropertiesTypeDef",
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DatadogConnectorProfileCredentialsTypeDef = TypedDict(
    "DatadogConnectorProfileCredentialsTypeDef", {"apiKey": str, "applicationKey": str}
)

DatadogConnectorProfilePropertiesTypeDef = TypedDict(
    "DatadogConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

DatadogSourcePropertiesTypeDef = TypedDict("DatadogSourcePropertiesTypeDef", {"object": str})

DestinationConnectorPropertiesTypeDef = TypedDict(
    "DestinationConnectorPropertiesTypeDef",
    {
        "Redshift": "RedshiftDestinationPropertiesTypeDef",
        "S3": "S3DestinationPropertiesTypeDef",
        "Salesforce": "SalesforceDestinationPropertiesTypeDef",
        "Snowflake": "SnowflakeDestinationPropertiesTypeDef",
        "EventBridge": "EventBridgeDestinationPropertiesTypeDef",
        "Upsolver": "UpsolverDestinationPropertiesTypeDef",
    },
    total=False,
)

DestinationFieldPropertiesTypeDef = TypedDict(
    "DestinationFieldPropertiesTypeDef",
    {
        "isCreatable": bool,
        "isNullable": bool,
        "isUpsertable": bool,
        "isUpdatable": bool,
        "supportedWriteOperations": List[Literal["INSERT", "UPSERT", "UPDATE"]],
    },
    total=False,
)

_RequiredDestinationFlowConfigTypeDef = TypedDict(
    "_RequiredDestinationFlowConfigTypeDef",
    {
        "connectorType": Literal[
            "Salesforce",
            "Singular",
            "Slack",
            "Redshift",
            "S3",
            "Marketo",
            "Googleanalytics",
            "Zendesk",
            "Servicenow",
            "Datadog",
            "Trendmicro",
            "Snowflake",
            "Dynatrace",
            "Infornexus",
            "Amplitude",
            "Veeva",
            "EventBridge",
            "Upsolver",
        ],
        "destinationConnectorProperties": "DestinationConnectorPropertiesTypeDef",
    },
)
_OptionalDestinationFlowConfigTypeDef = TypedDict(
    "_OptionalDestinationFlowConfigTypeDef", {"connectorProfileName": str}, total=False
)


class DestinationFlowConfigTypeDef(
    _RequiredDestinationFlowConfigTypeDef, _OptionalDestinationFlowConfigTypeDef
):
    pass


DynatraceConnectorProfileCredentialsTypeDef = TypedDict(
    "DynatraceConnectorProfileCredentialsTypeDef", {"apiToken": str}
)

DynatraceConnectorProfilePropertiesTypeDef = TypedDict(
    "DynatraceConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

DynatraceSourcePropertiesTypeDef = TypedDict("DynatraceSourcePropertiesTypeDef", {"object": str})

ErrorHandlingConfigTypeDef = TypedDict(
    "ErrorHandlingConfigTypeDef",
    {"failOnFirstDestinationError": bool, "bucketPrefix": str, "bucketName": str},
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef", {"putFailuresCount": int, "executionMessage": str}, total=False
)

_RequiredEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredEventBridgeDestinationPropertiesTypeDef", {"object": str}
)
_OptionalEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalEventBridgeDestinationPropertiesTypeDef",
    {"errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class EventBridgeDestinationPropertiesTypeDef(
    _RequiredEventBridgeDestinationPropertiesTypeDef,
    _OptionalEventBridgeDestinationPropertiesTypeDef,
):
    pass


ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "mostRecentExecutionMessage": str,
        "mostRecentExecutionTime": datetime,
        "mostRecentExecutionStatus": Literal["InProgress", "Successful", "Error"],
    },
    total=False,
)

ExecutionRecordTypeDef = TypedDict(
    "ExecutionRecordTypeDef",
    {
        "executionId": str,
        "executionStatus": Literal["InProgress", "Successful", "Error"],
        "executionResult": "ExecutionResultTypeDef",
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

ExecutionResultTypeDef = TypedDict(
    "ExecutionResultTypeDef",
    {
        "errorInfo": "ErrorInfoTypeDef",
        "bytesProcessed": int,
        "bytesWritten": int,
        "recordsProcessed": int,
    },
    total=False,
)

_RequiredFieldTypeDetailsTypeDef = TypedDict(
    "_RequiredFieldTypeDetailsTypeDef",
    {
        "fieldType": str,
        "filterOperators": List[
            Literal[
                "PROJECTION",
                "LESS_THAN",
                "GREATER_THAN",
                "CONTAINS",
                "BETWEEN",
                "LESS_THAN_OR_EQUAL_TO",
                "GREATER_THAN_OR_EQUAL_TO",
                "EQUAL_TO",
                "NOT_EQUAL_TO",
                "ADDITION",
                "MULTIPLICATION",
                "DIVISION",
                "SUBTRACTION",
                "MASK_ALL",
                "MASK_FIRST_N",
                "MASK_LAST_N",
                "VALIDATE_NON_NULL",
                "VALIDATE_NON_ZERO",
                "VALIDATE_NON_NEGATIVE",
                "VALIDATE_NUMERIC",
                "NO_OP",
            ]
        ],
    },
)
_OptionalFieldTypeDetailsTypeDef = TypedDict(
    "_OptionalFieldTypeDetailsTypeDef", {"supportedValues": List[str]}, total=False
)


class FieldTypeDetailsTypeDef(_RequiredFieldTypeDetailsTypeDef, _OptionalFieldTypeDetailsTypeDef):
    pass


FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "flowStatus": Literal["Active", "Deprecated", "Deleted", "Draft", "Errored", "Suspended"],
        "sourceConnectorType": Literal[
            "Salesforce",
            "Singular",
            "Slack",
            "Redshift",
            "S3",
            "Marketo",
            "Googleanalytics",
            "Zendesk",
            "Servicenow",
            "Datadog",
            "Trendmicro",
            "Snowflake",
            "Dynatrace",
            "Infornexus",
            "Amplitude",
            "Veeva",
            "EventBridge",
            "Upsolver",
        ],
        "destinationConnectorType": Literal[
            "Salesforce",
            "Singular",
            "Slack",
            "Redshift",
            "S3",
            "Marketo",
            "Googleanalytics",
            "Zendesk",
            "Servicenow",
            "Datadog",
            "Trendmicro",
            "Snowflake",
            "Dynatrace",
            "Infornexus",
            "Amplitude",
            "Veeva",
            "EventBridge",
            "Upsolver",
        ],
        "triggerType": Literal["Scheduled", "Event", "OnDemand"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
        "lastRunExecutionDetails": "ExecutionDetailsTypeDef",
    },
    total=False,
)

_RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {"clientId": str, "clientSecret": str},
)
_OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {"accessToken": str, "refreshToken": str, "oAuthRequest": "ConnectorOAuthRequestTypeDef"},
    total=False,
)


class GoogleAnalyticsConnectorProfileCredentialsTypeDef(
    _RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef,
    _OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef,
):
    pass


GoogleAnalyticsMetadataTypeDef = TypedDict(
    "GoogleAnalyticsMetadataTypeDef", {"oAuthScopes": List[str]}, total=False
)

GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef", {"object": str}
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef", {"datetimeTypeFieldName": str}, total=False
)

InforNexusConnectorProfileCredentialsTypeDef = TypedDict(
    "InforNexusConnectorProfileCredentialsTypeDef",
    {"accessKeyId": str, "userId": str, "secretAccessKey": str, "datakey": str},
)

InforNexusConnectorProfilePropertiesTypeDef = TypedDict(
    "InforNexusConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

InforNexusSourcePropertiesTypeDef = TypedDict("InforNexusSourcePropertiesTypeDef", {"object": str})

_RequiredMarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredMarketoConnectorProfileCredentialsTypeDef", {"clientId": str, "clientSecret": str}
)
_OptionalMarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalMarketoConnectorProfileCredentialsTypeDef",
    {"accessToken": str, "oAuthRequest": "ConnectorOAuthRequestTypeDef"},
    total=False,
)


class MarketoConnectorProfileCredentialsTypeDef(
    _RequiredMarketoConnectorProfileCredentialsTypeDef,
    _OptionalMarketoConnectorProfileCredentialsTypeDef,
):
    pass


MarketoConnectorProfilePropertiesTypeDef = TypedDict(
    "MarketoConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

MarketoSourcePropertiesTypeDef = TypedDict("MarketoSourcePropertiesTypeDef", {"object": str})

PrefixConfigTypeDef = TypedDict(
    "PrefixConfigTypeDef",
    {
        "prefixType": Literal["FILENAME", "PATH", "PATH_AND_FILENAME"],
        "prefixFormat": Literal["YEAR", "MONTH", "DAY", "HOUR", "MINUTE"],
    },
    total=False,
)

RedshiftConnectorProfileCredentialsTypeDef = TypedDict(
    "RedshiftConnectorProfileCredentialsTypeDef", {"username": str, "password": str}
)

_RequiredRedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredRedshiftConnectorProfilePropertiesTypeDef",
    {"databaseUrl": str, "bucketName": str, "roleArn": str},
)
_OptionalRedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalRedshiftConnectorProfilePropertiesTypeDef", {"bucketPrefix": str}, total=False
)


class RedshiftConnectorProfilePropertiesTypeDef(
    _RequiredRedshiftConnectorProfilePropertiesTypeDef,
    _OptionalRedshiftConnectorProfilePropertiesTypeDef,
):
    pass


_RequiredRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_RequiredRedshiftDestinationPropertiesTypeDef", {"object": str, "intermediateBucketName": str}
)
_OptionalRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_OptionalRedshiftDestinationPropertiesTypeDef",
    {"bucketPrefix": str, "errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class RedshiftDestinationPropertiesTypeDef(
    _RequiredRedshiftDestinationPropertiesTypeDef, _OptionalRedshiftDestinationPropertiesTypeDef
):
    pass


_RequiredS3DestinationPropertiesTypeDef = TypedDict(
    "_RequiredS3DestinationPropertiesTypeDef", {"bucketName": str}
)
_OptionalS3DestinationPropertiesTypeDef = TypedDict(
    "_OptionalS3DestinationPropertiesTypeDef",
    {"bucketPrefix": str, "s3OutputFormatConfig": "S3OutputFormatConfigTypeDef"},
    total=False,
)


class S3DestinationPropertiesTypeDef(
    _RequiredS3DestinationPropertiesTypeDef, _OptionalS3DestinationPropertiesTypeDef
):
    pass


S3OutputFormatConfigTypeDef = TypedDict(
    "S3OutputFormatConfigTypeDef",
    {
        "fileType": Literal["CSV", "JSON", "PARQUET"],
        "prefixConfig": "PrefixConfigTypeDef",
        "aggregationConfig": "AggregationConfigTypeDef",
    },
    total=False,
)

_RequiredS3SourcePropertiesTypeDef = TypedDict(
    "_RequiredS3SourcePropertiesTypeDef", {"bucketName": str}
)
_OptionalS3SourcePropertiesTypeDef = TypedDict(
    "_OptionalS3SourcePropertiesTypeDef", {"bucketPrefix": str}, total=False
)


class S3SourcePropertiesTypeDef(
    _RequiredS3SourcePropertiesTypeDef, _OptionalS3SourcePropertiesTypeDef
):
    pass


SalesforceConnectorProfileCredentialsTypeDef = TypedDict(
    "SalesforceConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
        "clientCredentialsArn": str,
    },
    total=False,
)

SalesforceConnectorProfilePropertiesTypeDef = TypedDict(
    "SalesforceConnectorProfilePropertiesTypeDef",
    {"instanceUrl": str, "isSandboxEnvironment": bool},
    total=False,
)

_RequiredSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSalesforceDestinationPropertiesTypeDef", {"object": str}
)
_OptionalSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSalesforceDestinationPropertiesTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": Literal["INSERT", "UPSERT", "UPDATE"],
    },
    total=False,
)


class SalesforceDestinationPropertiesTypeDef(
    _RequiredSalesforceDestinationPropertiesTypeDef, _OptionalSalesforceDestinationPropertiesTypeDef
):
    pass


SalesforceMetadataTypeDef = TypedDict(
    "SalesforceMetadataTypeDef", {"oAuthScopes": List[str]}, total=False
)

_RequiredSalesforceSourcePropertiesTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesTypeDef", {"object": str}
)
_OptionalSalesforceSourcePropertiesTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesTypeDef",
    {"enableDynamicFieldUpdate": bool, "includeDeletedRecords": bool},
    total=False,
)


class SalesforceSourcePropertiesTypeDef(
    _RequiredSalesforceSourcePropertiesTypeDef, _OptionalSalesforceSourcePropertiesTypeDef
):
    pass


_RequiredScheduledTriggerPropertiesTypeDef = TypedDict(
    "_RequiredScheduledTriggerPropertiesTypeDef", {"scheduleExpression": str}
)
_OptionalScheduledTriggerPropertiesTypeDef = TypedDict(
    "_OptionalScheduledTriggerPropertiesTypeDef",
    {
        "dataPullMode": Literal["Incremental", "Complete"],
        "scheduleStartTime": datetime,
        "scheduleEndTime": datetime,
        "timezone": str,
    },
    total=False,
)


class ScheduledTriggerPropertiesTypeDef(
    _RequiredScheduledTriggerPropertiesTypeDef, _OptionalScheduledTriggerPropertiesTypeDef
):
    pass


ServiceNowConnectorProfileCredentialsTypeDef = TypedDict(
    "ServiceNowConnectorProfileCredentialsTypeDef", {"username": str, "password": str}
)

ServiceNowConnectorProfilePropertiesTypeDef = TypedDict(
    "ServiceNowConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

ServiceNowSourcePropertiesTypeDef = TypedDict("ServiceNowSourcePropertiesTypeDef", {"object": str})

SingularConnectorProfileCredentialsTypeDef = TypedDict(
    "SingularConnectorProfileCredentialsTypeDef", {"apiKey": str}
)

SingularSourcePropertiesTypeDef = TypedDict("SingularSourcePropertiesTypeDef", {"object": str})

_RequiredSlackConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredSlackConnectorProfileCredentialsTypeDef", {"clientId": str, "clientSecret": str}
)
_OptionalSlackConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalSlackConnectorProfileCredentialsTypeDef",
    {"accessToken": str, "oAuthRequest": "ConnectorOAuthRequestTypeDef"},
    total=False,
)


class SlackConnectorProfileCredentialsTypeDef(
    _RequiredSlackConnectorProfileCredentialsTypeDef,
    _OptionalSlackConnectorProfileCredentialsTypeDef,
):
    pass


SlackConnectorProfilePropertiesTypeDef = TypedDict(
    "SlackConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

SlackMetadataTypeDef = TypedDict("SlackMetadataTypeDef", {"oAuthScopes": List[str]}, total=False)

SlackSourcePropertiesTypeDef = TypedDict("SlackSourcePropertiesTypeDef", {"object": str})

SnowflakeConnectorProfileCredentialsTypeDef = TypedDict(
    "SnowflakeConnectorProfileCredentialsTypeDef", {"username": str, "password": str}
)

_RequiredSnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeConnectorProfilePropertiesTypeDef",
    {"warehouse": str, "stage": str, "bucketName": str},
)
_OptionalSnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeConnectorProfilePropertiesTypeDef",
    {"bucketPrefix": str, "privateLinkServiceName": str, "accountName": str, "region": str},
    total=False,
)


class SnowflakeConnectorProfilePropertiesTypeDef(
    _RequiredSnowflakeConnectorProfilePropertiesTypeDef,
    _OptionalSnowflakeConnectorProfilePropertiesTypeDef,
):
    pass


_RequiredSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeDestinationPropertiesTypeDef", {"object": str, "intermediateBucketName": str}
)
_OptionalSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeDestinationPropertiesTypeDef",
    {"bucketPrefix": str, "errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class SnowflakeDestinationPropertiesTypeDef(
    _RequiredSnowflakeDestinationPropertiesTypeDef, _OptionalSnowflakeDestinationPropertiesTypeDef
):
    pass


SnowflakeMetadataTypeDef = TypedDict(
    "SnowflakeMetadataTypeDef", {"supportedRegions": List[str]}, total=False
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Amplitude": "AmplitudeSourcePropertiesTypeDef",
        "Datadog": "DatadogSourcePropertiesTypeDef",
        "Dynatrace": "DynatraceSourcePropertiesTypeDef",
        "GoogleAnalytics": "GoogleAnalyticsSourcePropertiesTypeDef",
        "InforNexus": "InforNexusSourcePropertiesTypeDef",
        "Marketo": "MarketoSourcePropertiesTypeDef",
        "S3": "S3SourcePropertiesTypeDef",
        "Salesforce": "SalesforceSourcePropertiesTypeDef",
        "ServiceNow": "ServiceNowSourcePropertiesTypeDef",
        "Singular": "SingularSourcePropertiesTypeDef",
        "Slack": "SlackSourcePropertiesTypeDef",
        "Trendmicro": "TrendmicroSourcePropertiesTypeDef",
        "Veeva": "VeevaSourcePropertiesTypeDef",
        "Zendesk": "ZendeskSourcePropertiesTypeDef",
    },
    total=False,
)

SourceFieldPropertiesTypeDef = TypedDict(
    "SourceFieldPropertiesTypeDef", {"isRetrievable": bool, "isQueryable": bool}, total=False
)

_RequiredSourceFlowConfigTypeDef = TypedDict(
    "_RequiredSourceFlowConfigTypeDef",
    {
        "connectorType": Literal[
            "Salesforce",
            "Singular",
            "Slack",
            "Redshift",
            "S3",
            "Marketo",
            "Googleanalytics",
            "Zendesk",
            "Servicenow",
            "Datadog",
            "Trendmicro",
            "Snowflake",
            "Dynatrace",
            "Infornexus",
            "Amplitude",
            "Veeva",
            "EventBridge",
            "Upsolver",
        ],
        "sourceConnectorProperties": "SourceConnectorPropertiesTypeDef",
    },
)
_OptionalSourceFlowConfigTypeDef = TypedDict(
    "_OptionalSourceFlowConfigTypeDef",
    {"connectorProfileName": str, "incrementalPullConfig": "IncrementalPullConfigTypeDef"},
    total=False,
)


class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, _OptionalSourceFlowConfigTypeDef):
    pass


SupportedFieldTypeDetailsTypeDef = TypedDict(
    "SupportedFieldTypeDetailsTypeDef", {"v1": "FieldTypeDetailsTypeDef"}
)

_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "sourceFields": List[str],
        "taskType": Literal["Arithmetic", "Filter", "Map", "Mask", "Merge", "Truncate", "Validate"],
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "connectorOperator": "ConnectorOperatorTypeDef",
        "destinationField": str,
        "taskProperties": Dict[
            Literal[
                "VALUE",
                "VALUES",
                "DATA_TYPE",
                "UPPER_BOUND",
                "LOWER_BOUND",
                "SOURCE_DATA_TYPE",
                "DESTINATION_DATA_TYPE",
                "VALIDATION_ACTION",
                "MASK_VALUE",
                "MASK_LENGTH",
                "TRUNCATE_LENGTH",
                "MATH_OPERATION_FIELDS_ORDER",
                "CONCAT_FORMAT",
                "SUBFIELD_CATEGORY_MAP",
            ],
            str,
        ],
    },
    total=False,
)


class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass


TrendmicroConnectorProfileCredentialsTypeDef = TypedDict(
    "TrendmicroConnectorProfileCredentialsTypeDef", {"apiSecretKey": str}
)

TrendmicroSourcePropertiesTypeDef = TypedDict("TrendmicroSourcePropertiesTypeDef", {"object": str})

_RequiredTriggerConfigTypeDef = TypedDict(
    "_RequiredTriggerConfigTypeDef", {"triggerType": Literal["Scheduled", "Event", "OnDemand"]}
)
_OptionalTriggerConfigTypeDef = TypedDict(
    "_OptionalTriggerConfigTypeDef", {"triggerProperties": "TriggerPropertiesTypeDef"}, total=False
)


class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, _OptionalTriggerConfigTypeDef):
    pass


TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef", {"Scheduled": "ScheduledTriggerPropertiesTypeDef"}, total=False
)

_RequiredUpsolverDestinationPropertiesTypeDef = TypedDict(
    "_RequiredUpsolverDestinationPropertiesTypeDef",
    {"bucketName": str, "s3OutputFormatConfig": "UpsolverS3OutputFormatConfigTypeDef"},
)
_OptionalUpsolverDestinationPropertiesTypeDef = TypedDict(
    "_OptionalUpsolverDestinationPropertiesTypeDef", {"bucketPrefix": str}, total=False
)


class UpsolverDestinationPropertiesTypeDef(
    _RequiredUpsolverDestinationPropertiesTypeDef, _OptionalUpsolverDestinationPropertiesTypeDef
):
    pass


_RequiredUpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "_RequiredUpsolverS3OutputFormatConfigTypeDef", {"prefixConfig": "PrefixConfigTypeDef"}
)
_OptionalUpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "_OptionalUpsolverS3OutputFormatConfigTypeDef",
    {
        "fileType": Literal["CSV", "JSON", "PARQUET"],
        "aggregationConfig": "AggregationConfigTypeDef",
    },
    total=False,
)


class UpsolverS3OutputFormatConfigTypeDef(
    _RequiredUpsolverS3OutputFormatConfigTypeDef, _OptionalUpsolverS3OutputFormatConfigTypeDef
):
    pass


VeevaConnectorProfileCredentialsTypeDef = TypedDict(
    "VeevaConnectorProfileCredentialsTypeDef", {"username": str, "password": str}
)

VeevaConnectorProfilePropertiesTypeDef = TypedDict(
    "VeevaConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

VeevaSourcePropertiesTypeDef = TypedDict("VeevaSourcePropertiesTypeDef", {"object": str})

_RequiredZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredZendeskConnectorProfileCredentialsTypeDef", {"clientId": str, "clientSecret": str}
)
_OptionalZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalZendeskConnectorProfileCredentialsTypeDef",
    {"accessToken": str, "oAuthRequest": "ConnectorOAuthRequestTypeDef"},
    total=False,
)


class ZendeskConnectorProfileCredentialsTypeDef(
    _RequiredZendeskConnectorProfileCredentialsTypeDef,
    _OptionalZendeskConnectorProfileCredentialsTypeDef,
):
    pass


ZendeskConnectorProfilePropertiesTypeDef = TypedDict(
    "ZendeskConnectorProfilePropertiesTypeDef", {"instanceUrl": str}
)

ZendeskMetadataTypeDef = TypedDict(
    "ZendeskMetadataTypeDef", {"oAuthScopes": List[str]}, total=False
)

ZendeskSourcePropertiesTypeDef = TypedDict("ZendeskSourcePropertiesTypeDef", {"object": str})

ConnectorProfileConfigTypeDef = TypedDict(
    "ConnectorProfileConfigTypeDef",
    {
        "connectorProfileProperties": "ConnectorProfilePropertiesTypeDef",
        "connectorProfileCredentials": "ConnectorProfileCredentialsTypeDef",
    },
)

CreateConnectorProfileResponseTypeDef = TypedDict(
    "CreateConnectorProfileResponseTypeDef", {"connectorProfileArn": str}, total=False
)

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": Literal["Active", "Deprecated", "Deleted", "Draft", "Errored", "Suspended"],
    },
    total=False,
)

DescribeConnectorEntityResponseTypeDef = TypedDict(
    "DescribeConnectorEntityResponseTypeDef",
    {"connectorEntityFields": List["ConnectorEntityFieldTypeDef"]},
)

DescribeConnectorProfilesResponseTypeDef = TypedDict(
    "DescribeConnectorProfilesResponseTypeDef",
    {"connectorProfileDetails": List["ConnectorProfileTypeDef"], "nextToken": str},
    total=False,
)

DescribeConnectorsResponseTypeDef = TypedDict(
    "DescribeConnectorsResponseTypeDef",
    {
        "connectorConfigurations": Dict[
            Literal[
                "Salesforce",
                "Singular",
                "Slack",
                "Redshift",
                "S3",
                "Marketo",
                "Googleanalytics",
                "Zendesk",
                "Servicenow",
                "Datadog",
                "Trendmicro",
                "Snowflake",
                "Dynatrace",
                "Infornexus",
                "Amplitude",
                "Veeva",
                "EventBridge",
                "Upsolver",
            ],
            "ConnectorConfigurationTypeDef",
        ],
        "nextToken": str,
    },
    total=False,
)

DescribeFlowExecutionRecordsResponseTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsResponseTypeDef",
    {"flowExecutions": List["ExecutionRecordTypeDef"], "nextToken": str},
    total=False,
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "kmsArn": str,
        "flowStatus": Literal["Active", "Deprecated", "Deleted", "Draft", "Errored", "Suspended"],
        "flowStatusMessage": str,
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
        "destinationFlowConfigList": List["DestinationFlowConfigTypeDef"],
        "lastRunExecutionDetails": "ExecutionDetailsTypeDef",
        "triggerConfig": "TriggerConfigTypeDef",
        "tasks": List["TaskTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ListConnectorEntitiesResponseTypeDef = TypedDict(
    "ListConnectorEntitiesResponseTypeDef",
    {"connectorEntityMap": Dict[str, List["ConnectorEntityTypeDef"]]},
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {"flows": List["FlowDefinitionTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": Literal["Active", "Deprecated", "Deleted", "Draft", "Errored", "Suspended"],
        "executionId": str,
    },
    total=False,
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": Literal["Active", "Deprecated", "Deleted", "Draft", "Errored", "Suspended"],
    },
    total=False,
)

UpdateConnectorProfileResponseTypeDef = TypedDict(
    "UpdateConnectorProfileResponseTypeDef", {"connectorProfileArn": str}, total=False
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {"flowStatus": Literal["Active", "Deprecated", "Deleted", "Draft", "Errored", "Suspended"]},
    total=False,
)
