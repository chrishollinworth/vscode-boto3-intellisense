"""
Type annotations for fms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fms.type_defs import AccountScopeTypeDef

    data: AccountScopeTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccountRoleStatusType,
    CustomerPolicyScopeIdTypeType,
    CustomerPolicyStatusType,
    DependentServiceNameType,
    DestinationTypeType,
    EntryTypeType,
    EntryViolationReasonType,
    FailedItemReasonType,
    FirewallDeploymentModelType,
    MarketplaceSubscriptionOnboardingStatusType,
    NetworkAclRuleActionType,
    OrganizationStatusType,
    PolicyComplianceStatusTypeType,
    RemediationActionTypeType,
    ResourceSetStatusType,
    RuleOrderType,
    SecurityServiceTypeType,
    StreamExceptionPolicyType,
    TargetTypeType,
    ThirdPartyFirewallAssociationStatusType,
    ThirdPartyFirewallType,
    ViolationReasonType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountScopeTypeDef",
    "ActionTargetTypeDef",
    "AdminAccountSummaryTypeDef",
    "AdminScopeTypeDef",
    "AppTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "AssociateAdminAccountRequestRequestTypeDef",
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    "AssociateThirdPartyFirewallResponseTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "BatchAssociateResourceRequestRequestTypeDef",
    "BatchAssociateResourceResponseTypeDef",
    "BatchDisassociateResourceRequestRequestTypeDef",
    "BatchDisassociateResourceResponseTypeDef",
    "ComplianceViolatorTypeDef",
    "CreateNetworkAclActionTypeDef",
    "CreateNetworkAclEntriesActionTypeDef",
    "DeleteAppsListRequestRequestTypeDef",
    "DeleteNetworkAclEntriesActionTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeleteProtocolsListRequestRequestTypeDef",
    "DeleteResourceSetRequestRequestTypeDef",
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    "DisassociateThirdPartyFirewallResponseTypeDef",
    "DiscoveredResourceTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EC2AssociateRouteTableActionTypeDef",
    "EC2CopyRouteTableActionTypeDef",
    "EC2CreateRouteActionTypeDef",
    "EC2CreateRouteTableActionTypeDef",
    "EC2DeleteRouteActionTypeDef",
    "EC2ReplaceRouteActionTypeDef",
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    "EntryDescriptionTypeDef",
    "EntryViolationTypeDef",
    "EvaluationResultTypeDef",
    "ExpectedRouteTypeDef",
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    "FailedItemTypeDef",
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetAdminScopeRequestRequestTypeDef",
    "GetAdminScopeResponseTypeDef",
    "GetAppsListRequestRequestTypeDef",
    "GetAppsListResponseTypeDef",
    "GetComplianceDetailRequestRequestTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProtectionStatusRequestRequestTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetProtocolsListRequestRequestTypeDef",
    "GetProtocolsListResponseTypeDef",
    "GetResourceSetRequestRequestTypeDef",
    "GetResourceSetResponseTypeDef",
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    "GetViolationDetailsRequestRequestTypeDef",
    "GetViolationDetailsResponseTypeDef",
    "InvalidNetworkAclEntriesViolationTypeDef",
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    "ListAdminAccountsForOrganizationResponseTypeDef",
    "ListAdminsManagingAccountRequestRequestTypeDef",
    "ListAdminsManagingAccountResponseTypeDef",
    "ListAppsListsRequestRequestTypeDef",
    "ListAppsListsResponseTypeDef",
    "ListComplianceStatusRequestRequestTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsRequestRequestTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListResourceSetResourcesRequestRequestTypeDef",
    "ListResourceSetResourcesResponseTypeDef",
    "ListResourceSetsRequestRequestTypeDef",
    "ListResourceSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    "NetworkAclCommonPolicyTypeDef",
    "NetworkAclEntrySetTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkAclIcmpTypeCodeTypeDef",
    "NetworkAclPortRangeTypeDef",
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "NetworkFirewallPolicyTypeDef",
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    "OrganizationalUnitScopeTypeDef",
    "PaginatorConfigTypeDef",
    "PartialMatchTypeDef",
    "PolicyComplianceDetailTypeDef",
    "PolicyComplianceStatusTypeDef",
    "PolicyOptionTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTypeDef",
    "PolicyTypeScopeTypeDef",
    "PossibleRemediationActionTypeDef",
    "PossibleRemediationActionsTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ProtocolsListDataTypeDef",
    "PutAdminAccountRequestRequestTypeDef",
    "PutAppsListRequestRequestTypeDef",
    "PutAppsListResponseTypeDef",
    "PutNotificationChannelRequestRequestTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "PutPolicyResponseTypeDef",
    "PutProtocolsListRequestRequestTypeDef",
    "PutProtocolsListResponseTypeDef",
    "PutResourceSetRequestRequestTypeDef",
    "PutResourceSetResponseTypeDef",
    "RegionScopeTypeDef",
    "RemediationActionTypeDef",
    "RemediationActionWithOrderTypeDef",
    "ReplaceNetworkAclAssociationActionTypeDef",
    "ResourceSetSummaryTypeDef",
    "ResourceSetTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResourceViolationTypeDef",
    "ResponseMetadataTypeDef",
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    "RouteTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatefulRuleGroupTypeDef",
    "StatelessRuleGroupTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    "ThirdPartyFirewallPolicyTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ViolationDetailTypeDef",
)

AccountScopeTypeDef = TypedDict(
    "AccountScopeTypeDef",
    {
        "Accounts": List[str],
        "AllAccountsEnabled": bool,
        "ExcludeSpecifiedAccounts": bool,
    },
    total=False,
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ResourceId": str,
        "Description": str,
    },
    total=False,
)

AdminAccountSummaryTypeDef = TypedDict(
    "AdminAccountSummaryTypeDef",
    {
        "AdminAccount": str,
        "DefaultAdmin": bool,
        "Status": OrganizationStatusType,
    },
    total=False,
)

AdminScopeTypeDef = TypedDict(
    "AdminScopeTypeDef",
    {
        "AccountScope": "AccountScopeTypeDef",
        "OrganizationalUnitScope": "OrganizationalUnitScopeTypeDef",
        "RegionScope": "RegionScopeTypeDef",
        "PolicyTypeScope": "PolicyTypeScopeTypeDef",
    },
    total=False,
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppName": str,
        "Protocol": str,
        "Port": int,
    },
)

AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {
        "ListArn": str,
        "ListId": str,
        "ListName": str,
        "AppsList": List["AppTypeDef"],
    },
    total=False,
)

_RequiredAppsListDataTypeDef = TypedDict(
    "_RequiredAppsListDataTypeDef",
    {
        "ListName": str,
        "AppsList": List["AppTypeDef"],
    },
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

AssociateAdminAccountRequestRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)

AssociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)

AssociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "AssociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
    {
        "ViolationTarget": str,
        "ViolatingSecurityGroups": List[str],
    },
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

BatchAssociateResourceRequestRequestTypeDef = TypedDict(
    "BatchAssociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": List[str],
    },
)

BatchAssociateResourceResponseTypeDef = TypedDict(
    "BatchAssociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List["FailedItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateResourceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": List[str],
    },
)

BatchDisassociateResourceResponseTypeDef = TypedDict(
    "BatchDisassociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List["FailedItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": str,
        "ViolationReason": ViolationReasonType,
        "ResourceType": str,
        "Metadata": Dict[str, str],
    },
    total=False,
)

CreateNetworkAclActionTypeDef = TypedDict(
    "CreateNetworkAclActionTypeDef",
    {
        "Description": str,
        "Vpc": "ActionTargetTypeDef",
        "FMSCanRemediate": bool,
    },
    total=False,
)

CreateNetworkAclEntriesActionTypeDef = TypedDict(
    "CreateNetworkAclEntriesActionTypeDef",
    {
        "Description": str,
        "NetworkAclId": "ActionTargetTypeDef",
        "NetworkAclEntriesToBeCreated": List["EntryDescriptionTypeDef"],
        "FMSCanRemediate": bool,
    },
    total=False,
)

DeleteAppsListRequestRequestTypeDef = TypedDict(
    "DeleteAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

DeleteNetworkAclEntriesActionTypeDef = TypedDict(
    "DeleteNetworkAclEntriesActionTypeDef",
    {
        "Description": str,
        "NetworkAclId": "ActionTargetTypeDef",
        "NetworkAclEntriesToBeDeleted": List["EntryDescriptionTypeDef"],
        "FMSCanRemediate": bool,
    },
    total=False,
)

_RequiredDeletePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalDeletePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePolicyRequestRequestTypeDef",
    {
        "DeleteAllPolicyResources": bool,
    },
    total=False,
)

class DeletePolicyRequestRequestTypeDef(
    _RequiredDeletePolicyRequestRequestTypeDef, _OptionalDeletePolicyRequestRequestTypeDef
):
    pass

DeleteProtocolsListRequestRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

DeleteResourceSetRequestRequestTypeDef = TypedDict(
    "DeleteResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DisassociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)

DisassociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscoveredResourceTypeDef = TypedDict(
    "DiscoveredResourceTypeDef",
    {
        "URI": str,
        "AccountId": str,
        "Type": str,
        "Name": str,
    },
    total=False,
)

DnsDuplicateRuleGroupViolationTypeDef = TypedDict(
    "DnsDuplicateRuleGroupViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
    },
    total=False,
)

DnsRuleGroupLimitExceededViolationTypeDef = TypedDict(
    "DnsRuleGroupLimitExceededViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "NumberOfRuleGroupsAlreadyAssociated": int,
    },
    total=False,
)

DnsRuleGroupPriorityConflictViolationTypeDef = TypedDict(
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "ConflictingPriority": int,
        "ConflictingPolicyId": str,
        "UnavailablePriorities": List[int],
    },
    total=False,
)

_RequiredEC2AssociateRouteTableActionTypeDef = TypedDict(
    "_RequiredEC2AssociateRouteTableActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
    },
)
_OptionalEC2AssociateRouteTableActionTypeDef = TypedDict(
    "_OptionalEC2AssociateRouteTableActionTypeDef",
    {
        "Description": str,
        "SubnetId": "ActionTargetTypeDef",
        "GatewayId": "ActionTargetTypeDef",
    },
    total=False,
)

class EC2AssociateRouteTableActionTypeDef(
    _RequiredEC2AssociateRouteTableActionTypeDef, _OptionalEC2AssociateRouteTableActionTypeDef
):
    pass

_RequiredEC2CopyRouteTableActionTypeDef = TypedDict(
    "_RequiredEC2CopyRouteTableActionTypeDef",
    {
        "VpcId": "ActionTargetTypeDef",
        "RouteTableId": "ActionTargetTypeDef",
    },
)
_OptionalEC2CopyRouteTableActionTypeDef = TypedDict(
    "_OptionalEC2CopyRouteTableActionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class EC2CopyRouteTableActionTypeDef(
    _RequiredEC2CopyRouteTableActionTypeDef, _OptionalEC2CopyRouteTableActionTypeDef
):
    pass

_RequiredEC2CreateRouteActionTypeDef = TypedDict(
    "_RequiredEC2CreateRouteActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
    },
)
_OptionalEC2CreateRouteActionTypeDef = TypedDict(
    "_OptionalEC2CreateRouteActionTypeDef",
    {
        "Description": str,
        "DestinationCidrBlock": str,
        "DestinationPrefixListId": str,
        "DestinationIpv6CidrBlock": str,
        "VpcEndpointId": "ActionTargetTypeDef",
        "GatewayId": "ActionTargetTypeDef",
    },
    total=False,
)

class EC2CreateRouteActionTypeDef(
    _RequiredEC2CreateRouteActionTypeDef, _OptionalEC2CreateRouteActionTypeDef
):
    pass

_RequiredEC2CreateRouteTableActionTypeDef = TypedDict(
    "_RequiredEC2CreateRouteTableActionTypeDef",
    {
        "VpcId": "ActionTargetTypeDef",
    },
)
_OptionalEC2CreateRouteTableActionTypeDef = TypedDict(
    "_OptionalEC2CreateRouteTableActionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class EC2CreateRouteTableActionTypeDef(
    _RequiredEC2CreateRouteTableActionTypeDef, _OptionalEC2CreateRouteTableActionTypeDef
):
    pass

_RequiredEC2DeleteRouteActionTypeDef = TypedDict(
    "_RequiredEC2DeleteRouteActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
    },
)
_OptionalEC2DeleteRouteActionTypeDef = TypedDict(
    "_OptionalEC2DeleteRouteActionTypeDef",
    {
        "Description": str,
        "DestinationCidrBlock": str,
        "DestinationPrefixListId": str,
        "DestinationIpv6CidrBlock": str,
    },
    total=False,
)

class EC2DeleteRouteActionTypeDef(
    _RequiredEC2DeleteRouteActionTypeDef, _OptionalEC2DeleteRouteActionTypeDef
):
    pass

_RequiredEC2ReplaceRouteActionTypeDef = TypedDict(
    "_RequiredEC2ReplaceRouteActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
    },
)
_OptionalEC2ReplaceRouteActionTypeDef = TypedDict(
    "_OptionalEC2ReplaceRouteActionTypeDef",
    {
        "Description": str,
        "DestinationCidrBlock": str,
        "DestinationPrefixListId": str,
        "DestinationIpv6CidrBlock": str,
        "GatewayId": "ActionTargetTypeDef",
    },
    total=False,
)

class EC2ReplaceRouteActionTypeDef(
    _RequiredEC2ReplaceRouteActionTypeDef, _OptionalEC2ReplaceRouteActionTypeDef
):
    pass

_RequiredEC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "_RequiredEC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "AssociationId": "ActionTargetTypeDef",
        "RouteTableId": "ActionTargetTypeDef",
    },
)
_OptionalEC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "_OptionalEC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class EC2ReplaceRouteTableAssociationActionTypeDef(
    _RequiredEC2ReplaceRouteTableAssociationActionTypeDef,
    _OptionalEC2ReplaceRouteTableAssociationActionTypeDef,
):
    pass

EntryDescriptionTypeDef = TypedDict(
    "EntryDescriptionTypeDef",
    {
        "EntryDetail": "NetworkAclEntryTypeDef",
        "EntryRuleNumber": int,
        "EntryType": EntryTypeType,
    },
    total=False,
)

EntryViolationTypeDef = TypedDict(
    "EntryViolationTypeDef",
    {
        "ExpectedEntry": "EntryDescriptionTypeDef",
        "ExpectedEvaluationOrder": str,
        "ActualEvaluationOrder": str,
        "EntryAtExpectedEvaluationOrder": "EntryDescriptionTypeDef",
        "EntriesWithConflicts": List["EntryDescriptionTypeDef"],
        "EntryViolationReasons": List[EntryViolationReasonType],
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": PolicyComplianceStatusTypeType,
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

ExpectedRouteTypeDef = TypedDict(
    "ExpectedRouteTypeDef",
    {
        "IpV4Cidr": str,
        "PrefixListId": str,
        "IpV6Cidr": str,
        "ContributingSubnets": List[str],
        "AllowedTargets": List[str],
        "RouteTableId": str,
    },
    total=False,
)

FMSPolicyUpdateFirewallCreationConfigActionTypeDef = TypedDict(
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    {
        "Description": str,
        "FirewallCreationConfig": str,
    },
    total=False,
)

FailedItemTypeDef = TypedDict(
    "FailedItemTypeDef",
    {
        "URI": str,
        "Reason": FailedItemReasonType,
    },
    total=False,
)

FirewallSubnetIsOutOfScopeViolationTypeDef = TypedDict(
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    {
        "FirewallSubnetId": str,
        "VpcId": str,
        "SubnetAvailabilityZone": str,
        "SubnetAvailabilityZoneId": str,
        "VpcEndpointId": str,
    },
    total=False,
)

FirewallSubnetMissingVPCEndpointViolationTypeDef = TypedDict(
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    {
        "FirewallSubnetId": str,
        "VpcId": str,
        "SubnetAvailabilityZone": str,
        "SubnetAvailabilityZoneId": str,
    },
    total=False,
)

GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAdminScopeRequestRequestTypeDef = TypedDict(
    "GetAdminScopeRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)

GetAdminScopeResponseTypeDef = TypedDict(
    "GetAdminScopeResponseTypeDef",
    {
        "AdminScope": "AdminScopeTypeDef",
        "Status": OrganizationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAppsListRequestRequestTypeDef = TypedDict(
    "_RequiredGetAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetAppsListRequestRequestTypeDef = TypedDict(
    "_OptionalGetAppsListRequestRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)

class GetAppsListRequestRequestTypeDef(
    _RequiredGetAppsListRequestRequestTypeDef, _OptionalGetAppsListRequestRequestTypeDef
):
    pass

GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceDetailRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)

GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": "PolicyComplianceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProtectionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetProtectionStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalGetProtectionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetProtectionStatusRequestRequestTypeDef",
    {
        "MemberAccountId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetProtectionStatusRequestRequestTypeDef(
    _RequiredGetProtectionStatusRequestRequestTypeDef,
    _OptionalGetProtectionStatusRequestRequestTypeDef,
):
    pass

GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProtocolsListRequestRequestTypeDef = TypedDict(
    "_RequiredGetProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetProtocolsListRequestRequestTypeDef = TypedDict(
    "_OptionalGetProtocolsListRequestRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)

class GetProtocolsListRequestRequestTypeDef(
    _RequiredGetProtocolsListRequestRequestTypeDef, _OptionalGetProtocolsListRequestRequestTypeDef
):
    pass

GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceSetRequestRequestTypeDef = TypedDict(
    "GetResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetResourceSetResponseTypeDef = TypedDict(
    "GetResourceSetResponseTypeDef",
    {
        "ResourceSet": "ResourceSetTypeDef",
        "ResourceSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)

GetThirdPartyFirewallAssociationStatusResponseTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "MarketplaceOnboardingStatus": MarketplaceSubscriptionOnboardingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetViolationDetailsRequestRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)

GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef",
    {
        "ViolationDetail": "ViolationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvalidNetworkAclEntriesViolationTypeDef = TypedDict(
    "InvalidNetworkAclEntriesViolationTypeDef",
    {
        "Vpc": str,
        "Subnet": str,
        "SubnetAvailabilityZone": str,
        "CurrentAssociatedNetworkAcl": str,
        "EntryViolations": List["EntryViolationTypeDef"],
    },
    total=False,
)

ListAdminAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAdminAccountsForOrganizationResponseTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAdminsManagingAccountRequestRequestTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAdminsManagingAccountResponseTypeDef = TypedDict(
    "ListAdminsManagingAccountResponseTypeDef",
    {
        "AdminAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppsListsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListAppsListsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppsListsRequestRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)

class ListAppsListsRequestRequestTypeDef(
    _RequiredListAppsListsRequestRequestTypeDef, _OptionalListAppsListsRequestRequestTypeDef
):
    pass

ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {
        "AppsLists": List["AppsListDataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComplianceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListComplianceStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalListComplianceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListComplianceStatusRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListComplianceStatusRequestRequestTypeDef(
    _RequiredListComplianceStatusRequestRequestTypeDef,
    _OptionalListComplianceStatusRequestRequestTypeDef,
):
    pass

ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List["PolicyComplianceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestRequestTypeDef",
    {
        "MemberAccountIds": List[str],
        "ResourceType": str,
    },
)
_OptionalListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListDiscoveredResourcesRequestRequestTypeDef,
):
    pass

ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "Items": List["DiscoveredResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "PolicyList": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProtocolsListsRequestRequestTypeDef = TypedDict(
    "_RequiredListProtocolsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListProtocolsListsRequestRequestTypeDef = TypedDict(
    "_OptionalListProtocolsListsRequestRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)

class ListProtocolsListsRequestRequestTypeDef(
    _RequiredListProtocolsListsRequestRequestTypeDef,
    _OptionalListProtocolsListsRequestRequestTypeDef,
):
    pass

ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {
        "ProtocolsLists": List["ProtocolsListDataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceSetResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceSetResourcesRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalListResourceSetResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceSetResourcesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListResourceSetResourcesRequestRequestTypeDef(
    _RequiredListResourceSetResourcesRequestRequestTypeDef,
    _OptionalListResourceSetResourcesRequestRequestTypeDef,
):
    pass

ListResourceSetResourcesResponseTypeDef = TypedDict(
    "ListResourceSetResourcesResponseTypeDef",
    {
        "Items": List["ResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceSetsRequestRequestTypeDef = TypedDict(
    "ListResourceSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListResourceSetsResponseTypeDef = TypedDict(
    "ListResourceSetsResponseTypeDef",
    {
        "ResourceSets": List["ResourceSetSummaryTypeDef"],
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

_RequiredListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
        "MaxResults": int,
    },
)
_OptionalListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef(
    _RequiredListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef,
    _OptionalListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef,
):
    pass

ListThirdPartyFirewallFirewallPoliciesResponseTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    {
        "ThirdPartyFirewallFirewallPolicies": List["ThirdPartyFirewallFirewallPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkAclCommonPolicyTypeDef = TypedDict(
    "NetworkAclCommonPolicyTypeDef",
    {
        "NetworkAclEntrySet": "NetworkAclEntrySetTypeDef",
    },
)

_RequiredNetworkAclEntrySetTypeDef = TypedDict(
    "_RequiredNetworkAclEntrySetTypeDef",
    {
        "ForceRemediateForFirstEntries": bool,
        "ForceRemediateForLastEntries": bool,
    },
)
_OptionalNetworkAclEntrySetTypeDef = TypedDict(
    "_OptionalNetworkAclEntrySetTypeDef",
    {
        "FirstEntries": List["NetworkAclEntryTypeDef"],
        "LastEntries": List["NetworkAclEntryTypeDef"],
    },
    total=False,
)

class NetworkAclEntrySetTypeDef(
    _RequiredNetworkAclEntrySetTypeDef, _OptionalNetworkAclEntrySetTypeDef
):
    pass

_RequiredNetworkAclEntryTypeDef = TypedDict(
    "_RequiredNetworkAclEntryTypeDef",
    {
        "Protocol": str,
        "RuleAction": NetworkAclRuleActionType,
        "Egress": bool,
    },
)
_OptionalNetworkAclEntryTypeDef = TypedDict(
    "_OptionalNetworkAclEntryTypeDef",
    {
        "IcmpTypeCode": "NetworkAclIcmpTypeCodeTypeDef",
        "PortRange": "NetworkAclPortRangeTypeDef",
        "CidrBlock": str,
        "Ipv6CidrBlock": str,
    },
    total=False,
)

class NetworkAclEntryTypeDef(_RequiredNetworkAclEntryTypeDef, _OptionalNetworkAclEntryTypeDef):
    pass

NetworkAclIcmpTypeCodeTypeDef = TypedDict(
    "NetworkAclIcmpTypeCodeTypeDef",
    {
        "Code": int,
        "Type": int,
    },
    total=False,
)

NetworkAclPortRangeTypeDef = TypedDict(
    "NetworkAclPortRangeTypeDef",
    {
        "From": int,
        "To": int,
    },
    total=False,
)

NetworkFirewallBlackHoleRouteDetectedViolationTypeDef = TypedDict(
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    {
        "ViolationTarget": str,
        "RouteTableId": str,
        "VpcId": str,
        "ViolatingRoutes": List["RouteTypeDef"],
    },
    total=False,
)

NetworkFirewallInternetTrafficNotInspectedViolationTypeDef = TypedDict(
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    {
        "SubnetId": str,
        "SubnetAvailabilityZone": str,
        "RouteTableId": str,
        "ViolatingRoutes": List["RouteTypeDef"],
        "IsRouteTableUsedInDifferentAZ": bool,
        "CurrentFirewallSubnetRouteTable": str,
        "ExpectedFirewallEndpoint": str,
        "FirewallSubnetId": str,
        "ExpectedFirewallSubnetRoutes": List["ExpectedRouteTypeDef"],
        "ActualFirewallSubnetRoutes": List["RouteTypeDef"],
        "InternetGatewayId": str,
        "CurrentInternetGatewayRouteTable": str,
        "ExpectedInternetGatewayRoutes": List["ExpectedRouteTypeDef"],
        "ActualInternetGatewayRoutes": List["RouteTypeDef"],
        "VpcId": str,
    },
    total=False,
)

NetworkFirewallInvalidRouteConfigurationViolationTypeDef = TypedDict(
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    {
        "AffectedSubnets": List[str],
        "RouteTableId": str,
        "IsRouteTableUsedInDifferentAZ": bool,
        "ViolatingRoute": "RouteTypeDef",
        "CurrentFirewallSubnetRouteTable": str,
        "ExpectedFirewallEndpoint": str,
        "ActualFirewallEndpoint": str,
        "ExpectedFirewallSubnetId": str,
        "ActualFirewallSubnetId": str,
        "ExpectedFirewallSubnetRoutes": List["ExpectedRouteTypeDef"],
        "ActualFirewallSubnetRoutes": List["RouteTypeDef"],
        "InternetGatewayId": str,
        "CurrentInternetGatewayRouteTable": str,
        "ExpectedInternetGatewayRoutes": List["ExpectedRouteTypeDef"],
        "ActualInternetGatewayRoutes": List["RouteTypeDef"],
        "VpcId": str,
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

NetworkFirewallMissingExpectedRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    {
        "ViolationTarget": str,
        "ExpectedRoutes": List["ExpectedRouteTypeDef"],
        "VpcId": str,
    },
    total=False,
)

NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
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
        "StatefulDefaultActions": List[str],
        "StatefulEngineOptions": "StatefulEngineOptionsTypeDef",
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

NetworkFirewallPolicyTypeDef = TypedDict(
    "NetworkFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": FirewallDeploymentModelType,
    },
    total=False,
)

NetworkFirewallStatefulRuleGroupOverrideTypeDef = TypedDict(
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    {
        "Action": Literal["DROP_TO_ALERT"],
    },
    total=False,
)

NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    {
        "FirewallSubnetId": str,
        "ViolatingRoutes": List["RouteTypeDef"],
        "RouteTableId": str,
        "FirewallEndpoint": str,
        "VpcId": str,
    },
    total=False,
)

NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    {
        "GatewayId": str,
        "ViolatingRoutes": List["RouteTypeDef"],
        "RouteTableId": str,
        "VpcId": str,
    },
    total=False,
)

OrganizationalUnitScopeTypeDef = TypedDict(
    "OrganizationalUnitScopeTypeDef",
    {
        "OrganizationalUnits": List[str],
        "AllOrganizationalUnitsEnabled": bool,
        "ExcludeSpecifiedOrganizationalUnits": bool,
    },
    total=False,
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

PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef",
    {
        "Reference": str,
        "TargetViolationReasons": List[str],
    },
    total=False,
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
        "IssueInfoMap": Dict[DependentServiceNameType, str],
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
        "IssueInfoMap": Dict[DependentServiceNameType, str],
    },
    total=False,
)

PolicyOptionTypeDef = TypedDict(
    "PolicyOptionTypeDef",
    {
        "NetworkFirewallPolicy": "NetworkFirewallPolicyTypeDef",
        "ThirdPartyFirewallPolicy": "ThirdPartyFirewallPolicyTypeDef",
        "NetworkAclCommonPolicy": "NetworkAclCommonPolicyTypeDef",
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
        "SecurityServiceType": SecurityServiceTypeType,
        "RemediationEnabled": bool,
        "DeleteUnusedFMManagedResources": bool,
        "PolicyStatus": CustomerPolicyStatusType,
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
        "DeleteUnusedFMManagedResources": bool,
        "IncludeMap": Dict[CustomerPolicyScopeIdTypeType, List[str]],
        "ExcludeMap": Dict[CustomerPolicyScopeIdTypeType, List[str]],
        "ResourceSetIds": List[str],
        "PolicyDescription": str,
        "PolicyStatus": CustomerPolicyStatusType,
    },
    total=False,
)

class PolicyTypeDef(_RequiredPolicyTypeDef, _OptionalPolicyTypeDef):
    pass

PolicyTypeScopeTypeDef = TypedDict(
    "PolicyTypeScopeTypeDef",
    {
        "PolicyTypes": List[SecurityServiceTypeType],
        "AllPolicyTypesEnabled": bool,
    },
    total=False,
)

_RequiredPossibleRemediationActionTypeDef = TypedDict(
    "_RequiredPossibleRemediationActionTypeDef",
    {
        "OrderedRemediationActions": List["RemediationActionWithOrderTypeDef"],
    },
)
_OptionalPossibleRemediationActionTypeDef = TypedDict(
    "_OptionalPossibleRemediationActionTypeDef",
    {
        "Description": str,
        "IsDefaultAction": bool,
    },
    total=False,
)

class PossibleRemediationActionTypeDef(
    _RequiredPossibleRemediationActionTypeDef, _OptionalPossibleRemediationActionTypeDef
):
    pass

PossibleRemediationActionsTypeDef = TypedDict(
    "PossibleRemediationActionsTypeDef",
    {
        "Description": str,
        "Actions": List["PossibleRemediationActionTypeDef"],
    },
    total=False,
)

ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {
        "ListArn": str,
        "ListId": str,
        "ListName": str,
        "ProtocolsList": List[str],
    },
    total=False,
)

_RequiredProtocolsListDataTypeDef = TypedDict(
    "_RequiredProtocolsListDataTypeDef",
    {
        "ListName": str,
        "ProtocolsList": List[str],
    },
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

_RequiredPutAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredPutAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)
_OptionalPutAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalPutAdminAccountRequestRequestTypeDef",
    {
        "AdminScope": "AdminScopeTypeDef",
    },
    total=False,
)

class PutAdminAccountRequestRequestTypeDef(
    _RequiredPutAdminAccountRequestRequestTypeDef, _OptionalPutAdminAccountRequestRequestTypeDef
):
    pass

_RequiredPutAppsListRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppsListRequestRequestTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
    },
)
_OptionalPutAppsListRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppsListRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class PutAppsListRequestRequestTypeDef(
    _RequiredPutAppsListRequestRequestTypeDef, _OptionalPutAppsListRequestRequestTypeDef
):
    pass

PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutNotificationChannelRequestRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)

_RequiredPutPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutPolicyRequestRequestTypeDef",
    {
        "Policy": "PolicyTypeDef",
    },
)
_OptionalPutPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutPolicyRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class PutPolicyRequestRequestTypeDef(
    _RequiredPutPolicyRequestRequestTypeDef, _OptionalPutPolicyRequestRequestTypeDef
):
    pass

PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutProtocolsListRequestRequestTypeDef = TypedDict(
    "_RequiredPutProtocolsListRequestRequestTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
    },
)
_OptionalPutProtocolsListRequestRequestTypeDef = TypedDict(
    "_OptionalPutProtocolsListRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class PutProtocolsListRequestRequestTypeDef(
    _RequiredPutProtocolsListRequestRequestTypeDef, _OptionalPutProtocolsListRequestRequestTypeDef
):
    pass

PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutResourceSetRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourceSetRequestRequestTypeDef",
    {
        "ResourceSet": "ResourceSetTypeDef",
    },
)
_OptionalPutResourceSetRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourceSetRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class PutResourceSetRequestRequestTypeDef(
    _RequiredPutResourceSetRequestRequestTypeDef, _OptionalPutResourceSetRequestRequestTypeDef
):
    pass

PutResourceSetResponseTypeDef = TypedDict(
    "PutResourceSetResponseTypeDef",
    {
        "ResourceSet": "ResourceSetTypeDef",
        "ResourceSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionScopeTypeDef = TypedDict(
    "RegionScopeTypeDef",
    {
        "Regions": List[str],
        "AllRegionsEnabled": bool,
    },
    total=False,
)

RemediationActionTypeDef = TypedDict(
    "RemediationActionTypeDef",
    {
        "Description": str,
        "EC2CreateRouteAction": "EC2CreateRouteActionTypeDef",
        "EC2ReplaceRouteAction": "EC2ReplaceRouteActionTypeDef",
        "EC2DeleteRouteAction": "EC2DeleteRouteActionTypeDef",
        "EC2CopyRouteTableAction": "EC2CopyRouteTableActionTypeDef",
        "EC2ReplaceRouteTableAssociationAction": "EC2ReplaceRouteTableAssociationActionTypeDef",
        "EC2AssociateRouteTableAction": "EC2AssociateRouteTableActionTypeDef",
        "EC2CreateRouteTableAction": "EC2CreateRouteTableActionTypeDef",
        "FMSPolicyUpdateFirewallCreationConfigAction": "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
        "CreateNetworkAclAction": "CreateNetworkAclActionTypeDef",
        "ReplaceNetworkAclAssociationAction": "ReplaceNetworkAclAssociationActionTypeDef",
        "CreateNetworkAclEntriesAction": "CreateNetworkAclEntriesActionTypeDef",
        "DeleteNetworkAclEntriesAction": "DeleteNetworkAclEntriesActionTypeDef",
    },
    total=False,
)

RemediationActionWithOrderTypeDef = TypedDict(
    "RemediationActionWithOrderTypeDef",
    {
        "RemediationAction": "RemediationActionTypeDef",
        "Order": int,
    },
    total=False,
)

ReplaceNetworkAclAssociationActionTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationActionTypeDef",
    {
        "Description": str,
        "AssociationId": "ActionTargetTypeDef",
        "NetworkAclId": "ActionTargetTypeDef",
        "FMSCanRemediate": bool,
    },
    total=False,
)

ResourceSetSummaryTypeDef = TypedDict(
    "ResourceSetSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "LastUpdateTime": datetime,
        "ResourceSetStatus": ResourceSetStatusType,
    },
    total=False,
)

_RequiredResourceSetTypeDef = TypedDict(
    "_RequiredResourceSetTypeDef",
    {
        "Name": str,
        "ResourceTypeList": List[str],
    },
)
_OptionalResourceSetTypeDef = TypedDict(
    "_OptionalResourceSetTypeDef",
    {
        "Id": str,
        "Description": str,
        "UpdateToken": str,
        "LastUpdateTime": datetime,
        "ResourceSetStatus": ResourceSetStatusType,
    },
    total=False,
)

class ResourceSetTypeDef(_RequiredResourceSetTypeDef, _OptionalResourceSetTypeDef):
    pass

_RequiredResourceTagTypeDef = TypedDict(
    "_RequiredResourceTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalResourceTagTypeDef = TypedDict(
    "_OptionalResourceTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
    pass

_RequiredResourceTypeDef = TypedDict(
    "_RequiredResourceTypeDef",
    {
        "URI": str,
    },
)
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
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
        "NetworkFirewallInternetTrafficNotInspectedViolation": "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
        "NetworkFirewallInvalidRouteConfigurationViolation": "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
        "NetworkFirewallBlackHoleRouteDetectedViolation": "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
        "NetworkFirewallUnexpectedFirewallRoutesViolation": "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
        "NetworkFirewallUnexpectedGatewayRoutesViolation": "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
        "NetworkFirewallMissingExpectedRoutesViolation": "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
        "DnsRuleGroupPriorityConflictViolation": "DnsRuleGroupPriorityConflictViolationTypeDef",
        "DnsDuplicateRuleGroupViolation": "DnsDuplicateRuleGroupViolationTypeDef",
        "DnsRuleGroupLimitExceededViolation": "DnsRuleGroupLimitExceededViolationTypeDef",
        "FirewallSubnetIsOutOfScopeViolation": "FirewallSubnetIsOutOfScopeViolationTypeDef",
        "RouteHasOutOfScopeEndpointViolation": "RouteHasOutOfScopeEndpointViolationTypeDef",
        "ThirdPartyFirewallMissingFirewallViolation": "ThirdPartyFirewallMissingFirewallViolationTypeDef",
        "ThirdPartyFirewallMissingSubnetViolation": "ThirdPartyFirewallMissingSubnetViolationTypeDef",
        "ThirdPartyFirewallMissingExpectedRouteTableViolation": "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
        "FirewallSubnetMissingVPCEndpointViolation": "FirewallSubnetMissingVPCEndpointViolationTypeDef",
        "InvalidNetworkAclEntriesViolation": "InvalidNetworkAclEntriesViolationTypeDef",
        "PossibleRemediationActions": "PossibleRemediationActionsTypeDef",
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

RouteHasOutOfScopeEndpointViolationTypeDef = TypedDict(
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    {
        "SubnetId": str,
        "VpcId": str,
        "RouteTableId": str,
        "ViolatingRoutes": List["RouteTypeDef"],
        "SubnetAvailabilityZone": str,
        "SubnetAvailabilityZoneId": str,
        "CurrentFirewallSubnetRouteTable": str,
        "FirewallSubnetId": str,
        "FirewallSubnetRoutes": List["RouteTypeDef"],
        "InternetGatewayId": str,
        "CurrentInternetGatewayRouteTable": str,
        "InternetGatewayRoutes": List["RouteTypeDef"],
    },
    total=False,
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationType": DestinationTypeType,
        "TargetType": TargetTypeType,
        "Destination": str,
        "Target": str,
    },
    total=False,
)

SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": RemediationActionTypeType,
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
        "Type": SecurityServiceTypeType,
    },
)
_OptionalSecurityServicePolicyDataTypeDef = TypedDict(
    "_OptionalSecurityServicePolicyDataTypeDef",
    {
        "ManagedServiceData": str,
        "PolicyOption": "PolicyOptionTypeDef",
    },
    total=False,
)

class SecurityServicePolicyDataTypeDef(
    _RequiredSecurityServicePolicyDataTypeDef, _OptionalSecurityServicePolicyDataTypeDef
):
    pass

StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": RuleOrderType,
        "StreamExceptionPolicy": StreamExceptionPolicyType,
    },
    total=False,
)

StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef",
    {
        "RuleGroupName": str,
        "ResourceId": str,
        "Priority": int,
        "Override": "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    },
    total=False,
)

StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {
        "RuleGroupName": str,
        "ResourceId": str,
        "Priority": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ThirdPartyFirewallFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    {
        "FirewallPolicyId": str,
        "FirewallPolicyName": str,
    },
    total=False,
)

ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "CurrentRouteTable": str,
        "ExpectedRouteTable": str,
    },
    total=False,
)

ThirdPartyFirewallMissingFirewallViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

ThirdPartyFirewallMissingSubnetViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

ThirdPartyFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": FirewallDeploymentModelType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

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
    {
        "ResourceTags": List["TagTypeDef"],
        "ResourceDescription": str,
    },
    total=False,
)

class ViolationDetailTypeDef(_RequiredViolationDetailTypeDef, _OptionalViolationDetailTypeDef):
    pass
