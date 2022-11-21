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
    AuthenticationTypeType,
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
    OAuth2CustomPropTypeType,
    OAuth2GrantTypeType,
    OperatorPropertiesKeysType,
    OperatorsType,
    OperatorType,
    PathPrefixType,
    PrefixFormatType,
    PrefixTypeType,
    PrivateConnectionProvisioningFailureCauseType,
    PrivateConnectionProvisioningStatusType,
    S3ConnectorOperatorType,
    S3InputFileTypeType,
    SalesforceConnectorOperatorType,
    SalesforceDataTransferApiType,
    SAPODataConnectorOperatorType,
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
    "ApiKeyCredentialsTypeDef",
    "AuthParameterTypeDef",
    "AuthenticationConfigTypeDef",
    "BasicAuthCredentialsTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorDetailTypeDef",
    "ConnectorEntityFieldTypeDef",
    "ConnectorEntityTypeDef",
    "ConnectorMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "ConnectorProfileConfigTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "ConnectorProfileTypeDef",
    "ConnectorProvisioningConfigTypeDef",
    "ConnectorRuntimeSettingTypeDef",
    "CreateConnectorProfileRequestRequestTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CustomAuthConfigTypeDef",
    "CustomAuthCredentialsTypeDef",
    "CustomConnectorDestinationPropertiesTypeDef",
    "CustomConnectorProfileCredentialsTypeDef",
    "CustomConnectorProfilePropertiesTypeDef",
    "CustomConnectorSourcePropertiesTypeDef",
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
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
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
    "GlueDataCatalogConfigTypeDef",
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
    "LambdaConnectorProvisioningConfigTypeDef",
    "ListConnectorEntitiesRequestRequestTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "MarketoDestinationPropertiesTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MetadataCatalogConfigTypeDef",
    "MetadataCatalogDetailTypeDef",
    "OAuth2CredentialsTypeDef",
    "OAuth2CustomParameterTypeDef",
    "OAuth2DefaultsTypeDef",
    "OAuth2PropertiesTypeDef",
    "OAuthCredentialsTypeDef",
    "OAuthPropertiesTypeDef",
    "PrefixConfigTypeDef",
    "PrivateConnectionProvisioningStateTypeDef",
    "RangeTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "RegisterConnectorRequestRequestTypeDef",
    "RegisterConnectorResponseTypeDef",
    "RegistrationOutputTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationPropertiesTypeDef",
    "S3InputFormatConfigTypeDef",
    "S3OutputFormatConfigTypeDef",
    "S3SourcePropertiesTypeDef",
    "SAPODataConnectorProfileCredentialsTypeDef",
    "SAPODataConnectorProfilePropertiesTypeDef",
    "SAPODataDestinationPropertiesTypeDef",
    "SAPODataSourcePropertiesTypeDef",
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
    "SuccessResponseHandlingConfigTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UnregisterConnectorRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectorProfileRequestRequestTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateConnectorRegistrationRequestRequestTypeDef",
    "UpdateConnectorRegistrationResponseTypeDef",
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
        "targetFileSize": int,
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

_RequiredApiKeyCredentialsTypeDef = TypedDict(
    "_RequiredApiKeyCredentialsTypeDef",
    {
        "apiKey": str,
    },
)
_OptionalApiKeyCredentialsTypeDef = TypedDict(
    "_OptionalApiKeyCredentialsTypeDef",
    {
        "apiSecretKey": str,
    },
    total=False,
)

class ApiKeyCredentialsTypeDef(
    _RequiredApiKeyCredentialsTypeDef, _OptionalApiKeyCredentialsTypeDef
):
    pass

AuthParameterTypeDef = TypedDict(
    "AuthParameterTypeDef",
    {
        "key": str,
        "isRequired": bool,
        "label": str,
        "description": str,
        "isSensitiveField": bool,
        "connectorSuppliedValues": List[str],
    },
    total=False,
)

