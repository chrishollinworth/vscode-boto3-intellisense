"""
Type annotations for panorama service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/type_defs.html)

Usage::

    ```python
    from mypy_boto3_panorama.type_defs import AlternateSoftwareMetadataTypeDef

    data: AlternateSoftwareMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ApplicationInstanceHealthStatusType,
    ApplicationInstanceStatusType,
    ConnectionTypeType,
    DeviceAggregatedStatusType,
    DeviceBrandType,
    DeviceConnectionStatusType,
    DeviceStatusType,
    DeviceTypeType,
    ListDevicesSortByType,
    NetworkConnectionStatusType,
    NodeCategoryType,
    NodeFromTemplateJobStatusType,
    NodeInstanceStatusType,
    PackageImportJobStatusType,
    PackageImportJobTypeType,
    PackageVersionStatusType,
    PortTypeType,
    SortOrderType,
    StatusFilterType,
    UpdateProgressType,
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
    "AlternateSoftwareMetadataTypeDef",
    "ApplicationInstanceTypeDef",
    "CreateApplicationInstanceRequestRequestTypeDef",
    "CreateApplicationInstanceResponseTypeDef",
    "CreateJobForDevicesRequestRequestTypeDef",
    "CreateJobForDevicesResponseTypeDef",
    "CreateNodeFromTemplateJobRequestRequestTypeDef",
    "CreateNodeFromTemplateJobResponseTypeDef",
    "CreatePackageImportJobRequestRequestTypeDef",
    "CreatePackageImportJobResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeregisterPackageVersionRequestRequestTypeDef",
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    "DescribeApplicationInstanceRequestRequestTypeDef",
    "DescribeApplicationInstanceResponseTypeDef",
    "DescribeDeviceJobRequestRequestTypeDef",
    "DescribeDeviceJobResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    "DescribeNodeFromTemplateJobResponseTypeDef",
    "DescribeNodeRequestRequestTypeDef",
    "DescribeNodeResponseTypeDef",
    "DescribePackageImportJobRequestRequestTypeDef",
    "DescribePackageImportJobResponseTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageResponseTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribePackageVersionResponseTypeDef",
    "DeviceJobConfigTypeDef",
    "DeviceJobTypeDef",
    "DeviceTypeDef",
    "EthernetPayloadTypeDef",
    "EthernetStatusTypeDef",
    "JobResourceTagsTypeDef",
    "JobTypeDef",
    "LatestDeviceJobTypeDef",
    "ListApplicationInstanceDependenciesRequestRequestTypeDef",
    "ListApplicationInstanceDependenciesResponseTypeDef",
    "ListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    "ListApplicationInstancesRequestRequestTypeDef",
    "ListApplicationInstancesResponseTypeDef",
    "ListDevicesJobsRequestRequestTypeDef",
    "ListDevicesJobsResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    "ListNodeFromTemplateJobsResponseTypeDef",
    "ListNodesRequestRequestTypeDef",
    "ListNodesResponseTypeDef",
    "ListPackageImportJobsRequestRequestTypeDef",
    "ListPackageImportJobsResponseTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "ListPackagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManifestOverridesPayloadTypeDef",
    "ManifestPayloadTypeDef",
    "NetworkPayloadTypeDef",
    "NetworkStatusTypeDef",
    "NodeFromTemplateJobTypeDef",
    "NodeInputPortTypeDef",
    "NodeInstanceTypeDef",
    "NodeInterfaceTypeDef",
    "NodeOutputPortTypeDef",
    "NodeTypeDef",
    "NtpPayloadTypeDef",
    "NtpStatusTypeDef",
    "OTAJobConfigTypeDef",
    "OutPutS3LocationTypeDef",
    "PackageImportJobInputConfigTypeDef",
    "PackageImportJobOutputConfigTypeDef",
    "PackageImportJobOutputTypeDef",
    "PackageImportJobTypeDef",
    "PackageListItemTypeDef",
    "PackageObjectTypeDef",
    "PackageVersionInputConfigTypeDef",
    "PackageVersionOutputConfigTypeDef",
    "ProvisionDeviceRequestRequestTypeDef",
    "ProvisionDeviceResponseTypeDef",
    "RegisterPackageVersionRequestRequestTypeDef",
    "RemoveApplicationInstanceRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StaticIpConnectionInfoTypeDef",
    "StorageLocationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceMetadataRequestRequestTypeDef",
    "UpdateDeviceMetadataResponseTypeDef",
)

AlternateSoftwareMetadataTypeDef = TypedDict(
    "AlternateSoftwareMetadataTypeDef",
    {
        "Version": str,
    },
    total=False,
)

ApplicationInstanceTypeDef = TypedDict(
    "ApplicationInstanceTypeDef",
    {
        "ApplicationInstanceId": str,
        "Arn": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "Name": str,
        "Status": ApplicationInstanceStatusType,
        "StatusDescription": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationInstanceRequestRequestTypeDef",
    {
        "DefaultRuntimeContextDevice": str,
        "ManifestPayload": "ManifestPayloadTypeDef",
    },
)
_OptionalCreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceIdToReplace": str,
        "Description": str,
        "ManifestOverridesPayload": "ManifestOverridesPayloadTypeDef",
        "Name": str,
        "RuntimeRoleArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationInstanceRequestRequestTypeDef(
    _RequiredCreateApplicationInstanceRequestRequestTypeDef,
    _OptionalCreateApplicationInstanceRequestRequestTypeDef,
):
    pass

CreateApplicationInstanceResponseTypeDef = TypedDict(
    "CreateApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobForDevicesRequestRequestTypeDef = TypedDict(
    "CreateJobForDevicesRequestRequestTypeDef",
    {
        "DeviceIds": List[str],
        "DeviceJobConfig": "DeviceJobConfigTypeDef",
        "JobType": Literal["OTA"],
    },
)

CreateJobForDevicesResponseTypeDef = TypedDict(
    "CreateJobForDevicesResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "TemplateParameters": Dict[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
    },
)
_OptionalCreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "JobTags": List["JobResourceTagsTypeDef"],
        "NodeDescription": str,
    },
    total=False,
)

class CreateNodeFromTemplateJobRequestRequestTypeDef(
    _RequiredCreateNodeFromTemplateJobRequestRequestTypeDef,
    _OptionalCreateNodeFromTemplateJobRequestRequestTypeDef,
):
    pass

CreateNodeFromTemplateJobResponseTypeDef = TypedDict(
    "CreateNodeFromTemplateJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageImportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InputConfig": "PackageImportJobInputConfigTypeDef",
        "JobType": PackageImportJobTypeType,
        "OutputConfig": "PackageImportJobOutputConfigTypeDef",
    },
)
_OptionalCreatePackageImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageImportJobRequestRequestTypeDef",
    {
        "JobTags": List["JobResourceTagsTypeDef"],
    },
    total=False,
)

class CreatePackageImportJobRequestRequestTypeDef(
    _RequiredCreatePackageImportJobRequestRequestTypeDef,
    _OptionalCreatePackageImportJobRequestRequestTypeDef,
):
    pass

CreatePackageImportJobResponseTypeDef = TypedDict(
    "CreatePackageImportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
    },
)
_OptionalCreatePackageRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
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
        "Arn": str,
        "PackageId": str,
        "StorageLocation": "StorageLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageRequestRequestTypeDef",
    {
        "PackageId": str,
    },
)
_OptionalDeletePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageRequestRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)

class DeletePackageRequestRequestTypeDef(
    _RequiredDeletePackageRequestRequestTypeDef, _OptionalDeletePackageRequestRequestTypeDef
):
    pass

_RequiredDeregisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
_OptionalDeregisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterPackageVersionRequestRequestTypeDef",
    {
        "OwnerAccount": str,
        "UpdatedLatestPatchVersion": str,
    },
    total=False,
)

class DeregisterPackageVersionRequestRequestTypeDef(
    _RequiredDeregisterPackageVersionRequestRequestTypeDef,
    _OptionalDeregisterPackageVersionRequestRequestTypeDef,
):
    pass

DescribeApplicationInstanceDetailsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

DescribeApplicationInstanceDetailsResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "Description": str,
        "ManifestOverridesPayload": "ManifestOverridesPayloadTypeDef",
        "ManifestPayload": "ManifestPayloadTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationInstanceRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

DescribeApplicationInstanceResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "Arn": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "LastUpdatedTime": datetime,
        "Name": str,
        "RuntimeRoleArn": str,
        "Status": ApplicationInstanceStatusType,
        "StatusDescription": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceJobRequestRequestTypeDef = TypedDict(
    "DescribeDeviceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDeviceJobResponseTypeDef = TypedDict(
    "DescribeDeviceJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "DeviceArn": str,
        "DeviceId": str,
        "DeviceName": str,
        "DeviceType": DeviceTypeType,
        "ImageVersion": str,
        "JobId": str,
        "Status": UpdateProgressType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "AlternateSoftwares": List["AlternateSoftwareMetadataTypeDef"],
        "Arn": str,
        "Brand": DeviceBrandType,
        "CreatedTime": datetime,
        "CurrentNetworkingStatus": "NetworkStatusTypeDef",
        "CurrentSoftware": str,
        "Description": str,
        "DeviceAggregatedStatus": DeviceAggregatedStatusType,
        "DeviceConnectionStatus": DeviceConnectionStatusType,
        "DeviceId": str,
        "LatestAlternateSoftware": str,
        "LatestDeviceJob": "LatestDeviceJobTypeDef",
        "LatestSoftware": str,
        "LeaseExpirationTime": datetime,
        "Name": str,
        "NetworkingConfiguration": "NetworkPayloadTypeDef",
        "ProvisioningStatus": DeviceStatusType,
        "SerialNumber": str,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeNodeFromTemplateJobResponseTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "JobTags": List["JobResourceTagsTypeDef"],
        "LastUpdatedTime": datetime,
        "NodeDescription": str,
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "TemplateParameters": Dict[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeNodeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeNodeRequestRequestTypeDef",
    {
        "NodeId": str,
    },
)
_OptionalDescribeNodeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeNodeRequestRequestTypeDef",
    {
        "OwnerAccount": str,
    },
    total=False,
)

class DescribeNodeRequestRequestTypeDef(
    _RequiredDescribeNodeRequestRequestTypeDef, _OptionalDescribeNodeRequestRequestTypeDef
):
    pass

DescribeNodeResponseTypeDef = TypedDict(
    "DescribeNodeResponseTypeDef",
    {
        "AssetName": str,
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Description": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "NodeInterface": "NodeInterfaceTypeDef",
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackageImportJobRequestRequestTypeDef = TypedDict(
    "DescribePackageImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePackageImportJobResponseTypeDef = TypedDict(
    "DescribePackageImportJobResponseTypeDef",
    {
        "ClientToken": str,
        "CreatedTime": datetime,
        "InputConfig": "PackageImportJobInputConfigTypeDef",
        "JobId": str,
        "JobTags": List["JobResourceTagsTypeDef"],
        "JobType": PackageImportJobTypeType,
        "LastUpdatedTime": datetime,
        "Output": "PackageImportJobOutputTypeDef",
        "OutputConfig": "PackageImportJobOutputConfigTypeDef",
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackageRequestRequestTypeDef = TypedDict(
    "DescribePackageRequestRequestTypeDef",
    {
        "PackageId": str,
    },
)

DescribePackageResponseTypeDef = TypedDict(
    "DescribePackageResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "PackageId": str,
        "PackageName": str,
        "ReadAccessPrincipalArns": List[str],
        "StorageLocation": "StorageLocationTypeDef",
        "Tags": Dict[str, str],
        "WriteAccessPrincipalArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
    },
)
_OptionalDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageVersionRequestRequestTypeDef",
    {
        "OwnerAccount": str,
        "PatchVersion": str,
    },
    total=False,
)

class DescribePackageVersionRequestRequestTypeDef(
    _RequiredDescribePackageVersionRequestRequestTypeDef,
    _OptionalDescribePackageVersionRequestRequestTypeDef,
):
    pass

DescribePackageVersionResponseTypeDef = TypedDict(
    "DescribePackageVersionResponseTypeDef",
    {
        "IsLatestPatch": bool,
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "RegisteredTime": datetime,
        "Status": PackageVersionStatusType,
        "StatusDescription": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceJobConfigTypeDef = TypedDict(
    "DeviceJobConfigTypeDef",
    {
        "OTAJobConfig": "OTAJobConfigTypeDef",
    },
    total=False,
)

DeviceJobTypeDef = TypedDict(
    "DeviceJobTypeDef",
    {
        "CreatedTime": datetime,
        "DeviceId": str,
        "DeviceName": str,
        "JobId": str,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Brand": DeviceBrandType,
        "CreatedTime": datetime,
        "CurrentSoftware": str,
        "Description": str,
        "DeviceAggregatedStatus": DeviceAggregatedStatusType,
        "DeviceId": str,
        "LastUpdatedTime": datetime,
        "LatestDeviceJob": "LatestDeviceJobTypeDef",
        "LeaseExpirationTime": datetime,
        "Name": str,
        "ProvisioningStatus": DeviceStatusType,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
    },
    total=False,
)

_RequiredEthernetPayloadTypeDef = TypedDict(
    "_RequiredEthernetPayloadTypeDef",
    {
        "ConnectionType": ConnectionTypeType,
    },
)
_OptionalEthernetPayloadTypeDef = TypedDict(
    "_OptionalEthernetPayloadTypeDef",
    {
        "StaticIpConnectionInfo": "StaticIpConnectionInfoTypeDef",
    },
    total=False,
)

class EthernetPayloadTypeDef(_RequiredEthernetPayloadTypeDef, _OptionalEthernetPayloadTypeDef):
    pass

EthernetStatusTypeDef = TypedDict(
    "EthernetStatusTypeDef",
    {
        "ConnectionStatus": NetworkConnectionStatusType,
        "HwAddress": str,
        "IpAddress": str,
    },
    total=False,
)

JobResourceTagsTypeDef = TypedDict(
    "JobResourceTagsTypeDef",
    {
        "ResourceType": Literal["PACKAGE"],
        "Tags": Dict[str, str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "DeviceId": str,
        "JobId": str,
    },
    total=False,
)

LatestDeviceJobTypeDef = TypedDict(
    "LatestDeviceJobTypeDef",
    {
        "ImageVersion": str,
        "Status": UpdateProgressType,
    },
    total=False,
)

_RequiredListApplicationInstanceDependenciesRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationInstanceDependenciesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)
_OptionalListApplicationInstanceDependenciesRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationInstanceDependenciesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationInstanceDependenciesRequestRequestTypeDef(
    _RequiredListApplicationInstanceDependenciesRequestRequestTypeDef,
    _OptionalListApplicationInstanceDependenciesRequestRequestTypeDef,
):
    pass

ListApplicationInstanceDependenciesResponseTypeDef = TypedDict(
    "ListApplicationInstanceDependenciesResponseTypeDef",
    {
        "NextToken": str,
        "PackageObjects": List["PackageObjectTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)
_OptionalListApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationInstanceNodeInstancesRequestRequestTypeDef(
    _RequiredListApplicationInstanceNodeInstancesRequestRequestTypeDef,
    _OptionalListApplicationInstanceNodeInstancesRequestRequestTypeDef,
):
    pass

ListApplicationInstanceNodeInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInstances": List["NodeInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstancesRequestRequestTypeDef",
    {
        "DeviceId": str,
        "MaxResults": int,
        "NextToken": str,
        "StatusFilter": StatusFilterType,
    },
    total=False,
)

ListApplicationInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstancesResponseTypeDef",
    {
        "ApplicationInstances": List["ApplicationInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesJobsRequestRequestTypeDef = TypedDict(
    "ListDevicesJobsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDevicesJobsResponseTypeDef = TypedDict(
    "ListDevicesJobsResponseTypeDef",
    {
        "DeviceJobs": List["DeviceJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceAggregatedStatusFilter": DeviceAggregatedStatusType,
        "MaxResults": int,
        "NameFilter": str,
        "NextToken": str,
        "SortBy": ListDevicesSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodeFromTemplateJobsRequestRequestTypeDef = TypedDict(
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListNodeFromTemplateJobsResponseTypeDef = TypedDict(
    "ListNodeFromTemplateJobsResponseTypeDef",
    {
        "NextToken": str,
        "NodeFromTemplateJobs": List["NodeFromTemplateJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodesRequestRequestTypeDef = TypedDict(
    "ListNodesRequestRequestTypeDef",
    {
        "Category": NodeCategoryType,
        "MaxResults": int,
        "NextToken": str,
        "OwnerAccount": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
    total=False,
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "Nodes": List["NodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageImportJobsRequestRequestTypeDef = TypedDict(
    "ListPackageImportJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPackageImportJobsResponseTypeDef = TypedDict(
    "ListPackageImportJobsResponseTypeDef",
    {
        "NextToken": str,
        "PackageImportJobs": List["PackageImportJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPackagesResponseTypeDef = TypedDict(
    "ListPackagesResponseTypeDef",
    {
        "NextToken": str,
        "Packages": List["PackageListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManifestOverridesPayloadTypeDef = TypedDict(
    "ManifestOverridesPayloadTypeDef",
    {
        "PayloadData": str,
    },
    total=False,
)

ManifestPayloadTypeDef = TypedDict(
    "ManifestPayloadTypeDef",
    {
        "PayloadData": str,
    },
    total=False,
)

NetworkPayloadTypeDef = TypedDict(
    "NetworkPayloadTypeDef",
    {
        "Ethernet0": "EthernetPayloadTypeDef",
        "Ethernet1": "EthernetPayloadTypeDef",
        "Ntp": "NtpPayloadTypeDef",
    },
    total=False,
)

NetworkStatusTypeDef = TypedDict(
    "NetworkStatusTypeDef",
    {
        "Ethernet0Status": "EthernetStatusTypeDef",
        "Ethernet1Status": "EthernetStatusTypeDef",
        "LastUpdatedTime": datetime,
        "NtpStatus": "NtpStatusTypeDef",
    },
    total=False,
)

NodeFromTemplateJobTypeDef = TypedDict(
    "NodeFromTemplateJobTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "NodeName": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
    },
    total=False,
)

NodeInputPortTypeDef = TypedDict(
    "NodeInputPortTypeDef",
    {
        "DefaultValue": str,
        "Description": str,
        "MaxConnections": int,
        "Name": str,
        "Type": PortTypeType,
    },
    total=False,
)

_RequiredNodeInstanceTypeDef = TypedDict(
    "_RequiredNodeInstanceTypeDef",
    {
        "CurrentStatus": NodeInstanceStatusType,
        "NodeInstanceId": str,
    },
)
_OptionalNodeInstanceTypeDef = TypedDict(
    "_OptionalNodeInstanceTypeDef",
    {
        "NodeId": str,
        "NodeName": str,
        "PackageName": str,
        "PackagePatchVersion": str,
        "PackageVersion": str,
    },
    total=False,
)

class NodeInstanceTypeDef(_RequiredNodeInstanceTypeDef, _OptionalNodeInstanceTypeDef):
    pass

NodeInterfaceTypeDef = TypedDict(
    "NodeInterfaceTypeDef",
    {
        "Inputs": List["NodeInputPortTypeDef"],
        "Outputs": List["NodeOutputPortTypeDef"],
    },
)

NodeOutputPortTypeDef = TypedDict(
    "NodeOutputPortTypeDef",
    {
        "Description": str,
        "Name": str,
        "Type": PortTypeType,
    },
    total=False,
)

_RequiredNodeTypeDef = TypedDict(
    "_RequiredNodeTypeDef",
    {
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
_OptionalNodeTypeDef = TypedDict(
    "_OptionalNodeTypeDef",
    {
        "Description": str,
        "OwnerAccount": str,
        "PackageArn": str,
    },
    total=False,
)

class NodeTypeDef(_RequiredNodeTypeDef, _OptionalNodeTypeDef):
    pass

NtpPayloadTypeDef = TypedDict(
    "NtpPayloadTypeDef",
    {
        "NtpServers": List[str],
    },
)

NtpStatusTypeDef = TypedDict(
    "NtpStatusTypeDef",
    {
        "ConnectionStatus": NetworkConnectionStatusType,
        "IpAddress": str,
        "NtpServerName": str,
    },
    total=False,
)

OTAJobConfigTypeDef = TypedDict(
    "OTAJobConfigTypeDef",
    {
        "ImageVersion": str,
    },
)

OutPutS3LocationTypeDef = TypedDict(
    "OutPutS3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)

PackageImportJobInputConfigTypeDef = TypedDict(
    "PackageImportJobInputConfigTypeDef",
    {
        "PackageVersionInputConfig": "PackageVersionInputConfigTypeDef",
    },
    total=False,
)

PackageImportJobOutputConfigTypeDef = TypedDict(
    "PackageImportJobOutputConfigTypeDef",
    {
        "PackageVersionOutputConfig": "PackageVersionOutputConfigTypeDef",
    },
    total=False,
)

PackageImportJobOutputTypeDef = TypedDict(
    "PackageImportJobOutputTypeDef",
    {
        "OutputS3Location": "OutPutS3LocationTypeDef",
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)

PackageImportJobTypeDef = TypedDict(
    "PackageImportJobTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "JobType": PackageImportJobTypeType,
        "LastUpdatedTime": datetime,
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
    },
    total=False,
)

PackageListItemTypeDef = TypedDict(
    "PackageListItemTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "PackageId": str,
        "PackageName": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

PackageObjectTypeDef = TypedDict(
    "PackageObjectTypeDef",
    {
        "Name": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)

PackageVersionInputConfigTypeDef = TypedDict(
    "PackageVersionInputConfigTypeDef",
    {
        "S3Location": "S3LocationTypeDef",
    },
)

_RequiredPackageVersionOutputConfigTypeDef = TypedDict(
    "_RequiredPackageVersionOutputConfigTypeDef",
    {
        "PackageName": str,
        "PackageVersion": str,
    },
)
_OptionalPackageVersionOutputConfigTypeDef = TypedDict(
    "_OptionalPackageVersionOutputConfigTypeDef",
    {
        "MarkLatest": bool,
    },
    total=False,
)

class PackageVersionOutputConfigTypeDef(
    _RequiredPackageVersionOutputConfigTypeDef, _OptionalPackageVersionOutputConfigTypeDef
):
    pass

_RequiredProvisionDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionDeviceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalProvisionDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionDeviceRequestRequestTypeDef",
    {
        "Description": str,
        "NetworkingConfiguration": "NetworkPayloadTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class ProvisionDeviceRequestRequestTypeDef(
    _RequiredProvisionDeviceRequestRequestTypeDef, _OptionalProvisionDeviceRequestRequestTypeDef
):
    pass

ProvisionDeviceResponseTypeDef = TypedDict(
    "ProvisionDeviceResponseTypeDef",
    {
        "Arn": str,
        "Certificates": bytes,
        "DeviceId": str,
        "IotThingName": str,
        "Status": DeviceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
_OptionalRegisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterPackageVersionRequestRequestTypeDef",
    {
        "MarkLatest": bool,
        "OwnerAccount": str,
    },
    total=False,
)

class RegisterPackageVersionRequestRequestTypeDef(
    _RequiredRegisterPackageVersionRequestRequestTypeDef,
    _OptionalRegisterPackageVersionRequestRequestTypeDef,
):
    pass

RemoveApplicationInstanceRequestRequestTypeDef = TypedDict(
    "RemoveApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
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

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Region": str,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

StaticIpConnectionInfoTypeDef = TypedDict(
    "StaticIpConnectionInfoTypeDef",
    {
        "DefaultGateway": str,
        "Dns": List[str],
        "IpAddress": str,
        "Mask": str,
    },
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "BinaryPrefixLocation": str,
        "Bucket": str,
        "GeneratedPrefixLocation": str,
        "ManifestPrefixLocation": str,
        "RepoPrefixLocation": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDeviceMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceMetadataRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceMetadataRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateDeviceMetadataRequestRequestTypeDef(
    _RequiredUpdateDeviceMetadataRequestRequestTypeDef,
    _OptionalUpdateDeviceMetadataRequestRequestTypeDef,
):
    pass

UpdateDeviceMetadataResponseTypeDef = TypedDict(
    "UpdateDeviceMetadataResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
