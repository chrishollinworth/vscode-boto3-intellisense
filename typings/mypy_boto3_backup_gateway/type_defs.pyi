"""
Type annotations for backup-gateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_backup_gateway.type_defs import AssociateGatewayToServerInputRequestTypeDef

    data: AssociateGatewayToServerInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import HypervisorStateType, SyncMetadataStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateGatewayToServerInputRequestTypeDef",
    "AssociateGatewayToServerOutputTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "CreateGatewayInputRequestTypeDef",
    "CreateGatewayOutputTypeDef",
    "DeleteGatewayInputRequestTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteHypervisorInputRequestTypeDef",
    "DeleteHypervisorOutputTypeDef",
    "DisassociateGatewayFromServerInputRequestTypeDef",
    "DisassociateGatewayFromServerOutputTypeDef",
    "GatewayDetailsTypeDef",
    "GatewayTypeDef",
    "GetBandwidthRateLimitScheduleInputRequestTypeDef",
    "GetBandwidthRateLimitScheduleOutputTypeDef",
    "GetGatewayInputRequestTypeDef",
    "GetGatewayOutputTypeDef",
    "GetHypervisorInputRequestTypeDef",
    "GetHypervisorOutputTypeDef",
    "GetHypervisorPropertyMappingsInputRequestTypeDef",
    "GetHypervisorPropertyMappingsOutputTypeDef",
    "GetVirtualMachineInputRequestTypeDef",
    "GetVirtualMachineOutputTypeDef",
    "HypervisorDetailsTypeDef",
    "HypervisorTypeDef",
    "ImportHypervisorConfigurationInputRequestTypeDef",
    "ImportHypervisorConfigurationOutputTypeDef",
    "ListGatewaysInputRequestTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListHypervisorsInputRequestTypeDef",
    "ListHypervisorsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualMachinesInputRequestTypeDef",
    "ListVirtualMachinesOutputTypeDef",
    "MaintenanceStartTimeTypeDef",
    "PaginatorConfigTypeDef",
    "PutBandwidthRateLimitScheduleInputRequestTypeDef",
    "PutBandwidthRateLimitScheduleOutputTypeDef",
    "PutHypervisorPropertyMappingsInputRequestTypeDef",
    "PutHypervisorPropertyMappingsOutputTypeDef",
    "PutMaintenanceStartTimeInputRequestTypeDef",
    "PutMaintenanceStartTimeOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartVirtualMachinesMetadataSyncInputRequestTypeDef",
    "StartVirtualMachinesMetadataSyncOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagResourceOutputTypeDef",
    "TagTypeDef",
    "TestHypervisorConfigurationInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagResourceOutputTypeDef",
    "UpdateGatewayInformationInputRequestTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateHypervisorInputRequestTypeDef",
    "UpdateHypervisorOutputTypeDef",
    "VirtualMachineDetailsTypeDef",
    "VirtualMachineTypeDef",
    "VmwareTagTypeDef",
    "VmwareToAwsTagMappingTypeDef",
)

AssociateGatewayToServerInputRequestTypeDef = TypedDict(
    "AssociateGatewayToServerInputRequestTypeDef",
    {
        "GatewayArn": str,
        "ServerArn": str,
    },
)

AssociateGatewayToServerOutputTypeDef = TypedDict(
    "AssociateGatewayToServerOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_RequiredBandwidthRateLimitIntervalTypeDef",
    {
        "DaysOfWeek": List[int],
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
    },
)
_OptionalBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_OptionalBandwidthRateLimitIntervalTypeDef",
    {
        "AverageUploadRateLimitInBitsPerSec": int,
    },
    total=False,
)

class BandwidthRateLimitIntervalTypeDef(
    _RequiredBandwidthRateLimitIntervalTypeDef, _OptionalBandwidthRateLimitIntervalTypeDef
):
    pass

_RequiredCreateGatewayInputRequestTypeDef = TypedDict(
    "_RequiredCreateGatewayInputRequestTypeDef",
    {
        "ActivationKey": str,
        "GatewayDisplayName": str,
        "GatewayType": Literal["BACKUP_VM"],
    },
)
_OptionalCreateGatewayInputRequestTypeDef = TypedDict(
    "_OptionalCreateGatewayInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateGatewayInputRequestTypeDef(
    _RequiredCreateGatewayInputRequestTypeDef, _OptionalCreateGatewayInputRequestTypeDef
):
    pass

CreateGatewayOutputTypeDef = TypedDict(
    "CreateGatewayOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayInputRequestTypeDef = TypedDict(
    "DeleteGatewayInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHypervisorInputRequestTypeDef = TypedDict(
    "DeleteHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)

DeleteHypervisorOutputTypeDef = TypedDict(
    "DeleteHypervisorOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateGatewayFromServerInputRequestTypeDef = TypedDict(
    "DisassociateGatewayFromServerInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

DisassociateGatewayFromServerOutputTypeDef = TypedDict(
    "DisassociateGatewayFromServerOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GatewayDetailsTypeDef = TypedDict(
    "GatewayDetailsTypeDef",
    {
        "GatewayArn": str,
        "GatewayDisplayName": str,
        "GatewayType": Literal["BACKUP_VM"],
        "HypervisorId": str,
        "LastSeenTime": datetime,
        "MaintenanceStartTime": "MaintenanceStartTimeTypeDef",
        "NextUpdateAvailabilityTime": datetime,
        "VpcEndpoint": str,
    },
    total=False,
)

GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {
        "GatewayArn": str,
        "GatewayDisplayName": str,
        "GatewayType": Literal["BACKUP_VM"],
        "HypervisorId": str,
        "LastSeenTime": datetime,
    },
    total=False,
)

GetBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "GetBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

GetBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "GetBandwidthRateLimitScheduleOutputTypeDef",
    {
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGatewayInputRequestTypeDef = TypedDict(
    "GetGatewayInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

GetGatewayOutputTypeDef = TypedDict(
    "GetGatewayOutputTypeDef",
    {
        "Gateway": "GatewayDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHypervisorInputRequestTypeDef = TypedDict(
    "GetHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)

GetHypervisorOutputTypeDef = TypedDict(
    "GetHypervisorOutputTypeDef",
    {
        "Hypervisor": "HypervisorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHypervisorPropertyMappingsInputRequestTypeDef = TypedDict(
    "GetHypervisorPropertyMappingsInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)

GetHypervisorPropertyMappingsOutputTypeDef = TypedDict(
    "GetHypervisorPropertyMappingsOutputTypeDef",
    {
        "HypervisorArn": str,
        "IamRoleArn": str,
        "VmwareToAwsTagMappings": List["VmwareToAwsTagMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVirtualMachineInputRequestTypeDef = TypedDict(
    "GetVirtualMachineInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetVirtualMachineOutputTypeDef = TypedDict(
    "GetVirtualMachineOutputTypeDef",
    {
        "VirtualMachine": "VirtualMachineDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HypervisorDetailsTypeDef = TypedDict(
    "HypervisorDetailsTypeDef",
    {
        "Host": str,
        "HypervisorArn": str,
        "KmsKeyArn": str,
        "LastSuccessfulMetadataSyncTime": datetime,
        "LatestMetadataSyncStatus": SyncMetadataStatusType,
        "LatestMetadataSyncStatusMessage": str,
        "LogGroupArn": str,
        "Name": str,
        "State": HypervisorStateType,
    },
    total=False,
)

HypervisorTypeDef = TypedDict(
    "HypervisorTypeDef",
    {
        "Host": str,
        "HypervisorArn": str,
        "KmsKeyArn": str,
        "Name": str,
        "State": HypervisorStateType,
    },
    total=False,
)

_RequiredImportHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredImportHypervisorConfigurationInputRequestTypeDef",
    {
        "Host": str,
        "Name": str,
    },
)
_OptionalImportHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalImportHypervisorConfigurationInputRequestTypeDef",
    {
        "KmsKeyArn": str,
        "Password": str,
        "Tags": List["TagTypeDef"],
        "Username": str,
    },
    total=False,
)

class ImportHypervisorConfigurationInputRequestTypeDef(
    _RequiredImportHypervisorConfigurationInputRequestTypeDef,
    _OptionalImportHypervisorConfigurationInputRequestTypeDef,
):
    pass

ImportHypervisorConfigurationOutputTypeDef = TypedDict(
    "ImportHypervisorConfigurationOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysInputRequestTypeDef = TypedDict(
    "ListGatewaysInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List["GatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHypervisorsInputRequestTypeDef = TypedDict(
    "ListHypervisorsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHypervisorsOutputTypeDef = TypedDict(
    "ListHypervisorsOutputTypeDef",
    {
        "Hypervisors": List["HypervisorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualMachinesInputRequestTypeDef = TypedDict(
    "ListVirtualMachinesInputRequestTypeDef",
    {
        "HypervisorArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVirtualMachinesOutputTypeDef = TypedDict(
    "ListVirtualMachinesOutputTypeDef",
    {
        "NextToken": str,
        "VirtualMachines": List["VirtualMachineTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMaintenanceStartTimeTypeDef = TypedDict(
    "_RequiredMaintenanceStartTimeTypeDef",
    {
        "HourOfDay": int,
        "MinuteOfHour": int,
    },
)
_OptionalMaintenanceStartTimeTypeDef = TypedDict(
    "_OptionalMaintenanceStartTimeTypeDef",
    {
        "DayOfMonth": int,
        "DayOfWeek": int,
    },
    total=False,
)

class MaintenanceStartTimeTypeDef(
    _RequiredMaintenanceStartTimeTypeDef, _OptionalMaintenanceStartTimeTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PutBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "PutBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "GatewayArn": str,
    },
)

PutBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "PutBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutHypervisorPropertyMappingsInputRequestTypeDef = TypedDict(
    "PutHypervisorPropertyMappingsInputRequestTypeDef",
    {
        "HypervisorArn": str,
        "IamRoleArn": str,
        "VmwareToAwsTagMappings": List["VmwareToAwsTagMappingTypeDef"],
    },
)

PutHypervisorPropertyMappingsOutputTypeDef = TypedDict(
    "PutHypervisorPropertyMappingsOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "_RequiredPutMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayArn": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
    },
)
_OptionalPutMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "_OptionalPutMaintenanceStartTimeInputRequestTypeDef",
    {
        "DayOfMonth": int,
        "DayOfWeek": int,
    },
    total=False,
)

class PutMaintenanceStartTimeInputRequestTypeDef(
    _RequiredPutMaintenanceStartTimeInputRequestTypeDef,
    _OptionalPutMaintenanceStartTimeInputRequestTypeDef,
):
    pass

PutMaintenanceStartTimeOutputTypeDef = TypedDict(
    "PutMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

StartVirtualMachinesMetadataSyncInputRequestTypeDef = TypedDict(
    "StartVirtualMachinesMetadataSyncInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)

StartVirtualMachinesMetadataSyncOutputTypeDef = TypedDict(
    "StartVirtualMachinesMetadataSyncOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagResourceOutputTypeDef = TypedDict(
    "TagResourceOutputTypeDef",
    {
        "ResourceARN": str,
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

_RequiredTestHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredTestHypervisorConfigurationInputRequestTypeDef",
    {
        "GatewayArn": str,
        "Host": str,
    },
)
_OptionalTestHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalTestHypervisorConfigurationInputRequestTypeDef",
    {
        "Password": str,
        "Username": str,
    },
    total=False,
)

class TestHypervisorConfigurationInputRequestTypeDef(
    _RequiredTestHypervisorConfigurationInputRequestTypeDef,
    _OptionalTestHypervisorConfigurationInputRequestTypeDef,
):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UntagResourceOutputTypeDef = TypedDict(
    "UntagResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
_OptionalUpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayDisplayName": str,
    },
    total=False,
)

class UpdateGatewayInformationInputRequestTypeDef(
    _RequiredUpdateGatewayInformationInputRequestTypeDef,
    _OptionalUpdateGatewayInformationInputRequestTypeDef,
):
    pass

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewaySoftwareNowInputRequestTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateHypervisorInputRequestTypeDef = TypedDict(
    "_RequiredUpdateHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)
_OptionalUpdateHypervisorInputRequestTypeDef = TypedDict(
    "_OptionalUpdateHypervisorInputRequestTypeDef",
    {
        "Host": str,
        "LogGroupArn": str,
        "Name": str,
        "Password": str,
        "Username": str,
    },
    total=False,
)

class UpdateHypervisorInputRequestTypeDef(
    _RequiredUpdateHypervisorInputRequestTypeDef, _OptionalUpdateHypervisorInputRequestTypeDef
):
    pass

UpdateHypervisorOutputTypeDef = TypedDict(
    "UpdateHypervisorOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualMachineDetailsTypeDef = TypedDict(
    "VirtualMachineDetailsTypeDef",
    {
        "HostName": str,
        "HypervisorId": str,
        "LastBackupDate": datetime,
        "Name": str,
        "Path": str,
        "ResourceArn": str,
        "VmwareTags": List["VmwareTagTypeDef"],
    },
    total=False,
)

VirtualMachineTypeDef = TypedDict(
    "VirtualMachineTypeDef",
    {
        "HostName": str,
        "HypervisorId": str,
        "LastBackupDate": datetime,
        "Name": str,
        "Path": str,
        "ResourceArn": str,
    },
    total=False,
)

VmwareTagTypeDef = TypedDict(
    "VmwareTagTypeDef",
    {
        "VmwareCategory": str,
        "VmwareTagDescription": str,
        "VmwareTagName": str,
    },
    total=False,
)

VmwareToAwsTagMappingTypeDef = TypedDict(
    "VmwareToAwsTagMappingTypeDef",
    {
        "AwsTagKey": str,
        "AwsTagValue": str,
        "VmwareCategory": str,
        "VmwareTagName": str,
    },
)
