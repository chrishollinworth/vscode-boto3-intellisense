"""
Type annotations for opensearch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opensearch.type_defs import AWSDomainInformationTypeDef

    data: AWSDomainInformationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionSeverityType,
    ActionStatusType,
    ActionTypeType,
    AutoTuneDesiredStateType,
    AutoTuneStateType,
    ConfigChangeStatusType,
    ConnectionModeType,
    DataSourceStatusType,
    DeploymentStatusType,
    DescribePackagesFilterNameType,
    DomainHealthType,
    DomainPackageStatusType,
    DomainProcessingStatusTypeType,
    DomainStateType,
    DryRunModeType,
    EngineTypeType,
    InboundConnectionStatusCodeType,
    InitiatedByType,
    IPAddressTypeType,
    LogTypeType,
    MaintenanceStatusType,
    MaintenanceTypeType,
    MasterNodeStatusType,
    NodeStatusType,
    NodeTypeType,
    OpenSearchPartitionInstanceTypeType,
    OpenSearchWarmPartitionInstanceTypeType,
    OptionStateType,
    OutboundConnectionStatusCodeType,
    OverallChangeStatusType,
    PackageStatusType,
    PackageTypeType,
    PrincipalTypeType,
    PropertyValueTypeType,
    ReservedInstancePaymentOptionType,
    RollbackOnDisableType,
    ScheduleAtType,
    ScheduledAutoTuneActionTypeType,
    ScheduledAutoTuneSeverityTypeType,
    ScheduledByType,
    SkipUnavailableStatusType,
    TLSSecurityPolicyType,
    UpgradeStatusType,
    UpgradeStepType,
    VolumeTypeType,
    VpcEndpointErrorCodeType,
    VpcEndpointStatusType,
    ZoneStatusType,
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
    "AWSDomainInformationTypeDef",
    "AcceptInboundConnectionRequestRequestTypeDef",
    "AcceptInboundConnectionResponseTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AddDataSourceRequestRequestTypeDef",
    "AddDataSourceResponseTypeDef",
    "AddTagsRequestRequestTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AssociatePackageRequestRequestTypeDef",
    "AssociatePackageResponseTypeDef",
    "AuthorizeVpcEndpointAccessRequestRequestTypeDef",
    "AuthorizeVpcEndpointAccessResponseTypeDef",
    "AuthorizedPrincipalTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "AvailabilityZoneInfoTypeDef",
    "CancelDomainConfigChangeRequestRequestTypeDef",
    "CancelDomainConfigChangeResponseTypeDef",
    "CancelServiceSoftwareUpdateRequestRequestTypeDef",
    "CancelServiceSoftwareUpdateResponseTypeDef",
    "CancelledChangePropertyTypeDef",
    "ChangeProgressDetailsTypeDef",
    "ChangeProgressStageTypeDef",
    "ChangeProgressStatusDetailsTypeDef",
    "ClusterConfigStatusTypeDef",
    "ClusterConfigTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "ColdStorageOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "ConnectionPropertiesTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateOutboundConnectionRequestRequestTypeDef",
    "CreateOutboundConnectionResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "CreateVpcEndpointRequestRequestTypeDef",
    "CreateVpcEndpointResponseTypeDef",
    "CrossClusterSearchConnectionPropertiesTypeDef",
    "DataSourceDetailsTypeDef",
    "DataSourceTypeTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteInboundConnectionRequestRequestTypeDef",
    "DeleteInboundConnectionResponseTypeDef",
    "DeleteOutboundConnectionRequestRequestTypeDef",
    "DeleteOutboundConnectionResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageResponseTypeDef",
    "DeleteVpcEndpointRequestRequestTypeDef",
    "DeleteVpcEndpointResponseTypeDef",
    "DescribeDomainAutoTunesRequestRequestTypeDef",
    "DescribeDomainAutoTunesResponseTypeDef",
    "DescribeDomainChangeProgressRequestRequestTypeDef",
    "DescribeDomainChangeProgressResponseTypeDef",
    "DescribeDomainConfigRequestRequestTypeDef",
    "DescribeDomainConfigResponseTypeDef",
    "DescribeDomainHealthRequestRequestTypeDef",
    "DescribeDomainHealthResponseTypeDef",
    "DescribeDomainNodesRequestRequestTypeDef",
    "DescribeDomainNodesResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeDryRunProgressRequestRequestTypeDef",
    "DescribeDryRunProgressResponseTypeDef",
    "DescribeInboundConnectionsRequestRequestTypeDef",
    "DescribeInboundConnectionsResponseTypeDef",
    "DescribeInstanceTypeLimitsRequestRequestTypeDef",
    "DescribeInstanceTypeLimitsResponseTypeDef",
    "DescribeOutboundConnectionsRequestRequestTypeDef",
    "DescribeOutboundConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesRequestRequestTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedInstanceOfferingsRequestRequestTypeDef",
    "DescribeReservedInstanceOfferingsResponseTypeDef",
    "DescribeReservedInstancesRequestRequestTypeDef",
    "DescribeReservedInstancesResponseTypeDef",
    "DescribeVpcEndpointsRequestRequestTypeDef",
    "DescribeVpcEndpointsResponseTypeDef",
    "DissociatePackageRequestRequestTypeDef",
    "DissociatePackageResponseTypeDef",
    "DomainConfigTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationContainerTypeDef",
    "DomainMaintenanceDetailsTypeDef",
    "DomainNodesStatusTypeDef",
    "DomainPackageDetailsTypeDef",
    "DomainStatusTypeDef",
    "DryRunProgressStatusTypeDef",
    "DryRunResultsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "EnvironmentInfoTypeDef",
    "ErrorDetailsTypeDef",
    "FilterTypeDef",
    "GetCompatibleVersionsRequestRequestTypeDef",
    "GetCompatibleVersionsResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetDomainMaintenanceStatusRequestRequestTypeDef",
    "GetDomainMaintenanceStatusResponseTypeDef",
    "GetPackageVersionHistoryRequestRequestTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryRequestRequestTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusRequestRequestTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "IPAddressTypeStatusTypeDef",
    "InboundConnectionStatusTypeDef",
    "InboundConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "InstanceTypeDetailsTypeDef",
    "LimitsTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListDomainMaintenancesRequestRequestTypeDef",
    "ListDomainMaintenancesResponseTypeDef",
    "ListDomainNamesRequestRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageRequestRequestTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListInstanceTypeDetailsRequestRequestTypeDef",
    "ListInstanceTypeDetailsResponseTypeDef",
    "ListPackagesForDomainRequestRequestTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListScheduledActionsRequestRequestTypeDef",
    "ListScheduledActionsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListVersionsResponseTypeDef",
    "ListVpcEndpointAccessRequestRequestTypeDef",
    "ListVpcEndpointAccessResponseTypeDef",
    "ListVpcEndpointsForDomainRequestRequestTypeDef",
    "ListVpcEndpointsForDomainResponseTypeDef",
    "ListVpcEndpointsRequestRequestTypeDef",
    "ListVpcEndpointsResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "ModifyingPropertiesTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OffPeakWindowOptionsStatusTypeDef",
    "OffPeakWindowOptionsTypeDef",
    "OffPeakWindowTypeDef",
    "OptionStatusTypeDef",
    "OutboundConnectionStatusTypeDef",
    "OutboundConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageSourceTypeDef",
    "PackageVersionHistoryTypeDef",
    "PluginPropertiesTypeDef",
    "PurchaseReservedInstanceOfferingRequestRequestTypeDef",
    "PurchaseReservedInstanceOfferingResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundConnectionRequestRequestTypeDef",
    "RejectInboundConnectionResponseTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ReservedInstanceOfferingTypeDef",
    "ReservedInstanceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeVpcEndpointAccessRequestRequestTypeDef",
    "S3GlueDataCatalogTypeDef",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "SoftwareUpdateOptionsStatusTypeDef",
    "SoftwareUpdateOptionsTypeDef",
    "StartDomainMaintenanceRequestRequestTypeDef",
    "StartDomainMaintenanceResponseTypeDef",
    "StartServiceSoftwareUpdateRequestRequestTypeDef",
    "StartServiceSoftwareUpdateResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateDomainConfigRequestRequestTypeDef",
    "UpdateDomainConfigResponseTypeDef",
    "UpdatePackageRequestRequestTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpdateScheduledActionRequestRequestTypeDef",
    "UpdateScheduledActionResponseTypeDef",
    "UpdateVpcEndpointRequestRequestTypeDef",
    "UpdateVpcEndpointResponseTypeDef",
    "UpgradeDomainRequestRequestTypeDef",
    "UpgradeDomainResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "ValidationFailureTypeDef",
    "VersionStatusTypeDef",
    "VpcEndpointErrorTypeDef",
    "VpcEndpointSummaryTypeDef",
    "VpcEndpointTypeDef",
    "WindowStartTimeTypeDef",
    "ZoneAwarenessConfigTypeDef",
)

_RequiredAWSDomainInformationTypeDef = TypedDict(
    "_RequiredAWSDomainInformationTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalAWSDomainInformationTypeDef = TypedDict(
    "_OptionalAWSDomainInformationTypeDef",
    {
        "OwnerId": str,
        "Region": str,
    },
    total=False,
)

class AWSDomainInformationTypeDef(
    _RequiredAWSDomainInformationTypeDef, _OptionalAWSDomainInformationTypeDef
):
    pass

AcceptInboundConnectionRequestRequestTypeDef = TypedDict(
    "AcceptInboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

AcceptInboundConnectionResponseTypeDef = TypedDict(
    "AcceptInboundConnectionResponseTypeDef",
    {
        "Connection": "InboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

_RequiredAddDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredAddDataSourceRequestRequestTypeDef",
    {
        "DomainName": str,
        "Name": str,
        "DataSourceType": "DataSourceTypeTypeDef",
    },
)
_OptionalAddDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalAddDataSourceRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class AddDataSourceRequestRequestTypeDef(
    _RequiredAddDataSourceRequestRequestTypeDef, _OptionalAddDataSourceRequestRequestTypeDef
):
    pass

AddDataSourceResponseTypeDef = TypedDict(
    "AddDataSourceResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsRequestRequestTypeDef = TypedDict(
    "AddTagsRequestRequestTypeDef",
    {
        "ARN": str,
        "TagList": List["TagTypeDef"],
    },
)

AdditionalLimitTypeDef = TypedDict(
    "AdditionalLimitTypeDef",
    {
        "LimitName": str,
        "LimitValues": List[str],
    },
    total=False,
)

AdvancedOptionsStatusTypeDef = TypedDict(
    "AdvancedOptionsStatusTypeDef",
    {
        "Options": Dict[str, str],
        "Status": "OptionStatusTypeDef",
    },
)

AdvancedSecurityOptionsInputTypeDef = TypedDict(
    "AdvancedSecurityOptionsInputTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "MasterUserOptions": "MasterUserOptionsTypeDef",
        "SAMLOptions": "SAMLOptionsInputTypeDef",
        "AnonymousAuthEnabled": bool,
    },
    total=False,
)

AdvancedSecurityOptionsStatusTypeDef = TypedDict(
    "AdvancedSecurityOptionsStatusTypeDef",
    {
        "Options": "AdvancedSecurityOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

AdvancedSecurityOptionsTypeDef = TypedDict(
    "AdvancedSecurityOptionsTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "SAMLOptions": "SAMLOptionsOutputTypeDef",
        "AnonymousAuthDisableDate": datetime,
        "AnonymousAuthEnabled": bool,
    },
    total=False,
)

AssociatePackageRequestRequestTypeDef = TypedDict(
    "AssociatePackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "DomainName": str,
    },
)

AssociatePackageResponseTypeDef = TypedDict(
    "AssociatePackageResponseTypeDef",
    {
        "DomainPackageDetails": "DomainPackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeVpcEndpointAccessRequestRequestTypeDef = TypedDict(
    "AuthorizeVpcEndpointAccessRequestRequestTypeDef",
    {
        "DomainName": str,
        "Account": str,
    },
)

AuthorizeVpcEndpointAccessResponseTypeDef = TypedDict(
    "AuthorizeVpcEndpointAccessResponseTypeDef",
    {
        "AuthorizedPrincipal": "AuthorizedPrincipalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizedPrincipalTypeDef = TypedDict(
    "AuthorizedPrincipalTypeDef",
    {
        "PrincipalType": PrincipalTypeType,
        "Principal": str,
    },
    total=False,
)

AutoTuneDetailsTypeDef = TypedDict(
    "AutoTuneDetailsTypeDef",
    {
        "ScheduledAutoTuneDetails": "ScheduledAutoTuneDetailsTypeDef",
    },
    total=False,
)

AutoTuneMaintenanceScheduleTypeDef = TypedDict(
    "AutoTuneMaintenanceScheduleTypeDef",
    {
        "StartAt": Union[datetime, str],
        "Duration": "DurationTypeDef",
        "CronExpressionForRecurrence": str,
    },
    total=False,
)

AutoTuneOptionsInputTypeDef = TypedDict(
    "AutoTuneOptionsInputTypeDef",
    {
        "DesiredState": AutoTuneDesiredStateType,
        "MaintenanceSchedules": List["AutoTuneMaintenanceScheduleTypeDef"],
        "UseOffPeakWindow": bool,
    },
    total=False,
)

AutoTuneOptionsOutputTypeDef = TypedDict(
    "AutoTuneOptionsOutputTypeDef",
    {
        "State": AutoTuneStateType,
        "ErrorMessage": str,
        "UseOffPeakWindow": bool,
    },
    total=False,
)

AutoTuneOptionsStatusTypeDef = TypedDict(
    "AutoTuneOptionsStatusTypeDef",
    {
        "Options": "AutoTuneOptionsTypeDef",
        "Status": "AutoTuneStatusTypeDef",
    },
    total=False,
)

AutoTuneOptionsTypeDef = TypedDict(
    "AutoTuneOptionsTypeDef",
    {
        "DesiredState": AutoTuneDesiredStateType,
        "RollbackOnDisable": RollbackOnDisableType,
        "MaintenanceSchedules": List["AutoTuneMaintenanceScheduleTypeDef"],
        "UseOffPeakWindow": bool,
    },
    total=False,
)

_RequiredAutoTuneStatusTypeDef = TypedDict(
    "_RequiredAutoTuneStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": AutoTuneStateType,
    },
)
_OptionalAutoTuneStatusTypeDef = TypedDict(
    "_OptionalAutoTuneStatusTypeDef",
    {
        "UpdateVersion": int,
        "ErrorMessage": str,
        "PendingDeletion": bool,
    },
    total=False,
)

class AutoTuneStatusTypeDef(_RequiredAutoTuneStatusTypeDef, _OptionalAutoTuneStatusTypeDef):
    pass

AutoTuneTypeDef = TypedDict(
    "AutoTuneTypeDef",
    {
        "AutoTuneType": Literal["SCHEDULED_ACTION"],
        "AutoTuneDetails": "AutoTuneDetailsTypeDef",
    },
    total=False,
)

AvailabilityZoneInfoTypeDef = TypedDict(
    "AvailabilityZoneInfoTypeDef",
    {
        "AvailabilityZoneName": str,
        "ZoneStatus": ZoneStatusType,
        "ConfiguredDataNodeCount": str,
        "AvailableDataNodeCount": str,
        "TotalShards": str,
        "TotalUnAssignedShards": str,
    },
    total=False,
)

_RequiredCancelDomainConfigChangeRequestRequestTypeDef = TypedDict(
    "_RequiredCancelDomainConfigChangeRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCancelDomainConfigChangeRequestRequestTypeDef = TypedDict(
    "_OptionalCancelDomainConfigChangeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelDomainConfigChangeRequestRequestTypeDef(
    _RequiredCancelDomainConfigChangeRequestRequestTypeDef,
    _OptionalCancelDomainConfigChangeRequestRequestTypeDef,
):
    pass

CancelDomainConfigChangeResponseTypeDef = TypedDict(
    "CancelDomainConfigChangeResponseTypeDef",
    {
        "CancelledChangeIds": List[str],
        "CancelledChangeProperties": List["CancelledChangePropertyTypeDef"],
        "DryRun": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "CancelServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "CancelServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelledChangePropertyTypeDef = TypedDict(
    "CancelledChangePropertyTypeDef",
    {
        "PropertyName": str,
        "CancelledValue": str,
        "ActiveValue": str,
    },
    total=False,
)

ChangeProgressDetailsTypeDef = TypedDict(
    "ChangeProgressDetailsTypeDef",
    {
        "ChangeId": str,
        "Message": str,
        "ConfigChangeStatus": ConfigChangeStatusType,
        "InitiatedBy": InitiatedByType,
        "StartTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ChangeProgressStageTypeDef = TypedDict(
    "ChangeProgressStageTypeDef",
    {
        "Name": str,
        "Status": str,
        "Description": str,
        "LastUpdated": datetime,
    },
    total=False,
)

ChangeProgressStatusDetailsTypeDef = TypedDict(
    "ChangeProgressStatusDetailsTypeDef",
    {
        "ChangeId": str,
        "StartTime": datetime,
        "Status": OverallChangeStatusType,
        "PendingProperties": List[str],
        "CompletedProperties": List[str],
        "TotalNumberOfStages": int,
        "ChangeProgressStages": List["ChangeProgressStageTypeDef"],
        "LastUpdatedTime": datetime,
        "ConfigChangeStatus": ConfigChangeStatusType,
        "InitiatedBy": InitiatedByType,
    },
    total=False,
)

ClusterConfigStatusTypeDef = TypedDict(
    "ClusterConfigStatusTypeDef",
    {
        "Options": "ClusterConfigTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ClusterConfigTypeDef = TypedDict(
    "ClusterConfigTypeDef",
    {
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": "ZoneAwarenessConfigTypeDef",
        "DedicatedMasterType": OpenSearchPartitionInstanceTypeType,
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": OpenSearchWarmPartitionInstanceTypeType,
        "WarmCount": int,
        "ColdStorageOptions": "ColdStorageOptionsTypeDef",
        "MultiAZWithStandbyEnabled": bool,
    },
    total=False,
)

CognitoOptionsStatusTypeDef = TypedDict(
    "CognitoOptionsStatusTypeDef",
    {
        "Options": "CognitoOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

CognitoOptionsTypeDef = TypedDict(
    "CognitoOptionsTypeDef",
    {
        "Enabled": bool,
        "UserPoolId": str,
        "IdentityPoolId": str,
        "RoleArn": str,
    },
    total=False,
)

ColdStorageOptionsTypeDef = TypedDict(
    "ColdStorageOptionsTypeDef",
    {
        "Enabled": bool,
    },
)

CompatibleVersionsMapTypeDef = TypedDict(
    "CompatibleVersionsMapTypeDef",
    {
        "SourceVersion": str,
        "TargetVersions": List[str],
    },
    total=False,
)

ConnectionPropertiesTypeDef = TypedDict(
    "ConnectionPropertiesTypeDef",
    {
        "Endpoint": str,
        "CrossClusterSearch": "CrossClusterSearchConnectionPropertiesTypeDef",
    },
    total=False,
)

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "EngineVersion": str,
        "ClusterConfig": "ClusterConfigTypeDef",
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
        "IPAddressType": IPAddressTypeType,
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCOptionsTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsInputTypeDef",
        "TagList": List["TagTypeDef"],
        "AutoTuneOptions": "AutoTuneOptionsInputTypeDef",
        "OffPeakWindowOptions": "OffPeakWindowOptionsTypeDef",
        "SoftwareUpdateOptions": "SoftwareUpdateOptionsTypeDef",
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOutboundConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOutboundConnectionRequestRequestTypeDef",
    {
        "LocalDomainInfo": "DomainInformationContainerTypeDef",
        "RemoteDomainInfo": "DomainInformationContainerTypeDef",
        "ConnectionAlias": str,
    },
)
_OptionalCreateOutboundConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOutboundConnectionRequestRequestTypeDef",
    {
        "ConnectionMode": ConnectionModeType,
        "ConnectionProperties": "ConnectionPropertiesTypeDef",
    },
    total=False,
)

class CreateOutboundConnectionRequestRequestTypeDef(
    _RequiredCreateOutboundConnectionRequestRequestTypeDef,
    _OptionalCreateOutboundConnectionRequestRequestTypeDef,
):
    pass

CreateOutboundConnectionResponseTypeDef = TypedDict(
    "CreateOutboundConnectionResponseTypeDef",
    {
        "LocalDomainInfo": "DomainInformationContainerTypeDef",
        "RemoteDomainInfo": "DomainInformationContainerTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundConnectionStatusTypeDef",
        "ConnectionId": str,
        "ConnectionMode": ConnectionModeType,
        "ConnectionProperties": "ConnectionPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
        "PackageType": PackageTypeType,
        "PackageSource": "PackageSourceTypeDef",
    },
)
_OptionalCreatePackageRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageRequestRequestTypeDef",
    {
        "PackageDescription": str,
    },
    total=False,
)

class CreatePackageRequestRequestTypeDef(
    _RequiredCreatePackageRequestRequestTypeDef, _OptionalCreatePackageRequestRequestTypeDef
):
    pass

CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcEndpointRequestRequestTypeDef",
    {
        "DomainArn": str,
        "VpcOptions": "VPCOptionsTypeDef",
    },
)
_OptionalCreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcEndpointRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateVpcEndpointRequestRequestTypeDef(
    _RequiredCreateVpcEndpointRequestRequestTypeDef, _OptionalCreateVpcEndpointRequestRequestTypeDef
):
    pass

CreateVpcEndpointResponseTypeDef = TypedDict(
    "CreateVpcEndpointResponseTypeDef",
    {
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CrossClusterSearchConnectionPropertiesTypeDef = TypedDict(
    "CrossClusterSearchConnectionPropertiesTypeDef",
    {
        "SkipUnavailable": SkipUnavailableStatusType,
    },
    total=False,
)

DataSourceDetailsTypeDef = TypedDict(
    "DataSourceDetailsTypeDef",
    {
        "DataSourceType": "DataSourceTypeTypeDef",
        "Name": str,
        "Description": str,
        "Status": DataSourceStatusType,
    },
    total=False,
)

DataSourceTypeTypeDef = TypedDict(
    "DataSourceTypeTypeDef",
    {
        "S3GlueDataCatalog": "S3GlueDataCatalogTypeDef",
    },
    total=False,
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "DomainName": str,
        "Name": str,
    },
)

DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInboundConnectionRequestRequestTypeDef = TypedDict(
    "DeleteInboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

DeleteInboundConnectionResponseTypeDef = TypedDict(
    "DeleteInboundConnectionResponseTypeDef",
    {
        "Connection": "InboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutboundConnectionRequestRequestTypeDef = TypedDict(
    "DeleteOutboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

DeleteOutboundConnectionResponseTypeDef = TypedDict(
    "DeleteOutboundConnectionResponseTypeDef",
    {
        "Connection": "OutboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePackageRequestRequestTypeDef = TypedDict(
    "DeletePackageRequestRequestTypeDef",
    {
        "PackageID": str,
    },
)

DeletePackageResponseTypeDef = TypedDict(
    "DeletePackageResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcEndpointRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointRequestRequestTypeDef",
    {
        "VpcEndpointId": str,
    },
)

DeleteVpcEndpointResponseTypeDef = TypedDict(
    "DeleteVpcEndpointResponseTypeDef",
    {
        "VpcEndpointSummary": "VpcEndpointSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainAutoTunesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainAutoTunesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDomainAutoTunesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainAutoTunesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeDomainAutoTunesRequestRequestTypeDef(
    _RequiredDescribeDomainAutoTunesRequestRequestTypeDef,
    _OptionalDescribeDomainAutoTunesRequestRequestTypeDef,
):
    pass

DescribeDomainAutoTunesResponseTypeDef = TypedDict(
    "DescribeDomainAutoTunesResponseTypeDef",
    {
        "AutoTunes": List["AutoTuneTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainChangeProgressRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainChangeProgressRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDomainChangeProgressRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainChangeProgressRequestRequestTypeDef",
    {
        "ChangeId": str,
    },
    total=False,
)

class DescribeDomainChangeProgressRequestRequestTypeDef(
    _RequiredDescribeDomainChangeProgressRequestRequestTypeDef,
    _OptionalDescribeDomainChangeProgressRequestRequestTypeDef,
):
    pass

DescribeDomainChangeProgressResponseTypeDef = TypedDict(
    "DescribeDomainChangeProgressResponseTypeDef",
    {
        "ChangeProgressStatus": "ChangeProgressStatusDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainConfigRequestRequestTypeDef = TypedDict(
    "DescribeDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeDomainConfigResponseTypeDef = TypedDict(
    "DescribeDomainConfigResponseTypeDef",
    {
        "DomainConfig": "DomainConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainHealthRequestRequestTypeDef = TypedDict(
    "DescribeDomainHealthRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeDomainHealthResponseTypeDef = TypedDict(
    "DescribeDomainHealthResponseTypeDef",
    {
        "DomainState": DomainStateType,
        "AvailabilityZoneCount": str,
        "ActiveAvailabilityZoneCount": str,
        "StandByAvailabilityZoneCount": str,
        "DataNodeCount": str,
        "DedicatedMaster": bool,
        "MasterEligibleNodeCount": str,
        "WarmNodeCount": str,
        "MasterNode": MasterNodeStatusType,
        "ClusterHealth": DomainHealthType,
        "TotalShards": str,
        "TotalUnAssignedShards": str,
        "EnvironmentInformation": List["EnvironmentInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainNodesRequestRequestTypeDef = TypedDict(
    "DescribeDomainNodesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeDomainNodesResponseTypeDef = TypedDict(
    "DescribeDomainNodesResponseTypeDef",
    {
        "DomainNodesStatusList": List["DomainNodesStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainsRequestRequestTypeDef = TypedDict(
    "DescribeDomainsRequestRequestTypeDef",
    {
        "DomainNames": List[str],
    },
)

DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef",
    {
        "DomainStatusList": List["DomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDryRunProgressRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDryRunProgressRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDryRunProgressRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDryRunProgressRequestRequestTypeDef",
    {
        "DryRunId": str,
        "LoadDryRunConfig": bool,
    },
    total=False,
)

class DescribeDryRunProgressRequestRequestTypeDef(
    _RequiredDescribeDryRunProgressRequestRequestTypeDef,
    _OptionalDescribeDryRunProgressRequestRequestTypeDef,
):
    pass

DescribeDryRunProgressResponseTypeDef = TypedDict(
    "DescribeDryRunProgressResponseTypeDef",
    {
        "DryRunProgressStatus": "DryRunProgressStatusTypeDef",
        "DryRunConfig": "DomainStatusTypeDef",
        "DryRunResults": "DryRunResultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInboundConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeInboundConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInboundConnectionsResponseTypeDef = TypedDict(
    "DescribeInboundConnectionsResponseTypeDef",
    {
        "Connections": List["InboundConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceTypeLimitsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInstanceTypeLimitsRequestRequestTypeDef",
    {
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "EngineVersion": str,
    },
)
_OptionalDescribeInstanceTypeLimitsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInstanceTypeLimitsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

class DescribeInstanceTypeLimitsRequestRequestTypeDef(
    _RequiredDescribeInstanceTypeLimitsRequestRequestTypeDef,
    _OptionalDescribeInstanceTypeLimitsRequestRequestTypeDef,
):
    pass

DescribeInstanceTypeLimitsResponseTypeDef = TypedDict(
    "DescribeInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[str, "LimitsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOutboundConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeOutboundConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOutboundConnectionsResponseTypeDef = TypedDict(
    "DescribeOutboundConnectionsResponseTypeDef",
    {
        "Connections": List["OutboundConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagesFilterTypeDef = TypedDict(
    "DescribePackagesFilterTypeDef",
    {
        "Name": DescribePackagesFilterNameType,
        "Value": List[str],
    },
    total=False,
)

DescribePackagesRequestRequestTypeDef = TypedDict(
    "DescribePackagesRequestRequestTypeDef",
    {
        "Filters": List["DescribePackagesFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribePackagesResponseTypeDef = TypedDict(
    "DescribePackagesResponseTypeDef",
    {
        "PackageDetailsList": List["PackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstanceOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstanceOfferingsRequestRequestTypeDef",
    {
        "ReservedInstanceOfferingId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReservedInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedInstanceOfferings": List["ReservedInstanceOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstanceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReservedInstancesResponseTypeDef = TypedDict(
    "DescribeReservedInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedInstances": List["ReservedInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointsRequestRequestTypeDef",
    {
        "VpcEndpointIds": List[str],
    },
)

DescribeVpcEndpointsResponseTypeDef = TypedDict(
    "DescribeVpcEndpointsResponseTypeDef",
    {
        "VpcEndpoints": List["VpcEndpointTypeDef"],
        "VpcEndpointErrors": List["VpcEndpointErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DissociatePackageRequestRequestTypeDef = TypedDict(
    "DissociatePackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "DomainName": str,
    },
)

DissociatePackageResponseTypeDef = TypedDict(
    "DissociatePackageResponseTypeDef",
    {
        "DomainPackageDetails": "DomainPackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainConfigTypeDef = TypedDict(
    "DomainConfigTypeDef",
    {
        "EngineVersion": "VersionStatusTypeDef",
        "ClusterConfig": "ClusterConfigStatusTypeDef",
        "EBSOptions": "EBSOptionsStatusTypeDef",
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "IPAddressType": "IPAddressTypeStatusTypeDef",
        "SnapshotOptions": "SnapshotOptionsStatusTypeDef",
        "VPCOptions": "VPCDerivedInfoStatusTypeDef",
        "CognitoOptions": "CognitoOptionsStatusTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsStatusTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsStatusTypeDef",
        "AdvancedOptions": "AdvancedOptionsStatusTypeDef",
        "LogPublishingOptions": "LogPublishingOptionsStatusTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsStatusTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsStatusTypeDef",
        "ChangeProgressDetails": "ChangeProgressDetailsTypeDef",
        "OffPeakWindowOptions": "OffPeakWindowOptionsStatusTypeDef",
        "SoftwareUpdateOptions": "SoftwareUpdateOptionsStatusTypeDef",
        "ModifyingProperties": List["ModifyingPropertiesTypeDef"],
    },
    total=False,
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": "DomainEndpointOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicyType,
        "CustomEndpointEnabled": bool,
        "CustomEndpoint": str,
        "CustomEndpointCertificateArn": str,
    },
    total=False,
)

DomainInfoTypeDef = TypedDict(
    "DomainInfoTypeDef",
    {
        "DomainName": str,
        "EngineType": EngineTypeType,
    },
    total=False,
)

DomainInformationContainerTypeDef = TypedDict(
    "DomainInformationContainerTypeDef",
    {
        "AWSDomainInformation": "AWSDomainInformationTypeDef",
    },
    total=False,
)

DomainMaintenanceDetailsTypeDef = TypedDict(
    "DomainMaintenanceDetailsTypeDef",
    {
        "MaintenanceId": str,
        "DomainName": str,
        "Action": MaintenanceTypeType,
        "NodeId": str,
        "Status": MaintenanceStatusType,
        "StatusMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

DomainNodesStatusTypeDef = TypedDict(
    "DomainNodesStatusTypeDef",
    {
        "NodeId": str,
        "NodeType": NodeTypeType,
        "AvailabilityZone": str,
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "NodeStatus": NodeStatusType,
        "StorageType": str,
        "StorageVolumeType": VolumeTypeType,
        "StorageSize": str,
    },
    total=False,
)

DomainPackageDetailsTypeDef = TypedDict(
    "DomainPackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": PackageTypeType,
        "LastUpdated": datetime,
        "DomainName": str,
        "DomainPackageStatus": DomainPackageStatusType,
        "PackageVersion": str,
        "ReferencePath": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

_RequiredDomainStatusTypeDef = TypedDict(
    "_RequiredDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "ClusterConfig": "ClusterConfigTypeDef",
    },
)
_OptionalDomainStatusTypeDef = TypedDict(
    "_OptionalDomainStatusTypeDef",
    {
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "EndpointV2": str,
        "Endpoints": Dict[str, str],
        "DomainEndpointV2HostedZoneId": str,
        "Processing": bool,
        "UpgradeProcessing": bool,
        "EngineVersion": str,
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
        "IPAddressType": IPAddressTypeType,
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCDerivedInfoTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsOutputTypeDef",
        "ChangeProgressDetails": "ChangeProgressDetailsTypeDef",
        "OffPeakWindowOptions": "OffPeakWindowOptionsTypeDef",
        "SoftwareUpdateOptions": "SoftwareUpdateOptionsTypeDef",
        "DomainProcessingStatus": DomainProcessingStatusTypeType,
        "ModifyingProperties": List["ModifyingPropertiesTypeDef"],
    },
    total=False,
)

class DomainStatusTypeDef(_RequiredDomainStatusTypeDef, _OptionalDomainStatusTypeDef):
    pass

_RequiredDryRunProgressStatusTypeDef = TypedDict(
    "_RequiredDryRunProgressStatusTypeDef",
    {
        "DryRunId": str,
        "DryRunStatus": str,
        "CreationDate": str,
        "UpdateDate": str,
    },
)
_OptionalDryRunProgressStatusTypeDef = TypedDict(
    "_OptionalDryRunProgressStatusTypeDef",
    {
        "ValidationFailures": List["ValidationFailureTypeDef"],
    },
    total=False,
)

class DryRunProgressStatusTypeDef(
    _RequiredDryRunProgressStatusTypeDef, _OptionalDryRunProgressStatusTypeDef
):
    pass

DryRunResultsTypeDef = TypedDict(
    "DryRunResultsTypeDef",
    {
        "DeploymentType": str,
        "Message": str,
    },
    total=False,
)

DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "Value": int,
        "Unit": Literal["HOURS"],
    },
    total=False,
)

EBSOptionsStatusTypeDef = TypedDict(
    "EBSOptionsStatusTypeDef",
    {
        "Options": "EBSOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

EBSOptionsTypeDef = TypedDict(
    "EBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": VolumeTypeType,
        "VolumeSize": int,
        "Iops": int,
        "Throughput": int,
    },
    total=False,
)

EncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "EncryptionAtRestOptionsStatusTypeDef",
    {
        "Options": "EncryptionAtRestOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

EncryptionAtRestOptionsTypeDef = TypedDict(
    "EncryptionAtRestOptionsTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

EnvironmentInfoTypeDef = TypedDict(
    "EnvironmentInfoTypeDef",
    {
        "AvailabilityZoneInformation": List["AvailabilityZoneInfoTypeDef"],
    },
    total=False,
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

GetCompatibleVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleVersionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

GetCompatibleVersionsResponseTypeDef = TypedDict(
    "GetCompatibleVersionsResponseTypeDef",
    {
        "CompatibleVersions": List["CompatibleVersionsMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "DomainName": str,
        "Name": str,
    },
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "DataSourceType": "DataSourceTypeTypeDef",
        "Name": str,
        "Description": str,
        "Status": DataSourceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainMaintenanceStatusRequestRequestTypeDef = TypedDict(
    "GetDomainMaintenanceStatusRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaintenanceId": str,
    },
)

GetDomainMaintenanceStatusResponseTypeDef = TypedDict(
    "GetDomainMaintenanceStatusResponseTypeDef",
    {
        "Status": MaintenanceStatusType,
        "StatusMessage": str,
        "NodeId": str,
        "Action": MaintenanceTypeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPackageVersionHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionHistoryRequestRequestTypeDef",
    {
        "PackageID": str,
    },
)
_OptionalGetPackageVersionHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionHistoryRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetPackageVersionHistoryRequestRequestTypeDef(
    _RequiredGetPackageVersionHistoryRequestRequestTypeDef,
    _OptionalGetPackageVersionHistoryRequestRequestTypeDef,
):
    pass

GetPackageVersionHistoryResponseTypeDef = TypedDict(
    "GetPackageVersionHistoryResponseTypeDef",
    {
        "PackageID": str,
        "PackageVersionHistoryList": List["PackageVersionHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUpgradeHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetUpgradeHistoryRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalGetUpgradeHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetUpgradeHistoryRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetUpgradeHistoryRequestRequestTypeDef(
    _RequiredGetUpgradeHistoryRequestRequestTypeDef, _OptionalGetUpgradeHistoryRequestRequestTypeDef
):
    pass

GetUpgradeHistoryResponseTypeDef = TypedDict(
    "GetUpgradeHistoryResponseTypeDef",
    {
        "UpgradeHistories": List["UpgradeHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUpgradeStatusRequestRequestTypeDef = TypedDict(
    "GetUpgradeStatusRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetUpgradeStatusResponseTypeDef = TypedDict(
    "GetUpgradeStatusResponseTypeDef",
    {
        "UpgradeStep": UpgradeStepType,
        "StepStatus": UpgradeStatusType,
        "UpgradeName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IPAddressTypeStatusTypeDef = TypedDict(
    "IPAddressTypeStatusTypeDef",
    {
        "Options": IPAddressTypeType,
        "Status": "OptionStatusTypeDef",
    },
)

InboundConnectionStatusTypeDef = TypedDict(
    "InboundConnectionStatusTypeDef",
    {
        "StatusCode": InboundConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

InboundConnectionTypeDef = TypedDict(
    "InboundConnectionTypeDef",
    {
        "LocalDomainInfo": "DomainInformationContainerTypeDef",
        "RemoteDomainInfo": "DomainInformationContainerTypeDef",
        "ConnectionId": str,
        "ConnectionStatus": "InboundConnectionStatusTypeDef",
        "ConnectionMode": ConnectionModeType,
    },
    total=False,
)

InstanceCountLimitsTypeDef = TypedDict(
    "InstanceCountLimitsTypeDef",
    {
        "MinimumInstanceCount": int,
        "MaximumInstanceCount": int,
    },
    total=False,
)

InstanceLimitsTypeDef = TypedDict(
    "InstanceLimitsTypeDef",
    {
        "InstanceCountLimits": "InstanceCountLimitsTypeDef",
    },
    total=False,
)

InstanceTypeDetailsTypeDef = TypedDict(
    "InstanceTypeDetailsTypeDef",
    {
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "EncryptionEnabled": bool,
        "CognitoEnabled": bool,
        "AppLogsEnabled": bool,
        "AdvancedSecurityEnabled": bool,
        "WarmEnabled": bool,
        "InstanceRole": List[str],
        "AvailabilityZones": List[str],
    },
    total=False,
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "StorageTypes": List["StorageTypeTypeDef"],
        "InstanceLimits": "InstanceLimitsTypeDef",
        "AdditionalLimits": List["AdditionalLimitTypeDef"],
    },
    total=False,
)

ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "DataSources": List["DataSourceDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainMaintenancesRequestRequestTypeDef = TypedDict(
    "_RequiredListDomainMaintenancesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListDomainMaintenancesRequestRequestTypeDef = TypedDict(
    "_OptionalListDomainMaintenancesRequestRequestTypeDef",
    {
        "Action": MaintenanceTypeType,
        "Status": MaintenanceStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDomainMaintenancesRequestRequestTypeDef(
    _RequiredListDomainMaintenancesRequestRequestTypeDef,
    _OptionalListDomainMaintenancesRequestRequestTypeDef,
):
    pass

ListDomainMaintenancesResponseTypeDef = TypedDict(
    "ListDomainMaintenancesResponseTypeDef",
    {
        "DomainMaintenances": List["DomainMaintenanceDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainNamesRequestRequestTypeDef = TypedDict(
    "ListDomainNamesRequestRequestTypeDef",
    {
        "EngineType": EngineTypeType,
    },
    total=False,
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "DomainNames": List["DomainInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainsForPackageRequestRequestTypeDef = TypedDict(
    "_RequiredListDomainsForPackageRequestRequestTypeDef",
    {
        "PackageID": str,
    },
)
_OptionalListDomainsForPackageRequestRequestTypeDef = TypedDict(
    "_OptionalListDomainsForPackageRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDomainsForPackageRequestRequestTypeDef(
    _RequiredListDomainsForPackageRequestRequestTypeDef,
    _OptionalListDomainsForPackageRequestRequestTypeDef,
):
    pass

ListDomainsForPackageResponseTypeDef = TypedDict(
    "ListDomainsForPackageResponseTypeDef",
    {
        "DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceTypeDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceTypeDetailsRequestRequestTypeDef",
    {
        "EngineVersion": str,
    },
)
_OptionalListInstanceTypeDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceTypeDetailsRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": int,
        "NextToken": str,
        "RetrieveAZs": bool,
        "InstanceType": str,
    },
    total=False,
)

class ListInstanceTypeDetailsRequestRequestTypeDef(
    _RequiredListInstanceTypeDetailsRequestRequestTypeDef,
    _OptionalListInstanceTypeDetailsRequestRequestTypeDef,
):
    pass

ListInstanceTypeDetailsResponseTypeDef = TypedDict(
    "ListInstanceTypeDetailsResponseTypeDef",
    {
        "InstanceTypeDetails": List["InstanceTypeDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackagesForDomainRequestRequestTypeDef = TypedDict(
    "_RequiredListPackagesForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListPackagesForDomainRequestRequestTypeDef = TypedDict(
    "_OptionalListPackagesForDomainRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPackagesForDomainRequestRequestTypeDef(
    _RequiredListPackagesForDomainRequestRequestTypeDef,
    _OptionalListPackagesForDomainRequestRequestTypeDef,
):
    pass

ListPackagesForDomainResponseTypeDef = TypedDict(
    "ListPackagesForDomainResponseTypeDef",
    {
        "DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListScheduledActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListScheduledActionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListScheduledActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListScheduledActionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListScheduledActionsRequestRequestTypeDef(
    _RequiredListScheduledActionsRequestRequestTypeDef,
    _OptionalListScheduledActionsRequestRequestTypeDef,
):
    pass

ListScheduledActionsResponseTypeDef = TypedDict(
    "ListScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ARN": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVersionsRequestRequestTypeDef = TypedDict(
    "ListVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVersionsResponseTypeDef = TypedDict(
    "ListVersionsResponseTypeDef",
    {
        "Versions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVpcEndpointAccessRequestRequestTypeDef = TypedDict(
    "_RequiredListVpcEndpointAccessRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListVpcEndpointAccessRequestRequestTypeDef = TypedDict(
    "_OptionalListVpcEndpointAccessRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListVpcEndpointAccessRequestRequestTypeDef(
    _RequiredListVpcEndpointAccessRequestRequestTypeDef,
    _OptionalListVpcEndpointAccessRequestRequestTypeDef,
):
    pass

ListVpcEndpointAccessResponseTypeDef = TypedDict(
    "ListVpcEndpointAccessResponseTypeDef",
    {
        "AuthorizedPrincipalList": List["AuthorizedPrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVpcEndpointsForDomainRequestRequestTypeDef = TypedDict(
    "_RequiredListVpcEndpointsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListVpcEndpointsForDomainRequestRequestTypeDef = TypedDict(
    "_OptionalListVpcEndpointsForDomainRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListVpcEndpointsForDomainRequestRequestTypeDef(
    _RequiredListVpcEndpointsForDomainRequestRequestTypeDef,
    _OptionalListVpcEndpointsForDomainRequestRequestTypeDef,
):
    pass

ListVpcEndpointsForDomainResponseTypeDef = TypedDict(
    "ListVpcEndpointsForDomainResponseTypeDef",
    {
        "VpcEndpointSummaryList": List["VpcEndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVpcEndpointsRequestRequestTypeDef = TypedDict(
    "ListVpcEndpointsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListVpcEndpointsResponseTypeDef = TypedDict(
    "ListVpcEndpointsResponseTypeDef",
    {
        "VpcEndpointSummaryList": List["VpcEndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogPublishingOptionTypeDef = TypedDict(
    "LogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
    total=False,
)

LogPublishingOptionsStatusTypeDef = TypedDict(
    "LogPublishingOptionsStatusTypeDef",
    {
        "Options": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "Status": "OptionStatusTypeDef",
    },
    total=False,
)

MasterUserOptionsTypeDef = TypedDict(
    "MasterUserOptionsTypeDef",
    {
        "MasterUserARN": str,
        "MasterUserName": str,
        "MasterUserPassword": str,
    },
    total=False,
)

ModifyingPropertiesTypeDef = TypedDict(
    "ModifyingPropertiesTypeDef",
    {
        "Name": str,
        "ActiveValue": str,
        "PendingValue": str,
        "ValueType": PropertyValueTypeType,
    },
    total=False,
)

NodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "Options": "NodeToNodeEncryptionOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

NodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

OffPeakWindowOptionsStatusTypeDef = TypedDict(
    "OffPeakWindowOptionsStatusTypeDef",
    {
        "Options": "OffPeakWindowOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
    total=False,
)

OffPeakWindowOptionsTypeDef = TypedDict(
    "OffPeakWindowOptionsTypeDef",
    {
        "Enabled": bool,
        "OffPeakWindow": "OffPeakWindowTypeDef",
    },
    total=False,
)

OffPeakWindowTypeDef = TypedDict(
    "OffPeakWindowTypeDef",
    {
        "WindowStartTime": "WindowStartTimeTypeDef",
    },
    total=False,
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
    },
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef",
    {
        "UpdateVersion": int,
        "PendingDeletion": bool,
    },
    total=False,
)

class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass

OutboundConnectionStatusTypeDef = TypedDict(
    "OutboundConnectionStatusTypeDef",
    {
        "StatusCode": OutboundConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

OutboundConnectionTypeDef = TypedDict(
    "OutboundConnectionTypeDef",
    {
        "LocalDomainInfo": "DomainInformationContainerTypeDef",
        "RemoteDomainInfo": "DomainInformationContainerTypeDef",
        "ConnectionId": str,
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundConnectionStatusTypeDef",
        "ConnectionMode": ConnectionModeType,
        "ConnectionProperties": "ConnectionPropertiesTypeDef",
    },
    total=False,
)

PackageDetailsTypeDef = TypedDict(
    "PackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": PackageTypeType,
        "PackageDescription": str,
        "PackageStatus": PackageStatusType,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "AvailablePackageVersion": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
        "EngineVersion": str,
        "AvailablePluginProperties": "PluginPropertiesTypeDef",
    },
    total=False,
)

PackageSourceTypeDef = TypedDict(
    "PackageSourceTypeDef",
    {
        "S3BucketName": str,
        "S3Key": str,
    },
    total=False,
)

PackageVersionHistoryTypeDef = TypedDict(
    "PackageVersionHistoryTypeDef",
    {
        "PackageVersion": str,
        "CommitMessage": str,
        "CreatedAt": datetime,
        "PluginProperties": "PluginPropertiesTypeDef",
    },
    total=False,
)

PluginPropertiesTypeDef = TypedDict(
    "PluginPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Version": str,
        "ClassName": str,
        "UncompressedSizeInBytes": int,
    },
    total=False,
)

_RequiredPurchaseReservedInstanceOfferingRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedInstanceOfferingRequestRequestTypeDef",
    {
        "ReservedInstanceOfferingId": str,
        "ReservationName": str,
    },
)
_OptionalPurchaseReservedInstanceOfferingRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedInstanceOfferingRequestRequestTypeDef",
    {
        "InstanceCount": int,
    },
    total=False,
)

class PurchaseReservedInstanceOfferingRequestRequestTypeDef(
    _RequiredPurchaseReservedInstanceOfferingRequestRequestTypeDef,
    _OptionalPurchaseReservedInstanceOfferingRequestRequestTypeDef,
):
    pass

PurchaseReservedInstanceOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedInstanceOfferingResponseTypeDef",
    {
        "ReservedInstanceId": str,
        "ReservationName": str,
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

RejectInboundConnectionRequestRequestTypeDef = TypedDict(
    "RejectInboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

RejectInboundConnectionResponseTypeDef = TypedDict(
    "RejectInboundConnectionResponseTypeDef",
    {
        "Connection": "InboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsRequestRequestTypeDef = TypedDict(
    "RemoveTagsRequestRequestTypeDef",
    {
        "ARN": str,
        "TagKeys": List[str],
    },
)

ReservedInstanceOfferingTypeDef = TypedDict(
    "ReservedInstanceOfferingTypeDef",
    {
        "ReservedInstanceOfferingId": str,
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": ReservedInstancePaymentOptionType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ReservedInstanceTypeDef = TypedDict(
    "ReservedInstanceTypeDef",
    {
        "ReservationName": str,
        "ReservedInstanceId": str,
        "BillingSubscriptionId": int,
        "ReservedInstanceOfferingId": str,
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "InstanceCount": int,
        "State": str,
        "PaymentOption": ReservedInstancePaymentOptionType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
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

RevokeVpcEndpointAccessRequestRequestTypeDef = TypedDict(
    "RevokeVpcEndpointAccessRequestRequestTypeDef",
    {
        "DomainName": str,
        "Account": str,
    },
)

S3GlueDataCatalogTypeDef = TypedDict(
    "S3GlueDataCatalogTypeDef",
    {
        "RoleArn": str,
    },
    total=False,
)

SAMLIdpTypeDef = TypedDict(
    "SAMLIdpTypeDef",
    {
        "MetadataContent": str,
        "EntityId": str,
    },
)

SAMLOptionsInputTypeDef = TypedDict(
    "SAMLOptionsInputTypeDef",
    {
        "Enabled": bool,
        "Idp": "SAMLIdpTypeDef",
        "MasterUserName": str,
        "MasterBackendRole": str,
        "SubjectKey": str,
        "RolesKey": str,
        "SessionTimeoutMinutes": int,
    },
    total=False,
)

SAMLOptionsOutputTypeDef = TypedDict(
    "SAMLOptionsOutputTypeDef",
    {
        "Enabled": bool,
        "Idp": "SAMLIdpTypeDef",
        "SubjectKey": str,
        "RolesKey": str,
        "SessionTimeoutMinutes": int,
    },
    total=False,
)

_RequiredScheduledActionTypeDef = TypedDict(
    "_RequiredScheduledActionTypeDef",
    {
        "Id": str,
        "Type": ActionTypeType,
        "Severity": ActionSeverityType,
        "ScheduledTime": int,
    },
)
_OptionalScheduledActionTypeDef = TypedDict(
    "_OptionalScheduledActionTypeDef",
    {
        "Description": str,
        "ScheduledBy": ScheduledByType,
        "Status": ActionStatusType,
        "Mandatory": bool,
        "Cancellable": bool,
    },
    total=False,
)

class ScheduledActionTypeDef(_RequiredScheduledActionTypeDef, _OptionalScheduledActionTypeDef):
    pass

ScheduledAutoTuneDetailsTypeDef = TypedDict(
    "ScheduledAutoTuneDetailsTypeDef",
    {
        "Date": datetime,
        "ActionType": ScheduledAutoTuneActionTypeType,
        "Action": str,
        "Severity": ScheduledAutoTuneSeverityTypeType,
    },
    total=False,
)

ServiceSoftwareOptionsTypeDef = TypedDict(
    "ServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": DeploymentStatusType,
        "Description": str,
        "AutomatedUpdateDate": datetime,
        "OptionalDeployment": bool,
    },
    total=False,
)

SnapshotOptionsStatusTypeDef = TypedDict(
    "SnapshotOptionsStatusTypeDef",
    {
        "Options": "SnapshotOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

SnapshotOptionsTypeDef = TypedDict(
    "SnapshotOptionsTypeDef",
    {
        "AutomatedSnapshotStartHour": int,
    },
    total=False,
)

SoftwareUpdateOptionsStatusTypeDef = TypedDict(
    "SoftwareUpdateOptionsStatusTypeDef",
    {
        "Options": "SoftwareUpdateOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
    total=False,
)

SoftwareUpdateOptionsTypeDef = TypedDict(
    "SoftwareUpdateOptionsTypeDef",
    {
        "AutoSoftwareUpdateEnabled": bool,
    },
    total=False,
)

_RequiredStartDomainMaintenanceRequestRequestTypeDef = TypedDict(
    "_RequiredStartDomainMaintenanceRequestRequestTypeDef",
    {
        "DomainName": str,
        "Action": MaintenanceTypeType,
    },
)
_OptionalStartDomainMaintenanceRequestRequestTypeDef = TypedDict(
    "_OptionalStartDomainMaintenanceRequestRequestTypeDef",
    {
        "NodeId": str,
    },
    total=False,
)

class StartDomainMaintenanceRequestRequestTypeDef(
    _RequiredStartDomainMaintenanceRequestRequestTypeDef,
    _OptionalStartDomainMaintenanceRequestRequestTypeDef,
):
    pass

StartDomainMaintenanceResponseTypeDef = TypedDict(
    "StartDomainMaintenanceResponseTypeDef",
    {
        "MaintenanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredStartServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalStartServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalStartServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "ScheduleAt": ScheduleAtType,
        "DesiredStartTime": int,
    },
    total=False,
)

class StartServiceSoftwareUpdateRequestRequestTypeDef(
    _RequiredStartServiceSoftwareUpdateRequestRequestTypeDef,
    _OptionalStartServiceSoftwareUpdateRequestRequestTypeDef,
):
    pass

StartServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "StartServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageTypeLimitTypeDef = TypedDict(
    "StorageTypeLimitTypeDef",
    {
        "LimitName": str,
        "LimitValues": List[str],
    },
    total=False,
)

StorageTypeTypeDef = TypedDict(
    "StorageTypeTypeDef",
    {
        "StorageTypeName": str,
        "StorageSubTypeName": str,
        "StorageTypeLimits": List["StorageTypeLimitTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "DomainName": str,
        "Name": str,
        "DataSourceType": "DataSourceTypeTypeDef",
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "Description": str,
        "Status": DataSourceStatusType,
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainConfigRequestRequestTypeDef",
    {
        "ClusterConfig": "ClusterConfigTypeDef",
        "EBSOptions": "EBSOptionsTypeDef",
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCOptionsTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "AccessPolicies": str,
        "IPAddressType": IPAddressTypeType,
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsInputTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsTypeDef",
        "DryRun": bool,
        "DryRunMode": DryRunModeType,
        "OffPeakWindowOptions": "OffPeakWindowOptionsTypeDef",
        "SoftwareUpdateOptions": "SoftwareUpdateOptionsTypeDef",
    },
    total=False,
)

class UpdateDomainConfigRequestRequestTypeDef(
    _RequiredUpdateDomainConfigRequestRequestTypeDef,
    _OptionalUpdateDomainConfigRequestRequestTypeDef,
):
    pass

UpdateDomainConfigResponseTypeDef = TypedDict(
    "UpdateDomainConfigResponseTypeDef",
    {
        "DomainConfig": "DomainConfigTypeDef",
        "DryRunResults": "DryRunResultsTypeDef",
        "DryRunProgressStatus": "DryRunProgressStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "PackageSource": "PackageSourceTypeDef",
    },
)
_OptionalUpdatePackageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageRequestRequestTypeDef",
    {
        "PackageDescription": str,
        "CommitMessage": str,
    },
    total=False,
)

class UpdatePackageRequestRequestTypeDef(
    _RequiredUpdatePackageRequestRequestTypeDef, _OptionalUpdatePackageRequestRequestTypeDef
):
    pass

UpdatePackageResponseTypeDef = TypedDict(
    "UpdatePackageResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduledActionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduledActionRequestRequestTypeDef",
    {
        "DomainName": str,
        "ActionID": str,
        "ActionType": ActionTypeType,
        "ScheduleAt": ScheduleAtType,
    },
)
_OptionalUpdateScheduledActionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduledActionRequestRequestTypeDef",
    {
        "DesiredStartTime": int,
    },
    total=False,
)

class UpdateScheduledActionRequestRequestTypeDef(
    _RequiredUpdateScheduledActionRequestRequestTypeDef,
    _OptionalUpdateScheduledActionRequestRequestTypeDef,
):
    pass

UpdateScheduledActionResponseTypeDef = TypedDict(
    "UpdateScheduledActionResponseTypeDef",
    {
        "ScheduledAction": "ScheduledActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVpcEndpointRequestRequestTypeDef = TypedDict(
    "UpdateVpcEndpointRequestRequestTypeDef",
    {
        "VpcEndpointId": str,
        "VpcOptions": "VPCOptionsTypeDef",
    },
)

UpdateVpcEndpointResponseTypeDef = TypedDict(
    "UpdateVpcEndpointResponseTypeDef",
    {
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpgradeDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpgradeDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
    },
)
_OptionalUpgradeDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpgradeDomainRequestRequestTypeDef",
    {
        "PerformCheckOnly": bool,
        "AdvancedOptions": Dict[str, str],
    },
    total=False,
)

class UpgradeDomainRequestRequestTypeDef(
    _RequiredUpgradeDomainRequestRequestTypeDef, _OptionalUpgradeDomainRequestRequestTypeDef
):
    pass

UpgradeDomainResponseTypeDef = TypedDict(
    "UpgradeDomainResponseTypeDef",
    {
        "UpgradeId": str,
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": bool,
        "AdvancedOptions": Dict[str, str],
        "ChangeProgressDetails": "ChangeProgressDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpgradeHistoryTypeDef = TypedDict(
    "UpgradeHistoryTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": UpgradeStatusType,
        "StepsList": List["UpgradeStepItemTypeDef"],
    },
    total=False,
)

UpgradeStepItemTypeDef = TypedDict(
    "UpgradeStepItemTypeDef",
    {
        "UpgradeStep": UpgradeStepType,
        "UpgradeStepStatus": UpgradeStatusType,
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)

VPCDerivedInfoStatusTypeDef = TypedDict(
    "VPCDerivedInfoStatusTypeDef",
    {
        "Options": "VPCDerivedInfoTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

VPCDerivedInfoTypeDef = TypedDict(
    "VPCDerivedInfoTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

VPCOptionsTypeDef = TypedDict(
    "VPCOptionsTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ValidationFailureTypeDef = TypedDict(
    "ValidationFailureTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

VersionStatusTypeDef = TypedDict(
    "VersionStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

VpcEndpointErrorTypeDef = TypedDict(
    "VpcEndpointErrorTypeDef",
    {
        "VpcEndpointId": str,
        "ErrorCode": VpcEndpointErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

VpcEndpointSummaryTypeDef = TypedDict(
    "VpcEndpointSummaryTypeDef",
    {
        "VpcEndpointId": str,
        "VpcEndpointOwner": str,
        "DomainArn": str,
        "Status": VpcEndpointStatusType,
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcEndpointOwner": str,
        "DomainArn": str,
        "VpcOptions": "VPCDerivedInfoTypeDef",
        "Status": VpcEndpointStatusType,
        "Endpoint": str,
    },
    total=False,
)

WindowStartTimeTypeDef = TypedDict(
    "WindowStartTimeTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
)

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
    total=False,
)