AuthenticationConfigTypeDef = TypedDict(
    "AuthenticationConfigTypeDef",
    {
        "isBasicAuthSupported": bool,
        "isApiKeyAuthSupported": bool,
        "isOAuth2Supported": bool,
        "isCustomAuthSupported": bool,
        "oAuth2Defaults": "OAuth2DefaultsTypeDef",
        "customAuthConfigs": List["CustomAuthConfigTypeDef"],
    },
    total=False,
)

BasicAuthCredentialsTypeDef = TypedDict(
    "BasicAuthCredentialsTypeDef",
    {
        "username": str,
        "password": str,
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
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "connectorDescription": str,
        "connectorOwner": str,
        "connectorName": str,
        "connectorVersion": str,
        "connectorArn": str,
        "connectorModes": List[str],
        "authenticationConfig": "AuthenticationConfigTypeDef",
        "connectorRuntimeSettings": List["ConnectorRuntimeSettingTypeDef"],
        "supportedApiVersions": List[str],
        "supportedOperators": List[OperatorsType],
        "supportedWriteOperations": List[WriteOperationTypeType],
        "connectorProvisioningType": Literal["LAMBDA"],
        "connectorProvisioningConfig": "ConnectorProvisioningConfigTypeDef",
        "logoURL": str,
        "registeredAt": datetime,
        "registeredBy": str,
    },
    total=False,
)

ConnectorDetailTypeDef = TypedDict(
    "ConnectorDetailTypeDef",
    {
        "connectorDescription": str,
        "connectorName": str,
        "connectorOwner": str,
        "connectorVersion": str,
        "applicationType": str,
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "registeredAt": datetime,
        "registeredBy": str,
        "connectorProvisioningType": Literal["LAMBDA"],
        "connectorModes": List[str],
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
        "parentIdentifier": str,
        "label": str,
        "isPrimaryKey": bool,
        "defaultValue": str,
        "isDeprecated": bool,
        "supportedFieldTypeDetails": "SupportedFieldTypeDetailsTypeDef",
        "description": str,
        "sourceProperties": "SourceFieldPropertiesTypeDef",
        "destinationProperties": "DestinationFieldPropertiesTypeDef",
        "customProperties": Dict[str, str],
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
        "SAPOData": Dict[str, Any],
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
        "SAPOData": SAPODataConnectorOperatorType,
        "CustomConnector": OperatorType,
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
        "SAPOData": "SAPODataConnectorProfileCredentialsTypeDef",
        "CustomConnector": "CustomConnectorProfileCredentialsTypeDef",
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
        "SAPOData": "SAPODataConnectorProfilePropertiesTypeDef",
        "CustomConnector": "CustomConnectorProfilePropertiesTypeDef",
    },
    total=False,
)

ConnectorProfileTypeDef = TypedDict(
    "ConnectorProfileTypeDef",
    {
        "connectorProfileArn": str,
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "connectionMode": ConnectionModeType,
        "credentialsArn": str,
        "connectorProfileProperties": "ConnectorProfilePropertiesTypeDef",
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "privateConnectionProvisioningState": "PrivateConnectionProvisioningStateTypeDef",
    },
    total=False,
)

ConnectorProvisioningConfigTypeDef = TypedDict(
    "ConnectorProvisioningConfigTypeDef",
    {
        "lambda": "LambdaConnectorProvisioningConfigTypeDef",
    },
    total=False,
)

