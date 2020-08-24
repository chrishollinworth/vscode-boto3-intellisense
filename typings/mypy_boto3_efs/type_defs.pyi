"""
Main interface for efs service type definitions.

Usage::

    ```python
    from mypy_boto3_efs.type_defs import AccessPointDescriptionTypeDef

    data: AccessPointDescriptionTypeDef = {...}
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
    "AccessPointDescriptionTypeDef",
    "BackupPolicyTypeDef",
    "CreationInfoTypeDef",
    "FileSystemDescriptionTypeDef",
    "FileSystemSizeTypeDef",
    "LifecyclePolicyTypeDef",
    "MountTargetDescriptionTypeDef",
    "PosixUserTypeDef",
    "RootDirectoryTypeDef",
    "TagTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "DescribeAccessPointsResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
)

AccessPointDescriptionTypeDef = TypedDict(
    "AccessPointDescriptionTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List["TagTypeDef"],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": "PosixUserTypeDef",
        "RootDirectory": "RootDirectoryTypeDef",
        "OwnerId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
    },
    total=False,
)

BackupPolicyTypeDef = TypedDict(
    "BackupPolicyTypeDef", {"Status": Literal["ENABLED", "ENABLING", "DISABLED", "DISABLING"]}
)

CreationInfoTypeDef = TypedDict(
    "CreationInfoTypeDef", {"OwnerUid": int, "OwnerGid": int, "Permissions": str}
)

_RequiredFileSystemDescriptionTypeDef = TypedDict(
    "_RequiredFileSystemDescriptionTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "NumberOfMountTargets": int,
        "SizeInBytes": "FileSystemSizeTypeDef",
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Tags": List["TagTypeDef"],
    },
)
_OptionalFileSystemDescriptionTypeDef = TypedDict(
    "_OptionalFileSystemDescriptionTypeDef",
    {
        "FileSystemArn": str,
        "Name": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
    },
    total=False,
)


class FileSystemDescriptionTypeDef(
    _RequiredFileSystemDescriptionTypeDef, _OptionalFileSystemDescriptionTypeDef
):
    pass


_RequiredFileSystemSizeTypeDef = TypedDict("_RequiredFileSystemSizeTypeDef", {"Value": int})
_OptionalFileSystemSizeTypeDef = TypedDict(
    "_OptionalFileSystemSizeTypeDef",
    {"Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class FileSystemSizeTypeDef(_RequiredFileSystemSizeTypeDef, _OptionalFileSystemSizeTypeDef):
    pass


LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

_RequiredMountTargetDescriptionTypeDef = TypedDict(
    "_RequiredMountTargetDescriptionTypeDef",
    {
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
    },
)
_OptionalMountTargetDescriptionTypeDef = TypedDict(
    "_OptionalMountTargetDescriptionTypeDef",
    {
        "OwnerId": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
    },
    total=False,
)


class MountTargetDescriptionTypeDef(
    _RequiredMountTargetDescriptionTypeDef, _OptionalMountTargetDescriptionTypeDef
):
    pass


_RequiredPosixUserTypeDef = TypedDict("_RequiredPosixUserTypeDef", {"Uid": int, "Gid": int})
_OptionalPosixUserTypeDef = TypedDict(
    "_OptionalPosixUserTypeDef", {"SecondaryGids": List[int]}, total=False
)


class PosixUserTypeDef(_RequiredPosixUserTypeDef, _OptionalPosixUserTypeDef):
    pass


RootDirectoryTypeDef = TypedDict(
    "RootDirectoryTypeDef", {"Path": str, "CreationInfo": "CreationInfoTypeDef"}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

BackupPolicyDescriptionTypeDef = TypedDict(
    "BackupPolicyDescriptionTypeDef", {"BackupPolicy": "BackupPolicyTypeDef"}, total=False
)

DescribeAccessPointsResponseTypeDef = TypedDict(
    "DescribeAccessPointsResponseTypeDef",
    {"AccessPoints": List["AccessPointDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {"Marker": str, "FileSystems": List["FileSystemDescriptionTypeDef"], "NextMarker": str},
    total=False,
)

DescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsResponseTypeDef", {"SecurityGroups": List[str]}
)

DescribeMountTargetsResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseTypeDef",
    {"Marker": str, "MountTargets": List["MountTargetDescriptionTypeDef"], "NextMarker": str},
    total=False,
)

_RequiredDescribeTagsResponseTypeDef = TypedDict(
    "_RequiredDescribeTagsResponseTypeDef", {"Tags": List["TagTypeDef"]}
)
_OptionalDescribeTagsResponseTypeDef = TypedDict(
    "_OptionalDescribeTagsResponseTypeDef", {"Marker": str, "NextMarker": str}, total=False
)


class DescribeTagsResponseTypeDef(
    _RequiredDescribeTagsResponseTypeDef, _OptionalDescribeTagsResponseTypeDef
):
    pass


FileSystemPolicyDescriptionTypeDef = TypedDict(
    "FileSystemPolicyDescriptionTypeDef", {"FileSystemId": str, "Policy": str}, total=False
)

LifecycleConfigurationDescriptionTypeDef = TypedDict(
    "LifecycleConfigurationDescriptionTypeDef",
    {"LifecyclePolicies": List["LifecyclePolicyTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
