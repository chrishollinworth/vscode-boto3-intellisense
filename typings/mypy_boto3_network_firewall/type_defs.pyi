"""
Main interface for network-firewall service type definitions.

Usage::

    ```python
    from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef

    data: ActionDefinitionTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionDefinitionTypeDef",
    "AddressTypeDef",
    "AttachmentTypeDef",
    "CustomActionTypeDef",
    "DimensionTypeDef",
    "FirewallMetadataTypeDef",
    "FirewallPolicyMetadataTypeDef",
    "FirewallPolicyResponseTypeDef",
    "FirewallPolicyTypeDef",
    "FirewallStatusTypeDef",
    "FirewallTypeDef",
    "HeaderTypeDef",
    "IPSetTypeDef",
    "LogDestinationConfigTypeDef",
    "LoggingConfigurationTypeDef",
    "MatchAttributesTypeDef",
    "PerObjectStatusTypeDef",
    "PortRangeTypeDef",
    "PortSetTypeDef",
    "PublishMetricActionTypeDef",
    "RuleDefinitionTypeDef",
    "RuleGroupMetadataTypeDef",
    "RuleGroupResponseTypeDef",
    "RuleGroupTypeDef",
    "RuleOptionTypeDef",
    "RuleVariablesTypeDef",
    "RulesSourceListTypeDef",
    "RulesSourceTypeDef",
    "StatefulRuleGroupReferenceTypeDef",
    "StatefulRuleTypeDef",
    "StatelessRuleGroupReferenceTypeDef",
    "StatelessRuleTypeDef",
    "StatelessRulesAndCustomActionsTypeDef",
    "SubnetMappingTypeDef",
    "SyncStateTypeDef",
    "TCPFlagFieldTypeDef",
    "TagTypeDef",
    "AssociateFirewallPolicyResponseTypeDef",
    "AssociateSubnetsResponseTypeDef",
    "CreateFirewallPolicyResponseTypeDef",
    "CreateFirewallResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "DeleteFirewallPolicyResponseTypeDef",
    "DeleteFirewallResponseTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DescribeFirewallPolicyResponseTypeDef",
    "DescribeFirewallResponseTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRuleGroupResponseTypeDef",
    "DisassociateSubnetsResponseTypeDef",
    "ListFirewallPoliciesResponseTypeDef",
    "ListFirewallsResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    "UpdateFirewallDescriptionResponseTypeDef",
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    "UpdateFirewallPolicyResponseTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateSubnetChangeProtectionResponseTypeDef",
)

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef", {"PublishMetricAction": "PublishMetricActionTypeDef"}, total=False
)

AddressTypeDef = TypedDict("AddressTypeDef", {"AddressDefinition": str})

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "SubnetId": str,
        "EndpointId": str,
        "Status": Literal["CREATING", "DELETING", "SCALING", "READY"],
    },
    total=False,
)

CustomActionTypeDef = TypedDict(
    "CustomActionTypeDef", {"ActionName": str, "ActionDefinition": "ActionDefinitionTypeDef"}
)

DimensionTypeDef = TypedDict("DimensionTypeDef", {"Value": str})

FirewallMetadataTypeDef = TypedDict(
    "FirewallMetadataTypeDef", {"FirewallName": str, "FirewallArn": str}, total=False
)

FirewallPolicyMetadataTypeDef = TypedDict(
    "FirewallPolicyMetadataTypeDef", {"Name": str, "Arn": str}, total=False
)

_RequiredFirewallPolicyResponseTypeDef = TypedDict(
    "_RequiredFirewallPolicyResponseTypeDef",
    {"FirewallPolicyName": str, "FirewallPolicyArn": str, "FirewallPolicyId": str},
)
_OptionalFirewallPolicyResponseTypeDef = TypedDict(
    "_OptionalFirewallPolicyResponseTypeDef",
    {
        "Description": str,
        "FirewallPolicyStatus": Literal["ACTIVE", "DELETING"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class FirewallPolicyResponseTypeDef(
    _RequiredFirewallPolicyResponseTypeDef, _OptionalFirewallPolicyResponseTypeDef
):
    pass


_RequiredFirewallPolicyTypeDef = TypedDict(
    "_RequiredFirewallPolicyTypeDef",
    {"StatelessDefaultActions": List[str], "StatelessFragmentDefaultActions": List[str]},
)
_OptionalFirewallPolicyTypeDef = TypedDict(
    "_OptionalFirewallPolicyTypeDef",
    {
        "StatelessRuleGroupReferences": List["StatelessRuleGroupReferenceTypeDef"],
        "StatelessCustomActions": List["CustomActionTypeDef"],
        "StatefulRuleGroupReferences": List["StatefulRuleGroupReferenceTypeDef"],
    },
    total=False,
)


class FirewallPolicyTypeDef(_RequiredFirewallPolicyTypeDef, _OptionalFirewallPolicyTypeDef):
    pass


_RequiredFirewallStatusTypeDef = TypedDict(
    "_RequiredFirewallStatusTypeDef",
    {
        "Status": Literal["PROVISIONING", "DELETING", "READY"],
        "ConfigurationSyncStateSummary": Literal["PENDING", "IN_SYNC"],
    },
)
_OptionalFirewallStatusTypeDef = TypedDict(
    "_OptionalFirewallStatusTypeDef", {"SyncStates": Dict[str, "SyncStateTypeDef"]}, total=False
)


class FirewallStatusTypeDef(_RequiredFirewallStatusTypeDef, _OptionalFirewallStatusTypeDef):
    pass


_RequiredFirewallTypeDef = TypedDict(
    "_RequiredFirewallTypeDef",
    {
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "FirewallId": str,
    },
)
_OptionalFirewallTypeDef = TypedDict(
    "_OptionalFirewallTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
        "DeleteProtection": bool,
        "SubnetChangeProtection": bool,
        "FirewallPolicyChangeProtection": bool,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class FirewallTypeDef(_RequiredFirewallTypeDef, _OptionalFirewallTypeDef):
    pass


HeaderTypeDef = TypedDict(
    "HeaderTypeDef",
    {
        "Protocol": Literal[
            "IP",
            "TCP",
            "UDP",
            "ICMP",
            "HTTP",
            "FTP",
            "TLS",
            "SMB",
            "DNS",
            "DCERPC",
            "SSH",
            "SMTP",
            "IMAP",
            "MSN",
            "KRB5",
            "IKEV2",
            "TFTP",
            "NTP",
            "DHCP",
        ],
        "Source": str,
        "SourcePort": str,
        "Direction": Literal["FORWARD", "ANY"],
        "Destination": str,
        "DestinationPort": str,
    },
)

IPSetTypeDef = TypedDict("IPSetTypeDef", {"Definition": List[str]})

LogDestinationConfigTypeDef = TypedDict(
    "LogDestinationConfigTypeDef",
    {
        "LogType": Literal["ALERT", "FLOW"],
        "LogDestinationType": Literal["S3", "CloudWatchLogs", "KinesisDataFirehose"],
        "LogDestination": Dict[str, str],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef", {"LogDestinationConfigs": List["LogDestinationConfigTypeDef"]}
)

MatchAttributesTypeDef = TypedDict(
    "MatchAttributesTypeDef",
    {
        "Sources": List["AddressTypeDef"],
        "Destinations": List["AddressTypeDef"],
        "SourcePorts": List["PortRangeTypeDef"],
        "DestinationPorts": List["PortRangeTypeDef"],
        "Protocols": List[int],
        "TCPFlags": List["TCPFlagFieldTypeDef"],
    },
    total=False,
)

PerObjectStatusTypeDef = TypedDict(
    "PerObjectStatusTypeDef", {"SyncStatus": Literal["PENDING", "IN_SYNC"]}, total=False
)

PortRangeTypeDef = TypedDict("PortRangeTypeDef", {"FromPort": int, "ToPort": int})

PortSetTypeDef = TypedDict("PortSetTypeDef", {"Definition": List[str]}, total=False)

PublishMetricActionTypeDef = TypedDict(
    "PublishMetricActionTypeDef", {"Dimensions": List["DimensionTypeDef"]}
)

RuleDefinitionTypeDef = TypedDict(
    "RuleDefinitionTypeDef", {"MatchAttributes": "MatchAttributesTypeDef", "Actions": List[str]}
)

RuleGroupMetadataTypeDef = TypedDict(
    "RuleGroupMetadataTypeDef", {"Name": str, "Arn": str}, total=False
)

_RequiredRuleGroupResponseTypeDef = TypedDict(
    "_RequiredRuleGroupResponseTypeDef",
    {"RuleGroupArn": str, "RuleGroupName": str, "RuleGroupId": str},
)
_OptionalRuleGroupResponseTypeDef = TypedDict(
    "_OptionalRuleGroupResponseTypeDef",
    {
        "Description": str,
        "Type": Literal["STATELESS", "STATEFUL"],
        "Capacity": int,
        "RuleGroupStatus": Literal["ACTIVE", "DELETING"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RuleGroupResponseTypeDef(
    _RequiredRuleGroupResponseTypeDef, _OptionalRuleGroupResponseTypeDef
):
    pass


_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef", {"RulesSource": "RulesSourceTypeDef"}
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef", {"RuleVariables": "RuleVariablesTypeDef"}, total=False
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


_RequiredRuleOptionTypeDef = TypedDict("_RequiredRuleOptionTypeDef", {"Keyword": str})
_OptionalRuleOptionTypeDef = TypedDict(
    "_OptionalRuleOptionTypeDef", {"Settings": List[str]}, total=False
)


class RuleOptionTypeDef(_RequiredRuleOptionTypeDef, _OptionalRuleOptionTypeDef):
    pass


RuleVariablesTypeDef = TypedDict(
    "RuleVariablesTypeDef",
    {"IPSets": Dict[str, "IPSetTypeDef"], "PortSets": Dict[str, "PortSetTypeDef"]},
    total=False,
)

RulesSourceListTypeDef = TypedDict(
    "RulesSourceListTypeDef",
    {
        "Targets": List[str],
        "TargetTypes": List[Literal["TLS_SNI", "HTTP_HOST"]],
        "GeneratedRulesType": Literal["ALLOWLIST", "DENYLIST"],
    },
)

RulesSourceTypeDef = TypedDict(
    "RulesSourceTypeDef",
    {
        "RulesString": str,
        "RulesSourceList": "RulesSourceListTypeDef",
        "StatefulRules": List["StatefulRuleTypeDef"],
        "StatelessRulesAndCustomActions": "StatelessRulesAndCustomActionsTypeDef",
    },
    total=False,
)

StatefulRuleGroupReferenceTypeDef = TypedDict(
    "StatefulRuleGroupReferenceTypeDef", {"ResourceArn": str}
)

StatefulRuleTypeDef = TypedDict(
    "StatefulRuleTypeDef",
    {
        "Action": Literal["PASS", "DROP", "ALERT"],
        "Header": "HeaderTypeDef",
        "RuleOptions": List["RuleOptionTypeDef"],
    },
)

StatelessRuleGroupReferenceTypeDef = TypedDict(
    "StatelessRuleGroupReferenceTypeDef", {"ResourceArn": str, "Priority": int}
)

StatelessRuleTypeDef = TypedDict(
    "StatelessRuleTypeDef", {"RuleDefinition": "RuleDefinitionTypeDef", "Priority": int}
)

_RequiredStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_RequiredStatelessRulesAndCustomActionsTypeDef",
    {"StatelessRules": List["StatelessRuleTypeDef"]},
)
_OptionalStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_OptionalStatelessRulesAndCustomActionsTypeDef",
    {"CustomActions": List["CustomActionTypeDef"]},
    total=False,
)


class StatelessRulesAndCustomActionsTypeDef(
    _RequiredStatelessRulesAndCustomActionsTypeDef, _OptionalStatelessRulesAndCustomActionsTypeDef
):
    pass


SubnetMappingTypeDef = TypedDict("SubnetMappingTypeDef", {"SubnetId": str})

SyncStateTypeDef = TypedDict(
    "SyncStateTypeDef",
    {"Attachment": "AttachmentTypeDef", "Config": Dict[str, "PerObjectStatusTypeDef"]},
    total=False,
)

_RequiredTCPFlagFieldTypeDef = TypedDict(
    "_RequiredTCPFlagFieldTypeDef",
    {"Flags": List[Literal["FIN", "SYN", "RST", "PSH", "ACK", "URG", "ECE", "CWR"]]},
)
_OptionalTCPFlagFieldTypeDef = TypedDict(
    "_OptionalTCPFlagFieldTypeDef",
    {"Masks": List[Literal["FIN", "SYN", "RST", "PSH", "ACK", "URG", "ECE", "CWR"]]},
    total=False,
)


class TCPFlagFieldTypeDef(_RequiredTCPFlagFieldTypeDef, _OptionalTCPFlagFieldTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

AssociateFirewallPolicyResponseTypeDef = TypedDict(
    "AssociateFirewallPolicyResponseTypeDef",
    {"FirewallArn": str, "FirewallName": str, "FirewallPolicyArn": str, "UpdateToken": str},
    total=False,
)

AssociateSubnetsResponseTypeDef = TypedDict(
    "AssociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
    },
    total=False,
)

CreateFirewallPolicyResponseTypeDef = TypedDict(
    "CreateFirewallPolicyResponseTypeDef",
    {"UpdateToken": str, "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef"},
)

CreateFirewallResponseTypeDef = TypedDict(
    "CreateFirewallResponseTypeDef",
    {"Firewall": "FirewallTypeDef", "FirewallStatus": "FirewallStatusTypeDef"},
    total=False,
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {"UpdateToken": str, "RuleGroupResponse": "RuleGroupResponseTypeDef"},
)

DeleteFirewallPolicyResponseTypeDef = TypedDict(
    "DeleteFirewallPolicyResponseTypeDef",
    {"FirewallPolicyResponse": "FirewallPolicyResponseTypeDef"},
)

DeleteFirewallResponseTypeDef = TypedDict(
    "DeleteFirewallResponseTypeDef",
    {"Firewall": "FirewallTypeDef", "FirewallStatus": "FirewallStatusTypeDef"},
    total=False,
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef", {"RuleGroupResponse": "RuleGroupResponseTypeDef"}
)

_RequiredDescribeFirewallPolicyResponseTypeDef = TypedDict(
    "_RequiredDescribeFirewallPolicyResponseTypeDef",
    {"UpdateToken": str, "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef"},
)
_OptionalDescribeFirewallPolicyResponseTypeDef = TypedDict(
    "_OptionalDescribeFirewallPolicyResponseTypeDef",
    {"FirewallPolicy": "FirewallPolicyTypeDef"},
    total=False,
)


class DescribeFirewallPolicyResponseTypeDef(
    _RequiredDescribeFirewallPolicyResponseTypeDef, _OptionalDescribeFirewallPolicyResponseTypeDef
):
    pass


DescribeFirewallResponseTypeDef = TypedDict(
    "DescribeFirewallResponseTypeDef",
    {"UpdateToken": str, "Firewall": "FirewallTypeDef", "FirewallStatus": "FirewallStatusTypeDef"},
    total=False,
)

DescribeLoggingConfigurationResponseTypeDef = TypedDict(
    "DescribeLoggingConfigurationResponseTypeDef",
    {"FirewallArn": str, "LoggingConfiguration": "LoggingConfigurationTypeDef"},
    total=False,
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef", {"Policy": str}, total=False
)

_RequiredDescribeRuleGroupResponseTypeDef = TypedDict(
    "_RequiredDescribeRuleGroupResponseTypeDef",
    {"UpdateToken": str, "RuleGroupResponse": "RuleGroupResponseTypeDef"},
)
_OptionalDescribeRuleGroupResponseTypeDef = TypedDict(
    "_OptionalDescribeRuleGroupResponseTypeDef", {"RuleGroup": "RuleGroupTypeDef"}, total=False
)


class DescribeRuleGroupResponseTypeDef(
    _RequiredDescribeRuleGroupResponseTypeDef, _OptionalDescribeRuleGroupResponseTypeDef
):
    pass


DisassociateSubnetsResponseTypeDef = TypedDict(
    "DisassociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
    },
    total=False,
)

ListFirewallPoliciesResponseTypeDef = TypedDict(
    "ListFirewallPoliciesResponseTypeDef",
    {"NextToken": str, "FirewallPolicies": List["FirewallPolicyMetadataTypeDef"]},
    total=False,
)

ListFirewallsResponseTypeDef = TypedDict(
    "ListFirewallsResponseTypeDef",
    {"NextToken": str, "Firewalls": List["FirewallMetadataTypeDef"]},
    total=False,
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {"NextToken": str, "RuleGroups": List["RuleGroupMetadataTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"NextToken": str, "Tags": List["TagTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateFirewallDeleteProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    {"FirewallArn": str, "FirewallName": str, "DeleteProtection": bool, "UpdateToken": str},
    total=False,
)

UpdateFirewallDescriptionResponseTypeDef = TypedDict(
    "UpdateFirewallDescriptionResponseTypeDef",
    {"FirewallArn": str, "FirewallName": str, "Description": str, "UpdateToken": str},
    total=False,
)

UpdateFirewallPolicyChangeProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyChangeProtection": bool,
    },
    total=False,
)

UpdateFirewallPolicyResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyResponseTypeDef",
    {"UpdateToken": str, "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef"},
)

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
    total=False,
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {"UpdateToken": str, "RuleGroupResponse": "RuleGroupResponseTypeDef"},
)

UpdateSubnetChangeProtectionResponseTypeDef = TypedDict(
    "UpdateSubnetChangeProtectionResponseTypeDef",
    {"UpdateToken": str, "FirewallArn": str, "FirewallName": str, "SubnetChangeProtection": bool},
    total=False,
)
