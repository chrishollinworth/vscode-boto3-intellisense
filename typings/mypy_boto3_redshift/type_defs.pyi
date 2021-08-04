"""
Type annotations for redshift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeInputMessageRequestTypeDef

    data: AcceptReservedNodeExchangeInputMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionTypeType,
    AquaConfigurationStatusType,
    AquaStatusType,
    AuthorizationStatusType,
    DataShareStatusForConsumerType,
    DataShareStatusForProducerType,
    DataShareStatusType,
    ModeType,
    NodeConfigurationOptionsFilterNameType,
    OperatorTypeType,
    ParameterApplyTypeType,
    PartnerIntegrationStatusType,
    ReservedNodeOfferingTypeType,
    ScheduledActionFilterNameType,
    ScheduledActionStateType,
    ScheduledActionTypeValuesType,
    ScheduleStateType,
    SnapshotAttributeToSortByType,
    SortByOrderType,
    SourceTypeType,
    TableRestoreStatusTypeType,
    UsageLimitBreachActionType,
    UsageLimitFeatureTypeType,
    UsageLimitLimitTypeType,
    UsageLimitPeriodType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptReservedNodeExchangeInputMessageRequestTypeDef",
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    "AccountAttributeListTypeDef",
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AquaConfigurationTypeDef",
    "AssociateDataShareConsumerMessageRequestTypeDef",
    "AttributeValueTargetTypeDef",
    "AuthenticationProfileTypeDef",
    "AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    "AuthorizeDataShareMessageRequestTypeDef",
    "AuthorizeEndpointAccessMessageRequestTypeDef",
    "AuthorizeSnapshotAccessMessageRequestTypeDef",
    "AuthorizeSnapshotAccessResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchDeleteClusterSnapshotsRequestRequestTypeDef",
    "BatchDeleteClusterSnapshotsResultTypeDef",
    "BatchModifyClusterSnapshotsMessageRequestTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    "CancelResizeMessageRequestTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterCredentialsTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterGroupDetailsTypeDef",
    "ClusterParameterGroupNameMessageTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterGroupsMessageTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSecurityGroupMessageTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "ClusterSubnetGroupMessageTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterTypeDef",
    "ClusterVersionTypeDef",
    "ClusterVersionsMessageTypeDef",
    "ClustersMessageTypeDef",
    "CopyClusterSnapshotMessageRequestTypeDef",
    "CopyClusterSnapshotResultTypeDef",
    "CreateAuthenticationProfileMessageRequestTypeDef",
    "CreateAuthenticationProfileResultTypeDef",
    "CreateClusterMessageRequestTypeDef",
    "CreateClusterParameterGroupMessageRequestTypeDef",
    "CreateClusterParameterGroupResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateClusterSecurityGroupMessageRequestTypeDef",
    "CreateClusterSecurityGroupResultTypeDef",
    "CreateClusterSnapshotMessageRequestTypeDef",
    "CreateClusterSnapshotResultTypeDef",
    "CreateClusterSubnetGroupMessageRequestTypeDef",
    "CreateClusterSubnetGroupResultTypeDef",
    "CreateEndpointAccessMessageRequestTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateHsmClientCertificateMessageRequestTypeDef",
    "CreateHsmClientCertificateResultTypeDef",
    "CreateHsmConfigurationMessageRequestTypeDef",
    "CreateHsmConfigurationResultTypeDef",
    "CreateScheduledActionMessageRequestTypeDef",
    "CreateSnapshotCopyGrantMessageRequestTypeDef",
    "CreateSnapshotCopyGrantResultTypeDef",
    "CreateSnapshotScheduleMessageRequestTypeDef",
    "CreateTagsMessageRequestTypeDef",
    "CreateUsageLimitMessageRequestTypeDef",
    "CustomerStorageMessageTypeDef",
    "DataShareAssociationTypeDef",
    "DataShareResponseMetadataTypeDef",
    "DataShareTypeDef",
    "DataTransferProgressTypeDef",
    "DeauthorizeDataShareMessageRequestTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "DeleteAuthenticationProfileMessageRequestTypeDef",
    "DeleteAuthenticationProfileResultTypeDef",
    "DeleteClusterMessageRequestTypeDef",
    "DeleteClusterParameterGroupMessageRequestTypeDef",
    "DeleteClusterResultTypeDef",
    "DeleteClusterSecurityGroupMessageRequestTypeDef",
    "DeleteClusterSnapshotMessageRequestTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultTypeDef",
    "DeleteClusterSubnetGroupMessageRequestTypeDef",
    "DeleteEndpointAccessMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteHsmClientCertificateMessageRequestTypeDef",
    "DeleteHsmConfigurationMessageRequestTypeDef",
    "DeleteScheduledActionMessageRequestTypeDef",
    "DeleteSnapshotCopyGrantMessageRequestTypeDef",
    "DeleteSnapshotScheduleMessageRequestTypeDef",
    "DeleteTagsMessageRequestTypeDef",
    "DeleteUsageLimitMessageRequestTypeDef",
    "DescribeAccountAttributesMessageRequestTypeDef",
    "DescribeAuthenticationProfilesMessageRequestTypeDef",
    "DescribeAuthenticationProfilesResultTypeDef",
    "DescribeClusterDbRevisionsMessageRequestTypeDef",
    "DescribeClusterParameterGroupsMessageRequestTypeDef",
    "DescribeClusterParametersMessageRequestTypeDef",
    "DescribeClusterSecurityGroupsMessageRequestTypeDef",
    "DescribeClusterSnapshotsMessageRequestTypeDef",
    "DescribeClusterSubnetGroupsMessageRequestTypeDef",
    "DescribeClusterTracksMessageRequestTypeDef",
    "DescribeClusterVersionsMessageRequestTypeDef",
    "DescribeClustersMessageRequestTypeDef",
    "DescribeDataSharesForConsumerMessageRequestTypeDef",
    "DescribeDataSharesForConsumerResultTypeDef",
    "DescribeDataSharesForProducerMessageRequestTypeDef",
    "DescribeDataSharesForProducerResultTypeDef",
    "DescribeDataSharesMessageRequestTypeDef",
    "DescribeDataSharesResultTypeDef",
    "DescribeDefaultClusterParametersMessageRequestTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "DescribeEndpointAccessMessageRequestTypeDef",
    "DescribeEndpointAuthorizationMessageRequestTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeHsmClientCertificatesMessageRequestTypeDef",
    "DescribeHsmConfigurationsMessageRequestTypeDef",
    "DescribeLoggingStatusMessageRequestTypeDef",
    "DescribeNodeConfigurationOptionsMessageRequestTypeDef",
    "DescribeOrderableClusterOptionsMessageRequestTypeDef",
    "DescribePartnersInputMessageRequestTypeDef",
    "DescribePartnersOutputMessageTypeDef",
    "DescribeReservedNodeOfferingsMessageRequestTypeDef",
    "DescribeReservedNodesMessageRequestTypeDef",
    "DescribeResizeMessageRequestTypeDef",
    "DescribeScheduledActionsMessageRequestTypeDef",
    "DescribeSnapshotCopyGrantsMessageRequestTypeDef",
    "DescribeSnapshotSchedulesMessageRequestTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "DescribeTableRestoreStatusMessageRequestTypeDef",
    "DescribeTagsMessageRequestTypeDef",
    "DescribeUsageLimitsMessageRequestTypeDef",
    "DisableLoggingMessageRequestTypeDef",
    "DisableSnapshotCopyMessageRequestTypeDef",
    "DisableSnapshotCopyResultTypeDef",
    "DisassociateDataShareConsumerMessageRequestTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EnableLoggingMessageRequestTypeDef",
    "EnableSnapshotCopyMessageRequestTypeDef",
    "EnableSnapshotCopyResultTypeDef",
    "EndpointAccessListTypeDef",
    "EndpointAccessResponseMetadataTypeDef",
    "EndpointAccessTypeDef",
    "EndpointAuthorizationListTypeDef",
    "EndpointAuthorizationResponseMetadataTypeDef",
    "EndpointAuthorizationTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "GetClusterCredentialsMessageRequestTypeDef",
    "GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationMessageTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "LoggingStatusTypeDef",
    "MaintenanceTrackTypeDef",
    "ModifyAquaInputMessageRequestTypeDef",
    "ModifyAquaOutputMessageTypeDef",
    "ModifyAuthenticationProfileMessageRequestTypeDef",
    "ModifyAuthenticationProfileResultTypeDef",
    "ModifyClusterDbRevisionMessageRequestTypeDef",
    "ModifyClusterDbRevisionResultTypeDef",
    "ModifyClusterIamRolesMessageRequestTypeDef",
    "ModifyClusterIamRolesResultTypeDef",
    "ModifyClusterMaintenanceMessageRequestTypeDef",
    "ModifyClusterMaintenanceResultTypeDef",
    "ModifyClusterMessageRequestTypeDef",
    "ModifyClusterParameterGroupMessageRequestTypeDef",
    "ModifyClusterResultTypeDef",
    "ModifyClusterSnapshotMessageRequestTypeDef",
    "ModifyClusterSnapshotResultTypeDef",
    "ModifyClusterSnapshotScheduleMessageRequestTypeDef",
    "ModifyClusterSubnetGroupMessageRequestTypeDef",
    "ModifyClusterSubnetGroupResultTypeDef",
    "ModifyEndpointAccessMessageRequestTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyScheduledActionMessageRequestTypeDef",
    "ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    "ModifySnapshotScheduleMessageRequestTypeDef",
    "ModifyUsageLimitMessageRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeConfigurationOptionTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionsMessageTypeDef",
    "OrderableClusterOptionTypeDef",
    "OrderableClusterOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PartnerIntegrationInfoTypeDef",
    "PartnerIntegrationInputMessageRequestTypeDef",
    "PartnerIntegrationOutputMessageTypeDef",
    "PauseClusterMessageRequestTypeDef",
    "PauseClusterMessageTypeDef",
    "PauseClusterResultTypeDef",
    "PendingModifiedValuesTypeDef",
    "PurchaseReservedNodeOfferingMessageRequestTypeDef",
    "PurchaseReservedNodeOfferingResultTypeDef",
    "RebootClusterMessageRequestTypeDef",
    "RebootClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "RejectDataShareMessageRequestTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageTypeDef",
    "ResetClusterParameterGroupMessageRequestTypeDef",
    "ResizeClusterMessageRequestTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeClusterResultTypeDef",
    "ResizeInfoTypeDef",
    "ResizeProgressMessageTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromClusterSnapshotMessageRequestTypeDef",
    "RestoreFromClusterSnapshotResultTypeDef",
    "RestoreStatusTypeDef",
    "RestoreTableFromClusterSnapshotMessageRequestTypeDef",
    "RestoreTableFromClusterSnapshotResultTypeDef",
    "ResumeClusterMessageRequestTypeDef",
    "ResumeClusterMessageTypeDef",
    "ResumeClusterResultTypeDef",
    "RevisionTargetTypeDef",
    "RevokeClusterSecurityGroupIngressMessageRequestTypeDef",
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    "RevokeEndpointAccessMessageRequestTypeDef",
    "RevokeSnapshotAccessMessageRequestTypeDef",
    "RevokeSnapshotAccessResultTypeDef",
    "RotateEncryptionKeyMessageRequestTypeDef",
    "RotateEncryptionKeyResultTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionResponseMetadataTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotScheduleResponseMetadataTypeDef",
    "SnapshotScheduleTypeDef",
    "SnapshotSortingEntityTypeDef",
    "SnapshotTypeDef",
    "SubnetTypeDef",
    "SupportedOperationTypeDef",
    "SupportedPlatformTypeDef",
    "TableRestoreStatusMessageTypeDef",
    "TableRestoreStatusTypeDef",
    "TagTypeDef",
    "TaggedResourceListMessageTypeDef",
    "TaggedResourceTypeDef",
    "TrackListMessageTypeDef",
    "UpdatePartnerStatusInputMessageRequestTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitListTypeDef",
    "UsageLimitResponseMetadataTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AcceptReservedNodeExchangeInputMessageRequestTypeDef = TypedDict(
    "AcceptReservedNodeExchangeInputMessageRequestTypeDef",
    {
        "ReservedNodeId": str,
        "TargetReservedNodeOfferingId": str,
    },
)

AcceptReservedNodeExchangeOutputMessageTypeDef = TypedDict(
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    {
        "ExchangedReservedNode": "ReservedNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAttributeListTypeDef = TypedDict(
    "AccountAttributeListTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List["AttributeValueTargetTypeDef"],
    },
    total=False,
)

AccountWithRestoreAccessTypeDef = TypedDict(
    "AccountWithRestoreAccessTypeDef",
    {
        "AccountId": str,
        "AccountAlias": str,
    },
    total=False,
)

AquaConfigurationTypeDef = TypedDict(
    "AquaConfigurationTypeDef",
    {
        "AquaStatus": AquaStatusType,
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)

_RequiredAssociateDataShareConsumerMessageRequestTypeDef = TypedDict(
    "_RequiredAssociateDataShareConsumerMessageRequestTypeDef",
    {
        "DataShareArn": str,
    },
)
_OptionalAssociateDataShareConsumerMessageRequestTypeDef = TypedDict(
    "_OptionalAssociateDataShareConsumerMessageRequestTypeDef",
    {
        "AssociateEntireAccount": bool,
        "ConsumerArn": str,
    },
    total=False,
)

class AssociateDataShareConsumerMessageRequestTypeDef(
    _RequiredAssociateDataShareConsumerMessageRequestTypeDef,
    _OptionalAssociateDataShareConsumerMessageRequestTypeDef,
):
    pass

AttributeValueTargetTypeDef = TypedDict(
    "AttributeValueTargetTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

AuthenticationProfileTypeDef = TypedDict(
    "AuthenticationProfileTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
    },
    total=False,
)

_RequiredAuthorizeClusterSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_RequiredAuthorizeClusterSecurityGroupIngressMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
)
_OptionalAuthorizeClusterSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_OptionalAuthorizeClusterSecurityGroupIngressMessageRequestTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

class AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef(
    _RequiredAuthorizeClusterSecurityGroupIngressMessageRequestTypeDef,
    _OptionalAuthorizeClusterSecurityGroupIngressMessageRequestTypeDef,
):
    pass

AuthorizeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeDataShareMessageRequestTypeDef = TypedDict(
    "AuthorizeDataShareMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "ConsumerIdentifier": str,
    },
)

_RequiredAuthorizeEndpointAccessMessageRequestTypeDef = TypedDict(
    "_RequiredAuthorizeEndpointAccessMessageRequestTypeDef",
    {
        "Account": str,
    },
)
_OptionalAuthorizeEndpointAccessMessageRequestTypeDef = TypedDict(
    "_OptionalAuthorizeEndpointAccessMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "VpcIds": List[str],
    },
    total=False,
)

class AuthorizeEndpointAccessMessageRequestTypeDef(
    _RequiredAuthorizeEndpointAccessMessageRequestTypeDef,
    _OptionalAuthorizeEndpointAccessMessageRequestTypeDef,
):
    pass

_RequiredAuthorizeSnapshotAccessMessageRequestTypeDef = TypedDict(
    "_RequiredAuthorizeSnapshotAccessMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "AccountWithRestoreAccess": str,
    },
)
_OptionalAuthorizeSnapshotAccessMessageRequestTypeDef = TypedDict(
    "_OptionalAuthorizeSnapshotAccessMessageRequestTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)

class AuthorizeSnapshotAccessMessageRequestTypeDef(
    _RequiredAuthorizeSnapshotAccessMessageRequestTypeDef,
    _OptionalAuthorizeSnapshotAccessMessageRequestTypeDef,
):
    pass

AuthorizeSnapshotAccessResultTypeDef = TypedDict(
    "AuthorizeSnapshotAccessResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List["SupportedPlatformTypeDef"],
    },
    total=False,
)

BatchDeleteClusterSnapshotsRequestRequestTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsRequestRequestTypeDef",
    {
        "Identifiers": List["DeleteClusterSnapshotMessageTypeDef"],
    },
)

BatchDeleteClusterSnapshotsResultTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsResultTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchModifyClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "_RequiredBatchModifyClusterSnapshotsMessageRequestTypeDef",
    {
        "SnapshotIdentifierList": List[str],
    },
)
_OptionalBatchModifyClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "_OptionalBatchModifyClusterSnapshotsMessageRequestTypeDef",
    {
        "ManualSnapshotRetentionPeriod": int,
        "Force": bool,
    },
    total=False,
)

class BatchModifyClusterSnapshotsMessageRequestTypeDef(
    _RequiredBatchModifyClusterSnapshotsMessageRequestTypeDef,
    _OptionalBatchModifyClusterSnapshotsMessageRequestTypeDef,
):
    pass

BatchModifyClusterSnapshotsOutputMessageTypeDef = TypedDict(
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelResizeMessageRequestTypeDef = TypedDict(
    "CancelResizeMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ClusterAssociatedToScheduleTypeDef = TypedDict(
    "ClusterAssociatedToScheduleTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": ScheduleStateType,
    },
    total=False,
)

ClusterCredentialsTypeDef = TypedDict(
    "ClusterCredentialsTypeDef",
    {
        "DbUser": str,
        "DbPassword": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterDbRevisionTypeDef = TypedDict(
    "ClusterDbRevisionTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List["RevisionTargetTypeDef"],
    },
    total=False,
)

ClusterDbRevisionsMessageTypeDef = TypedDict(
    "ClusterDbRevisionsMessageTypeDef",
    {
        "Marker": str,
        "ClusterDbRevisions": List["ClusterDbRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterIamRoleTypeDef = TypedDict(
    "ClusterIamRoleTypeDef",
    {
        "IamRoleArn": str,
        "ApplyStatus": str,
    },
    total=False,
)

ClusterNodeTypeDef = TypedDict(
    "ClusterNodeTypeDef",
    {
        "NodeRole": str,
        "PrivateIPAddress": str,
        "PublicIPAddress": str,
    },
    total=False,
)

ClusterParameterGroupDetailsTypeDef = TypedDict(
    "ClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterGroupNameMessageTypeDef = TypedDict(
    "ClusterParameterGroupNameMessageTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterGroupStatusTypeDef = TypedDict(
    "ClusterParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List["ClusterParameterStatusTypeDef"],
    },
    total=False,
)

ClusterParameterGroupTypeDef = TypedDict(
    "ClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterParameterGroupsMessageTypeDef = TypedDict(
    "ClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "ParameterGroups": List["ClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterStatusTypeDef = TypedDict(
    "ClusterParameterStatusTypeDef",
    {
        "ParameterName": str,
        "ParameterApplyStatus": str,
        "ParameterApplyErrorDescription": str,
    },
    total=False,
)

ClusterSecurityGroupMembershipTypeDef = TypedDict(
    "ClusterSecurityGroupMembershipTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

ClusterSecurityGroupMessageTypeDef = TypedDict(
    "ClusterSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "ClusterSecurityGroups": List["ClusterSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterSecurityGroupTypeDef = TypedDict(
    "ClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "IPRanges": List["IPRangeTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClusterSubnetGroupMessageTypeDef = TypedDict(
    "ClusterSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "ClusterSubnetGroups": List["ClusterSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterSubnetGroupTypeDef = TypedDict(
    "ClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": "EndpointTypeDef",
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List["ClusterSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "ClusterParameterGroups": List["ClusterParameterGroupStatusTypeDef"],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": "RestoreStatusTypeDef",
        "DataTransferProgress": "DataTransferProgressTypeDef",
        "HsmStatus": "HsmStatusTypeDef",
        "ClusterSnapshotCopyStatus": "ClusterSnapshotCopyStatusTypeDef",
        "ClusterPublicKey": str,
        "ClusterNodes": List["ClusterNodeTypeDef"],
        "ElasticIpStatus": "ElasticIpStatusTypeDef",
        "ClusterRevisionNumber": str,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List["ClusterIamRoleTypeDef"],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List["DeferredMaintenanceWindowTypeDef"],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": ScheduleStateType,
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": "ResizeInfoTypeDef",
        "AvailabilityZoneRelocationStatus": str,
        "ClusterNamespaceArn": str,
        "TotalStorageCapacityInMegaBytes": int,
        "AquaConfiguration": "AquaConfigurationTypeDef",
    },
    total=False,
)

ClusterVersionTypeDef = TypedDict(
    "ClusterVersionTypeDef",
    {
        "ClusterVersion": str,
        "ClusterParameterGroupFamily": str,
        "Description": str,
    },
    total=False,
)

ClusterVersionsMessageTypeDef = TypedDict(
    "ClusterVersionsMessageTypeDef",
    {
        "Marker": str,
        "ClusterVersions": List["ClusterVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClustersMessageTypeDef = TypedDict(
    "ClustersMessageTypeDef",
    {
        "Marker": str,
        "Clusters": List["ClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCopyClusterSnapshotMessageRequestTypeDef",
    {
        "SourceSnapshotIdentifier": str,
        "TargetSnapshotIdentifier": str,
    },
)
_OptionalCopyClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCopyClusterSnapshotMessageRequestTypeDef",
    {
        "SourceSnapshotClusterIdentifier": str,
        "ManualSnapshotRetentionPeriod": int,
    },
    total=False,
)

class CopyClusterSnapshotMessageRequestTypeDef(
    _RequiredCopyClusterSnapshotMessageRequestTypeDef,
    _OptionalCopyClusterSnapshotMessageRequestTypeDef,
):
    pass

CopyClusterSnapshotResultTypeDef = TypedDict(
    "CopyClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAuthenticationProfileMessageRequestTypeDef = TypedDict(
    "CreateAuthenticationProfileMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
    },
)

CreateAuthenticationProfileResultTypeDef = TypedDict(
    "CreateAuthenticationProfileResultTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterMessageRequestTypeDef = TypedDict(
    "_RequiredCreateClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
    },
)
_OptionalCreateClusterMessageRequestTypeDef = TypedDict(
    "_OptionalCreateClusterMessageRequestTypeDef",
    {
        "DBName": str,
        "ClusterType": str,
        "ClusterSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "ClusterSubnetGroupName": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "ClusterParameterGroupName": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "Port": int,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "ElasticIp": str,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "AdditionalInfo": str,
        "IamRoles": List[str],
        "MaintenanceTrackName": str,
        "SnapshotScheduleIdentifier": str,
        "AvailabilityZoneRelocation": bool,
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)

class CreateClusterMessageRequestTypeDef(
    _RequiredCreateClusterMessageRequestTypeDef, _OptionalCreateClusterMessageRequestTypeDef
):
    pass

_RequiredCreateClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateClusterParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateClusterParameterGroupMessageRequestTypeDef(
    _RequiredCreateClusterParameterGroupMessageRequestTypeDef,
    _OptionalCreateClusterParameterGroupMessageRequestTypeDef,
):
    pass

CreateClusterParameterGroupResultTypeDef = TypedDict(
    "CreateClusterParameterGroupResultTypeDef",
    {
        "ClusterParameterGroup": "ClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSecurityGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateClusterSecurityGroupMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
    },
)
_OptionalCreateClusterSecurityGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateClusterSecurityGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateClusterSecurityGroupMessageRequestTypeDef(
    _RequiredCreateClusterSecurityGroupMessageRequestTypeDef,
    _OptionalCreateClusterSecurityGroupMessageRequestTypeDef,
):
    pass

CreateClusterSecurityGroupResultTypeDef = TypedDict(
    "CreateClusterSecurityGroupResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCreateClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
    },
)
_OptionalCreateClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCreateClusterSnapshotMessageRequestTypeDef",
    {
        "ManualSnapshotRetentionPeriod": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateClusterSnapshotMessageRequestTypeDef(
    _RequiredCreateClusterSnapshotMessageRequestTypeDef,
    _OptionalCreateClusterSnapshotMessageRequestTypeDef,
):
    pass

CreateClusterSnapshotResultTypeDef = TypedDict(
    "CreateClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateClusterSubnetGroupMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateClusterSubnetGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateClusterSubnetGroupMessageRequestTypeDef(
    _RequiredCreateClusterSubnetGroupMessageRequestTypeDef,
    _OptionalCreateClusterSubnetGroupMessageRequestTypeDef,
):
    pass

CreateClusterSubnetGroupResultTypeDef = TypedDict(
    "CreateClusterSubnetGroupResultTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointAccessMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointAccessMessageRequestTypeDef",
    {
        "EndpointName": str,
        "SubnetGroupName": str,
    },
)
_OptionalCreateEndpointAccessMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointAccessMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)

class CreateEndpointAccessMessageRequestTypeDef(
    _RequiredCreateEndpointAccessMessageRequestTypeDef,
    _OptionalCreateEndpointAccessMessageRequestTypeDef,
):
    pass

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
        "SourceIds": List[str],
        "EventCategories": List[str],
        "Severity": str,
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

_RequiredCreateHsmClientCertificateMessageRequestTypeDef = TypedDict(
    "_RequiredCreateHsmClientCertificateMessageRequestTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
    },
)
_OptionalCreateHsmClientCertificateMessageRequestTypeDef = TypedDict(
    "_OptionalCreateHsmClientCertificateMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHsmClientCertificateMessageRequestTypeDef(
    _RequiredCreateHsmClientCertificateMessageRequestTypeDef,
    _OptionalCreateHsmClientCertificateMessageRequestTypeDef,
):
    pass

CreateHsmClientCertificateResultTypeDef = TypedDict(
    "CreateHsmClientCertificateResultTypeDef",
    {
        "HsmClientCertificate": "HsmClientCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHsmConfigurationMessageRequestTypeDef = TypedDict(
    "_RequiredCreateHsmConfigurationMessageRequestTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "HsmPartitionPassword": str,
        "HsmServerPublicCertificate": str,
    },
)
_OptionalCreateHsmConfigurationMessageRequestTypeDef = TypedDict(
    "_OptionalCreateHsmConfigurationMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHsmConfigurationMessageRequestTypeDef(
    _RequiredCreateHsmConfigurationMessageRequestTypeDef,
    _OptionalCreateHsmConfigurationMessageRequestTypeDef,
):
    pass

CreateHsmConfigurationResultTypeDef = TypedDict(
    "CreateHsmConfigurationResultTypeDef",
    {
        "HsmConfiguration": "HsmConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduledActionMessageRequestTypeDef = TypedDict(
    "_RequiredCreateScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
    },
)
_OptionalCreateScheduledActionMessageRequestTypeDef = TypedDict(
    "_OptionalCreateScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionDescription": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Enable": bool,
    },
    total=False,
)

class CreateScheduledActionMessageRequestTypeDef(
    _RequiredCreateScheduledActionMessageRequestTypeDef,
    _OptionalCreateScheduledActionMessageRequestTypeDef,
):
    pass

_RequiredCreateSnapshotCopyGrantMessageRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotCopyGrantMessageRequestTypeDef",
    {
        "SnapshotCopyGrantName": str,
    },
)
_OptionalCreateSnapshotCopyGrantMessageRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotCopyGrantMessageRequestTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSnapshotCopyGrantMessageRequestTypeDef(
    _RequiredCreateSnapshotCopyGrantMessageRequestTypeDef,
    _OptionalCreateSnapshotCopyGrantMessageRequestTypeDef,
):
    pass

CreateSnapshotCopyGrantResultTypeDef = TypedDict(
    "CreateSnapshotCopyGrantResultTypeDef",
    {
        "SnapshotCopyGrant": "SnapshotCopyGrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "CreateSnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
        "NextInvocations": int,
    },
    total=False,
)

CreateTagsMessageRequestTypeDef = TypedDict(
    "CreateTagsMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredCreateUsageLimitMessageRequestTypeDef = TypedDict(
    "_RequiredCreateUsageLimitMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
    },
)
_OptionalCreateUsageLimitMessageRequestTypeDef = TypedDict(
    "_OptionalCreateUsageLimitMessageRequestTypeDef",
    {
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUsageLimitMessageRequestTypeDef(
    _RequiredCreateUsageLimitMessageRequestTypeDef, _OptionalCreateUsageLimitMessageRequestTypeDef
):
    pass

CustomerStorageMessageTypeDef = TypedDict(
    "CustomerStorageMessageTypeDef",
    {
        "TotalBackupSizeInMegaBytes": float,
        "TotalProvisionedStorageInMegaBytes": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataShareAssociationTypeDef = TypedDict(
    "DataShareAssociationTypeDef",
    {
        "ConsumerIdentifier": str,
        "Status": DataShareStatusType,
        "CreatedDate": datetime,
        "StatusChangeDate": datetime,
    },
    total=False,
)

DataShareResponseMetadataTypeDef = TypedDict(
    "DataShareResponseMetadataTypeDef",
    {
        "DataShareArn": str,
        "ProducerArn": str,
        "AllowPubliclyAccessibleConsumers": bool,
        "DataShareAssociations": List["DataShareAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataShareTypeDef = TypedDict(
    "DataShareTypeDef",
    {
        "DataShareArn": str,
        "ProducerArn": str,
        "AllowPubliclyAccessibleConsumers": bool,
        "DataShareAssociations": List["DataShareAssociationTypeDef"],
    },
    total=False,
)

DataTransferProgressTypeDef = TypedDict(
    "DataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

DeauthorizeDataShareMessageRequestTypeDef = TypedDict(
    "DeauthorizeDataShareMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "ConsumerIdentifier": str,
    },
)

DefaultClusterParametersTypeDef = TypedDict(
    "DefaultClusterParametersTypeDef",
    {
        "ParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

DeferredMaintenanceWindowTypeDef = TypedDict(
    "DeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

DeleteAuthenticationProfileMessageRequestTypeDef = TypedDict(
    "DeleteAuthenticationProfileMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
    },
)

DeleteAuthenticationProfileResultTypeDef = TypedDict(
    "DeleteAuthenticationProfileResultTypeDef",
    {
        "AuthenticationProfileName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClusterMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalDeleteClusterMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteClusterMessageRequestTypeDef",
    {
        "SkipFinalClusterSnapshot": bool,
        "FinalClusterSnapshotIdentifier": str,
        "FinalClusterSnapshotRetentionPeriod": int,
    },
    total=False,
)

class DeleteClusterMessageRequestTypeDef(
    _RequiredDeleteClusterMessageRequestTypeDef, _OptionalDeleteClusterMessageRequestTypeDef
):
    pass

DeleteClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)

DeleteClusterResultTypeDef = TypedDict(
    "DeleteClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteClusterSecurityGroupMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
)

_RequiredDeleteClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
    },
)
_OptionalDeleteClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)

class DeleteClusterSnapshotMessageRequestTypeDef(
    _RequiredDeleteClusterSnapshotMessageRequestTypeDef,
    _OptionalDeleteClusterSnapshotMessageRequestTypeDef,
):
    pass

_RequiredDeleteClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredDeleteClusterSnapshotMessageTypeDef",
    {
        "SnapshotIdentifier": str,
    },
)
_OptionalDeleteClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalDeleteClusterSnapshotMessageTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)

class DeleteClusterSnapshotMessageTypeDef(
    _RequiredDeleteClusterSnapshotMessageTypeDef, _OptionalDeleteClusterSnapshotMessageTypeDef
):
    pass

DeleteClusterSnapshotResultTypeDef = TypedDict(
    "DeleteClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteClusterSubnetGroupMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
    },
)

DeleteEndpointAccessMessageRequestTypeDef = TypedDict(
    "DeleteEndpointAccessMessageRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteHsmClientCertificateMessageRequestTypeDef = TypedDict(
    "DeleteHsmClientCertificateMessageRequestTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
    },
)

DeleteHsmConfigurationMessageRequestTypeDef = TypedDict(
    "DeleteHsmConfigurationMessageRequestTypeDef",
    {
        "HsmConfigurationIdentifier": str,
    },
)

DeleteScheduledActionMessageRequestTypeDef = TypedDict(
    "DeleteScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)

DeleteSnapshotCopyGrantMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotCopyGrantMessageRequestTypeDef",
    {
        "SnapshotCopyGrantName": str,
    },
)

DeleteSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleIdentifier": str,
    },
)

DeleteTagsMessageRequestTypeDef = TypedDict(
    "DeleteTagsMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

DeleteUsageLimitMessageRequestTypeDef = TypedDict(
    "DeleteUsageLimitMessageRequestTypeDef",
    {
        "UsageLimitId": str,
    },
)

DescribeAccountAttributesMessageRequestTypeDef = TypedDict(
    "DescribeAccountAttributesMessageRequestTypeDef",
    {
        "AttributeNames": List[str],
    },
    total=False,
)

DescribeAuthenticationProfilesMessageRequestTypeDef = TypedDict(
    "DescribeAuthenticationProfilesMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
    },
    total=False,
)

DescribeAuthenticationProfilesResultTypeDef = TypedDict(
    "DescribeAuthenticationProfilesResultTypeDef",
    {
        "AuthenticationProfiles": List["AuthenticationProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterDbRevisionsMessageRequestTypeDef = TypedDict(
    "DescribeClusterDbRevisionsMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeClusterParameterGroupsMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

_RequiredDescribeClusterParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeClusterParametersMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalDescribeClusterParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeClusterParametersMessageRequestTypeDef",
    {
        "Source": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeClusterParametersMessageRequestTypeDef(
    _RequiredDescribeClusterParametersMessageRequestTypeDef,
    _OptionalDescribeClusterParametersMessageRequestTypeDef,
):
    pass

DescribeClusterSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeClusterSecurityGroupsMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeClusterSnapshotsMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SnapshotType": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxRecords": int,
        "Marker": str,
        "OwnerAccount": str,
        "TagKeys": List[str],
        "TagValues": List[str],
        "ClusterExists": bool,
        "SortingEntities": List["SnapshotSortingEntityTypeDef"],
    },
    total=False,
)

DescribeClusterSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeClusterSubnetGroupsMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeClusterTracksMessageRequestTypeDef = TypedDict(
    "DescribeClusterTracksMessageRequestTypeDef",
    {
        "MaintenanceTrackName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeClusterVersionsMessageRequestTypeDef = TypedDict(
    "DescribeClusterVersionsMessageRequestTypeDef",
    {
        "ClusterVersion": str,
        "ClusterParameterGroupFamily": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeClustersMessageRequestTypeDef = TypedDict(
    "DescribeClustersMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeDataSharesForConsumerMessageRequestTypeDef = TypedDict(
    "DescribeDataSharesForConsumerMessageRequestTypeDef",
    {
        "ConsumerArn": str,
        "Status": DataShareStatusForConsumerType,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDataSharesForConsumerResultTypeDef = TypedDict(
    "DescribeDataSharesForConsumerResultTypeDef",
    {
        "DataShares": List["DataShareTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSharesForProducerMessageRequestTypeDef = TypedDict(
    "DescribeDataSharesForProducerMessageRequestTypeDef",
    {
        "ProducerArn": str,
        "Status": DataShareStatusForProducerType,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDataSharesForProducerResultTypeDef = TypedDict(
    "DescribeDataSharesForProducerResultTypeDef",
    {
        "DataShares": List["DataShareTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSharesMessageRequestTypeDef = TypedDict(
    "DescribeDataSharesMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDataSharesResultTypeDef = TypedDict(
    "DescribeDataSharesResultTypeDef",
    {
        "DataShares": List["DataShareTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDefaultClusterParametersMessageRequestTypeDef",
    {
        "ParameterGroupFamily": str,
    },
)
_OptionalDescribeDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDefaultClusterParametersMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDefaultClusterParametersMessageRequestTypeDef(
    _RequiredDescribeDefaultClusterParametersMessageRequestTypeDef,
    _OptionalDescribeDefaultClusterParametersMessageRequestTypeDef,
):
    pass

DescribeDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeDefaultClusterParametersResultTypeDef",
    {
        "DefaultClusterParameters": "DefaultClusterParametersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointAccessMessageRequestTypeDef = TypedDict(
    "DescribeEndpointAccessMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "EndpointName": str,
        "VpcId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointAuthorizationMessageRequestTypeDef = TypedDict(
    "DescribeEndpointAuthorizationMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Account": str,
        "Grantee": bool,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)

DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
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
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeHsmClientCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeHsmClientCertificatesMessageRequestTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeHsmConfigurationsMessageRequestTypeDef = TypedDict(
    "DescribeHsmConfigurationsMessageRequestTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeLoggingStatusMessageRequestTypeDef = TypedDict(
    "DescribeLoggingStatusMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

_RequiredDescribeNodeConfigurationOptionsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeNodeConfigurationOptionsMessageRequestTypeDef",
    {
        "ActionType": ActionTypeType,
    },
)
_OptionalDescribeNodeConfigurationOptionsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeNodeConfigurationOptionsMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "OwnerAccount": str,
        "Filters": List["NodeConfigurationOptionsFilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeNodeConfigurationOptionsMessageRequestTypeDef(
    _RequiredDescribeNodeConfigurationOptionsMessageRequestTypeDef,
    _OptionalDescribeNodeConfigurationOptionsMessageRequestTypeDef,
):
    pass

DescribeOrderableClusterOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOrderableClusterOptionsMessageRequestTypeDef",
    {
        "ClusterVersion": str,
        "NodeType": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribePartnersInputMessageRequestTypeDef = TypedDict(
    "_RequiredDescribePartnersInputMessageRequestTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
    },
)
_OptionalDescribePartnersInputMessageRequestTypeDef = TypedDict(
    "_OptionalDescribePartnersInputMessageRequestTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
    },
    total=False,
)

class DescribePartnersInputMessageRequestTypeDef(
    _RequiredDescribePartnersInputMessageRequestTypeDef,
    _OptionalDescribePartnersInputMessageRequestTypeDef,
):
    pass

DescribePartnersOutputMessageTypeDef = TypedDict(
    "DescribePartnersOutputMessageTypeDef",
    {
        "PartnerIntegrationInfoList": List["PartnerIntegrationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedNodeOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedNodeOfferingsMessageRequestTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedNodesMessageRequestTypeDef = TypedDict(
    "DescribeReservedNodesMessageRequestTypeDef",
    {
        "ReservedNodeId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeResizeMessageRequestTypeDef = TypedDict(
    "DescribeResizeMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DescribeScheduledActionsMessageRequestTypeDef = TypedDict(
    "DescribeScheduledActionsMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
        "TargetActionType": ScheduledActionTypeValuesType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Active": bool,
        "Filters": List["ScheduledActionFilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeSnapshotCopyGrantsMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotCopyGrantsMessageRequestTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeSnapshotSchedulesMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotSchedulesMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleIdentifier": str,
        "TagKeys": List[str],
        "TagValues": List[str],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeSnapshotSchedulesOutputMessageTypeDef = TypedDict(
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    {
        "SnapshotSchedules": List["SnapshotScheduleTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableRestoreStatusMessageRequestTypeDef = TypedDict(
    "DescribeTableRestoreStatusMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "TableRestoreRequestId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeTagsMessageRequestTypeDef = TypedDict(
    "DescribeTagsMessageRequestTypeDef",
    {
        "ResourceName": str,
        "ResourceType": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeUsageLimitsMessageRequestTypeDef = TypedDict(
    "DescribeUsageLimitsMessageRequestTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DisableLoggingMessageRequestTypeDef = TypedDict(
    "DisableLoggingMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DisableSnapshotCopyMessageRequestTypeDef = TypedDict(
    "DisableSnapshotCopyMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DisableSnapshotCopyResultTypeDef = TypedDict(
    "DisableSnapshotCopyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateDataShareConsumerMessageRequestTypeDef = TypedDict(
    "_RequiredDisassociateDataShareConsumerMessageRequestTypeDef",
    {
        "DataShareArn": str,
    },
)
_OptionalDisassociateDataShareConsumerMessageRequestTypeDef = TypedDict(
    "_OptionalDisassociateDataShareConsumerMessageRequestTypeDef",
    {
        "DisassociateEntireAccount": bool,
        "ConsumerArn": str,
    },
    total=False,
)

class DisassociateDataShareConsumerMessageRequestTypeDef(
    _RequiredDisassociateDataShareConsumerMessageRequestTypeDef,
    _OptionalDisassociateDataShareConsumerMessageRequestTypeDef,
):
    pass

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticIpStatusTypeDef = TypedDict(
    "ElasticIpStatusTypeDef",
    {
        "ElasticIp": str,
        "Status": str,
    },
    total=False,
)

_RequiredEnableLoggingMessageRequestTypeDef = TypedDict(
    "_RequiredEnableLoggingMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "BucketName": str,
    },
)
_OptionalEnableLoggingMessageRequestTypeDef = TypedDict(
    "_OptionalEnableLoggingMessageRequestTypeDef",
    {
        "S3KeyPrefix": str,
    },
    total=False,
)

class EnableLoggingMessageRequestTypeDef(
    _RequiredEnableLoggingMessageRequestTypeDef, _OptionalEnableLoggingMessageRequestTypeDef
):
    pass

_RequiredEnableSnapshotCopyMessageRequestTypeDef = TypedDict(
    "_RequiredEnableSnapshotCopyMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "DestinationRegion": str,
    },
)
_OptionalEnableSnapshotCopyMessageRequestTypeDef = TypedDict(
    "_OptionalEnableSnapshotCopyMessageRequestTypeDef",
    {
        "RetentionPeriod": int,
        "SnapshotCopyGrantName": str,
        "ManualSnapshotRetentionPeriod": int,
    },
    total=False,
)

class EnableSnapshotCopyMessageRequestTypeDef(
    _RequiredEnableSnapshotCopyMessageRequestTypeDef,
    _OptionalEnableSnapshotCopyMessageRequestTypeDef,
):
    pass

EnableSnapshotCopyResultTypeDef = TypedDict(
    "EnableSnapshotCopyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessListTypeDef = TypedDict(
    "EndpointAccessListTypeDef",
    {
        "EndpointAccessList": List["EndpointAccessTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessResponseMetadataTypeDef = TypedDict(
    "EndpointAccessResponseMetadataTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "SubnetGroupName": str,
        "EndpointStatus": str,
        "EndpointName": str,
        "EndpointCreateTime": datetime,
        "Port": int,
        "Address": str,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessTypeDef = TypedDict(
    "EndpointAccessTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "SubnetGroupName": str,
        "EndpointStatus": str,
        "EndpointName": str,
        "EndpointCreateTime": datetime,
        "Port": int,
        "Address": str,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "VpcEndpoint": "VpcEndpointTypeDef",
    },
    total=False,
)

EndpointAuthorizationListTypeDef = TypedDict(
    "EndpointAuthorizationListTypeDef",
    {
        "EndpointAuthorizationList": List["EndpointAuthorizationTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAuthorizationResponseMetadataTypeDef = TypedDict(
    "EndpointAuthorizationResponseMetadataTypeDef",
    {
        "Grantor": str,
        "Grantee": str,
        "ClusterIdentifier": str,
        "AuthorizeTime": datetime,
        "ClusterStatus": str,
        "Status": AuthorizationStatusType,
        "AllowedAllVPCs": bool,
        "AllowedVPCs": List[str],
        "EndpointCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAuthorizationTypeDef = TypedDict(
    "EndpointAuthorizationTypeDef",
    {
        "Grantor": str,
        "Grantee": str,
        "ClusterIdentifier": str,
        "AuthorizeTime": datetime,
        "ClusterStatus": str,
        "Status": AuthorizationStatusType,
        "AllowedAllVPCs": bool,
        "AllowedVPCs": List[str],
        "EndpointCount": int,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "VpcEndpoints": List["VpcEndpointTypeDef"],
    },
    total=False,
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": str,
        "Events": List["EventInfoMapTypeDef"],
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

EventInfoMapTypeDef = TypedDict(
    "EventInfoMapTypeDef",
    {
        "EventId": str,
        "EventCategories": List[str],
        "EventDescription": str,
        "Severity": str,
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
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
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
        "Severity": str,
        "Date": datetime,
        "EventId": str,
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

_RequiredGetClusterCredentialsMessageRequestTypeDef = TypedDict(
    "_RequiredGetClusterCredentialsMessageRequestTypeDef",
    {
        "DbUser": str,
        "ClusterIdentifier": str,
    },
)
_OptionalGetClusterCredentialsMessageRequestTypeDef = TypedDict(
    "_OptionalGetClusterCredentialsMessageRequestTypeDef",
    {
        "DbName": str,
        "DurationSeconds": int,
        "AutoCreate": bool,
        "DbGroups": List[str],
    },
    total=False,
)

class GetClusterCredentialsMessageRequestTypeDef(
    _RequiredGetClusterCredentialsMessageRequestTypeDef,
    _OptionalGetClusterCredentialsMessageRequestTypeDef,
):
    pass

_RequiredGetReservedNodeExchangeOfferingsInputMessageRequestTypeDef = TypedDict(
    "_RequiredGetReservedNodeExchangeOfferingsInputMessageRequestTypeDef",
    {
        "ReservedNodeId": str,
    },
)
_OptionalGetReservedNodeExchangeOfferingsInputMessageRequestTypeDef = TypedDict(
    "_OptionalGetReservedNodeExchangeOfferingsInputMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef(
    _RequiredGetReservedNodeExchangeOfferingsInputMessageRequestTypeDef,
    _OptionalGetReservedNodeExchangeOfferingsInputMessageRequestTypeDef,
):
    pass

GetReservedNodeExchangeOfferingsOutputMessageTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmClientCertificateMessageTypeDef = TypedDict(
    "HsmClientCertificateMessageTypeDef",
    {
        "Marker": str,
        "HsmClientCertificates": List["HsmClientCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmClientCertificateTypeDef = TypedDict(
    "HsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HsmConfigurationMessageTypeDef = TypedDict(
    "HsmConfigurationMessageTypeDef",
    {
        "Marker": str,
        "HsmConfigurations": List["HsmConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmConfigurationTypeDef = TypedDict(
    "HsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HsmStatusTypeDef = TypedDict(
    "HsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "Status": str,
    },
    total=False,
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LoggingStatusTypeDef = TypedDict(
    "LoggingStatusTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MaintenanceTrackTypeDef = TypedDict(
    "MaintenanceTrackTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List["UpdateTargetTypeDef"],
    },
    total=False,
)

_RequiredModifyAquaInputMessageRequestTypeDef = TypedDict(
    "_RequiredModifyAquaInputMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyAquaInputMessageRequestTypeDef = TypedDict(
    "_OptionalModifyAquaInputMessageRequestTypeDef",
    {
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)

class ModifyAquaInputMessageRequestTypeDef(
    _RequiredModifyAquaInputMessageRequestTypeDef, _OptionalModifyAquaInputMessageRequestTypeDef
):
    pass

ModifyAquaOutputMessageTypeDef = TypedDict(
    "ModifyAquaOutputMessageTypeDef",
    {
        "AquaConfiguration": "AquaConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyAuthenticationProfileMessageRequestTypeDef = TypedDict(
    "ModifyAuthenticationProfileMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
    },
)

ModifyAuthenticationProfileResultTypeDef = TypedDict(
    "ModifyAuthenticationProfileResultTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterDbRevisionMessageRequestTypeDef = TypedDict(
    "ModifyClusterDbRevisionMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "RevisionTarget": str,
    },
)

ModifyClusterDbRevisionResultTypeDef = TypedDict(
    "ModifyClusterDbRevisionResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterIamRolesMessageRequestTypeDef = TypedDict(
    "_RequiredModifyClusterIamRolesMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterIamRolesMessageRequestTypeDef = TypedDict(
    "_OptionalModifyClusterIamRolesMessageRequestTypeDef",
    {
        "AddIamRoles": List[str],
        "RemoveIamRoles": List[str],
    },
    total=False,
)

class ModifyClusterIamRolesMessageRequestTypeDef(
    _RequiredModifyClusterIamRolesMessageRequestTypeDef,
    _OptionalModifyClusterIamRolesMessageRequestTypeDef,
):
    pass

ModifyClusterIamRolesResultTypeDef = TypedDict(
    "ModifyClusterIamRolesResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterMaintenanceMessageRequestTypeDef = TypedDict(
    "_RequiredModifyClusterMaintenanceMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterMaintenanceMessageRequestTypeDef = TypedDict(
    "_OptionalModifyClusterMaintenanceMessageRequestTypeDef",
    {
        "DeferMaintenance": bool,
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": Union[datetime, str],
        "DeferMaintenanceEndTime": Union[datetime, str],
        "DeferMaintenanceDuration": int,
    },
    total=False,
)

class ModifyClusterMaintenanceMessageRequestTypeDef(
    _RequiredModifyClusterMaintenanceMessageRequestTypeDef,
    _OptionalModifyClusterMaintenanceMessageRequestTypeDef,
):
    pass

ModifyClusterMaintenanceResultTypeDef = TypedDict(
    "ModifyClusterMaintenanceResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterMessageRequestTypeDef = TypedDict(
    "_RequiredModifyClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterMessageRequestTypeDef = TypedDict(
    "_OptionalModifyClusterMessageRequestTypeDef",
    {
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "MasterUserPassword": str,
        "ClusterParameterGroupName": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "PreferredMaintenanceWindow": str,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "NewClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "ElasticIp": str,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "AvailabilityZoneRelocation": bool,
        "AvailabilityZone": str,
        "Port": int,
    },
    total=False,
)

class ModifyClusterMessageRequestTypeDef(
    _RequiredModifyClusterMessageRequestTypeDef, _OptionalModifyClusterMessageRequestTypeDef
):
    pass

ModifyClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

ModifyClusterResultTypeDef = TypedDict(
    "ModifyClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredModifyClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
    },
)
_OptionalModifyClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalModifyClusterSnapshotMessageRequestTypeDef",
    {
        "ManualSnapshotRetentionPeriod": int,
        "Force": bool,
    },
    total=False,
)

class ModifyClusterSnapshotMessageRequestTypeDef(
    _RequiredModifyClusterSnapshotMessageRequestTypeDef,
    _OptionalModifyClusterSnapshotMessageRequestTypeDef,
):
    pass

ModifyClusterSnapshotResultTypeDef = TypedDict(
    "ModifyClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "_RequiredModifyClusterSnapshotScheduleMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "_OptionalModifyClusterSnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleIdentifier": str,
        "DisassociateSchedule": bool,
    },
    total=False,
)

class ModifyClusterSnapshotScheduleMessageRequestTypeDef(
    _RequiredModifyClusterSnapshotScheduleMessageRequestTypeDef,
    _OptionalModifyClusterSnapshotScheduleMessageRequestTypeDef,
):
    pass

_RequiredModifyClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyClusterSubnetGroupMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyClusterSubnetGroupMessageRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ModifyClusterSubnetGroupMessageRequestTypeDef(
    _RequiredModifyClusterSubnetGroupMessageRequestTypeDef,
    _OptionalModifyClusterSubnetGroupMessageRequestTypeDef,
):
    pass

ModifyClusterSubnetGroupResultTypeDef = TypedDict(
    "ModifyClusterSubnetGroupResultTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEndpointAccessMessageRequestTypeDef = TypedDict(
    "_RequiredModifyEndpointAccessMessageRequestTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalModifyEndpointAccessMessageRequestTypeDef = TypedDict(
    "_OptionalModifyEndpointAccessMessageRequestTypeDef",
    {
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)

class ModifyEndpointAccessMessageRequestTypeDef(
    _RequiredModifyEndpointAccessMessageRequestTypeDef,
    _OptionalModifyEndpointAccessMessageRequestTypeDef,
):
    pass

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
        "SourceIds": List[str],
        "EventCategories": List[str],
        "Severity": str,
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

_RequiredModifyScheduledActionMessageRequestTypeDef = TypedDict(
    "_RequiredModifyScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)
_OptionalModifyScheduledActionMessageRequestTypeDef = TypedDict(
    "_OptionalModifyScheduledActionMessageRequestTypeDef",
    {
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Enable": bool,
    },
    total=False,
)

class ModifyScheduledActionMessageRequestTypeDef(
    _RequiredModifyScheduledActionMessageRequestTypeDef,
    _OptionalModifyScheduledActionMessageRequestTypeDef,
):
    pass

_RequiredModifySnapshotCopyRetentionPeriodMessageRequestTypeDef = TypedDict(
    "_RequiredModifySnapshotCopyRetentionPeriodMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "RetentionPeriod": int,
    },
)
_OptionalModifySnapshotCopyRetentionPeriodMessageRequestTypeDef = TypedDict(
    "_OptionalModifySnapshotCopyRetentionPeriodMessageRequestTypeDef",
    {
        "Manual": bool,
    },
    total=False,
)

class ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef(
    _RequiredModifySnapshotCopyRetentionPeriodMessageRequestTypeDef,
    _OptionalModifySnapshotCopyRetentionPeriodMessageRequestTypeDef,
):
    pass

ModifySnapshotCopyRetentionPeriodResultTypeDef = TypedDict(
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySnapshotScheduleMessageRequestTypeDef = TypedDict(
    "ModifySnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleIdentifier": str,
        "ScheduleDefinitions": List[str],
    },
)

_RequiredModifyUsageLimitMessageRequestTypeDef = TypedDict(
    "_RequiredModifyUsageLimitMessageRequestTypeDef",
    {
        "UsageLimitId": str,
    },
)
_OptionalModifyUsageLimitMessageRequestTypeDef = TypedDict(
    "_OptionalModifyUsageLimitMessageRequestTypeDef",
    {
        "Amount": int,
        "BreachAction": UsageLimitBreachActionType,
    },
    total=False,
)

class ModifyUsageLimitMessageRequestTypeDef(
    _RequiredModifyUsageLimitMessageRequestTypeDef, _OptionalModifyUsageLimitMessageRequestTypeDef
):
    pass

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "NetworkInterfaceId": str,
        "SubnetId": str,
        "PrivateIpAddress": str,
        "AvailabilityZone": str,
    },
    total=False,
)

NodeConfigurationOptionTypeDef = TypedDict(
    "NodeConfigurationOptionTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": ModeType,
    },
    total=False,
)

NodeConfigurationOptionsFilterTypeDef = TypedDict(
    "NodeConfigurationOptionsFilterTypeDef",
    {
        "Name": NodeConfigurationOptionsFilterNameType,
        "Operator": OperatorTypeType,
        "Values": List[str],
    },
    total=False,
)

NodeConfigurationOptionsMessageTypeDef = TypedDict(
    "NodeConfigurationOptionsMessageTypeDef",
    {
        "NodeConfigurationOptionList": List["NodeConfigurationOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderableClusterOptionTypeDef = TypedDict(
    "OrderableClusterOptionTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
    },
    total=False,
)

OrderableClusterOptionsMessageTypeDef = TypedDict(
    "OrderableClusterOptionsMessageTypeDef",
    {
        "OrderableClusterOptions": List["OrderableClusterOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": ParameterApplyTypeType,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

PartnerIntegrationInfoTypeDef = TypedDict(
    "PartnerIntegrationInfoTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
        "Status": PartnerIntegrationStatusType,
        "StatusMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

PartnerIntegrationInputMessageRequestTypeDef = TypedDict(
    "PartnerIntegrationInputMessageRequestTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": str,
        "PartnerName": str,
    },
)

PartnerIntegrationOutputMessageTypeDef = TypedDict(
    "PartnerIntegrationOutputMessageTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PauseClusterMessageRequestTypeDef = TypedDict(
    "PauseClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

PauseClusterMessageTypeDef = TypedDict(
    "PauseClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

PauseClusterResultTypeDef = TypedDict(
    "PauseClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

_RequiredPurchaseReservedNodeOfferingMessageRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedNodeOfferingMessageRequestTypeDef",
    {
        "ReservedNodeOfferingId": str,
    },
)
_OptionalPurchaseReservedNodeOfferingMessageRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedNodeOfferingMessageRequestTypeDef",
    {
        "NodeCount": int,
    },
    total=False,
)

class PurchaseReservedNodeOfferingMessageRequestTypeDef(
    _RequiredPurchaseReservedNodeOfferingMessageRequestTypeDef,
    _OptionalPurchaseReservedNodeOfferingMessageRequestTypeDef,
):
    pass

PurchaseReservedNodeOfferingResultTypeDef = TypedDict(
    "PurchaseReservedNodeOfferingResultTypeDef",
    {
        "ReservedNode": "ReservedNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootClusterMessageRequestTypeDef = TypedDict(
    "RebootClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

RebootClusterResultTypeDef = TypedDict(
    "RebootClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RejectDataShareMessageRequestTypeDef = TypedDict(
    "RejectDataShareMessageRequestTypeDef",
    {
        "DataShareArn": str,
    },
)

ReservedNodeOfferingTypeDef = TypedDict(
    "ReservedNodeOfferingTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedNodeOfferingType": ReservedNodeOfferingTypeType,
    },
    total=False,
)

ReservedNodeOfferingsMessageTypeDef = TypedDict(
    "ReservedNodeOfferingsMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedNodeTypeDef = TypedDict(
    "ReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedNodeOfferingType": ReservedNodeOfferingTypeType,
    },
    total=False,
)

ReservedNodesMessageTypeDef = TypedDict(
    "ReservedNodesMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodes": List["ReservedNodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredResetClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalResetClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalResetClusterParameterGroupMessageRequestTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

class ResetClusterParameterGroupMessageRequestTypeDef(
    _RequiredResetClusterParameterGroupMessageRequestTypeDef,
    _OptionalResetClusterParameterGroupMessageRequestTypeDef,
):
    pass

_RequiredResizeClusterMessageRequestTypeDef = TypedDict(
    "_RequiredResizeClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalResizeClusterMessageRequestTypeDef = TypedDict(
    "_OptionalResizeClusterMessageRequestTypeDef",
    {
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)

class ResizeClusterMessageRequestTypeDef(
    _RequiredResizeClusterMessageRequestTypeDef, _OptionalResizeClusterMessageRequestTypeDef
):
    pass

_RequiredResizeClusterMessageTypeDef = TypedDict(
    "_RequiredResizeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalResizeClusterMessageTypeDef = TypedDict(
    "_OptionalResizeClusterMessageTypeDef",
    {
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)

class ResizeClusterMessageTypeDef(
    _RequiredResizeClusterMessageTypeDef, _OptionalResizeClusterMessageTypeDef
):
    pass

ResizeClusterResultTypeDef = TypedDict(
    "ResizeClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResizeInfoTypeDef = TypedDict(
    "ResizeInfoTypeDef",
    {
        "ResizeType": str,
        "AllowCancelResize": bool,
    },
    total=False,
)

ResizeProgressMessageTypeDef = TypedDict(
    "ResizeProgressMessageTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredRestoreFromClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreFromClusterSnapshotMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
    },
)
_OptionalRestoreFromClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreFromClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotClusterIdentifier": str,
        "Port": int,
        "AvailabilityZone": str,
        "AllowVersionUpgrade": bool,
        "ClusterSubnetGroupName": str,
        "PubliclyAccessible": bool,
        "OwnerAccount": str,
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "ElasticIp": str,
        "ClusterParameterGroupName": str,
        "ClusterSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "KmsKeyId": str,
        "NodeType": str,
        "EnhancedVpcRouting": bool,
        "AdditionalInfo": str,
        "IamRoles": List[str],
        "MaintenanceTrackName": str,
        "SnapshotScheduleIdentifier": str,
        "NumberOfNodes": int,
        "AvailabilityZoneRelocation": bool,
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)

class RestoreFromClusterSnapshotMessageRequestTypeDef(
    _RequiredRestoreFromClusterSnapshotMessageRequestTypeDef,
    _OptionalRestoreFromClusterSnapshotMessageRequestTypeDef,
):
    pass

RestoreFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreFromClusterSnapshotResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreStatusTypeDef = TypedDict(
    "RestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

_RequiredRestoreTableFromClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreTableFromClusterSnapshotMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceTableName": str,
        "NewTableName": str,
    },
)
_OptionalRestoreTableFromClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreTableFromClusterSnapshotMessageRequestTypeDef",
    {
        "SourceSchemaName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "EnableCaseSensitiveIdentifier": bool,
    },
    total=False,
)

class RestoreTableFromClusterSnapshotMessageRequestTypeDef(
    _RequiredRestoreTableFromClusterSnapshotMessageRequestTypeDef,
    _OptionalRestoreTableFromClusterSnapshotMessageRequestTypeDef,
):
    pass

RestoreTableFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreTableFromClusterSnapshotResultTypeDef",
    {
        "TableRestoreStatus": "TableRestoreStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResumeClusterMessageRequestTypeDef = TypedDict(
    "ResumeClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ResumeClusterMessageTypeDef = TypedDict(
    "ResumeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ResumeClusterResultTypeDef = TypedDict(
    "ResumeClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevisionTargetTypeDef = TypedDict(
    "RevisionTargetTypeDef",
    {
        "DatabaseRevision": str,
        "Description": str,
        "DatabaseRevisionReleaseDate": datetime,
    },
    total=False,
)

_RequiredRevokeClusterSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_RequiredRevokeClusterSecurityGroupIngressMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
)
_OptionalRevokeClusterSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "_OptionalRevokeClusterSecurityGroupIngressMessageRequestTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

class RevokeClusterSecurityGroupIngressMessageRequestTypeDef(
    _RequiredRevokeClusterSecurityGroupIngressMessageRequestTypeDef,
    _OptionalRevokeClusterSecurityGroupIngressMessageRequestTypeDef,
):
    pass

RevokeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeEndpointAccessMessageRequestTypeDef = TypedDict(
    "RevokeEndpointAccessMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Account": str,
        "VpcIds": List[str],
        "Force": bool,
    },
    total=False,
)

_RequiredRevokeSnapshotAccessMessageRequestTypeDef = TypedDict(
    "_RequiredRevokeSnapshotAccessMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "AccountWithRestoreAccess": str,
    },
)
_OptionalRevokeSnapshotAccessMessageRequestTypeDef = TypedDict(
    "_OptionalRevokeSnapshotAccessMessageRequestTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)

class RevokeSnapshotAccessMessageRequestTypeDef(
    _RequiredRevokeSnapshotAccessMessageRequestTypeDef,
    _OptionalRevokeSnapshotAccessMessageRequestTypeDef,
):
    pass

RevokeSnapshotAccessResultTypeDef = TypedDict(
    "RevokeSnapshotAccessResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotateEncryptionKeyMessageRequestTypeDef = TypedDict(
    "RotateEncryptionKeyMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

RotateEncryptionKeyResultTypeDef = TypedDict(
    "RotateEncryptionKeyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduledActionFilterTypeDef = TypedDict(
    "ScheduledActionFilterTypeDef",
    {
        "Name": ScheduledActionFilterNameType,
        "Values": List[str],
    },
)

ScheduledActionResponseMetadataTypeDef = TypedDict(
    "ScheduledActionResponseMetadataTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": ScheduledActionStateType,
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": ScheduledActionStateType,
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ScheduledActionTypeTypeDef = TypedDict(
    "ScheduledActionTypeTypeDef",
    {
        "ResizeCluster": "ResizeClusterMessageTypeDef",
        "PauseCluster": "PauseClusterMessageTypeDef",
        "ResumeCluster": "ResumeClusterMessageTypeDef",
    },
    total=False,
)

ScheduledActionsMessageTypeDef = TypedDict(
    "ScheduledActionsMessageTypeDef",
    {
        "Marker": str,
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotCopyGrantMessageTypeDef = TypedDict(
    "SnapshotCopyGrantMessageTypeDef",
    {
        "Marker": str,
        "SnapshotCopyGrants": List["SnapshotCopyGrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotCopyGrantTypeDef = TypedDict(
    "SnapshotCopyGrantTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SnapshotErrorMessageTypeDef = TypedDict(
    "SnapshotErrorMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

SnapshotMessageTypeDef = TypedDict(
    "SnapshotMessageTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotScheduleResponseMetadataTypeDef = TypedDict(
    "SnapshotScheduleResponseMetadataTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List["ClusterAssociatedToScheduleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotScheduleTypeDef = TypedDict(
    "SnapshotScheduleTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List["ClusterAssociatedToScheduleTypeDef"],
    },
    total=False,
)

_RequiredSnapshotSortingEntityTypeDef = TypedDict(
    "_RequiredSnapshotSortingEntityTypeDef",
    {
        "Attribute": SnapshotAttributeToSortByType,
    },
)
_OptionalSnapshotSortingEntityTypeDef = TypedDict(
    "_OptionalSnapshotSortingEntityTypeDef",
    {
        "SortOrder": SortByOrderType,
    },
    total=False,
)

class SnapshotSortingEntityTypeDef(
    _RequiredSnapshotSortingEntityTypeDef, _OptionalSnapshotSortingEntityTypeDef
):
    pass

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "EngineFullVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List["AccountWithRestoreAccessTypeDef"],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List["TagTypeDef"],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
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

SupportedOperationTypeDef = TypedDict(
    "SupportedOperationTypeDef",
    {
        "OperationName": str,
    },
    total=False,
)

SupportedPlatformTypeDef = TypedDict(
    "SupportedPlatformTypeDef",
    {
        "Name": str,
    },
    total=False,
)

TableRestoreStatusMessageTypeDef = TypedDict(
    "TableRestoreStatusMessageTypeDef",
    {
        "TableRestoreStatusDetails": List["TableRestoreStatusTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableRestoreStatusTypeDef = TypedDict(
    "TableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": TableRestoreStatusTypeType,
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TaggedResourceListMessageTypeDef = TypedDict(
    "TaggedResourceListMessageTypeDef",
    {
        "TaggedResources": List["TaggedResourceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TaggedResourceTypeDef = TypedDict(
    "TaggedResourceTypeDef",
    {
        "Tag": "TagTypeDef",
        "ResourceName": str,
        "ResourceType": str,
    },
    total=False,
)

TrackListMessageTypeDef = TypedDict(
    "TrackListMessageTypeDef",
    {
        "MaintenanceTracks": List["MaintenanceTrackTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePartnerStatusInputMessageRequestTypeDef = TypedDict(
    "_RequiredUpdatePartnerStatusInputMessageRequestTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": str,
        "PartnerName": str,
        "Status": PartnerIntegrationStatusType,
    },
)
_OptionalUpdatePartnerStatusInputMessageRequestTypeDef = TypedDict(
    "_OptionalUpdatePartnerStatusInputMessageRequestTypeDef",
    {
        "StatusMessage": str,
    },
    total=False,
)

class UpdatePartnerStatusInputMessageRequestTypeDef(
    _RequiredUpdatePartnerStatusInputMessageRequestTypeDef,
    _OptionalUpdatePartnerStatusInputMessageRequestTypeDef,
):
    pass

UpdateTargetTypeDef = TypedDict(
    "UpdateTargetTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List["SupportedOperationTypeDef"],
    },
    total=False,
)

UsageLimitListTypeDef = TypedDict(
    "UsageLimitListTypeDef",
    {
        "UsageLimits": List["UsageLimitTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageLimitResponseMetadataTypeDef = TypedDict(
    "UsageLimitResponseMetadataTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageLimitTypeDef = TypedDict(
    "UsageLimitTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcId": str,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
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
