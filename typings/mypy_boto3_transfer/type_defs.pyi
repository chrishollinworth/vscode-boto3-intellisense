"""
Type annotations for transfer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transfer.type_defs import CreateAccessRequestRequestTypeDef

    data: CreateAccessRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DomainType,
    EndpointTypeType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    ProtocolType,
    StateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateAccessRequestRequestTypeDef",
    "CreateAccessResponseTypeDef",
    "CreateServerRequestRequestTypeDef",
    "CreateServerResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteAccessRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "DeleteSshPublicKeyRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeAccessRequestRequestTypeDef",
    "DescribeAccessResponseTypeDef",
    "DescribeSecurityPolicyRequestRequestTypeDef",
    "DescribeSecurityPolicyResponseTypeDef",
    "DescribeServerRequestRequestTypeDef",
    "DescribeServerResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribedAccessTypeDef",
    "DescribedSecurityPolicyTypeDef",
    "DescribedServerTypeDef",
    "DescribedUserTypeDef",
    "EndpointDetailsTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ImportSshPublicKeyRequestRequestTypeDef",
    "ImportSshPublicKeyResponseTypeDef",
    "ListAccessesRequestRequestTypeDef",
    "ListAccessesResponseTypeDef",
    "ListSecurityPoliciesRequestRequestTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListServersRequestRequestTypeDef",
    "ListServersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListedAccessTypeDef",
    "ListedServerTypeDef",
    "ListedUserTypeDef",
    "PaginatorConfigTypeDef",
    "PosixProfileTypeDef",
    "ProtocolDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "SshPublicKeyTypeDef",
    "StartServerRequestRequestTypeDef",
    "StopServerRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestIdentityProviderRequestRequestTypeDef",
    "TestIdentityProviderResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessRequestRequestTypeDef",
    "UpdateAccessResponseTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "UpdateServerResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
)

_RequiredCreateAccessRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "ExternalId": str,
    },
)
_OptionalCreateAccessRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
    },
    total=False,
)

class CreateAccessRequestRequestTypeDef(
    _RequiredCreateAccessRequestRequestTypeDef, _OptionalCreateAccessRequestRequestTypeDef
):
    pass

CreateAccessResponseTypeDef = TypedDict(
    "CreateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServerRequestRequestTypeDef = TypedDict(
    "CreateServerRequestRequestTypeDef",
    {
        "Certificate": str,
        "Domain": DomainType,
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKey": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": IdentityProviderTypeType,
        "LoggingRole": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "SshPublicKeyBody": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessRequestRequestTypeDef = TypedDict(
    "DeleteAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

DeleteSshPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DescribeAccessRequestRequestTypeDef = TypedDict(
    "DescribeAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DescribeAccessResponseTypeDef = TypedDict(
    "DescribeAccessResponseTypeDef",
    {
        "ServerId": str,
        "Access": "DescribedAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityPolicyRequestRequestTypeDef = TypedDict(
    "DescribeSecurityPolicyRequestRequestTypeDef",
    {
        "SecurityPolicyName": str,
    },
)

DescribeSecurityPolicyResponseTypeDef = TypedDict(
    "DescribeSecurityPolicyResponseTypeDef",
    {
        "SecurityPolicy": "DescribedSecurityPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServerRequestRequestTypeDef = TypedDict(
    "DescribeServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

DescribeServerResponseTypeDef = TypedDict(
    "DescribeServerResponseTypeDef",
    {
        "Server": "DescribedServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "ServerId": str,
        "User": "DescribedUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribedAccessTypeDef = TypedDict(
    "DescribedAccessTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
        "ExternalId": str,
    },
    total=False,
)

_RequiredDescribedSecurityPolicyTypeDef = TypedDict(
    "_RequiredDescribedSecurityPolicyTypeDef",
    {
        "SecurityPolicyName": str,
    },
)
_OptionalDescribedSecurityPolicyTypeDef = TypedDict(
    "_OptionalDescribedSecurityPolicyTypeDef",
    {
        "Fips": bool,
        "SshCiphers": List[str],
        "SshKexs": List[str],
        "SshMacs": List[str],
        "TlsCiphers": List[str],
    },
    total=False,
)

class DescribedSecurityPolicyTypeDef(
    _RequiredDescribedSecurityPolicyTypeDef, _OptionalDescribedSecurityPolicyTypeDef
):
    pass

_RequiredDescribedServerTypeDef = TypedDict(
    "_RequiredDescribedServerTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedServerTypeDef = TypedDict(
    "_OptionalDescribedServerTypeDef",
    {
        "Certificate": str,
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "Domain": DomainType,
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": IdentityProviderTypeType,
        "LoggingRole": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
        "ServerId": str,
        "State": StateType,
        "Tags": List["TagTypeDef"],
        "UserCount": int,
    },
    total=False,
)

class DescribedServerTypeDef(_RequiredDescribedServerTypeDef, _OptionalDescribedServerTypeDef):
    pass

_RequiredDescribedUserTypeDef = TypedDict(
    "_RequiredDescribedUserTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedUserTypeDef = TypedDict(
    "_OptionalDescribedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
        "SshPublicKeys": List["SshPublicKeyTypeDef"],
        "Tags": List["TagTypeDef"],
        "UserName": str,
    },
    total=False,
)

class DescribedUserTypeDef(_RequiredDescribedUserTypeDef, _OptionalDescribedUserTypeDef):
    pass

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "AddressAllocationIds": List[str],
        "SubnetIds": List[str],
        "VpcEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": List[str],
    },
    total=False,
)

HomeDirectoryMapEntryTypeDef = TypedDict(
    "HomeDirectoryMapEntryTypeDef",
    {
        "Entry": str,
        "Target": str,
    },
)

IdentityProviderDetailsTypeDef = TypedDict(
    "IdentityProviderDetailsTypeDef",
    {
        "Url": str,
        "InvocationRole": str,
        "DirectoryId": str,
    },
    total=False,
)

ImportSshPublicKeyRequestRequestTypeDef = TypedDict(
    "ImportSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyBody": str,
        "UserName": str,
    },
)

ImportSshPublicKeyResponseTypeDef = TypedDict(
    "ImportSshPublicKeyResponseTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessesRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessesRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListAccessesRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccessesRequestRequestTypeDef(
    _RequiredListAccessesRequestRequestTypeDef, _OptionalListAccessesRequestRequestTypeDef
):
    pass

ListAccessesResponseTypeDef = TypedDict(
    "ListAccessesResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Accesses": List["ListedAccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityPoliciesRequestRequestTypeDef = TypedDict(
    "ListSecurityPoliciesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSecurityPoliciesResponseTypeDef = TypedDict(
    "ListSecurityPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "SecurityPolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "NextToken": str,
        "Servers": List["ListedServerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Arn": str,
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Users": List["ListedUserTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListedAccessTypeDef = TypedDict(
    "ListedAccessTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Role": str,
        "ExternalId": str,
    },
    total=False,
)

_RequiredListedServerTypeDef = TypedDict(
    "_RequiredListedServerTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListedServerTypeDef = TypedDict(
    "_OptionalListedServerTypeDef",
    {
        "Domain": DomainType,
        "IdentityProviderType": IdentityProviderTypeType,
        "EndpointType": EndpointTypeType,
        "LoggingRole": str,
        "ServerId": str,
        "State": StateType,
        "UserCount": int,
    },
    total=False,
)

class ListedServerTypeDef(_RequiredListedServerTypeDef, _OptionalListedServerTypeDef):
    pass

_RequiredListedUserTypeDef = TypedDict(
    "_RequiredListedUserTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListedUserTypeDef = TypedDict(
    "_OptionalListedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)

class ListedUserTypeDef(_RequiredListedUserTypeDef, _OptionalListedUserTypeDef):
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

_RequiredPosixProfileTypeDef = TypedDict(
    "_RequiredPosixProfileTypeDef",
    {
        "Uid": int,
        "Gid": int,
    },
)
_OptionalPosixProfileTypeDef = TypedDict(
    "_OptionalPosixProfileTypeDef",
    {
        "SecondaryGids": List[int],
    },
    total=False,
)

class PosixProfileTypeDef(_RequiredPosixProfileTypeDef, _OptionalPosixProfileTypeDef):
    pass

ProtocolDetailsTypeDef = TypedDict(
    "ProtocolDetailsTypeDef",
    {
        "PassiveIp": str,
    },
    total=False,
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

SshPublicKeyTypeDef = TypedDict(
    "SshPublicKeyTypeDef",
    {
        "DateImported": datetime,
        "SshPublicKeyBody": str,
        "SshPublicKeyId": str,
    },
)

StartServerRequestRequestTypeDef = TypedDict(
    "StartServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

StopServerRequestRequestTypeDef = TypedDict(
    "StopServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTestIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredTestIdentityProviderRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalTestIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalTestIdentityProviderRequestRequestTypeDef",
    {
        "ServerProtocol": ProtocolType,
        "SourceIp": str,
        "UserPassword": str,
    },
    total=False,
)

class TestIdentityProviderRequestRequestTypeDef(
    _RequiredTestIdentityProviderRequestRequestTypeDef,
    _OptionalTestIdentityProviderRequestRequestTypeDef,
):
    pass

TestIdentityProviderResponseTypeDef = TypedDict(
    "TestIdentityProviderResponseTypeDef",
    {
        "Response": str,
        "StatusCode": int,
        "Message": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAccessRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)
_OptionalUpdateAccessRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
    },
    total=False,
)

class UpdateAccessRequestRequestTypeDef(
    _RequiredUpdateAccessRequestRequestTypeDef, _OptionalUpdateAccessRequestRequestTypeDef
):
    pass

UpdateAccessResponseTypeDef = TypedDict(
    "UpdateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalUpdateServerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerRequestRequestTypeDef",
    {
        "Certificate": str,
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKey": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "LoggingRole": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
    },
    total=False,
)

class UpdateServerRequestRequestTypeDef(
    _RequiredUpdateServerRequestRequestTypeDef, _OptionalUpdateServerRequestRequestTypeDef
):
    pass

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
