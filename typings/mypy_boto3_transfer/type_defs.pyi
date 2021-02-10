"""
Main interface for transfer service type definitions.

Usage::

    ```python
    from mypy_boto3_transfer.type_defs import DescribedSecurityPolicyTypeDef

    data: DescribedSecurityPolicyTypeDef = {...}
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
    "DescribedSecurityPolicyTypeDef",
    "DescribedServerTypeDef",
    "DescribedUserTypeDef",
    "EndpointDetailsTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ListedServerTypeDef",
    "ListedUserTypeDef",
    "PosixProfileTypeDef",
    "SshPublicKeyTypeDef",
    "TagTypeDef",
    "CreateServerResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeSecurityPolicyResponseTypeDef",
    "DescribeServerResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "ImportSshPublicKeyResponseTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListServersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TestIdentityProviderResponseTypeDef",
    "UpdateServerResponseTypeDef",
    "UpdateUserResponseTypeDef",
)

_RequiredDescribedSecurityPolicyTypeDef = TypedDict(
    "_RequiredDescribedSecurityPolicyTypeDef", {"SecurityPolicyName": str}
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


_RequiredDescribedServerTypeDef = TypedDict("_RequiredDescribedServerTypeDef", {"Arn": str})
_OptionalDescribedServerTypeDef = TypedDict(
    "_OptionalDescribedServerTypeDef",
    {
        "Certificate": str,
        "Domain": Literal["S3", "EFS"],
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": Literal["PUBLIC", "VPC", "VPC_ENDPOINT"],
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "LoggingRole": str,
        "Protocols": List[Literal["SFTP", "FTP", "FTPS"]],
        "SecurityPolicyName": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "Tags": List["TagTypeDef"],
        "UserCount": int,
    },
    total=False,
)


class DescribedServerTypeDef(_RequiredDescribedServerTypeDef, _OptionalDescribedServerTypeDef):
    pass


_RequiredDescribedUserTypeDef = TypedDict("_RequiredDescribedUserTypeDef", {"Arn": str})
_OptionalDescribedUserTypeDef = TypedDict(
    "_OptionalDescribedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": Literal["PATH", "LOGICAL"],
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
    "HomeDirectoryMapEntryTypeDef", {"Entry": str, "Target": str}
)

IdentityProviderDetailsTypeDef = TypedDict(
    "IdentityProviderDetailsTypeDef", {"Url": str, "InvocationRole": str}, total=False
)

_RequiredListedServerTypeDef = TypedDict("_RequiredListedServerTypeDef", {"Arn": str})
_OptionalListedServerTypeDef = TypedDict(
    "_OptionalListedServerTypeDef",
    {
        "Domain": Literal["S3", "EFS"],
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "EndpointType": Literal["PUBLIC", "VPC", "VPC_ENDPOINT"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "UserCount": int,
    },
    total=False,
)


class ListedServerTypeDef(_RequiredListedServerTypeDef, _OptionalListedServerTypeDef):
    pass


_RequiredListedUserTypeDef = TypedDict("_RequiredListedUserTypeDef", {"Arn": str})
_OptionalListedUserTypeDef = TypedDict(
    "_OptionalListedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": Literal["PATH", "LOGICAL"],
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)


class ListedUserTypeDef(_RequiredListedUserTypeDef, _OptionalListedUserTypeDef):
    pass


_RequiredPosixProfileTypeDef = TypedDict("_RequiredPosixProfileTypeDef", {"Uid": int, "Gid": int})
_OptionalPosixProfileTypeDef = TypedDict(
    "_OptionalPosixProfileTypeDef", {"SecondaryGids": List[int]}, total=False
)


class PosixProfileTypeDef(_RequiredPosixProfileTypeDef, _OptionalPosixProfileTypeDef):
    pass


SshPublicKeyTypeDef = TypedDict(
    "SshPublicKeyTypeDef",
    {"DateImported": datetime, "SshPublicKeyBody": str, "SshPublicKeyId": str},
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateServerResponseTypeDef = TypedDict("CreateServerResponseTypeDef", {"ServerId": str})

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef", {"ServerId": str, "UserName": str}
)

DescribeSecurityPolicyResponseTypeDef = TypedDict(
    "DescribeSecurityPolicyResponseTypeDef", {"SecurityPolicy": "DescribedSecurityPolicyTypeDef"}
)

DescribeServerResponseTypeDef = TypedDict(
    "DescribeServerResponseTypeDef", {"Server": "DescribedServerTypeDef"}
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef", {"ServerId": str, "User": "DescribedUserTypeDef"}
)

ImportSshPublicKeyResponseTypeDef = TypedDict(
    "ImportSshPublicKeyResponseTypeDef", {"ServerId": str, "SshPublicKeyId": str, "UserName": str}
)

_RequiredListSecurityPoliciesResponseTypeDef = TypedDict(
    "_RequiredListSecurityPoliciesResponseTypeDef", {"SecurityPolicyNames": List[str]}
)
_OptionalListSecurityPoliciesResponseTypeDef = TypedDict(
    "_OptionalListSecurityPoliciesResponseTypeDef", {"NextToken": str}, total=False
)


class ListSecurityPoliciesResponseTypeDef(
    _RequiredListSecurityPoliciesResponseTypeDef, _OptionalListSecurityPoliciesResponseTypeDef
):
    pass


_RequiredListServersResponseTypeDef = TypedDict(
    "_RequiredListServersResponseTypeDef", {"Servers": List["ListedServerTypeDef"]}
)
_OptionalListServersResponseTypeDef = TypedDict(
    "_OptionalListServersResponseTypeDef", {"NextToken": str}, total=False
)


class ListServersResponseTypeDef(
    _RequiredListServersResponseTypeDef, _OptionalListServersResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Arn": str, "NextToken": str, "Tags": List["TagTypeDef"]},
    total=False,
)

_RequiredListUsersResponseTypeDef = TypedDict(
    "_RequiredListUsersResponseTypeDef", {"ServerId": str, "Users": List["ListedUserTypeDef"]}
)
_OptionalListUsersResponseTypeDef = TypedDict(
    "_OptionalListUsersResponseTypeDef", {"NextToken": str}, total=False
)


class ListUsersResponseTypeDef(
    _RequiredListUsersResponseTypeDef, _OptionalListUsersResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredTestIdentityProviderResponseTypeDef = TypedDict(
    "_RequiredTestIdentityProviderResponseTypeDef", {"StatusCode": int, "Url": str}
)
_OptionalTestIdentityProviderResponseTypeDef = TypedDict(
    "_OptionalTestIdentityProviderResponseTypeDef", {"Response": str, "Message": str}, total=False
)


class TestIdentityProviderResponseTypeDef(
    _RequiredTestIdentityProviderResponseTypeDef, _OptionalTestIdentityProviderResponseTypeDef
):
    pass


UpdateServerResponseTypeDef = TypedDict("UpdateServerResponseTypeDef", {"ServerId": str})

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef", {"ServerId": str, "UserName": str}
)
