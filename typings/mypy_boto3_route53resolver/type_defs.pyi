"""
Main interface for route53resolver service type definitions.

Usage::

    ```python
    from mypy_boto3_route53resolver.type_defs import IpAddressResponseTypeDef

    data: IpAddressResponseTypeDef = {...}
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
    "IpAddressResponseTypeDef",
    "ResolverEndpointTypeDef",
    "ResolverRuleAssociationTypeDef",
    "ResolverRuleTypeDef",
    "TagTypeDef",
    "TargetAddressTypeDef",
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    "AssociateResolverRuleResponseTypeDef",
    "CreateResolverEndpointResponseTypeDef",
    "CreateResolverRuleResponseTypeDef",
    "DeleteResolverEndpointResponseTypeDef",
    "DeleteResolverRuleResponseTypeDef",
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    "DisassociateResolverRuleResponseTypeDef",
    "FilterTypeDef",
    "GetResolverEndpointResponseTypeDef",
    "GetResolverRuleAssociationResponseTypeDef",
    "GetResolverRulePolicyResponseTypeDef",
    "GetResolverRuleResponseTypeDef",
    "IpAddressRequestTypeDef",
    "IpAddressUpdateTypeDef",
    "ListResolverEndpointIpAddressesResponseTypeDef",
    "ListResolverEndpointsResponseTypeDef",
    "ListResolverRuleAssociationsResponseTypeDef",
    "ListResolverRulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResolverRulePolicyResponseTypeDef",
    "ResolverRuleConfigTypeDef",
    "UpdateResolverEndpointResponseTypeDef",
    "UpdateResolverRuleResponseTypeDef",
)

IpAddressResponseTypeDef = TypedDict(
    "IpAddressResponseTypeDef",
    {
        "IpId": str,
        "SubnetId": str,
        "Ip": str,
        "Status": Literal[
            "CREATING",
            "FAILED_CREATION",
            "ATTACHING",
            "ATTACHED",
            "REMAP_DETACHING",
            "REMAP_ATTACHING",
            "DETACHING",
            "FAILED_RESOURCE_GONE",
            "DELETING",
            "DELETE_FAILED_FAS_EXPIRED",
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ResolverEndpointTypeDef = TypedDict(
    "ResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ResolverRuleAssociationTypeDef = TypedDict(
    "ResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)

ResolverRuleTypeDef = TypedDict(
    "ResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List["TargetAddressTypeDef"],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

_RequiredTargetAddressTypeDef = TypedDict("_RequiredTargetAddressTypeDef", {"Ip": str})
_OptionalTargetAddressTypeDef = TypedDict(
    "_OptionalTargetAddressTypeDef", {"Port": int}, total=False
)


class TargetAddressTypeDef(_RequiredTargetAddressTypeDef, _OptionalTargetAddressTypeDef):
    pass


AssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    {"ResolverEndpoint": "ResolverEndpointTypeDef"},
    total=False,
)

AssociateResolverRuleResponseTypeDef = TypedDict(
    "AssociateResolverRuleResponseTypeDef",
    {"ResolverRuleAssociation": "ResolverRuleAssociationTypeDef"},
    total=False,
)

CreateResolverEndpointResponseTypeDef = TypedDict(
    "CreateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": "ResolverEndpointTypeDef"},
    total=False,
)

CreateResolverRuleResponseTypeDef = TypedDict(
    "CreateResolverRuleResponseTypeDef", {"ResolverRule": "ResolverRuleTypeDef"}, total=False
)

DeleteResolverEndpointResponseTypeDef = TypedDict(
    "DeleteResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": "ResolverEndpointTypeDef"},
    total=False,
)

DeleteResolverRuleResponseTypeDef = TypedDict(
    "DeleteResolverRuleResponseTypeDef", {"ResolverRule": "ResolverRuleTypeDef"}, total=False
)

DisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    {"ResolverEndpoint": "ResolverEndpointTypeDef"},
    total=False,
)

DisassociateResolverRuleResponseTypeDef = TypedDict(
    "DisassociateResolverRuleResponseTypeDef",
    {"ResolverRuleAssociation": "ResolverRuleAssociationTypeDef"},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

GetResolverEndpointResponseTypeDef = TypedDict(
    "GetResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": "ResolverEndpointTypeDef"},
    total=False,
)

GetResolverRuleAssociationResponseTypeDef = TypedDict(
    "GetResolverRuleAssociationResponseTypeDef",
    {"ResolverRuleAssociation": "ResolverRuleAssociationTypeDef"},
    total=False,
)

GetResolverRulePolicyResponseTypeDef = TypedDict(
    "GetResolverRulePolicyResponseTypeDef", {"ResolverRulePolicy": str}, total=False
)

GetResolverRuleResponseTypeDef = TypedDict(
    "GetResolverRuleResponseTypeDef", {"ResolverRule": "ResolverRuleTypeDef"}, total=False
)

_RequiredIpAddressRequestTypeDef = TypedDict("_RequiredIpAddressRequestTypeDef", {"SubnetId": str})
_OptionalIpAddressRequestTypeDef = TypedDict(
    "_OptionalIpAddressRequestTypeDef", {"Ip": str}, total=False
)


class IpAddressRequestTypeDef(_RequiredIpAddressRequestTypeDef, _OptionalIpAddressRequestTypeDef):
    pass


IpAddressUpdateTypeDef = TypedDict(
    "IpAddressUpdateTypeDef", {"IpId": str, "SubnetId": str, "Ip": str}, total=False
)

ListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesResponseTypeDef",
    {"NextToken": str, "MaxResults": int, "IpAddresses": List["IpAddressResponseTypeDef"]},
    total=False,
)

ListResolverEndpointsResponseTypeDef = TypedDict(
    "ListResolverEndpointsResponseTypeDef",
    {"NextToken": str, "MaxResults": int, "ResolverEndpoints": List["ResolverEndpointTypeDef"]},
    total=False,
)

ListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "ListResolverRuleAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List["ResolverRuleAssociationTypeDef"],
    },
    total=False,
)

ListResolverRulesResponseTypeDef = TypedDict(
    "ListResolverRulesResponseTypeDef",
    {"NextToken": str, "MaxResults": int, "ResolverRules": List["ResolverRuleTypeDef"]},
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

PutResolverRulePolicyResponseTypeDef = TypedDict(
    "PutResolverRulePolicyResponseTypeDef", {"ReturnValue": bool}, total=False
)

ResolverRuleConfigTypeDef = TypedDict(
    "ResolverRuleConfigTypeDef",
    {"Name": str, "TargetIps": List["TargetAddressTypeDef"], "ResolverEndpointId": str},
    total=False,
)

UpdateResolverEndpointResponseTypeDef = TypedDict(
    "UpdateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": "ResolverEndpointTypeDef"},
    total=False,
)

UpdateResolverRuleResponseTypeDef = TypedDict(
    "UpdateResolverRuleResponseTypeDef", {"ResolverRule": "ResolverRuleTypeDef"}, total=False
)
