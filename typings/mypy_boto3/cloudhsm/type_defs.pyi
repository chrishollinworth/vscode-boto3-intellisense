"""
Type annotations for cloudhsm service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import ClientVersionType, CloudHsmObjectStateType, HsmStatusType

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
    "AddTagsToResourceRequestTypeDef",
    "AddTagsToResourceResponseTypeDef",
    "CreateHapgRequestTypeDef",
    "CreateHapgResponseTypeDef",
    "CreateHsmRequestTypeDef",
    "CreateHsmResponseTypeDef",
    "CreateLunaClientRequestTypeDef",
    "CreateLunaClientResponseTypeDef",
    "DeleteHapgRequestTypeDef",
    "DeleteHapgResponseTypeDef",
    "DeleteHsmRequestTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteLunaClientRequestTypeDef",
    "DeleteLunaClientResponseTypeDef",
    "DescribeHapgRequestTypeDef",
    "DescribeHapgResponseTypeDef",
    "DescribeHsmRequestTypeDef",
    "DescribeHsmResponseTypeDef",
    "DescribeLunaClientRequestTypeDef",
    "DescribeLunaClientResponseTypeDef",
    "GetConfigRequestTypeDef",
    "GetConfigResponseTypeDef",
    "ListAvailableZonesResponseTypeDef",
    "ListHapgsRequestPaginateTypeDef",
    "ListHapgsRequestTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsRequestPaginateTypeDef",
    "ListHsmsRequestTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsRequestPaginateTypeDef",
    "ListLunaClientsRequestTypeDef",
    "ListLunaClientsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyHapgRequestTypeDef",
    "ModifyHapgResponseTypeDef",
    "ModifyHsmRequestTypeDef",
    "ModifyHsmResponseTypeDef",
    "ModifyLunaClientRequestTypeDef",
    "ModifyLunaClientResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveTagsFromResourceRequestTypeDef",
    "RemoveTagsFromResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateHapgRequestTypeDef(TypedDict):
    Label: str

class CreateHsmRequestTypeDef(TypedDict):
    SubnetId: str
    SshKey: str
    IamRoleArn: str
    SubscriptionType: Literal["PRODUCTION"]
    EniIp: NotRequired[str]
    ExternalId: NotRequired[str]
    ClientToken: NotRequired[str]
    SyslogIp: NotRequired[str]

class CreateLunaClientRequestTypeDef(TypedDict):
    Certificate: str
    Label: NotRequired[str]

class DeleteHapgRequestTypeDef(TypedDict):
    HapgArn: str

class DeleteHsmRequestTypeDef(TypedDict):
    HsmArn: str

class DeleteLunaClientRequestTypeDef(TypedDict):
    ClientArn: str

class DescribeHapgRequestTypeDef(TypedDict):
    HapgArn: str

class DescribeHsmRequestTypeDef(TypedDict):
    HsmArn: NotRequired[str]
    HsmSerialNumber: NotRequired[str]

class DescribeLunaClientRequestTypeDef(TypedDict):
    ClientArn: NotRequired[str]
    CertificateFingerprint: NotRequired[str]

class GetConfigRequestTypeDef(TypedDict):
    ClientArn: str
    ClientVersion: ClientVersionType
    HapgList: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListHapgsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ListHsmsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ListLunaClientsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ModifyHapgRequestTypeDef(TypedDict):
    HapgArn: str
    Label: NotRequired[str]
    PartitionSerialList: NotRequired[Sequence[str]]

class ModifyHsmRequestTypeDef(TypedDict):
    HsmArn: str
    SubnetId: NotRequired[str]
    EniIp: NotRequired[str]
    IamRoleArn: NotRequired[str]
    ExternalId: NotRequired[str]
    SyslogIp: NotRequired[str]

class ModifyLunaClientRequestTypeDef(TypedDict):
    ClientArn: str
    Certificate: str

class RemoveTagsFromResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeyList: Sequence[str]

class AddTagsToResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagList: Sequence[TagTypeDef]

class AddTagsToResourceResponseTypeDef(TypedDict):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHapgResponseTypeDef(TypedDict):
    HapgArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmResponseTypeDef(TypedDict):
    HsmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLunaClientResponseTypeDef(TypedDict):
    ClientArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHapgResponseTypeDef(TypedDict):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHsmResponseTypeDef(TypedDict):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLunaClientResponseTypeDef(TypedDict):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHapgResponseTypeDef(TypedDict):
    HapgArn: str
    HapgSerial: str
    HsmsLastActionFailed: List[str]
    HsmsPendingDeletion: List[str]
    HsmsPendingRegistration: List[str]
    Label: str
    LastModifiedTimestamp: str
    PartitionSerialList: List[str]
    State: CloudHsmObjectStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHsmResponseTypeDef(TypedDict):
    HsmArn: str
    Status: HsmStatusType
    StatusDetails: str
    AvailabilityZone: str
    EniId: str
    EniIp: str
    SubscriptionType: Literal["PRODUCTION"]
    SubscriptionStartDate: str
    SubscriptionEndDate: str
    VpcId: str
    SubnetId: str
    IamRoleArn: str
    SerialNumber: str
    VendorName: str
    HsmType: str
    SoftwareVersion: str
    SshPublicKey: str
    SshKeyLastUpdated: str
    ServerCertUri: str
    ServerCertLastUpdated: str
    Partitions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLunaClientResponseTypeDef(TypedDict):
    ClientArn: str
    Certificate: str
    CertificateFingerprint: str
    LastModifiedTimestamp: str
    Label: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigResponseTypeDef(TypedDict):
    ConfigType: str
    ConfigFile: str
    ConfigCred: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableZonesResponseTypeDef(TypedDict):
    AZList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHapgsResponseTypeDef(TypedDict):
    HapgList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListHsmsResponseTypeDef(TypedDict):
    HsmList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLunaClientsResponseTypeDef(TypedDict):
    ClientList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyHapgResponseTypeDef(TypedDict):
    HapgArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyHsmResponseTypeDef(TypedDict):
    HsmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLunaClientResponseTypeDef(TypedDict):
    ClientArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveTagsFromResourceResponseTypeDef(TypedDict):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHapgsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHsmsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLunaClientsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]
