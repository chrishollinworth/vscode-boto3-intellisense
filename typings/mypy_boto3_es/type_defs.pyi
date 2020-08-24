"""
Main interface for es service type definitions.

Usage::

    ```python
    from mypy_boto3_es.type_defs import AccessPoliciesStatusTypeDef

    data: AccessPoliciesStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPoliciesStatusTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationTypeDef",
    "DomainPackageDetailsTypeDef",
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
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    "InboundCrossClusterSearchConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "LimitsTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionTypeDef",
    "PackageDetailsTypeDef",
    "RecurringChargeTypeDef",
    "ReservedElasticsearchInstanceOfferingTypeDef",
    "ReservedElasticsearchInstanceTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "ZoneAwarenessConfigTypeDef",
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AssociatePackageResponseTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "CreateElasticsearchDomainResponseTypeDef",
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteElasticsearchDomainResponseTypeDef",
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    "DeletePackageResponseTypeDef",
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    "DescribeElasticsearchDomainResponseTypeDef",
    "DescribeElasticsearchDomainsResponseTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    "DissociatePackageResponseTypeDef",
    "FilterTypeDef",
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListElasticsearchInstanceTypesResponseTypeDef",
    "ListElasticsearchVersionsResponseTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListTagsResponseTypeDef",
    "PackageSourceTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    "UpgradeElasticsearchDomainResponseTypeDef",
    "VPCOptionsTypeDef",
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef", {"Options": str, "Status": "OptionStatusTypeDef"}
)

AdditionalLimitTypeDef = TypedDict(
    "AdditionalLimitTypeDef", {"LimitName": str, "LimitValues": List[str]}, total=False
)

AdvancedOptionsStatusTypeDef = TypedDict(
    "AdvancedOptionsStatusTypeDef", {"Options": Dict[str, str], "Status": "OptionStatusTypeDef"}
)

AdvancedSecurityOptionsStatusTypeDef = TypedDict(
    "AdvancedSecurityOptionsStatusTypeDef",
    {"Options": "AdvancedSecurityOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

AdvancedSecurityOptionsTypeDef = TypedDict(
    "AdvancedSecurityOptionsTypeDef",
    {"Enabled": bool, "InternalUserDatabaseEnabled": bool},
    total=False,
)

CognitoOptionsStatusTypeDef = TypedDict(
    "CognitoOptionsStatusTypeDef",
    {"Options": "CognitoOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

CognitoOptionsTypeDef = TypedDict(
    "CognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

CompatibleVersionsMapTypeDef = TypedDict(
    "CompatibleVersionsMapTypeDef", {"SourceVersion": str, "TargetVersions": List[str]}, total=False
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {"Options": "DomainEndpointOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

DomainInfoTypeDef = TypedDict("DomainInfoTypeDef", {"DomainName": str}, total=False)

_RequiredDomainInformationTypeDef = TypedDict(
    "_RequiredDomainInformationTypeDef", {"DomainName": str}
)
_OptionalDomainInformationTypeDef = TypedDict(
    "_OptionalDomainInformationTypeDef", {"OwnerId": str, "Region": str}, total=False
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
        "DomainPackageStatus": Literal[
            "ASSOCIATING", "ASSOCIATION_FAILED", "ACTIVE", "DISSOCIATING", "DISSOCIATION_FAILED"
        ],
        "ReferencePath": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

EBSOptionsStatusTypeDef = TypedDict(
    "EBSOptionsStatusTypeDef", {"Options": "EBSOptionsTypeDef", "Status": "OptionStatusTypeDef"}
)

EBSOptionsTypeDef = TypedDict(
    "EBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ElasticsearchClusterConfigStatusTypeDef",
    {"Options": "ElasticsearchClusterConfigTypeDef", "Status": "OptionStatusTypeDef"},
)

ElasticsearchClusterConfigTypeDef = TypedDict(
    "ElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": "ZoneAwarenessConfigTypeDef",
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
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
        "LogPublishingOptions": Dict[
            Literal["INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS", "ES_APPLICATION_LOGS"],
            "LogPublishingOptionTypeDef",
        ],
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsTypeDef",
    },
    total=False,
)


class ElasticsearchDomainStatusTypeDef(
    _RequiredElasticsearchDomainStatusTypeDef, _OptionalElasticsearchDomainStatusTypeDef
):
    pass


ElasticsearchVersionStatusTypeDef = TypedDict(
    "ElasticsearchVersionStatusTypeDef", {"Options": str, "Status": "OptionStatusTypeDef"}
)

EncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "EncryptionAtRestOptionsStatusTypeDef",
    {"Options": "EncryptionAtRestOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

EncryptionAtRestOptionsTypeDef = TypedDict(
    "EncryptionAtRestOptionsTypeDef", {"Enabled": bool, "KmsKeyId": str}, total=False
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef", {"ErrorType": str, "ErrorMessage": str}, total=False
)

InboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": Literal[
            "PENDING_ACCEPTANCE", "APPROVED", "REJECTING", "REJECTED", "DELETING", "DELETED"
        ],
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
    {"MinimumInstanceCount": int, "MaximumInstanceCount": int},
    total=False,
)

InstanceLimitsTypeDef = TypedDict(
    "InstanceLimitsTypeDef", {"InstanceCountLimits": "InstanceCountLimitsTypeDef"}, total=False
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

LogPublishingOptionTypeDef = TypedDict(
    "LogPublishingOptionTypeDef", {"CloudWatchLogsLogGroupArn": str, "Enabled": bool}, total=False
)

LogPublishingOptionsStatusTypeDef = TypedDict(
    "LogPublishingOptionsStatusTypeDef",
    {
        "Options": Dict[
            Literal["INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS", "ES_APPLICATION_LOGS"],
            "LogPublishingOptionTypeDef",
        ],
        "Status": "OptionStatusTypeDef",
    },
    total=False,
)

MasterUserOptionsTypeDef = TypedDict(
    "MasterUserOptionsTypeDef",
    {"MasterUserARN": str, "MasterUserName": str, "MasterUserPassword": str},
    total=False,
)

NodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    {"Options": "NodeToNodeEncryptionOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

NodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsTypeDef", {"Enabled": bool}, total=False
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
    },
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef", {"UpdateVersion": int, "PendingDeletion": bool}, total=False
)


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass


OutboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": Literal[
            "PENDING_ACCEPTANCE",
            "VALIDATING",
            "VALIDATION_FAILED",
            "PROVISIONING",
            "ACTIVE",
            "REJECTED",
            "DELETING",
            "DELETED",
        ],
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
        "PackageStatus": Literal[
            "COPYING",
            "COPY_FAILED",
            "VALIDATING",
            "VALIDATION_FAILED",
            "AVAILABLE",
            "DELETING",
            "DELETED",
            "DELETE_FAILED",
        ],
        "CreatedAt": datetime,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedElasticsearchInstanceOfferingTypeDef = TypedDict(
    "ReservedElasticsearchInstanceOfferingTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
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
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List["RecurringChargeTypeDef"],
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
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
        "OptionalDeployment": bool,
    },
    total=False,
)

SnapshotOptionsStatusTypeDef = TypedDict(
    "SnapshotOptionsStatusTypeDef",
    {"Options": "SnapshotOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

SnapshotOptionsTypeDef = TypedDict(
    "SnapshotOptionsTypeDef", {"AutomatedSnapshotStartHour": int}, total=False
)

StorageTypeLimitTypeDef = TypedDict(
    "StorageTypeLimitTypeDef", {"LimitName": str, "LimitValues": List[str]}, total=False
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

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

UpgradeHistoryTypeDef = TypedDict(
    "UpgradeHistoryTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "StepsList": List["UpgradeStepItemTypeDef"],
    },
    total=False,
)

UpgradeStepItemTypeDef = TypedDict(
    "UpgradeStepItemTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "UpgradeStepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)

VPCDerivedInfoStatusTypeDef = TypedDict(
    "VPCDerivedInfoStatusTypeDef",
    {"Options": "VPCDerivedInfoTypeDef", "Status": "OptionStatusTypeDef"},
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

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef", {"AvailabilityZoneCount": int}, total=False
)

AcceptInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

AdvancedSecurityOptionsInputTypeDef = TypedDict(
    "AdvancedSecurityOptionsInputTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "MasterUserOptions": "MasterUserOptionsTypeDef",
    },
    total=False,
)

AssociatePackageResponseTypeDef = TypedDict(
    "AssociatePackageResponseTypeDef",
    {"DomainPackageDetails": "DomainPackageDetailsTypeDef"},
    total=False,
)

CancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {"ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef"},
    total=False,
)

CreateElasticsearchDomainResponseTypeDef = TypedDict(
    "CreateElasticsearchDomainResponseTypeDef",
    {"DomainStatus": "ElasticsearchDomainStatusTypeDef"},
    total=False,
)

CreateOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
        "CrossClusterSearchConnectionId": str,
    },
    total=False,
)

CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef", {"PackageDetails": "PackageDetailsTypeDef"}, total=False
)

DeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "DeleteElasticsearchDomainResponseTypeDef",
    {"DomainStatus": "ElasticsearchDomainStatusTypeDef"},
    total=False,
)

DeleteInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

DeleteOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "OutboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

DeletePackageResponseTypeDef = TypedDict(
    "DeletePackageResponseTypeDef", {"PackageDetails": "PackageDetailsTypeDef"}, total=False
)

DescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": "ElasticsearchDomainConfigTypeDef"},
)

DescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainResponseTypeDef",
    {"DomainStatus": "ElasticsearchDomainStatusTypeDef"},
)

DescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainsResponseTypeDef",
    {"DomainStatusList": List["ElasticsearchDomainStatusTypeDef"]},
)

DescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {"LimitsByRole": Dict[str, "LimitsTypeDef"]},
    total=False,
)

DescribeInboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["InboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["OutboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribePackagesFilterTypeDef = TypedDict(
    "DescribePackagesFilterTypeDef",
    {"Name": Literal["PackageID", "PackageName", "PackageStatus"], "Value": List[str]},
    total=False,
)

DescribePackagesResponseTypeDef = TypedDict(
    "DescribePackagesResponseTypeDef",
    {"PackageDetailsList": List["PackageDetailsTypeDef"], "NextToken": str},
    total=False,
)

DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            "ReservedElasticsearchInstanceOfferingTypeDef"
        ],
    },
    total=False,
)

DescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List["ReservedElasticsearchInstanceTypeDef"],
    },
    total=False,
)

DissociatePackageResponseTypeDef = TypedDict(
    "DissociatePackageResponseTypeDef",
    {"DomainPackageDetails": "DomainPackageDetailsTypeDef"},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

GetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    {"CompatibleElasticsearchVersions": List["CompatibleVersionsMapTypeDef"]},
    total=False,
)

GetUpgradeHistoryResponseTypeDef = TypedDict(
    "GetUpgradeHistoryResponseTypeDef",
    {"UpgradeHistories": List["UpgradeHistoryTypeDef"], "NextToken": str},
    total=False,
)

GetUpgradeStatusResponseTypeDef = TypedDict(
    "GetUpgradeStatusResponseTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "StepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "UpgradeName": str,
    },
    total=False,
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef", {"DomainNames": List["DomainInfoTypeDef"]}, total=False
)

ListDomainsForPackageResponseTypeDef = TypedDict(
    "ListDomainsForPackageResponseTypeDef",
    {"DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"], "NextToken": str},
    total=False,
)

ListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[
            Literal[
                "m3.medium.elasticsearch",
                "m3.large.elasticsearch",
                "m3.xlarge.elasticsearch",
                "m3.2xlarge.elasticsearch",
                "m4.large.elasticsearch",
                "m4.xlarge.elasticsearch",
                "m4.2xlarge.elasticsearch",
                "m4.4xlarge.elasticsearch",
                "m4.10xlarge.elasticsearch",
                "m5.large.elasticsearch",
                "m5.xlarge.elasticsearch",
                "m5.2xlarge.elasticsearch",
                "m5.4xlarge.elasticsearch",
                "m5.12xlarge.elasticsearch",
                "r5.large.elasticsearch",
                "r5.xlarge.elasticsearch",
                "r5.2xlarge.elasticsearch",
                "r5.4xlarge.elasticsearch",
                "r5.12xlarge.elasticsearch",
                "c5.large.elasticsearch",
                "c5.xlarge.elasticsearch",
                "c5.2xlarge.elasticsearch",
                "c5.4xlarge.elasticsearch",
                "c5.9xlarge.elasticsearch",
                "c5.18xlarge.elasticsearch",
                "ultrawarm1.medium.elasticsearch",
                "ultrawarm1.large.elasticsearch",
                "t2.micro.elasticsearch",
                "t2.small.elasticsearch",
                "t2.medium.elasticsearch",
                "r3.large.elasticsearch",
                "r3.xlarge.elasticsearch",
                "r3.2xlarge.elasticsearch",
                "r3.4xlarge.elasticsearch",
                "r3.8xlarge.elasticsearch",
                "i2.xlarge.elasticsearch",
                "i2.2xlarge.elasticsearch",
                "d2.xlarge.elasticsearch",
                "d2.2xlarge.elasticsearch",
                "d2.4xlarge.elasticsearch",
                "d2.8xlarge.elasticsearch",
                "c4.large.elasticsearch",
                "c4.xlarge.elasticsearch",
                "c4.2xlarge.elasticsearch",
                "c4.4xlarge.elasticsearch",
                "c4.8xlarge.elasticsearch",
                "r4.large.elasticsearch",
                "r4.xlarge.elasticsearch",
                "r4.2xlarge.elasticsearch",
                "r4.4xlarge.elasticsearch",
                "r4.8xlarge.elasticsearch",
                "r4.16xlarge.elasticsearch",
                "i3.large.elasticsearch",
                "i3.xlarge.elasticsearch",
                "i3.2xlarge.elasticsearch",
                "i3.4xlarge.elasticsearch",
                "i3.8xlarge.elasticsearch",
                "i3.16xlarge.elasticsearch",
            ]
        ],
        "NextToken": str,
    },
    total=False,
)

ListElasticsearchVersionsResponseTypeDef = TypedDict(
    "ListElasticsearchVersionsResponseTypeDef",
    {"ElasticsearchVersions": List[str], "NextToken": str},
    total=False,
)

ListPackagesForDomainResponseTypeDef = TypedDict(
    "ListPackagesForDomainResponseTypeDef",
    {"DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"], "NextToken": str},
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

PackageSourceTypeDef = TypedDict(
    "PackageSourceTypeDef", {"S3BucketName": str, "S3Key": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {"ReservedElasticsearchInstanceId": str, "ReservationName": str},
    total=False,
)

RejectInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

StartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {"ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef"},
    total=False,
)

UpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": "ElasticsearchDomainConfigTypeDef"},
)

UpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "UpgradeElasticsearchDomainResponseTypeDef",
    {"DomainName": str, "TargetVersion": str, "PerformCheckOnly": bool},
    total=False,
)

VPCOptionsTypeDef = TypedDict(
    "VPCOptionsTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}, total=False
)
