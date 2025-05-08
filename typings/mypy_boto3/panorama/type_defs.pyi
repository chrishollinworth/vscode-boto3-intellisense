"""
Type annotations for panorama service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_panorama/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_panorama.type_defs import AlternateSoftwareMetadataTypeDef

    data: AlternateSoftwareMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ApplicationInstanceHealthStatusType,
    ApplicationInstanceStatusType,
    ConnectionTypeType,
    DesiredStateType,
    DeviceAggregatedStatusType,
    DeviceBrandType,
    DeviceConnectionStatusType,
    DeviceReportedStatusType,
    DeviceStatusType,
    DeviceTypeType,
    JobTypeType,
    ListDevicesSortByType,
    NetworkConnectionStatusType,
    NodeCategoryType,
    NodeFromTemplateJobStatusType,
    NodeInstanceStatusType,
    NodeSignalValueType,
    PackageImportJobStatusType,
    PackageImportJobTypeType,
    PackageVersionStatusType,
    PortTypeType,
    SortOrderType,
    StatusFilterType,
    UpdateProgressType,
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
    "AlternateSoftwareMetadataTypeDef",
    "ApplicationInstanceTypeDef",
    "CreateApplicationInstanceRequestTypeDef",
    "CreateApplicationInstanceResponseTypeDef",
    "CreateJobForDevicesRequestTypeDef",
    "CreateJobForDevicesResponseTypeDef",
    "CreateNodeFromTemplateJobRequestTypeDef",
    "CreateNodeFromTemplateJobResponseTypeDef",
    "CreatePackageImportJobRequestTypeDef",
    "CreatePackageImportJobResponseTypeDef",
    "CreatePackageRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteDeviceRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeletePackageRequestTypeDef",
    "DeregisterPackageVersionRequestTypeDef",
    "DescribeApplicationInstanceDetailsRequestTypeDef",
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    "DescribeApplicationInstanceRequestTypeDef",
    "DescribeApplicationInstanceResponseTypeDef",
    "DescribeDeviceJobRequestTypeDef",
    "DescribeDeviceJobResponseTypeDef",
    "DescribeDeviceRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeNodeFromTemplateJobRequestTypeDef",
    "DescribeNodeFromTemplateJobResponseTypeDef",
    "DescribeNodeRequestTypeDef",
    "DescribeNodeResponseTypeDef",
    "DescribePackageImportJobRequestTypeDef",
    "DescribePackageImportJobResponseTypeDef",
    "DescribePackageRequestTypeDef",
    "DescribePackageResponseTypeDef",
    "DescribePackageVersionRequestTypeDef",
    "DescribePackageVersionResponseTypeDef",
    "DeviceJobConfigTypeDef",
    "DeviceJobTypeDef",
    "DeviceTypeDef",
    "EthernetPayloadOutputTypeDef",
    "EthernetPayloadTypeDef",
    "EthernetStatusTypeDef",
    "JobResourceTagsOutputTypeDef",
    "JobResourceTagsTypeDef",
    "JobResourceTagsUnionTypeDef",
    "JobTypeDef",
    "LatestDeviceJobTypeDef",
    "ListApplicationInstanceDependenciesRequestTypeDef",
    "ListApplicationInstanceDependenciesResponseTypeDef",
    "ListApplicationInstanceNodeInstancesRequestTypeDef",
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    "ListApplicationInstancesRequestTypeDef",
    "ListApplicationInstancesResponseTypeDef",
    "ListDevicesJobsRequestTypeDef",
    "ListDevicesJobsResponseTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListNodeFromTemplateJobsRequestTypeDef",
    "ListNodeFromTemplateJobsResponseTypeDef",
    "ListNodesRequestTypeDef",
    "ListNodesResponseTypeDef",
    "ListPackageImportJobsRequestTypeDef",
    "ListPackageImportJobsResponseTypeDef",
    "ListPackagesRequestTypeDef",
    "ListPackagesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManifestOverridesPayloadTypeDef",
    "ManifestPayloadTypeDef",
    "NetworkPayloadOutputTypeDef",
    "NetworkPayloadTypeDef",
    "NetworkPayloadUnionTypeDef",
    "NetworkStatusTypeDef",
    "NodeFromTemplateJobTypeDef",
    "NodeInputPortTypeDef",
    "NodeInstanceTypeDef",
    "NodeInterfaceTypeDef",
    "NodeOutputPortTypeDef",
    "NodeSignalTypeDef",
    "NodeTypeDef",
    "NtpPayloadOutputTypeDef",
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
    "ProvisionDeviceRequestTypeDef",
    "ProvisionDeviceResponseTypeDef",
    "RegisterPackageVersionRequestTypeDef",
    "RemoveApplicationInstanceRequestTypeDef",
    "ReportedRuntimeContextStateTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SignalApplicationInstanceNodeInstancesRequestTypeDef",
    "SignalApplicationInstanceNodeInstancesResponseTypeDef",
    "StaticIpConnectionInfoOutputTypeDef",
    "StaticIpConnectionInfoTypeDef",
    "StorageLocationTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeviceMetadataRequestTypeDef",
    "UpdateDeviceMetadataResponseTypeDef",
)

class AlternateSoftwareMetadataTypeDef(TypedDict):
    Version: NotRequired[str]

class ReportedRuntimeContextStateTypeDef(TypedDict):
    DesiredState: DesiredStateType
    DeviceReportedStatus: DeviceReportedStatusType
    DeviceReportedTime: datetime
    RuntimeContextName: str

class ManifestOverridesPayloadTypeDef(TypedDict):
    PayloadData: NotRequired[str]

class ManifestPayloadTypeDef(TypedDict):
    PayloadData: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class JobTypeDef(TypedDict):
    DeviceId: NotRequired[str]
    JobId: NotRequired[str]

class CreatePackageRequestTypeDef(TypedDict):
    PackageName: str
    Tags: NotRequired[Mapping[str, str]]

class StorageLocationTypeDef(TypedDict):
    BinaryPrefixLocation: str
    Bucket: str
    GeneratedPrefixLocation: str
    ManifestPrefixLocation: str
    RepoPrefixLocation: str

class DeleteDeviceRequestTypeDef(TypedDict):
    DeviceId: str

class DeletePackageRequestTypeDef(TypedDict):
    PackageId: str
    ForceDelete: NotRequired[bool]

class DeregisterPackageVersionRequestTypeDef(TypedDict):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    OwnerAccount: NotRequired[str]
    UpdatedLatestPatchVersion: NotRequired[str]

class DescribeApplicationInstanceDetailsRequestTypeDef(TypedDict):
    ApplicationInstanceId: str

class DescribeApplicationInstanceRequestTypeDef(TypedDict):
    ApplicationInstanceId: str

class DescribeDeviceJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeDeviceRequestTypeDef(TypedDict):
    DeviceId: str

class LatestDeviceJobTypeDef(TypedDict):
    ImageVersion: NotRequired[str]
    JobType: NotRequired[JobTypeType]
    Status: NotRequired[UpdateProgressType]

class DescribeNodeFromTemplateJobRequestTypeDef(TypedDict):
    JobId: str

class JobResourceTagsOutputTypeDef(TypedDict):
    ResourceType: Literal["PACKAGE"]
    Tags: Dict[str, str]

class DescribeNodeRequestTypeDef(TypedDict):
    NodeId: str
    OwnerAccount: NotRequired[str]

class DescribePackageImportJobRequestTypeDef(TypedDict):
    JobId: str

class DescribePackageRequestTypeDef(TypedDict):
    PackageId: str

class DescribePackageVersionRequestTypeDef(TypedDict):
    PackageId: str
    PackageVersion: str
    OwnerAccount: NotRequired[str]
    PatchVersion: NotRequired[str]

class OTAJobConfigTypeDef(TypedDict):
    ImageVersion: str
    AllowMajorVersionUpdate: NotRequired[bool]

class DeviceJobTypeDef(TypedDict):
    CreatedTime: NotRequired[datetime]
    DeviceId: NotRequired[str]
    DeviceName: NotRequired[str]
    JobId: NotRequired[str]
    JobType: NotRequired[JobTypeType]

class StaticIpConnectionInfoOutputTypeDef(TypedDict):
    DefaultGateway: str
    Dns: List[str]
    IpAddress: str
    Mask: str

class StaticIpConnectionInfoTypeDef(TypedDict):
    DefaultGateway: str
    Dns: Sequence[str]
    IpAddress: str
    Mask: str

class EthernetStatusTypeDef(TypedDict):
    ConnectionStatus: NotRequired[NetworkConnectionStatusType]
    HwAddress: NotRequired[str]
    IpAddress: NotRequired[str]

class JobResourceTagsTypeDef(TypedDict):
    ResourceType: Literal["PACKAGE"]
    Tags: Mapping[str, str]

class ListApplicationInstanceDependenciesRequestTypeDef(TypedDict):
    ApplicationInstanceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PackageObjectTypeDef(TypedDict):
    Name: str
    PackageVersion: str
    PatchVersion: str

class ListApplicationInstanceNodeInstancesRequestTypeDef(TypedDict):
    ApplicationInstanceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class NodeInstanceTypeDef(TypedDict):
    CurrentStatus: NodeInstanceStatusType
    NodeInstanceId: str
    NodeId: NotRequired[str]
    NodeName: NotRequired[str]
    PackageName: NotRequired[str]
    PackagePatchVersion: NotRequired[str]
    PackageVersion: NotRequired[str]

class ListApplicationInstancesRequestTypeDef(TypedDict):
    DeviceId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    StatusFilter: NotRequired[StatusFilterType]

class ListDevicesJobsRequestTypeDef(TypedDict):
    DeviceId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListDevicesRequestTypeDef(TypedDict):
    DeviceAggregatedStatusFilter: NotRequired[DeviceAggregatedStatusType]
    MaxResults: NotRequired[int]
    NameFilter: NotRequired[str]
    NextToken: NotRequired[str]
    SortBy: NotRequired[ListDevicesSortByType]
    SortOrder: NotRequired[SortOrderType]

class ListNodeFromTemplateJobsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class NodeFromTemplateJobTypeDef(TypedDict):
    CreatedTime: NotRequired[datetime]
    JobId: NotRequired[str]
    NodeName: NotRequired[str]
    Status: NotRequired[NodeFromTemplateJobStatusType]
    StatusMessage: NotRequired[str]
    TemplateType: NotRequired[Literal["RTSP_CAMERA_STREAM"]]

class ListNodesRequestTypeDef(TypedDict):
    Category: NotRequired[NodeCategoryType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    OwnerAccount: NotRequired[str]
    PackageName: NotRequired[str]
    PackageVersion: NotRequired[str]
    PatchVersion: NotRequired[str]

class NodeTypeDef(TypedDict):
    Category: NodeCategoryType
    CreatedTime: datetime
    Name: str
    NodeId: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    Description: NotRequired[str]
    OwnerAccount: NotRequired[str]
    PackageArn: NotRequired[str]

class ListPackageImportJobsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PackageImportJobTypeDef(TypedDict):
    CreatedTime: NotRequired[datetime]
    JobId: NotRequired[str]
    JobType: NotRequired[PackageImportJobTypeType]
    LastUpdatedTime: NotRequired[datetime]
    Status: NotRequired[PackageImportJobStatusType]
    StatusMessage: NotRequired[str]

class ListPackagesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PackageListItemTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    PackageId: NotRequired[str]
    PackageName: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class NtpPayloadOutputTypeDef(TypedDict):
    NtpServers: List[str]

class NtpPayloadTypeDef(TypedDict):
    NtpServers: Sequence[str]

class NtpStatusTypeDef(TypedDict):
    ConnectionStatus: NotRequired[NetworkConnectionStatusType]
    IpAddress: NotRequired[str]
    NtpServerName: NotRequired[str]

NodeInputPortTypeDef = TypedDict(
    "NodeInputPortTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "MaxConnections": NotRequired[int],
        "Name": NotRequired[str],
        "Type": NotRequired[PortTypeType],
    },
)
NodeOutputPortTypeDef = TypedDict(
    "NodeOutputPortTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[PortTypeType],
    },
)

class NodeSignalTypeDef(TypedDict):
    NodeInstanceId: str
    Signal: NodeSignalValueType

class OutPutS3LocationTypeDef(TypedDict):
    BucketName: str
    ObjectKey: str

class PackageVersionOutputConfigTypeDef(TypedDict):
    PackageName: str
    PackageVersion: str
    MarkLatest: NotRequired[bool]

class S3LocationTypeDef(TypedDict):
    BucketName: str
    ObjectKey: str
    Region: NotRequired[str]

class RegisterPackageVersionRequestTypeDef(TypedDict):
    PackageId: str
    PackageVersion: str
    PatchVersion: str
    MarkLatest: NotRequired[bool]
    OwnerAccount: NotRequired[str]

class RemoveApplicationInstanceRequestTypeDef(TypedDict):
    ApplicationInstanceId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDeviceMetadataRequestTypeDef(TypedDict):
    DeviceId: str
    Description: NotRequired[str]

class ApplicationInstanceTypeDef(TypedDict):
    ApplicationInstanceId: NotRequired[str]
    Arn: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    DefaultRuntimeContextDevice: NotRequired[str]
    DefaultRuntimeContextDeviceName: NotRequired[str]
    Description: NotRequired[str]
    HealthStatus: NotRequired[ApplicationInstanceHealthStatusType]
    Name: NotRequired[str]
    RuntimeContextStates: NotRequired[List[ReportedRuntimeContextStateTypeDef]]
    Status: NotRequired[ApplicationInstanceStatusType]
    StatusDescription: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class CreateApplicationInstanceRequestTypeDef(TypedDict):
    DefaultRuntimeContextDevice: str
    ManifestPayload: ManifestPayloadTypeDef
    ApplicationInstanceIdToReplace: NotRequired[str]
    Description: NotRequired[str]
    ManifestOverridesPayload: NotRequired[ManifestOverridesPayloadTypeDef]
    Name: NotRequired[str]
    RuntimeRoleArn: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateApplicationInstanceResponseTypeDef(TypedDict):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeFromTemplateJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageImportJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeviceResponseTypeDef(TypedDict):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationInstanceDetailsResponseTypeDef(TypedDict):
    ApplicationInstanceId: str
    ApplicationInstanceIdToReplace: str
    CreatedTime: datetime
    DefaultRuntimeContextDevice: str
    Description: str
    ManifestOverridesPayload: ManifestOverridesPayloadTypeDef
    ManifestPayload: ManifestPayloadTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationInstanceResponseTypeDef(TypedDict):
    ApplicationInstanceId: str
    ApplicationInstanceIdToReplace: str
    Arn: str
    CreatedTime: datetime
    DefaultRuntimeContextDevice: str
    DefaultRuntimeContextDeviceName: str
    Description: str
    HealthStatus: ApplicationInstanceHealthStatusType
    LastUpdatedTime: datetime
    Name: str
    RuntimeContextStates: List[ReportedRuntimeContextStateTypeDef]
    RuntimeRoleArn: str
    Status: ApplicationInstanceStatusType
    StatusDescription: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeviceJobResponseTypeDef(TypedDict):
    CreatedTime: datetime
    DeviceArn: str
    DeviceId: str
    DeviceName: str
    DeviceType: DeviceTypeType
    ImageVersion: str
    JobId: str
    JobType: JobTypeType
    Status: UpdateProgressType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageVersionResponseTypeDef(TypedDict):
    IsLatestPatch: bool
    OwnerAccount: str
    PackageArn: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    RegisteredTime: datetime
    Status: PackageVersionStatusType
    StatusDescription: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionDeviceResponseTypeDef(TypedDict):
    Arn: str
    Certificates: bytes
    DeviceId: str
    IotThingName: str
    Status: DeviceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class SignalApplicationInstanceNodeInstancesResponseTypeDef(TypedDict):
    ApplicationInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceMetadataResponseTypeDef(TypedDict):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobForDevicesResponseTypeDef(TypedDict):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageResponseTypeDef(TypedDict):
    Arn: str
    PackageId: str
    StorageLocation: StorageLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageResponseTypeDef(TypedDict):
    Arn: str
    CreatedTime: datetime
    PackageId: str
    PackageName: str
    ReadAccessPrincipalArns: List[str]
    StorageLocation: StorageLocationTypeDef
    Tags: Dict[str, str]
    WriteAccessPrincipalArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Brand": NotRequired[DeviceBrandType],
        "CreatedTime": NotRequired[datetime],
        "CurrentSoftware": NotRequired[str],
        "Description": NotRequired[str],
        "DeviceAggregatedStatus": NotRequired[DeviceAggregatedStatusType],
        "DeviceId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "LatestDeviceJob": NotRequired[LatestDeviceJobTypeDef],
        "LeaseExpirationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "ProvisioningStatus": NotRequired[DeviceStatusType],
        "Tags": NotRequired[Dict[str, str]],
        "Type": NotRequired[DeviceTypeType],
    },
)

class DescribeNodeFromTemplateJobResponseTypeDef(TypedDict):
    CreatedTime: datetime
    JobId: str
    JobTags: List[JobResourceTagsOutputTypeDef]
    LastUpdatedTime: datetime
    NodeDescription: str
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    Status: NodeFromTemplateJobStatusType
    StatusMessage: str
    TemplateParameters: Dict[str, str]
    TemplateType: Literal["RTSP_CAMERA_STREAM"]
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceJobConfigTypeDef(TypedDict):
    OTAJobConfig: NotRequired[OTAJobConfigTypeDef]

class ListDevicesJobsResponseTypeDef(TypedDict):
    DeviceJobs: List[DeviceJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EthernetPayloadOutputTypeDef(TypedDict):
    ConnectionType: ConnectionTypeType
    StaticIpConnectionInfo: NotRequired[StaticIpConnectionInfoOutputTypeDef]

class EthernetPayloadTypeDef(TypedDict):
    ConnectionType: ConnectionTypeType
    StaticIpConnectionInfo: NotRequired[StaticIpConnectionInfoTypeDef]

JobResourceTagsUnionTypeDef = Union[JobResourceTagsTypeDef, JobResourceTagsOutputTypeDef]

class ListApplicationInstanceDependenciesResponseTypeDef(TypedDict):
    PackageObjects: List[PackageObjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListApplicationInstanceNodeInstancesResponseTypeDef(TypedDict):
    NodeInstances: List[NodeInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListNodeFromTemplateJobsResponseTypeDef(TypedDict):
    NodeFromTemplateJobs: List[NodeFromTemplateJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListNodesResponseTypeDef(TypedDict):
    Nodes: List[NodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPackageImportJobsResponseTypeDef(TypedDict):
    PackageImportJobs: List[PackageImportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPackagesResponseTypeDef(TypedDict):
    Packages: List[PackageListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class NetworkStatusTypeDef(TypedDict):
    Ethernet0Status: NotRequired[EthernetStatusTypeDef]
    Ethernet1Status: NotRequired[EthernetStatusTypeDef]
    LastUpdatedTime: NotRequired[datetime]
    NtpStatus: NotRequired[NtpStatusTypeDef]

class NodeInterfaceTypeDef(TypedDict):
    Inputs: List[NodeInputPortTypeDef]
    Outputs: List[NodeOutputPortTypeDef]

class SignalApplicationInstanceNodeInstancesRequestTypeDef(TypedDict):
    ApplicationInstanceId: str
    NodeSignals: Sequence[NodeSignalTypeDef]

class PackageImportJobOutputTypeDef(TypedDict):
    OutputS3Location: OutPutS3LocationTypeDef
    PackageId: str
    PackageVersion: str
    PatchVersion: str

class PackageImportJobOutputConfigTypeDef(TypedDict):
    PackageVersionOutputConfig: NotRequired[PackageVersionOutputConfigTypeDef]

class PackageVersionInputConfigTypeDef(TypedDict):
    S3Location: S3LocationTypeDef

class ListApplicationInstancesResponseTypeDef(TypedDict):
    ApplicationInstances: List[ApplicationInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDevicesResponseTypeDef(TypedDict):
    Devices: List[DeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateJobForDevicesRequestTypeDef(TypedDict):
    DeviceIds: Sequence[str]
    JobType: JobTypeType
    DeviceJobConfig: NotRequired[DeviceJobConfigTypeDef]

class NetworkPayloadOutputTypeDef(TypedDict):
    Ethernet0: NotRequired[EthernetPayloadOutputTypeDef]
    Ethernet1: NotRequired[EthernetPayloadOutputTypeDef]
    Ntp: NotRequired[NtpPayloadOutputTypeDef]

class NetworkPayloadTypeDef(TypedDict):
    Ethernet0: NotRequired[EthernetPayloadTypeDef]
    Ethernet1: NotRequired[EthernetPayloadTypeDef]
    Ntp: NotRequired[NtpPayloadTypeDef]

class CreateNodeFromTemplateJobRequestTypeDef(TypedDict):
    NodeName: str
    OutputPackageName: str
    OutputPackageVersion: str
    TemplateParameters: Mapping[str, str]
    TemplateType: Literal["RTSP_CAMERA_STREAM"]
    JobTags: NotRequired[Sequence[JobResourceTagsUnionTypeDef]]
    NodeDescription: NotRequired[str]

class DescribeNodeResponseTypeDef(TypedDict):
    AssetName: str
    Category: NodeCategoryType
    CreatedTime: datetime
    Description: str
    LastUpdatedTime: datetime
    Name: str
    NodeId: str
    NodeInterface: NodeInterfaceTypeDef
    OwnerAccount: str
    PackageArn: str
    PackageId: str
    PackageName: str
    PackageVersion: str
    PatchVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class PackageImportJobInputConfigTypeDef(TypedDict):
    PackageVersionInputConfig: NotRequired[PackageVersionInputConfigTypeDef]

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "AlternateSoftwares": List[AlternateSoftwareMetadataTypeDef],
        "Arn": str,
        "Brand": DeviceBrandType,
        "CreatedTime": datetime,
        "CurrentNetworkingStatus": NetworkStatusTypeDef,
        "CurrentSoftware": str,
        "Description": str,
        "DeviceAggregatedStatus": DeviceAggregatedStatusType,
        "DeviceConnectionStatus": DeviceConnectionStatusType,
        "DeviceId": str,
        "LatestAlternateSoftware": str,
        "LatestDeviceJob": LatestDeviceJobTypeDef,
        "LatestSoftware": str,
        "LeaseExpirationTime": datetime,
        "Name": str,
        "NetworkingConfiguration": NetworkPayloadOutputTypeDef,
        "ProvisioningStatus": DeviceStatusType,
        "SerialNumber": str,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkPayloadUnionTypeDef = Union[NetworkPayloadTypeDef, NetworkPayloadOutputTypeDef]

class CreatePackageImportJobRequestTypeDef(TypedDict):
    ClientToken: str
    InputConfig: PackageImportJobInputConfigTypeDef
    JobType: PackageImportJobTypeType
    OutputConfig: PackageImportJobOutputConfigTypeDef
    JobTags: NotRequired[Sequence[JobResourceTagsUnionTypeDef]]

class DescribePackageImportJobResponseTypeDef(TypedDict):
    ClientToken: str
    CreatedTime: datetime
    InputConfig: PackageImportJobInputConfigTypeDef
    JobId: str
    JobTags: List[JobResourceTagsOutputTypeDef]
    JobType: PackageImportJobTypeType
    LastUpdatedTime: datetime
    Output: PackageImportJobOutputTypeDef
    OutputConfig: PackageImportJobOutputConfigTypeDef
    Status: PackageImportJobStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionDeviceRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    NetworkingConfiguration: NotRequired[NetworkPayloadUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]
