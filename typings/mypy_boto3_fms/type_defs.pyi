"""
Main interface for fms service type definitions.

Usage::

    ```python
    from mypy_boto3_fms.type_defs import AppTypeDef

    data: AppTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
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
    "AppTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "ComplianceViolatorTypeDef",
    "EvaluationResultTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "PartialMatchTypeDef",
    "PolicyComplianceDetailTypeDef",
    "PolicyComplianceStatusTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ProtocolsListDataTypeDef",
    "ResourceTagTypeDef",
    "ResourceViolationTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "StatefulRuleGroupTypeDef",
    "StatelessRuleGroupTypeDef",
    "TagTypeDef",
    "ViolationDetailTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetAppsListResponseTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetProtocolsListResponseTypeDef",
    "GetViolationDetailsResponseTypeDef",
    "ListAppsListsResponseTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAppsListResponseTypeDef",
    "PutPolicyResponseTypeDef",
    "PutProtocolsListResponseTypeDef",
)

AppTypeDef = TypedDict("AppTypeDef", {"AppName": str, "Protocol": str, "Port": int})

AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {"ListArn": str, "ListId": str, "ListName": str, "AppsList": List["AppTypeDef"]},
    total=False,
)

_RequiredAppsListDataTypeDef = TypedDict(
    "_RequiredAppsListDataTypeDef", {"ListName": str, "AppsList": List["AppTypeDef"]}
)
_OptionalAppsListDataTypeDef = TypedDict(
    "_OptionalAppsListDataTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
        "PreviousAppsList": Dict[str, List["AppTypeDef"]],
    },
    total=False,
)


class AppsListDataTypeDef(_RequiredAppsListDataTypeDef, _OptionalAppsListDataTypeDef):
    pass


AwsEc2InstanceViolationTypeDef = TypedDict(
    "AwsEc2InstanceViolationTypeDef",
    {
        "ViolationTarget": str,
        "AwsEc2NetworkInterfaceViolations": List["AwsEc2NetworkInterfaceViolationTypeDef"],
    },
    total=False,
)

AwsEc2NetworkInterfaceViolationTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceViolationTypeDef",
    {"ViolationTarget": str, "ViolatingSecurityGroups": List[str]},
    total=False,
)

AwsVPCSecurityGroupViolationTypeDef = TypedDict(
    "AwsVPCSecurityGroupViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "PartialMatches": List["PartialMatchTypeDef"],
        "PossibleSecurityGroupRemediationActions": List["SecurityGroupRemediationActionTypeDef"],
    },
    total=False,
)

ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": str,
        "ViolationReason": Literal[
            "WEB_ACL_MISSING_RULE_GROUP",
            "RESOURCE_MISSING_WEB_ACL",
            "RESOURCE_INCORRECT_WEB_ACL",
            "RESOURCE_MISSING_SHIELD_PROTECTION",
            "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
            "RESOURCE_MISSING_SECURITY_GROUP",
            "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
            "SECURITY_GROUP_UNUSED",
            "SECURITY_GROUP_REDUNDANT",
            "MISSING_FIREWALL",
            "MISSING_FIREWALL_SUBNET_IN_AZ",
            "MISSING_EXPECTED_ROUTE_TABLE",
            "NETWORK_FIREWALL_POLICY_MODIFIED",
        ],
        "ResourceType": str,
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

NetworkFirewallMissingExpectedRTViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "CurrentRouteTable": str,
        "ExpectedRouteTable": str,
    },
    total=False,
)

NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {"ViolationTarget": str, "VPC": str, "AvailabilityZone": str, "TargetViolationReason": str},
    total=False,
)

NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {"ViolationTarget": str, "VPC": str, "AvailabilityZone": str, "TargetViolationReason": str},
    total=False,
)

NetworkFirewallPolicyDescriptionTypeDef = TypedDict(
    "NetworkFirewallPolicyDescriptionTypeDef",
    {
        "StatelessRuleGroups": List["StatelessRuleGroupTypeDef"],
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
        "StatelessCustomActions": List[str],
        "StatefulRuleGroups": List["StatefulRuleGroupTypeDef"],
    },
    total=False,
)

NetworkFirewallPolicyModifiedViolationTypeDef = TypedDict(
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    {
        "ViolationTarget": str,
        "CurrentPolicyDescription": "NetworkFirewallPolicyDescriptionTypeDef",
        "ExpectedPolicyDescription": "NetworkFirewallPolicyDescriptionTypeDef",
    },
    total=False,
)

PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef", {"Reference": str, "TargetViolationReasons": List[str]}, total=False
)

PolicyComplianceDetailTypeDef = TypedDict(
    "PolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "MemberAccount": str,
        "Violators": List["ComplianceViolatorTypeDef"],
        "EvaluationLimitExceeded": bool,
        "ExpiredAt": datetime,
        "IssueInfoMap": Dict[Literal["AWSCONFIG", "AWSWAF", "AWSSHIELD_ADVANCED", "AWSVPC"], str],
    },
    total=False,
)

PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[Literal["AWSCONFIG", "AWSWAF", "AWSSHIELD_ADVANCED", "AWSVPC"], str],
    },
    total=False,
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": Literal[
            "WAF",
            "WAFV2",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
            "NETWORK_FIREWALL",
        ],
        "RemediationEnabled": bool,
    },
    total=False,
)

_RequiredPolicyTypeDef = TypedDict(
    "_RequiredPolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": "SecurityServicePolicyDataTypeDef",
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
    },
)
_OptionalPolicyTypeDef = TypedDict(
    "_OptionalPolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyUpdateToken": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List["ResourceTagTypeDef"],
        "IncludeMap": Dict[Literal["ACCOUNT", "ORG_UNIT"], List[str]],
        "ExcludeMap": Dict[Literal["ACCOUNT", "ORG_UNIT"], List[str]],
    },
    total=False,
)


class PolicyTypeDef(_RequiredPolicyTypeDef, _OptionalPolicyTypeDef):
    pass


ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {"ListArn": str, "ListId": str, "ListName": str, "ProtocolsList": List[str]},
    total=False,
)

_RequiredProtocolsListDataTypeDef = TypedDict(
    "_RequiredProtocolsListDataTypeDef", {"ListName": str, "ProtocolsList": List[str]}
)
_OptionalProtocolsListDataTypeDef = TypedDict(
    "_OptionalProtocolsListDataTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
        "PreviousProtocolsList": Dict[str, List[str]],
    },
    total=False,
)


class ProtocolsListDataTypeDef(
    _RequiredProtocolsListDataTypeDef, _OptionalProtocolsListDataTypeDef
):
    pass


_RequiredResourceTagTypeDef = TypedDict("_RequiredResourceTagTypeDef", {"Key": str})
_OptionalResourceTagTypeDef = TypedDict("_OptionalResourceTagTypeDef", {"Value": str}, total=False)


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
    pass


ResourceViolationTypeDef = TypedDict(
    "ResourceViolationTypeDef",
    {
        "AwsVPCSecurityGroupViolation": "AwsVPCSecurityGroupViolationTypeDef",
        "AwsEc2NetworkInterfaceViolation": "AwsEc2NetworkInterfaceViolationTypeDef",
        "AwsEc2InstanceViolation": "AwsEc2InstanceViolationTypeDef",
        "NetworkFirewallMissingFirewallViolation": "NetworkFirewallMissingFirewallViolationTypeDef",
        "NetworkFirewallMissingSubnetViolation": "NetworkFirewallMissingSubnetViolationTypeDef",
        "NetworkFirewallMissingExpectedRTViolation": "NetworkFirewallMissingExpectedRTViolationTypeDef",
        "NetworkFirewallPolicyModifiedViolation": "NetworkFirewallPolicyModifiedViolationTypeDef",
    },
    total=False,
)

SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": Literal["REMOVE", "MODIFY"],
        "Description": str,
        "RemediationResult": "SecurityGroupRuleDescriptionTypeDef",
        "IsDefaultAction": bool,
    },
    total=False,
)

SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": str,
        "IPV6Range": str,
        "PrefixListId": str,
        "Protocol": str,
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

_RequiredSecurityServicePolicyDataTypeDef = TypedDict(
    "_RequiredSecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "WAFV2",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
            "NETWORK_FIREWALL",
        ]
    },
)
_OptionalSecurityServicePolicyDataTypeDef = TypedDict(
    "_OptionalSecurityServicePolicyDataTypeDef", {"ManagedServiceData": str}, total=False
)


class SecurityServicePolicyDataTypeDef(
    _RequiredSecurityServicePolicyDataTypeDef, _OptionalSecurityServicePolicyDataTypeDef
):
    pass


StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef", {"RuleGroupName": str, "ResourceId": str}, total=False
)

StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {"RuleGroupName": str, "ResourceId": str, "Priority": int},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredViolationDetailTypeDef = TypedDict(
    "_RequiredViolationDetailTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceViolations": List["ResourceViolationTypeDef"],
    },
)
_OptionalViolationDetailTypeDef = TypedDict(
    "_OptionalViolationDetailTypeDef",
    {"ResourceTags": List["TagTypeDef"], "ResourceDescription": str},
    total=False,
)


class ViolationDetailTypeDef(_RequiredViolationDetailTypeDef, _OptionalViolationDetailTypeDef):
    pass


GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": Literal["READY", "CREATING", "PENDING_DELETION", "DELETING", "DELETED"],
    },
    total=False,
)

GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {"AppsList": "AppsListDataTypeDef", "AppsListArn": str},
    total=False,
)

GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {"PolicyComplianceDetail": "PolicyComplianceDetailTypeDef"},
    total=False,
)

GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef", {"SnsTopicArn": str, "SnsRoleName": str}, total=False
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef", {"Policy": "PolicyTypeDef", "PolicyArn": str}, total=False
)

GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": Literal[
            "WAF",
            "WAFV2",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
            "NETWORK_FIREWALL",
        ],
        "Data": str,
        "NextToken": str,
    },
    total=False,
)

GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {"ProtocolsList": "ProtocolsListDataTypeDef", "ProtocolsListArn": str},
    total=False,
)

GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef", {"ViolationDetail": "ViolationDetailTypeDef"}, total=False
)

ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {"AppsLists": List["AppsListDataSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {"PolicyComplianceStatusList": List["PolicyComplianceStatusTypeDef"], "NextToken": str},
    total=False,
)

ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {"MemberAccounts": List[str], "NextToken": str},
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {"PolicyList": List["PolicySummaryTypeDef"], "NextToken": str},
    total=False,
)

ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {"ProtocolsLists": List["ProtocolsListDataSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {"AppsList": "AppsListDataTypeDef", "AppsListArn": str},
    total=False,
)

PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef", {"Policy": "PolicyTypeDef", "PolicyArn": str}, total=False
)

PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {"ProtocolsList": "ProtocolsListDataTypeDef", "ProtocolsListArn": str},
    total=False,
)
