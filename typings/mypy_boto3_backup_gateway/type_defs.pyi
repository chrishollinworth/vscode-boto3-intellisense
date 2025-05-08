"""
Type annotations for backup-gateway service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_backup_gateway.type_defs import AssociateGatewayToServerInputTypeDef

    data: AssociateGatewayToServerInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import HypervisorStateType, SyncMetadataStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateGatewayToServerInputTypeDef",
    "AssociateGatewayToServerOutputTypeDef",
    "BandwidthRateLimitIntervalOutputTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "BandwidthRateLimitIntervalUnionTypeDef",
    "CreateGatewayInputTypeDef",
    "CreateGatewayOutputTypeDef",
    "DeleteGatewayInputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteHypervisorInputTypeDef",
    "DeleteHypervisorOutputTypeDef",
    "DisassociateGatewayFromServerInputTypeDef",
    "DisassociateGatewayFromServerOutputTypeDef",
    "GatewayDetailsTypeDef",
    "GatewayTypeDef",
    "GetBandwidthRateLimitScheduleInputTypeDef",
    "GetBandwidthRateLimitScheduleOutputTypeDef",
    "GetGatewayInputTypeDef",
    "GetGatewayOutputTypeDef",
    "GetHypervisorInputTypeDef",
    "GetHypervisorOutputTypeDef",
    "GetHypervisorPropertyMappingsInputTypeDef",
    "GetHypervisorPropertyMappingsOutputTypeDef",
    "GetVirtualMachineInputTypeDef",
    "GetVirtualMachineOutputTypeDef",
    "HypervisorDetailsTypeDef",
    "HypervisorTypeDef",
    "ImportHypervisorConfigurationInputTypeDef",
    "ImportHypervisorConfigurationOutputTypeDef",
    "ListGatewaysInputPaginateTypeDef",
    "ListGatewaysInputTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListHypervisorsInputPaginateTypeDef",
    "ListHypervisorsInputTypeDef",
    "ListHypervisorsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualMachinesInputPaginateTypeDef",
    "ListVirtualMachinesInputTypeDef",
    "ListVirtualMachinesOutputTypeDef",
    "MaintenanceStartTimeTypeDef",
    "PaginatorConfigTypeDef",
    "PutBandwidthRateLimitScheduleInputTypeDef",
    "PutBandwidthRateLimitScheduleOutputTypeDef",
    "PutHypervisorPropertyMappingsInputTypeDef",
    "PutHypervisorPropertyMappingsOutputTypeDef",
    "PutMaintenanceStartTimeInputTypeDef",
    "PutMaintenanceStartTimeOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartVirtualMachinesMetadataSyncInputTypeDef",
    "StartVirtualMachinesMetadataSyncOutputTypeDef",
    "TagResourceInputTypeDef",
    "TagResourceOutputTypeDef",
    "TagTypeDef",
    "TestHypervisorConfigurationInputTypeDef",
    "UntagResourceInputTypeDef",
    "UntagResourceOutputTypeDef",
    "UpdateGatewayInformationInputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowInputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateHypervisorInputTypeDef",
    "UpdateHypervisorOutputTypeDef",
    "VirtualMachineDetailsTypeDef",
    "VirtualMachineTypeDef",
    "VmwareTagTypeDef",
    "VmwareToAwsTagMappingTypeDef",
)

class AssociateGatewayToServerInputTypeDef(TypedDict):
    GatewayArn: str
    ServerArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BandwidthRateLimitIntervalOutputTypeDef(TypedDict):
    DaysOfWeek: List[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: NotRequired[int]

class BandwidthRateLimitIntervalTypeDef(TypedDict):
    DaysOfWeek: Sequence[int]
    EndHourOfDay: int
    EndMinuteOfHour: int
    StartHourOfDay: int
    StartMinuteOfHour: int
    AverageUploadRateLimitInBitsPerSec: NotRequired[int]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteGatewayInputTypeDef(TypedDict):
    GatewayArn: str

class DeleteHypervisorInputTypeDef(TypedDict):
    HypervisorArn: str

class DisassociateGatewayFromServerInputTypeDef(TypedDict):
    GatewayArn: str

class MaintenanceStartTimeTypeDef(TypedDict):
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: NotRequired[int]
    DayOfWeek: NotRequired[int]

class GatewayTypeDef(TypedDict):
    GatewayArn: NotRequired[str]
    GatewayDisplayName: NotRequired[str]
    GatewayType: NotRequired[Literal["BACKUP_VM"]]
    HypervisorId: NotRequired[str]
    LastSeenTime: NotRequired[datetime]

class GetBandwidthRateLimitScheduleInputTypeDef(TypedDict):
    GatewayArn: str

class GetGatewayInputTypeDef(TypedDict):
    GatewayArn: str

class GetHypervisorInputTypeDef(TypedDict):
    HypervisorArn: str

class HypervisorDetailsTypeDef(TypedDict):
    Host: NotRequired[str]
    HypervisorArn: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    LastSuccessfulMetadataSyncTime: NotRequired[datetime]
    LatestMetadataSyncStatus: NotRequired[SyncMetadataStatusType]
    LatestMetadataSyncStatusMessage: NotRequired[str]
    LogGroupArn: NotRequired[str]
    Name: NotRequired[str]
    State: NotRequired[HypervisorStateType]

class GetHypervisorPropertyMappingsInputTypeDef(TypedDict):
    HypervisorArn: str

class VmwareToAwsTagMappingTypeDef(TypedDict):
    AwsTagKey: str
    AwsTagValue: str
    VmwareCategory: str
    VmwareTagName: str

class GetVirtualMachineInputTypeDef(TypedDict):
    ResourceArn: str

class HypervisorTypeDef(TypedDict):
    Host: NotRequired[str]
    HypervisorArn: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    Name: NotRequired[str]
    State: NotRequired[HypervisorStateType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListGatewaysInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListHypervisorsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceArn: str

class ListVirtualMachinesInputTypeDef(TypedDict):
    HypervisorArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class VirtualMachineTypeDef(TypedDict):
    HostName: NotRequired[str]
    HypervisorId: NotRequired[str]
    LastBackupDate: NotRequired[datetime]
    Name: NotRequired[str]
    Path: NotRequired[str]
    ResourceArn: NotRequired[str]

class PutMaintenanceStartTimeInputTypeDef(TypedDict):
    GatewayArn: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfMonth: NotRequired[int]
    DayOfWeek: NotRequired[int]

class StartVirtualMachinesMetadataSyncInputTypeDef(TypedDict):
    HypervisorArn: str

class TestHypervisorConfigurationInputTypeDef(TypedDict):
    GatewayArn: str
    Host: str
    Password: NotRequired[str]
    Username: NotRequired[str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateGatewayInformationInputTypeDef(TypedDict):
    GatewayArn: str
    GatewayDisplayName: NotRequired[str]

class UpdateGatewaySoftwareNowInputTypeDef(TypedDict):
    GatewayArn: str

class UpdateHypervisorInputTypeDef(TypedDict):
    HypervisorArn: str
    Host: NotRequired[str]
    LogGroupArn: NotRequired[str]
    Name: NotRequired[str]
    Password: NotRequired[str]
    Username: NotRequired[str]

class VmwareTagTypeDef(TypedDict):
    VmwareCategory: NotRequired[str]
    VmwareTagDescription: NotRequired[str]
    VmwareTagName: NotRequired[str]

class AssociateGatewayToServerOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHypervisorOutputTypeDef(TypedDict):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateGatewayFromServerOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportHypervisorConfigurationOutputTypeDef(TypedDict):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutBandwidthRateLimitScheduleOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutHypervisorPropertyMappingsOutputTypeDef(TypedDict):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutMaintenanceStartTimeOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartVirtualMachinesMetadataSyncOutputTypeDef(TypedDict):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInformationOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewaySoftwareNowOutputTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHypervisorOutputTypeDef(TypedDict):
    HypervisorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBandwidthRateLimitScheduleOutputTypeDef(TypedDict):
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutputTypeDef]
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

BandwidthRateLimitIntervalUnionTypeDef = Union[
    BandwidthRateLimitIntervalTypeDef, BandwidthRateLimitIntervalOutputTypeDef
]

class CreateGatewayInputTypeDef(TypedDict):
    ActivationKey: str
    GatewayDisplayName: str
    GatewayType: Literal["BACKUP_VM"]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ImportHypervisorConfigurationInputTypeDef(TypedDict):
    Host: str
    Name: str
    KmsKeyArn: NotRequired[str]
    Password: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    Username: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class GatewayDetailsTypeDef(TypedDict):
    GatewayArn: NotRequired[str]
    GatewayDisplayName: NotRequired[str]
    GatewayType: NotRequired[Literal["BACKUP_VM"]]
    HypervisorId: NotRequired[str]
    LastSeenTime: NotRequired[datetime]
    MaintenanceStartTime: NotRequired[MaintenanceStartTimeTypeDef]
    NextUpdateAvailabilityTime: NotRequired[datetime]
    VpcEndpoint: NotRequired[str]

class ListGatewaysOutputTypeDef(TypedDict):
    Gateways: List[GatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetHypervisorOutputTypeDef(TypedDict):
    Hypervisor: HypervisorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHypervisorPropertyMappingsOutputTypeDef(TypedDict):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: List[VmwareToAwsTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutHypervisorPropertyMappingsInputTypeDef(TypedDict):
    HypervisorArn: str
    IamRoleArn: str
    VmwareToAwsTagMappings: Sequence[VmwareToAwsTagMappingTypeDef]

class ListHypervisorsOutputTypeDef(TypedDict):
    Hypervisors: List[HypervisorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGatewaysInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHypervisorsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualMachinesInputPaginateTypeDef(TypedDict):
    HypervisorArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualMachinesOutputTypeDef(TypedDict):
    VirtualMachines: List[VirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class VirtualMachineDetailsTypeDef(TypedDict):
    HostName: NotRequired[str]
    HypervisorId: NotRequired[str]
    LastBackupDate: NotRequired[datetime]
    Name: NotRequired[str]
    Path: NotRequired[str]
    ResourceArn: NotRequired[str]
    VmwareTags: NotRequired[List[VmwareTagTypeDef]]

class PutBandwidthRateLimitScheduleInputTypeDef(TypedDict):
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalUnionTypeDef]
    GatewayArn: str

class GetGatewayOutputTypeDef(TypedDict):
    Gateway: GatewayDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVirtualMachineOutputTypeDef(TypedDict):
    VirtualMachine: VirtualMachineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
