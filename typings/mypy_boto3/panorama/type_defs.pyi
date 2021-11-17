"""
Type annotations for panorama service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/type_defs.html)

Usage::

    ```python
    from mypy_boto3_panorama.type_defs import ApplicationInstanceTypeDef

    data: ApplicationInstanceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ApplicationInstanceHealthStatusType,
    ApplicationInstanceStatusType,
    ConnectionTypeType,
    DeviceConnectionStatusType,
    DeviceStatusType,
    DeviceTypeType,
    NetworkConnectionStatusType,
    NodeCategoryType,
    NodeFromTemplateJobStatusType,
    NodeInstanceStatusType,
    PackageImportJobStatusType,
    PackageVersionStatusType,
    PortTypeType,
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

ApplicationInstanceTypeDef = TypedDict(
    "ApplicationInstanceTypeDef",
    {
        "Name": str,
        "ApplicationInstanceId": str,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "Status": ApplicationInstanceStatusType,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "StatusDescription": str,
        "CreatedTime": datetime,
        "Arn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationInstanceRequestRequestTypeDef",
    {
        "ManifestPayload": "ManifestPayloadTypeDef",
        "DefaultRuntimeContextDevice": str,
    },
)
_OptionalCreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ManifestOverridesPayload": "ManifestOverridesPayloadTypeDef",
        "ApplicationInstanceIdToReplace": str,
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
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "NodeName": str,
        "TemplateParameters": Dict[str, str],
    },
)
_OptionalCreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "NodeDescription": str,
        "JobTags": List["JobResourceTagsTypeDef"],
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
        "JobType": Literal["NODE_PACKAGE_VERSION"],
        "InputConfig": "PackageImportJobInputConfigTypeDef",
        "OutputConfig": "PackageImportJobOutputConfigTypeDef",
        "ClientToken": str,
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
        "PackageId": str,
        "Arn": str,
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
        "Name": str,
        "Description": str,
        "DefaultRuntimeContextDevice": str,
        "ManifestPayload": "ManifestPayloadTypeDef",
        "ManifestOverridesPayload": "ManifestOverridesPayloadTypeDef",
        "ApplicationInstanceIdToReplace": str,
        "CreatedTime": datetime,
        "ApplicationInstanceId": str,
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
        "Name": str,
        "Description": str,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "ApplicationInstanceIdToReplace": str,
        "RuntimeRoleArn": str,
        "Status": ApplicationInstanceStatusType,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "StatusDescription": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ApplicationInstanceId": str,
        "Arn": str,
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
        "JobId": str,
        "DeviceId": str,
        "DeviceArn": str,
        "DeviceName": str,
        "DeviceType": DeviceTypeType,
        "ImageVersion": str,
        "Status": UpdateProgressType,
        "CreatedTime": datetime,
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
        "DeviceId": str,
        "Name": str,
        "Arn": str,
        "Description": str,
        "Type": DeviceTypeType,
        "DeviceConnectionStatus": DeviceConnectionStatusType,
        "CreatedTime": datetime,
        "ProvisioningStatus": DeviceStatusType,
        "LatestSoftware": str,
        "CurrentSoftware": str,
        "SerialNumber": str,
        "Tags": Dict[str, str],
        "NetworkingConfiguration": "NetworkPayloadTypeDef",
        "CurrentNetworkingStatus": "NetworkStatusTypeDef",
        "LeaseExpirationTime": datetime,
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
        "JobId": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "NodeName": str,
        "NodeDescription": str,
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "TemplateParameters": Dict[str, str],
        "JobTags": List["JobResourceTagsTypeDef"],
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
        "NodeId": str,
        "Name": str,
        "Category": NodeCategoryType,
        "OwnerAccount": str,
        "PackageName": str,
        "PackageId": str,
        "PackageArn": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "NodeInterface": "NodeInterfaceTypeDef",
        "AssetName": str,
        "Description": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
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
        "JobId": str,
        "ClientToken": str,
        "JobType": Literal["NODE_PACKAGE_VERSION"],
        "InputConfig": "PackageImportJobInputConfigTypeDef",
        "OutputConfig": "PackageImportJobOutputConfigTypeDef",
        "Output": "PackageImportJobOutputTypeDef",
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
        "JobTags": List["JobResourceTagsTypeDef"],
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
        "PackageId": str,
        "PackageName": str,
        "Arn": str,
        "StorageLocation": "StorageLocationTypeDef",
        "ReadAccessPrincipalArns": List[str],
        "WriteAccessPrincipalArns": List[str],
        "CreatedTime": datetime,
        "Tags": Dict[str, str],
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
        "OwnerAccount": str,
        "PackageId": str,
        "PackageArn": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "IsLatestPatch": bool,
        "Status": PackageVersionStatusType,
        "StatusDescription": str,
        "RegisteredTime": datetime,
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
        "DeviceName": str,
        "DeviceId": str,
        "JobId": str,
        "CreatedTime": datetime,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": str,
        "Name": str,
        "CreatedTime": datetime,
        "ProvisioningStatus": DeviceStatusType,
        "LastUpdatedTime": datetime,
        "LeaseExpirationTime": datetime,
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
        "IpAddress": str,
        "ConnectionStatus": NetworkConnectionStatusType,
        "HwAddress": str,
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
        "JobId": str,
        "DeviceId": str,
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
        "PackageObjects": List["PackageObjectTypeDef"],
        "NextToken": str,
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
        "NodeInstances": List["NodeInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstancesRequestRequestTypeDef",
    {
        "DeviceId": str,
        "StatusFilter": StatusFilterType,
        "MaxResults": int,
        "NextToken": str,
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
        "NextToken": str,
        "MaxResults": int,
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
        "NextToken": str,
        "MaxResults": int,
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
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListNodeFromTemplateJobsResponseTypeDef = TypedDict(
    "ListNodeFromTemplateJobsResponseTypeDef",
    {
        "NodeFromTemplateJobs": List["NodeFromTemplateJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodesRequestRequestTypeDef = TypedDict(
    "ListNodesRequestRequestTypeDef",
    {
        "Category": NodeCategoryType,
        "OwnerAccount": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "Nodes": List["NodeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageImportJobsRequestRequestTypeDef = TypedDict(
    "ListPackageImportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPackageImportJobsResponseTypeDef = TypedDict(
    "ListPackageImportJobsResponseTypeDef",
    {
        "PackageImportJobs": List["PackageImportJobTypeDef"],
        "NextToken": str,
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
        "Packages": List["PackageListItemTypeDef"],
        "NextToken": str,
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
    },
    total=False,
)

NetworkStatusTypeDef = TypedDict(
    "NetworkStatusTypeDef",
    {
        "Ethernet0Status": "EthernetStatusTypeDef",
        "Ethernet1Status": "EthernetStatusTypeDef",
    },
    total=False,
)

NodeFromTemplateJobTypeDef = TypedDict(
    "NodeFromTemplateJobTypeDef",
    {
        "JobId": str,
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "NodeName": str,
    },
    total=False,
)

NodeInputPortTypeDef = TypedDict(
    "NodeInputPortTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": PortTypeType,
        "DefaultValue": str,
        "MaxConnections": int,
    },
    total=False,
)

_RequiredNodeInstanceTypeDef = TypedDict(
    "_RequiredNodeInstanceTypeDef",
    {
        "NodeInstanceId": str,
        "CurrentStatus": NodeInstanceStatusType,
    },
)
_OptionalNodeInstanceTypeDef = TypedDict(
    "_OptionalNodeInstanceTypeDef",
    {
        "NodeId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PackagePatchVersion": str,
        "NodeName": str,
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
        "Name": str,
        "Description": str,
        "Type": PortTypeType,
    },
    total=False,
)

_RequiredNodeTypeDef = TypedDict(
    "_RequiredNodeTypeDef",
    {
        "NodeId": str,
        "Name": str,
        "Category": NodeCategoryType,
        "PackageName": str,
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "CreatedTime": datetime,
    },
)
_OptionalNodeTypeDef = TypedDict(
    "_OptionalNodeTypeDef",
    {
        "OwnerAccount": str,
        "PackageArn": str,
        "Description": str,
    },
    total=False,
)

class NodeTypeDef(_RequiredNodeTypeDef, _OptionalNodeTypeDef):
    pass

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
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "OutputS3Location": "OutPutS3LocationTypeDef",
    },
)

PackageImportJobTypeDef = TypedDict(
    "PackageImportJobTypeDef",
    {
        "JobId": str,
        "JobType": Literal["NODE_PACKAGE_VERSION"],
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

PackageListItemTypeDef = TypedDict(
    "PackageListItemTypeDef",
    {
        "PackageId": str,
        "PackageName": str,
        "Arn": str,
        "CreatedTime": datetime,
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
        "Tags": Dict[str, str],
        "NetworkingConfiguration": "NetworkPayloadTypeDef",
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
        "DeviceId": str,
        "Arn": str,
        "Status": DeviceStatusType,
        "Certificates": bytes,
        "IotThingName": str,
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
        "OwnerAccount": str,
        "MarkLatest": bool,
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
        "IpAddress": str,
        "Mask": str,
        "Dns": List[str],
        "DefaultGateway": str,
    },
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "Bucket": str,
        "RepoPrefixLocation": str,
        "GeneratedPrefixLocation": str,
        "BinaryPrefixLocation": str,
        "ManifestPrefixLocation": str,
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
