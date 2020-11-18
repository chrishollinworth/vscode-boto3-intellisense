"""
Main interface for cloudhsm service type definitions.

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import TagTypeDef

    data: TagTypeDef = {...}
    ```
"""
import sys
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
    "TagTypeDef",
    "AddTagsToResourceResponseTypeDef",
    "CreateHapgResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "CreateLunaClientResponseTypeDef",
    "DeleteHapgResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteLunaClientResponseTypeDef",
    "DescribeHapgResponseTypeDef",
    "DescribeHsmResponseTypeDef",
    "DescribeLunaClientResponseTypeDef",
    "GetConfigResponseTypeDef",
    "ListAvailableZonesResponseTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyHapgResponseTypeDef",
    "ModifyHsmResponseTypeDef",
    "ModifyLunaClientResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveTagsFromResourceResponseTypeDef",
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

AddTagsToResourceResponseTypeDef = TypedDict("AddTagsToResourceResponseTypeDef", {"Status": str})

CreateHapgResponseTypeDef = TypedDict("CreateHapgResponseTypeDef", {"HapgArn": str}, total=False)

CreateHsmResponseTypeDef = TypedDict("CreateHsmResponseTypeDef", {"HsmArn": str}, total=False)

CreateLunaClientResponseTypeDef = TypedDict(
    "CreateLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)

DeleteHapgResponseTypeDef = TypedDict("DeleteHapgResponseTypeDef", {"Status": str})

DeleteHsmResponseTypeDef = TypedDict("DeleteHsmResponseTypeDef", {"Status": str})

DeleteLunaClientResponseTypeDef = TypedDict("DeleteLunaClientResponseTypeDef", {"Status": str})

DescribeHapgResponseTypeDef = TypedDict(
    "DescribeHapgResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": Literal["READY", "UPDATING", "DEGRADED"],
    },
    total=False,
)

DescribeHsmResponseTypeDef = TypedDict(
    "DescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": Literal[
            "PENDING", "RUNNING", "UPDATING", "SUSPENDED", "TERMINATING", "TERMINATED", "DEGRADED"
        ],
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": Literal["PRODUCTION"],
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
    },
    total=False,
)

DescribeLunaClientResponseTypeDef = TypedDict(
    "DescribeLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
    },
    total=False,
)

GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {"ConfigType": str, "ConfigFile": str, "ConfigCred": str},
    total=False,
)

ListAvailableZonesResponseTypeDef = TypedDict(
    "ListAvailableZonesResponseTypeDef", {"AZList": List[str]}, total=False
)

_RequiredListHapgsResponseTypeDef = TypedDict(
    "_RequiredListHapgsResponseTypeDef", {"HapgList": List[str]}
)
_OptionalListHapgsResponseTypeDef = TypedDict(
    "_OptionalListHapgsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHapgsResponseTypeDef(
    _RequiredListHapgsResponseTypeDef, _OptionalListHapgsResponseTypeDef
):
    pass


ListHsmsResponseTypeDef = TypedDict(
    "ListHsmsResponseTypeDef", {"HsmList": List[str], "NextToken": str}, total=False
)

_RequiredListLunaClientsResponseTypeDef = TypedDict(
    "_RequiredListLunaClientsResponseTypeDef", {"ClientList": List[str]}
)
_OptionalListLunaClientsResponseTypeDef = TypedDict(
    "_OptionalListLunaClientsResponseTypeDef", {"NextToken": str}, total=False
)


class ListLunaClientsResponseTypeDef(
    _RequiredListLunaClientsResponseTypeDef, _OptionalListLunaClientsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"TagList": List["TagTypeDef"]}
)

ModifyHapgResponseTypeDef = TypedDict("ModifyHapgResponseTypeDef", {"HapgArn": str}, total=False)

ModifyHsmResponseTypeDef = TypedDict("ModifyHsmResponseTypeDef", {"HsmArn": str}, total=False)

ModifyLunaClientResponseTypeDef = TypedDict(
    "ModifyLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RemoveTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveTagsFromResourceResponseTypeDef", {"Status": str}
)
