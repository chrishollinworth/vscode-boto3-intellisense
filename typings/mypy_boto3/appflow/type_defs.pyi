"""
Type annotations for appflow service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef

    data: AggregationConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AggregationTypeType,
    ConnectionModeType,
    ConnectorTypeType,
    DatadogConnectorOperatorType,
    DataPullModeType,
    DynatraceConnectorOperatorType,
    ExecutionStatusType,
    FileTypeType,
    FlowStatusType,
    GoogleAnalyticsConnectorOperatorType,
    InforNexusConnectorOperatorType,
    MarketoConnectorOperatorType,
    OperatorPropertiesKeysType,
    OperatorType,
    PrefixFormatType,
    PrefixTypeType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ScheduleFrequencyTypeType,
    ServiceNowConnectorOperatorType,
    SingularConnectorOperatorType,
    SlackConnectorOperatorType,
    TaskTypeType,
    TrendmicroConnectorOperatorType,
    TriggerTypeType,
    VeevaConnectorOperatorType,
    WriteOperationTypeType,
    ZendeskConnectorOperatorType,
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
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorEntityFieldTypeDef",
    "ConnectorEntityTypeDef",
    "ConnectorMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "ConnectorProfileConfigTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "ConnectorProfileTypeDef",
    "CreateConnectorProfileRequestRequestTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CustomerProfilesDestinationPropertiesTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DeleteConnectorProfileRequestRequestTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DescribeConnectorEntityRequestRequestTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorProfilesRequestRequestTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DescribeConnectorsRequestRequestTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeFlowExecutionRecordsRequestRequestTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
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
    "HoneycodeConnectorProfileCredentialsTypeDef",
    "HoneycodeDestinationPropertiesTypeDef",
    "HoneycodeMetadataTypeDef",
    "IncrementalPullConfigTypeDef",
    "InforNexusConnectorProfileCredentialsTypeDef",
    "InforNexusConnectorProfilePropertiesTypeDef",
    "InforNexusSourcePropertiesTypeDef",
    "ListConnectorEntitiesRequestRequestTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "PrefixConfigTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "ResponseMetadataTypeDef",
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
    "StartFlowRequestRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestRequestTypeDef",
    "StopFlowResponseTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectorProfileRequestRequestTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateFlowRequestRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "ZendeskDestinationPropertiesTypeDef",
    "ZendeskMetadataTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

AggregationConfigTypeDef = TypedDict(
    "AggregationConfigTypeDef",
    {
        "aggregationType": AggregationTypeType,
    },
    total=False,
)

AmplitudeConnectorProfileCredentialsTypeDef = TypedDict(
    "AmplitudeConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "secretKey": str,
    },
)

AmplitudeSourcePropertiesTypeDef = TypedDict(
    "AmplitudeSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ConnectorConfigurationTypeDef = TypedDict(
    "ConnectorConfigurationTypeDef",
    {
        "canUseAsSource": bool,
        "canUseAsDestination": bool,
        "supportedDestinationConnectors": List[ConnectorTypeType],
        "supportedSchedulingFrequencies": List[ScheduleFrequencyTypeType],
        "isPrivateLinkEnabled": bool,
        "isPrivateLinkEndpointUrlRequired": bool,
        "supportedTriggerTypes": List[TriggerTypeType],
        "connectorMetadata": "ConnectorMetadataTypeDef",
    },
    total=False,
)

_RequiredConnectorEntityFieldTypeDef = TypedDict(
    "_RequiredConnectorEntityFieldTypeDef",
    {
        "identifier": str,
    },
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

_RequiredConnectorEntityTypeDef = TypedDict(
    "_RequiredConnectorEntityTypeDef",
    {
        "name": str,
    },
)
_OptionalConnectorEntityTypeDef = TypedDict(
    "_OptionalConnectorEntityTypeDef",
    {
        "label": str,
        "hasNestedEntities": bool,
    },
    total=False,
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
        "CustomerProfiles": Dict[str, Any],
        "Honeycode": "HoneycodeMetadataTypeDef",
    },
    total=False,
)

ConnectorOAuthRequestTypeDef = TypedDict(
    "ConnectorOAuthRequestTypeDef",
    {
        "authCode": str,
        "redirectUri": str,
    },
    total=False,
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Amplitude": Literal["BETWEEN"],
        "Datadog": DatadogConnectorOperatorType,
        "Dynatrace": DynatraceConnectorOperatorType,
        "GoogleAnalytics": GoogleAnalyticsConnectorOperatorType,
        "InforNexus": InforNexusConnectorOperatorType,
        "Marketo": MarketoConnectorOperatorType,
        "S3": S3ConnectorOperatorType,
        "Salesforce": SalesforceConnectorOperatorType,
        "ServiceNow": ServiceNowConnectorOperatorType,
        "Singular": SingularConnectorOperatorType,
        "Slack": SlackConnectorOperatorType,
        "Trendmicro": TrendmicroConnectorOperatorType,
        "Veeva": VeevaConnectorOperatorType,
        "Zendesk": ZendeskConnectorOperatorType,
    },
    total=False,
)

ConnectorProfileConfigTypeDef = TypedDict(
    "ConnectorProfileConfigTypeDef",
    {
        "connectorProfileProperties": "ConnectorProfilePropertiesTypeDef",
        "connectorProfileCredentials": "ConnectorProfileCredentialsTypeDef",
    },
)

ConnectorProfileCredentialsTypeDef = TypedDict(
    "ConnectorProfileCredentialsTypeDef",
    {
        "Amplitude": "AmplitudeConnectorProfileCredentialsTypeDef",
        "Datadog": "DatadogConnectorProfileCredentialsTypeDef",
        "Dynatrace": "DynatraceConnectorProfileCredentialsTypeDef",
        "GoogleAnalytics": "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
        "Honeycode": "HoneycodeConnectorProfileCredentialsTypeDef",
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
        "Honeycode": Dict[str, Any],
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
        "connectorType": ConnectorTypeType,
        "connectionMode": ConnectionModeType,
        "credentialsArn": str,
        "connectorProfileProperties": "ConnectorProfilePropertiesTypeDef",
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

_RequiredCreateConnectorProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": "ConnectorProfileConfigTypeDef",
    },
)
_OptionalCreateConnectorProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorProfileRequestRequestTypeDef",
    {
        "kmsArn": str,
    },
    total=False,
)

class CreateConnectorProfileRequestRequestTypeDef(
    _RequiredCreateConnectorProfileRequestRequestTypeDef,
    _OptionalCreateConnectorProfileRequestRequestTypeDef,
):
    pass

CreateConnectorProfileResponseTypeDef = TypedDict(
    "CreateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": "TriggerConfigTypeDef",
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
        "destinationFlowConfigList": List["DestinationFlowConfigTypeDef"],
        "tasks": List["TaskTypeDef"],
    },
)
_OptionalCreateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowRequestRequestTypeDef",
    {
        "description": str,
        "kmsArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFlowRequestRequestTypeDef(
    _RequiredCreateFlowRequestRequestTypeDef, _OptionalCreateFlowRequestRequestTypeDef
):
    pass

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomerProfilesDestinationPropertiesTypeDef = TypedDict(
    "_RequiredCustomerProfilesDestinationPropertiesTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCustomerProfilesDestinationPropertiesTypeDef = TypedDict(
    "_OptionalCustomerProfilesDestinationPropertiesTypeDef",
    {
        "objectTypeName": str,
    },
    total=False,
)

class CustomerProfilesDestinationPropertiesTypeDef(
    _RequiredCustomerProfilesDestinationPropertiesTypeDef,
    _OptionalCustomerProfilesDestinationPropertiesTypeDef,
):
    pass

DatadogConnectorProfileCredentialsTypeDef = TypedDict(
    "DatadogConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "applicationKey": str,
    },
)

DatadogConnectorProfilePropertiesTypeDef = TypedDict(
    "DatadogConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

DatadogSourcePropertiesTypeDef = TypedDict(
    "DatadogSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredDeleteConnectorProfileRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
    },
)
_OptionalDeleteConnectorProfileRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteConnectorProfileRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class DeleteConnectorProfileRequestRequestTypeDef(
    _RequiredDeleteConnectorProfileRequestRequestTypeDef,
    _OptionalDeleteConnectorProfileRequestRequestTypeDef,
):
    pass

_RequiredDeleteFlowRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)
_OptionalDeleteFlowRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFlowRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class DeleteFlowRequestRequestTypeDef(
    _RequiredDeleteFlowRequestRequestTypeDef, _OptionalDeleteFlowRequestRequestTypeDef
):
    pass

_RequiredDescribeConnectorEntityRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectorEntityRequestRequestTypeDef",
    {
        "connectorEntityName": str,
    },
)
_OptionalDescribeConnectorEntityRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectorEntityRequestRequestTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "connectorProfileName": str,
    },
    total=False,
)

class DescribeConnectorEntityRequestRequestTypeDef(
    _RequiredDescribeConnectorEntityRequestRequestTypeDef,
    _OptionalDescribeConnectorEntityRequestRequestTypeDef,
):
    pass

DescribeConnectorEntityResponseTypeDef = TypedDict(
    "DescribeConnectorEntityResponseTypeDef",
    {
        "connectorEntityFields": List["ConnectorEntityFieldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorProfilesRequestRequestTypeDef = TypedDict(
    "DescribeConnectorProfilesRequestRequestTypeDef",
    {
        "connectorProfileNames": List[str],
        "connectorType": ConnectorTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeConnectorProfilesResponseTypeDef = TypedDict(
    "DescribeConnectorProfilesResponseTypeDef",
    {
        "connectorProfileDetails": List["ConnectorProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorsRequestRequestTypeDef = TypedDict(
    "DescribeConnectorsRequestRequestTypeDef",
    {
        "connectorTypes": List[ConnectorTypeType],
        "nextToken": str,
    },
    total=False,
)

DescribeConnectorsResponseTypeDef = TypedDict(
    "DescribeConnectorsResponseTypeDef",
    {
        "connectorConfigurations": Dict[ConnectorTypeType, "ConnectorConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFlowExecutionRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFlowExecutionRecordsRequestRequestTypeDef",
    {
        "flowName": str,
    },
)
_OptionalDescribeFlowExecutionRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFlowExecutionRecordsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class DescribeFlowExecutionRecordsRequestRequestTypeDef(
    _RequiredDescribeFlowExecutionRecordsRequestRequestTypeDef,
    _OptionalDescribeFlowExecutionRecordsRequestRequestTypeDef,
):
    pass

DescribeFlowExecutionRecordsResponseTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsResponseTypeDef",
    {
        "flowExecutions": List["ExecutionRecordTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "kmsArn": str,
        "flowStatus": FlowStatusType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConnectorPropertiesTypeDef = TypedDict(
    "DestinationConnectorPropertiesTypeDef",
    {
        "Redshift": "RedshiftDestinationPropertiesTypeDef",
        "S3": "S3DestinationPropertiesTypeDef",
        "Salesforce": "SalesforceDestinationPropertiesTypeDef",
        "Snowflake": "SnowflakeDestinationPropertiesTypeDef",
        "EventBridge": "EventBridgeDestinationPropertiesTypeDef",
        "LookoutMetrics": Dict[str, Any],
        "Upsolver": "UpsolverDestinationPropertiesTypeDef",
        "Honeycode": "HoneycodeDestinationPropertiesTypeDef",
        "CustomerProfiles": "CustomerProfilesDestinationPropertiesTypeDef",
        "Zendesk": "ZendeskDestinationPropertiesTypeDef",
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
        "supportedWriteOperations": List[WriteOperationTypeType],
    },
    total=False,
)

_RequiredDestinationFlowConfigTypeDef = TypedDict(
    "_RequiredDestinationFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "destinationConnectorProperties": "DestinationConnectorPropertiesTypeDef",
    },
)
_OptionalDestinationFlowConfigTypeDef = TypedDict(
    "_OptionalDestinationFlowConfigTypeDef",
    {
        "connectorProfileName": str,
    },
    total=False,
)

class DestinationFlowConfigTypeDef(
    _RequiredDestinationFlowConfigTypeDef, _OptionalDestinationFlowConfigTypeDef
):
    pass

DynatraceConnectorProfileCredentialsTypeDef = TypedDict(
    "DynatraceConnectorProfileCredentialsTypeDef",
    {
        "apiToken": str,
    },
)

DynatraceConnectorProfilePropertiesTypeDef = TypedDict(
    "DynatraceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

DynatraceSourcePropertiesTypeDef = TypedDict(
    "DynatraceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ErrorHandlingConfigTypeDef = TypedDict(
    "ErrorHandlingConfigTypeDef",
    {
        "failOnFirstDestinationError": bool,
        "bucketPrefix": str,
        "bucketName": str,
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "putFailuresCount": int,
        "executionMessage": str,
    },
    total=False,
)

_RequiredEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredEventBridgeDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalEventBridgeDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
    },
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
        "mostRecentExecutionStatus": ExecutionStatusType,
    },
    total=False,
)

ExecutionRecordTypeDef = TypedDict(
    "ExecutionRecordTypeDef",
    {
        "executionId": str,
        "executionStatus": ExecutionStatusType,
        "executionResult": "ExecutionResultTypeDef",
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "dataPullStartTime": datetime,
        "dataPullEndTime": datetime,
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
        "filterOperators": List[OperatorType],
    },
)
_OptionalFieldTypeDetailsTypeDef = TypedDict(
    "_OptionalFieldTypeDetailsTypeDef",
    {
        "supportedValues": List[str],
    },
    total=False,
)

class FieldTypeDetailsTypeDef(_RequiredFieldTypeDetailsTypeDef, _OptionalFieldTypeDetailsTypeDef):
    pass

FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "flowStatus": FlowStatusType,
        "sourceConnectorType": ConnectorTypeType,
        "destinationConnectorType": ConnectorTypeType,
        "triggerType": TriggerTypeType,
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
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

class GoogleAnalyticsConnectorProfileCredentialsTypeDef(
    _RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef,
    _OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef,
):
    pass

GoogleAnalyticsMetadataTypeDef = TypedDict(
    "GoogleAnalyticsMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

HoneycodeConnectorProfileCredentialsTypeDef = TypedDict(
    "HoneycodeConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

_RequiredHoneycodeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredHoneycodeDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalHoneycodeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalHoneycodeDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
    },
    total=False,
)

class HoneycodeDestinationPropertiesTypeDef(
    _RequiredHoneycodeDestinationPropertiesTypeDef, _OptionalHoneycodeDestinationPropertiesTypeDef
):
    pass

HoneycodeMetadataTypeDef = TypedDict(
    "HoneycodeMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "datetimeTypeFieldName": str,
    },
    total=False,
)

InforNexusConnectorProfileCredentialsTypeDef = TypedDict(
    "InforNexusConnectorProfileCredentialsTypeDef",
    {
        "accessKeyId": str,
        "userId": str,
        "secretAccessKey": str,
        "datakey": str,
    },
)

InforNexusConnectorProfilePropertiesTypeDef = TypedDict(
    "InforNexusConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

InforNexusSourcePropertiesTypeDef = TypedDict(
    "InforNexusSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ListConnectorEntitiesRequestRequestTypeDef = TypedDict(
    "ListConnectorEntitiesRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "entitiesPath": str,
    },
    total=False,
)

ListConnectorEntitiesResponseTypeDef = TypedDict(
    "ListConnectorEntitiesResponseTypeDef",
    {
        "connectorEntityMap": Dict[str, List["ConnectorEntityTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "flows": List["FlowDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredMarketoConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalMarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalMarketoConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

class MarketoConnectorProfileCredentialsTypeDef(
    _RequiredMarketoConnectorProfileCredentialsTypeDef,
    _OptionalMarketoConnectorProfileCredentialsTypeDef,
):
    pass

MarketoConnectorProfilePropertiesTypeDef = TypedDict(
    "MarketoConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

PrefixConfigTypeDef = TypedDict(
    "PrefixConfigTypeDef",
    {
        "prefixType": PrefixTypeType,
        "prefixFormat": PrefixFormatType,
    },
    total=False,
)

RedshiftConnectorProfileCredentialsTypeDef = TypedDict(
    "RedshiftConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

_RequiredRedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredRedshiftConnectorProfilePropertiesTypeDef",
    {
        "databaseUrl": str,
        "bucketName": str,
        "roleArn": str,
    },
)
_OptionalRedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalRedshiftConnectorProfilePropertiesTypeDef",
    {
        "bucketPrefix": str,
    },
    total=False,
)

class RedshiftConnectorProfilePropertiesTypeDef(
    _RequiredRedshiftConnectorProfilePropertiesTypeDef,
    _OptionalRedshiftConnectorProfilePropertiesTypeDef,
):
    pass

_RequiredRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_RequiredRedshiftDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
    },
)
_OptionalRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_OptionalRedshiftDestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
    },
    total=False,
)

class RedshiftDestinationPropertiesTypeDef(
    _RequiredRedshiftDestinationPropertiesTypeDef, _OptionalRedshiftDestinationPropertiesTypeDef
):
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

_RequiredS3DestinationPropertiesTypeDef = TypedDict(
    "_RequiredS3DestinationPropertiesTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3DestinationPropertiesTypeDef = TypedDict(
    "_OptionalS3DestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
        "s3OutputFormatConfig": "S3OutputFormatConfigTypeDef",
    },
    total=False,
)

class S3DestinationPropertiesTypeDef(
    _RequiredS3DestinationPropertiesTypeDef, _OptionalS3DestinationPropertiesTypeDef
):
    pass

S3OutputFormatConfigTypeDef = TypedDict(
    "S3OutputFormatConfigTypeDef",
    {
        "fileType": FileTypeType,
        "prefixConfig": "PrefixConfigTypeDef",
        "aggregationConfig": "AggregationConfigTypeDef",
    },
    total=False,
)

_RequiredS3SourcePropertiesTypeDef = TypedDict(
    "_RequiredS3SourcePropertiesTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3SourcePropertiesTypeDef = TypedDict(
    "_OptionalS3SourcePropertiesTypeDef",
    {
        "bucketPrefix": str,
    },
    total=False,
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
    {
        "instanceUrl": str,
        "isSandboxEnvironment": bool,
    },
    total=False,
)

_RequiredSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSalesforceDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSalesforceDestinationPropertiesTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class SalesforceDestinationPropertiesTypeDef(
    _RequiredSalesforceDestinationPropertiesTypeDef, _OptionalSalesforceDestinationPropertiesTypeDef
):
    pass

SalesforceMetadataTypeDef = TypedDict(
    "SalesforceMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

_RequiredSalesforceSourcePropertiesTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalSalesforceSourcePropertiesTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesTypeDef",
    {
        "enableDynamicFieldUpdate": bool,
        "includeDeletedRecords": bool,
    },
    total=False,
)

class SalesforceSourcePropertiesTypeDef(
    _RequiredSalesforceSourcePropertiesTypeDef, _OptionalSalesforceSourcePropertiesTypeDef
):
    pass

_RequiredScheduledTriggerPropertiesTypeDef = TypedDict(
    "_RequiredScheduledTriggerPropertiesTypeDef",
    {
        "scheduleExpression": str,
    },
)
_OptionalScheduledTriggerPropertiesTypeDef = TypedDict(
    "_OptionalScheduledTriggerPropertiesTypeDef",
    {
        "dataPullMode": DataPullModeType,
        "scheduleStartTime": Union[datetime, str],
        "scheduleEndTime": Union[datetime, str],
        "timezone": str,
        "scheduleOffset": int,
        "firstExecutionFrom": Union[datetime, str],
    },
    total=False,
)

class ScheduledTriggerPropertiesTypeDef(
    _RequiredScheduledTriggerPropertiesTypeDef, _OptionalScheduledTriggerPropertiesTypeDef
):
    pass

ServiceNowConnectorProfileCredentialsTypeDef = TypedDict(
    "ServiceNowConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

ServiceNowConnectorProfilePropertiesTypeDef = TypedDict(
    "ServiceNowConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SingularConnectorProfileCredentialsTypeDef = TypedDict(
    "SingularConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
    },
)

SingularSourcePropertiesTypeDef = TypedDict(
    "SingularSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredSlackConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredSlackConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalSlackConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalSlackConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

class SlackConnectorProfileCredentialsTypeDef(
    _RequiredSlackConnectorProfileCredentialsTypeDef,
    _OptionalSlackConnectorProfileCredentialsTypeDef,
):
    pass

SlackConnectorProfilePropertiesTypeDef = TypedDict(
    "SlackConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

SlackMetadataTypeDef = TypedDict(
    "SlackMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

SlackSourcePropertiesTypeDef = TypedDict(
    "SlackSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SnowflakeConnectorProfileCredentialsTypeDef = TypedDict(
    "SnowflakeConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

_RequiredSnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeConnectorProfilePropertiesTypeDef",
    {
        "warehouse": str,
        "stage": str,
        "bucketName": str,
    },
)
_OptionalSnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeConnectorProfilePropertiesTypeDef",
    {
        "bucketPrefix": str,
        "privateLinkServiceName": str,
        "accountName": str,
        "region": str,
    },
    total=False,
)

class SnowflakeConnectorProfilePropertiesTypeDef(
    _RequiredSnowflakeConnectorProfilePropertiesTypeDef,
    _OptionalSnowflakeConnectorProfilePropertiesTypeDef,
):
    pass

_RequiredSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
    },
)
_OptionalSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeDestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
    },
    total=False,
)

class SnowflakeDestinationPropertiesTypeDef(
    _RequiredSnowflakeDestinationPropertiesTypeDef, _OptionalSnowflakeDestinationPropertiesTypeDef
):
    pass

SnowflakeMetadataTypeDef = TypedDict(
    "SnowflakeMetadataTypeDef",
    {
        "supportedRegions": List[str],
    },
    total=False,
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
    "SourceFieldPropertiesTypeDef",
    {
        "isRetrievable": bool,
        "isQueryable": bool,
    },
    total=False,
)

_RequiredSourceFlowConfigTypeDef = TypedDict(
    "_RequiredSourceFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "sourceConnectorProperties": "SourceConnectorPropertiesTypeDef",
    },
)
_OptionalSourceFlowConfigTypeDef = TypedDict(
    "_OptionalSourceFlowConfigTypeDef",
    {
        "connectorProfileName": str,
        "incrementalPullConfig": "IncrementalPullConfigTypeDef",
    },
    total=False,
)

class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, _OptionalSourceFlowConfigTypeDef):
    pass

StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "executionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SupportedFieldTypeDetailsTypeDef = TypedDict(
    "SupportedFieldTypeDetailsTypeDef",
    {
        "v1": "FieldTypeDetailsTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "sourceFields": List[str],
        "taskType": TaskTypeType,
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "connectorOperator": "ConnectorOperatorTypeDef",
        "destinationField": str,
        "taskProperties": Dict[OperatorPropertiesKeysType, str],
    },
    total=False,
)

class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass

TrendmicroConnectorProfileCredentialsTypeDef = TypedDict(
    "TrendmicroConnectorProfileCredentialsTypeDef",
    {
        "apiSecretKey": str,
    },
)

TrendmicroSourcePropertiesTypeDef = TypedDict(
    "TrendmicroSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredTriggerConfigTypeDef = TypedDict(
    "_RequiredTriggerConfigTypeDef",
    {
        "triggerType": TriggerTypeType,
    },
)
_OptionalTriggerConfigTypeDef = TypedDict(
    "_OptionalTriggerConfigTypeDef",
    {
        "triggerProperties": "TriggerPropertiesTypeDef",
    },
    total=False,
)

class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, _OptionalTriggerConfigTypeDef):
    pass

TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": "ScheduledTriggerPropertiesTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateConnectorProfileRequestRequestTypeDef = TypedDict(
    "UpdateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": "ConnectorProfileConfigTypeDef",
    },
)

UpdateConnectorProfileResponseTypeDef = TypedDict(
    "UpdateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": "TriggerConfigTypeDef",
        "destinationFlowConfigList": List["DestinationFlowConfigTypeDef"],
        "tasks": List["TaskTypeDef"],
    },
)
_OptionalUpdateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowRequestRequestTypeDef",
    {
        "description": str,
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
    },
    total=False,
)

class UpdateFlowRequestRequestTypeDef(
    _RequiredUpdateFlowRequestRequestTypeDef, _OptionalUpdateFlowRequestRequestTypeDef
):
    pass

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpsolverDestinationPropertiesTypeDef = TypedDict(
    "_RequiredUpsolverDestinationPropertiesTypeDef",
    {
        "bucketName": str,
        "s3OutputFormatConfig": "UpsolverS3OutputFormatConfigTypeDef",
    },
)
_OptionalUpsolverDestinationPropertiesTypeDef = TypedDict(
    "_OptionalUpsolverDestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
    },
    total=False,
)

class UpsolverDestinationPropertiesTypeDef(
    _RequiredUpsolverDestinationPropertiesTypeDef, _OptionalUpsolverDestinationPropertiesTypeDef
):
    pass

_RequiredUpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "_RequiredUpsolverS3OutputFormatConfigTypeDef",
    {
        "prefixConfig": "PrefixConfigTypeDef",
    },
)
_OptionalUpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "_OptionalUpsolverS3OutputFormatConfigTypeDef",
    {
        "fileType": FileTypeType,
        "aggregationConfig": "AggregationConfigTypeDef",
    },
    total=False,
)

class UpsolverS3OutputFormatConfigTypeDef(
    _RequiredUpsolverS3OutputFormatConfigTypeDef, _OptionalUpsolverS3OutputFormatConfigTypeDef
):
    pass

VeevaConnectorProfileCredentialsTypeDef = TypedDict(
    "VeevaConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

VeevaConnectorProfilePropertiesTypeDef = TypedDict(
    "VeevaConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

VeevaSourcePropertiesTypeDef = TypedDict(
    "VeevaSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredZendeskConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalZendeskConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

class ZendeskConnectorProfileCredentialsTypeDef(
    _RequiredZendeskConnectorProfileCredentialsTypeDef,
    _OptionalZendeskConnectorProfileCredentialsTypeDef,
):
    pass

ZendeskConnectorProfilePropertiesTypeDef = TypedDict(
    "ZendeskConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

_RequiredZendeskDestinationPropertiesTypeDef = TypedDict(
    "_RequiredZendeskDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalZendeskDestinationPropertiesTypeDef = TypedDict(
    "_OptionalZendeskDestinationPropertiesTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class ZendeskDestinationPropertiesTypeDef(
    _RequiredZendeskDestinationPropertiesTypeDef, _OptionalZendeskDestinationPropertiesTypeDef
):
    pass

ZendeskMetadataTypeDef = TypedDict(
    "ZendeskMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
