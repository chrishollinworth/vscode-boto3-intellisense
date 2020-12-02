"""
Main interface for ds service type definitions.

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DomainControllerTypeDef",
    "EventTopicTypeDef",
    "IpRouteInfoTypeDef",
    "LDAPSSettingInfoTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "SchemaExtensionInfoTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "AcceptSharedDirectoryResultTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasResultTypeDef",
    "CreateComputerResultTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustResultTypeDef",
    "DescribeCertificateResultTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsResultTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "IpRouteTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterCertificateResultTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustResultTypeDef",
)

AttributeTypeDef = TypedDict("AttributeTypeDef", {"Name": str, "Value": str}, total=False)

CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": str,
        "CommonName": str,
        "State": Literal[
            "Registering",
            "Registered",
            "RegisterFailed",
            "Deregistering",
            "Deregistered",
            "DeregisterFailed",
        ],
        "ExpiryDateTime": datetime,
        "Type": Literal["ClientCertAuth", "ClientLDAPS"],
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": str,
        "State": Literal[
            "Registering",
            "Registered",
            "RegisterFailed",
            "Deregistering",
            "Deregistered",
            "DeregisterFailed",
        ],
        "StateReason": str,
        "CommonName": str,
        "RegisteredDateTime": datetime,
        "ExpiryDateTime": datetime,
        "Type": Literal["ClientCertAuth", "ClientLDAPS"],
        "ClientCertAuthSettings": "ClientCertAuthSettingsTypeDef",
    },
    total=False,
)

ClientCertAuthSettingsTypeDef = TypedDict(
    "ClientCertAuthSettingsTypeDef", {"OCSPUrl": str}, total=False
)

ComputerTypeDef = TypedDict(
    "ComputerTypeDef",
    {"ComputerId": str, "ComputerName": str, "ComputerAttributes": List["AttributeTypeDef"]},
    total=False,
)

ConditionalForwarderTypeDef = TypedDict(
    "ConditionalForwarderTypeDef",
    {"RemoteDomainName": str, "DnsIpAddrs": List[str], "ReplicationScope": Literal["Domain"]},
    total=False,
)

DirectoryConnectSettingsDescriptionTypeDef = TypedDict(
    "DirectoryConnectSettingsDescriptionTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)

DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": Literal["Small", "Large"],
        "Edition": Literal["Enterprise", "Standard"],
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": Literal[
            "Requested",
            "Creating",
            "Created",
            "Active",
            "Inoperable",
            "Impaired",
            "Restoring",
            "RestoreFailed",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": Literal["SimpleAD", "ADConnector", "MicrosoftAD", "SharedMicrosoftAD"],
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "ConnectSettings": "DirectoryConnectSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": "OwnerDirectoryDescriptionTypeDef",
        "RegionsInfo": "RegionsInfoTypeDef",
    },
    total=False,
)

DirectoryLimitsTypeDef = TypedDict(
    "DirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": int,
        "CloudOnlyDirectoriesCurrentCount": int,
        "CloudOnlyDirectoriesLimitReached": bool,
        "CloudOnlyMicrosoftADLimit": int,
        "CloudOnlyMicrosoftADCurrentCount": int,
        "CloudOnlyMicrosoftADLimitReached": bool,
        "ConnectedDirectoriesLimit": int,
        "ConnectedDirectoriesCurrentCount": int,
        "ConnectedDirectoriesLimitReached": bool,
    },
    total=False,
)

DirectoryVpcSettingsDescriptionTypeDef = TypedDict(
    "DirectoryVpcSettingsDescriptionTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)

DirectoryVpcSettingsTypeDef = TypedDict(
    "DirectoryVpcSettingsTypeDef", {"VpcId": str, "SubnetIds": List[str]}
)

DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": Literal[
            "Creating", "Active", "Impaired", "Restoring", "Deleting", "Deleted", "Failed"
        ],
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)

EventTopicTypeDef = TypedDict(
    "EventTopicTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": Literal["Registered", "Topic not found", "Failed", "Deleted"],
    },
    total=False,
)

IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": Literal[
            "Adding", "Added", "Removing", "Removed", "AddFailed", "RemoveFailed"
        ],
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)

LDAPSSettingInfoTypeDef = TypedDict(
    "LDAPSSettingInfoTypeDef",
    {
        "LDAPSStatus": Literal["Enabling", "Enabled", "EnableFailed", "Disabled"],
        "LDAPSStatusReason": str,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)

OwnerDirectoryDescriptionTypeDef = TypedDict(
    "OwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
    },
    total=False,
)

RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

RegionDescriptionTypeDef = TypedDict(
    "RegionDescriptionTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "RegionType": Literal["Primary", "Additional"],
        "Status": Literal[
            "Requested",
            "Creating",
            "Created",
            "Active",
            "Inoperable",
            "Impaired",
            "Restoring",
            "RestoreFailed",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "DesiredNumberOfDomainControllers": int,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

RegionsInfoTypeDef = TypedDict(
    "RegionsInfoTypeDef", {"PrimaryRegion": str, "AdditionalRegions": List[str]}, total=False
)

SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": Literal[
            "Initializing",
            "CreatingSnapshot",
            "UpdatingSchema",
            "Replicating",
            "CancelInProgress",
            "RollbackInProgress",
            "Cancelled",
            "Failed",
            "Completed",
        ],
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

SnapshotLimitsTypeDef = TypedDict(
    "SnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": int,
        "ManualSnapshotsCurrentCount": int,
        "ManualSnapshotsLimitReached": bool,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": Literal["Auto", "Manual"],
        "Name": str,
        "Status": Literal["Creating", "Completed", "Failed"],
        "StartTime": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": Literal["Forest", "External"],
        "TrustDirection": Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        "TrustState": Literal[
            "Creating",
            "Created",
            "Verifying",
            "VerifyFailed",
            "Verified",
            "Updating",
            "UpdateFailed",
            "Updated",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": Literal["Enabled", "Disabled"],
    },
    total=False,
)

AcceptSharedDirectoryResultTypeDef = TypedDict(
    "AcceptSharedDirectoryResultTypeDef", {"SharedDirectory": "SharedDirectoryTypeDef"}, total=False
)

ConnectDirectoryResultTypeDef = TypedDict(
    "ConnectDirectoryResultTypeDef", {"DirectoryId": str}, total=False
)

CreateAliasResultTypeDef = TypedDict(
    "CreateAliasResultTypeDef", {"DirectoryId": str, "Alias": str}, total=False
)

CreateComputerResultTypeDef = TypedDict(
    "CreateComputerResultTypeDef", {"Computer": "ComputerTypeDef"}, total=False
)

CreateDirectoryResultTypeDef = TypedDict(
    "CreateDirectoryResultTypeDef", {"DirectoryId": str}, total=False
)

CreateMicrosoftADResultTypeDef = TypedDict(
    "CreateMicrosoftADResultTypeDef", {"DirectoryId": str}, total=False
)

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef", {"SnapshotId": str}, total=False
)

CreateTrustResultTypeDef = TypedDict("CreateTrustResultTypeDef", {"TrustId": str}, total=False)

DeleteDirectoryResultTypeDef = TypedDict(
    "DeleteDirectoryResultTypeDef", {"DirectoryId": str}, total=False
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef", {"SnapshotId": str}, total=False
)

DeleteTrustResultTypeDef = TypedDict("DeleteTrustResultTypeDef", {"TrustId": str}, total=False)

DescribeCertificateResultTypeDef = TypedDict(
    "DescribeCertificateResultTypeDef", {"Certificate": "CertificateTypeDef"}, total=False
)

DescribeConditionalForwardersResultTypeDef = TypedDict(
    "DescribeConditionalForwardersResultTypeDef",
    {"ConditionalForwarders": List["ConditionalForwarderTypeDef"]},
    total=False,
)

DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {"DirectoryDescriptions": List["DirectoryDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {"DomainControllers": List["DomainControllerTypeDef"], "NextToken": str},
    total=False,
)

DescribeEventTopicsResultTypeDef = TypedDict(
    "DescribeEventTopicsResultTypeDef", {"EventTopics": List["EventTopicTypeDef"]}, total=False
)

DescribeLDAPSSettingsResultTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultTypeDef",
    {"LDAPSSettingsInfo": List["LDAPSSettingInfoTypeDef"], "NextToken": str},
    total=False,
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {"RegionsDescription": List["RegionDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {"SharedDirectories": List["SharedDirectoryTypeDef"], "NextToken": str},
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {"Snapshots": List["SnapshotTypeDef"], "NextToken": str},
    total=False,
)

DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef", {"Trusts": List["TrustTypeDef"], "NextToken": str}, total=False
)

DirectoryConnectSettingsTypeDef = TypedDict(
    "DirectoryConnectSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "CustomerDnsIps": List[str], "CustomerUserName": str},
)

GetDirectoryLimitsResultTypeDef = TypedDict(
    "GetDirectoryLimitsResultTypeDef", {"DirectoryLimits": "DirectoryLimitsTypeDef"}, total=False
)

GetSnapshotLimitsResultTypeDef = TypedDict(
    "GetSnapshotLimitsResultTypeDef", {"SnapshotLimits": "SnapshotLimitsTypeDef"}, total=False
)

IpRouteTypeDef = TypedDict("IpRouteTypeDef", {"CidrIp": str, "Description": str}, total=False)

ListCertificatesResultTypeDef = TypedDict(
    "ListCertificatesResultTypeDef",
    {"NextToken": str, "CertificatesInfo": List["CertificateInfoTypeDef"]},
    total=False,
)

ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {"IpRoutesInfo": List["IpRouteInfoTypeDef"], "NextToken": str},
    total=False,
)

ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {"LogSubscriptions": List["LogSubscriptionTypeDef"], "NextToken": str},
    total=False,
)

ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {"SchemaExtensionsInfo": List["SchemaExtensionInfoTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"Tags": List["TagTypeDef"], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterCertificateResultTypeDef = TypedDict(
    "RegisterCertificateResultTypeDef", {"CertificateId": str}, total=False
)

RejectSharedDirectoryResultTypeDef = TypedDict(
    "RejectSharedDirectoryResultTypeDef", {"SharedDirectoryId": str}, total=False
)

ShareDirectoryResultTypeDef = TypedDict(
    "ShareDirectoryResultTypeDef", {"SharedDirectoryId": str}, total=False
)

ShareTargetTypeDef = TypedDict("ShareTargetTypeDef", {"Id": str, "Type": Literal["ACCOUNT"]})

StartSchemaExtensionResultTypeDef = TypedDict(
    "StartSchemaExtensionResultTypeDef", {"SchemaExtensionId": str}, total=False
)

UnshareDirectoryResultTypeDef = TypedDict(
    "UnshareDirectoryResultTypeDef", {"SharedDirectoryId": str}, total=False
)

UnshareTargetTypeDef = TypedDict("UnshareTargetTypeDef", {"Id": str, "Type": Literal["ACCOUNT"]})

UpdateTrustResultTypeDef = TypedDict(
    "UpdateTrustResultTypeDef", {"RequestId": str, "TrustId": str}, total=False
)

VerifyTrustResultTypeDef = TypedDict("VerifyTrustResultTypeDef", {"TrustId": str}, total=False)
