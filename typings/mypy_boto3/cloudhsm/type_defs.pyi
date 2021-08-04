"""
Type annotations for cloudhsm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import AddTagsToResourceRequestRequestTypeDef

    data: AddTagsToResourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ClientVersionType, CloudHsmObjectStateType, HsmStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddTagsToResourceRequestRequestTypeDef",
    "AddTagsToResourceResponseTypeDef",
    "CreateHapgRequestRequestTypeDef",
    "CreateHapgResponseTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "CreateHsmResponseTypeDef",
    "CreateLunaClientRequestRequestTypeDef",
    "CreateLunaClientResponseTypeDef",
    "DeleteHapgRequestRequestTypeDef",
    "DeleteHapgResponseTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteLunaClientRequestRequestTypeDef",
    "DeleteLunaClientResponseTypeDef",
    "DescribeHapgRequestRequestTypeDef",
    "DescribeHapgResponseTypeDef",
    "DescribeHsmRequestRequestTypeDef",
    "DescribeHsmResponseTypeDef",
    "DescribeLunaClientRequestRequestTypeDef",
    "DescribeLunaClientResponseTypeDef",
    "GetConfigRequestRequestTypeDef",
    "GetConfigResponseTypeDef",
    "ListAvailableZonesResponseTypeDef",
    "ListHapgsRequestRequestTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsRequestRequestTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsRequestRequestTypeDef",
    "ListLunaClientsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyHapgRequestRequestTypeDef",
    "ModifyHapgResponseTypeDef",
    "ModifyHsmRequestRequestTypeDef",
    "ModifyHsmResponseTypeDef",
    "ModifyLunaClientRequestRequestTypeDef",
    "ModifyLunaClientResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "RemoveTagsFromResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": List["TagTypeDef"],
    },
)

AddTagsToResourceResponseTypeDef = TypedDict(
    "AddTagsToResourceResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHapgRequestRequestTypeDef = TypedDict(
    "CreateHapgRequestRequestTypeDef",
    {
        "Label": str,
    },
)

CreateHapgResponseTypeDef = TypedDict(
    "CreateHapgResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHsmRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHsmRequestRequestTypeDef",
    {
        "SubnetId": str,
        "SshKey": str,
        "IamRoleArn": str,
        "SubscriptionType": Literal["PRODUCTION"],
    },
)
_OptionalCreateHsmRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHsmRequestRequestTypeDef",
    {
        "EniIp": str,
        "ExternalId": str,
        "ClientToken": str,
        "SyslogIp": str,
    },
    total=False,
)

class CreateHsmRequestRequestTypeDef(
    _RequiredCreateHsmRequestRequestTypeDef, _OptionalCreateHsmRequestRequestTypeDef
):
    pass

CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLunaClientRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLunaClientRequestRequestTypeDef",
    {
        "Certificate": str,
    },
)
_OptionalCreateLunaClientRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLunaClientRequestRequestTypeDef",
    {
        "Label": str,
    },
    total=False,
)

class CreateLunaClientRequestRequestTypeDef(
    _RequiredCreateLunaClientRequestRequestTypeDef, _OptionalCreateLunaClientRequestRequestTypeDef
):
    pass

CreateLunaClientResponseTypeDef = TypedDict(
    "CreateLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHapgRequestRequestTypeDef = TypedDict(
    "DeleteHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)

DeleteHapgResponseTypeDef = TypedDict(
    "DeleteHapgResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHsmRequestRequestTypeDef = TypedDict(
    "DeleteHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
    },
)

DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLunaClientRequestRequestTypeDef = TypedDict(
    "DeleteLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
    },
)

DeleteLunaClientResponseTypeDef = TypedDict(
    "DeleteLunaClientResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHapgRequestRequestTypeDef = TypedDict(
    "DescribeHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)

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
        "State": CloudHsmObjectStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHsmRequestRequestTypeDef = TypedDict(
    "DescribeHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
        "HsmSerialNumber": str,
    },
    total=False,
)

DescribeHsmResponseTypeDef = TypedDict(
    "DescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": HsmStatusType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLunaClientRequestRequestTypeDef = TypedDict(
    "DescribeLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
        "CertificateFingerprint": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigRequestRequestTypeDef = TypedDict(
    "GetConfigRequestRequestTypeDef",
    {
        "ClientArn": str,
        "ClientVersion": ClientVersionType,
        "HapgList": List[str],
    },
)

GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {
        "ConfigType": str,
        "ConfigFile": str,
        "ConfigCred": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableZonesResponseTypeDef = TypedDict(
    "ListAvailableZonesResponseTypeDef",
    {
        "AZList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHapgsRequestRequestTypeDef = TypedDict(
    "ListHapgsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListHapgsResponseTypeDef = TypedDict(
    "ListHapgsResponseTypeDef",
    {
        "HapgList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHsmsRequestRequestTypeDef = TypedDict(
    "ListHsmsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListHsmsResponseTypeDef = TypedDict(
    "ListHsmsResponseTypeDef",
    {
        "HsmList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLunaClientsRequestRequestTypeDef = TypedDict(
    "ListLunaClientsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListLunaClientsResponseTypeDef = TypedDict(
    "ListLunaClientsResponseTypeDef",
    {
        "ClientList": List[str],
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
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyHapgRequestRequestTypeDef = TypedDict(
    "_RequiredModifyHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)
_OptionalModifyHapgRequestRequestTypeDef = TypedDict(
    "_OptionalModifyHapgRequestRequestTypeDef",
    {
        "Label": str,
        "PartitionSerialList": List[str],
    },
    total=False,
)

class ModifyHapgRequestRequestTypeDef(
    _RequiredModifyHapgRequestRequestTypeDef, _OptionalModifyHapgRequestRequestTypeDef
):
    pass

ModifyHapgResponseTypeDef = TypedDict(
    "ModifyHapgResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyHsmRequestRequestTypeDef = TypedDict(
    "_RequiredModifyHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
    },
)
_OptionalModifyHsmRequestRequestTypeDef = TypedDict(
    "_OptionalModifyHsmRequestRequestTypeDef",
    {
        "SubnetId": str,
        "EniIp": str,
        "IamRoleArn": str,
        "ExternalId": str,
        "SyslogIp": str,
    },
    total=False,
)

class ModifyHsmRequestRequestTypeDef(
    _RequiredModifyHsmRequestRequestTypeDef, _OptionalModifyHsmRequestRequestTypeDef
):
    pass

ModifyHsmResponseTypeDef = TypedDict(
    "ModifyHsmResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLunaClientRequestRequestTypeDef = TypedDict(
    "ModifyLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
    },
)

ModifyLunaClientResponseTypeDef = TypedDict(
    "ModifyLunaClientResponseTypeDef",
    {
        "ClientArn": str,
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

RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": List[str],
    },
)

RemoveTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveTagsFromResourceResponseTypeDef",
    {
        "Status": str,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
