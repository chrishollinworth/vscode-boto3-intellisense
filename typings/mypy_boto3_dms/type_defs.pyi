"""
Type annotations for dms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AuthMechanismValueType,
    AuthTypeValueType,
    CharLengthSemanticsType,
    CompressionTypeValueType,
    DataFormatValueType,
    DatePartitionDelimiterValueType,
    DatePartitionSequenceValueType,
    DmsSslModeValueType,
    EncodingTypeValueType,
    EncryptionModeValueType,
    EndpointSettingTypeValueType,
    KafkaSecurityProtocolType,
    MessageFormatValueType,
    MigrationTypeValueType,
    NestingLevelValueType,
    ParquetVersionValueType,
    PluginNameValueType,
    RefreshSchemasStatusTypeValueType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    SafeguardPolicyType,
    StartReplicationTaskTypeValueType,
    TargetDbTypeType,
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
    "AccountQuotaTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "CertificateTypeDef",
    "ConnectionTypeDef",
    "CreateEndpointMessageRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "CreateReplicationInstanceMessageRequestTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "CreateReplicationSubnetGroupMessageRequestTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "CreateReplicationTaskMessageRequestTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DeleteCertificateMessageRequestTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DeleteConnectionMessageRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEndpointMessageRequestTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DeleteReplicationInstanceMessageRequestTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskMessageRequestTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "DescribeConnectionsMessageRequestTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "DescribeEndpointSettingsMessageRequestTypeDef",
    "DescribeEndpointSettingsResponseTypeDef",
    "DescribeEndpointTypesMessageRequestTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEndpointsMessageRequestTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationInstancesMessageRequestTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "DescribeReplicationTasksMessageRequestTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeSchemasMessageRequestTypeDef",
    "DescribeSchemasResponseTypeDef",
    "DescribeTableStatisticsMessageRequestTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EndpointSettingTypeDef",
    "EndpointTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "FilterTypeDef",
    "IBMDb2SettingsTypeDef",
    "ImportCertificateMessageRequestTypeDef",
    "ImportCertificateResponseTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "ModifyEndpointMessageRequestTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "ModifyReplicationInstanceMessageRequestTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "ModifyReplicationSubnetGroupMessageRequestTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ModifyReplicationTaskMessageRequestTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MongoDbSettingsTypeDef",
    "MoveReplicationTaskMessageRequestTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "MySQLSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleSettingsTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "RebootReplicationInstanceMessageRequestTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasMessageRequestTypeDef",
    "RefreshSchemasResponseTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReloadTablesMessageRequestTypeDef",
    "ReloadTablesResponseTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3SettingsTypeDef",
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskAssessmentRunMessageRequestTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "StartReplicationTaskMessageRequestTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopReplicationTaskMessageRequestTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TableToReloadTypeDef",
    "TagTypeDef",
    "TestConnectionMessageRequestTypeDef",
    "TestConnectionResponseTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": str,
        "Used": int,
        "Max": int,
    },
    total=False,
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

CancelReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

CancelReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

_RequiredCreateEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointMessageRequestTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
    },
)
_OptionalCreateEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointMessageRequestTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "ResourceIdentifier": str,
        "DocDbSettings": "DocDbSettingsTypeDef",
    },
    total=False,
)

class CreateEndpointMessageRequestTypeDef(
    _RequiredCreateEndpointMessageRequestTypeDef, _OptionalCreateEndpointMessageRequestTypeDef
):
    pass

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
    },
)
_OptionalCreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEventSubscriptionMessageRequestTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
        "SourceIds": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEventSubscriptionMessageRequestTypeDef(
    _RequiredCreateEventSubscriptionMessageRequestTypeDef,
    _OptionalCreateEventSubscriptionMessageRequestTypeDef,
):
    pass

CreateEventSubscriptionResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
    },
)
_OptionalCreateReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationInstanceMessageRequestTypeDef",
    {
        "AllocatedStorage": int,
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "ReplicationSubnetGroupIdentifier": str,
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "DnsNameServers": str,
        "ResourceIdentifier": str,
    },
    total=False,
)

class CreateReplicationInstanceMessageRequestTypeDef(
    _RequiredCreateReplicationInstanceMessageRequestTypeDef,
    _OptionalCreateReplicationInstanceMessageRequestTypeDef,
):
    pass

CreateReplicationInstanceResponseTypeDef = TypedDict(
    "CreateReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationSubnetGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateReplicationSubnetGroupMessageRequestTypeDef(
    _RequiredCreateReplicationSubnetGroupMessageRequestTypeDef,
    _OptionalCreateReplicationSubnetGroupMessageRequestTypeDef,
):
    pass

CreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "CreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationTaskMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
    },
)
_OptionalCreateReplicationTaskMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskSettings": str,
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "Tags": List["TagTypeDef"],
        "TaskData": str,
        "ResourceIdentifier": str,
    },
    total=False,
)

class CreateReplicationTaskMessageRequestTypeDef(
    _RequiredCreateReplicationTaskMessageRequestTypeDef,
    _OptionalCreateReplicationTaskMessageRequestTypeDef,
):
    pass

CreateReplicationTaskResponseTypeDef = TypedDict(
    "CreateReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCertificateMessageRequestTypeDef = TypedDict(
    "DeleteCertificateMessageRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DeleteCertificateResponseTypeDef = TypedDict(
    "DeleteCertificateResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionMessageRequestTypeDef = TypedDict(
    "DeleteConnectionMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointMessageRequestTypeDef = TypedDict(
    "DeleteEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationInstanceMessageRequestTypeDef = TypedDict(
    "DeleteReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)

DeleteReplicationInstanceResponseTypeDef = TypedDict(
    "DeleteReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
    },
)

DeleteReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

DeleteReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationTaskMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

DeleteReplicationTaskResponseTypeDef = TypedDict(
    "DeleteReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "UniqueAccountIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicableIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ReplicationInstanceArn": str,
        "SourceEngineName": str,
        "TargetEngineName": str,
        "MigrationType": MigrationTypeValueType,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeApplicableIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    {
        "IndividualAssessmentNames": List[str],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeCertificatesResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseTypeDef",
    {
        "Marker": str,
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionsMessageRequestTypeDef = TypedDict(
    "DescribeConnectionsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeConnectionsResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseTypeDef",
    {
        "Marker": str,
        "Connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEndpointSettingsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEndpointSettingsMessageRequestTypeDef",
    {
        "EngineName": str,
    },
)
_OptionalDescribeEndpointSettingsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEndpointSettingsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEndpointSettingsMessageRequestTypeDef(
    _RequiredDescribeEndpointSettingsMessageRequestTypeDef,
    _OptionalDescribeEndpointSettingsMessageRequestTypeDef,
):
    pass

DescribeEndpointSettingsResponseTypeDef = TypedDict(
    "DescribeEndpointSettingsResponseTypeDef",
    {
        "Marker": str,
        "EndpointSettings": List["EndpointSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointTypesMessageRequestTypeDef = TypedDict(
    "DescribeEndpointTypesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointTypesResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List["SupportedEndpointTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeEndpointsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Marker": str,
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEventCategoriesResponseTypeDef = TypedDict(
    "DescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List["EventCategoryGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "EventCategories": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrderableReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List["OrderableReplicationInstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRefreshSchemasStatusMessageRequestTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeReplicationInstanceTaskLogsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalDescribeReplicationInstanceTaskLogsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeReplicationInstanceTaskLogsMessageRequestTypeDef(
    _RequiredDescribeReplicationInstanceTaskLogsMessageRequestTypeDef,
    _OptionalDescribeReplicationInstanceTaskLogsMessageRequestTypeDef,
):
    pass

DescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List["ReplicationInstanceTaskLogTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List["ReplicationInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List["ReplicationSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List["ReplicationTaskAssessmentResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskAssessmentRuns": List["ReplicationTaskAssessmentRunTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskIndividualAssessments": List["ReplicationTaskIndividualAssessmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTasksMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTasksMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "WithoutSettings": bool,
    },
    total=False,
)

DescribeReplicationTasksResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List["ReplicationTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSchemasMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalDescribeSchemasMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeSchemasMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeSchemasMessageRequestTypeDef(
    _RequiredDescribeSchemasMessageRequestTypeDef, _OptionalDescribeSchemasMessageRequestTypeDef
):
    pass

DescribeSchemasResponseTypeDef = TypedDict(
    "DescribeSchemasResponseTypeDef",
    {
        "Marker": str,
        "Schemas": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTableStatisticsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeTableStatisticsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
_OptionalDescribeTableStatisticsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeTableStatisticsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class DescribeTableStatisticsMessageRequestTypeDef(
    _RequiredDescribeTableStatisticsMessageRequestTypeDef,
    _OptionalDescribeTableStatisticsMessageRequestTypeDef,
):
    pass

DescribeTableStatisticsResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List["TableStatisticsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "BucketName": str,
    },
    total=False,
)

DocDbSettingsTypeDef = TypedDict(
    "DocDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "NestingLevel": NestingLevelValueType,
        "ExtractDocId": bool,
        "DocsToInvestigate": int,
        "KmsKeyId": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

DynamoDbSettingsTypeDef = TypedDict(
    "DynamoDbSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
    },
)

_RequiredElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
    },
)
_OptionalElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalElasticsearchSettingsTypeDef",
    {
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

class ElasticsearchSettingsTypeDef(
    _RequiredElasticsearchSettingsTypeDef, _OptionalElasticsearchSettingsTypeDef
):
    pass

EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": str,
        "Type": EndpointSettingTypeValueType,
        "EnumValues": List[str],
        "Sensitive": bool,
        "Units": str,
        "Applicability": str,
        "IntValueMin": int,
        "IntValueMax": int,
        "DefaultValue": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "DocDbSettings": "DocDbSettingsTypeDef",
    },
    total=False,
)

EventCategoryGroupTypeDef = TypedDict(
    "EventCategoryGroupTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
    },
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

IBMDb2SettingsTypeDef = TypedDict(
    "IBMDb2SettingsTypeDef",
    {
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "SetDataCaptureChanges": bool,
        "CurrentLsn": str,
        "MaxKBytesPerRead": int,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredImportCertificateMessageRequestTypeDef = TypedDict(
    "_RequiredImportCertificateMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
    },
)
_OptionalImportCertificateMessageRequestTypeDef = TypedDict(
    "_OptionalImportCertificateMessageRequestTypeDef",
    {
        "CertificatePem": str,
        "CertificateWallet": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportCertificateMessageRequestTypeDef(
    _RequiredImportCertificateMessageRequestTypeDef, _OptionalImportCertificateMessageRequestTypeDef
):
    pass

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KafkaSettingsTypeDef = TypedDict(
    "KafkaSettingsTypeDef",
    {
        "Broker": str,
        "Topic": str,
        "MessageFormat": MessageFormatValueType,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
        "MessageMaxBytes": int,
        "IncludeNullAndEmpty": bool,
        "SecurityProtocol": KafkaSecurityProtocolType,
        "SslClientCertificateArn": str,
        "SslClientKeyArn": str,
        "SslClientKeyPassword": str,
        "SslCaCertificateArn": str,
        "SaslUsername": str,
        "SaslPassword": str,
        "NoHexPrefix": bool,
    },
    total=False,
)

KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {
        "StreamArn": str,
        "MessageFormat": MessageFormatValueType,
        "ServiceAccessRoleArn": str,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
        "IncludeNullAndEmpty": bool,
        "NoHexPrefix": bool,
    },
    total=False,
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MicrosoftSQLServerSettingsTypeDef = TypedDict(
    "MicrosoftSQLServerSettingsTypeDef",
    {
        "Port": int,
        "BcpPacketSize": int,
        "DatabaseName": str,
        "ControlTablesFileGroup": str,
        "Password": str,
        "QuerySingleAlwaysOnNode": bool,
        "ReadBackupOnly": bool,
        "SafeguardPolicy": SafeguardPolicyType,
        "ServerName": str,
        "Username": str,
        "UseBcpFullLoad": bool,
        "UseThirdPartyBackupDevice": bool,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredModifyEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredModifyEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalModifyEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalModifyEndpointMessageRequestTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "DocDbSettings": "DocDbSettingsTypeDef",
        "ExactSettings": bool,
    },
    total=False,
)

class ModifyEndpointMessageRequestTypeDef(
    _RequiredModifyEndpointMessageRequestTypeDef, _OptionalModifyEndpointMessageRequestTypeDef
):
    pass

ModifyEndpointResponseTypeDef = TypedDict(
    "ModifyEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_RequiredModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)
_OptionalModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_OptionalModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SourceType": str,
        "EventCategories": List[str],
        "Enabled": bool,
    },
    total=False,
)

class ModifyEventSubscriptionMessageRequestTypeDef(
    _RequiredModifyEventSubscriptionMessageRequestTypeDef,
    _OptionalModifyEventSubscriptionMessageRequestTypeDef,
):
    pass

ModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalModifyReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationInstanceMessageRequestTypeDef",
    {
        "AllocatedStorage": int,
        "ApplyImmediately": bool,
        "ReplicationInstanceClass": str,
        "VpcSecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "AutoMinorVersionUpgrade": bool,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

class ModifyReplicationInstanceMessageRequestTypeDef(
    _RequiredModifyReplicationInstanceMessageRequestTypeDef,
    _OptionalModifyReplicationInstanceMessageRequestTypeDef,
):
    pass

ModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ModifyReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupDescription": str,
    },
    total=False,
)

class ModifyReplicationSubnetGroupMessageRequestTypeDef(
    _RequiredModifyReplicationSubnetGroupMessageRequestTypeDef,
    _OptionalModifyReplicationSubnetGroupMessageRequestTypeDef,
):
    pass

ModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationTaskMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
_OptionalModifyReplicationTaskMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "TaskData": str,
    },
    total=False,
)

class ModifyReplicationTaskMessageRequestTypeDef(
    _RequiredModifyReplicationTaskMessageRequestTypeDef,
    _OptionalModifyReplicationTaskMessageRequestTypeDef,
):
    pass

ModifyReplicationTaskResponseTypeDef = TypedDict(
    "ModifyReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MongoDbSettingsTypeDef = TypedDict(
    "MongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": AuthTypeValueType,
        "AuthMechanism": AuthMechanismValueType,
        "NestingLevel": NestingLevelValueType,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

MoveReplicationTaskMessageRequestTypeDef = TypedDict(
    "MoveReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TargetReplicationInstanceArn": str,
    },
)

MoveReplicationTaskResponseTypeDef = TypedDict(
    "MoveReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MySQLSettingsTypeDef = TypedDict(
    "MySQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CleanSourceMetadataOnMismatch": bool,
        "DatabaseName": str,
        "EventsPollInterval": int,
        "TargetDbType": TargetDbTypeType,
        "MaxFileSize": int,
        "ParallelLoadThreads": int,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "ServerTimezone": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredNeptuneSettingsTypeDef = TypedDict(
    "_RequiredNeptuneSettingsTypeDef",
    {
        "S3BucketName": str,
        "S3BucketFolder": str,
    },
)
_OptionalNeptuneSettingsTypeDef = TypedDict(
    "_OptionalNeptuneSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ErrorRetryDuration": int,
        "MaxFileSize": int,
        "MaxRetryCount": int,
        "IamAuthEnabled": bool,
    },
    total=False,
)

class NeptuneSettingsTypeDef(_RequiredNeptuneSettingsTypeDef, _OptionalNeptuneSettingsTypeDef):
    pass

OracleSettingsTypeDef = TypedDict(
    "OracleSettingsTypeDef",
    {
        "AddSupplementalLogging": bool,
        "ArchivedLogDestId": int,
        "AdditionalArchivedLogDestId": int,
        "AllowSelectNestedTables": bool,
        "ParallelAsmReadThreads": int,
        "ReadAheadBlocks": int,
        "AccessAlternateDirectly": bool,
        "UseAlternateFolderForOnline": bool,
        "OraclePathPrefix": str,
        "UsePathPrefix": str,
        "ReplacePathPrefix": bool,
        "EnableHomogenousTablespace": bool,
        "DirectPathNoLog": bool,
        "ArchivedLogsOnly": bool,
        "AsmPassword": str,
        "AsmServer": str,
        "AsmUser": str,
        "CharLengthSemantics": CharLengthSemanticsType,
        "DatabaseName": str,
        "DirectPathParallelLoad": bool,
        "FailTasksOnLobTruncation": bool,
        "NumberDatatypeScale": int,
        "Password": str,
        "Port": int,
        "ReadTableSpaceName": bool,
        "RetryInterval": int,
        "SecurityDbEncryption": str,
        "SecurityDbEncryptionName": str,
        "ServerName": str,
        "SpatialDataOptionToGeoJsonFunctionName": str,
        "StandbyDelayTime": int,
        "Username": str,
        "UseBFile": bool,
        "UseDirectPathFullLoad": bool,
        "UseLogminerReader": bool,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "SecretsManagerOracleAsmAccessRoleArn": str,
        "SecretsManagerOracleAsmSecretId": str,
    },
    total=False,
)

OrderableReplicationInstanceTypeDef = TypedDict(
    "OrderableReplicationInstanceTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": Literal["beta"],
    },
    total=False,
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

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

PostgreSQLSettingsTypeDef = TypedDict(
    "PostgreSQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CaptureDdls": bool,
        "MaxFileSize": int,
        "DatabaseName": str,
        "DdlArtifactsSchema": str,
        "ExecuteTimeout": int,
        "FailTasksOnLobTruncation": bool,
        "HeartbeatEnable": bool,
        "HeartbeatSchema": str,
        "HeartbeatFrequency": int,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "Username": str,
        "SlotName": str,
        "PluginName": PluginNameValueType,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredRebootReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredRebootReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalRebootReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalRebootReplicationInstanceMessageRequestTypeDef",
    {
        "ForceFailover": bool,
    },
    total=False,
)

class RebootReplicationInstanceMessageRequestTypeDef(
    _RequiredRebootReplicationInstanceMessageRequestTypeDef,
    _OptionalRebootReplicationInstanceMessageRequestTypeDef,
):
    pass

RebootReplicationInstanceResponseTypeDef = TypedDict(
    "RebootReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "CaseSensitiveNames": bool,
        "CompUpdate": bool,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": EncryptionModeValueType,
        "ExplicitIds": bool,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

RefreshSchemasMessageRequestTypeDef = TypedDict(
    "RefreshSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

RefreshSchemasResponseTypeDef = TypedDict(
    "RefreshSchemasResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RefreshSchemasStatusTypeDef = TypedDict(
    "RefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": RefreshSchemasStatusTypeValueType,
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

_RequiredReloadTablesMessageRequestTypeDef = TypedDict(
    "_RequiredReloadTablesMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TablesToReload": List["TableToReloadTypeDef"],
    },
)
_OptionalReloadTablesMessageRequestTypeDef = TypedDict(
    "_OptionalReloadTablesMessageRequestTypeDef",
    {
        "ReloadOption": ReloadOptionValueType,
    },
    total=False,
)

class ReloadTablesMessageRequestTypeDef(
    _RequiredReloadTablesMessageRequestTypeDef, _OptionalReloadTablesMessageRequestTypeDef
):
    pass

ReloadTablesResponseTypeDef = TypedDict(
    "ReloadTablesResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

ReplicationInstanceTaskLogTypeDef = TypedDict(
    "ReplicationInstanceTaskLogTypeDef",
    {
        "ReplicationTaskName": str,
        "ReplicationTaskArn": str,
        "ReplicationInstanceTaskLogSize": int,
    },
    total=False,
)

ReplicationInstanceTypeDef = TypedDict(
    "ReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "ReplicationPendingModifiedValuesTypeDef",
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ReplicationPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ReplicationSubnetGroupTypeDef = TypedDict(
    "ReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
    },
    total=False,
)

ReplicationTaskAssessmentResultTypeDef = TypedDict(
    "ReplicationTaskAssessmentResultTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

ReplicationTaskAssessmentRunProgressTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunProgressTypeDef",
    {
        "IndividualAssessmentCount": int,
        "IndividualAssessmentCompletedCount": int,
    },
    total=False,
)

ReplicationTaskAssessmentRunTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
        "ReplicationTaskArn": str,
        "Status": str,
        "ReplicationTaskAssessmentRunCreationDate": datetime,
        "AssessmentProgress": "ReplicationTaskAssessmentRunProgressTypeDef",
        "LastFailureMessage": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "ResultLocationFolder": str,
        "ResultEncryptionMode": str,
        "ResultKmsKeyArn": str,
        "AssessmentRunName": str,
    },
    total=False,
)

ReplicationTaskIndividualAssessmentTypeDef = TypedDict(
    "ReplicationTaskIndividualAssessmentTypeDef",
    {
        "ReplicationTaskIndividualAssessmentArn": str,
        "ReplicationTaskAssessmentRunArn": str,
        "IndividualAssessmentName": str,
        "Status": str,
        "ReplicationTaskIndividualAssessmentStartDate": datetime,
    },
    total=False,
)

ReplicationTaskStatsTypeDef = TypedDict(
    "ReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ReplicationTaskTypeDef = TypedDict(
    "ReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": "ReplicationTaskStatsTypeDef",
        "TaskData": str,
        "TargetReplicationInstanceArn": str,
    },
    total=False,
)

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
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

S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": CompressionTypeValueType,
        "EncryptionMode": EncryptionModeValueType,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": DataFormatValueType,
        "EncodingType": EncodingTypeValueType,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": ParquetVersionValueType,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
        "CdcInsertsAndUpdates": bool,
        "DatePartitionEnabled": bool,
        "DatePartitionSequence": DatePartitionSequenceValueType,
        "DatePartitionDelimiter": DatePartitionDelimiterValueType,
        "UseCsvNoSupValue": bool,
        "CsvNoSupValue": str,
        "PreserveTransactions": bool,
        "CdcPath": str,
    },
    total=False,
)

StartReplicationTaskAssessmentMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "_RequiredStartReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "AssessmentRunName": str,
    },
)
_OptionalStartReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "_OptionalStartReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ResultLocationFolder": str,
        "ResultEncryptionMode": str,
        "ResultKmsKeyArn": str,
        "IncludeOnly": List[str],
        "Exclude": List[str],
    },
    total=False,
)

class StartReplicationTaskAssessmentRunMessageRequestTypeDef(
    _RequiredStartReplicationTaskAssessmentRunMessageRequestTypeDef,
    _OptionalStartReplicationTaskAssessmentRunMessageRequestTypeDef,
):
    pass

StartReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplicationTaskMessageRequestTypeDef = TypedDict(
    "_RequiredStartReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "StartReplicationTaskType": StartReplicationTaskTypeValueType,
    },
)
_OptionalStartReplicationTaskMessageRequestTypeDef = TypedDict(
    "_OptionalStartReplicationTaskMessageRequestTypeDef",
    {
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
    },
    total=False,
)

class StartReplicationTaskMessageRequestTypeDef(
    _RequiredStartReplicationTaskMessageRequestTypeDef,
    _OptionalStartReplicationTaskMessageRequestTypeDef,
):
    pass

StartReplicationTaskResponseTypeDef = TypedDict(
    "StartReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopReplicationTaskMessageRequestTypeDef = TypedDict(
    "StopReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StopReplicationTaskResponseTypeDef = TypedDict(
    "StopReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

SupportedEndpointTypeTypeDef = TypedDict(
    "SupportedEndpointTypeTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": ReplicationEndpointTypeValueType,
        "ReplicationInstanceEngineMinimumVersion": str,
        "EngineDisplayName": str,
    },
    total=False,
)

SybaseSettingsTypeDef = TypedDict(
    "SybaseSettingsTypeDef",
    {
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

TableStatisticsTypeDef = TypedDict(
    "TableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "FullLoadStartTime": datetime,
        "FullLoadEndTime": datetime,
        "FullLoadReloaded": bool,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

TableToReloadTypeDef = TypedDict(
    "TableToReloadTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TestConnectionMessageRequestTypeDef = TypedDict(
    "TestConnectionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
    },
)

TestConnectionResponseTypeDef = TypedDict(
    "TestConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
