"""
Type annotations for redshift service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift import RedshiftClient

    client: RedshiftClient = boto3.client("redshift")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ActionTypeType,
    AquaConfigurationStatusType,
    DataShareStatusForConsumerType,
    DataShareStatusForProducerType,
    PartnerIntegrationStatusType,
    ReservedNodeExchangeActionTypeType,
    ScheduledActionTypeValuesType,
    SourceTypeType,
    UsageLimitBreachActionType,
    UsageLimitFeatureTypeType,
    UsageLimitLimitTypeType,
    UsageLimitPeriodType,
)
from .paginator import (
    DescribeClusterDbRevisionsPaginator,
    DescribeClusterParameterGroupsPaginator,
    DescribeClusterParametersPaginator,
    DescribeClusterSecurityGroupsPaginator,
    DescribeClusterSnapshotsPaginator,
    DescribeClustersPaginator,
    DescribeClusterSubnetGroupsPaginator,
    DescribeClusterTracksPaginator,
    DescribeClusterVersionsPaginator,
    DescribeDataSharesForConsumerPaginator,
    DescribeDataSharesForProducerPaginator,
    DescribeDataSharesPaginator,
    DescribeDefaultClusterParametersPaginator,
    DescribeEndpointAccessPaginator,
    DescribeEndpointAuthorizationPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeHsmClientCertificatesPaginator,
    DescribeHsmConfigurationsPaginator,
    DescribeNodeConfigurationOptionsPaginator,
    DescribeOrderableClusterOptionsPaginator,
    DescribeReservedNodeExchangeStatusPaginator,
    DescribeReservedNodeOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeSnapshotCopyGrantsPaginator,
    DescribeSnapshotSchedulesPaginator,
    DescribeTableRestoreStatusPaginator,
    DescribeTagsPaginator,
    DescribeUsageLimitsPaginator,
    GetReservedNodeExchangeConfigurationOptionsPaginator,
    GetReservedNodeExchangeOfferingsPaginator,
)
from .type_defs import (
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
    CreateAuthenticationProfileResultTypeDef,
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
    DataShareResponseMetadataTypeDef,
    DeleteAuthenticationProfileResultTypeDef,
    DeleteClusterResultTypeDef,
    DeleteClusterSnapshotMessageTypeDef,
    DeleteClusterSnapshotResultTypeDef,
    DescribeAuthenticationProfilesResultTypeDef,
    DescribeDataSharesForConsumerResultTypeDef,
    DescribeDataSharesForProducerResultTypeDef,
    DescribeDataSharesResultTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribePartnersOutputMessageTypeDef,
    DescribeReservedNodeExchangeStatusOutputMessageTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    DisableSnapshotCopyResultTypeDef,
    EnableSnapshotCopyResultTypeDef,
    EndpointAccessListTypeDef,
    EndpointAccessResponseMetadataTypeDef,
    EndpointAuthorizationListTypeDef,
    EndpointAuthorizationResponseMetadataTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef,
    GetReservedNodeExchangeOfferingsOutputMessageTypeDef,
    HsmClientCertificateMessageTypeDef,
    HsmConfigurationMessageTypeDef,
    LoggingStatusTypeDef,
    ModifyAquaOutputMessageTypeDef,
    ModifyAuthenticationProfileResultTypeDef,
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
    PartnerIntegrationOutputMessageTypeDef,
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
    ScheduledActionResponseMetadataTypeDef,
    ScheduledActionsMessageTypeDef,
    ScheduledActionTypeTypeDef,
    SnapshotCopyGrantMessageTypeDef,
    SnapshotMessageTypeDef,
    SnapshotScheduleResponseMetadataTypeDef,
    SnapshotSortingEntityTypeDef,
    TableRestoreStatusMessageTypeDef,
    TaggedResourceListMessageTypeDef,
    TagTypeDef,
    TrackListMessageTypeDef,
    UsageLimitListTypeDef,
    UsageLimitResponseMetadataTypeDef,
)
from .waiter import (
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

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessToClusterDeniedFault: Type[BotocoreClientError]
    AccessToSnapshotDeniedFault: Type[BotocoreClientError]
    AuthenticationProfileAlreadyExistsFault: Type[BotocoreClientError]
    AuthenticationProfileNotFoundFault: Type[BotocoreClientError]
    AuthenticationProfileQuotaExceededFault: Type[BotocoreClientError]
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    AuthorizationQuotaExceededFault: Type[BotocoreClientError]
    BatchDeleteRequestSizeExceededFault: Type[BotocoreClientError]
    BatchModifyClusterSnapshotsLimitExceededFault: Type[BotocoreClientError]
    BucketNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClusterAlreadyExistsFault: Type[BotocoreClientError]
    ClusterNotFoundFault: Type[BotocoreClientError]
    ClusterOnLatestRevisionFault: Type[BotocoreClientError]
    ClusterParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    ClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    ClusterParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    ClusterQuotaExceededFault: Type[BotocoreClientError]
    ClusterSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    ClusterSecurityGroupNotFoundFault: Type[BotocoreClientError]
    ClusterSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    ClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    ClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    ClusterSnapshotQuotaExceededFault: Type[BotocoreClientError]
    ClusterSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    ClusterSubnetGroupNotFoundFault: Type[BotocoreClientError]
    ClusterSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    ClusterSubnetQuotaExceededFault: Type[BotocoreClientError]
    CopyToRegionDisabledFault: Type[BotocoreClientError]
    DependentServiceRequestThrottlingFault: Type[BotocoreClientError]
    DependentServiceUnavailableFault: Type[BotocoreClientError]
    EndpointAlreadyExistsFault: Type[BotocoreClientError]
    EndpointAuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    EndpointAuthorizationNotFoundFault: Type[BotocoreClientError]
    EndpointAuthorizationsPerClusterLimitExceededFault: Type[BotocoreClientError]
    EndpointNotFoundFault: Type[BotocoreClientError]
    EndpointsPerAuthorizationLimitExceededFault: Type[BotocoreClientError]
    EndpointsPerClusterLimitExceededFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    HsmClientCertificateAlreadyExistsFault: Type[BotocoreClientError]
    HsmClientCertificateNotFoundFault: Type[BotocoreClientError]
    HsmClientCertificateQuotaExceededFault: Type[BotocoreClientError]
    HsmConfigurationAlreadyExistsFault: Type[BotocoreClientError]
    HsmConfigurationNotFoundFault: Type[BotocoreClientError]
    HsmConfigurationQuotaExceededFault: Type[BotocoreClientError]
    InProgressTableRestoreQuotaExceededFault: Type[BotocoreClientError]
    IncompatibleOrderableOptions: Type[BotocoreClientError]
    InsufficientClusterCapacityFault: Type[BotocoreClientError]
    InsufficientS3BucketPolicyFault: Type[BotocoreClientError]
    InvalidAuthenticationProfileRequestFault: Type[BotocoreClientError]
    InvalidAuthorizationStateFault: Type[BotocoreClientError]
    InvalidClusterParameterGroupStateFault: Type[BotocoreClientError]
    InvalidClusterSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidClusterSnapshotScheduleStateFault: Type[BotocoreClientError]
    InvalidClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidClusterStateFault: Type[BotocoreClientError]
    InvalidClusterSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidClusterSubnetStateFault: Type[BotocoreClientError]
    InvalidClusterTrackFault: Type[BotocoreClientError]
    InvalidDataShareFault: Type[BotocoreClientError]
    InvalidElasticIpFault: Type[BotocoreClientError]
    InvalidEndpointStateFault: Type[BotocoreClientError]
    InvalidHsmClientCertificateStateFault: Type[BotocoreClientError]
    InvalidHsmConfigurationStateFault: Type[BotocoreClientError]
    InvalidNamespaceFault: Type[BotocoreClientError]
    InvalidReservedNodeStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidRetentionPeriodFault: Type[BotocoreClientError]
    InvalidS3BucketNameFault: Type[BotocoreClientError]
    InvalidS3KeyPrefixFault: Type[BotocoreClientError]
    InvalidScheduleFault: Type[BotocoreClientError]
    InvalidScheduledActionFault: Type[BotocoreClientError]
    InvalidSnapshotCopyGrantStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidSubscriptionStateFault: Type[BotocoreClientError]
    InvalidTableRestoreArgumentFault: Type[BotocoreClientError]
    InvalidTagFault: Type[BotocoreClientError]
    InvalidUsageLimitFault: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    NumberOfNodesPerClusterLimitExceededFault: Type[BotocoreClientError]
    NumberOfNodesQuotaExceededFault: Type[BotocoreClientError]
    PartnerNotFoundFault: Type[BotocoreClientError]
    ReservedNodeAlreadyExistsFault: Type[BotocoreClientError]
    ReservedNodeAlreadyMigratedFault: Type[BotocoreClientError]
    ReservedNodeExchangeNotFoundFault: Type[BotocoreClientError]
    ReservedNodeNotFoundFault: Type[BotocoreClientError]
    ReservedNodeOfferingNotFoundFault: Type[BotocoreClientError]
    ReservedNodeQuotaExceededFault: Type[BotocoreClientError]
    ResizeNotFoundFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    ScheduleDefinitionTypeUnsupportedFault: Type[BotocoreClientError]
    ScheduledActionAlreadyExistsFault: Type[BotocoreClientError]
    ScheduledActionNotFoundFault: Type[BotocoreClientError]
    ScheduledActionQuotaExceededFault: Type[BotocoreClientError]
    ScheduledActionTypeUnsupportedFault: Type[BotocoreClientError]
    SnapshotCopyAlreadyDisabledFault: Type[BotocoreClientError]
    SnapshotCopyAlreadyEnabledFault: Type[BotocoreClientError]
    SnapshotCopyDisabledFault: Type[BotocoreClientError]
    SnapshotCopyGrantAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotCopyGrantNotFoundFault: Type[BotocoreClientError]
    SnapshotCopyGrantQuotaExceededFault: Type[BotocoreClientError]
    SnapshotScheduleAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotScheduleNotFoundFault: Type[BotocoreClientError]
    SnapshotScheduleQuotaExceededFault: Type[BotocoreClientError]
    SnapshotScheduleUpdateInProgressFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionEventIdNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]
    SubscriptionSeverityNotFoundFault: Type[BotocoreClientError]
    TableLimitExceededFault: Type[BotocoreClientError]
    TableRestoreNotFoundFault: Type[BotocoreClientError]
    TagLimitExceededFault: Type[BotocoreClientError]
    UnauthorizedOperation: Type[BotocoreClientError]
    UnauthorizedPartnerIntegrationFault: Type[BotocoreClientError]
    UnknownSnapshotCopyRegionFault: Type[BotocoreClientError]
    UnsupportedOperationFault: Type[BotocoreClientError]
    UnsupportedOptionFault: Type[BotocoreClientError]
    UsageLimitAlreadyExistsFault: Type[BotocoreClientError]
    UsageLimitNotFoundFault: Type[BotocoreClientError]

class RedshiftClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftClient exceptions.
        """
    def accept_reserved_node_exchange(
        self, *, ReservedNodeId: str, TargetReservedNodeOfferingId: str
    ) -> AcceptReservedNodeExchangeOutputMessageTypeDef:
        """
        Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the
        configuration (term, payment type, or number of nodes) and no additional costs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.accept_reserved_node_exchange)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#accept_reserved_node_exchange)
        """
    def add_partner(
        self, *, AccountId: str, ClusterIdentifier: str, DatabaseName: str, PartnerName: str
    ) -> PartnerIntegrationOutputMessageTypeDef:
        """
        Adds a partner integration to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.add_partner)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#add_partner)
        """
    def associate_data_share_consumer(
        self, *, DataShareArn: str, AssociateEntireAccount: bool = None, ConsumerArn: str = None
    ) -> DataShareResponseMetadataTypeDef:
        """
        From a datashare consumer account, associates a datashare with the account
        (AssociateEntireAccount) or the specified namespace (ConsumerArn).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.associate_data_share_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#associate_data_share_consumer)
        """
    def authorize_cluster_security_group_ingress(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None
    ) -> AuthorizeClusterSecurityGroupIngressResultTypeDef:
        """
        Adds an inbound (ingress) rule to an Amazon Redshift security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.authorize_cluster_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_cluster_security_group_ingress)
        """
    def authorize_data_share(
        self, *, DataShareArn: str, ConsumerIdentifier: str
    ) -> DataShareResponseMetadataTypeDef:
        """
        From a data producer account, authorizes the sharing of a datashare with one or
        more consumer accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.authorize_data_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_data_share)
        """
    def authorize_endpoint_access(
        self, *, Account: str, ClusterIdentifier: str = None, VpcIds: List[str] = None
    ) -> EndpointAuthorizationResponseMetadataTypeDef:
        """
        Grants access to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.authorize_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_endpoint_access)
        """
    def authorize_snapshot_access(
        self,
        *,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None
    ) -> AuthorizeSnapshotAccessResultTypeDef:
        """
        Authorizes the specified Amazon Web Services account to restore the specified
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.authorize_snapshot_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_snapshot_access)
        """
    def batch_delete_cluster_snapshots(
        self, *, Identifiers: List["DeleteClusterSnapshotMessageTypeDef"]
    ) -> BatchDeleteClusterSnapshotsResultTypeDef:
        """
        Deletes a set of cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.batch_delete_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#batch_delete_cluster_snapshots)
        """
    def batch_modify_cluster_snapshots(
        self,
        *,
        SnapshotIdentifierList: List[str],
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None
    ) -> BatchModifyClusterSnapshotsOutputMessageTypeDef:
        """
        Modifies the settings for a set of cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.batch_modify_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#batch_modify_cluster_snapshots)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#can_paginate)
        """
    def cancel_resize(self, *, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        Cancels a resize operation for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.cancel_resize)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#cancel_resize)
        """
    def copy_cluster_snapshot(
        self,
        *,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: str = None,
        ManualSnapshotRetentionPeriod: int = None
    ) -> CopyClusterSnapshotResultTypeDef:
        """
        Copies the specified automated cluster snapshot to a new manual cluster
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.copy_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#copy_cluster_snapshot)
        """
    def create_authentication_profile(
        self, *, AuthenticationProfileName: str, AuthenticationProfileContent: str
    ) -> CreateAuthenticationProfileResultTypeDef:
        """
        Creates an authentication profile with the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_authentication_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_authentication_profile)
        """
    def create_cluster(
        self,
        *,
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
        AvailabilityZoneRelocation: bool = None,
        AquaConfigurationStatus: AquaConfigurationStatusType = None,
        DefaultIamRoleArn: str = None
    ) -> CreateClusterResultTypeDef:
        """
        Creates a new cluster with the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster)
        """
    def create_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateClusterParameterGroupResultTypeDef:
        """
        Creates an Amazon Redshift parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_parameter_group)
        """
    def create_cluster_security_group(
        self, *, ClusterSecurityGroupName: str, Description: str, Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSecurityGroupResultTypeDef:
        """
        Creates a new Amazon Redshift security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_cluster_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_security_group)
        """
    def create_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSnapshotResultTypeDef:
        """
        Creates a manual snapshot of the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_snapshot)
        """
    def create_cluster_subnet_group(
        self,
        *,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSubnetGroupResultTypeDef:
        """
        Creates a new Amazon Redshift subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_cluster_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_subnet_group)
        """
    def create_endpoint_access(
        self,
        *,
        EndpointName: str,
        SubnetGroupName: str,
        ClusterIdentifier: str = None,
        ResourceOwner: str = None,
        VpcSecurityGroupIds: List[str] = None
    ) -> EndpointAccessResponseMetadataTypeDef:
        """
        Creates a Redshift-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_endpoint_access)
        """
    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an Amazon Redshift event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_event_subscription)
        """
    def create_hsm_client_certificate(
        self, *, HsmClientCertificateIdentifier: str, Tags: List["TagTypeDef"] = None
    ) -> CreateHsmClientCertificateResultTypeDef:
        """
        Creates an HSM client certificate that an Amazon Redshift cluster will use to
        connect to the client's HSM in order to store and retrieve the keys used to
        encrypt the cluster databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_hsm_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_hsm_client_certificate)
        """
    def create_hsm_configuration(
        self,
        *,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateHsmConfigurationResultTypeDef:
        """
        Creates an HSM configuration that contains the information required by an Amazon
        Redshift cluster to store and use database encryption keys in a Hardware
        Security Module (HSM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_hsm_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_hsm_configuration)
        """
    def create_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
        TargetAction: "ScheduledActionTypeTypeDef",
        Schedule: str,
        IamRole: str,
        ScheduledActionDescription: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Enable: bool = None
    ) -> ScheduledActionResponseMetadataTypeDef:
        """
        Creates a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_scheduled_action)
        """
    def create_snapshot_copy_grant(
        self, *, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotCopyGrantResultTypeDef:
        """
        Creates a snapshot copy grant that permits Amazon Redshift to use a customer
        master key (CMK) from Key Management Service (KMS) to encrypt copied snapshots
        in a destination region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_snapshot_copy_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_snapshot_copy_grant)
        """
    def create_snapshot_schedule(
        self,
        *,
        ScheduleDefinitions: List[str] = None,
        ScheduleIdentifier: str = None,
        ScheduleDescription: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
        NextInvocations: int = None
    ) -> SnapshotScheduleResponseMetadataTypeDef:
        """
        Create a snapshot schedule that can be associated to a cluster and which
        overrides the default system backup schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_snapshot_schedule)
        """
    def create_tags(self, *, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        Adds tags to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_tags)
        """
    def create_usage_limit(
        self,
        *,
        ClusterIdentifier: str,
        FeatureType: UsageLimitFeatureTypeType,
        LimitType: UsageLimitLimitTypeType,
        Amount: int,
        Period: UsageLimitPeriodType = None,
        BreachAction: UsageLimitBreachActionType = None,
        Tags: List["TagTypeDef"] = None
    ) -> UsageLimitResponseMetadataTypeDef:
        """
        Creates a usage limit for a specified Amazon Redshift feature on a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.create_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_usage_limit)
        """
    def deauthorize_data_share(
        self, *, DataShareArn: str, ConsumerIdentifier: str
    ) -> DataShareResponseMetadataTypeDef:
        """
        From the producer account, removes authorization from the specified datashare.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.deauthorize_data_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#deauthorize_data_share)
        """
    def delete_authentication_profile(
        self, *, AuthenticationProfileName: str
    ) -> DeleteAuthenticationProfileResultTypeDef:
        """
        Deletes an authentication profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_authentication_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_authentication_profile)
        """
    def delete_cluster(
        self,
        *,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: bool = None,
        FinalClusterSnapshotIdentifier: str = None,
        FinalClusterSnapshotRetentionPeriod: int = None
    ) -> DeleteClusterResultTypeDef:
        """
        Deletes a previously provisioned cluster without its final snapshot being
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster)
        """
    def delete_cluster_parameter_group(self, *, ParameterGroupName: str) -> None:
        """
        Deletes a specified Amazon Redshift parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_parameter_group)
        """
    def delete_cluster_security_group(self, *, ClusterSecurityGroupName: str) -> None:
        """
        Deletes an Amazon Redshift security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_cluster_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_security_group)
        """
    def delete_cluster_snapshot(
        self, *, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None
    ) -> DeleteClusterSnapshotResultTypeDef:
        """
        Deletes the specified manual snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_snapshot)
        """
    def delete_cluster_subnet_group(self, *, ClusterSubnetGroupName: str) -> None:
        """
        Deletes the specified cluster subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_cluster_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_subnet_group)
        """
    def delete_endpoint_access(self, *, EndpointName: str) -> EndpointAccessResponseMetadataTypeDef:
        """
        Deletes a Redshift-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_endpoint_access)
        """
    def delete_event_subscription(self, *, SubscriptionName: str) -> None:
        """
        Deletes an Amazon Redshift event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_event_subscription)
        """
    def delete_hsm_client_certificate(self, *, HsmClientCertificateIdentifier: str) -> None:
        """
        Deletes the specified HSM client certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_hsm_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_hsm_client_certificate)
        """
    def delete_hsm_configuration(self, *, HsmConfigurationIdentifier: str) -> None:
        """
        Deletes the specified Amazon Redshift HSM configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_hsm_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_hsm_configuration)
        """
    def delete_partner(
        self, *, AccountId: str, ClusterIdentifier: str, DatabaseName: str, PartnerName: str
    ) -> PartnerIntegrationOutputMessageTypeDef:
        """
        Deletes a partner integration from a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_partner)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_partner)
        """
    def delete_scheduled_action(self, *, ScheduledActionName: str) -> None:
        """
        Deletes a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_scheduled_action)
        """
    def delete_snapshot_copy_grant(self, *, SnapshotCopyGrantName: str) -> None:
        """
        Deletes the specified snapshot copy grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_snapshot_copy_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_snapshot_copy_grant)
        """
    def delete_snapshot_schedule(self, *, ScheduleIdentifier: str) -> None:
        """
        Deletes a snapshot schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_snapshot_schedule)
        """
    def delete_tags(self, *, ResourceName: str, TagKeys: List[str]) -> None:
        """
        Deletes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_tags)
        """
    def delete_usage_limit(self, *, UsageLimitId: str) -> None:
        """
        Deletes a usage limit from a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.delete_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_usage_limit)
        """
    def describe_account_attributes(
        self, *, AttributeNames: List[str] = None
    ) -> AccountAttributeListTypeDef:
        """
        Returns a list of attributes attached to an account See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/Descr
        ibeAccountAttributes>`_ **Request Syntax** response =
        client.describe_account_attributes( AttributeNames=[ 'string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_account_attributes)
        """
    def describe_authentication_profiles(
        self, *, AuthenticationProfileName: str = None
    ) -> DescribeAuthenticationProfilesResultTypeDef:
        """
        Describes an authentication profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_authentication_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_authentication_profiles)
        """
    def describe_cluster_db_revisions(
        self, *, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClusterDbRevisionsMessageTypeDef:
        """
        Returns an array of `ClusterDbRevision` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_db_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_db_revisions)
        """
    def describe_cluster_parameter_groups(
        self,
        *,
        ParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of Amazon Redshift parameter groups, including parameter groups
        you created and the default parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_parameter_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_parameter_groups)
        """
    def describe_cluster_parameters(
        self,
        *,
        ParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ClusterParameterGroupDetailsTypeDef:
        """
        Returns a detailed list of parameters contained within the specified Amazon
        Redshift parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_parameters)
        """
    def describe_cluster_security_groups(
        self,
        *,
        ClusterSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClusterSecurityGroupMessageTypeDef:
        """
        Returns information about Amazon Redshift security groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_security_groups)
        """
    def describe_cluster_snapshots(
        self,
        *,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List["SnapshotSortingEntityTypeDef"] = None
    ) -> SnapshotMessageTypeDef:
        """
        Returns one or more snapshot objects, which contain metadata about your cluster
        snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_snapshots)
        """
    def describe_cluster_subnet_groups(
        self,
        *,
        ClusterSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClusterSubnetGroupMessageTypeDef:
        """
        Returns one or more cluster subnet group objects, which contain metadata about
        your cluster subnet groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_subnet_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_subnet_groups)
        """
    def describe_cluster_tracks(
        self, *, MaintenanceTrackName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> TrackListMessageTypeDef:
        """
        Returns a list of all the available maintenance tracks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_tracks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_tracks)
        """
    def describe_cluster_versions(
        self,
        *,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ClusterVersionsMessageTypeDef:
        """
        Returns descriptions of the available Amazon Redshift cluster versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_cluster_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_versions)
        """
    def describe_clusters(
        self,
        *,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClustersMessageTypeDef:
        """
        Returns properties of provisioned clusters including general cluster properties,
        cluster database properties, maintenance and backup properties, and security and
        access properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_clusters)
        """
    def describe_data_shares(
        self, *, DataShareArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeDataSharesResultTypeDef:
        """
        Shows the status of any inbound or outbound datashares available in the
        specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_data_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_data_shares)
        """
    def describe_data_shares_for_consumer(
        self,
        *,
        ConsumerArn: str = None,
        Status: DataShareStatusForConsumerType = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeDataSharesForConsumerResultTypeDef:
        """
        Returns a list of datashares where the account identifier being called is a
        consumer account identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_data_shares_for_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_data_shares_for_consumer)
        """
    def describe_data_shares_for_producer(
        self,
        *,
        ProducerArn: str = None,
        Status: DataShareStatusForProducerType = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeDataSharesForProducerResultTypeDef:
        """
        Returns a list of datashares when the account identifier being called is a
        producer account identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_data_shares_for_producer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_data_shares_for_producer)
        """
    def describe_default_cluster_parameters(
        self, *, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeDefaultClusterParametersResultTypeDef:
        """
        Returns a list of parameter settings for the specified parameter group family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_default_cluster_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_default_cluster_parameters)
        """
    def describe_endpoint_access(
        self,
        *,
        ClusterIdentifier: str = None,
        ResourceOwner: str = None,
        EndpointName: str = None,
        VpcId: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EndpointAccessListTypeDef:
        """
        Describes a Redshift-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_endpoint_access)
        """
    def describe_endpoint_authorization(
        self,
        *,
        ClusterIdentifier: str = None,
        Account: str = None,
        Grantee: bool = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EndpointAuthorizationListTypeDef:
        """
        Describes an endpoint authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_endpoint_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_endpoint_authorization)
        """
    def describe_event_categories(self, *, SourceType: str = None) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of event categories for all event source types, or for a
        specified source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_event_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_event_categories)
        """
    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists descriptions of all the Amazon Redshift event notification subscriptions
        for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_event_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_event_subscriptions)
        """
    def describe_events(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EventsMessageTypeDef:
        """
        Returns events related to clusters, security groups, snapshots, and parameter
        groups for the past 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_events)
        """
    def describe_hsm_client_certificates(
        self,
        *,
        HsmClientCertificateIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> HsmClientCertificateMessageTypeDef:
        """
        Returns information about the specified HSM client certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_hsm_client_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_hsm_client_certificates)
        """
    def describe_hsm_configurations(
        self,
        *,
        HsmConfigurationIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> HsmConfigurationMessageTypeDef:
        """
        Returns information about the specified Amazon Redshift HSM configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_hsm_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_hsm_configurations)
        """
    def describe_logging_status(self, *, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        Describes whether information, such as queries and connection attempts, is being
        logged for the specified Amazon Redshift cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_logging_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_logging_status)
        """
    def describe_node_configuration_options(
        self,
        *,
        ActionType: ActionTypeType,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List["NodeConfigurationOptionsFilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> NodeConfigurationOptionsMessageTypeDef:
        """
        Returns properties of possible node configurations such as node type, number of
        nodes, and disk usage for the specified action type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_node_configuration_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_node_configuration_options)
        """
    def describe_orderable_cluster_options(
        self,
        *,
        ClusterVersion: str = None,
        NodeType: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> OrderableClusterOptionsMessageTypeDef:
        """
        Returns a list of orderable cluster options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_orderable_cluster_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_orderable_cluster_options)
        """
    def describe_partners(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str = None,
        PartnerName: str = None
    ) -> DescribePartnersOutputMessageTypeDef:
        """
        Returns information about the partner integrations defined for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_partners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_partners)
        """
    def describe_reserved_node_exchange_status(
        self,
        *,
        ReservedNodeId: str = None,
        ReservedNodeExchangeRequestId: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeReservedNodeExchangeStatusOutputMessageTypeDef:
        """
        Returns exchange status details and associated metadata for a reserved-node
        exchange.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_reserved_node_exchange_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_reserved_node_exchange_status)
        """
    def describe_reserved_node_offerings(
        self, *, ReservedNodeOfferingId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodeOfferingsMessageTypeDef:
        """
        Returns a list of the available reserved node offerings by Amazon Redshift with
        their descriptions including the node type, the fixed and recurring costs of
        reserving the node and duration the node will be reserved for you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_reserved_node_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_reserved_node_offerings)
        """
    def describe_reserved_nodes(
        self, *, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodesMessageTypeDef:
        """
        Returns the descriptions of the reserved nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_reserved_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_reserved_nodes)
        """
    def describe_resize(self, *, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        Returns information about the last resize operation for the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_resize)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_resize)
        """
    def describe_scheduled_actions(
        self,
        *,
        ScheduledActionName: str = None,
        TargetActionType: ScheduledActionTypeValuesType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Active: bool = None,
        Filters: List["ScheduledActionFilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> ScheduledActionsMessageTypeDef:
        """
        Describes properties of scheduled actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_scheduled_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_scheduled_actions)
        """
    def describe_snapshot_copy_grants(
        self,
        *,
        SnapshotCopyGrantName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> SnapshotCopyGrantMessageTypeDef:
        """
        Returns a list of snapshot copy grants owned by the Amazon Web Services account
        in the destination region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_snapshot_copy_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_snapshot_copy_grants)
        """
    def describe_snapshot_schedules(
        self,
        *,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeSnapshotSchedulesOutputMessageTypeDef:
        """
        Returns a list of snapshot schedules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_snapshot_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_snapshot_schedules)
        """
    def describe_storage(self) -> CustomerStorageMessageTypeDef:
        """
        Returns account level backups storage size and provisional storage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_storage)
        """
    def describe_table_restore_status(
        self,
        *,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> TableRestoreStatusMessageTypeDef:
        """
        Lists the status of one or more table restore requests made using the
        RestoreTableFromClusterSnapshot API action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_table_restore_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_table_restore_status)
        """
    def describe_tags(
        self,
        *,
        ResourceName: str = None,
        ResourceType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> TaggedResourceListMessageTypeDef:
        """
        Returns a list of tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_tags)
        """
    def describe_usage_limits(
        self,
        *,
        UsageLimitId: str = None,
        ClusterIdentifier: str = None,
        FeatureType: UsageLimitFeatureTypeType = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> UsageLimitListTypeDef:
        """
        Shows usage limits on a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.describe_usage_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_usage_limits)
        """
    def disable_logging(self, *, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        Stops logging information, such as queries and connection attempts, for the
        specified Amazon Redshift cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.disable_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#disable_logging)
        """
    def disable_snapshot_copy(self, *, ClusterIdentifier: str) -> DisableSnapshotCopyResultTypeDef:
        """
        Disables the automatic copying of snapshots from one region to another region
        for a specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.disable_snapshot_copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#disable_snapshot_copy)
        """
    def disassociate_data_share_consumer(
        self, *, DataShareArn: str, DisassociateEntireAccount: bool = None, ConsumerArn: str = None
    ) -> DataShareResponseMetadataTypeDef:
        """
        From a consumer account, remove association for the specified datashare.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.disassociate_data_share_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#disassociate_data_share_consumer)
        """
    def enable_logging(
        self, *, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None
    ) -> LoggingStatusTypeDef:
        """
        Starts logging information, such as queries and connection attempts, for the
        specified Amazon Redshift cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.enable_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#enable_logging)
        """
    def enable_snapshot_copy(
        self,
        *,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: int = None,
        SnapshotCopyGrantName: str = None,
        ManualSnapshotRetentionPeriod: int = None
    ) -> EnableSnapshotCopyResultTypeDef:
        """
        Enables the automatic copy of snapshots from one region to another region for a
        specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.enable_snapshot_copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#enable_snapshot_copy)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#generate_presigned_url)
        """
    def get_cluster_credentials(
        self,
        *,
        DbUser: str,
        ClusterIdentifier: str,
        DbName: str = None,
        DurationSeconds: int = None,
        AutoCreate: bool = None,
        DbGroups: List[str] = None
    ) -> ClusterCredentialsTypeDef:
        """
        Returns a database user name and temporary password with temporary authorization
        to log on to an Amazon Redshift database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.get_cluster_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#get_cluster_credentials)
        """
    def get_reserved_node_exchange_configuration_options(
        self,
        *,
        ActionType: ReservedNodeExchangeActionTypeType,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef:
        """
        Gets the configuration options for the reserved-node exchange.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.get_reserved_node_exchange_configuration_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#get_reserved_node_exchange_configuration_options)
        """
    def get_reserved_node_exchange_offerings(
        self, *, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None
    ) -> GetReservedNodeExchangeOfferingsOutputMessageTypeDef:
        """
        Returns an array of DC2 ReservedNodeOfferings that matches the payment type,
        term, and usage price of the given DC1 reserved node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.get_reserved_node_exchange_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#get_reserved_node_exchange_offerings)
        """
    def modify_aqua_configuration(
        self, *, ClusterIdentifier: str, AquaConfigurationStatus: AquaConfigurationStatusType = None
    ) -> ModifyAquaOutputMessageTypeDef:
        """
        Modifies whether a cluster can use AQUA (Advanced Query Accelerator).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_aqua_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_aqua_configuration)
        """
    def modify_authentication_profile(
        self, *, AuthenticationProfileName: str, AuthenticationProfileContent: str
    ) -> ModifyAuthenticationProfileResultTypeDef:
        """
        Modifies an authentication profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_authentication_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_authentication_profile)
        """
    def modify_cluster(
        self,
        *,
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
        AvailabilityZoneRelocation: bool = None,
        AvailabilityZone: str = None,
        Port: int = None
    ) -> ModifyClusterResultTypeDef:
        """
        Modifies the settings for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster)
        """
    def modify_cluster_db_revision(
        self, *, ClusterIdentifier: str, RevisionTarget: str
    ) -> ModifyClusterDbRevisionResultTypeDef:
        """
        Modifies the database revision of a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_db_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_db_revision)
        """
    def modify_cluster_iam_roles(
        self,
        *,
        ClusterIdentifier: str,
        AddIamRoles: List[str] = None,
        RemoveIamRoles: List[str] = None,
        DefaultIamRoleArn: str = None
    ) -> ModifyClusterIamRolesResultTypeDef:
        """
        Modifies the list of Identity and Access Management (IAM) roles that can be used
        by the cluster to access other Amazon Web Services services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_iam_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_iam_roles)
        """
    def modify_cluster_maintenance(
        self,
        *,
        ClusterIdentifier: str,
        DeferMaintenance: bool = None,
        DeferMaintenanceIdentifier: str = None,
        DeferMaintenanceStartTime: Union[datetime, str] = None,
        DeferMaintenanceEndTime: Union[datetime, str] = None,
        DeferMaintenanceDuration: int = None
    ) -> ModifyClusterMaintenanceResultTypeDef:
        """
        Modifies the maintenance settings of a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_maintenance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_maintenance)
        """
    def modify_cluster_parameter_group(
        self, *, ParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_parameter_group)
        """
    def modify_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None
    ) -> ModifyClusterSnapshotResultTypeDef:
        """
        Modifies the settings for a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_snapshot)
        """
    def modify_cluster_snapshot_schedule(
        self,
        *,
        ClusterIdentifier: str,
        ScheduleIdentifier: str = None,
        DisassociateSchedule: bool = None
    ) -> None:
        """
        Modifies a snapshot schedule for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_snapshot_schedule)
        """
    def modify_cluster_subnet_group(
        self, *, ClusterSubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> ModifyClusterSubnetGroupResultTypeDef:
        """
        Modifies a cluster subnet group to include the specified list of VPC subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_cluster_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_subnet_group)
        """
    def modify_endpoint_access(
        self, *, EndpointName: str, VpcSecurityGroupIds: List[str] = None
    ) -> EndpointAccessResponseMetadataTypeDef:
        """
        Modifies a Redshift-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_endpoint_access)
        """
    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing Amazon Redshift event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_event_subscription)
        """
    def modify_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
        TargetAction: "ScheduledActionTypeTypeDef" = None,
        Schedule: str = None,
        IamRole: str = None,
        ScheduledActionDescription: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Enable: bool = None
    ) -> ScheduledActionResponseMetadataTypeDef:
        """
        Modifies a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_scheduled_action)
        """
    def modify_snapshot_copy_retention_period(
        self, *, ClusterIdentifier: str, RetentionPeriod: int, Manual: bool = None
    ) -> ModifySnapshotCopyRetentionPeriodResultTypeDef:
        """
        Modifies the number of days to retain snapshots in the destination Amazon Web
        Services Region after they are copied from the source Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_snapshot_copy_retention_period)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_snapshot_copy_retention_period)
        """
    def modify_snapshot_schedule(
        self, *, ScheduleIdentifier: str, ScheduleDefinitions: List[str]
    ) -> SnapshotScheduleResponseMetadataTypeDef:
        """
        Modifies a snapshot schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_snapshot_schedule)
        """
    def modify_usage_limit(
        self,
        *,
        UsageLimitId: str,
        Amount: int = None,
        BreachAction: UsageLimitBreachActionType = None
    ) -> UsageLimitResponseMetadataTypeDef:
        """
        Modifies a usage limit in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.modify_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_usage_limit)
        """
    def pause_cluster(self, *, ClusterIdentifier: str) -> PauseClusterResultTypeDef:
        """
        Pauses a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.pause_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#pause_cluster)
        """
    def purchase_reserved_node_offering(
        self, *, ReservedNodeOfferingId: str, NodeCount: int = None
    ) -> PurchaseReservedNodeOfferingResultTypeDef:
        """
        Allows you to purchase reserved nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.purchase_reserved_node_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#purchase_reserved_node_offering)
        """
    def reboot_cluster(self, *, ClusterIdentifier: str) -> RebootClusterResultTypeDef:
        """
        Reboots a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.reboot_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#reboot_cluster)
        """
    def reject_data_share(self, *, DataShareArn: str) -> DataShareResponseMetadataTypeDef:
        """
        From the consumer account, rejects the specified datashare.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.reject_data_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#reject_data_share)
        """
    def reset_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        Sets one or more parameters of the specified parameter group to their default
        values and sets the source values of the parameters to "engine-default".

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.reset_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#reset_cluster_parameter_group)
        """
    def resize_cluster(
        self,
        *,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        Classic: bool = None,
        ReservedNodeId: str = None,
        TargetReservedNodeOfferingId: str = None
    ) -> ResizeClusterResultTypeDef:
        """
        Changes the size of the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.resize_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#resize_cluster)
        """
    def restore_from_cluster_snapshot(
        self,
        *,
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
        AvailabilityZoneRelocation: bool = None,
        AquaConfigurationStatus: AquaConfigurationStatusType = None,
        DefaultIamRoleArn: str = None,
        ReservedNodeId: str = None,
        TargetReservedNodeOfferingId: str = None
    ) -> RestoreFromClusterSnapshotResultTypeDef:
        """
        Creates a new cluster from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.restore_from_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#restore_from_cluster_snapshot)
        """
    def restore_table_from_cluster_snapshot(
        self,
        *,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: str = None,
        TargetDatabaseName: str = None,
        TargetSchemaName: str = None,
        EnableCaseSensitiveIdentifier: bool = None
    ) -> RestoreTableFromClusterSnapshotResultTypeDef:
        """
        Creates a new table from a table in an Amazon Redshift cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.restore_table_from_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#restore_table_from_cluster_snapshot)
        """
    def resume_cluster(self, *, ClusterIdentifier: str) -> ResumeClusterResultTypeDef:
        """
        Resumes a paused cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.resume_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#resume_cluster)
        """
    def revoke_cluster_security_group_ingress(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None
    ) -> RevokeClusterSecurityGroupIngressResultTypeDef:
        """
        Revokes an ingress rule in an Amazon Redshift security group for a previously
        authorized IP range or Amazon EC2 security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.revoke_cluster_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#revoke_cluster_security_group_ingress)
        """
    def revoke_endpoint_access(
        self,
        *,
        ClusterIdentifier: str = None,
        Account: str = None,
        VpcIds: List[str] = None,
        Force: bool = None
    ) -> EndpointAuthorizationResponseMetadataTypeDef:
        """
        Revokes access to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.revoke_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#revoke_endpoint_access)
        """
    def revoke_snapshot_access(
        self,
        *,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None
    ) -> RevokeSnapshotAccessResultTypeDef:
        """
        Removes the ability of the specified Amazon Web Services account to restore the
        specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.revoke_snapshot_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#revoke_snapshot_access)
        """
    def rotate_encryption_key(self, *, ClusterIdentifier: str) -> RotateEncryptionKeyResultTypeDef:
        """
        Rotates the encryption keys for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.rotate_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#rotate_encryption_key)
        """
    def update_partner_status(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str,
        PartnerName: str,
        Status: PartnerIntegrationStatusType,
        StatusMessage: str = None
    ) -> PartnerIntegrationOutputMessageTypeDef:
        """
        Updates the status of a partner integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Client.update_partner_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#update_partner_status)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_db_revisions"]
    ) -> DescribeClusterDbRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterdbrevisionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameter_groups"]
    ) -> DescribeClusterParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparametergroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameters"]
    ) -> DescribeClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_security_groups"]
    ) -> DescribeClusterSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersecuritygroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_snapshots"]
    ) -> DescribeClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_subnet_groups"]
    ) -> DescribeClusterSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersubnetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_tracks"]
    ) -> DescribeClusterTracksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustertrackspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_versions"]
    ) -> DescribeClusterVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_shares"]
    ) -> DescribeDataSharesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeDataShares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_shares_for_consumer"]
    ) -> DescribeDataSharesForConsumerPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeDataSharesForConsumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharesforconsumerpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_shares_for_producer"]
    ) -> DescribeDataSharesForProducerPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeDataSharesForProducer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharesforproducerpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_default_cluster_parameters"]
    ) -> DescribeDefaultClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedefaultclusterparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_access"]
    ) -> DescribeEndpointAccessPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAccess)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointaccesspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_authorization"]
    ) -> DescribeEndpointAuthorizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAuthorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointauthorizationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventsubscriptionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hsm_client_certificates"]
    ) -> DescribeHsmClientCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmclientcertificatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hsm_configurations"]
    ) -> DescribeHsmConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_node_configuration_options"]
    ) -> DescribeNodeConfigurationOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describenodeconfigurationoptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_cluster_options"]
    ) -> DescribeOrderableClusterOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeorderableclusteroptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_node_exchange_status"]
    ) -> DescribeReservedNodeExchangeStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeExchangeStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeexchangestatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_node_offerings"]
    ) -> DescribeReservedNodeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeofferingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_nodes"]
    ) -> DescribeReservedNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describescheduledactionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_copy_grants"]
    ) -> DescribeSnapshotCopyGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotcopygrantspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_schedules"]
    ) -> DescribeSnapshotSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotschedulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_restore_status"]
    ) -> DescribeTableRestoreStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetablerestorestatuspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_usage_limits"]
    ) -> DescribeUsageLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeusagelimitspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_reserved_node_exchange_configuration_options"]
    ) -> GetReservedNodeExchangeConfigurationOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeConfigurationOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeconfigurationoptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_reserved_node_exchange_offerings"]
    ) -> GetReservedNodeExchangeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeofferingspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_available"]) -> ClusterAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#clusteravailablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#clusterdeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_restored"]) -> ClusterRestoredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Waiter.ClusterRestored)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#clusterrestoredwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_available"]) -> SnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#snapshotavailablewaiter)
        """
