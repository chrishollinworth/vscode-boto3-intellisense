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

from .literals import HypervisorStateType

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
    "GetGatewayInputRequestTypeDef",
    "GetGatewayOutputTypeDef",
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
    "PaginatorConfigTypeDef",
    "PutMaintenanceStartTimeInputRequestTypeDef",
    "PutMaintenanceStartTimeOutputTypeDef",
    "ResponseMetadataTypeDef",
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
    "VirtualMachineTypeDef",
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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
