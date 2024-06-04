"""
Type annotations for network-firewall service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/type_defs.html)

Usage::

    ```python
    from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef

    data: ActionDefinitionTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttachmentStatusType,
    ConfigurationSyncStateType,
    EncryptionTypeType,
    FirewallStatusValueType,
    GeneratedRulesTypeType,
    IdentifiedTypeType,
    IPAddressTypeType,
    LogDestinationTypeType,
    LogTypeType,
    PerObjectSyncStatusType,
    ResourceManagedStatusType,
    ResourceManagedTypeType,
    ResourceStatusType,
    RevocationCheckActionType,
    RuleGroupTypeType,
    RuleOrderType,
    StatefulActionType,
    StatefulRuleDirectionType,
    StatefulRuleProtocolType,
    StreamExceptionPolicyType,
    TargetTypeType,
    TCPFlagType,
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
    "ActionDefinitionTypeDef",
    "AddressTypeDef",
    "AnalysisResultTypeDef",
    "AssociateFirewallPolicyRequestRequestTypeDef",
    "AssociateFirewallPolicyResponseTypeDef",
    "AssociateSubnetsRequestRequestTypeDef",
    "AssociateSubnetsResponseTypeDef",
    "AttachmentTypeDef",
    "CIDRSummaryTypeDef",
    "CapacityUsageSummaryTypeDef",
    "CheckCertificateRevocationStatusActionsTypeDef",
    "CreateFirewallPolicyRequestRequestTypeDef",
    "CreateFirewallPolicyResponseTypeDef",
    "CreateFirewallRequestRequestTypeDef",
    "CreateFirewallResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateTLSInspectionConfigurationRequestRequestTypeDef",
    "CreateTLSInspectionConfigurationResponseTypeDef",
    "CustomActionTypeDef",
    "DeleteFirewallPolicyRequestRequestTypeDef",
    "DeleteFirewallPolicyResponseTypeDef",
    "DeleteFirewallRequestRequestTypeDef",
    "DeleteFirewallResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteTLSInspectionConfigurationRequestRequestTypeDef",
    "DeleteTLSInspectionConfigurationResponseTypeDef",
    "DescribeFirewallPolicyRequestRequestTypeDef",
    "DescribeFirewallPolicyResponseTypeDef",
    "DescribeFirewallRequestRequestTypeDef",
    "DescribeFirewallResponseTypeDef",
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRuleGroupMetadataRequestRequestTypeDef",
    "DescribeRuleGroupMetadataResponseTypeDef",
    "DescribeRuleGroupRequestRequestTypeDef",
    "DescribeRuleGroupResponseTypeDef",
    "DescribeTLSInspectionConfigurationRequestRequestTypeDef",
    "DescribeTLSInspectionConfigurationResponseTypeDef",
    "DimensionTypeDef",
    "DisassociateSubnetsRequestRequestTypeDef",
    "DisassociateSubnetsResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "FirewallMetadataTypeDef",
    "FirewallPolicyMetadataTypeDef",
    "FirewallPolicyResponseTypeDef",
    "FirewallPolicyTypeDef",
    "FirewallStatusTypeDef",
    "FirewallTypeDef",
    "HeaderTypeDef",
    "IPSetMetadataTypeDef",
    "IPSetReferenceTypeDef",
    "IPSetTypeDef",
    "ListFirewallPoliciesRequestRequestTypeDef",
    "ListFirewallPoliciesResponseTypeDef",
    "ListFirewallsRequestRequestTypeDef",
    "ListFirewallsResponseTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTLSInspectionConfigurationsRequestRequestTypeDef",
    "ListTLSInspectionConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogDestinationConfigTypeDef",
    "LoggingConfigurationTypeDef",
    "MatchAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PerObjectStatusTypeDef",
    "PolicyVariablesTypeDef",
    "PortRangeTypeDef",
    "PortSetTypeDef",
    "PublishMetricActionTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ReferenceSetsTypeDef",
    "ResponseMetadataTypeDef",
    "RuleDefinitionTypeDef",
    "RuleGroupMetadataTypeDef",
    "RuleGroupResponseTypeDef",
    "RuleGroupTypeDef",
    "RuleOptionTypeDef",
    "RuleVariablesTypeDef",
    "RulesSourceListTypeDef",
    "RulesSourceTypeDef",
    "ServerCertificateConfigurationTypeDef",
    "ServerCertificateScopeTypeDef",
    "ServerCertificateTypeDef",
    "SourceMetadataTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatefulRuleGroupOverrideTypeDef",
    "StatefulRuleGroupReferenceTypeDef",
    "StatefulRuleOptionsTypeDef",
    "StatefulRuleTypeDef",
    "StatelessRuleGroupReferenceTypeDef",
    "StatelessRuleTypeDef",
    "StatelessRulesAndCustomActionsTypeDef",
    "SubnetMappingTypeDef",
    "SyncStateTypeDef",
    "TCPFlagFieldTypeDef",
    "TLSInspectionConfigurationMetadataTypeDef",
    "TLSInspectionConfigurationResponseTypeDef",
    "TLSInspectionConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TlsCertificateDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFirewallDeleteProtectionRequestRequestTypeDef",
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    "UpdateFirewallDescriptionRequestRequestTypeDef",
    "UpdateFirewallDescriptionResponseTypeDef",
    "UpdateFirewallEncryptionConfigurationRequestRequestTypeDef",
    "UpdateFirewallEncryptionConfigurationResponseTypeDef",
    "UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    "UpdateFirewallPolicyRequestRequestTypeDef",
    "UpdateFirewallPolicyResponseTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateSubnetChangeProtectionRequestRequestTypeDef",
    "UpdateSubnetChangeProtectionResponseTypeDef",
    "UpdateTLSInspectionConfigurationRequestRequestTypeDef",
    "UpdateTLSInspectionConfigurationResponseTypeDef",
)

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef",
    {
        "PublishMetricAction": "PublishMetricActionTypeDef",
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressDefinition": str,
    },
)

AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "IdentifiedRuleIds": List[str],
        "IdentifiedType": IdentifiedTypeType,
        "AnalysisDetail": str,
    },
    total=False,
)

_RequiredAssociateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyArn": str,
    },
)
_OptionalAssociateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateFirewallPolicyRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

class AssociateFirewallPolicyRequestRequestTypeDef(
    _RequiredAssociateFirewallPolicyRequestRequestTypeDef,
    _OptionalAssociateFirewallPolicyRequestRequestTypeDef,
):
    pass

AssociateFirewallPolicyResponseTypeDef = TypedDict(
    "AssociateFirewallPolicyResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateSubnetsRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateSubnetsRequestRequestTypeDef",
    {
        "SubnetMappings": List["SubnetMappingTypeDef"],
    },
)
_OptionalAssociateSubnetsRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateSubnetsRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

class AssociateSubnetsRequestRequestTypeDef(
    _RequiredAssociateSubnetsRequestRequestTypeDef, _OptionalAssociateSubnetsRequestRequestTypeDef
):
    pass

AssociateSubnetsResponseTypeDef = TypedDict(
    "AssociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "SubnetId": str,
        "EndpointId": str,
        "Status": AttachmentStatusType,
        "StatusMessage": str,
    },
    total=False,
)

CIDRSummaryTypeDef = TypedDict(
    "CIDRSummaryTypeDef",
    {
        "AvailableCIDRCount": int,
        "UtilizedCIDRCount": int,
        "IPSetReferences": Dict[str, "IPSetMetadataTypeDef"],
    },
    total=False,
)

CapacityUsageSummaryTypeDef = TypedDict(
    "CapacityUsageSummaryTypeDef",
    {
        "CIDRs": "CIDRSummaryTypeDef",
    },
    total=False,
)

CheckCertificateRevocationStatusActionsTypeDef = TypedDict(
    "CheckCertificateRevocationStatusActionsTypeDef",
    {
        "RevokedStatusAction": RevocationCheckActionType,
        "UnknownStatusAction": RevocationCheckActionType,
    },
    total=False,
)

_RequiredCreateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicy": "FirewallPolicyTypeDef",
    },
)
_OptionalCreateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallPolicyRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class CreateFirewallPolicyRequestRequestTypeDef(
    _RequiredCreateFirewallPolicyRequestRequestTypeDef,
    _OptionalCreateFirewallPolicyRequestRequestTypeDef,
):
    pass

CreateFirewallPolicyResponseTypeDef = TypedDict(
    "CreateFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFirewallRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
    },
)
_OptionalCreateFirewallRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallRequestRequestTypeDef",
    {
        "DeleteProtection": bool,
        "SubnetChangeProtection": bool,
        "FirewallPolicyChangeProtection": bool,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class CreateFirewallRequestRequestTypeDef(
    _RequiredCreateFirewallRequestRequestTypeDef, _OptionalCreateFirewallRequestRequestTypeDef
):
    pass

CreateFirewallResponseTypeDef = TypedDict(
    "CreateFirewallResponseTypeDef",
    {
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
    },
)
_OptionalCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "Rules": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "SourceMetadata": "SourceMetadataTypeDef",
        "AnalyzeRuleGroup": bool,
    },
    total=False,
)

class CreateRuleGroupRequestRequestTypeDef(
    _RequiredCreateRuleGroupRequestRequestTypeDef, _OptionalCreateRuleGroupRequestRequestTypeDef
):
    pass

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationName": str,
        "TLSInspectionConfiguration": "TLSInspectionConfigurationTypeDef",
    },
)
_OptionalCreateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class CreateTLSInspectionConfigurationRequestRequestTypeDef(
    _RequiredCreateTLSInspectionConfigurationRequestRequestTypeDef,
    _OptionalCreateTLSInspectionConfigurationRequestRequestTypeDef,
):
    pass

CreateTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "CreateTLSInspectionConfigurationResponseTypeDef",
    {
        "UpdateToken": str,
        "TLSInspectionConfigurationResponse": "TLSInspectionConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomActionTypeDef = TypedDict(
    "CustomActionTypeDef",
    {
        "ActionName": str,
        "ActionDefinition": "ActionDefinitionTypeDef",
    },
)

DeleteFirewallPolicyRequestRequestTypeDef = TypedDict(
    "DeleteFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
    },
    total=False,
)

DeleteFirewallPolicyResponseTypeDef = TypedDict(
    "DeleteFirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

DeleteFirewallResponseTypeDef = TypedDict(
    "DeleteFirewallResponseTypeDef",
    {
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
    },
    total=False,
)

DeleteTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "DeleteTLSInspectionConfigurationResponseTypeDef",
    {
        "TLSInspectionConfigurationResponse": "TLSInspectionConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallPolicyRequestRequestTypeDef = TypedDict(
    "DescribeFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
    },
    total=False,
)

DescribeFirewallPolicyResponseTypeDef = TypedDict(
    "DescribeFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "FirewallPolicy": "FirewallPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallRequestRequestTypeDef = TypedDict(
    "DescribeFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

DescribeFirewallResponseTypeDef = TypedDict(
    "DescribeFirewallResponseTypeDef",
    {
        "UpdateToken": str,
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

DescribeLoggingConfigurationResponseTypeDef = TypedDict(
    "DescribeLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupMetadataRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupMetadataRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

DescribeRuleGroupMetadataResponseTypeDef = TypedDict(
    "DescribeRuleGroupMetadataResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "Description": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "StatefulRuleOptions": "StatefulRuleOptionsTypeDef",
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
        "AnalyzeRuleGroup": bool,
    },
    total=False,
)

DescribeRuleGroupResponseTypeDef = TypedDict(
    "DescribeRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroup": "RuleGroupTypeDef",
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
    },
    total=False,
)

DescribeTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "DescribeTLSInspectionConfigurationResponseTypeDef",
    {
        "UpdateToken": str,
        "TLSInspectionConfiguration": "TLSInspectionConfigurationTypeDef",
        "TLSInspectionConfigurationResponse": "TLSInspectionConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Value": str,
    },
)

_RequiredDisassociateSubnetsRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateSubnetsRequestRequestTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalDisassociateSubnetsRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateSubnetsRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

class DisassociateSubnetsRequestRequestTypeDef(
    _RequiredDisassociateSubnetsRequestRequestTypeDef,
    _OptionalDisassociateSubnetsRequestRequestTypeDef,
):
    pass

DisassociateSubnetsResponseTypeDef = TypedDict(
    "DisassociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "Type": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "KeyId": str,
    },
    total=False,
)

class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass

FirewallMetadataTypeDef = TypedDict(
    "FirewallMetadataTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

FirewallPolicyMetadataTypeDef = TypedDict(
    "FirewallPolicyMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

_RequiredFirewallPolicyResponseTypeDef = TypedDict(
    "_RequiredFirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
        "FirewallPolicyId": str,
    },
)
_OptionalFirewallPolicyResponseTypeDef = TypedDict(
    "_OptionalFirewallPolicyResponseTypeDef",
    {
        "Description": str,
        "FirewallPolicyStatus": ResourceStatusType,
        "Tags": List["TagTypeDef"],
        "ConsumedStatelessRuleCapacity": int,
        "ConsumedStatefulRuleCapacity": int,
        "NumberOfAssociations": int,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "LastModifiedTime": datetime,
    },
    total=False,
)

class FirewallPolicyResponseTypeDef(
    _RequiredFirewallPolicyResponseTypeDef, _OptionalFirewallPolicyResponseTypeDef
):
    pass

_RequiredFirewallPolicyTypeDef = TypedDict(
    "_RequiredFirewallPolicyTypeDef",
    {
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
    },
)
_OptionalFirewallPolicyTypeDef = TypedDict(
    "_OptionalFirewallPolicyTypeDef",
    {
        "StatelessRuleGroupReferences": List["StatelessRuleGroupReferenceTypeDef"],
        "StatelessCustomActions": List["CustomActionTypeDef"],
        "StatefulRuleGroupReferences": List["StatefulRuleGroupReferenceTypeDef"],
        "StatefulDefaultActions": List[str],
        "StatefulEngineOptions": "StatefulEngineOptionsTypeDef",
        "TLSInspectionConfigurationArn": str,
        "PolicyVariables": "PolicyVariablesTypeDef",
    },
    total=False,
)

class FirewallPolicyTypeDef(_RequiredFirewallPolicyTypeDef, _OptionalFirewallPolicyTypeDef):
    pass

_RequiredFirewallStatusTypeDef = TypedDict(
    "_RequiredFirewallStatusTypeDef",
    {
        "Status": FirewallStatusValueType,
        "ConfigurationSyncStateSummary": ConfigurationSyncStateType,
    },
)
_OptionalFirewallStatusTypeDef = TypedDict(
    "_OptionalFirewallStatusTypeDef",
    {
        "SyncStates": Dict[str, "SyncStateTypeDef"],
        "CapacityUsageSummary": "CapacityUsageSummaryTypeDef",
    },
    total=False,
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
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class FirewallTypeDef(_RequiredFirewallTypeDef, _OptionalFirewallTypeDef):
    pass

HeaderTypeDef = TypedDict(
    "HeaderTypeDef",
    {
        "Protocol": StatefulRuleProtocolType,
        "Source": str,
        "SourcePort": str,
        "Direction": StatefulRuleDirectionType,
        "Destination": str,
        "DestinationPort": str,
    },
)

IPSetMetadataTypeDef = TypedDict(
    "IPSetMetadataTypeDef",
    {
        "ResolvedCIDRCount": int,
    },
    total=False,
)

IPSetReferenceTypeDef = TypedDict(
    "IPSetReferenceTypeDef",
    {
        "ReferenceArn": str,
    },
    total=False,
)

IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "Definition": List[str],
    },
)

ListFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "ListFirewallPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFirewallPoliciesResponseTypeDef = TypedDict(
    "ListFirewallPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "FirewallPolicies": List["FirewallPolicyMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallsRequestRequestTypeDef = TypedDict(
    "ListFirewallsRequestRequestTypeDef",
    {
        "NextToken": str,
        "VpcIds": List[str],
        "MaxResults": int,
    },
    total=False,
)

ListFirewallsResponseTypeDef = TypedDict(
    "ListFirewallsResponseTypeDef",
    {
        "NextToken": str,
        "Firewalls": List["FirewallMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Scope": ResourceManagedStatusType,
        "ManagedType": ResourceManagedTypeType,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextToken": str,
        "RuleGroups": List["RuleGroupMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTLSInspectionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTLSInspectionConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTLSInspectionConfigurationsResponseTypeDef = TypedDict(
    "ListTLSInspectionConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "TLSInspectionConfigurations": List["TLSInspectionConfigurationMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
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
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDestinationConfigTypeDef = TypedDict(
    "LogDestinationConfigTypeDef",
    {
        "LogType": LogTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": Dict[str, str],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LogDestinationConfigs": List["LogDestinationConfigTypeDef"],
    },
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PerObjectStatusTypeDef = TypedDict(
    "PerObjectStatusTypeDef",
    {
        "SyncStatus": PerObjectSyncStatusType,
        "UpdateToken": str,
    },
    total=False,
)

PolicyVariablesTypeDef = TypedDict(
    "PolicyVariablesTypeDef",
    {
        "RuleVariables": Dict[str, "IPSetTypeDef"],
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

PortSetTypeDef = TypedDict(
    "PortSetTypeDef",
    {
        "Definition": List[str],
    },
    total=False,
)

PublishMetricActionTypeDef = TypedDict(
    "PublishMetricActionTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

ReferenceSetsTypeDef = TypedDict(
    "ReferenceSetsTypeDef",
    {
        "IPSetReferences": Dict[str, "IPSetReferenceTypeDef"],
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

RuleDefinitionTypeDef = TypedDict(
    "RuleDefinitionTypeDef",
    {
        "MatchAttributes": "MatchAttributesTypeDef",
        "Actions": List[str],
    },
)

RuleGroupMetadataTypeDef = TypedDict(
    "RuleGroupMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

_RequiredRuleGroupResponseTypeDef = TypedDict(
    "_RequiredRuleGroupResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroupId": str,
    },
)
_OptionalRuleGroupResponseTypeDef = TypedDict(
    "_OptionalRuleGroupResponseTypeDef",
    {
        "Description": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "RuleGroupStatus": ResourceStatusType,
        "Tags": List["TagTypeDef"],
        "ConsumedCapacity": int,
        "NumberOfAssociations": int,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "SourceMetadata": "SourceMetadataTypeDef",
        "SnsTopic": str,
        "LastModifiedTime": datetime,
        "AnalysisResults": List["AnalysisResultTypeDef"],
    },
    total=False,
)

class RuleGroupResponseTypeDef(
    _RequiredRuleGroupResponseTypeDef, _OptionalRuleGroupResponseTypeDef
):
    pass

_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "RulesSource": "RulesSourceTypeDef",
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "RuleVariables": "RuleVariablesTypeDef",
        "ReferenceSets": "ReferenceSetsTypeDef",
        "StatefulRuleOptions": "StatefulRuleOptionsTypeDef",
    },
    total=False,
)

class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass

_RequiredRuleOptionTypeDef = TypedDict(
    "_RequiredRuleOptionTypeDef",
    {
        "Keyword": str,
    },
)
_OptionalRuleOptionTypeDef = TypedDict(
    "_OptionalRuleOptionTypeDef",
    {
        "Settings": List[str],
    },
    total=False,
)

class RuleOptionTypeDef(_RequiredRuleOptionTypeDef, _OptionalRuleOptionTypeDef):
    pass

RuleVariablesTypeDef = TypedDict(
    "RuleVariablesTypeDef",
    {
        "IPSets": Dict[str, "IPSetTypeDef"],
        "PortSets": Dict[str, "PortSetTypeDef"],
    },
    total=False,
)

RulesSourceListTypeDef = TypedDict(
    "RulesSourceListTypeDef",
    {
        "Targets": List[str],
        "TargetTypes": List[TargetTypeType],
        "GeneratedRulesType": GeneratedRulesTypeType,
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

ServerCertificateConfigurationTypeDef = TypedDict(
    "ServerCertificateConfigurationTypeDef",
    {
        "ServerCertificates": List["ServerCertificateTypeDef"],
        "Scopes": List["ServerCertificateScopeTypeDef"],
        "CertificateAuthorityArn": str,
        "CheckCertificateRevocationStatus": "CheckCertificateRevocationStatusActionsTypeDef",
    },
    total=False,
)

ServerCertificateScopeTypeDef = TypedDict(
    "ServerCertificateScopeTypeDef",
    {
        "Sources": List["AddressTypeDef"],
        "Destinations": List["AddressTypeDef"],
        "SourcePorts": List["PortRangeTypeDef"],
        "DestinationPorts": List["PortRangeTypeDef"],
        "Protocols": List[int],
    },
    total=False,
)

ServerCertificateTypeDef = TypedDict(
    "ServerCertificateTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

SourceMetadataTypeDef = TypedDict(
    "SourceMetadataTypeDef",
    {
        "SourceArn": str,
        "SourceUpdateToken": str,
    },
    total=False,
)

StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": RuleOrderType,
        "StreamExceptionPolicy": StreamExceptionPolicyType,
    },
    total=False,
)

StatefulRuleGroupOverrideTypeDef = TypedDict(
    "StatefulRuleGroupOverrideTypeDef",
    {
        "Action": Literal["DROP_TO_ALERT"],
    },
    total=False,
)

_RequiredStatefulRuleGroupReferenceTypeDef = TypedDict(
    "_RequiredStatefulRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalStatefulRuleGroupReferenceTypeDef = TypedDict(
    "_OptionalStatefulRuleGroupReferenceTypeDef",
    {
        "Priority": int,
        "Override": "StatefulRuleGroupOverrideTypeDef",
    },
    total=False,
)

class StatefulRuleGroupReferenceTypeDef(
    _RequiredStatefulRuleGroupReferenceTypeDef, _OptionalStatefulRuleGroupReferenceTypeDef
):
    pass

StatefulRuleOptionsTypeDef = TypedDict(
    "StatefulRuleOptionsTypeDef",
    {
        "RuleOrder": RuleOrderType,
    },
    total=False,
)

StatefulRuleTypeDef = TypedDict(
    "StatefulRuleTypeDef",
    {
        "Action": StatefulActionType,
        "Header": "HeaderTypeDef",
        "RuleOptions": List["RuleOptionTypeDef"],
    },
)

StatelessRuleGroupReferenceTypeDef = TypedDict(
    "StatelessRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
        "Priority": int,
    },
)

StatelessRuleTypeDef = TypedDict(
    "StatelessRuleTypeDef",
    {
        "RuleDefinition": "RuleDefinitionTypeDef",
        "Priority": int,
    },
)

_RequiredStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_RequiredStatelessRulesAndCustomActionsTypeDef",
    {
        "StatelessRules": List["StatelessRuleTypeDef"],
    },
)
_OptionalStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_OptionalStatelessRulesAndCustomActionsTypeDef",
    {
        "CustomActions": List["CustomActionTypeDef"],
    },
    total=False,
)

class StatelessRulesAndCustomActionsTypeDef(
    _RequiredStatelessRulesAndCustomActionsTypeDef, _OptionalStatelessRulesAndCustomActionsTypeDef
):
    pass

_RequiredSubnetMappingTypeDef = TypedDict(
    "_RequiredSubnetMappingTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalSubnetMappingTypeDef = TypedDict(
    "_OptionalSubnetMappingTypeDef",
    {
        "IPAddressType": IPAddressTypeType,
    },
    total=False,
)

class SubnetMappingTypeDef(_RequiredSubnetMappingTypeDef, _OptionalSubnetMappingTypeDef):
    pass

SyncStateTypeDef = TypedDict(
    "SyncStateTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "Config": Dict[str, "PerObjectStatusTypeDef"],
    },
    total=False,
)

_RequiredTCPFlagFieldTypeDef = TypedDict(
    "_RequiredTCPFlagFieldTypeDef",
    {
        "Flags": List[TCPFlagType],
    },
)
_OptionalTCPFlagFieldTypeDef = TypedDict(
    "_OptionalTCPFlagFieldTypeDef",
    {
        "Masks": List[TCPFlagType],
    },
    total=False,
)

class TCPFlagFieldTypeDef(_RequiredTCPFlagFieldTypeDef, _OptionalTCPFlagFieldTypeDef):
    pass

TLSInspectionConfigurationMetadataTypeDef = TypedDict(
    "TLSInspectionConfigurationMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

_RequiredTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "_RequiredTLSInspectionConfigurationResponseTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
        "TLSInspectionConfigurationId": str,
    },
)
_OptionalTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "_OptionalTLSInspectionConfigurationResponseTypeDef",
    {
        "TLSInspectionConfigurationStatus": ResourceStatusType,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "LastModifiedTime": datetime,
        "NumberOfAssociations": int,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "Certificates": List["TlsCertificateDataTypeDef"],
        "CertificateAuthority": "TlsCertificateDataTypeDef",
    },
    total=False,
)

class TLSInspectionConfigurationResponseTypeDef(
    _RequiredTLSInspectionConfigurationResponseTypeDef,
    _OptionalTLSInspectionConfigurationResponseTypeDef,
):
    pass

TLSInspectionConfigurationTypeDef = TypedDict(
    "TLSInspectionConfigurationTypeDef",
    {
        "ServerCertificateConfigurations": List["ServerCertificateConfigurationTypeDef"],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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

TlsCertificateDataTypeDef = TypedDict(
    "TlsCertificateDataTypeDef",
    {
        "CertificateArn": str,
        "CertificateSerial": str,
        "Status": str,
        "StatusMessage": str,
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

_RequiredUpdateFirewallDeleteProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallDeleteProtectionRequestRequestTypeDef",
    {
        "DeleteProtection": bool,
    },
)
_OptionalUpdateFirewallDeleteProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallDeleteProtectionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

class UpdateFirewallDeleteProtectionRequestRequestTypeDef(
    _RequiredUpdateFirewallDeleteProtectionRequestRequestTypeDef,
    _OptionalUpdateFirewallDeleteProtectionRequestRequestTypeDef,
):
    pass

UpdateFirewallDeleteProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "DeleteProtection": bool,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateFirewallDescriptionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
    },
    total=False,
)

UpdateFirewallDescriptionResponseTypeDef = TypedDict(
    "UpdateFirewallDescriptionResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateFirewallEncryptionConfigurationRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

UpdateFirewallEncryptionConfigurationResponseTypeDef = TypedDict(
    "UpdateFirewallEncryptionConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "UpdateToken": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    {
        "FirewallPolicyChangeProtection": bool,
    },
)
_OptionalUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

class UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef(
    _RequiredUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef,
    _OptionalUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef,
):
    pass

UpdateFirewallPolicyChangeProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallPolicyRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicy": "FirewallPolicyTypeDef",
    },
)
_OptionalUpdateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyArn": str,
        "FirewallPolicyName": str,
        "Description": str,
        "DryRun": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class UpdateFirewallPolicyRequestRequestTypeDef(
    _RequiredUpdateFirewallPolicyRequestRequestTypeDef,
    _OptionalUpdateFirewallPolicyRequestRequestTypeDef,
):
    pass

UpdateFirewallPolicyResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
    total=False,
)

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleGroupRequestRequestTypeDef",
    {
        "UpdateToken": str,
    },
)
_OptionalUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroup": "RuleGroupTypeDef",
        "Rules": str,
        "Type": RuleGroupTypeType,
        "Description": str,
        "DryRun": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "SourceMetadata": "SourceMetadataTypeDef",
        "AnalyzeRuleGroup": bool,
    },
    total=False,
)

class UpdateRuleGroupRequestRequestTypeDef(
    _RequiredUpdateRuleGroupRequestRequestTypeDef, _OptionalUpdateRuleGroupRequestRequestTypeDef
):
    pass

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubnetChangeProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubnetChangeProtectionRequestRequestTypeDef",
    {
        "SubnetChangeProtection": bool,
    },
)
_OptionalUpdateSubnetChangeProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubnetChangeProtectionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

class UpdateSubnetChangeProtectionRequestRequestTypeDef(
    _RequiredUpdateSubnetChangeProtectionRequestRequestTypeDef,
    _OptionalUpdateSubnetChangeProtectionRequestRequestTypeDef,
):
    pass

UpdateSubnetChangeProtectionResponseTypeDef = TypedDict(
    "UpdateSubnetChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfiguration": "TLSInspectionConfigurationTypeDef",
        "UpdateToken": str,
    },
)
_OptionalUpdateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
        "Description": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class UpdateTLSInspectionConfigurationRequestRequestTypeDef(
    _RequiredUpdateTLSInspectionConfigurationRequestRequestTypeDef,
    _OptionalUpdateTLSInspectionConfigurationRequestRequestTypeDef,
):
    pass

UpdateTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "UpdateTLSInspectionConfigurationResponseTypeDef",
    {
        "UpdateToken": str,
        "TLSInspectionConfigurationResponse": "TLSInspectionConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
