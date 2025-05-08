"""
Type annotations for appflow service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef

    data: AggregationConfigTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AggregationTypeType,
    AuthenticationTypeType,
    ConnectionModeType,
    ConnectorTypeType,
    DatadogConnectorOperatorType,
    DataPullModeType,
    DataTransferApiTypeType,
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
    PardotConnectorOperatorType,
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
    SupportedDataTransferTypeType,
    TaskTypeType,
    TrendmicroConnectorOperatorType,
    TriggerTypeType,
    VeevaConnectorOperatorType,
    WriteOperationTypeType,
    ZendeskConnectorOperatorType,
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
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ApiKeyCredentialsTypeDef",
    "AuthParameterTypeDef",
    "AuthenticationConfigTypeDef",
    "BasicAuthCredentialsTypeDef",
    "CancelFlowExecutionsRequestTypeDef",
    "CancelFlowExecutionsResponseTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorDetailTypeDef",
    "ConnectorEntityFieldTypeDef",
    "ConnectorEntityTypeDef",
    "ConnectorMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "ConnectorProfileConfigTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorProfilePropertiesOutputTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "ConnectorProfilePropertiesUnionTypeDef",
    "ConnectorProfileTypeDef",
    "ConnectorProvisioningConfigTypeDef",
    "ConnectorRuntimeSettingTypeDef",
    "CreateConnectorProfileRequestTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CustomAuthConfigTypeDef",
    "CustomAuthCredentialsTypeDef",
    "CustomConnectorDestinationPropertiesOutputTypeDef",
    "CustomConnectorDestinationPropertiesTypeDef",
    "CustomConnectorDestinationPropertiesUnionTypeDef",
    "CustomConnectorProfileCredentialsTypeDef",
    "CustomConnectorProfilePropertiesOutputTypeDef",
    "CustomConnectorProfilePropertiesTypeDef",
    "CustomConnectorProfilePropertiesUnionTypeDef",
    "CustomConnectorSourcePropertiesOutputTypeDef",
    "CustomConnectorSourcePropertiesTypeDef",
    "CustomerProfilesDestinationPropertiesTypeDef",
    "DataTransferApiTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DeleteConnectorProfileRequestTypeDef",
    "DeleteFlowRequestTypeDef",
    "DescribeConnectorEntityRequestTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorProfilesRequestTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DescribeConnectorRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeConnectorsRequestTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeFlowExecutionRecordsRequestTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "DescribeFlowRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "DestinationConnectorPropertiesOutputTypeDef",
    "DestinationConnectorPropertiesTypeDef",
    "DestinationConnectorPropertiesUnionTypeDef",
    "DestinationFieldPropertiesTypeDef",
    "DestinationFlowConfigOutputTypeDef",
    "DestinationFlowConfigTypeDef",
    "DestinationFlowConfigUnionTypeDef",
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
    "ListConnectorEntitiesRequestTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ListConnectorsRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListFlowsRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
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
    "OAuth2PropertiesOutputTypeDef",
    "OAuth2PropertiesTypeDef",
    "OAuth2PropertiesUnionTypeDef",
    "OAuthCredentialsTypeDef",
    "OAuthPropertiesOutputTypeDef",
    "OAuthPropertiesTypeDef",
    "OAuthPropertiesUnionTypeDef",
    "PardotConnectorProfileCredentialsTypeDef",
    "PardotConnectorProfilePropertiesTypeDef",
    "PardotSourcePropertiesTypeDef",
    "PrefixConfigOutputTypeDef",
    "PrefixConfigTypeDef",
    "PrefixConfigUnionTypeDef",
    "PrivateConnectionProvisioningStateTypeDef",
    "RangeTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "RegisterConnectorRequestTypeDef",
    "RegisterConnectorResponseTypeDef",
    "RegistrationOutputTypeDef",
    "ResetConnectorMetadataCacheRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationPropertiesOutputTypeDef",
    "S3DestinationPropertiesTypeDef",
    "S3DestinationPropertiesUnionTypeDef",
    "S3InputFormatConfigTypeDef",
    "S3OutputFormatConfigOutputTypeDef",
    "S3OutputFormatConfigTypeDef",
    "S3OutputFormatConfigUnionTypeDef",
    "S3SourcePropertiesTypeDef",
    "SAPODataConnectorProfileCredentialsTypeDef",
    "SAPODataConnectorProfilePropertiesOutputTypeDef",
    "SAPODataConnectorProfilePropertiesTypeDef",
    "SAPODataConnectorProfilePropertiesUnionTypeDef",
    "SAPODataDestinationPropertiesOutputTypeDef",
    "SAPODataDestinationPropertiesTypeDef",
    "SAPODataDestinationPropertiesUnionTypeDef",
    "SAPODataPaginationConfigTypeDef",
    "SAPODataParallelismConfigTypeDef",
    "SAPODataSourcePropertiesTypeDef",
    "SalesforceConnectorProfileCredentialsTypeDef",
    "SalesforceConnectorProfilePropertiesTypeDef",
    "SalesforceDestinationPropertiesOutputTypeDef",
    "SalesforceDestinationPropertiesTypeDef",
    "SalesforceDestinationPropertiesUnionTypeDef",
    "SalesforceMetadataTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesOutputTypeDef",
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
    "SourceConnectorPropertiesOutputTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFieldPropertiesTypeDef",
    "SourceFlowConfigOutputTypeDef",
    "SourceFlowConfigTypeDef",
    "SourceFlowConfigUnionTypeDef",
    "StartFlowRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestTypeDef",
    "StopFlowResponseTypeDef",
    "SuccessResponseHandlingConfigTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "TagResourceRequestTypeDef",
    "TaskOutputTypeDef",
    "TaskTypeDef",
    "TaskUnionTypeDef",
    "TimestampTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "TriggerConfigOutputTypeDef",
    "TriggerConfigTypeDef",
    "TriggerConfigUnionTypeDef",
    "TriggerPropertiesOutputTypeDef",
    "TriggerPropertiesTypeDef",
    "UnregisterConnectorRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectorProfileRequestTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateConnectorRegistrationRequestTypeDef",
    "UpdateConnectorRegistrationResponseTypeDef",
    "UpdateFlowRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpsolverDestinationPropertiesOutputTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "UpsolverDestinationPropertiesUnionTypeDef",
    "UpsolverS3OutputFormatConfigOutputTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "UpsolverS3OutputFormatConfigUnionTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "ZendeskDestinationPropertiesOutputTypeDef",
    "ZendeskDestinationPropertiesTypeDef",
    "ZendeskDestinationPropertiesUnionTypeDef",
    "ZendeskMetadataTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

class AggregationConfigTypeDef(TypedDict):
    aggregationType: NotRequired[AggregationTypeType]
    targetFileSize: NotRequired[int]

class AmplitudeConnectorProfileCredentialsTypeDef(TypedDict):
    apiKey: str
    secretKey: str

AmplitudeSourcePropertiesTypeDef = TypedDict(
    "AmplitudeSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class ApiKeyCredentialsTypeDef(TypedDict):
    apiKey: str
    apiSecretKey: NotRequired[str]

class AuthParameterTypeDef(TypedDict):
    key: NotRequired[str]
    isRequired: NotRequired[bool]
    label: NotRequired[str]
    description: NotRequired[str]
    isSensitiveField: NotRequired[bool]
    connectorSuppliedValues: NotRequired[List[str]]

class BasicAuthCredentialsTypeDef(TypedDict):
    username: str
    password: str

class CancelFlowExecutionsRequestTypeDef(TypedDict):
    flowName: str
    executionIds: NotRequired[Sequence[str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ConnectorRuntimeSettingTypeDef(TypedDict):
    key: NotRequired[str]
    dataType: NotRequired[str]
    isRequired: NotRequired[bool]
    label: NotRequired[str]
    description: NotRequired[str]
    scope: NotRequired[str]
    connectorSuppliedValueOptions: NotRequired[List[str]]

DataTransferApiTypeDef = TypedDict(
    "DataTransferApiTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[DataTransferApiTypeType],
    },
)

class ConnectorDetailTypeDef(TypedDict):
    connectorDescription: NotRequired[str]
    connectorName: NotRequired[str]
    connectorOwner: NotRequired[str]
    connectorVersion: NotRequired[str]
    applicationType: NotRequired[str]
    connectorType: NotRequired[ConnectorTypeType]
    connectorLabel: NotRequired[str]
    registeredAt: NotRequired[datetime]
    registeredBy: NotRequired[str]
    connectorProvisioningType: NotRequired[Literal["LAMBDA"]]
    connectorModes: NotRequired[List[str]]
    supportedDataTransferTypes: NotRequired[List[SupportedDataTransferTypeType]]

class DestinationFieldPropertiesTypeDef(TypedDict):
    isCreatable: NotRequired[bool]
    isNullable: NotRequired[bool]
    isUpsertable: NotRequired[bool]
    isUpdatable: NotRequired[bool]
    isDefaultedOnCreate: NotRequired[bool]
    supportedWriteOperations: NotRequired[List[WriteOperationTypeType]]

class SourceFieldPropertiesTypeDef(TypedDict):
    isRetrievable: NotRequired[bool]
    isQueryable: NotRequired[bool]
    isTimestampFieldForIncrementalQueries: NotRequired[bool]

class ConnectorEntityTypeDef(TypedDict):
    name: str
    label: NotRequired[str]
    hasNestedEntities: NotRequired[bool]

class GoogleAnalyticsMetadataTypeDef(TypedDict):
    oAuthScopes: NotRequired[List[str]]

class HoneycodeMetadataTypeDef(TypedDict):
    oAuthScopes: NotRequired[List[str]]

class SalesforceMetadataTypeDef(TypedDict):
    oAuthScopes: NotRequired[List[str]]
    dataTransferApis: NotRequired[List[SalesforceDataTransferApiType]]
    oauth2GrantTypesSupported: NotRequired[List[OAuth2GrantTypeType]]

class SlackMetadataTypeDef(TypedDict):
    oAuthScopes: NotRequired[List[str]]

class SnowflakeMetadataTypeDef(TypedDict):
    supportedRegions: NotRequired[List[str]]

class ZendeskMetadataTypeDef(TypedDict):
    oAuthScopes: NotRequired[List[str]]

class ConnectorOAuthRequestTypeDef(TypedDict):
    authCode: NotRequired[str]
    redirectUri: NotRequired[str]

class ConnectorOperatorTypeDef(TypedDict):
    Amplitude: NotRequired[Literal["BETWEEN"]]
    Datadog: NotRequired[DatadogConnectorOperatorType]
    Dynatrace: NotRequired[DynatraceConnectorOperatorType]
    GoogleAnalytics: NotRequired[GoogleAnalyticsConnectorOperatorType]
    InforNexus: NotRequired[InforNexusConnectorOperatorType]
    Marketo: NotRequired[MarketoConnectorOperatorType]
    S3: NotRequired[S3ConnectorOperatorType]
    Salesforce: NotRequired[SalesforceConnectorOperatorType]
    ServiceNow: NotRequired[ServiceNowConnectorOperatorType]
    Singular: NotRequired[SingularConnectorOperatorType]
    Slack: NotRequired[SlackConnectorOperatorType]
    Trendmicro: NotRequired[TrendmicroConnectorOperatorType]
    Veeva: NotRequired[VeevaConnectorOperatorType]
    Zendesk: NotRequired[ZendeskConnectorOperatorType]
    SAPOData: NotRequired[SAPODataConnectorOperatorType]
    CustomConnector: NotRequired[OperatorType]
    Pardot: NotRequired[PardotConnectorOperatorType]

class DatadogConnectorProfileCredentialsTypeDef(TypedDict):
    apiKey: str
    applicationKey: str

class DynatraceConnectorProfileCredentialsTypeDef(TypedDict):
    apiToken: str

class InforNexusConnectorProfileCredentialsTypeDef(TypedDict):
    accessKeyId: str
    userId: str
    secretAccessKey: str
    datakey: str

class RedshiftConnectorProfileCredentialsTypeDef(TypedDict):
    username: NotRequired[str]
    password: NotRequired[str]

class SingularConnectorProfileCredentialsTypeDef(TypedDict):
    apiKey: str

class SnowflakeConnectorProfileCredentialsTypeDef(TypedDict):
    username: str
    password: str

class TrendmicroConnectorProfileCredentialsTypeDef(TypedDict):
    apiSecretKey: str

class VeevaConnectorProfileCredentialsTypeDef(TypedDict):
    username: str
    password: str

class DatadogConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class DynatraceConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class InforNexusConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class MarketoConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class PardotConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: NotRequired[str]
    isSandboxEnvironment: NotRequired[bool]
    businessUnitId: NotRequired[str]

class RedshiftConnectorProfilePropertiesTypeDef(TypedDict):
    bucketName: str
    roleArn: str
    databaseUrl: NotRequired[str]
    bucketPrefix: NotRequired[str]
    dataApiRoleArn: NotRequired[str]
    isRedshiftServerless: NotRequired[bool]
    clusterIdentifier: NotRequired[str]
    workgroupName: NotRequired[str]
    databaseName: NotRequired[str]

class SalesforceConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: NotRequired[str]
    isSandboxEnvironment: NotRequired[bool]
    usePrivateLinkForMetadataAndAuthorization: NotRequired[bool]

class ServiceNowConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class SlackConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class SnowflakeConnectorProfilePropertiesTypeDef(TypedDict):
    warehouse: str
    stage: str
    bucketName: str
    bucketPrefix: NotRequired[str]
    privateLinkServiceName: NotRequired[str]
    accountName: NotRequired[str]
    region: NotRequired[str]

class VeevaConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class ZendeskConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str

class PrivateConnectionProvisioningStateTypeDef(TypedDict):
    status: NotRequired[PrivateConnectionProvisioningStatusType]
    failureMessage: NotRequired[str]
    failureCause: NotRequired[PrivateConnectionProvisioningFailureCauseType]

class LambdaConnectorProvisioningConfigTypeDef(TypedDict):
    lambdaArn: str

class CustomAuthCredentialsTypeDef(TypedDict):
    customAuthenticationType: str
    credentialsMap: NotRequired[Mapping[str, str]]

class ErrorHandlingConfigTypeDef(TypedDict):
    failOnFirstDestinationError: NotRequired[bool]
    bucketPrefix: NotRequired[str]
    bucketName: NotRequired[str]

class OAuth2PropertiesOutputTypeDef(TypedDict):
    tokenUrl: str
    oAuth2GrantType: OAuth2GrantTypeType
    tokenUrlCustomProperties: NotRequired[Dict[str, str]]

class CustomerProfilesDestinationPropertiesTypeDef(TypedDict):
    domainName: str
    objectTypeName: NotRequired[str]

DatadogSourcePropertiesTypeDef = TypedDict(
    "DatadogSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class DeleteConnectorProfileRequestTypeDef(TypedDict):
    connectorProfileName: str
    forceDelete: NotRequired[bool]

class DeleteFlowRequestTypeDef(TypedDict):
    flowName: str
    forceDelete: NotRequired[bool]

class DescribeConnectorEntityRequestTypeDef(TypedDict):
    connectorEntityName: str
    connectorType: NotRequired[ConnectorTypeType]
    connectorProfileName: NotRequired[str]
    apiVersion: NotRequired[str]

class DescribeConnectorProfilesRequestTypeDef(TypedDict):
    connectorProfileNames: NotRequired[Sequence[str]]
    connectorType: NotRequired[ConnectorTypeType]
    connectorLabel: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeConnectorRequestTypeDef(TypedDict):
    connectorType: ConnectorTypeType
    connectorLabel: NotRequired[str]

class DescribeConnectorsRequestTypeDef(TypedDict):
    connectorTypes: NotRequired[Sequence[ConnectorTypeType]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeFlowExecutionRecordsRequestTypeDef(TypedDict):
    flowName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeFlowRequestTypeDef(TypedDict):
    flowName: str

class ExecutionDetailsTypeDef(TypedDict):
    mostRecentExecutionMessage: NotRequired[str]
    mostRecentExecutionTime: NotRequired[datetime]
    mostRecentExecutionStatus: NotRequired[ExecutionStatusType]

DynatraceSourcePropertiesTypeDef = TypedDict(
    "DynatraceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class ErrorInfoTypeDef(TypedDict):
    putFailuresCount: NotRequired[int]
    executionMessage: NotRequired[str]

class RangeTypeDef(TypedDict):
    maximum: NotRequired[float]
    minimum: NotRequired[float]

class GlueDataCatalogConfigTypeDef(TypedDict):
    roleArn: str
    databaseName: str
    tablePrefix: str

GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class IncrementalPullConfigTypeDef(TypedDict):
    datetimeTypeFieldName: NotRequired[str]

InforNexusSourcePropertiesTypeDef = TypedDict(
    "InforNexusSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class ListConnectorEntitiesRequestTypeDef(TypedDict):
    connectorProfileName: NotRequired[str]
    connectorType: NotRequired[ConnectorTypeType]
    entitiesPath: NotRequired[str]
    apiVersion: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListConnectorsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFlowsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class RegistrationOutputTypeDef(TypedDict):
    message: NotRequired[str]
    result: NotRequired[str]
    status: NotRequired[ExecutionStatusType]

OAuth2CustomParameterTypeDef = TypedDict(
    "OAuth2CustomParameterTypeDef",
    {
        "key": NotRequired[str],
        "isRequired": NotRequired[bool],
        "label": NotRequired[str],
        "description": NotRequired[str],
        "isSensitiveField": NotRequired[bool],
        "connectorSuppliedValues": NotRequired[List[str]],
        "type": NotRequired[OAuth2CustomPropTypeType],
    },
)

class OAuth2PropertiesTypeDef(TypedDict):
    tokenUrl: str
    oAuth2GrantType: OAuth2GrantTypeType
    tokenUrlCustomProperties: NotRequired[Mapping[str, str]]

class OAuthPropertiesOutputTypeDef(TypedDict):
    tokenUrl: str
    authCodeUrl: str
    oAuthScopes: List[str]

class OAuthPropertiesTypeDef(TypedDict):
    tokenUrl: str
    authCodeUrl: str
    oAuthScopes: Sequence[str]

PardotSourcePropertiesTypeDef = TypedDict(
    "PardotSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class PrefixConfigOutputTypeDef(TypedDict):
    prefixType: NotRequired[PrefixTypeType]
    prefixFormat: NotRequired[PrefixFormatType]
    pathPrefixHierarchy: NotRequired[List[PathPrefixType]]

class PrefixConfigTypeDef(TypedDict):
    prefixType: NotRequired[PrefixTypeType]
    prefixFormat: NotRequired[PrefixFormatType]
    pathPrefixHierarchy: NotRequired[Sequence[PathPrefixType]]

class ResetConnectorMetadataCacheRequestTypeDef(TypedDict):
    connectorProfileName: NotRequired[str]
    connectorType: NotRequired[ConnectorTypeType]
    connectorEntityName: NotRequired[str]
    entitiesPath: NotRequired[str]
    apiVersion: NotRequired[str]

class S3InputFormatConfigTypeDef(TypedDict):
    s3InputFileType: NotRequired[S3InputFileTypeType]

class SuccessResponseHandlingConfigTypeDef(TypedDict):
    bucketPrefix: NotRequired[str]
    bucketName: NotRequired[str]

class SAPODataPaginationConfigTypeDef(TypedDict):
    maxPageSize: int

class SAPODataParallelismConfigTypeDef(TypedDict):
    maxParallelism: int

SalesforceSourcePropertiesTypeDef = TypedDict(
    "SalesforceSourcePropertiesTypeDef",
    {
        "object": str,
        "enableDynamicFieldUpdate": NotRequired[bool],
        "includeDeletedRecords": NotRequired[bool],
        "dataTransferApi": NotRequired[SalesforceDataTransferApiType],
    },
)

class ScheduledTriggerPropertiesOutputTypeDef(TypedDict):
    scheduleExpression: str
    dataPullMode: NotRequired[DataPullModeType]
    scheduleStartTime: NotRequired[datetime]
    scheduleEndTime: NotRequired[datetime]
    timezone: NotRequired[str]
    scheduleOffset: NotRequired[int]
    firstExecutionFrom: NotRequired[datetime]
    flowErrorDeactivationThreshold: NotRequired[int]

TimestampTypeDef = Union[datetime, str]
ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
SingularSourcePropertiesTypeDef = TypedDict(
    "SingularSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
SlackSourcePropertiesTypeDef = TypedDict(
    "SlackSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
TrendmicroSourcePropertiesTypeDef = TypedDict(
    "TrendmicroSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
VeevaSourcePropertiesTypeDef = TypedDict(
    "VeevaSourcePropertiesTypeDef",
    {
        "object": str,
        "documentType": NotRequired[str],
        "includeSourceFiles": NotRequired[bool],
        "includeRenditions": NotRequired[bool],
        "includeAllVersions": NotRequired[bool],
    },
)
ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

class StartFlowRequestTypeDef(TypedDict):
    flowName: str
    clientToken: NotRequired[str]

class StopFlowRequestTypeDef(TypedDict):
    flowName: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UnregisterConnectorRequestTypeDef(TypedDict):
    connectorLabel: str
    forceDelete: NotRequired[bool]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CustomAuthConfigTypeDef(TypedDict):
    customAuthenticationType: NotRequired[str]
    authParameters: NotRequired[List[AuthParameterTypeDef]]

class CancelFlowExecutionsResponseTypeDef(TypedDict):
    invalidExecutions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorProfileResponseTypeDef(TypedDict):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowResponseTypeDef(TypedDict):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterConnectorResponseTypeDef(TypedDict):
    connectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlowResponseTypeDef(TypedDict):
    flowArn: str
    flowStatus: FlowStatusType
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopFlowResponseTypeDef(TypedDict):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorProfileResponseTypeDef(TypedDict):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorRegistrationResponseTypeDef(TypedDict):
    connectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(TypedDict):
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CustomConnectorSourcePropertiesOutputTypeDef(TypedDict):
    entityName: str
    customProperties: NotRequired[Dict[str, str]]
    dataTransferApi: NotRequired[DataTransferApiTypeDef]

class CustomConnectorSourcePropertiesTypeDef(TypedDict):
    entityName: str
    customProperties: NotRequired[Mapping[str, str]]
    dataTransferApi: NotRequired[DataTransferApiTypeDef]

class ListConnectorsResponseTypeDef(TypedDict):
    connectors: List[ConnectorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListConnectorEntitiesResponseTypeDef(TypedDict):
    connectorEntityMap: Dict[str, List[ConnectorEntityTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConnectorMetadataTypeDef(TypedDict):
    Amplitude: NotRequired[Dict[str, Any]]
    Datadog: NotRequired[Dict[str, Any]]
    Dynatrace: NotRequired[Dict[str, Any]]
    GoogleAnalytics: NotRequired[GoogleAnalyticsMetadataTypeDef]
    InforNexus: NotRequired[Dict[str, Any]]
    Marketo: NotRequired[Dict[str, Any]]
    Redshift: NotRequired[Dict[str, Any]]
    S3: NotRequired[Dict[str, Any]]
    Salesforce: NotRequired[SalesforceMetadataTypeDef]
    ServiceNow: NotRequired[Dict[str, Any]]
    Singular: NotRequired[Dict[str, Any]]
    Slack: NotRequired[SlackMetadataTypeDef]
    Snowflake: NotRequired[SnowflakeMetadataTypeDef]
    Trendmicro: NotRequired[Dict[str, Any]]
    Veeva: NotRequired[Dict[str, Any]]
    Zendesk: NotRequired[ZendeskMetadataTypeDef]
    EventBridge: NotRequired[Dict[str, Any]]
    Upsolver: NotRequired[Dict[str, Any]]
    CustomerProfiles: NotRequired[Dict[str, Any]]
    Honeycode: NotRequired[HoneycodeMetadataTypeDef]
    SAPOData: NotRequired[Dict[str, Any]]
    Pardot: NotRequired[Dict[str, Any]]

class GoogleAnalyticsConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    accessToken: NotRequired[str]
    refreshToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class HoneycodeConnectorProfileCredentialsTypeDef(TypedDict):
    accessToken: NotRequired[str]
    refreshToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class MarketoConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    accessToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class OAuth2CredentialsTypeDef(TypedDict):
    clientId: NotRequired[str]
    clientSecret: NotRequired[str]
    accessToken: NotRequired[str]
    refreshToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class OAuthCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    accessToken: NotRequired[str]
    refreshToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class PardotConnectorProfileCredentialsTypeDef(TypedDict):
    accessToken: NotRequired[str]
    refreshToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]
    clientCredentialsArn: NotRequired[str]

class SalesforceConnectorProfileCredentialsTypeDef(TypedDict):
    accessToken: NotRequired[str]
    refreshToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]
    clientCredentialsArn: NotRequired[str]
    oAuth2GrantType: NotRequired[OAuth2GrantTypeType]
    jwtToken: NotRequired[str]

class SlackConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    accessToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class ZendeskConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    accessToken: NotRequired[str]
    oAuthRequest: NotRequired[ConnectorOAuthRequestTypeDef]

class TaskOutputTypeDef(TypedDict):
    sourceFields: List[str]
    taskType: TaskTypeType
    connectorOperator: NotRequired[ConnectorOperatorTypeDef]
    destinationField: NotRequired[str]
    taskProperties: NotRequired[Dict[OperatorPropertiesKeysType, str]]

class TaskTypeDef(TypedDict):
    sourceFields: Sequence[str]
    taskType: TaskTypeType
    connectorOperator: NotRequired[ConnectorOperatorTypeDef]
    destinationField: NotRequired[str]
    taskProperties: NotRequired[Mapping[OperatorPropertiesKeysType, str]]

ConnectorProvisioningConfigTypeDef = TypedDict(
    "ConnectorProvisioningConfigTypeDef",
    {
        "lambda": NotRequired[LambdaConnectorProvisioningConfigTypeDef],
    },
)

class CustomConnectorDestinationPropertiesOutputTypeDef(TypedDict):
    entityName: str
    errorHandlingConfig: NotRequired[ErrorHandlingConfigTypeDef]
    writeOperationType: NotRequired[WriteOperationTypeType]
    idFieldNames: NotRequired[List[str]]
    customProperties: NotRequired[Dict[str, str]]

class CustomConnectorDestinationPropertiesTypeDef(TypedDict):
    entityName: str
    errorHandlingConfig: NotRequired[ErrorHandlingConfigTypeDef]
    writeOperationType: NotRequired[WriteOperationTypeType]
    idFieldNames: NotRequired[Sequence[str]]
    customProperties: NotRequired[Mapping[str, str]]

EventBridgeDestinationPropertiesTypeDef = TypedDict(
    "EventBridgeDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)
HoneycodeDestinationPropertiesTypeDef = TypedDict(
    "HoneycodeDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)
MarketoDestinationPropertiesTypeDef = TypedDict(
    "MarketoDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)
RedshiftDestinationPropertiesTypeDef = TypedDict(
    "RedshiftDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
        "bucketPrefix": NotRequired[str],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)
SalesforceDestinationPropertiesOutputTypeDef = TypedDict(
    "SalesforceDestinationPropertiesOutputTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[List[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
        "dataTransferApi": NotRequired[SalesforceDataTransferApiType],
    },
)
SalesforceDestinationPropertiesTypeDef = TypedDict(
    "SalesforceDestinationPropertiesTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
        "dataTransferApi": NotRequired[SalesforceDataTransferApiType],
    },
)
SnowflakeDestinationPropertiesTypeDef = TypedDict(
    "SnowflakeDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
        "bucketPrefix": NotRequired[str],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)
ZendeskDestinationPropertiesOutputTypeDef = TypedDict(
    "ZendeskDestinationPropertiesOutputTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[List[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)
ZendeskDestinationPropertiesTypeDef = TypedDict(
    "ZendeskDestinationPropertiesTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)

class CustomConnectorProfilePropertiesOutputTypeDef(TypedDict):
    profileProperties: NotRequired[Dict[str, str]]
    oAuth2Properties: NotRequired[OAuth2PropertiesOutputTypeDef]

class FlowDefinitionTypeDef(TypedDict):
    flowArn: NotRequired[str]
    description: NotRequired[str]
    flowName: NotRequired[str]
    flowStatus: NotRequired[FlowStatusType]
    sourceConnectorType: NotRequired[ConnectorTypeType]
    sourceConnectorLabel: NotRequired[str]
    destinationConnectorType: NotRequired[ConnectorTypeType]
    destinationConnectorLabel: NotRequired[str]
    triggerType: NotRequired[TriggerTypeType]
    createdAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    lastUpdatedBy: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    lastRunExecutionDetails: NotRequired[ExecutionDetailsTypeDef]

class ExecutionResultTypeDef(TypedDict):
    errorInfo: NotRequired[ErrorInfoTypeDef]
    bytesProcessed: NotRequired[int]
    bytesWritten: NotRequired[int]
    recordsProcessed: NotRequired[int]
    numParallelProcesses: NotRequired[int]
    maxPageSize: NotRequired[int]

class FieldTypeDetailsTypeDef(TypedDict):
    fieldType: str
    filterOperators: List[OperatorType]
    supportedValues: NotRequired[List[str]]
    valueRegexPattern: NotRequired[str]
    supportedDateFormat: NotRequired[str]
    fieldValueRange: NotRequired[RangeTypeDef]
    fieldLengthRange: NotRequired[RangeTypeDef]

class MetadataCatalogConfigTypeDef(TypedDict):
    glueDataCatalog: NotRequired[GlueDataCatalogConfigTypeDef]

class MetadataCatalogDetailTypeDef(TypedDict):
    catalogType: NotRequired[Literal["GLUE"]]
    tableName: NotRequired[str]
    tableRegistrationOutput: NotRequired[RegistrationOutputTypeDef]
    partitionRegistrationOutput: NotRequired[RegistrationOutputTypeDef]

class OAuth2DefaultsTypeDef(TypedDict):
    oauthScopes: NotRequired[List[str]]
    tokenUrls: NotRequired[List[str]]
    authCodeUrls: NotRequired[List[str]]
    oauth2GrantTypesSupported: NotRequired[List[OAuth2GrantTypeType]]
    oauth2CustomProperties: NotRequired[List[OAuth2CustomParameterTypeDef]]

OAuth2PropertiesUnionTypeDef = Union[OAuth2PropertiesTypeDef, OAuth2PropertiesOutputTypeDef]

class SAPODataConnectorProfilePropertiesOutputTypeDef(TypedDict):
    applicationHostUrl: str
    applicationServicePath: str
    portNumber: int
    clientNumber: str
    logonLanguage: NotRequired[str]
    privateLinkServiceName: NotRequired[str]
    oAuthProperties: NotRequired[OAuthPropertiesOutputTypeDef]
    disableSSO: NotRequired[bool]

OAuthPropertiesUnionTypeDef = Union[OAuthPropertiesTypeDef, OAuthPropertiesOutputTypeDef]

class S3OutputFormatConfigOutputTypeDef(TypedDict):
    fileType: NotRequired[FileTypeType]
    prefixConfig: NotRequired[PrefixConfigOutputTypeDef]
    aggregationConfig: NotRequired[AggregationConfigTypeDef]
    preserveSourceDataTyping: NotRequired[bool]

class UpsolverS3OutputFormatConfigOutputTypeDef(TypedDict):
    prefixConfig: PrefixConfigOutputTypeDef
    fileType: NotRequired[FileTypeType]
    aggregationConfig: NotRequired[AggregationConfigTypeDef]

PrefixConfigUnionTypeDef = Union[PrefixConfigTypeDef, PrefixConfigOutputTypeDef]

class S3SourcePropertiesTypeDef(TypedDict):
    bucketName: str
    bucketPrefix: NotRequired[str]
    s3InputFormatConfig: NotRequired[S3InputFormatConfigTypeDef]

class SAPODataDestinationPropertiesOutputTypeDef(TypedDict):
    objectPath: str
    successResponseHandlingConfig: NotRequired[SuccessResponseHandlingConfigTypeDef]
    idFieldNames: NotRequired[List[str]]
    errorHandlingConfig: NotRequired[ErrorHandlingConfigTypeDef]
    writeOperationType: NotRequired[WriteOperationTypeType]

class SAPODataDestinationPropertiesTypeDef(TypedDict):
    objectPath: str
    successResponseHandlingConfig: NotRequired[SuccessResponseHandlingConfigTypeDef]
    idFieldNames: NotRequired[Sequence[str]]
    errorHandlingConfig: NotRequired[ErrorHandlingConfigTypeDef]
    writeOperationType: NotRequired[WriteOperationTypeType]

class SAPODataSourcePropertiesTypeDef(TypedDict):
    objectPath: NotRequired[str]
    parallelismConfig: NotRequired[SAPODataParallelismConfigTypeDef]
    paginationConfig: NotRequired[SAPODataPaginationConfigTypeDef]

class TriggerPropertiesOutputTypeDef(TypedDict):
    Scheduled: NotRequired[ScheduledTriggerPropertiesOutputTypeDef]

class ScheduledTriggerPropertiesTypeDef(TypedDict):
    scheduleExpression: str
    dataPullMode: NotRequired[DataPullModeType]
    scheduleStartTime: NotRequired[TimestampTypeDef]
    scheduleEndTime: NotRequired[TimestampTypeDef]
    timezone: NotRequired[str]
    scheduleOffset: NotRequired[int]
    firstExecutionFrom: NotRequired[TimestampTypeDef]
    flowErrorDeactivationThreshold: NotRequired[int]

class CustomConnectorProfileCredentialsTypeDef(TypedDict):
    authenticationType: AuthenticationTypeType
    basic: NotRequired[BasicAuthCredentialsTypeDef]
    oauth2: NotRequired[OAuth2CredentialsTypeDef]
    apiKey: NotRequired[ApiKeyCredentialsTypeDef]
    custom: NotRequired[CustomAuthCredentialsTypeDef]

class ServiceNowConnectorProfileCredentialsTypeDef(TypedDict):
    username: NotRequired[str]
    password: NotRequired[str]
    oAuth2Credentials: NotRequired[OAuth2CredentialsTypeDef]

class SAPODataConnectorProfileCredentialsTypeDef(TypedDict):
    basicAuthCredentials: NotRequired[BasicAuthCredentialsTypeDef]
    oAuthCredentials: NotRequired[OAuthCredentialsTypeDef]

TaskUnionTypeDef = Union[TaskTypeDef, TaskOutputTypeDef]

class RegisterConnectorRequestTypeDef(TypedDict):
    connectorLabel: NotRequired[str]
    description: NotRequired[str]
    connectorProvisioningType: NotRequired[Literal["LAMBDA"]]
    connectorProvisioningConfig: NotRequired[ConnectorProvisioningConfigTypeDef]
    clientToken: NotRequired[str]

class UpdateConnectorRegistrationRequestTypeDef(TypedDict):
    connectorLabel: str
    description: NotRequired[str]
    connectorProvisioningConfig: NotRequired[ConnectorProvisioningConfigTypeDef]
    clientToken: NotRequired[str]

CustomConnectorDestinationPropertiesUnionTypeDef = Union[
    CustomConnectorDestinationPropertiesTypeDef, CustomConnectorDestinationPropertiesOutputTypeDef
]
SalesforceDestinationPropertiesUnionTypeDef = Union[
    SalesforceDestinationPropertiesTypeDef, SalesforceDestinationPropertiesOutputTypeDef
]
ZendeskDestinationPropertiesUnionTypeDef = Union[
    ZendeskDestinationPropertiesTypeDef, ZendeskDestinationPropertiesOutputTypeDef
]

class ListFlowsResponseTypeDef(TypedDict):
    flows: List[FlowDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SupportedFieldTypeDetailsTypeDef(TypedDict):
    v1: FieldTypeDetailsTypeDef

class ExecutionRecordTypeDef(TypedDict):
    executionId: NotRequired[str]
    executionStatus: NotRequired[ExecutionStatusType]
    executionResult: NotRequired[ExecutionResultTypeDef]
    startedAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]
    dataPullStartTime: NotRequired[datetime]
    dataPullEndTime: NotRequired[datetime]
    metadataCatalogDetails: NotRequired[List[MetadataCatalogDetailTypeDef]]

class AuthenticationConfigTypeDef(TypedDict):
    isBasicAuthSupported: NotRequired[bool]
    isApiKeyAuthSupported: NotRequired[bool]
    isOAuth2Supported: NotRequired[bool]
    isCustomAuthSupported: NotRequired[bool]
    oAuth2Defaults: NotRequired[OAuth2DefaultsTypeDef]
    customAuthConfigs: NotRequired[List[CustomAuthConfigTypeDef]]

class CustomConnectorProfilePropertiesTypeDef(TypedDict):
    profileProperties: NotRequired[Mapping[str, str]]
    oAuth2Properties: NotRequired[OAuth2PropertiesUnionTypeDef]

class ConnectorProfilePropertiesOutputTypeDef(TypedDict):
    Amplitude: NotRequired[Dict[str, Any]]
    Datadog: NotRequired[DatadogConnectorProfilePropertiesTypeDef]
    Dynatrace: NotRequired[DynatraceConnectorProfilePropertiesTypeDef]
    GoogleAnalytics: NotRequired[Dict[str, Any]]
    Honeycode: NotRequired[Dict[str, Any]]
    InforNexus: NotRequired[InforNexusConnectorProfilePropertiesTypeDef]
    Marketo: NotRequired[MarketoConnectorProfilePropertiesTypeDef]
    Redshift: NotRequired[RedshiftConnectorProfilePropertiesTypeDef]
    Salesforce: NotRequired[SalesforceConnectorProfilePropertiesTypeDef]
    ServiceNow: NotRequired[ServiceNowConnectorProfilePropertiesTypeDef]
    Singular: NotRequired[Dict[str, Any]]
    Slack: NotRequired[SlackConnectorProfilePropertiesTypeDef]
    Snowflake: NotRequired[SnowflakeConnectorProfilePropertiesTypeDef]
    Trendmicro: NotRequired[Dict[str, Any]]
    Veeva: NotRequired[VeevaConnectorProfilePropertiesTypeDef]
    Zendesk: NotRequired[ZendeskConnectorProfilePropertiesTypeDef]
    SAPOData: NotRequired[SAPODataConnectorProfilePropertiesOutputTypeDef]
    CustomConnector: NotRequired[CustomConnectorProfilePropertiesOutputTypeDef]
    Pardot: NotRequired[PardotConnectorProfilePropertiesTypeDef]

class SAPODataConnectorProfilePropertiesTypeDef(TypedDict):
    applicationHostUrl: str
    applicationServicePath: str
    portNumber: int
    clientNumber: str
    logonLanguage: NotRequired[str]
    privateLinkServiceName: NotRequired[str]
    oAuthProperties: NotRequired[OAuthPropertiesUnionTypeDef]
    disableSSO: NotRequired[bool]

class S3DestinationPropertiesOutputTypeDef(TypedDict):
    bucketName: str
    bucketPrefix: NotRequired[str]
    s3OutputFormatConfig: NotRequired[S3OutputFormatConfigOutputTypeDef]

class UpsolverDestinationPropertiesOutputTypeDef(TypedDict):
    bucketName: str
    s3OutputFormatConfig: UpsolverS3OutputFormatConfigOutputTypeDef
    bucketPrefix: NotRequired[str]

class S3OutputFormatConfigTypeDef(TypedDict):
    fileType: NotRequired[FileTypeType]
    prefixConfig: NotRequired[PrefixConfigUnionTypeDef]
    aggregationConfig: NotRequired[AggregationConfigTypeDef]
    preserveSourceDataTyping: NotRequired[bool]

class UpsolverS3OutputFormatConfigTypeDef(TypedDict):
    prefixConfig: PrefixConfigUnionTypeDef
    fileType: NotRequired[FileTypeType]
    aggregationConfig: NotRequired[AggregationConfigTypeDef]

SAPODataDestinationPropertiesUnionTypeDef = Union[
    SAPODataDestinationPropertiesTypeDef, SAPODataDestinationPropertiesOutputTypeDef
]

class SourceConnectorPropertiesOutputTypeDef(TypedDict):
    Amplitude: NotRequired[AmplitudeSourcePropertiesTypeDef]
    Datadog: NotRequired[DatadogSourcePropertiesTypeDef]
    Dynatrace: NotRequired[DynatraceSourcePropertiesTypeDef]
    GoogleAnalytics: NotRequired[GoogleAnalyticsSourcePropertiesTypeDef]
    InforNexus: NotRequired[InforNexusSourcePropertiesTypeDef]
    Marketo: NotRequired[MarketoSourcePropertiesTypeDef]
    S3: NotRequired[S3SourcePropertiesTypeDef]
    Salesforce: NotRequired[SalesforceSourcePropertiesTypeDef]
    ServiceNow: NotRequired[ServiceNowSourcePropertiesTypeDef]
    Singular: NotRequired[SingularSourcePropertiesTypeDef]
    Slack: NotRequired[SlackSourcePropertiesTypeDef]
    Trendmicro: NotRequired[TrendmicroSourcePropertiesTypeDef]
    Veeva: NotRequired[VeevaSourcePropertiesTypeDef]
    Zendesk: NotRequired[ZendeskSourcePropertiesTypeDef]
    SAPOData: NotRequired[SAPODataSourcePropertiesTypeDef]
    CustomConnector: NotRequired[CustomConnectorSourcePropertiesOutputTypeDef]
    Pardot: NotRequired[PardotSourcePropertiesTypeDef]

class SourceConnectorPropertiesTypeDef(TypedDict):
    Amplitude: NotRequired[AmplitudeSourcePropertiesTypeDef]
    Datadog: NotRequired[DatadogSourcePropertiesTypeDef]
    Dynatrace: NotRequired[DynatraceSourcePropertiesTypeDef]
    GoogleAnalytics: NotRequired[GoogleAnalyticsSourcePropertiesTypeDef]
    InforNexus: NotRequired[InforNexusSourcePropertiesTypeDef]
    Marketo: NotRequired[MarketoSourcePropertiesTypeDef]
    S3: NotRequired[S3SourcePropertiesTypeDef]
    Salesforce: NotRequired[SalesforceSourcePropertiesTypeDef]
    ServiceNow: NotRequired[ServiceNowSourcePropertiesTypeDef]
    Singular: NotRequired[SingularSourcePropertiesTypeDef]
    Slack: NotRequired[SlackSourcePropertiesTypeDef]
    Trendmicro: NotRequired[TrendmicroSourcePropertiesTypeDef]
    Veeva: NotRequired[VeevaSourcePropertiesTypeDef]
    Zendesk: NotRequired[ZendeskSourcePropertiesTypeDef]
    SAPOData: NotRequired[SAPODataSourcePropertiesTypeDef]
    CustomConnector: NotRequired[CustomConnectorSourcePropertiesTypeDef]
    Pardot: NotRequired[PardotSourcePropertiesTypeDef]

class TriggerConfigOutputTypeDef(TypedDict):
    triggerType: TriggerTypeType
    triggerProperties: NotRequired[TriggerPropertiesOutputTypeDef]

class TriggerPropertiesTypeDef(TypedDict):
    Scheduled: NotRequired[ScheduledTriggerPropertiesTypeDef]

class ConnectorProfileCredentialsTypeDef(TypedDict):
    Amplitude: NotRequired[AmplitudeConnectorProfileCredentialsTypeDef]
    Datadog: NotRequired[DatadogConnectorProfileCredentialsTypeDef]
    Dynatrace: NotRequired[DynatraceConnectorProfileCredentialsTypeDef]
    GoogleAnalytics: NotRequired[GoogleAnalyticsConnectorProfileCredentialsTypeDef]
    Honeycode: NotRequired[HoneycodeConnectorProfileCredentialsTypeDef]
    InforNexus: NotRequired[InforNexusConnectorProfileCredentialsTypeDef]
    Marketo: NotRequired[MarketoConnectorProfileCredentialsTypeDef]
    Redshift: NotRequired[RedshiftConnectorProfileCredentialsTypeDef]
    Salesforce: NotRequired[SalesforceConnectorProfileCredentialsTypeDef]
    ServiceNow: NotRequired[ServiceNowConnectorProfileCredentialsTypeDef]
    Singular: NotRequired[SingularConnectorProfileCredentialsTypeDef]
    Slack: NotRequired[SlackConnectorProfileCredentialsTypeDef]
    Snowflake: NotRequired[SnowflakeConnectorProfileCredentialsTypeDef]
    Trendmicro: NotRequired[TrendmicroConnectorProfileCredentialsTypeDef]
    Veeva: NotRequired[VeevaConnectorProfileCredentialsTypeDef]
    Zendesk: NotRequired[ZendeskConnectorProfileCredentialsTypeDef]
    SAPOData: NotRequired[SAPODataConnectorProfileCredentialsTypeDef]
    CustomConnector: NotRequired[CustomConnectorProfileCredentialsTypeDef]
    Pardot: NotRequired[PardotConnectorProfileCredentialsTypeDef]

class ConnectorEntityFieldTypeDef(TypedDict):
    identifier: str
    parentIdentifier: NotRequired[str]
    label: NotRequired[str]
    isPrimaryKey: NotRequired[bool]
    defaultValue: NotRequired[str]
    isDeprecated: NotRequired[bool]
    supportedFieldTypeDetails: NotRequired[SupportedFieldTypeDetailsTypeDef]
    description: NotRequired[str]
    sourceProperties: NotRequired[SourceFieldPropertiesTypeDef]
    destinationProperties: NotRequired[DestinationFieldPropertiesTypeDef]
    customProperties: NotRequired[Dict[str, str]]

class DescribeFlowExecutionRecordsResponseTypeDef(TypedDict):
    flowExecutions: List[ExecutionRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConnectorConfigurationTypeDef(TypedDict):
    canUseAsSource: NotRequired[bool]
    canUseAsDestination: NotRequired[bool]
    supportedDestinationConnectors: NotRequired[List[ConnectorTypeType]]
    supportedSchedulingFrequencies: NotRequired[List[ScheduleFrequencyTypeType]]
    isPrivateLinkEnabled: NotRequired[bool]
    isPrivateLinkEndpointUrlRequired: NotRequired[bool]
    supportedTriggerTypes: NotRequired[List[TriggerTypeType]]
    connectorMetadata: NotRequired[ConnectorMetadataTypeDef]
    connectorType: NotRequired[ConnectorTypeType]
    connectorLabel: NotRequired[str]
    connectorDescription: NotRequired[str]
    connectorOwner: NotRequired[str]
    connectorName: NotRequired[str]
    connectorVersion: NotRequired[str]
    connectorArn: NotRequired[str]
    connectorModes: NotRequired[List[str]]
    authenticationConfig: NotRequired[AuthenticationConfigTypeDef]
    connectorRuntimeSettings: NotRequired[List[ConnectorRuntimeSettingTypeDef]]
    supportedApiVersions: NotRequired[List[str]]
    supportedOperators: NotRequired[List[OperatorsType]]
    supportedWriteOperations: NotRequired[List[WriteOperationTypeType]]
    connectorProvisioningType: NotRequired[Literal["LAMBDA"]]
    connectorProvisioningConfig: NotRequired[ConnectorProvisioningConfigTypeDef]
    logoURL: NotRequired[str]
    registeredAt: NotRequired[datetime]
    registeredBy: NotRequired[str]
    supportedDataTransferTypes: NotRequired[List[SupportedDataTransferTypeType]]
    supportedDataTransferApis: NotRequired[List[DataTransferApiTypeDef]]

CustomConnectorProfilePropertiesUnionTypeDef = Union[
    CustomConnectorProfilePropertiesTypeDef, CustomConnectorProfilePropertiesOutputTypeDef
]

class ConnectorProfileTypeDef(TypedDict):
    connectorProfileArn: NotRequired[str]
    connectorProfileName: NotRequired[str]
    connectorType: NotRequired[ConnectorTypeType]
    connectorLabel: NotRequired[str]
    connectionMode: NotRequired[ConnectionModeType]
    credentialsArn: NotRequired[str]
    connectorProfileProperties: NotRequired[ConnectorProfilePropertiesOutputTypeDef]
    createdAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]
    privateConnectionProvisioningState: NotRequired[PrivateConnectionProvisioningStateTypeDef]

SAPODataConnectorProfilePropertiesUnionTypeDef = Union[
    SAPODataConnectorProfilePropertiesTypeDef, SAPODataConnectorProfilePropertiesOutputTypeDef
]

class DestinationConnectorPropertiesOutputTypeDef(TypedDict):
    Redshift: NotRequired[RedshiftDestinationPropertiesTypeDef]
    S3: NotRequired[S3DestinationPropertiesOutputTypeDef]
    Salesforce: NotRequired[SalesforceDestinationPropertiesOutputTypeDef]
    Snowflake: NotRequired[SnowflakeDestinationPropertiesTypeDef]
    EventBridge: NotRequired[EventBridgeDestinationPropertiesTypeDef]
    LookoutMetrics: NotRequired[Dict[str, Any]]
    Upsolver: NotRequired[UpsolverDestinationPropertiesOutputTypeDef]
    Honeycode: NotRequired[HoneycodeDestinationPropertiesTypeDef]
    CustomerProfiles: NotRequired[CustomerProfilesDestinationPropertiesTypeDef]
    Zendesk: NotRequired[ZendeskDestinationPropertiesOutputTypeDef]
    Marketo: NotRequired[MarketoDestinationPropertiesTypeDef]
    CustomConnector: NotRequired[CustomConnectorDestinationPropertiesOutputTypeDef]
    SAPOData: NotRequired[SAPODataDestinationPropertiesOutputTypeDef]

S3OutputFormatConfigUnionTypeDef = Union[
    S3OutputFormatConfigTypeDef, S3OutputFormatConfigOutputTypeDef
]
UpsolverS3OutputFormatConfigUnionTypeDef = Union[
    UpsolverS3OutputFormatConfigTypeDef, UpsolverS3OutputFormatConfigOutputTypeDef
]

class SourceFlowConfigOutputTypeDef(TypedDict):
    connectorType: ConnectorTypeType
    sourceConnectorProperties: SourceConnectorPropertiesOutputTypeDef
    apiVersion: NotRequired[str]
    connectorProfileName: NotRequired[str]
    incrementalPullConfig: NotRequired[IncrementalPullConfigTypeDef]

class SourceFlowConfigTypeDef(TypedDict):
    connectorType: ConnectorTypeType
    sourceConnectorProperties: SourceConnectorPropertiesTypeDef
    apiVersion: NotRequired[str]
    connectorProfileName: NotRequired[str]
    incrementalPullConfig: NotRequired[IncrementalPullConfigTypeDef]

class TriggerConfigTypeDef(TypedDict):
    triggerType: TriggerTypeType
    triggerProperties: NotRequired[TriggerPropertiesTypeDef]

class DescribeConnectorEntityResponseTypeDef(TypedDict):
    connectorEntityFields: List[ConnectorEntityFieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorResponseTypeDef(TypedDict):
    connectorConfiguration: ConnectorConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorsResponseTypeDef(TypedDict):
    connectorConfigurations: Dict[ConnectorTypeType, ConnectorConfigurationTypeDef]
    connectors: List[ConnectorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeConnectorProfilesResponseTypeDef(TypedDict):
    connectorProfileDetails: List[ConnectorProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConnectorProfilePropertiesTypeDef(TypedDict):
    Amplitude: NotRequired[Mapping[str, Any]]
    Datadog: NotRequired[DatadogConnectorProfilePropertiesTypeDef]
    Dynatrace: NotRequired[DynatraceConnectorProfilePropertiesTypeDef]
    GoogleAnalytics: NotRequired[Mapping[str, Any]]
    Honeycode: NotRequired[Mapping[str, Any]]
    InforNexus: NotRequired[InforNexusConnectorProfilePropertiesTypeDef]
    Marketo: NotRequired[MarketoConnectorProfilePropertiesTypeDef]
    Redshift: NotRequired[RedshiftConnectorProfilePropertiesTypeDef]
    Salesforce: NotRequired[SalesforceConnectorProfilePropertiesTypeDef]
    ServiceNow: NotRequired[ServiceNowConnectorProfilePropertiesTypeDef]
    Singular: NotRequired[Mapping[str, Any]]
    Slack: NotRequired[SlackConnectorProfilePropertiesTypeDef]
    Snowflake: NotRequired[SnowflakeConnectorProfilePropertiesTypeDef]
    Trendmicro: NotRequired[Mapping[str, Any]]
    Veeva: NotRequired[VeevaConnectorProfilePropertiesTypeDef]
    Zendesk: NotRequired[ZendeskConnectorProfilePropertiesTypeDef]
    SAPOData: NotRequired[SAPODataConnectorProfilePropertiesUnionTypeDef]
    CustomConnector: NotRequired[CustomConnectorProfilePropertiesUnionTypeDef]
    Pardot: NotRequired[PardotConnectorProfilePropertiesTypeDef]

class DestinationFlowConfigOutputTypeDef(TypedDict):
    connectorType: ConnectorTypeType
    destinationConnectorProperties: DestinationConnectorPropertiesOutputTypeDef
    apiVersion: NotRequired[str]
    connectorProfileName: NotRequired[str]

class S3DestinationPropertiesTypeDef(TypedDict):
    bucketName: str
    bucketPrefix: NotRequired[str]
    s3OutputFormatConfig: NotRequired[S3OutputFormatConfigUnionTypeDef]

class UpsolverDestinationPropertiesTypeDef(TypedDict):
    bucketName: str
    s3OutputFormatConfig: UpsolverS3OutputFormatConfigUnionTypeDef
    bucketPrefix: NotRequired[str]

SourceFlowConfigUnionTypeDef = Union[SourceFlowConfigTypeDef, SourceFlowConfigOutputTypeDef]
TriggerConfigUnionTypeDef = Union[TriggerConfigTypeDef, TriggerConfigOutputTypeDef]
ConnectorProfilePropertiesUnionTypeDef = Union[
    ConnectorProfilePropertiesTypeDef, ConnectorProfilePropertiesOutputTypeDef
]

class DescribeFlowResponseTypeDef(TypedDict):
    flowArn: str
    description: str
    flowName: str
    kmsArn: str
    flowStatus: FlowStatusType
    flowStatusMessage: str
    sourceFlowConfig: SourceFlowConfigOutputTypeDef
    destinationFlowConfigList: List[DestinationFlowConfigOutputTypeDef]
    lastRunExecutionDetails: ExecutionDetailsTypeDef
    triggerConfig: TriggerConfigOutputTypeDef
    tasks: List[TaskOutputTypeDef]
    createdAt: datetime
    lastUpdatedAt: datetime
    createdBy: str
    lastUpdatedBy: str
    tags: Dict[str, str]
    metadataCatalogConfig: MetadataCatalogConfigTypeDef
    lastRunMetadataCatalogDetails: List[MetadataCatalogDetailTypeDef]
    schemaVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

S3DestinationPropertiesUnionTypeDef = Union[
    S3DestinationPropertiesTypeDef, S3DestinationPropertiesOutputTypeDef
]
UpsolverDestinationPropertiesUnionTypeDef = Union[
    UpsolverDestinationPropertiesTypeDef, UpsolverDestinationPropertiesOutputTypeDef
]

class ConnectorProfileConfigTypeDef(TypedDict):
    connectorProfileProperties: ConnectorProfilePropertiesUnionTypeDef
    connectorProfileCredentials: NotRequired[ConnectorProfileCredentialsTypeDef]

class DestinationConnectorPropertiesTypeDef(TypedDict):
    Redshift: NotRequired[RedshiftDestinationPropertiesTypeDef]
    S3: NotRequired[S3DestinationPropertiesUnionTypeDef]
    Salesforce: NotRequired[SalesforceDestinationPropertiesUnionTypeDef]
    Snowflake: NotRequired[SnowflakeDestinationPropertiesTypeDef]
    EventBridge: NotRequired[EventBridgeDestinationPropertiesTypeDef]
    LookoutMetrics: NotRequired[Mapping[str, Any]]
    Upsolver: NotRequired[UpsolverDestinationPropertiesUnionTypeDef]
    Honeycode: NotRequired[HoneycodeDestinationPropertiesTypeDef]
    CustomerProfiles: NotRequired[CustomerProfilesDestinationPropertiesTypeDef]
    Zendesk: NotRequired[ZendeskDestinationPropertiesUnionTypeDef]
    Marketo: NotRequired[MarketoDestinationPropertiesTypeDef]
    CustomConnector: NotRequired[CustomConnectorDestinationPropertiesUnionTypeDef]
    SAPOData: NotRequired[SAPODataDestinationPropertiesUnionTypeDef]

class CreateConnectorProfileRequestTypeDef(TypedDict):
    connectorProfileName: str
    connectorType: ConnectorTypeType
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfigTypeDef
    kmsArn: NotRequired[str]
    connectorLabel: NotRequired[str]
    clientToken: NotRequired[str]

class UpdateConnectorProfileRequestTypeDef(TypedDict):
    connectorProfileName: str
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfigTypeDef
    clientToken: NotRequired[str]

DestinationConnectorPropertiesUnionTypeDef = Union[
    DestinationConnectorPropertiesTypeDef, DestinationConnectorPropertiesOutputTypeDef
]

class DestinationFlowConfigTypeDef(TypedDict):
    connectorType: ConnectorTypeType
    destinationConnectorProperties: DestinationConnectorPropertiesUnionTypeDef
    apiVersion: NotRequired[str]
    connectorProfileName: NotRequired[str]

DestinationFlowConfigUnionTypeDef = Union[
    DestinationFlowConfigTypeDef, DestinationFlowConfigOutputTypeDef
]

class CreateFlowRequestTypeDef(TypedDict):
    flowName: str
    triggerConfig: TriggerConfigUnionTypeDef
    sourceFlowConfig: SourceFlowConfigUnionTypeDef
    destinationFlowConfigList: Sequence[DestinationFlowConfigUnionTypeDef]
    tasks: Sequence[TaskUnionTypeDef]
    description: NotRequired[str]
    kmsArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    metadataCatalogConfig: NotRequired[MetadataCatalogConfigTypeDef]
    clientToken: NotRequired[str]

class UpdateFlowRequestTypeDef(TypedDict):
    flowName: str
    triggerConfig: TriggerConfigUnionTypeDef
    sourceFlowConfig: SourceFlowConfigUnionTypeDef
    destinationFlowConfigList: Sequence[DestinationFlowConfigUnionTypeDef]
    tasks: Sequence[TaskUnionTypeDef]
    description: NotRequired[str]
    metadataCatalogConfig: NotRequired[MetadataCatalogConfigTypeDef]
    clientToken: NotRequired[str]