ConnectorRuntimeSettingTypeDef = TypedDict(
    "ConnectorRuntimeSettingTypeDef",
    {
        "key": str,
        "dataType": str,
        "isRequired": bool,
        "label": str,
        "description": str,
        "scope": str,
        "connectorSuppliedValueOptions": List[str],
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
        "connectorLabel": str,
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
        "metadataCatalogConfig": "MetadataCatalogConfigTypeDef",
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

CustomAuthConfigTypeDef = TypedDict(
    "CustomAuthConfigTypeDef",
    {
        "customAuthenticationType": str,
        "authParameters": List["AuthParameterTypeDef"],
    },
    total=False,
)

_RequiredCustomAuthCredentialsTypeDef = TypedDict(
    "_RequiredCustomAuthCredentialsTypeDef",
    {
        "customAuthenticationType": str,
    },
)
_OptionalCustomAuthCredentialsTypeDef = TypedDict(
    "_OptionalCustomAuthCredentialsTypeDef",
    {
        "credentialsMap": Dict[str, str],
    },
    total=False,
)

class CustomAuthCredentialsTypeDef(
    _RequiredCustomAuthCredentialsTypeDef, _OptionalCustomAuthCredentialsTypeDef
):
    pass

_RequiredCustomConnectorDestinationPropertiesTypeDef = TypedDict(
    "_RequiredCustomConnectorDestinationPropertiesTypeDef",
    {
        "entityName": str,
    },
)
_OptionalCustomConnectorDestinationPropertiesTypeDef = TypedDict(
    "_OptionalCustomConnectorDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": WriteOperationTypeType,
        "idFieldNames": List[str],
        "customProperties": Dict[str, str],
    },
    total=False,
)

class CustomConnectorDestinationPropertiesTypeDef(
    _RequiredCustomConnectorDestinationPropertiesTypeDef,
    _OptionalCustomConnectorDestinationPropertiesTypeDef,
):
    pass

_RequiredCustomConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredCustomConnectorProfileCredentialsTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
    },
)
_OptionalCustomConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalCustomConnectorProfileCredentialsTypeDef",
    {
        "basic": "BasicAuthCredentialsTypeDef",
        "oauth2": "OAuth2CredentialsTypeDef",
        "apiKey": "ApiKeyCredentialsTypeDef",
        "custom": "CustomAuthCredentialsTypeDef",
    },
    total=False,
)

class CustomConnectorProfileCredentialsTypeDef(
    _RequiredCustomConnectorProfileCredentialsTypeDef,
    _OptionalCustomConnectorProfileCredentialsTypeDef,
):
    pass

CustomConnectorProfilePropertiesTypeDef = TypedDict(
    "CustomConnectorProfilePropertiesTypeDef",
    {
        "profileProperties": Dict[str, str],
        "oAuth2Properties": "OAuth2PropertiesTypeDef",
    },
    total=False,
)

_RequiredCustomConnectorSourcePropertiesTypeDef = TypedDict(
    "_RequiredCustomConnectorSourcePropertiesTypeDef",
    {
        "entityName": str,
    },
)
_OptionalCustomConnectorSourcePropertiesTypeDef = TypedDict(
    "_OptionalCustomConnectorSourcePropertiesTypeDef",
    {
        "customProperties": Dict[str, str],
    },
    total=False,
)

class CustomConnectorSourcePropertiesTypeDef(
    _RequiredCustomConnectorSourcePropertiesTypeDef, _OptionalCustomConnectorSourcePropertiesTypeDef
):
    pass

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
        "apiVersion": str,
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
        "connectorLabel": str,
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

_RequiredDescribeConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectorRequestRequestTypeDef",
    {
        "connectorType": ConnectorTypeType,
    },
)
_OptionalDescribeConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
    },
    total=False,
)

