"""
Type annotations for redshift service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeInputMessageTypeDef

    data: AcceptReservedNodeExchangeInputMessageTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionTypeType,
    AquaConfigurationStatusType,
    AquaStatusType,
    AuthorizationStatusType,
    DataShareStatusForConsumerType,
    DataShareStatusForProducerType,
    DataShareStatusType,
    DescribeIntegrationsFilterNameType,
    ImpactRankingTypeType,
    LogDestinationTypeType,
    ModeType,
    NamespaceRegistrationStatusType,
    NodeConfigurationOptionsFilterNameType,
    OperatorTypeType,
    ParameterApplyTypeType,
    PartnerIntegrationStatusType,
    RecommendedActionTypeType,
    ReservedNodeExchangeActionTypeType,
    ReservedNodeExchangeStatusTypeType,
    ReservedNodeOfferingTypeType,
    ScheduledActionFilterNameType,
    ScheduledActionStateType,
    ScheduledActionTypeValuesType,
    ScheduleStateType,
    ServiceAuthorizationType,
    SnapshotAttributeToSortByType,
    SortByOrderType,
    SourceTypeType,
    TableRestoreStatusTypeType,
    UsageLimitBreachActionType,
    UsageLimitFeatureTypeType,
    UsageLimitLimitTypeType,
    UsageLimitPeriodType,
    ZeroETLIntegrationStatusType,
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
    "AcceptReservedNodeExchangeInputMessageTypeDef",
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    "AccountAttributeListTypeDef",
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AquaConfigurationTypeDef",
    "AssociateDataShareConsumerMessageTypeDef",
    "AssociationTypeDef",
    "AttributeValueTargetTypeDef",
    "AuthenticationProfileTypeDef",
    "AuthorizeClusterSecurityGroupIngressMessageTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    "AuthorizeDataShareMessageTypeDef",
    "AuthorizeEndpointAccessMessageTypeDef",
    "AuthorizeSnapshotAccessMessageTypeDef",
    "AuthorizeSnapshotAccessResultTypeDef",
    "AuthorizedTokenIssuerOutputTypeDef",
    "AuthorizedTokenIssuerTypeDef",
    "AuthorizedTokenIssuerUnionTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchDeleteClusterSnapshotsRequestTypeDef",
    "BatchDeleteClusterSnapshotsResultTypeDef",
    "BatchModifyClusterSnapshotsMessageTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    "CancelResizeMessageTypeDef",
    "CertificateAssociationTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterCredentialsTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ClusterExtendedCredentialsTypeDef",
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
    "CopyClusterSnapshotMessageTypeDef",
    "CopyClusterSnapshotResultTypeDef",
    "CreateAuthenticationProfileMessageTypeDef",
    "CreateAuthenticationProfileResultTypeDef",
    "CreateClusterMessageTypeDef",
    "CreateClusterParameterGroupMessageTypeDef",
    "CreateClusterParameterGroupResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateClusterSecurityGroupMessageTypeDef",
    "CreateClusterSecurityGroupResultTypeDef",
    "CreateClusterSnapshotMessageTypeDef",
    "CreateClusterSnapshotResultTypeDef",
    "CreateClusterSubnetGroupMessageTypeDef",
    "CreateClusterSubnetGroupResultTypeDef",
    "CreateCustomDomainAssociationMessageTypeDef",
    "CreateCustomDomainAssociationResultTypeDef",
    "CreateEndpointAccessMessageTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateHsmClientCertificateMessageTypeDef",
    "CreateHsmClientCertificateResultTypeDef",
    "CreateHsmConfigurationMessageTypeDef",
    "CreateHsmConfigurationResultTypeDef",
    "CreateIntegrationMessageTypeDef",
    "CreateRedshiftIdcApplicationMessageTypeDef",
    "CreateRedshiftIdcApplicationResultTypeDef",
    "CreateScheduledActionMessageTypeDef",
    "CreateSnapshotCopyGrantMessageTypeDef",
    "CreateSnapshotCopyGrantResultTypeDef",
    "CreateSnapshotScheduleMessageTypeDef",
    "CreateTagsMessageTypeDef",
    "CreateUsageLimitMessageTypeDef",
    "CustomDomainAssociationsMessageTypeDef",
    "CustomerStorageMessageTypeDef",
    "DataShareAssociationTypeDef",
    "DataShareResponseTypeDef",
    "DataShareTypeDef",
    "DataTransferProgressTypeDef",
    "DeauthorizeDataShareMessageTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "DeleteAuthenticationProfileMessageTypeDef",
    "DeleteAuthenticationProfileResultTypeDef",
    "DeleteClusterMessageTypeDef",
    "DeleteClusterParameterGroupMessageTypeDef",
    "DeleteClusterResultTypeDef",
    "DeleteClusterSecurityGroupMessageTypeDef",
    "DeleteClusterSnapshotMessageRequestTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultTypeDef",
    "DeleteClusterSubnetGroupMessageTypeDef",
    "DeleteCustomDomainAssociationMessageTypeDef",
    "DeleteEndpointAccessMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteHsmClientCertificateMessageTypeDef",
    "DeleteHsmConfigurationMessageTypeDef",
    "DeleteIntegrationMessageTypeDef",
    "DeleteRedshiftIdcApplicationMessageTypeDef",
    "DeleteResourcePolicyMessageTypeDef",
    "DeleteScheduledActionMessageTypeDef",
    "DeleteSnapshotCopyGrantMessageTypeDef",
    "DeleteSnapshotScheduleMessageTypeDef",
    "DeleteTagsMessageTypeDef",
    "DeleteUsageLimitMessageTypeDef",
    "DeregisterNamespaceInputMessageTypeDef",
    "DeregisterNamespaceOutputMessageTypeDef",
    "DescribeAccountAttributesMessageTypeDef",
    "DescribeAuthenticationProfilesMessageTypeDef",
    "DescribeAuthenticationProfilesResultTypeDef",
    "DescribeClusterDbRevisionsMessagePaginateTypeDef",
    "DescribeClusterDbRevisionsMessageTypeDef",
    "DescribeClusterParameterGroupsMessagePaginateTypeDef",
    "DescribeClusterParameterGroupsMessageTypeDef",
    "DescribeClusterParametersMessagePaginateTypeDef",
    "DescribeClusterParametersMessageTypeDef",
    "DescribeClusterSecurityGroupsMessagePaginateTypeDef",
    "DescribeClusterSecurityGroupsMessageTypeDef",
    "DescribeClusterSnapshotsMessagePaginateTypeDef",
    "DescribeClusterSnapshotsMessageTypeDef",
    "DescribeClusterSnapshotsMessageWaitTypeDef",
    "DescribeClusterSubnetGroupsMessagePaginateTypeDef",
    "DescribeClusterSubnetGroupsMessageTypeDef",
    "DescribeClusterTracksMessagePaginateTypeDef",
    "DescribeClusterTracksMessageTypeDef",
    "DescribeClusterVersionsMessagePaginateTypeDef",
    "DescribeClusterVersionsMessageTypeDef",
    "DescribeClustersMessagePaginateTypeDef",
    "DescribeClustersMessageTypeDef",
    "DescribeClustersMessageWaitExtraExtraTypeDef",
    "DescribeClustersMessageWaitExtraTypeDef",
    "DescribeClustersMessageWaitTypeDef",
    "DescribeCustomDomainAssociationsMessagePaginateTypeDef",
    "DescribeCustomDomainAssociationsMessageTypeDef",
    "DescribeDataSharesForConsumerMessagePaginateTypeDef",
    "DescribeDataSharesForConsumerMessageTypeDef",
    "DescribeDataSharesForConsumerResultTypeDef",
    "DescribeDataSharesForProducerMessagePaginateTypeDef",
    "DescribeDataSharesForProducerMessageTypeDef",
    "DescribeDataSharesForProducerResultTypeDef",
    "DescribeDataSharesMessagePaginateTypeDef",
    "DescribeDataSharesMessageTypeDef",
    "DescribeDataSharesResultTypeDef",
    "DescribeDefaultClusterParametersMessagePaginateTypeDef",
    "DescribeDefaultClusterParametersMessageTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "DescribeEndpointAccessMessagePaginateTypeDef",
    "DescribeEndpointAccessMessageTypeDef",
    "DescribeEndpointAuthorizationMessagePaginateTypeDef",
    "DescribeEndpointAuthorizationMessageTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventSubscriptionsMessagePaginateTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventsMessagePaginateTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeHsmClientCertificatesMessagePaginateTypeDef",
    "DescribeHsmClientCertificatesMessageTypeDef",
    "DescribeHsmConfigurationsMessagePaginateTypeDef",
    "DescribeHsmConfigurationsMessageTypeDef",
    "DescribeInboundIntegrationsMessagePaginateTypeDef",
    "DescribeInboundIntegrationsMessageTypeDef",
    "DescribeIntegrationsFilterTypeDef",
    "DescribeIntegrationsMessagePaginateTypeDef",
    "DescribeIntegrationsMessageTypeDef",
    "DescribeLoggingStatusMessageTypeDef",
    "DescribeNodeConfigurationOptionsMessagePaginateTypeDef",
    "DescribeNodeConfigurationOptionsMessageTypeDef",
    "DescribeOrderableClusterOptionsMessagePaginateTypeDef",
    "DescribeOrderableClusterOptionsMessageTypeDef",
    "DescribePartnersInputMessageTypeDef",
    "DescribePartnersOutputMessageTypeDef",
    "DescribeRedshiftIdcApplicationsMessagePaginateTypeDef",
    "DescribeRedshiftIdcApplicationsMessageTypeDef",
    "DescribeRedshiftIdcApplicationsResultTypeDef",
    "DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef",
    "DescribeReservedNodeExchangeStatusInputMessageTypeDef",
    "DescribeReservedNodeExchangeStatusOutputMessageTypeDef",
    "DescribeReservedNodeOfferingsMessagePaginateTypeDef",
    "DescribeReservedNodeOfferingsMessageTypeDef",
    "DescribeReservedNodesMessagePaginateTypeDef",
    "DescribeReservedNodesMessageTypeDef",
    "DescribeResizeMessageTypeDef",
    "DescribeScheduledActionsMessagePaginateTypeDef",
    "DescribeScheduledActionsMessageTypeDef",
    "DescribeSnapshotCopyGrantsMessagePaginateTypeDef",
    "DescribeSnapshotCopyGrantsMessageTypeDef",
    "DescribeSnapshotSchedulesMessagePaginateTypeDef",
    "DescribeSnapshotSchedulesMessageTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "DescribeTableRestoreStatusMessagePaginateTypeDef",
    "DescribeTableRestoreStatusMessageTypeDef",
    "DescribeTagsMessagePaginateTypeDef",
    "DescribeTagsMessageTypeDef",
    "DescribeUsageLimitsMessagePaginateTypeDef",
    "DescribeUsageLimitsMessageTypeDef",
    "DisableLoggingMessageTypeDef",
    "DisableSnapshotCopyMessageTypeDef",
    "DisableSnapshotCopyResultTypeDef",
    "DisassociateDataShareConsumerMessageTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableLoggingMessageTypeDef",
    "EnableSnapshotCopyMessageTypeDef",
    "EnableSnapshotCopyResultTypeDef",
    "EndpointAccessListTypeDef",
    "EndpointAccessResponseTypeDef",
    "EndpointAccessTypeDef",
    "EndpointAuthorizationListTypeDef",
    "EndpointAuthorizationResponseTypeDef",
    "EndpointAuthorizationTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverPrimaryComputeInputMessageTypeDef",
    "FailoverPrimaryComputeResultTypeDef",
    "GetClusterCredentialsMessageTypeDef",
    "GetClusterCredentialsWithIAMMessageTypeDef",
    "GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef",
    "GetReservedNodeExchangeConfigurationOptionsInputMessageTypeDef",
    "GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef",
    "GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef",
    "GetReservedNodeExchangeOfferingsInputMessageTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "GetResourcePolicyMessageTypeDef",
    "GetResourcePolicyResultTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationMessageTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "InboundIntegrationTypeDef",
    "InboundIntegrationsMessageTypeDef",
    "IntegrationErrorTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "IntegrationsMessageTypeDef",
    "LakeFormationQueryTypeDef",
    "LakeFormationScopeUnionTypeDef",
    "ListRecommendationsMessagePaginateTypeDef",
    "ListRecommendationsMessageTypeDef",
    "ListRecommendationsResultTypeDef",
    "LoggingStatusTypeDef",
    "MaintenanceTrackTypeDef",
    "ModifyAquaInputMessageTypeDef",
    "ModifyAquaOutputMessageTypeDef",
    "ModifyAuthenticationProfileMessageTypeDef",
    "ModifyAuthenticationProfileResultTypeDef",
    "ModifyClusterDbRevisionMessageTypeDef",
    "ModifyClusterDbRevisionResultTypeDef",
    "ModifyClusterIamRolesMessageTypeDef",
    "ModifyClusterIamRolesResultTypeDef",
    "ModifyClusterMaintenanceMessageTypeDef",
    "ModifyClusterMaintenanceResultTypeDef",
    "ModifyClusterMessageTypeDef",
    "ModifyClusterParameterGroupMessageTypeDef",
    "ModifyClusterResultTypeDef",
    "ModifyClusterSnapshotMessageTypeDef",
    "ModifyClusterSnapshotResultTypeDef",
    "ModifyClusterSnapshotScheduleMessageTypeDef",
    "ModifyClusterSubnetGroupMessageTypeDef",
    "ModifyClusterSubnetGroupResultTypeDef",
    "ModifyCustomDomainAssociationMessageTypeDef",
    "ModifyCustomDomainAssociationResultTypeDef",
    "ModifyEndpointAccessMessageTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyIntegrationMessageTypeDef",
    "ModifyRedshiftIdcApplicationMessageTypeDef",
    "ModifyRedshiftIdcApplicationResultTypeDef",
    "ModifyScheduledActionMessageTypeDef",
    "ModifySnapshotCopyRetentionPeriodMessageTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    "ModifySnapshotScheduleMessageTypeDef",
    "ModifyUsageLimitMessageTypeDef",
    "NamespaceIdentifierUnionTypeDef",
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
    "PartnerIntegrationInputMessageTypeDef",
    "PartnerIntegrationOutputMessageTypeDef",
    "PauseClusterMessageRequestTypeDef",
    "PauseClusterMessageTypeDef",
    "PauseClusterResultTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProvisionedIdentifierTypeDef",
    "PurchaseReservedNodeOfferingMessageTypeDef",
    "PurchaseReservedNodeOfferingResultTypeDef",
    "PutResourcePolicyMessageTypeDef",
    "PutResourcePolicyResultTypeDef",
    "ReadWriteAccessTypeDef",
    "RebootClusterMessageTypeDef",
    "RebootClusterResultTypeDef",
    "RecommendationTypeDef",
    "RecommendedActionTypeDef",
    "RecurringChargeTypeDef",
    "RedshiftIdcApplicationTypeDef",
    "ReferenceLinkTypeDef",
    "RegisterNamespaceInputMessageTypeDef",
    "RegisterNamespaceOutputMessageTypeDef",
    "RejectDataShareMessageTypeDef",
    "ReservedNodeConfigurationOptionTypeDef",
    "ReservedNodeExchangeStatusTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageTypeDef",
    "ResetClusterParameterGroupMessageTypeDef",
    "ResizeClusterMessageRequestTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeClusterResultTypeDef",
    "ResizeInfoTypeDef",
    "ResizeProgressMessageTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromClusterSnapshotMessageTypeDef",
    "RestoreFromClusterSnapshotResultTypeDef",
    "RestoreStatusTypeDef",
    "RestoreTableFromClusterSnapshotMessageTypeDef",
    "RestoreTableFromClusterSnapshotResultTypeDef",
    "ResumeClusterMessageRequestTypeDef",
    "ResumeClusterMessageTypeDef",
    "ResumeClusterResultTypeDef",
    "RevisionTargetTypeDef",
    "RevokeClusterSecurityGroupIngressMessageTypeDef",
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    "RevokeEndpointAccessMessageTypeDef",
    "RevokeSnapshotAccessMessageTypeDef",
    "RevokeSnapshotAccessResultTypeDef",
    "RotateEncryptionKeyMessageTypeDef",
    "RotateEncryptionKeyResultTypeDef",
    "S3AccessGrantsScopeUnionTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionResponseTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SecondaryClusterInfoTypeDef",
    "ServerlessIdentifierTypeDef",
    "ServiceIntegrationsUnionOutputTypeDef",
    "ServiceIntegrationsUnionTypeDef",
    "ServiceIntegrationsUnionUnionTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotScheduleResponseTypeDef",
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
    "TimestampTypeDef",
    "TrackListMessageTypeDef",
    "UpdatePartnerStatusInputMessageTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitListTypeDef",
    "UsageLimitResponseTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

class AcceptReservedNodeExchangeInputMessageTypeDef(TypedDict):
    ReservedNodeId: str
    TargetReservedNodeOfferingId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AttributeValueTargetTypeDef(TypedDict):
    AttributeValue: NotRequired[str]

class AccountWithRestoreAccessTypeDef(TypedDict):
    AccountId: NotRequired[str]
    AccountAlias: NotRequired[str]

class AquaConfigurationTypeDef(TypedDict):
    AquaStatus: NotRequired[AquaStatusType]
    AquaConfigurationStatus: NotRequired[AquaConfigurationStatusType]

class AssociateDataShareConsumerMessageTypeDef(TypedDict):
    DataShareArn: str
    AssociateEntireAccount: NotRequired[bool]
    ConsumerArn: NotRequired[str]
    ConsumerRegion: NotRequired[str]
    AllowWrites: NotRequired[bool]

class CertificateAssociationTypeDef(TypedDict):
    CustomDomainName: NotRequired[str]
    ClusterIdentifier: NotRequired[str]

class AuthenticationProfileTypeDef(TypedDict):
    AuthenticationProfileName: NotRequired[str]
    AuthenticationProfileContent: NotRequired[str]

class AuthorizeClusterSecurityGroupIngressMessageTypeDef(TypedDict):
    ClusterSecurityGroupName: str
    CIDRIP: NotRequired[str]
    EC2SecurityGroupName: NotRequired[str]
    EC2SecurityGroupOwnerId: NotRequired[str]

class AuthorizeDataShareMessageTypeDef(TypedDict):
    DataShareArn: str
    ConsumerIdentifier: str
    AllowWrites: NotRequired[bool]

class AuthorizeEndpointAccessMessageTypeDef(TypedDict):
    Account: str
    ClusterIdentifier: NotRequired[str]
    VpcIds: NotRequired[Sequence[str]]

class AuthorizeSnapshotAccessMessageTypeDef(TypedDict):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    SnapshotClusterIdentifier: NotRequired[str]

class AuthorizedTokenIssuerOutputTypeDef(TypedDict):
    TrustedTokenIssuerArn: NotRequired[str]
    AuthorizedAudiencesList: NotRequired[List[str]]

class AuthorizedTokenIssuerTypeDef(TypedDict):
    TrustedTokenIssuerArn: NotRequired[str]
    AuthorizedAudiencesList: NotRequired[Sequence[str]]

class SupportedPlatformTypeDef(TypedDict):
    Name: NotRequired[str]

class DeleteClusterSnapshotMessageTypeDef(TypedDict):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: NotRequired[str]

class SnapshotErrorMessageTypeDef(TypedDict):
    SnapshotIdentifier: NotRequired[str]
    SnapshotClusterIdentifier: NotRequired[str]
    FailureCode: NotRequired[str]
    FailureReason: NotRequired[str]

class BatchModifyClusterSnapshotsMessageTypeDef(TypedDict):
    SnapshotIdentifierList: Sequence[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    Force: NotRequired[bool]

class CancelResizeMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class ClusterAssociatedToScheduleTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    ScheduleAssociationState: NotRequired[ScheduleStateType]

class RevisionTargetTypeDef(TypedDict):
    DatabaseRevision: NotRequired[str]
    Description: NotRequired[str]
    DatabaseRevisionReleaseDate: NotRequired[datetime]

class ClusterIamRoleTypeDef(TypedDict):
    IamRoleArn: NotRequired[str]
    ApplyStatus: NotRequired[str]

class ClusterNodeTypeDef(TypedDict):
    NodeRole: NotRequired[str]
    PrivateIPAddress: NotRequired[str]
    PublicIPAddress: NotRequired[str]

class ParameterTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterValue: NotRequired[str]
    Description: NotRequired[str]
    Source: NotRequired[str]
    DataType: NotRequired[str]
    AllowedValues: NotRequired[str]
    ApplyType: NotRequired[ParameterApplyTypeType]
    IsModifiable: NotRequired[bool]
    MinimumEngineVersion: NotRequired[str]

class ClusterParameterStatusTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]
    ParameterApplyErrorDescription: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ClusterSecurityGroupMembershipTypeDef(TypedDict):
    ClusterSecurityGroupName: NotRequired[str]
    Status: NotRequired[str]

class ClusterSnapshotCopyStatusTypeDef(TypedDict):
    DestinationRegion: NotRequired[str]
    RetentionPeriod: NotRequired[int]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    SnapshotCopyGrantName: NotRequired[str]

class DataTransferProgressTypeDef(TypedDict):
    Status: NotRequired[str]
    CurrentRateInMegaBytesPerSecond: NotRequired[float]
    TotalDataInMegaBytes: NotRequired[int]
    DataTransferredInMegaBytes: NotRequired[int]
    EstimatedTimeToCompletionInSeconds: NotRequired[int]
    ElapsedTimeInSeconds: NotRequired[int]

class DeferredMaintenanceWindowTypeDef(TypedDict):
    DeferMaintenanceIdentifier: NotRequired[str]
    DeferMaintenanceStartTime: NotRequired[datetime]
    DeferMaintenanceEndTime: NotRequired[datetime]

class ElasticIpStatusTypeDef(TypedDict):
    ElasticIp: NotRequired[str]
    Status: NotRequired[str]

class HsmStatusTypeDef(TypedDict):
    HsmClientCertificateIdentifier: NotRequired[str]
    HsmConfigurationIdentifier: NotRequired[str]
    Status: NotRequired[str]

class PendingModifiedValuesTypeDef(TypedDict):
    MasterUserPassword: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    ClusterType: NotRequired[str]
    ClusterVersion: NotRequired[str]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    ClusterIdentifier: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    EnhancedVpcRouting: NotRequired[bool]
    MaintenanceTrackName: NotRequired[str]
    EncryptionType: NotRequired[str]

class ReservedNodeExchangeStatusTypeDef(TypedDict):
    ReservedNodeExchangeRequestId: NotRequired[str]
    Status: NotRequired[ReservedNodeExchangeStatusTypeType]
    RequestTime: NotRequired[datetime]
    SourceReservedNodeId: NotRequired[str]
    SourceReservedNodeType: NotRequired[str]
    SourceReservedNodeCount: NotRequired[int]
    TargetReservedNodeOfferingId: NotRequired[str]
    TargetReservedNodeType: NotRequired[str]
    TargetReservedNodeCount: NotRequired[int]

class ResizeInfoTypeDef(TypedDict):
    ResizeType: NotRequired[str]
    AllowCancelResize: NotRequired[bool]

class RestoreStatusTypeDef(TypedDict):
    Status: NotRequired[str]
    CurrentRestoreRateInMegaBytesPerSecond: NotRequired[float]
    SnapshotSizeInMegaBytes: NotRequired[int]
    ProgressInMegaBytes: NotRequired[int]
    ElapsedTimeInSeconds: NotRequired[int]
    EstimatedTimeToCompletionInSeconds: NotRequired[int]

class VpcSecurityGroupMembershipTypeDef(TypedDict):
    VpcSecurityGroupId: NotRequired[str]
    Status: NotRequired[str]

class ClusterVersionTypeDef(TypedDict):
    ClusterVersion: NotRequired[str]
    ClusterParameterGroupFamily: NotRequired[str]
    Description: NotRequired[str]

class CopyClusterSnapshotMessageTypeDef(TypedDict):
    SourceSnapshotIdentifier: str
    TargetSnapshotIdentifier: str
    SourceSnapshotClusterIdentifier: NotRequired[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]

class CreateAuthenticationProfileMessageTypeDef(TypedDict):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str

class CreateCustomDomainAssociationMessageTypeDef(TypedDict):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str

class CreateEndpointAccessMessageTypeDef(TypedDict):
    EndpointName: str
    SubnetGroupName: str
    ClusterIdentifier: NotRequired[str]
    ResourceOwner: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]

TimestampTypeDef = Union[datetime, str]

class DataShareAssociationTypeDef(TypedDict):
    ConsumerIdentifier: NotRequired[str]
    Status: NotRequired[DataShareStatusType]
    ConsumerRegion: NotRequired[str]
    CreatedDate: NotRequired[datetime]
    StatusChangeDate: NotRequired[datetime]
    ProducerAllowedWrites: NotRequired[bool]
    ConsumerAcceptedWrites: NotRequired[bool]

class DeauthorizeDataShareMessageTypeDef(TypedDict):
    DataShareArn: str
    ConsumerIdentifier: str

class DeleteAuthenticationProfileMessageTypeDef(TypedDict):
    AuthenticationProfileName: str

class DeleteClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    SkipFinalClusterSnapshot: NotRequired[bool]
    FinalClusterSnapshotIdentifier: NotRequired[str]
    FinalClusterSnapshotRetentionPeriod: NotRequired[int]

class DeleteClusterParameterGroupMessageTypeDef(TypedDict):
    ParameterGroupName: str

class DeleteClusterSecurityGroupMessageTypeDef(TypedDict):
    ClusterSecurityGroupName: str

class DeleteClusterSnapshotMessageRequestTypeDef(TypedDict):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: NotRequired[str]

class DeleteClusterSubnetGroupMessageTypeDef(TypedDict):
    ClusterSubnetGroupName: str

class DeleteCustomDomainAssociationMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    CustomDomainName: str

class DeleteEndpointAccessMessageTypeDef(TypedDict):
    EndpointName: str

class DeleteEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str

class DeleteHsmClientCertificateMessageTypeDef(TypedDict):
    HsmClientCertificateIdentifier: str

class DeleteHsmConfigurationMessageTypeDef(TypedDict):
    HsmConfigurationIdentifier: str

class DeleteIntegrationMessageTypeDef(TypedDict):
    IntegrationArn: str

class DeleteRedshiftIdcApplicationMessageTypeDef(TypedDict):
    RedshiftIdcApplicationArn: str

class DeleteResourcePolicyMessageTypeDef(TypedDict):
    ResourceArn: str

class DeleteScheduledActionMessageTypeDef(TypedDict):
    ScheduledActionName: str

class DeleteSnapshotCopyGrantMessageTypeDef(TypedDict):
    SnapshotCopyGrantName: str

class DeleteSnapshotScheduleMessageTypeDef(TypedDict):
    ScheduleIdentifier: str

class DeleteTagsMessageTypeDef(TypedDict):
    ResourceName: str
    TagKeys: Sequence[str]

class DeleteUsageLimitMessageTypeDef(TypedDict):
    UsageLimitId: str

class DescribeAccountAttributesMessageTypeDef(TypedDict):
    AttributeNames: NotRequired[Sequence[str]]

class DescribeAuthenticationProfilesMessageTypeDef(TypedDict):
    AuthenticationProfileName: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeClusterDbRevisionsMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeClusterParameterGroupsMessageTypeDef(TypedDict):
    ParameterGroupName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeClusterParametersMessageTypeDef(TypedDict):
    ParameterGroupName: str
    Source: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeClusterSecurityGroupsMessageTypeDef(TypedDict):
    ClusterSecurityGroupName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class SnapshotSortingEntityTypeDef(TypedDict):
    Attribute: SnapshotAttributeToSortByType
    SortOrder: NotRequired[SortByOrderType]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeClusterSubnetGroupsMessageTypeDef(TypedDict):
    ClusterSubnetGroupName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeClusterTracksMessageTypeDef(TypedDict):
    MaintenanceTrackName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeClusterVersionsMessageTypeDef(TypedDict):
    ClusterVersion: NotRequired[str]
    ClusterParameterGroupFamily: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeClustersMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeCustomDomainAssociationsMessageTypeDef(TypedDict):
    CustomDomainName: NotRequired[str]
    CustomDomainCertificateArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDataSharesForConsumerMessageTypeDef(TypedDict):
    ConsumerArn: NotRequired[str]
    Status: NotRequired[DataShareStatusForConsumerType]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDataSharesForProducerMessageTypeDef(TypedDict):
    ProducerArn: NotRequired[str]
    Status: NotRequired[DataShareStatusForProducerType]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDataSharesMessageTypeDef(TypedDict):
    DataShareArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDefaultClusterParametersMessageTypeDef(TypedDict):
    ParameterGroupFamily: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEndpointAccessMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    ResourceOwner: NotRequired[str]
    EndpointName: NotRequired[str]
    VpcId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEndpointAuthorizationMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    Account: NotRequired[str]
    Grantee: NotRequired[bool]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEventCategoriesMessageTypeDef(TypedDict):
    SourceType: NotRequired[str]

class DescribeEventSubscriptionsMessageTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeHsmClientCertificatesMessageTypeDef(TypedDict):
    HsmClientCertificateIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeHsmConfigurationsMessageTypeDef(TypedDict):
    HsmConfigurationIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeInboundIntegrationsMessageTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    TargetArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeIntegrationsFilterTypeDef(TypedDict):
    Name: DescribeIntegrationsFilterNameType
    Values: Sequence[str]

class DescribeLoggingStatusMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class NodeConfigurationOptionsFilterTypeDef(TypedDict):
    Name: NotRequired[NodeConfigurationOptionsFilterNameType]
    Operator: NotRequired[OperatorTypeType]
    Values: NotRequired[Sequence[str]]

class DescribeOrderableClusterOptionsMessageTypeDef(TypedDict):
    ClusterVersion: NotRequired[str]
    NodeType: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribePartnersInputMessageTypeDef(TypedDict):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: NotRequired[str]
    PartnerName: NotRequired[str]

class PartnerIntegrationInfoTypeDef(TypedDict):
    DatabaseName: NotRequired[str]
    PartnerName: NotRequired[str]
    Status: NotRequired[PartnerIntegrationStatusType]
    StatusMessage: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class DescribeRedshiftIdcApplicationsMessageTypeDef(TypedDict):
    RedshiftIdcApplicationArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReservedNodeExchangeStatusInputMessageTypeDef(TypedDict):
    ReservedNodeId: NotRequired[str]
    ReservedNodeExchangeRequestId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReservedNodeOfferingsMessageTypeDef(TypedDict):
    ReservedNodeOfferingId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReservedNodesMessageTypeDef(TypedDict):
    ReservedNodeId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeResizeMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class ScheduledActionFilterTypeDef(TypedDict):
    Name: ScheduledActionFilterNameType
    Values: Sequence[str]

class DescribeSnapshotCopyGrantsMessageTypeDef(TypedDict):
    SnapshotCopyGrantName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeSnapshotSchedulesMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    ScheduleIdentifier: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeTableRestoreStatusMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    TableRestoreRequestId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeTagsMessageTypeDef(TypedDict):
    ResourceName: NotRequired[str]
    ResourceType: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DescribeUsageLimitsMessageTypeDef(TypedDict):
    UsageLimitId: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    FeatureType: NotRequired[UsageLimitFeatureTypeType]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]

class DisableLoggingMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class DisableSnapshotCopyMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class DisassociateDataShareConsumerMessageTypeDef(TypedDict):
    DataShareArn: str
    DisassociateEntireAccount: NotRequired[bool]
    ConsumerArn: NotRequired[str]
    ConsumerRegion: NotRequired[str]

class EnableLoggingMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    BucketName: NotRequired[str]
    S3KeyPrefix: NotRequired[str]
    LogDestinationType: NotRequired[LogDestinationTypeType]
    LogExports: NotRequired[Sequence[str]]

class EnableSnapshotCopyMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    DestinationRegion: str
    RetentionPeriod: NotRequired[int]
    SnapshotCopyGrantName: NotRequired[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]

class EndpointAuthorizationTypeDef(TypedDict):
    Grantor: NotRequired[str]
    Grantee: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    AuthorizeTime: NotRequired[datetime]
    ClusterStatus: NotRequired[str]
    Status: NotRequired[AuthorizationStatusType]
    AllowedAllVPCs: NotRequired[bool]
    AllowedVPCs: NotRequired[List[str]]
    EndpointCount: NotRequired[int]

class EventInfoMapTypeDef(TypedDict):
    EventId: NotRequired[str]
    EventCategories: NotRequired[List[str]]
    EventDescription: NotRequired[str]
    Severity: NotRequired[str]

class EventTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    Message: NotRequired[str]
    EventCategories: NotRequired[List[str]]
    Severity: NotRequired[str]
    Date: NotRequired[datetime]
    EventId: NotRequired[str]

class FailoverPrimaryComputeInputMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class GetClusterCredentialsMessageTypeDef(TypedDict):
    DbUser: str
    DbName: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    DurationSeconds: NotRequired[int]
    AutoCreate: NotRequired[bool]
    DbGroups: NotRequired[Sequence[str]]
    CustomDomainName: NotRequired[str]

class GetClusterCredentialsWithIAMMessageTypeDef(TypedDict):
    DbName: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    DurationSeconds: NotRequired[int]
    CustomDomainName: NotRequired[str]

class GetReservedNodeExchangeConfigurationOptionsInputMessageTypeDef(TypedDict):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class GetReservedNodeExchangeOfferingsInputMessageTypeDef(TypedDict):
    ReservedNodeId: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class GetResourcePolicyMessageTypeDef(TypedDict):
    ResourceArn: str

class ResourcePolicyTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    Policy: NotRequired[str]

class IntegrationErrorTypeDef(TypedDict):
    ErrorCode: str
    ErrorMessage: NotRequired[str]

class LakeFormationQueryTypeDef(TypedDict):
    Authorization: ServiceAuthorizationType

class ListRecommendationsMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    NamespaceArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class ModifyAquaInputMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    AquaConfigurationStatus: NotRequired[AquaConfigurationStatusType]

class ModifyAuthenticationProfileMessageTypeDef(TypedDict):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str

class ModifyClusterDbRevisionMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    RevisionTarget: str

class ModifyClusterIamRolesMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    AddIamRoles: NotRequired[Sequence[str]]
    RemoveIamRoles: NotRequired[Sequence[str]]
    DefaultIamRoleArn: NotRequired[str]

class ModifyClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    ClusterType: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    ClusterSecurityGroups: NotRequired[Sequence[str]]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    MasterUserPassword: NotRequired[str]
    ClusterParameterGroupName: NotRequired[str]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    PreferredMaintenanceWindow: NotRequired[str]
    ClusterVersion: NotRequired[str]
    AllowVersionUpgrade: NotRequired[bool]
    HsmClientCertificateIdentifier: NotRequired[str]
    HsmConfigurationIdentifier: NotRequired[str]
    NewClusterIdentifier: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    ElasticIp: NotRequired[str]
    EnhancedVpcRouting: NotRequired[bool]
    MaintenanceTrackName: NotRequired[str]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    AvailabilityZoneRelocation: NotRequired[bool]
    AvailabilityZone: NotRequired[str]
    Port: NotRequired[int]
    ManageMasterPassword: NotRequired[bool]
    MasterPasswordSecretKmsKeyId: NotRequired[str]
    IpAddressType: NotRequired[str]
    MultiAZ: NotRequired[bool]

class ModifyClusterSnapshotMessageTypeDef(TypedDict):
    SnapshotIdentifier: str
    ManualSnapshotRetentionPeriod: NotRequired[int]
    Force: NotRequired[bool]

class ModifyClusterSnapshotScheduleMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    ScheduleIdentifier: NotRequired[str]
    DisassociateSchedule: NotRequired[bool]

class ModifyClusterSubnetGroupMessageTypeDef(TypedDict):
    ClusterSubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: NotRequired[str]

class ModifyCustomDomainAssociationMessageTypeDef(TypedDict):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str

class ModifyEndpointAccessMessageTypeDef(TypedDict):
    EndpointName: str
    VpcSecurityGroupIds: NotRequired[Sequence[str]]

class ModifyEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SnsTopicArn: NotRequired[str]
    SourceType: NotRequired[str]
    SourceIds: NotRequired[Sequence[str]]
    EventCategories: NotRequired[Sequence[str]]
    Severity: NotRequired[str]
    Enabled: NotRequired[bool]

class ModifyIntegrationMessageTypeDef(TypedDict):
    IntegrationArn: str
    Description: NotRequired[str]
    IntegrationName: NotRequired[str]

class ModifySnapshotCopyRetentionPeriodMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    RetentionPeriod: int
    Manual: NotRequired[bool]

class ModifySnapshotScheduleMessageTypeDef(TypedDict):
    ScheduleIdentifier: str
    ScheduleDefinitions: Sequence[str]

class ModifyUsageLimitMessageTypeDef(TypedDict):
    UsageLimitId: str
    Amount: NotRequired[int]
    BreachAction: NotRequired[UsageLimitBreachActionType]

class ProvisionedIdentifierTypeDef(TypedDict):
    ClusterIdentifier: str

class ServerlessIdentifierTypeDef(TypedDict):
    NamespaceIdentifier: str
    WorkgroupIdentifier: str

class NetworkInterfaceTypeDef(TypedDict):
    NetworkInterfaceId: NotRequired[str]
    SubnetId: NotRequired[str]
    PrivateIpAddress: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    Ipv6Address: NotRequired[str]

class NodeConfigurationOptionTypeDef(TypedDict):
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    EstimatedDiskUtilizationPercent: NotRequired[float]
    Mode: NotRequired[ModeType]

class PartnerIntegrationInputMessageRequestTypeDef(TypedDict):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str

class PartnerIntegrationInputMessageTypeDef(TypedDict):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str

class PauseClusterMessageRequestTypeDef(TypedDict):
    ClusterIdentifier: str

class PauseClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class PurchaseReservedNodeOfferingMessageTypeDef(TypedDict):
    ReservedNodeOfferingId: str
    NodeCount: NotRequired[int]

class PutResourcePolicyMessageTypeDef(TypedDict):
    ResourceArn: str
    Policy: str

class ReadWriteAccessTypeDef(TypedDict):
    Authorization: ServiceAuthorizationType

class RebootClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str

RecommendedActionTypeDef = TypedDict(
    "RecommendedActionTypeDef",
    {
        "Text": NotRequired[str],
        "Database": NotRequired[str],
        "Command": NotRequired[str],
        "Type": NotRequired[RecommendedActionTypeType],
    },
)
ReferenceLinkTypeDef = TypedDict(
    "ReferenceLinkTypeDef",
    {
        "Text": NotRequired[str],
        "Link": NotRequired[str],
    },
)

class RecurringChargeTypeDef(TypedDict):
    RecurringChargeAmount: NotRequired[float]
    RecurringChargeFrequency: NotRequired[str]

class RejectDataShareMessageTypeDef(TypedDict):
    DataShareArn: str

class ResizeClusterMessageRequestTypeDef(TypedDict):
    ClusterIdentifier: str
    ClusterType: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    Classic: NotRequired[bool]
    ReservedNodeId: NotRequired[str]
    TargetReservedNodeOfferingId: NotRequired[str]

class ResizeClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    ClusterType: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    Classic: NotRequired[bool]
    ReservedNodeId: NotRequired[str]
    TargetReservedNodeOfferingId: NotRequired[str]

class RestoreFromClusterSnapshotMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    SnapshotClusterIdentifier: NotRequired[str]
    Port: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    AllowVersionUpgrade: NotRequired[bool]
    ClusterSubnetGroupName: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    OwnerAccount: NotRequired[str]
    HsmClientCertificateIdentifier: NotRequired[str]
    HsmConfigurationIdentifier: NotRequired[str]
    ElasticIp: NotRequired[str]
    ClusterParameterGroupName: NotRequired[str]
    ClusterSecurityGroups: NotRequired[Sequence[str]]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    PreferredMaintenanceWindow: NotRequired[str]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    KmsKeyId: NotRequired[str]
    NodeType: NotRequired[str]
    EnhancedVpcRouting: NotRequired[bool]
    AdditionalInfo: NotRequired[str]
    IamRoles: NotRequired[Sequence[str]]
    MaintenanceTrackName: NotRequired[str]
    SnapshotScheduleIdentifier: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    AvailabilityZoneRelocation: NotRequired[bool]
    AquaConfigurationStatus: NotRequired[AquaConfigurationStatusType]
    DefaultIamRoleArn: NotRequired[str]
    ReservedNodeId: NotRequired[str]
    TargetReservedNodeOfferingId: NotRequired[str]
    Encrypted: NotRequired[bool]
    ManageMasterPassword: NotRequired[bool]
    MasterPasswordSecretKmsKeyId: NotRequired[str]
    IpAddressType: NotRequired[str]
    MultiAZ: NotRequired[bool]

class RestoreTableFromClusterSnapshotMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    SnapshotIdentifier: str
    SourceDatabaseName: str
    SourceTableName: str
    NewTableName: str
    SourceSchemaName: NotRequired[str]
    TargetDatabaseName: NotRequired[str]
    TargetSchemaName: NotRequired[str]
    EnableCaseSensitiveIdentifier: NotRequired[bool]

class TableRestoreStatusTypeDef(TypedDict):
    TableRestoreRequestId: NotRequired[str]
    Status: NotRequired[TableRestoreStatusTypeType]
    Message: NotRequired[str]
    RequestTime: NotRequired[datetime]
    ProgressInMegaBytes: NotRequired[int]
    TotalDataInMegaBytes: NotRequired[int]
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    SourceDatabaseName: NotRequired[str]
    SourceSchemaName: NotRequired[str]
    SourceTableName: NotRequired[str]
    TargetDatabaseName: NotRequired[str]
    TargetSchemaName: NotRequired[str]
    NewTableName: NotRequired[str]

class ResumeClusterMessageRequestTypeDef(TypedDict):
    ClusterIdentifier: str

class ResumeClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class RevokeClusterSecurityGroupIngressMessageTypeDef(TypedDict):
    ClusterSecurityGroupName: str
    CIDRIP: NotRequired[str]
    EC2SecurityGroupName: NotRequired[str]
    EC2SecurityGroupOwnerId: NotRequired[str]

class RevokeEndpointAccessMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    Account: NotRequired[str]
    VpcIds: NotRequired[Sequence[str]]
    Force: NotRequired[bool]

class RevokeSnapshotAccessMessageTypeDef(TypedDict):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    SnapshotClusterIdentifier: NotRequired[str]

class RotateEncryptionKeyMessageTypeDef(TypedDict):
    ClusterIdentifier: str

class SupportedOperationTypeDef(TypedDict):
    OperationName: NotRequired[str]

class UpdatePartnerStatusInputMessageTypeDef(TypedDict):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str
    Status: PartnerIntegrationStatusType
    StatusMessage: NotRequired[str]

class ClusterCredentialsTypeDef(TypedDict):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterExtendedCredentialsTypeDef(TypedDict):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    NextRefreshTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterParameterGroupNameMessageTypeDef(TypedDict):
    ParameterGroupName: str
    ParameterGroupStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAuthenticationProfileResultTypeDef(TypedDict):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDomainAssociationResultTypeDef(TypedDict):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerStorageMessageTypeDef(TypedDict):
    TotalBackupSizeInMegaBytes: float
    TotalProvisionedStorageInMegaBytes: float
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAuthenticationProfileResultTypeDef(TypedDict):
    AuthenticationProfileName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterNamespaceOutputMessageTypeDef(TypedDict):
    Status: NamespaceRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAuthorizationResponseTypeDef(TypedDict):
    Grantor: str
    Grantee: str
    ClusterIdentifier: str
    AuthorizeTime: datetime
    ClusterStatus: str
    Status: AuthorizationStatusType
    AllowedAllVPCs: bool
    AllowedVPCs: List[str]
    EndpointCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingStatusTypeDef(TypedDict):
    LoggingEnabled: bool
    BucketName: str
    S3KeyPrefix: str
    LastSuccessfulDeliveryTime: datetime
    LastFailureTime: datetime
    LastFailureMessage: str
    LogDestinationType: LogDestinationTypeType
    LogExports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyAuthenticationProfileResultTypeDef(TypedDict):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCustomDomainAssociationResultTypeDef(TypedDict):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class PartnerIntegrationOutputMessageTypeDef(TypedDict):
    DatabaseName: str
    PartnerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterNamespaceOutputMessageTypeDef(TypedDict):
    Status: NamespaceRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ResizeProgressMessageTypeDef(TypedDict):
    TargetNodeType: str
    TargetNumberOfNodes: int
    TargetClusterType: str
    Status: str
    ImportTablesCompleted: List[str]
    ImportTablesInProgress: List[str]
    ImportTablesNotStarted: List[str]
    AvgResizeRateInMegaBytesPerSecond: float
    TotalResizeDataInMegaBytes: int
    ProgressInMegaBytes: int
    ElapsedTimeInSeconds: int
    EstimatedTimeToCompletionInSeconds: int
    ResizeType: str
    Message: str
    TargetEncryptionType: str
    DataTransferProgressPercent: float
    ResponseMetadata: ResponseMetadataTypeDef

class AccountAttributeTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeValues: NotRequired[List[AttributeValueTargetTypeDef]]

class ModifyAquaOutputMessageTypeDef(TypedDict):
    AquaConfiguration: AquaConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociationTypeDef(TypedDict):
    CustomDomainCertificateArn: NotRequired[str]
    CustomDomainCertificateExpiryDate: NotRequired[datetime]
    CertificateAssociations: NotRequired[List[CertificateAssociationTypeDef]]

class DescribeAuthenticationProfilesResultTypeDef(TypedDict):
    AuthenticationProfiles: List[AuthenticationProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

AuthorizedTokenIssuerUnionTypeDef = Union[
    AuthorizedTokenIssuerTypeDef, AuthorizedTokenIssuerOutputTypeDef
]

class AvailabilityZoneTypeDef(TypedDict):
    Name: NotRequired[str]
    SupportedPlatforms: NotRequired[List[SupportedPlatformTypeDef]]

class BatchDeleteClusterSnapshotsRequestTypeDef(TypedDict):
    Identifiers: Sequence[DeleteClusterSnapshotMessageTypeDef]

class BatchDeleteClusterSnapshotsResultTypeDef(TypedDict):
    Resources: List[str]
    Errors: List[SnapshotErrorMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchModifyClusterSnapshotsOutputMessageTypeDef(TypedDict):
    Resources: List[str]
    Errors: List[SnapshotErrorMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterDbRevisionTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    CurrentDatabaseRevision: NotRequired[str]
    DatabaseRevisionReleaseDate: NotRequired[datetime]
    RevisionTargets: NotRequired[List[RevisionTargetTypeDef]]

class SecondaryClusterInfoTypeDef(TypedDict):
    AvailabilityZone: NotRequired[str]
    ClusterNodes: NotRequired[List[ClusterNodeTypeDef]]

class ClusterParameterGroupDetailsTypeDef(TypedDict):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DefaultClusterParametersTypeDef(TypedDict):
    ParameterGroupFamily: NotRequired[str]
    Marker: NotRequired[str]
    Parameters: NotRequired[List[ParameterTypeDef]]

class ModifyClusterParameterGroupMessageTypeDef(TypedDict):
    ParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetClusterParameterGroupMessageTypeDef(TypedDict):
    ParameterGroupName: str
    ResetAllParameters: NotRequired[bool]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]

class ClusterParameterGroupStatusTypeDef(TypedDict):
    ParameterGroupName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]
    ClusterParameterStatusList: NotRequired[List[ClusterParameterStatusTypeDef]]

class ClusterParameterGroupTypeDef(TypedDict):
    ParameterGroupName: NotRequired[str]
    ParameterGroupFamily: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class CreateClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    NodeType: str
    MasterUsername: str
    DBName: NotRequired[str]
    ClusterType: NotRequired[str]
    MasterUserPassword: NotRequired[str]
    ClusterSecurityGroups: NotRequired[Sequence[str]]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    ClusterSubnetGroupName: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    ClusterParameterGroupName: NotRequired[str]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    Port: NotRequired[int]
    ClusterVersion: NotRequired[str]
    AllowVersionUpgrade: NotRequired[bool]
    NumberOfNodes: NotRequired[int]
    PubliclyAccessible: NotRequired[bool]
    Encrypted: NotRequired[bool]
    HsmClientCertificateIdentifier: NotRequired[str]
    HsmConfigurationIdentifier: NotRequired[str]
    ElasticIp: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    EnhancedVpcRouting: NotRequired[bool]
    AdditionalInfo: NotRequired[str]
    IamRoles: NotRequired[Sequence[str]]
    MaintenanceTrackName: NotRequired[str]
    SnapshotScheduleIdentifier: NotRequired[str]
    AvailabilityZoneRelocation: NotRequired[bool]
    AquaConfigurationStatus: NotRequired[AquaConfigurationStatusType]
    DefaultIamRoleArn: NotRequired[str]
    LoadSampleData: NotRequired[str]
    ManageMasterPassword: NotRequired[bool]
    MasterPasswordSecretKmsKeyId: NotRequired[str]
    IpAddressType: NotRequired[str]
    MultiAZ: NotRequired[bool]
    RedshiftIdcApplicationArn: NotRequired[str]

class CreateClusterParameterGroupMessageTypeDef(TypedDict):
    ParameterGroupName: str
    ParameterGroupFamily: str
    Description: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateClusterSecurityGroupMessageTypeDef(TypedDict):
    ClusterSecurityGroupName: str
    Description: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateClusterSnapshotMessageTypeDef(TypedDict):
    SnapshotIdentifier: str
    ClusterIdentifier: str
    ManualSnapshotRetentionPeriod: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateClusterSubnetGroupMessageTypeDef(TypedDict):
    ClusterSubnetGroupName: str
    Description: str
    SubnetIds: Sequence[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: NotRequired[str]
    SourceIds: NotRequired[Sequence[str]]
    EventCategories: NotRequired[Sequence[str]]
    Severity: NotRequired[str]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateHsmClientCertificateMessageTypeDef(TypedDict):
    HsmClientCertificateIdentifier: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateHsmConfigurationMessageTypeDef(TypedDict):
    HsmConfigurationIdentifier: str
    Description: str
    HsmIpAddress: str
    HsmPartitionName: str
    HsmPartitionPassword: str
    HsmServerPublicCertificate: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateIntegrationMessageTypeDef(TypedDict):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    KMSKeyId: NotRequired[str]
    TagList: NotRequired[Sequence[TagTypeDef]]
    AdditionalEncryptionContext: NotRequired[Mapping[str, str]]
    Description: NotRequired[str]

class CreateSnapshotCopyGrantMessageTypeDef(TypedDict):
    SnapshotCopyGrantName: str
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSnapshotScheduleMessageTypeDef(TypedDict):
    ScheduleDefinitions: NotRequired[Sequence[str]]
    ScheduleIdentifier: NotRequired[str]
    ScheduleDescription: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DryRun: NotRequired[bool]
    NextInvocations: NotRequired[int]

class CreateTagsMessageTypeDef(TypedDict):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CreateUsageLimitMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: NotRequired[UsageLimitPeriodType]
    BreachAction: NotRequired[UsageLimitBreachActionType]
    Tags: NotRequired[Sequence[TagTypeDef]]

class EC2SecurityGroupTypeDef(TypedDict):
    Status: NotRequired[str]
    EC2SecurityGroupName: NotRequired[str]
    EC2SecurityGroupOwnerId: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class EventSubscriptionTypeDef(TypedDict):
    CustomerAwsId: NotRequired[str]
    CustSubscriptionId: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    Status: NotRequired[str]
    SubscriptionCreationTime: NotRequired[datetime]
    SourceType: NotRequired[str]
    SourceIdsList: NotRequired[List[str]]
    EventCategoriesList: NotRequired[List[str]]
    Severity: NotRequired[str]
    Enabled: NotRequired[bool]
    Tags: NotRequired[List[TagTypeDef]]

class HsmClientCertificateTypeDef(TypedDict):
    HsmClientCertificateIdentifier: NotRequired[str]
    HsmClientCertificatePublicKey: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class HsmConfigurationTypeDef(TypedDict):
    HsmConfigurationIdentifier: NotRequired[str]
    Description: NotRequired[str]
    HsmIpAddress: NotRequired[str]
    HsmPartitionName: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class IPRangeTypeDef(TypedDict):
    Status: NotRequired[str]
    CIDRIP: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class SnapshotCopyGrantTypeDef(TypedDict):
    SnapshotCopyGrantName: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class SnapshotScheduleResponseTypeDef(TypedDict):
    ScheduleDefinitions: List[str]
    ScheduleIdentifier: str
    ScheduleDescription: str
    Tags: List[TagTypeDef]
    NextInvocations: List[datetime]
    AssociatedClusterCount: int
    AssociatedClusters: List[ClusterAssociatedToScheduleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotScheduleTypeDef(TypedDict):
    ScheduleDefinitions: NotRequired[List[str]]
    ScheduleIdentifier: NotRequired[str]
    ScheduleDescription: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    NextInvocations: NotRequired[List[datetime]]
    AssociatedClusterCount: NotRequired[int]
    AssociatedClusters: NotRequired[List[ClusterAssociatedToScheduleTypeDef]]

class SnapshotTypeDef(TypedDict):
    SnapshotIdentifier: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    SnapshotCreateTime: NotRequired[datetime]
    Status: NotRequired[str]
    Port: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    ClusterCreateTime: NotRequired[datetime]
    MasterUsername: NotRequired[str]
    ClusterVersion: NotRequired[str]
    EngineFullVersion: NotRequired[str]
    SnapshotType: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    DBName: NotRequired[str]
    VpcId: NotRequired[str]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    EncryptedWithHSM: NotRequired[bool]
    AccountsWithRestoreAccess: NotRequired[List[AccountWithRestoreAccessTypeDef]]
    OwnerAccount: NotRequired[str]
    TotalBackupSizeInMegaBytes: NotRequired[float]
    ActualIncrementalBackupSizeInMegaBytes: NotRequired[float]
    BackupProgressInMegaBytes: NotRequired[float]
    CurrentBackupRateInMegaBytesPerSecond: NotRequired[float]
    EstimatedSecondsToCompletion: NotRequired[int]
    ElapsedTimeInSeconds: NotRequired[int]
    SourceRegion: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    RestorableNodeTypes: NotRequired[List[str]]
    EnhancedVpcRouting: NotRequired[bool]
    MaintenanceTrackName: NotRequired[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    ManualSnapshotRemainingDays: NotRequired[int]
    SnapshotRetentionStartTime: NotRequired[datetime]
    MasterPasswordSecretArn: NotRequired[str]
    MasterPasswordSecretKmsKeyId: NotRequired[str]
    SnapshotArn: NotRequired[str]

class TaggedResourceTypeDef(TypedDict):
    Tag: NotRequired[TagTypeDef]
    ResourceName: NotRequired[str]
    ResourceType: NotRequired[str]

class UsageLimitResponseTypeDef(TypedDict):
    UsageLimitId: str
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: UsageLimitPeriodType
    BreachAction: UsageLimitBreachActionType
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsageLimitTypeDef(TypedDict):
    UsageLimitId: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    FeatureType: NotRequired[UsageLimitFeatureTypeType]
    LimitType: NotRequired[UsageLimitLimitTypeType]
    Amount: NotRequired[int]
    Period: NotRequired[UsageLimitPeriodType]
    BreachAction: NotRequired[UsageLimitBreachActionType]
    Tags: NotRequired[List[TagTypeDef]]

class DescribeReservedNodeExchangeStatusOutputMessageTypeDef(TypedDict):
    ReservedNodeExchangeStatusDetails: List[ReservedNodeExchangeStatusTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterVersionsMessageTypeDef(TypedDict):
    Marker: str
    ClusterVersions: List[ClusterVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsMessageTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class ModifyClusterMaintenanceMessageTypeDef(TypedDict):
    ClusterIdentifier: str
    DeferMaintenance: NotRequired[bool]
    DeferMaintenanceIdentifier: NotRequired[str]
    DeferMaintenanceStartTime: NotRequired[TimestampTypeDef]
    DeferMaintenanceEndTime: NotRequired[TimestampTypeDef]
    DeferMaintenanceDuration: NotRequired[int]

class DataShareResponseTypeDef(TypedDict):
    DataShareArn: str
    ProducerArn: str
    AllowPubliclyAccessibleConsumers: bool
    DataShareAssociations: List[DataShareAssociationTypeDef]
    ManagedBy: str
    DataShareType: Literal["INTERNAL"]
    ResponseMetadata: ResponseMetadataTypeDef

class DataShareTypeDef(TypedDict):
    DataShareArn: NotRequired[str]
    ProducerArn: NotRequired[str]
    AllowPubliclyAccessibleConsumers: NotRequired[bool]
    DataShareAssociations: NotRequired[List[DataShareAssociationTypeDef]]
    ManagedBy: NotRequired[str]
    DataShareType: NotRequired[Literal["INTERNAL"]]

class DescribeClusterDbRevisionsMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterParameterGroupsMessagePaginateTypeDef(TypedDict):
    ParameterGroupName: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterParametersMessagePaginateTypeDef(TypedDict):
    ParameterGroupName: str
    Source: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterSecurityGroupsMessagePaginateTypeDef(TypedDict):
    ClusterSecurityGroupName: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterSubnetGroupsMessagePaginateTypeDef(TypedDict):
    ClusterSubnetGroupName: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterTracksMessagePaginateTypeDef(TypedDict):
    MaintenanceTrackName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterVersionsMessagePaginateTypeDef(TypedDict):
    ClusterVersion: NotRequired[str]
    ClusterParameterGroupFamily: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClustersMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCustomDomainAssociationsMessagePaginateTypeDef(TypedDict):
    CustomDomainName: NotRequired[str]
    CustomDomainCertificateArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDataSharesForConsumerMessagePaginateTypeDef(TypedDict):
    ConsumerArn: NotRequired[str]
    Status: NotRequired[DataShareStatusForConsumerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDataSharesForProducerMessagePaginateTypeDef(TypedDict):
    ProducerArn: NotRequired[str]
    Status: NotRequired[DataShareStatusForProducerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDataSharesMessagePaginateTypeDef(TypedDict):
    DataShareArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDefaultClusterParametersMessagePaginateTypeDef(TypedDict):
    ParameterGroupFamily: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEndpointAccessMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    ResourceOwner: NotRequired[str]
    EndpointName: NotRequired[str]
    VpcId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEndpointAuthorizationMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    Account: NotRequired[str]
    Grantee: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventSubscriptionsMessagePaginateTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsMessagePaginateTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeHsmClientCertificatesMessagePaginateTypeDef(TypedDict):
    HsmClientCertificateIdentifier: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeHsmConfigurationsMessagePaginateTypeDef(TypedDict):
    HsmConfigurationIdentifier: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeInboundIntegrationsMessagePaginateTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    TargetArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrderableClusterOptionsMessagePaginateTypeDef(TypedDict):
    ClusterVersion: NotRequired[str]
    NodeType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRedshiftIdcApplicationsMessagePaginateTypeDef(TypedDict):
    RedshiftIdcApplicationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef(TypedDict):
    ReservedNodeId: NotRequired[str]
    ReservedNodeExchangeRequestId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReservedNodeOfferingsMessagePaginateTypeDef(TypedDict):
    ReservedNodeOfferingId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReservedNodesMessagePaginateTypeDef(TypedDict):
    ReservedNodeId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSnapshotCopyGrantsMessagePaginateTypeDef(TypedDict):
    SnapshotCopyGrantName: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSnapshotSchedulesMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    ScheduleIdentifier: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTableRestoreStatusMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    TableRestoreRequestId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTagsMessagePaginateTypeDef(TypedDict):
    ResourceName: NotRequired[str]
    ResourceType: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUsageLimitsMessagePaginateTypeDef(TypedDict):
    UsageLimitId: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    FeatureType: NotRequired[UsageLimitFeatureTypeType]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef(TypedDict):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef(TypedDict):
    ReservedNodeId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommendationsMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    NamespaceArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterSnapshotsMessagePaginateTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    SnapshotType: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    OwnerAccount: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    ClusterExists: NotRequired[bool]
    SortingEntities: NotRequired[Sequence[SnapshotSortingEntityTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClusterSnapshotsMessageTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    SnapshotType: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    OwnerAccount: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    ClusterExists: NotRequired[bool]
    SortingEntities: NotRequired[Sequence[SnapshotSortingEntityTypeDef]]

class DescribeClusterSnapshotsMessageWaitTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    SnapshotType: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    OwnerAccount: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    ClusterExists: NotRequired[bool]
    SortingEntities: NotRequired[Sequence[SnapshotSortingEntityTypeDef]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeClustersMessageWaitExtraExtraTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeClustersMessageWaitExtraTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeClustersMessageWaitTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    TagKeys: NotRequired[Sequence[str]]
    TagValues: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeIntegrationsMessagePaginateTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    Filters: NotRequired[Sequence[DescribeIntegrationsFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeIntegrationsMessageTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    Filters: NotRequired[Sequence[DescribeIntegrationsFilterTypeDef]]

class DescribeNodeConfigurationOptionsMessagePaginateTypeDef(TypedDict):
    ActionType: ActionTypeType
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    OwnerAccount: NotRequired[str]
    Filters: NotRequired[Sequence[NodeConfigurationOptionsFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeNodeConfigurationOptionsMessageTypeDef(TypedDict):
    ActionType: ActionTypeType
    ClusterIdentifier: NotRequired[str]
    SnapshotIdentifier: NotRequired[str]
    SnapshotArn: NotRequired[str]
    OwnerAccount: NotRequired[str]
    Filters: NotRequired[Sequence[NodeConfigurationOptionsFilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribePartnersOutputMessageTypeDef(TypedDict):
    PartnerIntegrationInfoList: List[PartnerIntegrationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScheduledActionsMessagePaginateTypeDef(TypedDict):
    ScheduledActionName: NotRequired[str]
    TargetActionType: NotRequired[ScheduledActionTypeValuesType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Active: NotRequired[bool]
    Filters: NotRequired[Sequence[ScheduledActionFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeScheduledActionsMessageTypeDef(TypedDict):
    ScheduledActionName: NotRequired[str]
    TargetActionType: NotRequired[ScheduledActionTypeValuesType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Active: NotRequired[bool]
    Filters: NotRequired[Sequence[ScheduledActionFilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class EndpointAuthorizationListTypeDef(TypedDict):
    EndpointAuthorizationList: List[EndpointAuthorizationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMapTypeDef(TypedDict):
    SourceType: NotRequired[str]
    Events: NotRequired[List[EventInfoMapTypeDef]]

class EventsMessageTypeDef(TypedDict):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResultTypeDef(TypedDict):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResultTypeDef(TypedDict):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    SourceArn: NotRequired[str]
    TargetArn: NotRequired[str]
    Status: NotRequired[ZeroETLIntegrationStatusType]
    Errors: NotRequired[List[IntegrationErrorTypeDef]]
    CreateTime: NotRequired[datetime]

class IntegrationResponseTypeDef(TypedDict):
    IntegrationArn: str
    IntegrationName: str
    SourceArn: str
    TargetArn: str
    Status: ZeroETLIntegrationStatusType
    Errors: List[IntegrationErrorTypeDef]
    CreateTime: datetime
    Description: str
    KMSKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    IntegrationName: NotRequired[str]
    SourceArn: NotRequired[str]
    TargetArn: NotRequired[str]
    Status: NotRequired[ZeroETLIntegrationStatusType]
    Errors: NotRequired[List[IntegrationErrorTypeDef]]
    CreateTime: NotRequired[datetime]
    Description: NotRequired[str]
    KMSKeyId: NotRequired[str]
    AdditionalEncryptionContext: NotRequired[Dict[str, str]]
    Tags: NotRequired[List[TagTypeDef]]

class LakeFormationScopeUnionTypeDef(TypedDict):
    LakeFormationQuery: NotRequired[LakeFormationQueryTypeDef]

class NamespaceIdentifierUnionTypeDef(TypedDict):
    ServerlessIdentifier: NotRequired[ServerlessIdentifierTypeDef]
    ProvisionedIdentifier: NotRequired[ProvisionedIdentifierTypeDef]

class VpcEndpointTypeDef(TypedDict):
    VpcEndpointId: NotRequired[str]
    VpcId: NotRequired[str]
    NetworkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]

class NodeConfigurationOptionsMessageTypeDef(TypedDict):
    NodeConfigurationOptionList: List[NodeConfigurationOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class S3AccessGrantsScopeUnionTypeDef(TypedDict):
    ReadWriteAccess: NotRequired[ReadWriteAccessTypeDef]

class RecommendationTypeDef(TypedDict):
    Id: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    NamespaceArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    RecommendationType: NotRequired[str]
    Title: NotRequired[str]
    Description: NotRequired[str]
    Observation: NotRequired[str]
    ImpactRanking: NotRequired[ImpactRankingTypeType]
    RecommendationText: NotRequired[str]
    RecommendedActions: NotRequired[List[RecommendedActionTypeDef]]
    ReferenceLinks: NotRequired[List[ReferenceLinkTypeDef]]

class ReservedNodeOfferingTypeDef(TypedDict):
    ReservedNodeOfferingId: NotRequired[str]
    NodeType: NotRequired[str]
    Duration: NotRequired[int]
    FixedPrice: NotRequired[float]
    UsagePrice: NotRequired[float]
    CurrencyCode: NotRequired[str]
    OfferingType: NotRequired[str]
    RecurringCharges: NotRequired[List[RecurringChargeTypeDef]]
    ReservedNodeOfferingType: NotRequired[ReservedNodeOfferingTypeType]

class ReservedNodeTypeDef(TypedDict):
    ReservedNodeId: NotRequired[str]
    ReservedNodeOfferingId: NotRequired[str]
    NodeType: NotRequired[str]
    StartTime: NotRequired[datetime]
    Duration: NotRequired[int]
    FixedPrice: NotRequired[float]
    UsagePrice: NotRequired[float]
    CurrencyCode: NotRequired[str]
    NodeCount: NotRequired[int]
    State: NotRequired[str]
    OfferingType: NotRequired[str]
    RecurringCharges: NotRequired[List[RecurringChargeTypeDef]]
    ReservedNodeOfferingType: NotRequired[ReservedNodeOfferingTypeType]

class RestoreTableFromClusterSnapshotResultTypeDef(TypedDict):
    TableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TableRestoreStatusMessageTypeDef(TypedDict):
    TableRestoreStatusDetails: List[TableRestoreStatusTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionTypeTypeDef(TypedDict):
    ResizeCluster: NotRequired[ResizeClusterMessageTypeDef]
    PauseCluster: NotRequired[PauseClusterMessageTypeDef]
    ResumeCluster: NotRequired[ResumeClusterMessageTypeDef]

class UpdateTargetTypeDef(TypedDict):
    MaintenanceTrackName: NotRequired[str]
    DatabaseVersion: NotRequired[str]
    SupportedOperations: NotRequired[List[SupportedOperationTypeDef]]

class AccountAttributeListTypeDef(TypedDict):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDomainAssociationsMessageTypeDef(TypedDict):
    Marker: str
    Associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableClusterOptionTypeDef(TypedDict):
    ClusterVersion: NotRequired[str]
    ClusterType: NotRequired[str]
    NodeType: NotRequired[str]
    AvailabilityZones: NotRequired[List[AvailabilityZoneTypeDef]]

class SubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[AvailabilityZoneTypeDef]
    SubnetStatus: NotRequired[str]

class ClusterDbRevisionsMessageTypeDef(TypedDict):
    Marker: str
    ClusterDbRevisions: List[ClusterDbRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDefaultClusterParametersResultTypeDef(TypedDict):
    DefaultClusterParameters: DefaultClusterParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterParameterGroupsMessageTypeDef(TypedDict):
    Marker: str
    ParameterGroups: List[ClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterParameterGroupResultTypeDef(TypedDict):
    ClusterParameterGroup: ClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(TypedDict):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmClientCertificateResultTypeDef(TypedDict):
    HsmClientCertificate: HsmClientCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HsmClientCertificateMessageTypeDef(TypedDict):
    Marker: str
    HsmClientCertificates: List[HsmClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmConfigurationResultTypeDef(TypedDict):
    HsmConfiguration: HsmConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HsmConfigurationMessageTypeDef(TypedDict):
    Marker: str
    HsmConfigurations: List[HsmConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSecurityGroupTypeDef(TypedDict):
    ClusterSecurityGroupName: NotRequired[str]
    Description: NotRequired[str]
    EC2SecurityGroups: NotRequired[List[EC2SecurityGroupTypeDef]]
    IPRanges: NotRequired[List[IPRangeTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]

class CreateSnapshotCopyGrantResultTypeDef(TypedDict):
    SnapshotCopyGrant: SnapshotCopyGrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotCopyGrantMessageTypeDef(TypedDict):
    Marker: str
    SnapshotCopyGrants: List[SnapshotCopyGrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotSchedulesOutputMessageTypeDef(TypedDict):
    SnapshotSchedules: List[SnapshotScheduleTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSnapshotAccessResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyClusterSnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterSnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterSnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeSnapshotAccessResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotMessageTypeDef(TypedDict):
    Marker: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaggedResourceListMessageTypeDef(TypedDict):
    TaggedResources: List[TaggedResourceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageLimitListTypeDef(TypedDict):
    UsageLimits: List[UsageLimitTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesForConsumerResultTypeDef(TypedDict):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesForProducerResultTypeDef(TypedDict):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesResultTypeDef(TypedDict):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMessageTypeDef(TypedDict):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationsMessageTypeDef(TypedDict):
    Marker: str
    InboundIntegrations: List[InboundIntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationsMessageTypeDef(TypedDict):
    Marker: str
    Integrations: List[IntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterNamespaceInputMessageTypeDef(TypedDict):
    NamespaceIdentifier: NamespaceIdentifierUnionTypeDef
    ConsumerIdentifiers: Sequence[str]

class RegisterNamespaceInputMessageTypeDef(TypedDict):
    NamespaceIdentifier: NamespaceIdentifierUnionTypeDef
    ConsumerIdentifiers: Sequence[str]

class EndpointAccessResponseTypeDef(TypedDict):
    ClusterIdentifier: str
    ResourceOwner: str
    SubnetGroupName: str
    EndpointStatus: str
    EndpointName: str
    EndpointCreateTime: datetime
    Port: int
    Address: str
    VpcSecurityGroups: List[VpcSecurityGroupMembershipTypeDef]
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAccessTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    ResourceOwner: NotRequired[str]
    SubnetGroupName: NotRequired[str]
    EndpointStatus: NotRequired[str]
    EndpointName: NotRequired[str]
    EndpointCreateTime: NotRequired[datetime]
    Port: NotRequired[int]
    Address: NotRequired[str]
    VpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    VpcEndpoint: NotRequired[VpcEndpointTypeDef]

class EndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]
    VpcEndpoints: NotRequired[List[VpcEndpointTypeDef]]

class ServiceIntegrationsUnionOutputTypeDef(TypedDict):
    LakeFormation: NotRequired[List[LakeFormationScopeUnionTypeDef]]
    S3AccessGrants: NotRequired[List[S3AccessGrantsScopeUnionTypeDef]]

class ServiceIntegrationsUnionTypeDef(TypedDict):
    LakeFormation: NotRequired[Sequence[LakeFormationScopeUnionTypeDef]]
    S3AccessGrants: NotRequired[Sequence[S3AccessGrantsScopeUnionTypeDef]]

class ListRecommendationsResultTypeDef(TypedDict):
    Recommendations: List[RecommendationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservedNodeExchangeOfferingsOutputMessageTypeDef(TypedDict):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedNodeOfferingsMessageTypeDef(TypedDict):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedNodeExchangeOutputMessageTypeDef(TypedDict):
    ExchangedReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodeOfferingResultTypeDef(TypedDict):
    ReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedNodeConfigurationOptionTypeDef(TypedDict):
    SourceReservedNode: NotRequired[ReservedNodeTypeDef]
    TargetReservedNodeCount: NotRequired[int]
    TargetReservedNodeOffering: NotRequired[ReservedNodeOfferingTypeDef]

class ReservedNodesMessageTypeDef(TypedDict):
    Marker: str
    ReservedNodes: List[ReservedNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledActionMessageTypeDef(TypedDict):
    ScheduledActionName: str
    TargetAction: ScheduledActionTypeTypeDef
    Schedule: str
    IamRole: str
    ScheduledActionDescription: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Enable: NotRequired[bool]

class ModifyScheduledActionMessageTypeDef(TypedDict):
    ScheduledActionName: str
    TargetAction: NotRequired[ScheduledActionTypeTypeDef]
    Schedule: NotRequired[str]
    IamRole: NotRequired[str]
    ScheduledActionDescription: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Enable: NotRequired[bool]

class ScheduledActionResponseTypeDef(TypedDict):
    ScheduledActionName: str
    TargetAction: ScheduledActionTypeTypeDef
    Schedule: str
    IamRole: str
    ScheduledActionDescription: str
    State: ScheduledActionStateType
    NextInvocations: List[datetime]
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionTypeDef(TypedDict):
    ScheduledActionName: NotRequired[str]
    TargetAction: NotRequired[ScheduledActionTypeTypeDef]
    Schedule: NotRequired[str]
    IamRole: NotRequired[str]
    ScheduledActionDescription: NotRequired[str]
    State: NotRequired[ScheduledActionStateType]
    NextInvocations: NotRequired[List[datetime]]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class MaintenanceTrackTypeDef(TypedDict):
    MaintenanceTrackName: NotRequired[str]
    DatabaseVersion: NotRequired[str]
    UpdateTargets: NotRequired[List[UpdateTargetTypeDef]]

class OrderableClusterOptionsMessageTypeDef(TypedDict):
    OrderableClusterOptions: List[OrderableClusterOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSubnetGroupTypeDef(TypedDict):
    ClusterSubnetGroupName: NotRequired[str]
    Description: NotRequired[str]
    VpcId: NotRequired[str]
    SubnetGroupStatus: NotRequired[str]
    Subnets: NotRequired[List[SubnetTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]
    SupportedClusterIpAddressTypes: NotRequired[List[str]]

class AuthorizeClusterSecurityGroupIngressResultTypeDef(TypedDict):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSecurityGroupMessageTypeDef(TypedDict):
    Marker: str
    ClusterSecurityGroups: List[ClusterSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSecurityGroupResultTypeDef(TypedDict):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeClusterSecurityGroupIngressResultTypeDef(TypedDict):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAccessListTypeDef(TypedDict):
    EndpointAccessList: List[EndpointAccessTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(TypedDict):
    ClusterIdentifier: NotRequired[str]
    NodeType: NotRequired[str]
    ClusterStatus: NotRequired[str]
    ClusterAvailabilityStatus: NotRequired[str]
    ModifyStatus: NotRequired[str]
    MasterUsername: NotRequired[str]
    DBName: NotRequired[str]
    Endpoint: NotRequired[EndpointTypeDef]
    ClusterCreateTime: NotRequired[datetime]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    ClusterSecurityGroups: NotRequired[List[ClusterSecurityGroupMembershipTypeDef]]
    VpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    ClusterParameterGroups: NotRequired[List[ClusterParameterGroupStatusTypeDef]]
    ClusterSubnetGroupName: NotRequired[str]
    VpcId: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[PendingModifiedValuesTypeDef]
    ClusterVersion: NotRequired[str]
    AllowVersionUpgrade: NotRequired[bool]
    NumberOfNodes: NotRequired[int]
    PubliclyAccessible: NotRequired[bool]
    Encrypted: NotRequired[bool]
    RestoreStatus: NotRequired[RestoreStatusTypeDef]
    DataTransferProgress: NotRequired[DataTransferProgressTypeDef]
    HsmStatus: NotRequired[HsmStatusTypeDef]
    ClusterSnapshotCopyStatus: NotRequired[ClusterSnapshotCopyStatusTypeDef]
    ClusterPublicKey: NotRequired[str]
    ClusterNodes: NotRequired[List[ClusterNodeTypeDef]]
    ElasticIpStatus: NotRequired[ElasticIpStatusTypeDef]
    ClusterRevisionNumber: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    EnhancedVpcRouting: NotRequired[bool]
    IamRoles: NotRequired[List[ClusterIamRoleTypeDef]]
    PendingActions: NotRequired[List[str]]
    MaintenanceTrackName: NotRequired[str]
    ElasticResizeNumberOfNodeOptions: NotRequired[str]
    DeferredMaintenanceWindows: NotRequired[List[DeferredMaintenanceWindowTypeDef]]
    SnapshotScheduleIdentifier: NotRequired[str]
    SnapshotScheduleState: NotRequired[ScheduleStateType]
    ExpectedNextSnapshotScheduleTime: NotRequired[datetime]
    ExpectedNextSnapshotScheduleTimeStatus: NotRequired[str]
    NextMaintenanceWindowStartTime: NotRequired[datetime]
    ResizeInfo: NotRequired[ResizeInfoTypeDef]
    AvailabilityZoneRelocationStatus: NotRequired[str]
    ClusterNamespaceArn: NotRequired[str]
    TotalStorageCapacityInMegaBytes: NotRequired[int]
    AquaConfiguration: NotRequired[AquaConfigurationTypeDef]
    DefaultIamRoleArn: NotRequired[str]
    ReservedNodeExchangeStatus: NotRequired[ReservedNodeExchangeStatusTypeDef]
    CustomDomainName: NotRequired[str]
    CustomDomainCertificateArn: NotRequired[str]
    CustomDomainCertificateExpiryDate: NotRequired[datetime]
    MasterPasswordSecretArn: NotRequired[str]
    MasterPasswordSecretKmsKeyId: NotRequired[str]
    IpAddressType: NotRequired[str]
    MultiAZ: NotRequired[str]
    MultiAZSecondary: NotRequired[SecondaryClusterInfoTypeDef]

class RedshiftIdcApplicationTypeDef(TypedDict):
    IdcInstanceArn: NotRequired[str]
    RedshiftIdcApplicationName: NotRequired[str]
    RedshiftIdcApplicationArn: NotRequired[str]
    IdentityNamespace: NotRequired[str]
    IdcDisplayName: NotRequired[str]
    IamRoleArn: NotRequired[str]
    IdcManagedApplicationArn: NotRequired[str]
    IdcOnboardStatus: NotRequired[str]
    AuthorizedTokenIssuerList: NotRequired[List[AuthorizedTokenIssuerOutputTypeDef]]
    ServiceIntegrations: NotRequired[List[ServiceIntegrationsUnionOutputTypeDef]]

ServiceIntegrationsUnionUnionTypeDef = Union[
    ServiceIntegrationsUnionTypeDef, ServiceIntegrationsUnionOutputTypeDef
]

class GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef(TypedDict):
    Marker: str
    ReservedNodeConfigurationOptionList: List[ReservedNodeConfigurationOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionsMessageTypeDef(TypedDict):
    Marker: str
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrackListMessageTypeDef(TypedDict):
    MaintenanceTracks: List[MaintenanceTrackTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSubnetGroupMessageTypeDef(TypedDict):
    Marker: str
    ClusterSubnetGroups: List[ClusterSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSubnetGroupResultTypeDef(TypedDict):
    ClusterSubnetGroup: ClusterSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterSubnetGroupResultTypeDef(TypedDict):
    ClusterSubnetGroup: ClusterSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClustersMessageTypeDef(TypedDict):
    Marker: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSnapshotCopyResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSnapshotCopyResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverPrimaryComputeResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterDbRevisionResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterIamRolesResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterMaintenanceResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySnapshotCopyRetentionPeriodResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PauseClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResizeClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreFromClusterSnapshotResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeClusterResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RotateEncryptionKeyResultTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRedshiftIdcApplicationResultTypeDef(TypedDict):
    RedshiftIdcApplication: RedshiftIdcApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRedshiftIdcApplicationsResultTypeDef(TypedDict):
    RedshiftIdcApplications: List[RedshiftIdcApplicationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRedshiftIdcApplicationResultTypeDef(TypedDict):
    RedshiftIdcApplication: RedshiftIdcApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRedshiftIdcApplicationMessageTypeDef(TypedDict):
    IdcInstanceArn: str
    RedshiftIdcApplicationName: str
    IdcDisplayName: str
    IamRoleArn: str
    IdentityNamespace: NotRequired[str]
    AuthorizedTokenIssuerList: NotRequired[Sequence[AuthorizedTokenIssuerUnionTypeDef]]
    ServiceIntegrations: NotRequired[Sequence[ServiceIntegrationsUnionUnionTypeDef]]

class ModifyRedshiftIdcApplicationMessageTypeDef(TypedDict):
    RedshiftIdcApplicationArn: str
    IdentityNamespace: NotRequired[str]
    IamRoleArn: NotRequired[str]
    IdcDisplayName: NotRequired[str]
    AuthorizedTokenIssuerList: NotRequired[Sequence[AuthorizedTokenIssuerUnionTypeDef]]
    ServiceIntegrations: NotRequired[Sequence[ServiceIntegrationsUnionUnionTypeDef]]
