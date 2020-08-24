# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for redshift service client

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift import RedshiftClient

    client: RedshiftClient = boto3.client("redshift")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_redshift.paginator import (
    DescribeClusterDbRevisionsPaginator,
    DescribeClusterParameterGroupsPaginator,
    DescribeClusterParametersPaginator,
    DescribeClusterSecurityGroupsPaginator,
    DescribeClusterSnapshotsPaginator,
    DescribeClustersPaginator,
    DescribeClusterSubnetGroupsPaginator,
    DescribeClusterTracksPaginator,
    DescribeClusterVersionsPaginator,
    DescribeDefaultClusterParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeHsmClientCertificatesPaginator,
    DescribeHsmConfigurationsPaginator,
    DescribeNodeConfigurationOptionsPaginator,
    DescribeOrderableClusterOptionsPaginator,
    DescribeReservedNodeOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeSnapshotCopyGrantsPaginator,
    DescribeSnapshotSchedulesPaginator,
    DescribeTableRestoreStatusPaginator,
    DescribeTagsPaginator,
    DescribeUsageLimitsPaginator,
    GetReservedNodeExchangeOfferingsPaginator,
)
from mypy_boto3_redshift.type_defs import (
    AcceptReservedNodeExchangeOutputMessageTypeDef,
    AccountAttributeListTypeDef,
    AuthorizeClusterSecurityGroupIngressResultTypeDef,
    AuthorizeSnapshotAccessResultTypeDef,
    BatchDeleteClusterSnapshotsResultTypeDef,
    BatchModifyClusterSnapshotsOutputMessageTypeDef,
    ClusterCredentialsTypeDef,
    ClusterDbRevisionsMessageTypeDef,
    ClusterParameterGroupDetailsTypeDef,
    ClusterParameterGroupNameMessageTypeDef,
    ClusterParameterGroupsMessageTypeDef,
    ClusterSecurityGroupMessageTypeDef,
    ClustersMessageTypeDef,
    ClusterSubnetGroupMessageTypeDef,
    ClusterVersionsMessageTypeDef,
    CopyClusterSnapshotResultTypeDef,
    CreateClusterParameterGroupResultTypeDef,
    CreateClusterResultTypeDef,
    CreateClusterSecurityGroupResultTypeDef,
    CreateClusterSnapshotResultTypeDef,
    CreateClusterSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateHsmClientCertificateResultTypeDef,
    CreateHsmConfigurationResultTypeDef,
    CreateSnapshotCopyGrantResultTypeDef,
    CustomerStorageMessageTypeDef,
    DeleteClusterResultTypeDef,
    DeleteClusterSnapshotMessageTypeDef,
    DeleteClusterSnapshotResultTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    DisableSnapshotCopyResultTypeDef,
    EnableSnapshotCopyResultTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    GetReservedNodeExchangeOfferingsOutputMessageTypeDef,
    HsmClientCertificateMessageTypeDef,
    HsmConfigurationMessageTypeDef,
    LoggingStatusTypeDef,
    ModifyClusterDbRevisionResultTypeDef,
    ModifyClusterIamRolesResultTypeDef,
    ModifyClusterMaintenanceResultTypeDef,
    ModifyClusterResultTypeDef,
    ModifyClusterSnapshotResultTypeDef,
    ModifyClusterSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifySnapshotCopyRetentionPeriodResultTypeDef,
    NodeConfigurationOptionsFilterTypeDef,
    NodeConfigurationOptionsMessageTypeDef,
    OrderableClusterOptionsMessageTypeDef,
    ParameterTypeDef,
    PauseClusterResultTypeDef,
    PurchaseReservedNodeOfferingResultTypeDef,
    RebootClusterResultTypeDef,
    ReservedNodeOfferingsMessageTypeDef,
    ReservedNodesMessageTypeDef,
    ResizeClusterResultTypeDef,
    ResizeProgressMessageTypeDef,
    RestoreFromClusterSnapshotResultTypeDef,
    RestoreTableFromClusterSnapshotResultTypeDef,
    ResumeClusterResultTypeDef,
    RevokeClusterSecurityGroupIngressResultTypeDef,
    RevokeSnapshotAccessResultTypeDef,
    RotateEncryptionKeyResultTypeDef,
    ScheduledActionFilterTypeDef,
    ScheduledActionsMessageTypeDef,
    ScheduledActionTypeDef,
    ScheduledActionTypeTypeDef,
    SnapshotCopyGrantMessageTypeDef,
    SnapshotMessageTypeDef,
    SnapshotScheduleTypeDef,
    SnapshotSortingEntityTypeDef,
    TableRestoreStatusMessageTypeDef,
    TaggedResourceListMessageTypeDef,
    TagTypeDef,
    TrackListMessageTypeDef,
    UsageLimitListTypeDef,
    UsageLimitTypeDef,
)
from mypy_boto3_redshift.waiter import (
    ClusterAvailableWaiter,
    ClusterDeletedWaiter,
    ClusterRestoredWaiter,
    SnapshotAvailableWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RedshiftClient",)


class Exceptions:
    AccessToSnapshotDeniedFault: Type[Boto3ClientError]
    AuthorizationAlreadyExistsFault: Type[Boto3ClientError]
    AuthorizationNotFoundFault: Type[Boto3ClientError]
    AuthorizationQuotaExceededFault: Type[Boto3ClientError]
    BatchDeleteRequestSizeExceededFault: Type[Boto3ClientError]
    BatchModifyClusterSnapshotsLimitExceededFault: Type[Boto3ClientError]
    BucketNotFoundFault: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ClusterAlreadyExistsFault: Type[Boto3ClientError]
    ClusterNotFoundFault: Type[Boto3ClientError]
    ClusterOnLatestRevisionFault: Type[Boto3ClientError]
    ClusterParameterGroupAlreadyExistsFault: Type[Boto3ClientError]
    ClusterParameterGroupNotFoundFault: Type[Boto3ClientError]
    ClusterParameterGroupQuotaExceededFault: Type[Boto3ClientError]
    ClusterQuotaExceededFault: Type[Boto3ClientError]
    ClusterSecurityGroupAlreadyExistsFault: Type[Boto3ClientError]
    ClusterSecurityGroupNotFoundFault: Type[Boto3ClientError]
    ClusterSecurityGroupQuotaExceededFault: Type[Boto3ClientError]
    ClusterSnapshotAlreadyExistsFault: Type[Boto3ClientError]
    ClusterSnapshotNotFoundFault: Type[Boto3ClientError]
    ClusterSnapshotQuotaExceededFault: Type[Boto3ClientError]
    ClusterSubnetGroupAlreadyExistsFault: Type[Boto3ClientError]
    ClusterSubnetGroupNotFoundFault: Type[Boto3ClientError]
    ClusterSubnetGroupQuotaExceededFault: Type[Boto3ClientError]
    ClusterSubnetQuotaExceededFault: Type[Boto3ClientError]
    CopyToRegionDisabledFault: Type[Boto3ClientError]
    DependentServiceRequestThrottlingFault: Type[Boto3ClientError]
    DependentServiceUnavailableFault: Type[Boto3ClientError]
    EventSubscriptionQuotaExceededFault: Type[Boto3ClientError]
    HsmClientCertificateAlreadyExistsFault: Type[Boto3ClientError]
    HsmClientCertificateNotFoundFault: Type[Boto3ClientError]
    HsmClientCertificateQuotaExceededFault: Type[Boto3ClientError]
    HsmConfigurationAlreadyExistsFault: Type[Boto3ClientError]
    HsmConfigurationNotFoundFault: Type[Boto3ClientError]
    HsmConfigurationQuotaExceededFault: Type[Boto3ClientError]
    InProgressTableRestoreQuotaExceededFault: Type[Boto3ClientError]
    IncompatibleOrderableOptions: Type[Boto3ClientError]
    InsufficientClusterCapacityFault: Type[Boto3ClientError]
    InsufficientS3BucketPolicyFault: Type[Boto3ClientError]
    InvalidClusterParameterGroupStateFault: Type[Boto3ClientError]
    InvalidClusterSecurityGroupStateFault: Type[Boto3ClientError]
    InvalidClusterSnapshotScheduleStateFault: Type[Boto3ClientError]
    InvalidClusterSnapshotStateFault: Type[Boto3ClientError]
    InvalidClusterStateFault: Type[Boto3ClientError]
    InvalidClusterSubnetGroupStateFault: Type[Boto3ClientError]
    InvalidClusterSubnetStateFault: Type[Boto3ClientError]
    InvalidClusterTrackFault: Type[Boto3ClientError]
    InvalidElasticIpFault: Type[Boto3ClientError]
    InvalidHsmClientCertificateStateFault: Type[Boto3ClientError]
    InvalidHsmConfigurationStateFault: Type[Boto3ClientError]
    InvalidReservedNodeStateFault: Type[Boto3ClientError]
    InvalidRestoreFault: Type[Boto3ClientError]
    InvalidRetentionPeriodFault: Type[Boto3ClientError]
    InvalidS3BucketNameFault: Type[Boto3ClientError]
    InvalidS3KeyPrefixFault: Type[Boto3ClientError]
    InvalidScheduleFault: Type[Boto3ClientError]
    InvalidScheduledActionFault: Type[Boto3ClientError]
    InvalidSnapshotCopyGrantStateFault: Type[Boto3ClientError]
    InvalidSubnet: Type[Boto3ClientError]
    InvalidSubscriptionStateFault: Type[Boto3ClientError]
    InvalidTableRestoreArgumentFault: Type[Boto3ClientError]
    InvalidTagFault: Type[Boto3ClientError]
    InvalidUsageLimitFault: Type[Boto3ClientError]
    InvalidVPCNetworkStateFault: Type[Boto3ClientError]
    LimitExceededFault: Type[Boto3ClientError]
    NumberOfNodesPerClusterLimitExceededFault: Type[Boto3ClientError]
    NumberOfNodesQuotaExceededFault: Type[Boto3ClientError]
    ReservedNodeAlreadyExistsFault: Type[Boto3ClientError]
    ReservedNodeAlreadyMigratedFault: Type[Boto3ClientError]
    ReservedNodeNotFoundFault: Type[Boto3ClientError]
    ReservedNodeOfferingNotFoundFault: Type[Boto3ClientError]
    ReservedNodeQuotaExceededFault: Type[Boto3ClientError]
    ResizeNotFoundFault: Type[Boto3ClientError]
    ResourceNotFoundFault: Type[Boto3ClientError]
    SNSInvalidTopicFault: Type[Boto3ClientError]
    SNSNoAuthorizationFault: Type[Boto3ClientError]
    SNSTopicArnNotFoundFault: Type[Boto3ClientError]
    ScheduleDefinitionTypeUnsupportedFault: Type[Boto3ClientError]
    ScheduledActionAlreadyExistsFault: Type[Boto3ClientError]
    ScheduledActionNotFoundFault: Type[Boto3ClientError]
    ScheduledActionQuotaExceededFault: Type[Boto3ClientError]
    ScheduledActionTypeUnsupportedFault: Type[Boto3ClientError]
    SnapshotCopyAlreadyDisabledFault: Type[Boto3ClientError]
    SnapshotCopyAlreadyEnabledFault: Type[Boto3ClientError]
    SnapshotCopyDisabledFault: Type[Boto3ClientError]
    SnapshotCopyGrantAlreadyExistsFault: Type[Boto3ClientError]
    SnapshotCopyGrantNotFoundFault: Type[Boto3ClientError]
    SnapshotCopyGrantQuotaExceededFault: Type[Boto3ClientError]
    SnapshotScheduleAlreadyExistsFault: Type[Boto3ClientError]
    SnapshotScheduleNotFoundFault: Type[Boto3ClientError]
    SnapshotScheduleQuotaExceededFault: Type[Boto3ClientError]
    SnapshotScheduleUpdateInProgressFault: Type[Boto3ClientError]
    SourceNotFoundFault: Type[Boto3ClientError]
    SubnetAlreadyInUse: Type[Boto3ClientError]
    SubscriptionAlreadyExistFault: Type[Boto3ClientError]
    SubscriptionCategoryNotFoundFault: Type[Boto3ClientError]
    SubscriptionEventIdNotFoundFault: Type[Boto3ClientError]
    SubscriptionNotFoundFault: Type[Boto3ClientError]
    SubscriptionSeverityNotFoundFault: Type[Boto3ClientError]
    TableLimitExceededFault: Type[Boto3ClientError]
    TableRestoreNotFoundFault: Type[Boto3ClientError]
    TagLimitExceededFault: Type[Boto3ClientError]
    UnauthorizedOperation: Type[Boto3ClientError]
    UnknownSnapshotCopyRegionFault: Type[Boto3ClientError]
    UnsupportedOperationFault: Type[Boto3ClientError]
    UnsupportedOptionFault: Type[Boto3ClientError]
    UsageLimitAlreadyExistsFault: Type[Boto3ClientError]
    UsageLimitNotFoundFault: Type[Boto3ClientError]


class RedshiftClient:
    """
    [Redshift.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client)
    """

    exceptions: Exceptions

    def accept_reserved_node_exchange(
        self, ReservedNodeId: str, TargetReservedNodeOfferingId: str
    ) -> AcceptReservedNodeExchangeOutputMessageTypeDef:
        """
        [Client.accept_reserved_node_exchange documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.accept_reserved_node_exchange)
        """

    def authorize_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> AuthorizeClusterSecurityGroupIngressResultTypeDef:
        """
        [Client.authorize_cluster_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.authorize_cluster_security_group_ingress)
        """

    def authorize_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None,
    ) -> AuthorizeSnapshotAccessResultTypeDef:
        """
        [Client.authorize_snapshot_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.authorize_snapshot_access)
        """

    def batch_delete_cluster_snapshots(
        self, Identifiers: List[DeleteClusterSnapshotMessageTypeDef]
    ) -> BatchDeleteClusterSnapshotsResultTypeDef:
        """
        [Client.batch_delete_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.batch_delete_cluster_snapshots)
        """

    def batch_modify_cluster_snapshots(
        self,
        SnapshotIdentifierList: List[str],
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None,
    ) -> BatchModifyClusterSnapshotsOutputMessageTypeDef:
        """
        [Client.batch_modify_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.batch_modify_cluster_snapshots)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.can_paginate)
        """

    def cancel_resize(self, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        [Client.cancel_resize documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.cancel_resize)
        """

    def copy_cluster_snapshot(
        self,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: str = None,
        ManualSnapshotRetentionPeriod: int = None,
    ) -> CopyClusterSnapshotResultTypeDef:
        """
        [Client.copy_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.copy_cluster_snapshot)
        """

    def create_cluster(
        self,
        ClusterIdentifier: str,
        NodeType: str,
        MasterUsername: str,
        MasterUserPassword: str,
        DBName: str = None,
        ClusterType: str = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ClusterSubnetGroupName: str = None,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        Port: int = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        NumberOfNodes: int = None,
        PubliclyAccessible: bool = None,
        Encrypted: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[str] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
    ) -> CreateClusterResultTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_cluster)
        """

    def create_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateClusterParameterGroupResultTypeDef:
        """
        [Client.create_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_cluster_parameter_group)
        """

    def create_cluster_security_group(
        self, ClusterSecurityGroupName: str, Description: str, Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSecurityGroupResultTypeDef:
        """
        [Client.create_cluster_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_cluster_security_group)
        """

    def create_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateClusterSnapshotResultTypeDef:
        """
        [Client.create_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_cluster_snapshot)
        """

    def create_cluster_subnet_group(
        self,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateClusterSubnetGroupResultTypeDef:
        """
        [Client.create_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_cluster_subnet_group)
        """

    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_event_subscription)
        """

    def create_hsm_client_certificate(
        self, HsmClientCertificateIdentifier: str, Tags: List["TagTypeDef"] = None
    ) -> CreateHsmClientCertificateResultTypeDef:
        """
        [Client.create_hsm_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_hsm_client_certificate)
        """

    def create_hsm_configuration(
        self,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateHsmConfigurationResultTypeDef:
        """
        [Client.create_hsm_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_hsm_configuration)
        """

    def create_scheduled_action(
        self,
        ScheduledActionName: str,
        TargetAction: "ScheduledActionTypeTypeDef",
        Schedule: str,
        IamRole: str,
        ScheduledActionDescription: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Enable: bool = None,
    ) -> "ScheduledActionTypeDef":
        """
        [Client.create_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_scheduled_action)
        """

    def create_snapshot_copy_grant(
        self, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotCopyGrantResultTypeDef:
        """
        [Client.create_snapshot_copy_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_snapshot_copy_grant)
        """

    def create_snapshot_schedule(
        self,
        ScheduleDefinitions: List[str] = None,
        ScheduleIdentifier: str = None,
        ScheduleDescription: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
        NextInvocations: int = None,
    ) -> "SnapshotScheduleTypeDef":
        """
        [Client.create_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_snapshot_schedule)
        """

    def create_tags(self, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_tags)
        """

    def create_usage_limit(
        self,
        ClusterIdentifier: str,
        FeatureType: Literal["spectrum", "concurrency-scaling"],
        LimitType: Literal["time", "data-scanned"],
        Amount: int,
        Period: Literal["daily", "weekly", "monthly"] = None,
        BreachAction: Literal["log", "emit-metric", "disable"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> "UsageLimitTypeDef":
        """
        [Client.create_usage_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.create_usage_limit)
        """

    def delete_cluster(
        self,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: bool = None,
        FinalClusterSnapshotIdentifier: str = None,
        FinalClusterSnapshotRetentionPeriod: int = None,
    ) -> DeleteClusterResultTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_cluster)
        """

    def delete_cluster_parameter_group(self, ParameterGroupName: str) -> None:
        """
        [Client.delete_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_cluster_parameter_group)
        """

    def delete_cluster_security_group(self, ClusterSecurityGroupName: str) -> None:
        """
        [Client.delete_cluster_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_cluster_security_group)
        """

    def delete_cluster_snapshot(
        self, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None
    ) -> DeleteClusterSnapshotResultTypeDef:
        """
        [Client.delete_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_cluster_snapshot)
        """

    def delete_cluster_subnet_group(self, ClusterSubnetGroupName: str) -> None:
        """
        [Client.delete_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_cluster_subnet_group)
        """

    def delete_event_subscription(self, SubscriptionName: str) -> None:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_event_subscription)
        """

    def delete_hsm_client_certificate(self, HsmClientCertificateIdentifier: str) -> None:
        """
        [Client.delete_hsm_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_hsm_client_certificate)
        """

    def delete_hsm_configuration(self, HsmConfigurationIdentifier: str) -> None:
        """
        [Client.delete_hsm_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_hsm_configuration)
        """

    def delete_scheduled_action(self, ScheduledActionName: str) -> None:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_scheduled_action)
        """

    def delete_snapshot_copy_grant(self, SnapshotCopyGrantName: str) -> None:
        """
        [Client.delete_snapshot_copy_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_snapshot_copy_grant)
        """

    def delete_snapshot_schedule(self, ScheduleIdentifier: str) -> None:
        """
        [Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_snapshot_schedule)
        """

    def delete_tags(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_tags)
        """

    def delete_usage_limit(self, UsageLimitId: str) -> None:
        """
        [Client.delete_usage_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.delete_usage_limit)
        """

    def describe_account_attributes(
        self, AttributeNames: List[str] = None
    ) -> AccountAttributeListTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_account_attributes)
        """

    def describe_cluster_db_revisions(
        self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClusterDbRevisionsMessageTypeDef:
        """
        [Client.describe_cluster_db_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_db_revisions)
        """

    def describe_cluster_parameter_groups(
        self,
        ParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClusterParameterGroupsMessageTypeDef:
        """
        [Client.describe_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_parameter_groups)
        """

    def describe_cluster_parameters(
        self,
        ParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClusterParameterGroupDetailsTypeDef:
        """
        [Client.describe_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_parameters)
        """

    def describe_cluster_security_groups(
        self,
        ClusterSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClusterSecurityGroupMessageTypeDef:
        """
        [Client.describe_cluster_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_security_groups)
        """

    def describe_cluster_snapshots(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None,
    ) -> SnapshotMessageTypeDef:
        """
        [Client.describe_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_snapshots)
        """

    def describe_cluster_subnet_groups(
        self,
        ClusterSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClusterSubnetGroupMessageTypeDef:
        """
        [Client.describe_cluster_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_subnet_groups)
        """

    def describe_cluster_tracks(
        self, MaintenanceTrackName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> TrackListMessageTypeDef:
        """
        [Client.describe_cluster_tracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_tracks)
        """

    def describe_cluster_versions(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClusterVersionsMessageTypeDef:
        """
        [Client.describe_cluster_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_cluster_versions)
        """

    def describe_clusters(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClustersMessageTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_clusters)
        """

    def describe_default_cluster_parameters(
        self, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeDefaultClusterParametersResultTypeDef:
        """
        [Client.describe_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_default_cluster_parameters)
        """

    def describe_event_categories(self, SourceType: str = None) -> EventCategoriesMessageTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_event_subscriptions)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_events)
        """

    def describe_hsm_client_certificates(
        self,
        HsmClientCertificateIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> HsmClientCertificateMessageTypeDef:
        """
        [Client.describe_hsm_client_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_hsm_client_certificates)
        """

    def describe_hsm_configurations(
        self,
        HsmConfigurationIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> HsmConfigurationMessageTypeDef:
        """
        [Client.describe_hsm_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_hsm_configurations)
        """

    def describe_logging_status(self, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        [Client.describe_logging_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_logging_status)
        """

    def describe_node_configuration_options(
        self,
        ActionType: Literal["restore-cluster", "recommend-node-config", "resize-cluster"],
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[NodeConfigurationOptionsFilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> NodeConfigurationOptionsMessageTypeDef:
        """
        [Client.describe_node_configuration_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_node_configuration_options)
        """

    def describe_orderable_cluster_options(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableClusterOptionsMessageTypeDef:
        """
        [Client.describe_orderable_cluster_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_orderable_cluster_options)
        """

    def describe_reserved_node_offerings(
        self, ReservedNodeOfferingId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodeOfferingsMessageTypeDef:
        """
        [Client.describe_reserved_node_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_reserved_node_offerings)
        """

    def describe_reserved_nodes(
        self, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodesMessageTypeDef:
        """
        [Client.describe_reserved_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_reserved_nodes)
        """

    def describe_resize(self, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        [Client.describe_resize documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_resize)
        """

    def describe_scheduled_actions(
        self,
        ScheduledActionName: str = None,
        TargetActionType: Literal["ResizeCluster", "PauseCluster", "ResumeCluster"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Active: bool = None,
        Filters: List[ScheduledActionFilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ScheduledActionsMessageTypeDef:
        """
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_scheduled_actions)
        """

    def describe_snapshot_copy_grants(
        self,
        SnapshotCopyGrantName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> SnapshotCopyGrantMessageTypeDef:
        """
        [Client.describe_snapshot_copy_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_snapshot_copy_grants)
        """

    def describe_snapshot_schedules(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeSnapshotSchedulesOutputMessageTypeDef:
        """
        [Client.describe_snapshot_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_snapshot_schedules)
        """

    def describe_storage(self) -> CustomerStorageMessageTypeDef:
        """
        [Client.describe_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_storage)
        """

    def describe_table_restore_status(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> TableRestoreStatusMessageTypeDef:
        """
        [Client.describe_table_restore_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_table_restore_status)
        """

    def describe_tags(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> TaggedResourceListMessageTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_tags)
        """

    def describe_usage_limits(
        self,
        UsageLimitId: str = None,
        ClusterIdentifier: str = None,
        FeatureType: Literal["spectrum", "concurrency-scaling"] = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> UsageLimitListTypeDef:
        """
        [Client.describe_usage_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.describe_usage_limits)
        """

    def disable_logging(self, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        [Client.disable_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.disable_logging)
        """

    def disable_snapshot_copy(self, ClusterIdentifier: str) -> DisableSnapshotCopyResultTypeDef:
        """
        [Client.disable_snapshot_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.disable_snapshot_copy)
        """

    def enable_logging(
        self, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None
    ) -> LoggingStatusTypeDef:
        """
        [Client.enable_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.enable_logging)
        """

    def enable_snapshot_copy(
        self,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: int = None,
        SnapshotCopyGrantName: str = None,
        ManualSnapshotRetentionPeriod: int = None,
    ) -> EnableSnapshotCopyResultTypeDef:
        """
        [Client.enable_snapshot_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.enable_snapshot_copy)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.generate_presigned_url)
        """

    def get_cluster_credentials(
        self,
        DbUser: str,
        ClusterIdentifier: str,
        DbName: str = None,
        DurationSeconds: int = None,
        AutoCreate: bool = None,
        DbGroups: List[str] = None,
    ) -> ClusterCredentialsTypeDef:
        """
        [Client.get_cluster_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.get_cluster_credentials)
        """

    def get_reserved_node_exchange_offerings(
        self, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None
    ) -> GetReservedNodeExchangeOfferingsOutputMessageTypeDef:
        """
        [Client.get_reserved_node_exchange_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.get_reserved_node_exchange_offerings)
        """

    def modify_cluster(
        self,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        MasterUserPassword: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        PreferredMaintenanceWindow: str = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        NewClusterIdentifier: str = None,
        PubliclyAccessible: bool = None,
        ElasticIp: str = None,
        EnhancedVpcRouting: bool = None,
        MaintenanceTrackName: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
    ) -> ModifyClusterResultTypeDef:
        """
        [Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster)
        """

    def modify_cluster_db_revision(
        self, ClusterIdentifier: str, RevisionTarget: str
    ) -> ModifyClusterDbRevisionResultTypeDef:
        """
        [Client.modify_cluster_db_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_db_revision)
        """

    def modify_cluster_iam_roles(
        self,
        ClusterIdentifier: str,
        AddIamRoles: List[str] = None,
        RemoveIamRoles: List[str] = None,
    ) -> ModifyClusterIamRolesResultTypeDef:
        """
        [Client.modify_cluster_iam_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_iam_roles)
        """

    def modify_cluster_maintenance(
        self,
        ClusterIdentifier: str,
        DeferMaintenance: bool = None,
        DeferMaintenanceIdentifier: str = None,
        DeferMaintenanceStartTime: datetime = None,
        DeferMaintenanceEndTime: datetime = None,
        DeferMaintenanceDuration: int = None,
    ) -> ModifyClusterMaintenanceResultTypeDef:
        """
        [Client.modify_cluster_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_maintenance)
        """

    def modify_cluster_parameter_group(
        self, ParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        [Client.modify_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_parameter_group)
        """

    def modify_cluster_snapshot(
        self, SnapshotIdentifier: str, ManualSnapshotRetentionPeriod: int = None, Force: bool = None
    ) -> ModifyClusterSnapshotResultTypeDef:
        """
        [Client.modify_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot)
        """

    def modify_cluster_snapshot_schedule(
        self,
        ClusterIdentifier: str,
        ScheduleIdentifier: str = None,
        DisassociateSchedule: bool = None,
    ) -> None:
        """
        [Client.modify_cluster_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot_schedule)
        """

    def modify_cluster_subnet_group(
        self, ClusterSubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> ModifyClusterSubnetGroupResultTypeDef:
        """
        [Client.modify_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_cluster_subnet_group)
        """

    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_event_subscription)
        """

    def modify_scheduled_action(
        self,
        ScheduledActionName: str,
        TargetAction: "ScheduledActionTypeTypeDef" = None,
        Schedule: str = None,
        IamRole: str = None,
        ScheduledActionDescription: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Enable: bool = None,
    ) -> "ScheduledActionTypeDef":
        """
        [Client.modify_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_scheduled_action)
        """

    def modify_snapshot_copy_retention_period(
        self, ClusterIdentifier: str, RetentionPeriod: int, Manual: bool = None
    ) -> ModifySnapshotCopyRetentionPeriodResultTypeDef:
        """
        [Client.modify_snapshot_copy_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_snapshot_copy_retention_period)
        """

    def modify_snapshot_schedule(
        self, ScheduleIdentifier: str, ScheduleDefinitions: List[str]
    ) -> "SnapshotScheduleTypeDef":
        """
        [Client.modify_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_snapshot_schedule)
        """

    def modify_usage_limit(
        self,
        UsageLimitId: str,
        Amount: int = None,
        BreachAction: Literal["log", "emit-metric", "disable"] = None,
    ) -> "UsageLimitTypeDef":
        """
        [Client.modify_usage_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.modify_usage_limit)
        """

    def pause_cluster(self, ClusterIdentifier: str) -> PauseClusterResultTypeDef:
        """
        [Client.pause_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.pause_cluster)
        """

    def purchase_reserved_node_offering(
        self, ReservedNodeOfferingId: str, NodeCount: int = None
    ) -> PurchaseReservedNodeOfferingResultTypeDef:
        """
        [Client.purchase_reserved_node_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.purchase_reserved_node_offering)
        """

    def reboot_cluster(self, ClusterIdentifier: str) -> RebootClusterResultTypeDef:
        """
        [Client.reboot_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.reboot_cluster)
        """

    def reset_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        [Client.reset_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.reset_cluster_parameter_group)
        """

    def resize_cluster(
        self,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        Classic: bool = None,
    ) -> ResizeClusterResultTypeDef:
        """
        [Client.resize_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.resize_cluster)
        """

    def restore_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        AllowVersionUpgrade: bool = None,
        ClusterSubnetGroupName: str = None,
        PubliclyAccessible: bool = None,
        OwnerAccount: str = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        ClusterParameterGroupName: str = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        KmsKeyId: str = None,
        NodeType: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[str] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
        NumberOfNodes: int = None,
    ) -> RestoreFromClusterSnapshotResultTypeDef:
        """
        [Client.restore_from_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.restore_from_cluster_snapshot)
        """

    def restore_table_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: str = None,
        TargetDatabaseName: str = None,
        TargetSchemaName: str = None,
    ) -> RestoreTableFromClusterSnapshotResultTypeDef:
        """
        [Client.restore_table_from_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.restore_table_from_cluster_snapshot)
        """

    def resume_cluster(self, ClusterIdentifier: str) -> ResumeClusterResultTypeDef:
        """
        [Client.resume_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.resume_cluster)
        """

    def revoke_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> RevokeClusterSecurityGroupIngressResultTypeDef:
        """
        [Client.revoke_cluster_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.revoke_cluster_security_group_ingress)
        """

    def revoke_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None,
    ) -> RevokeSnapshotAccessResultTypeDef:
        """
        [Client.revoke_snapshot_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.revoke_snapshot_access)
        """

    def rotate_encryption_key(self, ClusterIdentifier: str) -> RotateEncryptionKeyResultTypeDef:
        """
        [Client.rotate_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Client.rotate_encryption_key)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_db_revisions"]
    ) -> DescribeClusterDbRevisionsPaginator:
        """
        [Paginator.DescribeClusterDbRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameter_groups"]
    ) -> DescribeClusterParameterGroupsPaginator:
        """
        [Paginator.DescribeClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameters"]
    ) -> DescribeClusterParametersPaginator:
        """
        [Paginator.DescribeClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_security_groups"]
    ) -> DescribeClusterSecurityGroupsPaginator:
        """
        [Paginator.DescribeClusterSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_snapshots"]
    ) -> DescribeClusterSnapshotsPaginator:
        """
        [Paginator.DescribeClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_subnet_groups"]
    ) -> DescribeClusterSubnetGroupsPaginator:
        """
        [Paginator.DescribeClusterSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_tracks"]
    ) -> DescribeClusterTracksPaginator:
        """
        [Paginator.DescribeClusterTracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_versions"]
    ) -> DescribeClusterVersionsPaginator:
        """
        [Paginator.DescribeClusterVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_default_cluster_parameters"]
    ) -> DescribeDefaultClusterParametersPaginator:
        """
        [Paginator.DescribeDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hsm_client_certificates"]
    ) -> DescribeHsmClientCertificatesPaginator:
        """
        [Paginator.DescribeHsmClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hsm_configurations"]
    ) -> DescribeHsmConfigurationsPaginator:
        """
        [Paginator.DescribeHsmConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_node_configuration_options"]
    ) -> DescribeNodeConfigurationOptionsPaginator:
        """
        [Paginator.DescribeNodeConfigurationOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_cluster_options"]
    ) -> DescribeOrderableClusterOptionsPaginator:
        """
        [Paginator.DescribeOrderableClusterOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_node_offerings"]
    ) -> DescribeReservedNodeOfferingsPaginator:
        """
        [Paginator.DescribeReservedNodeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_nodes"]
    ) -> DescribeReservedNodesPaginator:
        """
        [Paginator.DescribeReservedNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_copy_grants"]
    ) -> DescribeSnapshotCopyGrantsPaginator:
        """
        [Paginator.DescribeSnapshotCopyGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_schedules"]
    ) -> DescribeSnapshotSchedulesPaginator:
        """
        [Paginator.DescribeSnapshotSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_restore_status"]
    ) -> DescribeTableRestoreStatusPaginator:
        """
        [Paginator.DescribeTableRestoreStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_usage_limits"]
    ) -> DescribeUsageLimitsPaginator:
        """
        [Paginator.DescribeUsageLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_reserved_node_exchange_offerings"]
    ) -> GetReservedNodeExchangeOfferingsPaginator:
        """
        [Paginator.GetReservedNodeExchangeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_available"]) -> ClusterAvailableWaiter:
        """
        [Waiter.ClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_restored"]) -> ClusterRestoredWaiter:
        """
        [Waiter.ClusterRestored documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Waiter.ClusterRestored)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_available"]) -> SnapshotAvailableWaiter:
        """
        [Waiter.SnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