class DescribeConnectorRequestRequestTypeDef(
    _RequiredDescribeConnectorRequestRequestTypeDef, _OptionalDescribeConnectorRequestRequestTypeDef
):
    pass

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "connectorConfiguration": "ConnectorConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorsRequestRequestTypeDef = TypedDict(
    "DescribeConnectorsRequestRequestTypeDef",
    {
        "connectorTypes": List[ConnectorTypeType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeConnectorsResponseTypeDef = TypedDict(
    "DescribeConnectorsResponseTypeDef",
    {
        "connectorConfigurations": Dict[ConnectorTypeType, "ConnectorConfigurationTypeDef"],
        "connectors": List["ConnectorDetailTypeDef"],
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
        "metadataCatalogConfig": "MetadataCatalogConfigTypeDef",
        "lastRunMetadataCatalogDetails": List["MetadataCatalogDetailTypeDef"],
        "schemaVersion": int,
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
        "Marketo": "MarketoDestinationPropertiesTypeDef",
        "CustomConnector": "CustomConnectorDestinationPropertiesTypeDef",
        "SAPOData": "SAPODataDestinationPropertiesTypeDef",
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
        "isDefaultedOnCreate": bool,
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
        "apiVersion": str,
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
        "metadataCatalogDetails": List["MetadataCatalogDetailTypeDef"],
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
        "valueRegexPattern": str,
        "supportedDateFormat": str,
        "fieldValueRange": "RangeTypeDef",
        "fieldLengthRange": "RangeTypeDef",
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
        "sourceConnectorLabel": str,
        "destinationConnectorType": ConnectorTypeType,
        "destinationConnectorLabel": str,
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

GlueDataCatalogConfigTypeDef = TypedDict(
    "GlueDataCatalogConfigTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tablePrefix": str,
    },
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

LambdaConnectorProvisioningConfigTypeDef = TypedDict(
    "LambdaConnectorProvisioningConfigTypeDef",
    {
        "lambdaArn": str,
    },
)

ListConnectorEntitiesRequestRequestTypeDef = TypedDict(
    "ListConnectorEntitiesRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "entitiesPath": str,
        "apiVersion": str,
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

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List["ConnectorDetailTypeDef"],
        "nextToken": str,
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

_RequiredMarketoDestinationPropertiesTypeDef = TypedDict(
    "_RequiredMarketoDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalMarketoDestinationPropertiesTypeDef = TypedDict(
    "_OptionalMarketoDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
    },
    total=False,
)

class MarketoDestinationPropertiesTypeDef(
    _RequiredMarketoDestinationPropertiesTypeDef, _OptionalMarketoDestinationPropertiesTypeDef
):
    pass

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

MetadataCatalogConfigTypeDef = TypedDict(
    "MetadataCatalogConfigTypeDef",
    {
        "glueDataCatalog": "GlueDataCatalogConfigTypeDef",
    },
    total=False,
)

MetadataCatalogDetailTypeDef = TypedDict(
    "MetadataCatalogDetailTypeDef",
    {
        "catalogType": Literal["GLUE"],
        "tableName": str,
        "tableRegistrationOutput": "RegistrationOutputTypeDef",
        "partitionRegistrationOutput": "RegistrationOutputTypeDef",
    },
    total=False,
)

OAuth2CredentialsTypeDef = TypedDict(
    "OAuth2CredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

OAuth2CustomParameterTypeDef = TypedDict(
    "OAuth2CustomParameterTypeDef",
    {
        "key": str,
        "isRequired": bool,
        "label": str,
        "description": str,
        "isSensitiveField": bool,
        "connectorSuppliedValues": List[str],
        "type": OAuth2CustomPropTypeType,
    },
    total=False,
)

OAuth2DefaultsTypeDef = TypedDict(
    "OAuth2DefaultsTypeDef",
    {
        "oauthScopes": List[str],
        "tokenUrls": List[str],
        "authCodeUrls": List[str],
        "oauth2GrantTypesSupported": List[OAuth2GrantTypeType],
        "oauth2CustomProperties": List["OAuth2CustomParameterTypeDef"],
    },
    total=False,
)

_RequiredOAuth2PropertiesTypeDef = TypedDict(
    "_RequiredOAuth2PropertiesTypeDef",
    {
        "tokenUrl": str,
        "oAuth2GrantType": OAuth2GrantTypeType,
    },
)
_OptionalOAuth2PropertiesTypeDef = TypedDict(
    "_OptionalOAuth2PropertiesTypeDef",
    {
        "tokenUrlCustomProperties": Dict[str, str],
    },
    total=False,
)

class OAuth2PropertiesTypeDef(_RequiredOAuth2PropertiesTypeDef, _OptionalOAuth2PropertiesTypeDef):
    pass

_RequiredOAuthCredentialsTypeDef = TypedDict(
    "_RequiredOAuthCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalOAuthCredentialsTypeDef = TypedDict(
    "_OptionalOAuthCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": "ConnectorOAuthRequestTypeDef",
    },
    total=False,
)

class OAuthCredentialsTypeDef(_RequiredOAuthCredentialsTypeDef, _OptionalOAuthCredentialsTypeDef):
    pass

OAuthPropertiesTypeDef = TypedDict(
    "OAuthPropertiesTypeDef",
    {
        "tokenUrl": str,
        "authCodeUrl": str,
        "oAuthScopes": List[str],
    },
)

PrefixConfigTypeDef = TypedDict(
    "PrefixConfigTypeDef",
    {
        "prefixType": PrefixTypeType,
        "prefixFormat": PrefixFormatType,
        "pathPrefixHierarchy": List[PathPrefixType],
    },
    total=False,
)

PrivateConnectionProvisioningStateTypeDef = TypedDict(
    "PrivateConnectionProvisioningStateTypeDef",
    {
        "status": PrivateConnectionProvisioningStatusType,
        "failureMessage": str,
        "failureCause": PrivateConnectionProvisioningFailureCauseType,
    },
    total=False,
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "maximum": float,
        "minimum": float,
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

RegisterConnectorRequestRequestTypeDef = TypedDict(
    "RegisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
        "description": str,
        "connectorProvisioningType": Literal["LAMBDA"],
        "connectorProvisioningConfig": "ConnectorProvisioningConfigTypeDef",
    },
    total=False,
)

RegisterConnectorResponseTypeDef = TypedDict(
    "RegisterConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrationOutputTypeDef = TypedDict(
    "RegistrationOutputTypeDef",
    {
        "message": str,
        "result": str,
        "status": ExecutionStatusType,
    },
    total=False,
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

S3InputFormatConfigTypeDef = TypedDict(
    "S3InputFormatConfigTypeDef",
    {
        "s3InputFileType": S3InputFileTypeType,
    },
    total=False,
)

S3OutputFormatConfigTypeDef = TypedDict(
    "S3OutputFormatConfigTypeDef",
    {
        "fileType": FileTypeType,
        "prefixConfig": "PrefixConfigTypeDef",
        "aggregationConfig": "AggregationConfigTypeDef",
        "preserveSourceDataTyping": bool,
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
        "s3InputFormatConfig": "S3InputFormatConfigTypeDef",
    },
    total=False,
)

class S3SourcePropertiesTypeDef(
    _RequiredS3SourcePropertiesTypeDef, _OptionalS3SourcePropertiesTypeDef
):
    pass

SAPODataConnectorProfileCredentialsTypeDef = TypedDict(
    "SAPODataConnectorProfileCredentialsTypeDef",
    {
        "basicAuthCredentials": "BasicAuthCredentialsTypeDef",
        "oAuthCredentials": "OAuthCredentialsTypeDef",
    },
    total=False,
)

_RequiredSAPODataConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredSAPODataConnectorProfilePropertiesTypeDef",
    {
        "applicationHostUrl": str,
        "applicationServicePath": str,
        "portNumber": int,
        "clientNumber": str,
    },
)
_OptionalSAPODataConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalSAPODataConnectorProfilePropertiesTypeDef",
    {
        "logonLanguage": str,
        "privateLinkServiceName": str,
        "oAuthProperties": "OAuthPropertiesTypeDef",
    },
    total=False,
)

class SAPODataConnectorProfilePropertiesTypeDef(
    _RequiredSAPODataConnectorProfilePropertiesTypeDef,
    _OptionalSAPODataConnectorProfilePropertiesTypeDef,
):
    pass

_RequiredSAPODataDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSAPODataDestinationPropertiesTypeDef",
    {
        "objectPath": str,
    },
)
_OptionalSAPODataDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSAPODataDestinationPropertiesTypeDef",
    {
        "successResponseHandlingConfig": "SuccessResponseHandlingConfigTypeDef",
        "idFieldNames": List[str],
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class SAPODataDestinationPropertiesTypeDef(
    _RequiredSAPODataDestinationPropertiesTypeDef, _OptionalSAPODataDestinationPropertiesTypeDef
):
    pass

SAPODataSourcePropertiesTypeDef = TypedDict(
    "SAPODataSourcePropertiesTypeDef",
    {
        "objectPath": str,
    },
    total=False,
)

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
        "dataTransferApi": SalesforceDataTransferApiType,
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
        "dataTransferApis": List[SalesforceDataTransferApiType],
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
        "dataTransferApi": SalesforceDataTransferApiType,
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
        "flowErrorDeactivationThreshold": int,
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
        "SAPOData": "SAPODataSourcePropertiesTypeDef",
        "CustomConnector": "CustomConnectorSourcePropertiesTypeDef",
    },
    total=False,
)

SourceFieldPropertiesTypeDef = TypedDict(
    "SourceFieldPropertiesTypeDef",
    {
        "isRetrievable": bool,
        "isQueryable": bool,
        "isTimestampFieldForIncrementalQueries": bool,
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
        "apiVersion": str,
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

SuccessResponseHandlingConfigTypeDef = TypedDict(
    "SuccessResponseHandlingConfigTypeDef",
    {
        "bucketPrefix": str,
        "bucketName": str,
    },
    total=False,
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

_RequiredUnregisterConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredUnregisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
    },
)
_OptionalUnregisterConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalUnregisterConnectorRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class UnregisterConnectorRequestRequestTypeDef(
    _RequiredUnregisterConnectorRequestRequestTypeDef,
    _OptionalUnregisterConnectorRequestRequestTypeDef,
):
    pass

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

_RequiredUpdateConnectorRegistrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectorRegistrationRequestRequestTypeDef",
    {
        "connectorLabel": str,
    },
)
_OptionalUpdateConnectorRegistrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectorRegistrationRequestRequestTypeDef",
    {
        "description": str,
        "connectorProvisioningConfig": "ConnectorProvisioningConfigTypeDef",
    },
    total=False,
)

