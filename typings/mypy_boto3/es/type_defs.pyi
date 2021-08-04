"""
Type annotations for es service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/type_defs.html)

Usage::

    ```python
    from mypy_boto3_es.type_defs import AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef

    data: AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AutoTuneDesiredStateType,
    AutoTuneStateType,
    DeploymentStatusType,
    DescribePackagesFilterNameType,
    DomainPackageStatusType,
    ESPartitionInstanceTypeType,
    ESWarmPartitionInstanceTypeType,
    InboundCrossClusterSearchConnectionStatusCodeType,
    LogTypeType,
    OptionStateType,
    OutboundCrossClusterSearchConnectionStatusCodeType,
    PackageStatusType,
    ReservedElasticsearchInstancePaymentOptionType,
    RollbackOnDisableType,
    ScheduledAutoTuneActionTypeType,
    ScheduledAutoTuneSeverityTypeType,
    TLSSecurityPolicyType,
    UpgradeStatusType,
    UpgradeStepType,
    VolumeTypeType,
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
    "AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AddTagsRequestRequestTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AssociatePackageRequestRequestTypeDef",
    "AssociatePackageResponseTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "ColdStorageOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "CreateElasticsearchDomainRequestRequestTypeDef",
    "CreateElasticsearchDomainResponseTypeDef",
    "CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteElasticsearchDomainRequestRequestTypeDef",
    "DeleteElasticsearchDomainResponseTypeDef",
    "DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageResponseTypeDef",
    "DescribeDomainAutoTunesRequestRequestTypeDef",
    "DescribeDomainAutoTunesResponseTypeDef",
    "DescribeElasticsearchDomainConfigRequestRequestTypeDef",
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    "DescribeElasticsearchDomainRequestRequestTypeDef",
    "DescribeElasticsearchDomainResponseTypeDef",
    "DescribeElasticsearchDomainsRequestRequestTypeDef",
    "DescribeElasticsearchDomainsResponseTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesRequestRequestTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "DescribeReservedElasticsearchInstancesRequestRequestTypeDef",
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    "DissociatePackageRequestRequestTypeDef",
    "DissociatePackageResponseTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationTypeDef",
    "DomainPackageDetailsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "ElasticsearchClusterConfigStatusTypeDef",
    "ElasticsearchClusterConfigTypeDef",
    "ElasticsearchDomainConfigTypeDef",
    "ElasticsearchDomainStatusTypeDef",
    "ElasticsearchVersionStatusTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "ErrorDetailsTypeDef",
    "FilterTypeDef",
    "GetCompatibleElasticsearchVersionsRequestRequestTypeDef",
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    "GetPackageVersionHistoryRequestRequestTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryRequestRequestTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusRequestRequestTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    "InboundCrossClusterSearchConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageRequestRequestTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListElasticsearchInstanceTypesRequestRequestTypeDef",
    "ListElasticsearchInstanceTypesResponseTypeDef",
    "ListElasticsearchVersionsRequestRequestTypeDef",
    "ListElasticsearchVersionsResponseTypeDef",
    "ListPackagesForDomainRequestRequestTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageSourceTypeDef",
    "PackageVersionHistoryTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ReservedElasticsearchInstanceOfferingTypeDef",
    "ReservedElasticsearchInstanceTypeDef",
    "ResponseMetadataTypeDef",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpdateElasticsearchDomainConfigRequestRequestTypeDef",
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    "UpdatePackageRequestRequestTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpgradeElasticsearchDomainRequestRequestTypeDef",
    "UpgradeElasticsearchDomainResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "ZoneAwarenessConfigTypeDef",
)

AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

AcceptInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
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
    },
    total=False,
)

AutoTuneOptionsOutputTypeDef = TypedDict(
    "AutoTuneOptionsOutputTypeDef",
    {
        "State": AutoTuneStateType,
        "ErrorMessage": str,
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

CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateElasticsearchDomainRequestRequestTypeDef",
    {
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCOptionsTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsInputTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsInputTypeDef",
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class CreateElasticsearchDomainRequestRequestTypeDef(
    _RequiredCreateElasticsearchDomainRequestRequestTypeDef,
    _OptionalCreateElasticsearchDomainRequestRequestTypeDef,
):
    pass

CreateElasticsearchDomainResponseTypeDef = TypedDict(
    "CreateElasticsearchDomainResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
    },
)

CreateOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
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

DeleteElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "DeleteElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "DeleteElasticsearchDomainResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

DeleteInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

DeleteOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "OutboundCrossClusterSearchConnectionTypeDef",
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

DescribeElasticsearchDomainConfigRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    {
        "DomainConfig": "ElasticsearchDomainConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainsRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainsRequestRequestTypeDef",
    {
        "DomainNames": List[str],
    },
)

DescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainsResponseTypeDef",
    {
        "DomainStatusList": List["ElasticsearchDomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef",
    {
        "InstanceType": ESPartitionInstanceTypeType,
        "ElasticsearchVersion": str,
    },
)
_OptionalDescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

class DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef(
    _RequiredDescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef,
    _OptionalDescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef,
):
    pass

DescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[str, "LimitsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["InboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["OutboundCrossClusterSearchConnectionTypeDef"],
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

DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            "ReservedElasticsearchInstanceOfferingTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedElasticsearchInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesRequestRequestTypeDef",
    {
        "ReservedElasticsearchInstanceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List["ReservedElasticsearchInstanceTypeDef"],
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
    },
    total=False,
)

_RequiredDomainInformationTypeDef = TypedDict(
    "_RequiredDomainInformationTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainInformationTypeDef = TypedDict(
    "_OptionalDomainInformationTypeDef",
    {
        "OwnerId": str,
        "Region": str,
    },
    total=False,
)

class DomainInformationTypeDef(
    _RequiredDomainInformationTypeDef, _OptionalDomainInformationTypeDef
):
    pass

DomainPackageDetailsTypeDef = TypedDict(
    "DomainPackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
        "LastUpdated": datetime,
        "DomainName": str,
        "DomainPackageStatus": DomainPackageStatusType,
        "PackageVersion": str,
        "ReferencePath": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
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
    },
    total=False,
)

ElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ElasticsearchClusterConfigStatusTypeDef",
    {
        "Options": "ElasticsearchClusterConfigTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ElasticsearchClusterConfigTypeDef = TypedDict(
    "ElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": ESPartitionInstanceTypeType,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": "ZoneAwarenessConfigTypeDef",
        "DedicatedMasterType": ESPartitionInstanceTypeType,
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": ESWarmPartitionInstanceTypeType,
        "WarmCount": int,
        "ColdStorageOptions": "ColdStorageOptionsTypeDef",
    },
    total=False,
)

ElasticsearchDomainConfigTypeDef = TypedDict(
    "ElasticsearchDomainConfigTypeDef",
    {
        "ElasticsearchVersion": "ElasticsearchVersionStatusTypeDef",
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigStatusTypeDef",
        "EBSOptions": "EBSOptionsStatusTypeDef",
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
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
    },
    total=False,
)

_RequiredElasticsearchDomainStatusTypeDef = TypedDict(
    "_RequiredElasticsearchDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
    },
)
_OptionalElasticsearchDomainStatusTypeDef = TypedDict(
    "_OptionalElasticsearchDomainStatusTypeDef",
    {
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
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
    },
    total=False,
)

class ElasticsearchDomainStatusTypeDef(
    _RequiredElasticsearchDomainStatusTypeDef, _OptionalElasticsearchDomainStatusTypeDef
):
    pass

ElasticsearchVersionStatusTypeDef = TypedDict(
    "ElasticsearchVersionStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
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

GetCompatibleElasticsearchVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

GetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    {
        "CompatibleElasticsearchVersions": List["CompatibleVersionsMapTypeDef"],
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

InboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": InboundCrossClusterSearchConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

InboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ConnectionStatus": "InboundCrossClusterSearchConnectionStatusTypeDef",
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

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "StorageTypes": List["StorageTypeTypeDef"],
        "InstanceLimits": "InstanceLimitsTypeDef",
        "AdditionalLimits": List["AdditionalLimitTypeDef"],
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

_RequiredListElasticsearchInstanceTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListElasticsearchInstanceTypesRequestRequestTypeDef",
    {
        "ElasticsearchVersion": str,
    },
)
_OptionalListElasticsearchInstanceTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListElasticsearchInstanceTypesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListElasticsearchInstanceTypesRequestRequestTypeDef(
    _RequiredListElasticsearchInstanceTypesRequestRequestTypeDef,
    _OptionalListElasticsearchInstanceTypesRequestRequestTypeDef,
):
    pass

ListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[ESPartitionInstanceTypeType],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListElasticsearchVersionsRequestRequestTypeDef = TypedDict(
    "ListElasticsearchVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListElasticsearchVersionsResponseTypeDef = TypedDict(
    "ListElasticsearchVersionsResponseTypeDef",
    {
        "ElasticsearchVersions": List[str],
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

OutboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": OutboundCrossClusterSearchConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

OutboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
    },
    total=False,
)

PackageDetailsTypeDef = TypedDict(
    "PackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
        "PackageDescription": str,
        "PackageStatus": PackageStatusType,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "AvailablePackageVersion": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
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

_RequiredPurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ReservationName": str,
    },
)
_OptionalPurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef",
    {
        "InstanceCount": int,
    },
    total=False,
)

class PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef(
    _RequiredPurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef,
    _OptionalPurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef,
):
    pass

PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {
        "ReservedElasticsearchInstanceId": str,
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

RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

RejectInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
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

ReservedElasticsearchInstanceOfferingTypeDef = TypedDict(
    "ReservedElasticsearchInstanceOfferingTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": ESPartitionInstanceTypeType,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": ReservedElasticsearchInstancePaymentOptionType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ReservedElasticsearchInstanceTypeDef = TypedDict(
    "ReservedElasticsearchInstanceTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": ESPartitionInstanceTypeType,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": ReservedElasticsearchInstancePaymentOptionType,
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

StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

StartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
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

_RequiredUpdateElasticsearchDomainConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateElasticsearchDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateElasticsearchDomainConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateElasticsearchDomainConfigRequestRequestTypeDef",
    {
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
        "EBSOptions": "EBSOptionsTypeDef",
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCOptionsTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "AccessPolicies": str,
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsInputTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsTypeDef",
    },
    total=False,
)

class UpdateElasticsearchDomainConfigRequestRequestTypeDef(
    _RequiredUpdateElasticsearchDomainConfigRequestRequestTypeDef,
    _OptionalUpdateElasticsearchDomainConfigRequestRequestTypeDef,
):
    pass

UpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    {
        "DomainConfig": "ElasticsearchDomainConfigTypeDef",
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

_RequiredUpgradeElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpgradeElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
    },
)
_OptionalUpgradeElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpgradeElasticsearchDomainRequestRequestTypeDef",
    {
        "PerformCheckOnly": bool,
    },
    total=False,
)

class UpgradeElasticsearchDomainRequestRequestTypeDef(
    _RequiredUpgradeElasticsearchDomainRequestRequestTypeDef,
    _OptionalUpgradeElasticsearchDomainRequestRequestTypeDef,
):
    pass

UpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "UpgradeElasticsearchDomainResponseTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": bool,
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

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
    total=False,
)
