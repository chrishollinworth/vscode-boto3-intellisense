"""
Type annotations for rds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds.type_defs import AccountAttributesMessageTypeDef

    data: AccountAttributesMessageTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActivityStreamModeType,
    ActivityStreamPolicyStatusType,
    ActivityStreamStatusType,
    ApplyMethodType,
    AuditPolicyStateType,
    AutomationModeType,
    ClientPasswordAuthTypeType,
    CustomEngineVersionStatusType,
    DBProxyEndpointStatusType,
    DBProxyEndpointTargetRoleType,
    DBProxyStatusType,
    EngineFamilyType,
    ExportSourceTypeType,
    FailoverStatusType,
    GlobalClusterMemberSynchronizationStatusType,
    IAMAuthModeType,
    IntegrationStatusType,
    LimitlessDatabaseStatusType,
    LocalWriteForwardingStatusType,
    ReplicaModeType,
    SourceTypeType,
    TargetHealthReasonType,
    TargetRoleType,
    TargetStateType,
    TargetTypeType,
    WriteForwardingStatusType,
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
    "AccountAttributesMessageTypeDef",
    "AccountQuotaTypeDef",
    "AddRoleToDBClusterMessageRequestTypeDef",
    "AddRoleToDBInstanceMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "BacktrackDBClusterMessageRequestTypeDef",
    "BlueGreenDeploymentTaskTypeDef",
    "BlueGreenDeploymentTypeDef",
    "CancelExportTaskMessageRequestTypeDef",
    "CertificateDetailsTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CharacterSetTypeDef",
    "ClientGenerateDbAuthTokenRequestTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "ConnectionPoolConfigurationTypeDef",
    "ContextAttributeTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupMessageRequestTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CopyDBSnapshotMessageRequestTypeDef",
    "CopyDBSnapshotResultTypeDef",
    "CopyOptionGroupMessageRequestTypeDef",
    "CopyOptionGroupResultTypeDef",
    "CreateBlueGreenDeploymentRequestRequestTypeDef",
    "CreateBlueGreenDeploymentResponseTypeDef",
    "CreateCustomDBEngineVersionMessageRequestTypeDef",
    "CreateDBClusterEndpointMessageRequestTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceReadReplicaMessageRequestTypeDef",
    "CreateDBInstanceReadReplicaResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupMessageRequestTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBProxyEndpointRequestRequestTypeDef",
    "CreateDBProxyEndpointResponseTypeDef",
    "CreateDBProxyRequestRequestTypeDef",
    "CreateDBProxyResponseTypeDef",
    "CreateDBSecurityGroupMessageRequestTypeDef",
    "CreateDBSecurityGroupResultTypeDef",
    "CreateDBShardGroupMessageRequestTypeDef",
    "CreateDBSnapshotMessageRequestTypeDef",
    "CreateDBSnapshotResultTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterMessageRequestTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "CreateIntegrationMessageRequestTypeDef",
    "CreateOptionGroupMessageRequestTypeDef",
    "CreateOptionGroupResultTypeDef",
    "CreateTenantDatabaseMessageRequestTypeDef",
    "CreateTenantDatabaseResultTypeDef",
    "CustomDBEngineVersionAMITypeDef",
    "DBClusterAutomatedBackupMessageTypeDef",
    "DBClusterAutomatedBackupTypeDef",
    "DBClusterBacktrackMessageTypeDef",
    "DBClusterBacktrackResponseMetadataTypeDef",
    "DBClusterBacktrackTypeDef",
    "DBClusterCapacityInfoTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterEndpointResponseMetadataTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterStatusInfoTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBEngineVersionResponseMetadataTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceAutomatedBackupMessageTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    "DBInstanceMessageTypeDef",
    "DBInstanceRoleTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBProxyEndpointTypeDef",
    "DBProxyTargetGroupTypeDef",
    "DBProxyTargetTypeDef",
    "DBProxyTypeDef",
    "DBRecommendationMessageTypeDef",
    "DBRecommendationTypeDef",
    "DBRecommendationsMessageTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSecurityGroupMessageTypeDef",
    "DBSecurityGroupTypeDef",
    "DBShardGroupResponseMetadataTypeDef",
    "DBShardGroupTypeDef",
    "DBSnapshotAttributeTypeDef",
    "DBSnapshotAttributesResultTypeDef",
    "DBSnapshotMessageTypeDef",
    "DBSnapshotTenantDatabaseTypeDef",
    "DBSnapshotTenantDatabasesMessageTypeDef",
    "DBSnapshotTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteBlueGreenDeploymentRequestRequestTypeDef",
    "DeleteBlueGreenDeploymentResponseTypeDef",
    "DeleteCustomDBEngineVersionMessageRequestTypeDef",
    "DeleteDBClusterAutomatedBackupMessageRequestTypeDef",
    "DeleteDBClusterAutomatedBackupResultTypeDef",
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceAutomatedBackupMessageRequestTypeDef",
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBParameterGroupMessageRequestTypeDef",
    "DeleteDBProxyEndpointRequestRequestTypeDef",
    "DeleteDBProxyEndpointResponseTypeDef",
    "DeleteDBProxyRequestRequestTypeDef",
    "DeleteDBProxyResponseTypeDef",
    "DeleteDBSecurityGroupMessageRequestTypeDef",
    "DeleteDBShardGroupMessageRequestTypeDef",
    "DeleteDBSnapshotMessageRequestTypeDef",
    "DeleteDBSnapshotResultTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterMessageRequestTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DeleteIntegrationMessageRequestTypeDef",
    "DeleteOptionGroupMessageRequestTypeDef",
    "DeleteTenantDatabaseMessageRequestTypeDef",
    "DeleteTenantDatabaseResultTypeDef",
    "DeregisterDBProxyTargetsRequestRequestTypeDef",
    "DescribeBlueGreenDeploymentsRequestRequestTypeDef",
    "DescribeBlueGreenDeploymentsResponseTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeDBClusterAutomatedBackupsMessageRequestTypeDef",
    "DescribeDBClusterBacktracksMessageRequestTypeDef",
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBLogFilesMessageRequestTypeDef",
    "DescribeDBLogFilesResponseTypeDef",
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    "DescribeDBParametersMessageRequestTypeDef",
    "DescribeDBProxiesRequestRequestTypeDef",
    "DescribeDBProxiesResponseTypeDef",
    "DescribeDBProxyEndpointsRequestRequestTypeDef",
    "DescribeDBProxyEndpointsResponseTypeDef",
    "DescribeDBProxyTargetGroupsRequestRequestTypeDef",
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    "DescribeDBProxyTargetsRequestRequestTypeDef",
    "DescribeDBProxyTargetsResponseTypeDef",
    "DescribeDBRecommendationsMessageRequestTypeDef",
    "DescribeDBSecurityGroupsMessageRequestTypeDef",
    "DescribeDBShardGroupsMessageRequestTypeDef",
    "DescribeDBShardGroupsResponseTypeDef",
    "DescribeDBSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBSnapshotAttributesResultTypeDef",
    "DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef",
    "DescribeDBSnapshotsMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeExportTasksMessageRequestTypeDef",
    "DescribeGlobalClustersMessageRequestTypeDef",
    "DescribeIntegrationsMessageRequestTypeDef",
    "DescribeIntegrationsResponseTypeDef",
    "DescribeOptionGroupOptionsMessageRequestTypeDef",
    "DescribeOptionGroupsMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribeReservedDBInstancesMessageRequestTypeDef",
    "DescribeReservedDBInstancesOfferingsMessageRequestTypeDef",
    "DescribeSourceRegionsMessageRequestTypeDef",
    "DescribeTenantDatabasesMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DisableHttpEndpointRequestRequestTypeDef",
    "DisableHttpEndpointResponseTypeDef",
    "DocLinkTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "DownloadDBLogFilePortionDetailsTypeDef",
    "DownloadDBLogFilePortionMessageRequestTypeDef",
    "EC2SecurityGroupTypeDef",
    "EnableHttpEndpointRequestRequestTypeDef",
    "EnableHttpEndpointResponseTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "ExportTaskResponseMetadataTypeDef",
    "ExportTaskTypeDef",
    "ExportTasksMessageTypeDef",
    "FailoverDBClusterMessageRequestTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FailoverGlobalClusterMessageRequestTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "FailoverStateTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "IPRangeTypeDef",
    "IntegrationErrorTypeDef",
    "IntegrationResponseMetadataTypeDef",
    "IntegrationTypeDef",
    "IssueDetailsTypeDef",
    "LimitlessDatabaseTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "MasterUserSecretTypeDef",
    "MetricQueryTypeDef",
    "MetricReferenceTypeDef",
    "MetricTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "ModifyActivityStreamRequestRequestTypeDef",
    "ModifyActivityStreamResponseTypeDef",
    "ModifyCertificatesMessageRequestTypeDef",
    "ModifyCertificatesResultTypeDef",
    "ModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    "ModifyCustomDBEngineVersionMessageRequestTypeDef",
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBParameterGroupMessageRequestTypeDef",
    "ModifyDBProxyEndpointRequestRequestTypeDef",
    "ModifyDBProxyEndpointResponseTypeDef",
    "ModifyDBProxyRequestRequestTypeDef",
    "ModifyDBProxyResponseTypeDef",
    "ModifyDBProxyTargetGroupRequestRequestTypeDef",
    "ModifyDBProxyTargetGroupResponseTypeDef",
    "ModifyDBRecommendationMessageRequestTypeDef",
    "ModifyDBShardGroupMessageRequestTypeDef",
    "ModifyDBSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBSnapshotAttributeResultTypeDef",
    "ModifyDBSnapshotMessageRequestTypeDef",
    "ModifyDBSnapshotResultTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterMessageRequestTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "ModifyIntegrationMessageRequestTypeDef",
    "ModifyOptionGroupMessageRequestTypeDef",
    "ModifyOptionGroupResultTypeDef",
    "ModifyTenantDatabaseMessageRequestTypeDef",
    "ModifyTenantDatabaseResultTypeDef",
    "OptionConfigurationTypeDef",
    "OptionGroupMembershipTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "OptionGroupOptionTypeDef",
    "OptionGroupOptionsMessageTypeDef",
    "OptionGroupTypeDef",
    "OptionGroupsTypeDef",
    "OptionSettingTypeDef",
    "OptionTypeDef",
    "OptionVersionTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    "PerformanceInsightsMetricQueryTypeDef",
    "PerformanceIssueDetailsTypeDef",
    "ProcessorFeatureTypeDef",
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "PromoteReadReplicaMessageRequestTypeDef",
    "PromoteReadReplicaResultTypeDef",
    "PurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    "RangeTypeDef",
    "RdsCustomClusterConfigurationTypeDef",
    "RebootDBClusterMessageRequestTypeDef",
    "RebootDBClusterResultTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RebootDBShardGroupMessageRequestTypeDef",
    "RecommendedActionParameterTypeDef",
    "RecommendedActionTypeDef",
    "RecommendedActionUpdateTypeDef",
    "RecurringChargeTypeDef",
    "ReferenceDetailsTypeDef",
    "RegisterDBProxyTargetsRequestRequestTypeDef",
    "RegisterDBProxyTargetsResponseTypeDef",
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    "RemoveRoleFromDBInstanceMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReservedDBInstanceMessageTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstancesOfferingMessageTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResetDBParameterGroupMessageRequestTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromS3MessageRequestTypeDef",
    "RestoreDBClusterFromS3ResultTypeDef",
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    "RestoreDBInstanceFromS3MessageRequestTypeDef",
    "RestoreDBInstanceFromS3ResultTypeDef",
    "RestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    "RestoreWindowTypeDef",
    "RevokeDBSecurityGroupIngressMessageRequestTypeDef",
    "RevokeDBSecurityGroupIngressResultTypeDef",
    "ScalarReferenceDetailsTypeDef",
    "ScalingConfigurationInfoTypeDef",
    "ScalingConfigurationTypeDef",
    "ServerlessV2ScalingConfigurationInfoTypeDef",
    "ServerlessV2ScalingConfigurationTypeDef",
    "SourceRegionMessageTypeDef",
    "SourceRegionTypeDef",
    "StartActivityStreamRequestRequestTypeDef",
    "StartActivityStreamResponseTypeDef",
    "StartDBClusterMessageRequestTypeDef",
    "StartDBClusterResultTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StartDBInstanceMessageRequestTypeDef",
    "StartDBInstanceResultTypeDef",
    "StartExportTaskMessageRequestTypeDef",
    "StopActivityStreamRequestRequestTypeDef",
    "StopActivityStreamResponseTypeDef",
    "StopDBClusterMessageRequestTypeDef",
    "StopDBClusterResultTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StopDBInstanceMessageRequestTypeDef",
    "StopDBInstanceResultTypeDef",
    "SubnetTypeDef",
    "SwitchoverBlueGreenDeploymentRequestRequestTypeDef",
    "SwitchoverBlueGreenDeploymentResponseTypeDef",
    "SwitchoverDetailTypeDef",
    "SwitchoverGlobalClusterMessageRequestTypeDef",
    "SwitchoverGlobalClusterResultTypeDef",
    "SwitchoverReadReplicaMessageRequestTypeDef",
    "SwitchoverReadReplicaResultTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TargetHealthTypeDef",
    "TenantDatabasePendingModifiedValuesTypeDef",
    "TenantDatabaseTypeDef",
    "TenantDatabasesMessageTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "UserAuthConfigInfoTypeDef",
    "UserAuthConfigTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributesMessageTypeDef = TypedDict(
    "AccountAttributesMessageTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredAddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredAddRoleToDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
    },
)
_OptionalAddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalAddRoleToDBClusterMessageRequestTypeDef",
    {
        "FeatureName": str,
    },
    total=False,
)

class AddRoleToDBClusterMessageRequestTypeDef(
    _RequiredAddRoleToDBClusterMessageRequestTypeDef,
    _OptionalAddRoleToDBClusterMessageRequestTypeDef,
):
    pass

AddRoleToDBInstanceMessageRequestTypeDef = TypedDict(
    "AddRoleToDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
    },
)

AddSourceIdentifierToSubscriptionMessageRequestTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAuthorizeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_RequiredAuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)
_OptionalAuthorizeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_OptionalAuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

class AuthorizeDBSecurityGroupIngressMessageRequestTypeDef(
    _RequiredAuthorizeDBSecurityGroupIngressMessageRequestTypeDef,
    _OptionalAuthorizeDBSecurityGroupIngressMessageRequestTypeDef,
):
    pass

AuthorizeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
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

AvailableProcessorFeatureTypeDef = TypedDict(
    "AvailableProcessorFeatureTypeDef",
    {
        "Name": str,
        "DefaultValue": str,
        "AllowedValues": str,
    },
    total=False,
)

_RequiredBacktrackDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredBacktrackDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackTo": Union[datetime, str],
    },
)
_OptionalBacktrackDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalBacktrackDBClusterMessageRequestTypeDef",
    {
        "Force": bool,
        "UseEarliestTimeOnPointInTimeUnavailable": bool,
    },
    total=False,
)

class BacktrackDBClusterMessageRequestTypeDef(
    _RequiredBacktrackDBClusterMessageRequestTypeDef,
    _OptionalBacktrackDBClusterMessageRequestTypeDef,
):
    pass

BlueGreenDeploymentTaskTypeDef = TypedDict(
    "BlueGreenDeploymentTaskTypeDef",
    {
        "Name": str,
        "Status": str,
    },
    total=False,
)

BlueGreenDeploymentTypeDef = TypedDict(
    "BlueGreenDeploymentTypeDef",
    {
        "BlueGreenDeploymentIdentifier": str,
        "BlueGreenDeploymentName": str,
        "Source": str,
        "Target": str,
        "SwitchoverDetails": List["SwitchoverDetailTypeDef"],
        "Tasks": List["BlueGreenDeploymentTaskTypeDef"],
        "Status": str,
        "StatusDetails": str,
        "CreateTime": datetime,
        "DeleteTime": datetime,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

CancelExportTaskMessageRequestTypeDef = TypedDict(
    "CancelExportTaskMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
    },
)

CertificateDetailsTypeDef = TypedDict(
    "CertificateDetailsTypeDef",
    {
        "CAIdentifier": str,
        "ValidTill": datetime,
    },
    total=False,
)

CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {
        "DefaultCertificateForNewLaunches": str,
        "Certificates": List["CertificateTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
        "CustomerOverride": bool,
        "CustomerOverrideValidTill": datetime,
    },
    total=False,
)

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef",
    {
        "CharacterSetName": str,
        "CharacterSetDescription": str,
    },
    total=False,
)

_RequiredClientGenerateDbAuthTokenRequestTypeDef = TypedDict(
    "_RequiredClientGenerateDbAuthTokenRequestTypeDef",
    {
        "DBHostname": str,
        "Port": int,
        "DBUsername": str,
    },
)
_OptionalClientGenerateDbAuthTokenRequestTypeDef = TypedDict(
    "_OptionalClientGenerateDbAuthTokenRequestTypeDef",
    {
        "Region": str,
    },
    total=False,
)

class ClientGenerateDbAuthTokenRequestTypeDef(
    _RequiredClientGenerateDbAuthTokenRequestTypeDef,
    _OptionalClientGenerateDbAuthTokenRequestTypeDef,
):
    pass

CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": List[str],
        "DisableLogTypes": List[str],
    },
    total=False,
)

ClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClusterPendingModifiedValuesTypeDef",
    {
        "PendingCloudwatchLogsExports": "PendingCloudwatchLogsExportsTypeDef",
        "DBClusterIdentifier": str,
        "MasterUserPassword": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "EngineVersion": str,
        "BackupRetentionPeriod": int,
        "AllocatedStorage": int,
        "RdsCustomClusterConfiguration": "RdsCustomClusterConfigurationTypeDef",
        "Iops": int,
        "StorageType": str,
        "CertificateDetails": "CertificateDetailsTypeDef",
    },
    total=False,
)

ConnectionPoolConfigurationInfoTypeDef = TypedDict(
    "ConnectionPoolConfigurationInfoTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

ConnectionPoolConfigurationTypeDef = TypedDict(
    "ConnectionPoolConfigurationTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

ContextAttributeTypeDef = TypedDict(
    "ContextAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredCopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "SourceDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupDescription": str,
    },
)
_OptionalCopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyDBClusterParameterGroupMessageRequestTypeDef(
    _RequiredCopyDBClusterParameterGroupMessageRequestTypeDef,
    _OptionalCopyDBClusterParameterGroupMessageRequestTypeDef,
):
    pass

CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "SourceDBClusterSnapshotIdentifier": str,
        "TargetDBClusterSnapshotIdentifier": str,
    },
)
_OptionalCopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "CopyTags": bool,
        "Tags": List["TagTypeDef"],
        "SourceRegion": str,
    },
    total=False,
)

class CopyDBClusterSnapshotMessageRequestTypeDef(
    _RequiredCopyDBClusterSnapshotMessageRequestTypeDef,
    _OptionalCopyDBClusterSnapshotMessageRequestTypeDef,
):
    pass

CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBParameterGroupMessageRequestTypeDef",
    {
        "SourceDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupDescription": str,
    },
)
_OptionalCopyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyDBParameterGroupMessageRequestTypeDef(
    _RequiredCopyDBParameterGroupMessageRequestTypeDef,
    _OptionalCopyDBParameterGroupMessageRequestTypeDef,
):
    pass

CopyDBParameterGroupResultTypeDef = TypedDict(
    "CopyDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyDBSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBSnapshotMessageRequestTypeDef",
    {
        "SourceDBSnapshotIdentifier": str,
        "TargetDBSnapshotIdentifier": str,
    },
)
_OptionalCopyDBSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBSnapshotMessageRequestTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "CopyTags": bool,
        "PreSignedUrl": str,
        "OptionGroupName": str,
        "TargetCustomAvailabilityZone": str,
        "CopyOptionGroup": bool,
        "SourceRegion": str,
    },
    total=False,
)

class CopyDBSnapshotMessageRequestTypeDef(
    _RequiredCopyDBSnapshotMessageRequestTypeDef, _OptionalCopyDBSnapshotMessageRequestTypeDef
):
    pass

CopyDBSnapshotResultTypeDef = TypedDict(
    "CopyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyOptionGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCopyOptionGroupMessageRequestTypeDef",
    {
        "SourceOptionGroupIdentifier": str,
        "TargetOptionGroupIdentifier": str,
        "TargetOptionGroupDescription": str,
    },
)
_OptionalCopyOptionGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCopyOptionGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyOptionGroupMessageRequestTypeDef(
    _RequiredCopyOptionGroupMessageRequestTypeDef, _OptionalCopyOptionGroupMessageRequestTypeDef
):
    pass

CopyOptionGroupResultTypeDef = TypedDict(
    "CopyOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBlueGreenDeploymentRequestRequestTypeDef",
    {
        "BlueGreenDeploymentName": str,
        "Source": str,
    },
)
_OptionalCreateBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBlueGreenDeploymentRequestRequestTypeDef",
    {
        "TargetEngineVersion": str,
        "TargetDBParameterGroupName": str,
        "TargetDBClusterParameterGroupName": str,
        "Tags": List["TagTypeDef"],
        "TargetDBInstanceClass": str,
        "UpgradeTargetStorageConfig": bool,
    },
    total=False,
)

class CreateBlueGreenDeploymentRequestRequestTypeDef(
    _RequiredCreateBlueGreenDeploymentRequestRequestTypeDef,
    _OptionalCreateBlueGreenDeploymentRequestRequestTypeDef,
):
    pass

CreateBlueGreenDeploymentResponseTypeDef = TypedDict(
    "CreateBlueGreenDeploymentResponseTypeDef",
    {
        "BlueGreenDeployment": "BlueGreenDeploymentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "_RequiredCreateCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
    },
)
_OptionalCreateCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "_OptionalCreateCustomDBEngineVersionMessageRequestTypeDef",
    {
        "DatabaseInstallationFilesS3BucketName": str,
        "DatabaseInstallationFilesS3Prefix": str,
        "ImageId": str,
        "KMSKeyId": str,
        "Description": str,
        "Manifest": str,
        "Tags": List["TagTypeDef"],
        "SourceCustomDbEngineVersionIdentifier": str,
        "UseAwsProvidedLatestImage": bool,
    },
    total=False,
)

class CreateCustomDBEngineVersionMessageRequestTypeDef(
    _RequiredCreateCustomDBEngineVersionMessageRequestTypeDef,
    _OptionalCreateCustomDBEngineVersionMessageRequestTypeDef,
):
    pass

_RequiredCreateDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "EndpointType": str,
    },
)
_OptionalCreateDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterEndpointMessageRequestTypeDef",
    {
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBClusterEndpointMessageRequestTypeDef(
    _RequiredCreateDBClusterEndpointMessageRequestTypeDef,
    _OptionalCreateDBClusterEndpointMessageRequestTypeDef,
):
    pass

_RequiredCreateDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
    },
)
_OptionalCreateDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterMessageRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableIAMDatabaseAuthentication": bool,
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "EngineMode": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "RdsCustomClusterConfiguration": "RdsCustomClusterConfigurationTypeDef",
        "DeletionProtection": bool,
        "GlobalClusterIdentifier": str,
        "EnableHttpEndpoint": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "EnableGlobalWriteForwarding": bool,
        "DBClusterInstanceClass": str,
        "AllocatedStorage": int,
        "StorageType": str,
        "Iops": int,
        "PubliclyAccessible": bool,
        "AutoMinorVersionUpgrade": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnableLimitlessDatabase": bool,
        "ServerlessV2ScalingConfiguration": "ServerlessV2ScalingConfigurationTypeDef",
        "NetworkType": str,
        "DBSystemId": str,
        "ManageMasterUserPassword": bool,
        "MasterUserSecretKmsKeyId": str,
        "EnableLocalWriteForwarding": bool,
        "CACertificateIdentifier": str,
        "EngineLifecycleSupport": str,
        "SourceRegion": str,
    },
    total=False,
)

class CreateDBClusterMessageRequestTypeDef(
    _RequiredCreateDBClusterMessageRequestTypeDef, _OptionalCreateDBClusterMessageRequestTypeDef
):
    pass

_RequiredCreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBClusterParameterGroupMessageRequestTypeDef(
    _RequiredCreateDBClusterParameterGroupMessageRequestTypeDef,
    _OptionalCreateDBClusterParameterGroupMessageRequestTypeDef,
):
    pass

CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
    },
)
_OptionalCreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBClusterSnapshotMessageRequestTypeDef(
    _RequiredCreateDBClusterSnapshotMessageRequestTypeDef,
    _OptionalCreateDBClusterSnapshotMessageRequestTypeDef,
):
    pass

CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
    },
)
_OptionalCreateDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBInstanceMessageRequestTypeDef",
    {
        "DBName": str,
        "AllocatedStorage": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "PreferredMaintenanceWindow": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "Port": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "CharacterSetName": str,
        "NcharCharacterSetName": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "DBClusterIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "Domain": str,
        "DomainFqdn": str,
        "DomainOu": str,
        "DomainAuthSecretArn": str,
        "DomainDnsIps": List[str],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "DomainIAMRoleName": str,
        "PromotionTier": int,
        "Timezone": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "DeletionProtection": bool,
        "MaxAllocatedStorage": int,
        "EnableCustomerOwnedIp": bool,
        "CustomIamInstanceProfile": str,
        "BackupTarget": str,
        "NetworkType": str,
        "StorageThroughput": int,
        "ManageMasterUserPassword": bool,
        "MasterUserSecretKmsKeyId": str,
        "CACertificateIdentifier": str,
        "DBSystemId": str,
        "DedicatedLogVolume": bool,
        "MultiTenant": bool,
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class CreateDBInstanceMessageRequestTypeDef(
    _RequiredCreateDBInstanceMessageRequestTypeDef, _OptionalCreateDBInstanceMessageRequestTypeDef
):
    pass

_RequiredCreateDBInstanceReadReplicaMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBInstanceReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalCreateDBInstanceReadReplicaMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBInstanceReadReplicaMessageRequestTypeDef",
    {
        "SourceDBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "AvailabilityZone": str,
        "Port": int,
        "MultiAZ": bool,
        "AutoMinorVersionUpgrade": bool,
        "Iops": int,
        "OptionGroupName": str,
        "DBParameterGroupName": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "DBSubnetGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "StorageType": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DeletionProtection": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "DomainFqdn": str,
        "DomainOu": str,
        "DomainAuthSecretArn": str,
        "DomainDnsIps": List[str],
        "ReplicaMode": ReplicaModeType,
        "MaxAllocatedStorage": int,
        "CustomIamInstanceProfile": str,
        "NetworkType": str,
        "StorageThroughput": int,
        "EnableCustomerOwnedIp": bool,
        "AllocatedStorage": int,
        "SourceDBClusterIdentifier": str,
        "DedicatedLogVolume": bool,
        "UpgradeStorageConfig": bool,
        "CACertificateIdentifier": str,
        "SourceRegion": str,
    },
    total=False,
)

class CreateDBInstanceReadReplicaMessageRequestTypeDef(
    _RequiredCreateDBInstanceReadReplicaMessageRequestTypeDef,
    _OptionalCreateDBInstanceReadReplicaMessageRequestTypeDef,
):
    pass

CreateDBInstanceReadReplicaResultTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBParameterGroupMessageRequestTypeDef(
    _RequiredCreateDBParameterGroupMessageRequestTypeDef,
    _OptionalCreateDBParameterGroupMessageRequestTypeDef,
):
    pass

CreateDBParameterGroupResultTypeDef = TypedDict(
    "CreateDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "DBProxyEndpointName": str,
        "VpcSubnetIds": List[str],
    },
)
_OptionalCreateDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDBProxyEndpointRequestRequestTypeDef",
    {
        "VpcSecurityGroupIds": List[str],
        "TargetRole": DBProxyEndpointTargetRoleType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBProxyEndpointRequestRequestTypeDef(
    _RequiredCreateDBProxyEndpointRequestRequestTypeDef,
    _OptionalCreateDBProxyEndpointRequestRequestTypeDef,
):
    pass

CreateDBProxyEndpointResponseTypeDef = TypedDict(
    "CreateDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBProxyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "EngineFamily": EngineFamilyType,
        "Auth": List["UserAuthConfigTypeDef"],
        "RoleArn": str,
        "VpcSubnetIds": List[str],
    },
)
_OptionalCreateDBProxyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDBProxyRequestRequestTypeDef",
    {
        "VpcSecurityGroupIds": List[str],
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBProxyRequestRequestTypeDef(
    _RequiredCreateDBProxyRequestRequestTypeDef, _OptionalCreateDBProxyRequestRequestTypeDef
):
    pass

CreateDBProxyResponseTypeDef = TypedDict(
    "CreateDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBSecurityGroupMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
    },
)
_OptionalCreateDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBSecurityGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBSecurityGroupMessageRequestTypeDef(
    _RequiredCreateDBSecurityGroupMessageRequestTypeDef,
    _OptionalCreateDBSecurityGroupMessageRequestTypeDef,
):
    pass

CreateDBSecurityGroupResultTypeDef = TypedDict(
    "CreateDBSecurityGroupResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBShardGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBShardGroupMessageRequestTypeDef",
    {
        "DBShardGroupIdentifier": str,
        "DBClusterIdentifier": str,
        "MaxACU": float,
    },
)
_OptionalCreateDBShardGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBShardGroupMessageRequestTypeDef",
    {
        "ComputeRedundancy": int,
        "PubliclyAccessible": bool,
    },
    total=False,
)

class CreateDBShardGroupMessageRequestTypeDef(
    _RequiredCreateDBShardGroupMessageRequestTypeDef,
    _OptionalCreateDBShardGroupMessageRequestTypeDef,
):
    pass

_RequiredCreateDBSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
    },
)
_OptionalCreateDBSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBSnapshotMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBSnapshotMessageRequestTypeDef(
    _RequiredCreateDBSnapshotMessageRequestTypeDef, _OptionalCreateDBSnapshotMessageRequestTypeDef
):
    pass

CreateDBSnapshotResultTypeDef = TypedDict(
    "CreateDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBSubnetGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBSubnetGroupMessageRequestTypeDef(
    _RequiredCreateDBSubnetGroupMessageRequestTypeDef,
    _OptionalCreateDBSubnetGroupMessageRequestTypeDef,
):
    pass

CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
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

CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalClusterMessageRequestTypeDef = TypedDict(
    "CreateGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "SourceDBClusterIdentifier": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineLifecycleSupport": str,
        "DeletionProtection": bool,
        "DatabaseName": str,
        "StorageEncrypted": bool,
    },
    total=False,
)

CreateGlobalClusterResultTypeDef = TypedDict(
    "CreateGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationMessageRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationMessageRequestTypeDef",
    {
        "SourceArn": str,
        "TargetArn": str,
        "IntegrationName": str,
    },
)
_OptionalCreateIntegrationMessageRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationMessageRequestTypeDef",
    {
        "KMSKeyId": str,
        "AdditionalEncryptionContext": Dict[str, str],
        "Tags": List["TagTypeDef"],
        "DataFilter": str,
        "Description": str,
    },
    total=False,
)

class CreateIntegrationMessageRequestTypeDef(
    _RequiredCreateIntegrationMessageRequestTypeDef, _OptionalCreateIntegrationMessageRequestTypeDef
):
    pass

_RequiredCreateOptionGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "OptionGroupDescription": str,
    },
)
_OptionalCreateOptionGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateOptionGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateOptionGroupMessageRequestTypeDef(
    _RequiredCreateOptionGroupMessageRequestTypeDef, _OptionalCreateOptionGroupMessageRequestTypeDef
):
    pass

CreateOptionGroupResultTypeDef = TypedDict(
    "CreateOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTenantDatabaseMessageRequestTypeDef = TypedDict(
    "_RequiredCreateTenantDatabaseMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
    },
)
_OptionalCreateTenantDatabaseMessageRequestTypeDef = TypedDict(
    "_OptionalCreateTenantDatabaseMessageRequestTypeDef",
    {
        "CharacterSetName": str,
        "NcharCharacterSetName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTenantDatabaseMessageRequestTypeDef(
    _RequiredCreateTenantDatabaseMessageRequestTypeDef,
    _OptionalCreateTenantDatabaseMessageRequestTypeDef,
):
    pass

CreateTenantDatabaseResultTypeDef = TypedDict(
    "CreateTenantDatabaseResultTypeDef",
    {
        "TenantDatabase": "TenantDatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDBEngineVersionAMITypeDef = TypedDict(
    "CustomDBEngineVersionAMITypeDef",
    {
        "ImageId": str,
        "Status": str,
    },
    total=False,
)

DBClusterAutomatedBackupMessageTypeDef = TypedDict(
    "DBClusterAutomatedBackupMessageTypeDef",
    {
        "Marker": str,
        "DBClusterAutomatedBackups": List["DBClusterAutomatedBackupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterAutomatedBackupTypeDef = TypedDict(
    "DBClusterAutomatedBackupTypeDef",
    {
        "Engine": str,
        "VpcId": str,
        "DBClusterAutomatedBackupsArn": str,
        "DBClusterIdentifier": str,
        "RestoreWindow": "RestoreWindowTypeDef",
        "MasterUsername": str,
        "DbClusterResourceId": str,
        "Region": str,
        "LicenseModel": str,
        "Status": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ClusterCreateTime": datetime,
        "StorageEncrypted": bool,
        "AllocatedStorage": int,
        "EngineVersion": str,
        "DBClusterArn": str,
        "BackupRetentionPeriod": int,
        "EngineMode": str,
        "AvailabilityZones": List[str],
        "Port": int,
        "KmsKeyId": str,
        "StorageType": str,
        "Iops": int,
        "AwsBackupRecoveryPointArn": str,
        "StorageThroughput": int,
    },
    total=False,
)

DBClusterBacktrackMessageTypeDef = TypedDict(
    "DBClusterBacktrackMessageTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List["DBClusterBacktrackTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterBacktrackResponseMetadataTypeDef = TypedDict(
    "DBClusterBacktrackResponseMetadataTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterBacktrackTypeDef = TypedDict(
    "DBClusterBacktrackTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)

DBClusterCapacityInfoTypeDef = TypedDict(
    "DBClusterCapacityInfoTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointMessageTypeDef = TypedDict(
    "DBClusterEndpointMessageTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List["DBClusterEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointResponseMetadataTypeDef = TypedDict(
    "DBClusterEndpointResponseMetadataTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointTypeDef = TypedDict(
    "DBClusterEndpointTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)

DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef",
    {
        "Marker": str,
        "DBClusters": List["DBClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {
        "DBClusterOptionGroupName": str,
        "Status": str,
    },
    total=False,
)

DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List["DBClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef",
    {
        "RoleArn": str,
        "Status": str,
        "FeatureName": str,
    },
    total=False,
)

DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[str],
    },
    total=False,
)

DBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List["DBClusterSnapshotAttributeTypeDef"],
    },
    total=False,
)

DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List["DBClusterSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "EngineMode": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "TagList": List["TagTypeDef"],
        "DBSystemId": str,
        "StorageType": str,
        "DbClusterResourceId": str,
        "StorageThroughput": int,
    },
    total=False,
)

DBClusterStatusInfoTypeDef = TypedDict(
    "DBClusterStatusInfoTypeDef",
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
    total=False,
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "AutomaticRestartTime": datetime,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List["DBClusterOptionGroupStatusTypeDef"],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "StatusInfos": List["DBClusterStatusInfoTypeDef"],
        "DBClusterMembers": List["DBClusterMemberTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List["DBClusterRoleTypeDef"],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": "ScalingConfigurationInfoTypeDef",
        "RdsCustomClusterConfiguration": "RdsCustomClusterConfigurationTypeDef",
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": ActivityStreamModeType,
        "ActivityStreamStatus": ActivityStreamStatusType,
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
        "DomainMemberships": List["DomainMembershipTypeDef"],
        "TagList": List["TagTypeDef"],
        "GlobalWriteForwardingStatus": WriteForwardingStatusType,
        "GlobalWriteForwardingRequested": bool,
        "PendingModifiedValues": "ClusterPendingModifiedValuesTypeDef",
        "DBClusterInstanceClass": str,
        "StorageType": str,
        "Iops": int,
        "PubliclyAccessible": bool,
        "AutoMinorVersionUpgrade": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "ServerlessV2ScalingConfiguration": "ServerlessV2ScalingConfigurationInfoTypeDef",
        "NetworkType": str,
        "DBSystemId": str,
        "MasterUserSecret": "MasterUserSecretTypeDef",
        "IOOptimizedNextAllowedModificationTime": datetime,
        "LocalWriteForwardingStatus": LocalWriteForwardingStatusType,
        "AwsBackupRecoveryPointArn": str,
        "LimitlessDatabase": "LimitlessDatabaseTypeDef",
        "StorageThroughput": int,
        "CertificateDetails": "CertificateDetailsTypeDef",
        "EngineLifecycleSupport": str,
    },
    total=False,
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List["DBEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBEngineVersionResponseMetadataTypeDef = TypedDict(
    "DBEngineVersionResponseMetadataTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": "CharacterSetTypeDef",
        "Image": "CustomDBEngineVersionAMITypeDef",
        "DBEngineMediaType": str,
        "SupportedCharacterSets": List["CharacterSetTypeDef"],
        "SupportedNcharCharacterSets": List["CharacterSetTypeDef"],
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "SupportedTimezones": List["TimezoneTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
        "MajorEngineVersion": str,
        "DatabaseInstallationFilesS3BucketName": str,
        "DatabaseInstallationFilesS3Prefix": str,
        "DBEngineVersionArn": str,
        "KMSKeyId": str,
        "CreateTime": datetime,
        "TagList": List["TagTypeDef"],
        "SupportsBabelfish": bool,
        "CustomDBEngineVersionManifest": str,
        "SupportsLimitlessDatabase": bool,
        "SupportsCertificateRotationWithoutRestart": bool,
        "SupportedCACertificateIdentifiers": List[str],
        "SupportsLocalWriteForwarding": bool,
        "SupportsIntegrations": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": "CharacterSetTypeDef",
        "Image": "CustomDBEngineVersionAMITypeDef",
        "DBEngineMediaType": str,
        "SupportedCharacterSets": List["CharacterSetTypeDef"],
        "SupportedNcharCharacterSets": List["CharacterSetTypeDef"],
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "SupportedTimezones": List["TimezoneTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
        "MajorEngineVersion": str,
        "DatabaseInstallationFilesS3BucketName": str,
        "DatabaseInstallationFilesS3Prefix": str,
        "DBEngineVersionArn": str,
        "KMSKeyId": str,
        "CreateTime": datetime,
        "TagList": List["TagTypeDef"],
        "SupportsBabelfish": bool,
        "CustomDBEngineVersionManifest": str,
        "SupportsLimitlessDatabase": bool,
        "SupportsCertificateRotationWithoutRestart": bool,
        "SupportedCACertificateIdentifiers": List[str],
        "SupportsLocalWriteForwarding": bool,
        "SupportsIntegrations": bool,
    },
    total=False,
)

DBInstanceAutomatedBackupMessageTypeDef = TypedDict(
    "DBInstanceAutomatedBackupMessageTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List["DBInstanceAutomatedBackupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBInstanceAutomatedBackupTypeDef = TypedDict(
    "DBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": "RestoreWindowTypeDef",
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "BackupRetentionPeriod": int,
        "DBInstanceAutomatedBackupsArn": str,
        "DBInstanceAutomatedBackupsReplications": List[
            "DBInstanceAutomatedBackupsReplicationTypeDef"
        ],
        "BackupTarget": str,
        "StorageThroughput": int,
        "AwsBackupRecoveryPointArn": str,
        "DedicatedLogVolume": bool,
        "MultiTenant": bool,
    },
    total=False,
)

DBInstanceAutomatedBackupsReplicationTypeDef = TypedDict(
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    {
        "DBInstanceAutomatedBackupsArn": str,
    },
    total=False,
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {
        "Marker": str,
        "DBInstances": List["DBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBInstanceRoleTypeDef = TypedDict(
    "DBInstanceRoleTypeDef",
    {
        "RoleArn": str,
        "FeatureName": str,
        "Status": str,
    },
    total=False,
)

DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
    total=False,
)

DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "AutomaticRestartTime": datetime,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": "EndpointTypeDef",
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List["DBSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "DBParameterGroups": List["DBParameterGroupStatusTypeDef"],
        "AvailabilityZone": str,
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "ReplicaMode": ReplicaModeType,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List["OptionGroupMembershipTypeDef"],
        "CharacterSetName": str,
        "NcharCharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List["DBInstanceStatusInfoTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List["DomainMembershipTypeDef"],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "DeletionProtection": bool,
        "AssociatedRoles": List["DBInstanceRoleTypeDef"],
        "ListenerEndpoint": "EndpointTypeDef",
        "MaxAllocatedStorage": int,
        "TagList": List["TagTypeDef"],
        "DBInstanceAutomatedBackupsReplications": List[
            "DBInstanceAutomatedBackupsReplicationTypeDef"
        ],
        "CustomerOwnedIpEnabled": bool,
        "AwsBackupRecoveryPointArn": str,
        "ActivityStreamStatus": ActivityStreamStatusType,
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "ActivityStreamMode": ActivityStreamModeType,
        "ActivityStreamEngineNativeAuditFieldsIncluded": bool,
        "AutomationMode": AutomationModeType,
        "ResumeFullAutomationModeTime": datetime,
        "CustomIamInstanceProfile": str,
        "BackupTarget": str,
        "NetworkType": str,
        "ActivityStreamPolicyStatus": ActivityStreamPolicyStatusType,
        "StorageThroughput": int,
        "DBSystemId": str,
        "MasterUserSecret": "MasterUserSecretTypeDef",
        "CertificateDetails": "CertificateDetailsTypeDef",
        "ReadReplicaSourceDBClusterIdentifier": str,
        "PercentProgress": str,
        "DedicatedLogVolume": bool,
        "IsStorageConfigUpgradeAvailable": bool,
        "MultiTenant": bool,
        "EngineLifecycleSupport": str,
    },
    total=False,
)

DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupNameMessageTypeDef = TypedDict(
    "DBParameterGroupNameMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {
        "DBParameterGroupName": str,
        "ParameterApplyStatus": str,
    },
    total=False,
)

DBParameterGroupTypeDef = TypedDict(
    "DBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List["DBParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBProxyEndpointTypeDef = TypedDict(
    "DBProxyEndpointTypeDef",
    {
        "DBProxyEndpointName": str,
        "DBProxyEndpointArn": str,
        "DBProxyName": str,
        "Status": DBProxyEndpointStatusType,
        "VpcId": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Endpoint": str,
        "CreatedDate": datetime,
        "TargetRole": DBProxyEndpointTargetRoleType,
        "IsDefault": bool,
    },
    total=False,
)

DBProxyTargetGroupTypeDef = TypedDict(
    "DBProxyTargetGroupTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": "ConnectionPoolConfigurationInfoTypeDef",
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

DBProxyTargetTypeDef = TypedDict(
    "DBProxyTargetTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": TargetTypeType,
        "Role": TargetRoleType,
        "TargetHealth": "TargetHealthTypeDef",
    },
    total=False,
)

DBProxyTypeDef = TypedDict(
    "DBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": DBProxyStatusType,
        "EngineFamily": str,
        "VpcId": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List["UserAuthConfigInfoTypeDef"],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

DBRecommendationMessageTypeDef = TypedDict(
    "DBRecommendationMessageTypeDef",
    {
        "DBRecommendation": "DBRecommendationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBRecommendationTypeDef = TypedDict(
    "DBRecommendationTypeDef",
    {
        "RecommendationId": str,
        "TypeId": str,
        "Severity": str,
        "ResourceArn": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "Detection": str,
        "Recommendation": str,
        "Description": str,
        "Reason": str,
        "RecommendedActions": List["RecommendedActionTypeDef"],
        "Category": str,
        "Source": str,
        "TypeDetection": str,
        "TypeRecommendation": str,
        "Impact": str,
        "AdditionalInfo": str,
        "Links": List["DocLinkTypeDef"],
        "IssueDetails": "IssueDetailsTypeDef",
    },
    total=False,
)

DBRecommendationsMessageTypeDef = TypedDict(
    "DBRecommendationsMessageTypeDef",
    {
        "DBRecommendations": List["DBRecommendationTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

DBSecurityGroupMessageTypeDef = TypedDict(
    "DBSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List["DBSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSecurityGroupTypeDef = TypedDict(
    "DBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "IPRanges": List["IPRangeTypeDef"],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

DBShardGroupResponseMetadataTypeDef = TypedDict(
    "DBShardGroupResponseMetadataTypeDef",
    {
        "DBShardGroupResourceId": str,
        "DBShardGroupIdentifier": str,
        "DBClusterIdentifier": str,
        "MaxACU": float,
        "ComputeRedundancy": int,
        "Status": str,
        "PubliclyAccessible": bool,
        "Endpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBShardGroupTypeDef = TypedDict(
    "DBShardGroupTypeDef",
    {
        "DBShardGroupResourceId": str,
        "DBShardGroupIdentifier": str,
        "DBClusterIdentifier": str,
        "MaxACU": float,
        "ComputeRedundancy": int,
        "Status": str,
        "PubliclyAccessible": bool,
        "Endpoint": str,
    },
    total=False,
)

DBSnapshotAttributeTypeDef = TypedDict(
    "DBSnapshotAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[str],
    },
    total=False,
)

DBSnapshotAttributesResultTypeDef = TypedDict(
    "DBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBSnapshotAttributes": List["DBSnapshotAttributeTypeDef"],
    },
    total=False,
)

DBSnapshotMessageTypeDef = TypedDict(
    "DBSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBSnapshots": List["DBSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSnapshotTenantDatabaseTypeDef = TypedDict(
    "DBSnapshotTenantDatabaseTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "DbiResourceId": str,
        "EngineName": str,
        "SnapshotType": str,
        "TenantDatabaseCreateTime": datetime,
        "TenantDBName": str,
        "MasterUsername": str,
        "TenantDatabaseResourceId": str,
        "CharacterSetName": str,
        "DBSnapshotTenantDatabaseARN": str,
        "NcharCharacterSetName": str,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

DBSnapshotTenantDatabasesMessageTypeDef = TypedDict(
    "DBSnapshotTenantDatabasesMessageTypeDef",
    {
        "Marker": str,
        "DBSnapshotTenantDatabases": List["DBSnapshotTenantDatabaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSnapshotTypeDef = TypedDict(
    "DBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "DbiResourceId": str,
        "TagList": List["TagTypeDef"],
        "OriginalSnapshotCreateTime": datetime,
        "SnapshotDatabaseTime": datetime,
        "SnapshotTarget": str,
        "StorageThroughput": int,
        "DBSystemId": str,
        "DedicatedLogVolume": bool,
        "MultiTenant": bool,
    },
    total=False,
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List["DBSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "DBSubnetGroupArn": str,
        "SupportedNetworkTypes": List[str],
    },
    total=False,
)

_RequiredDeleteBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBlueGreenDeploymentRequestRequestTypeDef",
    {
        "BlueGreenDeploymentIdentifier": str,
    },
)
_OptionalDeleteBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBlueGreenDeploymentRequestRequestTypeDef",
    {
        "DeleteTarget": bool,
    },
    total=False,
)

class DeleteBlueGreenDeploymentRequestRequestTypeDef(
    _RequiredDeleteBlueGreenDeploymentRequestRequestTypeDef,
    _OptionalDeleteBlueGreenDeploymentRequestRequestTypeDef,
):
    pass

DeleteBlueGreenDeploymentResponseTypeDef = TypedDict(
    "DeleteBlueGreenDeploymentResponseTypeDef",
    {
        "BlueGreenDeployment": "BlueGreenDeploymentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "DeleteCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
    },
)

DeleteDBClusterAutomatedBackupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterAutomatedBackupMessageRequestTypeDef",
    {
        "DbClusterResourceId": str,
    },
)

DeleteDBClusterAutomatedBackupResultTypeDef = TypedDict(
    "DeleteDBClusterAutomatedBackupResultTypeDef",
    {
        "DBClusterAutomatedBackup": "DBClusterAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)

_RequiredDeleteDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalDeleteDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteDBClusterMessageRequestTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
        "DeleteAutomatedBackups": bool,
    },
    total=False,
)

class DeleteDBClusterMessageRequestTypeDef(
    _RequiredDeleteDBClusterMessageRequestTypeDef, _OptionalDeleteDBClusterMessageRequestTypeDef
):
    pass

DeleteDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)

DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBInstanceAutomatedBackupMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupMessageRequestTypeDef",
    {
        "DbiResourceId": str,
        "DBInstanceAutomatedBackupsArn": str,
    },
    total=False,
)

DeleteDBInstanceAutomatedBackupResultTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalDeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteDBInstanceMessageRequestTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
        "DeleteAutomatedBackups": bool,
    },
    total=False,
)

class DeleteDBInstanceMessageRequestTypeDef(
    _RequiredDeleteDBInstanceMessageRequestTypeDef, _OptionalDeleteDBInstanceMessageRequestTypeDef
):
    pass

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
    },
)

DeleteDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "DeleteDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyEndpointName": str,
    },
)

DeleteDBProxyEndpointResponseTypeDef = TypedDict(
    "DeleteDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBProxyRequestRequestTypeDef = TypedDict(
    "DeleteDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)

DeleteDBProxyResponseTypeDef = TypedDict(
    "DeleteDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSecurityGroupMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)

DeleteDBShardGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBShardGroupMessageRequestTypeDef",
    {
        "DBShardGroupIdentifier": str,
    },
)

DeleteDBSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)

DeleteDBSnapshotResultTypeDef = TypedDict(
    "DeleteDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalClusterMessageRequestTypeDef = TypedDict(
    "DeleteGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)

DeleteGlobalClusterResultTypeDef = TypedDict(
    "DeleteGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntegrationMessageRequestTypeDef = TypedDict(
    "DeleteIntegrationMessageRequestTypeDef",
    {
        "IntegrationIdentifier": str,
    },
)

DeleteOptionGroupMessageRequestTypeDef = TypedDict(
    "DeleteOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
    },
)

_RequiredDeleteTenantDatabaseMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteTenantDatabaseMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
    },
)
_OptionalDeleteTenantDatabaseMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteTenantDatabaseMessageRequestTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
    },
    total=False,
)

class DeleteTenantDatabaseMessageRequestTypeDef(
    _RequiredDeleteTenantDatabaseMessageRequestTypeDef,
    _OptionalDeleteTenantDatabaseMessageRequestTypeDef,
):
    pass

DeleteTenantDatabaseResultTypeDef = TypedDict(
    "DeleteTenantDatabaseResultTypeDef",
    {
        "TenantDatabase": "TenantDatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeregisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalDeregisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterDBProxyTargetsRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBInstanceIdentifiers": List[str],
        "DBClusterIdentifiers": List[str],
    },
    total=False,
)

class DeregisterDBProxyTargetsRequestRequestTypeDef(
    _RequiredDeregisterDBProxyTargetsRequestRequestTypeDef,
    _OptionalDeregisterDBProxyTargetsRequestRequestTypeDef,
):
    pass

DescribeBlueGreenDeploymentsRequestRequestTypeDef = TypedDict(
    "DescribeBlueGreenDeploymentsRequestRequestTypeDef",
    {
        "BlueGreenDeploymentIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeBlueGreenDeploymentsResponseTypeDef = TypedDict(
    "DescribeBlueGreenDeploymentsResponseTypeDef",
    {
        "BlueGreenDeployments": List["BlueGreenDeploymentTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBClusterAutomatedBackupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterAutomatedBackupsMessageRequestTypeDef",
    {
        "DbClusterResourceId": str,
        "DBClusterIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBClusterBacktracksMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDBClusterBacktracksMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalDescribeDBClusterBacktracksMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDBClusterBacktracksMessageRequestTypeDef",
    {
        "BacktrackIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDBClusterBacktracksMessageRequestTypeDef(
    _RequiredDescribeDBClusterBacktracksMessageRequestTypeDef,
    _OptionalDescribeDBClusterBacktracksMessageRequestTypeDef,
):
    pass

DescribeDBClusterEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDBClusterParametersMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
_OptionalDescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDBClusterParametersMessageRequestTypeDef",
    {
        "Source": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDBClusterParametersMessageRequestTypeDef(
    _RequiredDescribeDBClusterParametersMessageRequestTypeDef,
    _OptionalDescribeDBClusterParametersMessageRequestTypeDef,
):
    pass

DescribeDBClusterSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterSnapshotIdentifier": str,
        "SnapshotType": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "IncludeShared": bool,
        "IncludePublic": bool,
        "DbClusterResourceId": str,
    },
    total=False,
)

DescribeDBClustersMessageRequestTypeDef = TypedDict(
    "DescribeDBClustersMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "IncludeShared": bool,
    },
    total=False,
)

DescribeDBEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "DefaultOnly": bool,
        "ListSupportedCharacterSets": bool,
        "ListSupportedTimezones": bool,
        "IncludeAll": bool,
    },
    total=False,
)

DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef = TypedDict(
    "DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef",
    {
        "DbiResourceId": str,
        "DBInstanceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "DBInstanceAutomatedBackupsArn": str,
    },
    total=False,
)

DescribeDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeDBInstancesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBLogFilesDetailsTypeDef = TypedDict(
    "DescribeDBLogFilesDetailsTypeDef",
    {
        "LogFileName": str,
        "LastWritten": int,
        "Size": int,
    },
    total=False,
)

_RequiredDescribeDBLogFilesMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDBLogFilesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalDescribeDBLogFilesMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDBLogFilesMessageRequestTypeDef",
    {
        "FilenameContains": str,
        "FileLastWritten": int,
        "FileSize": int,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDBLogFilesMessageRequestTypeDef(
    _RequiredDescribeDBLogFilesMessageRequestTypeDef,
    _OptionalDescribeDBLogFilesMessageRequestTypeDef,
):
    pass

DescribeDBLogFilesResponseTypeDef = TypedDict(
    "DescribeDBLogFilesResponseTypeDef",
    {
        "DescribeDBLogFiles": List["DescribeDBLogFilesDetailsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDBParametersMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
_OptionalDescribeDBParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDBParametersMessageRequestTypeDef",
    {
        "Source": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDBParametersMessageRequestTypeDef(
    _RequiredDescribeDBParametersMessageRequestTypeDef,
    _OptionalDescribeDBParametersMessageRequestTypeDef,
):
    pass

DescribeDBProxiesRequestRequestTypeDef = TypedDict(
    "DescribeDBProxiesRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeDBProxiesResponseTypeDef = TypedDict(
    "DescribeDBProxiesResponseTypeDef",
    {
        "DBProxies": List["DBProxyTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBProxyEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyEndpointsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "DBProxyEndpointName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeDBProxyEndpointsResponseTypeDef = TypedDict(
    "DescribeDBProxyEndpointsResponseTypeDef",
    {
        "DBProxyEndpoints": List["DBProxyEndpointTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDBProxyTargetGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDBProxyTargetGroupsRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalDescribeDBProxyTargetGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDBProxyTargetGroupsRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeDBProxyTargetGroupsRequestRequestTypeDef(
    _RequiredDescribeDBProxyTargetGroupsRequestRequestTypeDef,
    _OptionalDescribeDBProxyTargetGroupsRequestRequestTypeDef,
):
    pass

DescribeDBProxyTargetGroupsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List["DBProxyTargetGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalDescribeDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDBProxyTargetsRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeDBProxyTargetsRequestRequestTypeDef(
    _RequiredDescribeDBProxyTargetsRequestRequestTypeDef,
    _OptionalDescribeDBProxyTargetsRequestRequestTypeDef,
):
    pass

DescribeDBProxyTargetsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetsResponseTypeDef",
    {
        "Targets": List["DBProxyTargetTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBRecommendationsMessageRequestTypeDef = TypedDict(
    "DescribeDBRecommendationsMessageRequestTypeDef",
    {
        "LastUpdatedAfter": Union[datetime, str],
        "LastUpdatedBefore": Union[datetime, str],
        "Locale": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSecurityGroupsMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBShardGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBShardGroupsMessageRequestTypeDef",
    {
        "DBShardGroupIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeDBShardGroupsResponseTypeDef = TypedDict(
    "DescribeDBShardGroupsResponseTypeDef",
    {
        "DBShardGroups": List["DBShardGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)

DescribeDBSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": str,
        "SnapshotType": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "DbiResourceId": str,
    },
    total=False,
)

DescribeDBSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": str,
        "SnapshotType": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "IncludeShared": bool,
        "IncludePublic": bool,
        "DbiResourceId": str,
    },
    total=False,
)

DescribeDBSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEngineDefaultClusterParametersMessageRequestTypeDef(
    _RequiredDescribeEngineDefaultClusterParametersMessageRequestTypeDef,
    _OptionalDescribeEngineDefaultClusterParametersMessageRequestTypeDef,
):
    pass

DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEngineDefaultParametersMessageRequestTypeDef(
    _RequiredDescribeEngineDefaultParametersMessageRequestTypeDef,
    _OptionalDescribeEngineDefaultParametersMessageRequestTypeDef,
):
    pass

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
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

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
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

DescribeExportTasksMessageRequestTypeDef = TypedDict(
    "DescribeExportTasksMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
        "SourceType": ExportSourceTypeType,
    },
    total=False,
)

DescribeGlobalClustersMessageRequestTypeDef = TypedDict(
    "DescribeGlobalClustersMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeIntegrationsMessageRequestTypeDef = TypedDict(
    "DescribeIntegrationsMessageRequestTypeDef",
    {
        "IntegrationIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeIntegrationsResponseTypeDef = TypedDict(
    "DescribeIntegrationsResponseTypeDef",
    {
        "Marker": str,
        "Integrations": List["IntegrationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeOptionGroupOptionsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeOptionGroupOptionsMessageRequestTypeDef",
    {
        "EngineName": str,
    },
)
_OptionalDescribeOptionGroupOptionsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeOptionGroupOptionsMessageRequestTypeDef",
    {
        "MajorEngineVersion": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeOptionGroupOptionsMessageRequestTypeDef(
    _RequiredDescribeOptionGroupOptionsMessageRequestTypeDef,
    _OptionalDescribeOptionGroupOptionsMessageRequestTypeDef,
):
    pass

DescribeOptionGroupsMessageRequestTypeDef = TypedDict(
    "DescribeOptionGroupsMessageRequestTypeDef",
    {
        "OptionGroupName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
        "EngineName": str,
        "MajorEngineVersion": str,
    },
    total=False,
)

_RequiredDescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "Engine": str,
    },
)
_OptionalDescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZoneGroup": str,
        "Vpc": bool,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeOrderableDBInstanceOptionsMessageRequestTypeDef(
    _RequiredDescribeOrderableDBInstanceOptionsMessageRequestTypeDef,
    _OptionalDescribeOrderableDBInstanceOptionsMessageRequestTypeDef,
):
    pass

DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeReservedDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReservedDBInstancesMessageRequestTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "LeaseId": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedDBInstancesOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedDBInstancesOfferingsMessageRequestTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeSourceRegionsMessageRequestTypeDef = TypedDict(
    "DescribeSourceRegionsMessageRequestTypeDef",
    {
        "RegionName": str,
        "MaxRecords": int,
        "Marker": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeTenantDatabasesMessageRequestTypeDef = TypedDict(
    "DescribeTenantDatabasesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeValidDBInstanceModificationsMessageRequestTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DescribeValidDBInstanceModificationsResultTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultTypeDef",
    {
        "ValidDBInstanceModificationsMessage": "ValidDBInstanceModificationsMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableHttpEndpointRequestRequestTypeDef = TypedDict(
    "DisableHttpEndpointRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DisableHttpEndpointResponseTypeDef = TypedDict(
    "DisableHttpEndpointResponseTypeDef",
    {
        "ResourceArn": str,
        "HttpEndpointEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocLinkTypeDef = TypedDict(
    "DocLinkTypeDef",
    {
        "Text": str,
        "Url": str,
    },
    total=False,
)

DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {
        "Domain": str,
        "Status": str,
        "FQDN": str,
        "IAMRoleName": str,
        "OU": str,
        "AuthSecretArn": str,
        "DnsIps": List[str],
    },
    total=False,
)

DoubleRangeTypeDef = TypedDict(
    "DoubleRangeTypeDef",
    {
        "From": float,
        "To": float,
    },
    total=False,
)

DownloadDBLogFilePortionDetailsTypeDef = TypedDict(
    "DownloadDBLogFilePortionDetailsTypeDef",
    {
        "LogFileData": str,
        "Marker": str,
        "AdditionalDataPending": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDownloadDBLogFilePortionMessageRequestTypeDef = TypedDict(
    "_RequiredDownloadDBLogFilePortionMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "LogFileName": str,
    },
)
_OptionalDownloadDBLogFilePortionMessageRequestTypeDef = TypedDict(
    "_OptionalDownloadDBLogFilePortionMessageRequestTypeDef",
    {
        "Marker": str,
        "NumberOfLines": int,
    },
    total=False,
)

class DownloadDBLogFilePortionMessageRequestTypeDef(
    _RequiredDownloadDBLogFilePortionMessageRequestTypeDef,
    _OptionalDownloadDBLogFilePortionMessageRequestTypeDef,
):
    pass

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

EnableHttpEndpointRequestRequestTypeDef = TypedDict(
    "EnableHttpEndpointRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

EnableHttpEndpointResponseTypeDef = TypedDict(
    "EnableHttpEndpointResponseTypeDef",
    {
        "ResourceArn": str,
        "HttpEndpointEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "HostedZoneId": str,
    },
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
    },
    total=False,
)

EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "EventSubscriptionArn": str,
    },
    total=False,
)

EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportTaskResponseMetadataTypeDef = TypedDict(
    "ExportTaskResponseMetadataTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
        "SourceType": ExportSourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
        "SourceType": ExportSourceTypeType,
    },
    total=False,
)

ExportTasksMessageTypeDef = TypedDict(
    "ExportTasksMessageTypeDef",
    {
        "Marker": str,
        "ExportTasks": List["ExportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFailoverDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredFailoverDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalFailoverDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalFailoverDBClusterMessageRequestTypeDef",
    {
        "TargetDBInstanceIdentifier": str,
    },
    total=False,
)

class FailoverDBClusterMessageRequestTypeDef(
    _RequiredFailoverDBClusterMessageRequestTypeDef, _OptionalFailoverDBClusterMessageRequestTypeDef
):
    pass

FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFailoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "_RequiredFailoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
    },
)
_OptionalFailoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "_OptionalFailoverGlobalClusterMessageRequestTypeDef",
    {
        "AllowDataLoss": bool,
        "Switchover": bool,
    },
    total=False,
)

class FailoverGlobalClusterMessageRequestTypeDef(
    _RequiredFailoverGlobalClusterMessageRequestTypeDef,
    _OptionalFailoverGlobalClusterMessageRequestTypeDef,
):
    pass

FailoverGlobalClusterResultTypeDef = TypedDict(
    "FailoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverStateTypeDef = TypedDict(
    "FailoverStateTypeDef",
    {
        "Status": FailoverStatusType,
        "FromDbClusterArn": str,
        "ToDbClusterArn": str,
        "IsDataLossAllowed": bool,
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

GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {
        "DBClusterArn": str,
        "Readers": List[str],
        "IsWriter": bool,
        "GlobalWriteForwardingStatus": WriteForwardingStatusType,
        "SynchronizationStatus": GlobalClusterMemberSynchronizationStatusType,
    },
    total=False,
)

GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineLifecycleSupport": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List["GlobalClusterMemberTypeDef"],
        "FailoverState": "FailoverStateTypeDef",
    },
    total=False,
)

GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List["GlobalClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
    },
    total=False,
)

_RequiredIntegrationErrorTypeDef = TypedDict(
    "_RequiredIntegrationErrorTypeDef",
    {
        "ErrorCode": str,
    },
)
_OptionalIntegrationErrorTypeDef = TypedDict(
    "_OptionalIntegrationErrorTypeDef",
    {
        "ErrorMessage": str,
    },
    total=False,
)

class IntegrationErrorTypeDef(_RequiredIntegrationErrorTypeDef, _OptionalIntegrationErrorTypeDef):
    pass

IntegrationResponseMetadataTypeDef = TypedDict(
    "IntegrationResponseMetadataTypeDef",
    {
        "SourceArn": str,
        "TargetArn": str,
        "IntegrationName": str,
        "IntegrationArn": str,
        "KMSKeyId": str,
        "AdditionalEncryptionContext": Dict[str, str],
        "Status": IntegrationStatusType,
        "Tags": List["TagTypeDef"],
        "CreateTime": datetime,
        "Errors": List["IntegrationErrorTypeDef"],
        "DataFilter": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "SourceArn": str,
        "TargetArn": str,
        "IntegrationName": str,
        "IntegrationArn": str,
        "KMSKeyId": str,
        "AdditionalEncryptionContext": Dict[str, str],
        "Status": IntegrationStatusType,
        "Tags": List["TagTypeDef"],
        "CreateTime": datetime,
        "Errors": List["IntegrationErrorTypeDef"],
        "DataFilter": str,
        "Description": str,
    },
    total=False,
)

IssueDetailsTypeDef = TypedDict(
    "IssueDetailsTypeDef",
    {
        "PerformanceIssueDetails": "PerformanceIssueDetailsTypeDef",
    },
    total=False,
)

LimitlessDatabaseTypeDef = TypedDict(
    "LimitlessDatabaseTypeDef",
    {
        "Status": LimitlessDatabaseStatusType,
        "MinRequiredACU": float,
    },
    total=False,
)

_RequiredListTagsForResourceMessageRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
    },
)
_OptionalListTagsForResourceMessageRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListTagsForResourceMessageRequestTypeDef(
    _RequiredListTagsForResourceMessageRequestTypeDef,
    _OptionalListTagsForResourceMessageRequestTypeDef,
):
    pass

MasterUserSecretTypeDef = TypedDict(
    "MasterUserSecretTypeDef",
    {
        "SecretArn": str,
        "SecretStatus": str,
        "KmsKeyId": str,
    },
    total=False,
)

MetricQueryTypeDef = TypedDict(
    "MetricQueryTypeDef",
    {
        "PerformanceInsightsMetricQuery": "PerformanceInsightsMetricQueryTypeDef",
    },
    total=False,
)

MetricReferenceTypeDef = TypedDict(
    "MetricReferenceTypeDef",
    {
        "Name": str,
        "ReferenceDetails": "ReferenceDetailsTypeDef",
    },
    total=False,
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Name": str,
        "References": List["MetricReferenceTypeDef"],
        "StatisticsDetails": str,
        "MetricQuery": "MetricQueryTypeDef",
    },
    total=False,
)

MinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "MinimumEngineVersionPerAllowedValueTypeDef",
    {
        "AllowedValue": str,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ModifyActivityStreamRequestRequestTypeDef = TypedDict(
    "ModifyActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "AuditPolicyState": AuditPolicyStateType,
    },
    total=False,
)

ModifyActivityStreamResponseTypeDef = TypedDict(
    "ModifyActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "EngineNativeAuditFieldsIncluded": bool,
        "PolicyStatus": ActivityStreamPolicyStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCertificatesMessageRequestTypeDef = TypedDict(
    "ModifyCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
        "RemoveCustomerOverride": bool,
    },
    total=False,
)

ModifyCertificatesResultTypeDef = TypedDict(
    "ModifyCertificatesResultTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyCurrentDBClusterCapacityMessageRequestTypeDef = TypedDict(
    "_RequiredModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalModifyCurrentDBClusterCapacityMessageRequestTypeDef = TypedDict(
    "_OptionalModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    {
        "Capacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
    },
    total=False,
)

class ModifyCurrentDBClusterCapacityMessageRequestTypeDef(
    _RequiredModifyCurrentDBClusterCapacityMessageRequestTypeDef,
    _OptionalModifyCurrentDBClusterCapacityMessageRequestTypeDef,
):
    pass

_RequiredModifyCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "_RequiredModifyCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
    },
)
_OptionalModifyCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "_OptionalModifyCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Description": str,
        "Status": CustomEngineVersionStatusType,
    },
    total=False,
)

class ModifyCustomDBEngineVersionMessageRequestTypeDef(
    _RequiredModifyCustomDBEngineVersionMessageRequestTypeDef,
    _OptionalModifyCustomDBEngineVersionMessageRequestTypeDef,
):
    pass

_RequiredModifyDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)
_OptionalModifyDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBClusterEndpointMessageRequestTypeDef",
    {
        "EndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
    },
    total=False,
)

class ModifyDBClusterEndpointMessageRequestTypeDef(
    _RequiredModifyDBClusterEndpointMessageRequestTypeDef,
    _OptionalModifyDBClusterEndpointMessageRequestTypeDef,
):
    pass

_RequiredModifyDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalModifyDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBClusterMessageRequestTypeDef",
    {
        "NewDBClusterIdentifier": str,
        "ApplyImmediately": bool,
        "BackupRetentionPeriod": int,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Port": int,
        "MasterUserPassword": str,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "EnableIAMDatabaseAuthentication": bool,
        "BacktrackWindow": int,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "DBInstanceParameterGroupName": str,
        "Domain": str,
        "DomainIAMRoleName": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "DeletionProtection": bool,
        "EnableHttpEndpoint": bool,
        "CopyTagsToSnapshot": bool,
        "EnableGlobalWriteForwarding": bool,
        "DBClusterInstanceClass": str,
        "AllocatedStorage": int,
        "StorageType": str,
        "Iops": int,
        "AutoMinorVersionUpgrade": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "ServerlessV2ScalingConfiguration": "ServerlessV2ScalingConfigurationTypeDef",
        "NetworkType": str,
        "ManageMasterUserPassword": bool,
        "RotateMasterUserPassword": bool,
        "MasterUserSecretKmsKeyId": str,
        "EngineMode": str,
        "AllowEngineModeChange": bool,
        "EnableLocalWriteForwarding": bool,
        "AwsBackupRecoveryPointArn": str,
        "EnableLimitlessDatabase": bool,
        "CACertificateIdentifier": str,
    },
    total=False,
)

class ModifyDBClusterMessageRequestTypeDef(
    _RequiredModifyDBClusterMessageRequestTypeDef, _OptionalModifyDBClusterMessageRequestTypeDef
):
    pass

ModifyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "AttributeName": str,
    },
)
_OptionalModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "ValuesToAdd": List[str],
        "ValuesToRemove": List[str],
    },
    total=False,
)

class ModifyDBClusterSnapshotAttributeMessageRequestTypeDef(
    _RequiredModifyDBClusterSnapshotAttributeMessageRequestTypeDef,
    _OptionalModifyDBClusterSnapshotAttributeMessageRequestTypeDef,
):
    pass

ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBInstanceMessageRequestTypeDef",
    {
        "AllocatedStorage": int,
        "DBInstanceClass": str,
        "DBSubnetGroupName": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "ApplyImmediately": bool,
        "MasterUserPassword": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "NewDBInstanceIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "CACertificateIdentifier": str,
        "Domain": str,
        "DomainFqdn": str,
        "DomainOu": str,
        "DomainAuthSecretArn": str,
        "DomainDnsIps": List[str],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "DBPortNumber": int,
        "PubliclyAccessible": bool,
        "MonitoringRoleArn": str,
        "DomainIAMRoleName": str,
        "DisableDomain": bool,
        "PromotionTier": int,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DeletionProtection": bool,
        "MaxAllocatedStorage": int,
        "CertificateRotationRestart": bool,
        "ReplicaMode": ReplicaModeType,
        "EnableCustomerOwnedIp": bool,
        "AwsBackupRecoveryPointArn": str,
        "AutomationMode": AutomationModeType,
        "ResumeFullAutomationModeMinutes": int,
        "NetworkType": str,
        "StorageThroughput": int,
        "ManageMasterUserPassword": bool,
        "RotateMasterUserPassword": bool,
        "MasterUserSecretKmsKeyId": str,
        "Engine": str,
        "DedicatedLogVolume": bool,
        "MultiTenant": bool,
    },
    total=False,
)

class ModifyDBInstanceMessageRequestTypeDef(
    _RequiredModifyDBInstanceMessageRequestTypeDef, _OptionalModifyDBInstanceMessageRequestTypeDef
):
    pass

ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

_RequiredModifyDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredModifyDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyEndpointName": str,
    },
)
_OptionalModifyDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalModifyDBProxyEndpointRequestRequestTypeDef",
    {
        "NewDBProxyEndpointName": str,
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)

class ModifyDBProxyEndpointRequestRequestTypeDef(
    _RequiredModifyDBProxyEndpointRequestRequestTypeDef,
    _OptionalModifyDBProxyEndpointRequestRequestTypeDef,
):
    pass

ModifyDBProxyEndpointResponseTypeDef = TypedDict(
    "ModifyDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBProxyRequestRequestTypeDef = TypedDict(
    "_RequiredModifyDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalModifyDBProxyRequestRequestTypeDef = TypedDict(
    "_OptionalModifyDBProxyRequestRequestTypeDef",
    {
        "NewDBProxyName": str,
        "Auth": List["UserAuthConfigTypeDef"],
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "RoleArn": str,
        "SecurityGroups": List[str],
    },
    total=False,
)

class ModifyDBProxyRequestRequestTypeDef(
    _RequiredModifyDBProxyRequestRequestTypeDef, _OptionalModifyDBProxyRequestRequestTypeDef
):
    pass

ModifyDBProxyResponseTypeDef = TypedDict(
    "ModifyDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBProxyTargetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredModifyDBProxyTargetGroupRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBProxyName": str,
    },
)
_OptionalModifyDBProxyTargetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalModifyDBProxyTargetGroupRequestRequestTypeDef",
    {
        "ConnectionPoolConfig": "ConnectionPoolConfigurationTypeDef",
        "NewName": str,
    },
    total=False,
)

class ModifyDBProxyTargetGroupRequestRequestTypeDef(
    _RequiredModifyDBProxyTargetGroupRequestRequestTypeDef,
    _OptionalModifyDBProxyTargetGroupRequestRequestTypeDef,
):
    pass

ModifyDBProxyTargetGroupResponseTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupResponseTypeDef",
    {
        "DBProxyTargetGroup": "DBProxyTargetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBRecommendationMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBRecommendationMessageRequestTypeDef",
    {
        "RecommendationId": str,
    },
)
_OptionalModifyDBRecommendationMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBRecommendationMessageRequestTypeDef",
    {
        "Locale": str,
        "Status": str,
        "RecommendedActionUpdates": List["RecommendedActionUpdateTypeDef"],
    },
    total=False,
)

class ModifyDBRecommendationMessageRequestTypeDef(
    _RequiredModifyDBRecommendationMessageRequestTypeDef,
    _OptionalModifyDBRecommendationMessageRequestTypeDef,
):
    pass

_RequiredModifyDBShardGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBShardGroupMessageRequestTypeDef",
    {
        "DBShardGroupIdentifier": str,
    },
)
_OptionalModifyDBShardGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBShardGroupMessageRequestTypeDef",
    {
        "MaxACU": float,
    },
    total=False,
)

class ModifyDBShardGroupMessageRequestTypeDef(
    _RequiredModifyDBShardGroupMessageRequestTypeDef,
    _OptionalModifyDBShardGroupMessageRequestTypeDef,
):
    pass

_RequiredModifyDBSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBSnapshotAttributeMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "AttributeName": str,
    },
)
_OptionalModifyDBSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBSnapshotAttributeMessageRequestTypeDef",
    {
        "ValuesToAdd": List[str],
        "ValuesToRemove": List[str],
    },
    total=False,
)

class ModifyDBSnapshotAttributeMessageRequestTypeDef(
    _RequiredModifyDBSnapshotAttributeMessageRequestTypeDef,
    _OptionalModifyDBSnapshotAttributeMessageRequestTypeDef,
):
    pass

ModifyDBSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeResultTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)
_OptionalModifyDBSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBSnapshotMessageRequestTypeDef",
    {
        "EngineVersion": str,
        "OptionGroupName": str,
    },
    total=False,
)

class ModifyDBSnapshotMessageRequestTypeDef(
    _RequiredModifyDBSnapshotMessageRequestTypeDef, _OptionalModifyDBSnapshotMessageRequestTypeDef
):
    pass

ModifyDBSnapshotResultTypeDef = TypedDict(
    "ModifyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupDescription": str,
    },
    total=False,
)

class ModifyDBSubnetGroupMessageRequestTypeDef(
    _RequiredModifyDBSubnetGroupMessageRequestTypeDef,
    _OptionalModifyDBSubnetGroupMessageRequestTypeDef,
):
    pass

ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
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

ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyGlobalClusterMessageRequestTypeDef = TypedDict(
    "ModifyGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "NewGlobalClusterIdentifier": str,
        "DeletionProtection": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
    },
    total=False,
)

ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyIntegrationMessageRequestTypeDef = TypedDict(
    "_RequiredModifyIntegrationMessageRequestTypeDef",
    {
        "IntegrationIdentifier": str,
    },
)
_OptionalModifyIntegrationMessageRequestTypeDef = TypedDict(
    "_OptionalModifyIntegrationMessageRequestTypeDef",
    {
        "IntegrationName": str,
        "DataFilter": str,
        "Description": str,
    },
    total=False,
)

class ModifyIntegrationMessageRequestTypeDef(
    _RequiredModifyIntegrationMessageRequestTypeDef, _OptionalModifyIntegrationMessageRequestTypeDef
):
    pass

_RequiredModifyOptionGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
    },
)
_OptionalModifyOptionGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyOptionGroupMessageRequestTypeDef",
    {
        "OptionsToInclude": List["OptionConfigurationTypeDef"],
        "OptionsToRemove": List[str],
        "ApplyImmediately": bool,
    },
    total=False,
)

class ModifyOptionGroupMessageRequestTypeDef(
    _RequiredModifyOptionGroupMessageRequestTypeDef, _OptionalModifyOptionGroupMessageRequestTypeDef
):
    pass

ModifyOptionGroupResultTypeDef = TypedDict(
    "ModifyOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTenantDatabaseMessageRequestTypeDef = TypedDict(
    "_RequiredModifyTenantDatabaseMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
    },
)
_OptionalModifyTenantDatabaseMessageRequestTypeDef = TypedDict(
    "_OptionalModifyTenantDatabaseMessageRequestTypeDef",
    {
        "MasterUserPassword": str,
        "NewTenantDBName": str,
    },
    total=False,
)

class ModifyTenantDatabaseMessageRequestTypeDef(
    _RequiredModifyTenantDatabaseMessageRequestTypeDef,
    _OptionalModifyTenantDatabaseMessageRequestTypeDef,
):
    pass

ModifyTenantDatabaseResultTypeDef = TypedDict(
    "ModifyTenantDatabaseResultTypeDef",
    {
        "TenantDatabase": "TenantDatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOptionConfigurationTypeDef = TypedDict(
    "_RequiredOptionConfigurationTypeDef",
    {
        "OptionName": str,
    },
)
_OptionalOptionConfigurationTypeDef = TypedDict(
    "_OptionalOptionConfigurationTypeDef",
    {
        "Port": int,
        "OptionVersion": str,
        "DBSecurityGroupMemberships": List[str],
        "VpcSecurityGroupMemberships": List[str],
        "OptionSettings": List["OptionSettingTypeDef"],
    },
    total=False,
)

class OptionConfigurationTypeDef(
    _RequiredOptionConfigurationTypeDef, _OptionalOptionConfigurationTypeDef
):
    pass

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
    total=False,
)

OptionGroupOptionSettingTypeDef = TypedDict(
    "OptionGroupOptionSettingTypeDef",
    {
        "SettingName": str,
        "SettingDescription": str,
        "DefaultValue": str,
        "ApplyType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsRequired": bool,
        "MinimumEngineVersionPerAllowedValue": List["MinimumEngineVersionPerAllowedValueTypeDef"],
    },
    total=False,
)

OptionGroupOptionTypeDef = TypedDict(
    "OptionGroupOptionTypeDef",
    {
        "Name": str,
        "Description": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "MinimumRequiredMinorEngineVersion": str,
        "PortRequired": bool,
        "DefaultPort": int,
        "OptionsDependedOn": List[str],
        "OptionsConflictsWith": List[str],
        "Persistent": bool,
        "Permanent": bool,
        "RequiresAutoMinorEngineVersionUpgrade": bool,
        "VpcOnly": bool,
        "SupportsOptionVersionDowngrade": bool,
        "OptionGroupOptionSettings": List["OptionGroupOptionSettingTypeDef"],
        "OptionGroupOptionVersions": List["OptionVersionTypeDef"],
        "CopyableCrossAccount": bool,
    },
    total=False,
)

OptionGroupOptionsMessageTypeDef = TypedDict(
    "OptionGroupOptionsMessageTypeDef",
    {
        "OptionGroupOptions": List["OptionGroupOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionGroupTypeDef = TypedDict(
    "OptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List["OptionTypeDef"],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
        "SourceOptionGroup": str,
        "SourceAccountId": str,
        "CopyTimestamp": datetime,
    },
    total=False,
)

OptionGroupsTypeDef = TypedDict(
    "OptionGroupsTypeDef",
    {
        "OptionGroupsList": List["OptionGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionSettingTypeDef = TypedDict(
    "OptionSettingTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

OptionTypeDef = TypedDict(
    "OptionTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List["OptionSettingTypeDef"],
        "DBSecurityGroupMemberships": List["DBSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroupMemberships": List["VpcSecurityGroupMembershipTypeDef"],
    },
    total=False,
)

OptionVersionTypeDef = TypedDict(
    "OptionVersionTypeDef",
    {
        "Version": str,
        "IsDefault": bool,
    },
    total=False,
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZoneGroup": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
        "AvailableProcessorFeatures": List["AvailableProcessorFeatureTypeDef"],
        "SupportedEngineModes": List[str],
        "SupportsStorageAutoscaling": bool,
        "SupportsKerberosAuthentication": bool,
        "OutpostCapable": bool,
        "SupportedActivityStreamModes": List[str],
        "SupportsGlobalDatabases": bool,
        "SupportsClusters": bool,
        "SupportedNetworkTypes": List[str],
        "SupportsStorageThroughput": bool,
        "MinStorageThroughputPerDbInstance": int,
        "MaxStorageThroughputPerDbInstance": int,
        "MinStorageThroughputPerIops": float,
        "MaxStorageThroughputPerIops": float,
        "SupportsDedicatedLogVolume": bool,
    },
    total=False,
)

OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {
        "OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "Arn": str,
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

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": ApplyMethodType,
        "SupportedEngineModes": List[str],
    },
    total=False,
)

PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": List[str],
        "LogTypesToDisable": List[str],
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

PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": "PendingCloudwatchLogsExportsTypeDef",
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "IAMDatabaseAuthenticationEnabled": bool,
        "AutomationMode": AutomationModeType,
        "ResumeFullAutomationModeTime": datetime,
        "StorageThroughput": int,
        "Engine": str,
        "DedicatedLogVolume": bool,
        "MultiTenant": bool,
    },
    total=False,
)

PerformanceInsightsMetricDimensionGroupTypeDef = TypedDict(
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    {
        "Dimensions": List[str],
        "Group": str,
        "Limit": int,
    },
    total=False,
)

PerformanceInsightsMetricQueryTypeDef = TypedDict(
    "PerformanceInsightsMetricQueryTypeDef",
    {
        "GroupBy": "PerformanceInsightsMetricDimensionGroupTypeDef",
        "Metric": str,
    },
    total=False,
)

PerformanceIssueDetailsTypeDef = TypedDict(
    "PerformanceIssueDetailsTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Metrics": List["MetricTypeDef"],
        "Analysis": str,
    },
    total=False,
)

ProcessorFeatureTypeDef = TypedDict(
    "ProcessorFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

PromoteReadReplicaDBClusterMessageRequestTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

PromoteReadReplicaDBClusterResultTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPromoteReadReplicaMessageRequestTypeDef = TypedDict(
    "_RequiredPromoteReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalPromoteReadReplicaMessageRequestTypeDef = TypedDict(
    "_OptionalPromoteReadReplicaMessageRequestTypeDef",
    {
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
    },
    total=False,
)

class PromoteReadReplicaMessageRequestTypeDef(
    _RequiredPromoteReadReplicaMessageRequestTypeDef,
    _OptionalPromoteReadReplicaMessageRequestTypeDef,
):
    pass

PromoteReadReplicaResultTypeDef = TypedDict(
    "PromoteReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPurchaseReservedDBInstancesOfferingMessageRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
    },
)
_OptionalPurchaseReservedDBInstancesOfferingMessageRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    {
        "ReservedDBInstanceId": str,
        "DBInstanceCount": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PurchaseReservedDBInstancesOfferingMessageRequestTypeDef(
    _RequiredPurchaseReservedDBInstancesOfferingMessageRequestTypeDef,
    _OptionalPurchaseReservedDBInstancesOfferingMessageRequestTypeDef,
):
    pass

PurchaseReservedDBInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    {
        "ReservedDBInstance": "ReservedDBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "From": int,
        "To": int,
        "Step": int,
    },
    total=False,
)

RdsCustomClusterConfigurationTypeDef = TypedDict(
    "RdsCustomClusterConfigurationTypeDef",
    {
        "InterconnectSubnetId": str,
        "TransitGatewayMulticastDomainId": str,
        "ReplicaMode": ReplicaModeType,
    },
    total=False,
)

RebootDBClusterMessageRequestTypeDef = TypedDict(
    "RebootDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

RebootDBClusterResultTypeDef = TypedDict(
    "RebootDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRebootDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredRebootDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalRebootDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalRebootDBInstanceMessageRequestTypeDef",
    {
        "ForceFailover": bool,
    },
    total=False,
)

class RebootDBInstanceMessageRequestTypeDef(
    _RequiredRebootDBInstanceMessageRequestTypeDef, _OptionalRebootDBInstanceMessageRequestTypeDef
):
    pass

RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootDBShardGroupMessageRequestTypeDef = TypedDict(
    "RebootDBShardGroupMessageRequestTypeDef",
    {
        "DBShardGroupIdentifier": str,
    },
)

RecommendedActionParameterTypeDef = TypedDict(
    "RecommendedActionParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

RecommendedActionTypeDef = TypedDict(
    "RecommendedActionTypeDef",
    {
        "ActionId": str,
        "Title": str,
        "Description": str,
        "Operation": str,
        "Parameters": List["RecommendedActionParameterTypeDef"],
        "ApplyModes": List[str],
        "Status": str,
        "IssueDetails": "IssueDetailsTypeDef",
        "ContextAttributes": List["ContextAttributeTypeDef"],
    },
    total=False,
)

RecommendedActionUpdateTypeDef = TypedDict(
    "RecommendedActionUpdateTypeDef",
    {
        "ActionId": str,
        "Status": str,
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": float,
        "RecurringChargeFrequency": str,
    },
    total=False,
)

ReferenceDetailsTypeDef = TypedDict(
    "ReferenceDetailsTypeDef",
    {
        "ScalarReferenceDetails": "ScalarReferenceDetailsTypeDef",
    },
    total=False,
)

_RequiredRegisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalRegisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterDBProxyTargetsRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBInstanceIdentifiers": List[str],
        "DBClusterIdentifiers": List[str],
    },
    total=False,
)

class RegisterDBProxyTargetsRequestRequestTypeDef(
    _RequiredRegisterDBProxyTargetsRequestRequestTypeDef,
    _OptionalRegisterDBProxyTargetsRequestRequestTypeDef,
):
    pass

RegisterDBProxyTargetsResponseTypeDef = TypedDict(
    "RegisterDBProxyTargetsResponseTypeDef",
    {
        "DBProxyTargets": List["DBProxyTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFromGlobalClusterMessageRequestTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "DbClusterIdentifier": str,
    },
    total=False,
)

RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveRoleFromDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredRemoveRoleFromDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
    },
)
_OptionalRemoveRoleFromDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalRemoveRoleFromDBClusterMessageRequestTypeDef",
    {
        "FeatureName": str,
    },
    total=False,
)

class RemoveRoleFromDBClusterMessageRequestTypeDef(
    _RequiredRemoveRoleFromDBClusterMessageRequestTypeDef,
    _OptionalRemoveRoleFromDBClusterMessageRequestTypeDef,
):
    pass

RemoveRoleFromDBInstanceMessageRequestTypeDef = TypedDict(
    "RemoveRoleFromDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
    },
)

RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

ReservedDBInstanceMessageTypeDef = TypedDict(
    "ReservedDBInstanceMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List["ReservedDBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedDBInstanceTypeDef = TypedDict(
    "ReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)

ReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "ReservedDBInstancesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List["ReservedDBInstancesOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedDBInstancesOfferingTypeDef = TypedDict(
    "ReservedDBInstancesOfferingTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

_RequiredResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
_OptionalResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

class ResetDBClusterParameterGroupMessageRequestTypeDef(
    _RequiredResetDBClusterParameterGroupMessageRequestTypeDef,
    _OptionalResetDBClusterParameterGroupMessageRequestTypeDef,
):
    pass

_RequiredResetDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredResetDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
_OptionalResetDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalResetDBParameterGroupMessageRequestTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

class ResetDBParameterGroupMessageRequestTypeDef(
    _RequiredResetDBParameterGroupMessageRequestTypeDef,
    _OptionalResetDBParameterGroupMessageRequestTypeDef,
):
    pass

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

_RequiredRestoreDBClusterFromS3MessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBClusterFromS3MessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "MasterUsername": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
    },
)
_OptionalRestoreDBClusterFromS3MessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBClusterFromS3MessageRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUserPassword": str,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "S3Prefix": str,
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "ServerlessV2ScalingConfiguration": "ServerlessV2ScalingConfigurationTypeDef",
        "NetworkType": str,
        "ManageMasterUserPassword": bool,
        "MasterUserSecretKmsKeyId": str,
        "StorageType": str,
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class RestoreDBClusterFromS3MessageRequestTypeDef(
    _RequiredRestoreDBClusterFromS3MessageRequestTypeDef,
    _OptionalRestoreDBClusterFromS3MessageRequestTypeDef,
):
    pass

RestoreDBClusterFromS3ResultTypeDef = TypedDict(
    "RestoreDBClusterFromS3ResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "Engine": str,
    },
)
_OptionalRestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "EngineVersion": str,
        "Port": int,
        "DBSubnetGroupName": str,
        "DatabaseName": str,
        "OptionGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "EngineMode": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "DBClusterInstanceClass": str,
        "StorageType": str,
        "Iops": int,
        "PubliclyAccessible": bool,
        "ServerlessV2ScalingConfiguration": "ServerlessV2ScalingConfigurationTypeDef",
        "NetworkType": str,
        "RdsCustomClusterConfiguration": "RdsCustomClusterConfigurationTypeDef",
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class RestoreDBClusterFromSnapshotMessageRequestTypeDef(
    _RequiredRestoreDBClusterFromSnapshotMessageRequestTypeDef,
    _OptionalRestoreDBClusterFromSnapshotMessageRequestTypeDef,
):
    pass

RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalRestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "RestoreType": str,
        "SourceDBClusterIdentifier": str,
        "RestoreToTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "Port": int,
        "DBSubnetGroupName": str,
        "OptionGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "EngineMode": str,
        "DBClusterInstanceClass": str,
        "StorageType": str,
        "PubliclyAccessible": bool,
        "Iops": int,
        "ServerlessV2ScalingConfiguration": "ServerlessV2ScalingConfigurationTypeDef",
        "NetworkType": str,
        "SourceDbClusterResourceId": str,
        "RdsCustomClusterConfiguration": "RdsCustomClusterConfigurationTypeDef",
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class RestoreDBClusterToPointInTimeMessageRequestTypeDef(
    _RequiredRestoreDBClusterToPointInTimeMessageRequestTypeDef,
    _OptionalRestoreDBClusterToPointInTimeMessageRequestTypeDef,
):
    pass

RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBInstanceFromDBSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalRestoreDBInstanceFromDBSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceClass": str,
        "Port": int,
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "MultiAZ": bool,
        "PubliclyAccessible": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "DBName": str,
        "Engine": str,
        "Iops": int,
        "OptionGroupName": str,
        "Tags": List["TagTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "VpcSecurityGroupIds": List[str],
        "Domain": str,
        "DomainFqdn": str,
        "DomainOu": str,
        "DomainAuthSecretArn": str,
        "DomainDnsIps": List[str],
        "CopyTagsToSnapshot": bool,
        "DomainIAMRoleName": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DBParameterGroupName": str,
        "DeletionProtection": bool,
        "EnableCustomerOwnedIp": bool,
        "CustomIamInstanceProfile": str,
        "BackupTarget": str,
        "NetworkType": str,
        "StorageThroughput": int,
        "DBClusterSnapshotIdentifier": str,
        "AllocatedStorage": int,
        "DedicatedLogVolume": bool,
        "CACertificateIdentifier": str,
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef(
    _RequiredRestoreDBInstanceFromDBSnapshotMessageRequestTypeDef,
    _OptionalRestoreDBInstanceFromDBSnapshotMessageRequestTypeDef,
):
    pass

RestoreDBInstanceFromDBSnapshotResultTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBInstanceFromS3MessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBInstanceFromS3MessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
    },
)
_OptionalRestoreDBInstanceFromS3MessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBInstanceFromS3MessageRequestTypeDef",
    {
        "DBName": str,
        "AllocatedStorage": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "PreferredMaintenanceWindow": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "Port": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "StorageType": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "EnableIAMDatabaseAuthentication": bool,
        "S3Prefix": str,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DeletionProtection": bool,
        "MaxAllocatedStorage": int,
        "NetworkType": str,
        "StorageThroughput": int,
        "ManageMasterUserPassword": bool,
        "MasterUserSecretKmsKeyId": str,
        "DedicatedLogVolume": bool,
        "CACertificateIdentifier": str,
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class RestoreDBInstanceFromS3MessageRequestTypeDef(
    _RequiredRestoreDBInstanceFromS3MessageRequestTypeDef,
    _OptionalRestoreDBInstanceFromS3MessageRequestTypeDef,
):
    pass

RestoreDBInstanceFromS3ResultTypeDef = TypedDict(
    "RestoreDBInstanceFromS3ResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBInstanceToPointInTimeMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    {
        "TargetDBInstanceIdentifier": str,
    },
)
_OptionalRestoreDBInstanceToPointInTimeMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    {
        "SourceDBInstanceIdentifier": str,
        "RestoreTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "DBInstanceClass": str,
        "Port": int,
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "MultiAZ": bool,
        "PubliclyAccessible": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "DBName": str,
        "Engine": str,
        "Iops": int,
        "OptionGroupName": str,
        "CopyTagsToSnapshot": bool,
        "Tags": List["TagTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "VpcSecurityGroupIds": List[str],
        "Domain": str,
        "DomainIAMRoleName": str,
        "DomainFqdn": str,
        "DomainOu": str,
        "DomainAuthSecretArn": str,
        "DomainDnsIps": List[str],
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DBParameterGroupName": str,
        "DeletionProtection": bool,
        "SourceDbiResourceId": str,
        "MaxAllocatedStorage": int,
        "SourceDBInstanceAutomatedBackupsArn": str,
        "EnableCustomerOwnedIp": bool,
        "CustomIamInstanceProfile": str,
        "BackupTarget": str,
        "NetworkType": str,
        "StorageThroughput": int,
        "AllocatedStorage": int,
        "DedicatedLogVolume": bool,
        "CACertificateIdentifier": str,
        "EngineLifecycleSupport": str,
    },
    total=False,
)

class RestoreDBInstanceToPointInTimeMessageRequestTypeDef(
    _RequiredRestoreDBInstanceToPointInTimeMessageRequestTypeDef,
    _OptionalRestoreDBInstanceToPointInTimeMessageRequestTypeDef,
):
    pass

RestoreDBInstanceToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreWindowTypeDef = TypedDict(
    "RestoreWindowTypeDef",
    {
        "EarliestTime": datetime,
        "LatestTime": datetime,
    },
    total=False,
)

_RequiredRevokeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_RequiredRevokeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)
_OptionalRevokeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_OptionalRevokeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

class RevokeDBSecurityGroupIngressMessageRequestTypeDef(
    _RequiredRevokeDBSecurityGroupIngressMessageRequestTypeDef,
    _OptionalRevokeDBSecurityGroupIngressMessageRequestTypeDef,
):
    pass

RevokeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScalarReferenceDetailsTypeDef = TypedDict(
    "ScalarReferenceDetailsTypeDef",
    {
        "Value": float,
    },
    total=False,
)

ScalingConfigurationInfoTypeDef = TypedDict(
    "ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
        "SecondsBeforeTimeout": int,
    },
    total=False,
)

ScalingConfigurationTypeDef = TypedDict(
    "ScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
        "SecondsBeforeTimeout": int,
    },
    total=False,
)

ServerlessV2ScalingConfigurationInfoTypeDef = TypedDict(
    "ServerlessV2ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": float,
        "MaxCapacity": float,
    },
    total=False,
)

ServerlessV2ScalingConfigurationTypeDef = TypedDict(
    "ServerlessV2ScalingConfigurationTypeDef",
    {
        "MinCapacity": float,
        "MaxCapacity": float,
    },
    total=False,
)

SourceRegionMessageTypeDef = TypedDict(
    "SourceRegionMessageTypeDef",
    {
        "Marker": str,
        "SourceRegions": List["SourceRegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceRegionTypeDef = TypedDict(
    "SourceRegionTypeDef",
    {
        "RegionName": str,
        "Endpoint": str,
        "Status": str,
        "SupportsDBInstanceAutomatedBackupsReplication": bool,
    },
    total=False,
)

_RequiredStartActivityStreamRequestRequestTypeDef = TypedDict(
    "_RequiredStartActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Mode": ActivityStreamModeType,
        "KmsKeyId": str,
    },
)
_OptionalStartActivityStreamRequestRequestTypeDef = TypedDict(
    "_OptionalStartActivityStreamRequestRequestTypeDef",
    {
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
    },
    total=False,
)

class StartActivityStreamRequestRequestTypeDef(
    _RequiredStartActivityStreamRequestRequestTypeDef,
    _OptionalStartActivityStreamRequestRequestTypeDef,
):
    pass

StartActivityStreamResponseTypeDef = TypedDict(
    "StartActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBClusterMessageRequestTypeDef = TypedDict(
    "StartDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "_RequiredStartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "SourceDBInstanceArn": str,
    },
)
_OptionalStartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "_OptionalStartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "BackupRetentionPeriod": int,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "SourceRegion": str,
    },
    total=False,
)

class StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef(
    _RequiredStartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef,
    _OptionalStartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef,
):
    pass

StartDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBInstanceMessageRequestTypeDef = TypedDict(
    "StartDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

StartDBInstanceResultTypeDef = TypedDict(
    "StartDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartExportTaskMessageRequestTypeDef = TypedDict(
    "_RequiredStartExportTaskMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "S3BucketName": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
    },
)
_OptionalStartExportTaskMessageRequestTypeDef = TypedDict(
    "_OptionalStartExportTaskMessageRequestTypeDef",
    {
        "S3Prefix": str,
        "ExportOnly": List[str],
    },
    total=False,
)

class StartExportTaskMessageRequestTypeDef(
    _RequiredStartExportTaskMessageRequestTypeDef, _OptionalStartExportTaskMessageRequestTypeDef
):
    pass

_RequiredStopActivityStreamRequestRequestTypeDef = TypedDict(
    "_RequiredStopActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalStopActivityStreamRequestRequestTypeDef = TypedDict(
    "_OptionalStopActivityStreamRequestRequestTypeDef",
    {
        "ApplyImmediately": bool,
    },
    total=False,
)

class StopActivityStreamRequestRequestTypeDef(
    _RequiredStopActivityStreamRequestRequestTypeDef,
    _OptionalStopActivityStreamRequestRequestTypeDef,
):
    pass

StopActivityStreamResponseTypeDef = TypedDict(
    "StopActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDBClusterMessageRequestTypeDef = TypedDict(
    "StopDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "SourceDBInstanceArn": str,
    },
)

StopDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredStopDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalStopDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalStopDBInstanceMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
    total=False,
)

class StopDBInstanceMessageRequestTypeDef(
    _RequiredStopDBInstanceMessageRequestTypeDef, _OptionalStopDBInstanceMessageRequestTypeDef
):
    pass

StopDBInstanceResultTypeDef = TypedDict(
    "StopDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetOutpost": "OutpostTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

_RequiredSwitchoverBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredSwitchoverBlueGreenDeploymentRequestRequestTypeDef",
    {
        "BlueGreenDeploymentIdentifier": str,
    },
)
_OptionalSwitchoverBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalSwitchoverBlueGreenDeploymentRequestRequestTypeDef",
    {
        "SwitchoverTimeout": int,
    },
    total=False,
)

class SwitchoverBlueGreenDeploymentRequestRequestTypeDef(
    _RequiredSwitchoverBlueGreenDeploymentRequestRequestTypeDef,
    _OptionalSwitchoverBlueGreenDeploymentRequestRequestTypeDef,
):
    pass

SwitchoverBlueGreenDeploymentResponseTypeDef = TypedDict(
    "SwitchoverBlueGreenDeploymentResponseTypeDef",
    {
        "BlueGreenDeployment": "BlueGreenDeploymentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SwitchoverDetailTypeDef = TypedDict(
    "SwitchoverDetailTypeDef",
    {
        "SourceMember": str,
        "TargetMember": str,
        "Status": str,
    },
    total=False,
)

SwitchoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "SwitchoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
    },
)

SwitchoverGlobalClusterResultTypeDef = TypedDict(
    "SwitchoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SwitchoverReadReplicaMessageRequestTypeDef = TypedDict(
    "SwitchoverReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

SwitchoverReadReplicaResultTypeDef = TypedDict(
    "SwitchoverReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": TargetStateType,
        "Reason": TargetHealthReasonType,
        "Description": str,
    },
    total=False,
)

TenantDatabasePendingModifiedValuesTypeDef = TypedDict(
    "TenantDatabasePendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "TenantDBName": str,
    },
    total=False,
)

TenantDatabaseTypeDef = TypedDict(
    "TenantDatabaseTypeDef",
    {
        "TenantDatabaseCreateTime": datetime,
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
        "Status": str,
        "MasterUsername": str,
        "DbiResourceId": str,
        "TenantDatabaseResourceId": str,
        "TenantDatabaseARN": str,
        "CharacterSetName": str,
        "NcharCharacterSetName": str,
        "DeletionProtection": bool,
        "PendingModifiedValues": "TenantDatabasePendingModifiedValuesTypeDef",
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

TenantDatabasesMessageTypeDef = TypedDict(
    "TenantDatabasesMessageTypeDef",
    {
        "Marker": str,
        "TenantDatabases": List["TenantDatabaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimezoneTypeDef = TypedDict(
    "TimezoneTypeDef",
    {
        "TimezoneName": str,
    },
    total=False,
)

UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
        "SupportedEngineModes": List[str],
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
        "SupportsBabelfish": bool,
        "SupportsLimitlessDatabase": bool,
        "SupportsLocalWriteForwarding": bool,
        "SupportsIntegrations": bool,
    },
    total=False,
)

UserAuthConfigInfoTypeDef = TypedDict(
    "UserAuthConfigInfoTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": Literal["SECRETS"],
        "SecretArn": str,
        "IAMAuth": IAMAuthModeType,
        "ClientPasswordAuthType": ClientPasswordAuthTypeType,
    },
    total=False,
)

UserAuthConfigTypeDef = TypedDict(
    "UserAuthConfigTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": Literal["SECRETS"],
        "SecretArn": str,
        "IAMAuth": IAMAuthModeType,
        "ClientPasswordAuthType": ClientPasswordAuthTypeType,
    },
    total=False,
)

ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List["ValidStorageOptionsTypeDef"],
        "ValidProcessorFeatures": List["AvailableProcessorFeatureTypeDef"],
        "SupportsDedicatedLogVolume": bool,
    },
    total=False,
)

ValidStorageOptionsTypeDef = TypedDict(
    "ValidStorageOptionsTypeDef",
    {
        "StorageType": str,
        "StorageSize": List["RangeTypeDef"],
        "ProvisionedIops": List["RangeTypeDef"],
        "IopsToStorageRatio": List["DoubleRangeTypeDef"],
        "SupportsStorageAutoscaling": bool,
        "ProvisionedStorageThroughput": List["RangeTypeDef"],
        "StorageThroughputToIopsRatio": List["DoubleRangeTypeDef"],
    },
    total=False,
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