class UpdateConnectorRegistrationRequestRequestTypeDef(
    _RequiredUpdateConnectorRegistrationRequestRequestTypeDef,
    _OptionalUpdateConnectorRegistrationRequestRequestTypeDef,
):
    pass

UpdateConnectorRegistrationResponseTypeDef = TypedDict(
    "UpdateConnectorRegistrationResponseTypeDef",
    {
        "connectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": "TriggerConfigTypeDef",
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
        "destinationFlowConfigList": List["DestinationFlowConfigTypeDef"],
        "tasks": List["TaskTypeDef"],
    },
)
_OptionalUpdateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowRequestRequestTypeDef",
    {
        "description": str,
        "metadataCatalogConfig": "MetadataCatalogConfigTypeDef",
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

_RequiredVeevaSourcePropertiesTypeDef = TypedDict(
    "_RequiredVeevaSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalVeevaSourcePropertiesTypeDef = TypedDict(
    "_OptionalVeevaSourcePropertiesTypeDef",
    {
        "documentType": str,
        "includeSourceFiles": bool,
        "includeRenditions": bool,
        "includeAllVersions": bool,
    },
    total=False,
)

class VeevaSourcePropertiesTypeDef(
    _RequiredVeevaSourcePropertiesTypeDef, _OptionalVeevaSourcePropertiesTypeDef
):
    pass

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
