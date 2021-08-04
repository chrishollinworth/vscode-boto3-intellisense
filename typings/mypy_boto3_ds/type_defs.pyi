"""
Type annotations for ds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AcceptSharedDirectoryRequestRequestTypeDef

    data: AcceptSharedDirectoryRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CertificateStateType,
    CertificateTypeType,
    DirectoryEditionType,
    DirectorySizeType,
    DirectoryStageType,
    DirectoryTypeType,
    DomainControllerStatusType,
    IpRouteStatusMsgType,
    LDAPSStatusType,
    RadiusAuthenticationProtocolType,
    RadiusStatusType,
    RegionTypeType,
    SchemaExtensionStatusType,
    SelectiveAuthType,
    ShareMethodType,
    ShareStatusType,
    SnapshotStatusType,
    SnapshotTypeType,
    TopicStatusType,
    TrustDirectionType,
    TrustStateType,
    TrustTypeType,
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
    "AcceptSharedDirectoryRequestRequestTypeDef",
    "AcceptSharedDirectoryResultTypeDef",
    "AddIpRoutesRequestRequestTypeDef",
    "AddRegionRequestRequestTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "AttributeTypeDef",
    "CancelSchemaExtensionRequestRequestTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "ConnectDirectoryRequestRequestTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateAliasResultTypeDef",
    "CreateComputerRequestRequestTypeDef",
    "CreateComputerResultTypeDef",
    "CreateConditionalForwarderRequestRequestTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateLogSubscriptionRequestRequestTypeDef",
    "CreateMicrosoftADRequestRequestTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustRequestRequestTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteConditionalForwarderRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteLogSubscriptionRequestRequestTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustRequestRequestTypeDef",
    "DeleteTrustResultTypeDef",
    "DeregisterCertificateRequestRequestTypeDef",
    "DeregisterEventTopicRequestRequestTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeCertificateResultTypeDef",
    "DescribeConditionalForwardersRequestRequestTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "DescribeDirectoriesRequestRequestTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeDomainControllersRequestRequestTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsRequestRequestTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeLDAPSSettingsRequestRequestTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeRegionsRequestRequestTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSharedDirectoriesRequestRequestTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsRequestRequestTypeDef",
    "DescribeTrustsResultTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DisableClientAuthenticationRequestRequestTypeDef",
    "DisableLDAPSRequestRequestTypeDef",
    "DisableRadiusRequestRequestTypeDef",
    "DisableSsoRequestRequestTypeDef",
    "DomainControllerTypeDef",
    "EnableClientAuthenticationRequestRequestTypeDef",
    "EnableLDAPSRequestRequestTypeDef",
    "EnableRadiusRequestRequestTypeDef",
    "EnableSsoRequestRequestTypeDef",
    "EventTopicTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsRequestRequestTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "IpRouteInfoTypeDef",
    "IpRouteTypeDef",
    "LDAPSSettingInfoTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesRequestRequestTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsRequestRequestTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsRequestRequestTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "RegisterCertificateRequestRequestTypeDef",
    "RegisterCertificateResultTypeDef",
    "RegisterEventTopicRequestRequestTypeDef",
    "RejectSharedDirectoryRequestRequestTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "RemoveIpRoutesRequestRequestTypeDef",
    "RemoveRegionRequestRequestTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromSnapshotRequestRequestTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ShareDirectoryRequestRequestTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "StartSchemaExtensionRequestRequestTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "UnshareDirectoryRequestRequestTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateConditionalForwarderRequestRequestTypeDef",
    "UpdateNumberOfDomainControllersRequestRequestTypeDef",
    "UpdateRadiusRequestRequestTypeDef",
    "UpdateTrustRequestRequestTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustRequestRequestTypeDef",
    "VerifyTrustResultTypeDef",
)

AcceptSharedDirectoryRequestRequestTypeDef = TypedDict(
    "AcceptSharedDirectoryRequestRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)

AcceptSharedDirectoryResultTypeDef = TypedDict(
    "AcceptSharedDirectoryResultTypeDef",
    {
        "SharedDirectory": "SharedDirectoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddIpRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredAddIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "IpRoutes": List["IpRouteTypeDef"],
    },
)
_OptionalAddIpRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalAddIpRoutesRequestRequestTypeDef",
    {
        "UpdateSecurityGroupForDirectoryControllers": bool,
    },
    total=False,
)

class AddIpRoutesRequestRequestTypeDef(
    _RequiredAddIpRoutesRequestRequestTypeDef, _OptionalAddIpRoutesRequestRequestTypeDef
):
    pass

AddRegionRequestRequestTypeDef = TypedDict(
    "AddRegionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "VPCSettings": "DirectoryVpcSettingsTypeDef",
    },
)

AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

CancelSchemaExtensionRequestRequestTypeDef = TypedDict(
    "CancelSchemaExtensionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
    },
)

CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": str,
        "CommonName": str,
        "State": CertificateStateType,
        "ExpiryDateTime": datetime,
        "Type": CertificateTypeType,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": str,
        "State": CertificateStateType,
        "StateReason": str,
        "CommonName": str,
        "RegisteredDateTime": datetime,
        "ExpiryDateTime": datetime,
        "Type": CertificateTypeType,
        "ClientCertAuthSettings": "ClientCertAuthSettingsTypeDef",
    },
    total=False,
)

ClientCertAuthSettingsTypeDef = TypedDict(
    "ClientCertAuthSettingsTypeDef",
    {
        "OCSPUrl": str,
    },
    total=False,
)

ComputerTypeDef = TypedDict(
    "ComputerTypeDef",
    {
        "ComputerId": str,
        "ComputerName": str,
        "ComputerAttributes": List["AttributeTypeDef"],
    },
    total=False,
)

ConditionalForwarderTypeDef = TypedDict(
    "ConditionalForwarderTypeDef",
    {
        "RemoteDomainName": str,
        "DnsIpAddrs": List[str],
        "ReplicationScope": Literal["Domain"],
    },
    total=False,
)

_RequiredConnectDirectoryRequestRequestTypeDef = TypedDict(
    "_RequiredConnectDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
        "ConnectSettings": "DirectoryConnectSettingsTypeDef",
    },
)
_OptionalConnectDirectoryRequestRequestTypeDef = TypedDict(
    "_OptionalConnectDirectoryRequestRequestTypeDef",
    {
        "ShortName": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ConnectDirectoryRequestRequestTypeDef(
    _RequiredConnectDirectoryRequestRequestTypeDef, _OptionalConnectDirectoryRequestRequestTypeDef
):
    pass

ConnectDirectoryResultTypeDef = TypedDict(
    "ConnectDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
    },
)

CreateAliasResultTypeDef = TypedDict(
    "CreateAliasResultTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateComputerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComputerRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ComputerName": str,
        "Password": str,
    },
)
_OptionalCreateComputerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComputerRequestRequestTypeDef",
    {
        "OrganizationalUnitDistinguishedName": str,
        "ComputerAttributes": List["AttributeTypeDef"],
    },
    total=False,
)

class CreateComputerRequestRequestTypeDef(
    _RequiredCreateComputerRequestRequestTypeDef, _OptionalCreateComputerRequestRequestTypeDef
):
    pass

CreateComputerResultTypeDef = TypedDict(
    "CreateComputerResultTypeDef",
    {
        "Computer": "ComputerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConditionalForwarderRequestRequestTypeDef = TypedDict(
    "CreateConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": List[str],
    },
)

_RequiredCreateDirectoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
    },
)
_OptionalCreateDirectoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDirectoryRequestRequestTypeDef",
    {
        "ShortName": str,
        "Description": str,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDirectoryRequestRequestTypeDef(
    _RequiredCreateDirectoryRequestRequestTypeDef, _OptionalCreateDirectoryRequestRequestTypeDef
):
    pass

CreateDirectoryResultTypeDef = TypedDict(
    "CreateDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLogSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateLogSubscriptionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "LogGroupName": str,
    },
)

_RequiredCreateMicrosoftADRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMicrosoftADRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
    },
)
_OptionalCreateMicrosoftADRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMicrosoftADRequestRequestTypeDef",
    {
        "ShortName": str,
        "Description": str,
        "Edition": DirectoryEditionType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMicrosoftADRequestRequestTypeDef(
    _RequiredCreateMicrosoftADRequestRequestTypeDef, _OptionalCreateMicrosoftADRequestRequestTypeDef
):
    pass

CreateMicrosoftADResultTypeDef = TypedDict(
    "CreateMicrosoftADResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class CreateSnapshotRequestRequestTypeDef(
    _RequiredCreateSnapshotRequestRequestTypeDef, _OptionalCreateSnapshotRequestRequestTypeDef
):
    pass

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrustRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "TrustPassword": str,
        "TrustDirection": TrustDirectionType,
    },
)
_OptionalCreateTrustRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustRequestRequestTypeDef",
    {
        "TrustType": TrustTypeType,
        "ConditionalForwarderIpAddrs": List[str],
        "SelectiveAuth": SelectiveAuthType,
    },
    total=False,
)

class CreateTrustRequestRequestTypeDef(
    _RequiredCreateTrustRequestRequestTypeDef, _OptionalCreateTrustRequestRequestTypeDef
):
    pass

CreateTrustResultTypeDef = TypedDict(
    "CreateTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConditionalForwarderRequestRequestTypeDef = TypedDict(
    "DeleteConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
    },
)

DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DeleteDirectoryResultTypeDef = TypedDict(
    "DeleteDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLogSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteLogSubscriptionRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrustRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTrustRequestRequestTypeDef",
    {
        "TrustId": str,
    },
)
_OptionalDeleteTrustRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTrustRequestRequestTypeDef",
    {
        "DeleteAssociatedConditionalForwarder": bool,
    },
    total=False,
)

class DeleteTrustRequestRequestTypeDef(
    _RequiredDeleteTrustRequestRequestTypeDef, _OptionalDeleteTrustRequestRequestTypeDef
):
    pass

DeleteTrustResultTypeDef = TypedDict(
    "DeleteTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterCertificateRequestRequestTypeDef = TypedDict(
    "DeregisterCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)

DeregisterEventTopicRequestRequestTypeDef = TypedDict(
    "DeregisterEventTopicRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)

DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)

DescribeCertificateResultTypeDef = TypedDict(
    "DescribeCertificateResultTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConditionalForwardersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConditionalForwardersRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeConditionalForwardersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConditionalForwardersRequestRequestTypeDef",
    {
        "RemoteDomainNames": List[str],
    },
    total=False,
)

class DescribeConditionalForwardersRequestRequestTypeDef(
    _RequiredDescribeConditionalForwardersRequestRequestTypeDef,
    _OptionalDescribeConditionalForwardersRequestRequestTypeDef,
):
    pass

DescribeConditionalForwardersResultTypeDef = TypedDict(
    "DescribeConditionalForwardersResultTypeDef",
    {
        "ConditionalForwarders": List["ConditionalForwarderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeDirectoriesRequestRequestTypeDef",
    {
        "DirectoryIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {
        "DirectoryDescriptions": List["DirectoryDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainControllersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainControllersRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeDomainControllersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainControllersRequestRequestTypeDef",
    {
        "DomainControllerIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class DescribeDomainControllersRequestRequestTypeDef(
    _RequiredDescribeDomainControllersRequestRequestTypeDef,
    _OptionalDescribeDomainControllersRequestRequestTypeDef,
):
    pass

DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {
        "DomainControllers": List["DomainControllerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTopicsRequestRequestTypeDef = TypedDict(
    "DescribeEventTopicsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicNames": List[str],
    },
    total=False,
)

DescribeEventTopicsResultTypeDef = TypedDict(
    "DescribeEventTopicsResultTypeDef",
    {
        "EventTopics": List["EventTopicTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLDAPSSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeLDAPSSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeLDAPSSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeLDAPSSettingsRequestRequestTypeDef",
    {
        "Type": Literal["Client"],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class DescribeLDAPSSettingsRequestRequestTypeDef(
    _RequiredDescribeLDAPSSettingsRequestRequestTypeDef,
    _OptionalDescribeLDAPSSettingsRequestRequestTypeDef,
):
    pass

DescribeLDAPSSettingsResultTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultTypeDef",
    {
        "LDAPSSettingsInfo": List["LDAPSSettingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRegionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRegionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeRegionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRegionsRequestRequestTypeDef",
    {
        "RegionName": str,
        "NextToken": str,
    },
    total=False,
)

class DescribeRegionsRequestRequestTypeDef(
    _RequiredDescribeRegionsRequestRequestTypeDef, _OptionalDescribeRegionsRequestRequestTypeDef
):
    pass

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "RegionsDescription": List["RegionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSharedDirectoriesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSharedDirectoriesRequestRequestTypeDef",
    {
        "OwnerDirectoryId": str,
    },
)
_OptionalDescribeSharedDirectoriesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSharedDirectoriesRequestRequestTypeDef",
    {
        "SharedDirectoryIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class DescribeSharedDirectoriesRequestRequestTypeDef(
    _RequiredDescribeSharedDirectoriesRequestRequestTypeDef,
    _OptionalDescribeSharedDirectoriesRequestRequestTypeDef,
):
    pass

DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {
        "SharedDirectories": List["SharedDirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SnapshotIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustsRequestRequestTypeDef = TypedDict(
    "DescribeTrustsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TrustIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef",
    {
        "Trusts": List["TrustTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DirectoryConnectSettingsTypeDef = TypedDict(
    "DirectoryConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerDnsIps": List[str],
        "CustomerUserName": str,
    },
)

DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": DirectorySizeType,
        "Edition": DirectoryEditionType,
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": DirectoryStageType,
        "ShareStatus": ShareStatusType,
        "ShareMethod": ShareMethodType,
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": DirectoryTypeType,
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "ConnectSettings": "DirectoryConnectSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": RadiusStatusType,
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
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)

DirectoryVpcSettingsTypeDef = TypedDict(
    "DirectoryVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
    },
)

DisableClientAuthenticationRequestRequestTypeDef = TypedDict(
    "DisableClientAuthenticationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["SmartCard"],
    },
)

DisableLDAPSRequestRequestTypeDef = TypedDict(
    "DisableLDAPSRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

DisableRadiusRequestRequestTypeDef = TypedDict(
    "DisableRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

_RequiredDisableSsoRequestRequestTypeDef = TypedDict(
    "_RequiredDisableSsoRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDisableSsoRequestRequestTypeDef = TypedDict(
    "_OptionalDisableSsoRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
    },
    total=False,
)

class DisableSsoRequestRequestTypeDef(
    _RequiredDisableSsoRequestRequestTypeDef, _OptionalDisableSsoRequestRequestTypeDef
):
    pass

DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": DomainControllerStatusType,
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)

EnableClientAuthenticationRequestRequestTypeDef = TypedDict(
    "EnableClientAuthenticationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["SmartCard"],
    },
)

EnableLDAPSRequestRequestTypeDef = TypedDict(
    "EnableLDAPSRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

EnableRadiusRequestRequestTypeDef = TypedDict(
    "EnableRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": "RadiusSettingsTypeDef",
    },
)

_RequiredEnableSsoRequestRequestTypeDef = TypedDict(
    "_RequiredEnableSsoRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalEnableSsoRequestRequestTypeDef = TypedDict(
    "_OptionalEnableSsoRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
    },
    total=False,
)

class EnableSsoRequestRequestTypeDef(
    _RequiredEnableSsoRequestRequestTypeDef, _OptionalEnableSsoRequestRequestTypeDef
):
    pass

EventTopicTypeDef = TypedDict(
    "EventTopicTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": TopicStatusType,
    },
    total=False,
)

GetDirectoryLimitsResultTypeDef = TypedDict(
    "GetDirectoryLimitsResultTypeDef",
    {
        "DirectoryLimits": "DirectoryLimitsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotLimitsRequestRequestTypeDef = TypedDict(
    "GetSnapshotLimitsRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

GetSnapshotLimitsResultTypeDef = TypedDict(
    "GetSnapshotLimitsResultTypeDef",
    {
        "SnapshotLimits": "SnapshotLimitsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": IpRouteStatusMsgType,
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)

IpRouteTypeDef = TypedDict(
    "IpRouteTypeDef",
    {
        "CidrIp": str,
        "Description": str,
    },
    total=False,
)

LDAPSSettingInfoTypeDef = TypedDict(
    "LDAPSSettingInfoTypeDef",
    {
        "LDAPSStatus": LDAPSStatusType,
        "LDAPSStatusReason": str,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredListCertificatesRequestRequestTypeDef = TypedDict(
    "_RequiredListCertificatesRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalListCertificatesRequestRequestTypeDef = TypedDict(
    "_OptionalListCertificatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListCertificatesRequestRequestTypeDef(
    _RequiredListCertificatesRequestRequestTypeDef, _OptionalListCertificatesRequestRequestTypeDef
):
    pass

ListCertificatesResultTypeDef = TypedDict(
    "ListCertificatesResultTypeDef",
    {
        "NextToken": str,
        "CertificatesInfo": List["CertificateInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIpRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredListIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalListIpRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalListIpRoutesRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListIpRoutesRequestRequestTypeDef(
    _RequiredListIpRoutesRequestRequestTypeDef, _OptionalListIpRoutesRequestRequestTypeDef
):
    pass

ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {
        "IpRoutesInfo": List["IpRouteInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListLogSubscriptionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {
        "LogSubscriptions": List["LogSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemaExtensionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSchemaExtensionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalListSchemaExtensionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSchemaExtensionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListSchemaExtensionsRequestRequestTypeDef(
    _RequiredListSchemaExtensionsRequestRequestTypeDef,
    _OptionalListSchemaExtensionsRequestRequestTypeDef,
):
    pass

ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {
        "SchemaExtensionsInfo": List["SchemaExtensionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {
        "DirectoryId": str,
        "LogGroupName": str,
        "SubscriptionCreatedDateTime": datetime,
    },
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
        "RadiusStatus": RadiusStatusType,
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

RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": RadiusAuthenticationProtocolType,
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
        "RegionType": RegionTypeType,
        "Status": DirectoryStageType,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "DesiredNumberOfDomainControllers": int,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

RegionsInfoTypeDef = TypedDict(
    "RegionsInfoTypeDef",
    {
        "PrimaryRegion": str,
        "AdditionalRegions": List[str],
    },
    total=False,
)

_RequiredRegisterCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateData": str,
    },
)
_OptionalRegisterCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateRequestRequestTypeDef",
    {
        "Type": CertificateTypeType,
        "ClientCertAuthSettings": "ClientCertAuthSettingsTypeDef",
    },
    total=False,
)

class RegisterCertificateRequestRequestTypeDef(
    _RequiredRegisterCertificateRequestRequestTypeDef,
    _OptionalRegisterCertificateRequestRequestTypeDef,
):
    pass

RegisterCertificateResultTypeDef = TypedDict(
    "RegisterCertificateResultTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterEventTopicRequestRequestTypeDef = TypedDict(
    "RegisterEventTopicRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)

RejectSharedDirectoryRequestRequestTypeDef = TypedDict(
    "RejectSharedDirectoryRequestRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)

RejectSharedDirectoryResultTypeDef = TypedDict(
    "RejectSharedDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveIpRoutesRequestRequestTypeDef = TypedDict(
    "RemoveIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CidrIps": List[str],
    },
)

RemoveRegionRequestRequestTypeDef = TypedDict(
    "RemoveRegionRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

ResetUserPasswordRequestRequestTypeDef = TypedDict(
    "ResetUserPasswordRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "NewPassword": str,
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

RestoreFromSnapshotRequestRequestTypeDef = TypedDict(
    "RestoreFromSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)

SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": SchemaExtensionStatusType,
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

_RequiredShareDirectoryRequestRequestTypeDef = TypedDict(
    "_RequiredShareDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ShareTarget": "ShareTargetTypeDef",
        "ShareMethod": ShareMethodType,
    },
)
_OptionalShareDirectoryRequestRequestTypeDef = TypedDict(
    "_OptionalShareDirectoryRequestRequestTypeDef",
    {
        "ShareNotes": str,
    },
    total=False,
)

class ShareDirectoryRequestRequestTypeDef(
    _RequiredShareDirectoryRequestRequestTypeDef, _OptionalShareDirectoryRequestRequestTypeDef
):
    pass

ShareDirectoryResultTypeDef = TypedDict(
    "ShareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShareTargetTypeDef = TypedDict(
    "ShareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": ShareMethodType,
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": ShareStatusType,
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
        "Type": SnapshotTypeType,
        "Name": str,
        "Status": SnapshotStatusType,
        "StartTime": datetime,
    },
    total=False,
)

StartSchemaExtensionRequestRequestTypeDef = TypedDict(
    "StartSchemaExtensionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CreateSnapshotBeforeSchemaExtension": bool,
        "LdifContent": str,
        "Description": str,
    },
)

StartSchemaExtensionResultTypeDef = TypedDict(
    "StartSchemaExtensionResultTypeDef",
    {
        "SchemaExtensionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": TrustTypeType,
        "TrustDirection": TrustDirectionType,
        "TrustState": TrustStateType,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": SelectiveAuthType,
    },
    total=False,
)

UnshareDirectoryRequestRequestTypeDef = TypedDict(
    "UnshareDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UnshareTarget": "UnshareTargetTypeDef",
    },
)

UnshareDirectoryResultTypeDef = TypedDict(
    "UnshareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnshareTargetTypeDef = TypedDict(
    "UnshareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

UpdateConditionalForwarderRequestRequestTypeDef = TypedDict(
    "UpdateConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": List[str],
    },
)

UpdateNumberOfDomainControllersRequestRequestTypeDef = TypedDict(
    "UpdateNumberOfDomainControllersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "DesiredNumber": int,
    },
)

UpdateRadiusRequestRequestTypeDef = TypedDict(
    "UpdateRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": "RadiusSettingsTypeDef",
    },
)

_RequiredUpdateTrustRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustRequestRequestTypeDef",
    {
        "TrustId": str,
    },
)
_OptionalUpdateTrustRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustRequestRequestTypeDef",
    {
        "SelectiveAuth": SelectiveAuthType,
    },
    total=False,
)

class UpdateTrustRequestRequestTypeDef(
    _RequiredUpdateTrustRequestRequestTypeDef, _OptionalUpdateTrustRequestRequestTypeDef
):
    pass

UpdateTrustResultTypeDef = TypedDict(
    "UpdateTrustResultTypeDef",
    {
        "RequestId": str,
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyTrustRequestRequestTypeDef = TypedDict(
    "VerifyTrustRequestRequestTypeDef",
    {
        "TrustId": str,
    },
)

VerifyTrustResultTypeDef = TypedDict(
    "VerifyTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
