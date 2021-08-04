"""
Type annotations for route53-recovery-control-config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53_recovery_control_config.type_defs import AssertionRuleTypeDef

    data: AssertionRuleTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import RuleTypeType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssertionRuleTypeDef",
    "AssertionRuleUpdateTypeDef",
    "ClusterEndpointTypeDef",
    "ClusterTypeDef",
    "ControlPanelTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateControlPanelRequestRequestTypeDef",
    "CreateControlPanelResponseTypeDef",
    "CreateRoutingControlRequestRequestTypeDef",
    "CreateRoutingControlResponseTypeDef",
    "CreateSafetyRuleRequestRequestTypeDef",
    "CreateSafetyRuleResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteControlPanelRequestRequestTypeDef",
    "DeleteRoutingControlRequestRequestTypeDef",
    "DeleteSafetyRuleRequestRequestTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeControlPanelRequestRequestTypeDef",
    "DescribeControlPanelResponseTypeDef",
    "DescribeRoutingControlRequestRequestTypeDef",
    "DescribeRoutingControlResponseTypeDef",
    "DescribeSafetyRuleRequestRequestTypeDef",
    "DescribeSafetyRuleResponseTypeDef",
    "GatingRuleTypeDef",
    "GatingRuleUpdateTypeDef",
    "ListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    "ListAssociatedRoute53HealthChecksResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListControlPanelsRequestRequestTypeDef",
    "ListControlPanelsResponseTypeDef",
    "ListRoutingControlsRequestRequestTypeDef",
    "ListRoutingControlsResponseTypeDef",
    "ListSafetyRulesRequestRequestTypeDef",
    "ListSafetyRulesResponseTypeDef",
    "NewAssertionRuleTypeDef",
    "NewGatingRuleTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingControlTypeDef",
    "RuleConfigTypeDef",
    "RuleTypeDef",
    "UpdateControlPanelRequestRequestTypeDef",
    "UpdateControlPanelResponseTypeDef",
    "UpdateRoutingControlRequestRequestTypeDef",
    "UpdateRoutingControlResponseTypeDef",
    "UpdateSafetyRuleRequestRequestTypeDef",
    "UpdateSafetyRuleResponseTypeDef",
    "WaiterConfigTypeDef",
)

AssertionRuleTypeDef = TypedDict(
    "AssertionRuleTypeDef",
    {
        "AssertedControls": List[str],
        "ControlPanelArn": str,
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "SafetyRuleArn": str,
        "Status": StatusType,
        "WaitPeriodMs": int,
    },
)

AssertionRuleUpdateTypeDef = TypedDict(
    "AssertionRuleUpdateTypeDef",
    {
        "Name": str,
        "SafetyRuleArn": str,
        "WaitPeriodMs": int,
    },
)

ClusterEndpointTypeDef = TypedDict(
    "ClusterEndpointTypeDef",
    {
        "Endpoint": str,
        "Region": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterArn": str,
        "ClusterEndpoints": List["ClusterEndpointTypeDef"],
        "Name": str,
        "Status": StatusType,
    },
    total=False,
)

ControlPanelTypeDef = TypedDict(
    "ControlPanelTypeDef",
    {
        "ClusterArn": str,
        "ControlPanelArn": str,
        "DefaultControlPanel": bool,
        "Name": str,
        "RoutingControlCount": int,
        "Status": StatusType,
    },
    total=False,
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateControlPanelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateControlPanelRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ControlPanelName": str,
    },
)
_OptionalCreateControlPanelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateControlPanelRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateControlPanelRequestRequestTypeDef(
    _RequiredCreateControlPanelRequestRequestTypeDef,
    _OptionalCreateControlPanelRequestRequestTypeDef,
):
    pass

CreateControlPanelResponseTypeDef = TypedDict(
    "CreateControlPanelResponseTypeDef",
    {
        "ControlPanel": "ControlPanelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoutingControlRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoutingControlRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "RoutingControlName": str,
    },
)
_OptionalCreateRoutingControlRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoutingControlRequestRequestTypeDef",
    {
        "ClientToken": str,
        "ControlPanelArn": str,
    },
    total=False,
)

class CreateRoutingControlRequestRequestTypeDef(
    _RequiredCreateRoutingControlRequestRequestTypeDef,
    _OptionalCreateRoutingControlRequestRequestTypeDef,
):
    pass

CreateRoutingControlResponseTypeDef = TypedDict(
    "CreateRoutingControlResponseTypeDef",
    {
        "RoutingControl": "RoutingControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSafetyRuleRequestRequestTypeDef = TypedDict(
    "CreateSafetyRuleRequestRequestTypeDef",
    {
        "AssertionRule": "NewAssertionRuleTypeDef",
        "ClientToken": str,
        "GatingRule": "NewGatingRuleTypeDef",
    },
    total=False,
)

CreateSafetyRuleResponseTypeDef = TypedDict(
    "CreateSafetyRuleResponseTypeDef",
    {
        "AssertionRule": "AssertionRuleTypeDef",
        "GatingRule": "GatingRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DeleteControlPanelRequestRequestTypeDef = TypedDict(
    "DeleteControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)

DeleteRoutingControlRequestRequestTypeDef = TypedDict(
    "DeleteRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)

DeleteSafetyRuleRequestRequestTypeDef = TypedDict(
    "DeleteSafetyRuleRequestRequestTypeDef",
    {
        "SafetyRuleArn": str,
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeControlPanelRequestRequestTypeDef = TypedDict(
    "DescribeControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)

DescribeControlPanelResponseTypeDef = TypedDict(
    "DescribeControlPanelResponseTypeDef",
    {
        "ControlPanel": "ControlPanelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingControlRequestRequestTypeDef = TypedDict(
    "DescribeRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)

DescribeRoutingControlResponseTypeDef = TypedDict(
    "DescribeRoutingControlResponseTypeDef",
    {
        "RoutingControl": "RoutingControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSafetyRuleRequestRequestTypeDef = TypedDict(
    "DescribeSafetyRuleRequestRequestTypeDef",
    {
        "SafetyRuleArn": str,
    },
)

DescribeSafetyRuleResponseTypeDef = TypedDict(
    "DescribeSafetyRuleResponseTypeDef",
    {
        "AssertionRule": "AssertionRuleTypeDef",
        "GatingRule": "GatingRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GatingRuleTypeDef = TypedDict(
    "GatingRuleTypeDef",
    {
        "ControlPanelArn": str,
        "GatingControls": List[str],
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "SafetyRuleArn": str,
        "Status": StatusType,
        "TargetControls": List[str],
        "WaitPeriodMs": int,
    },
)

GatingRuleUpdateTypeDef = TypedDict(
    "GatingRuleUpdateTypeDef",
    {
        "Name": str,
        "SafetyRuleArn": str,
        "WaitPeriodMs": int,
    },
)

_RequiredListAssociatedRoute53HealthChecksRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)
_OptionalListAssociatedRoute53HealthChecksRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAssociatedRoute53HealthChecksRequestRequestTypeDef(
    _RequiredListAssociatedRoute53HealthChecksRequestRequestTypeDef,
    _OptionalListAssociatedRoute53HealthChecksRequestRequestTypeDef,
):
    pass

ListAssociatedRoute53HealthChecksResponseTypeDef = TypedDict(
    "ListAssociatedRoute53HealthChecksResponseTypeDef",
    {
        "HealthCheckIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "Clusters": List["ClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlPanelsRequestRequestTypeDef = TypedDict(
    "ListControlPanelsRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListControlPanelsResponseTypeDef = TypedDict(
    "ListControlPanelsResponseTypeDef",
    {
        "ControlPanels": List["ControlPanelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingControlsRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingControlsRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)
_OptionalListRoutingControlsRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingControlsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRoutingControlsRequestRequestTypeDef(
    _RequiredListRoutingControlsRequestRequestTypeDef,
    _OptionalListRoutingControlsRequestRequestTypeDef,
):
    pass

ListRoutingControlsResponseTypeDef = TypedDict(
    "ListRoutingControlsResponseTypeDef",
    {
        "NextToken": str,
        "RoutingControls": List["RoutingControlTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSafetyRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListSafetyRulesRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)
_OptionalListSafetyRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListSafetyRulesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSafetyRulesRequestRequestTypeDef(
    _RequiredListSafetyRulesRequestRequestTypeDef, _OptionalListSafetyRulesRequestRequestTypeDef
):
    pass

ListSafetyRulesResponseTypeDef = TypedDict(
    "ListSafetyRulesResponseTypeDef",
    {
        "NextToken": str,
        "SafetyRules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NewAssertionRuleTypeDef = TypedDict(
    "NewAssertionRuleTypeDef",
    {
        "AssertedControls": List[str],
        "ControlPanelArn": str,
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "WaitPeriodMs": int,
    },
)

NewGatingRuleTypeDef = TypedDict(
    "NewGatingRuleTypeDef",
    {
        "ControlPanelArn": str,
        "GatingControls": List[str],
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "TargetControls": List[str],
        "WaitPeriodMs": int,
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

RoutingControlTypeDef = TypedDict(
    "RoutingControlTypeDef",
    {
        "ControlPanelArn": str,
        "Name": str,
        "RoutingControlArn": str,
        "Status": StatusType,
    },
    total=False,
)

RuleConfigTypeDef = TypedDict(
    "RuleConfigTypeDef",
    {
        "Inverted": bool,
        "Threshold": int,
        "Type": RuleTypeType,
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "ASSERTION": "AssertionRuleTypeDef",
        "GATING": "GatingRuleTypeDef",
    },
    total=False,
)

UpdateControlPanelRequestRequestTypeDef = TypedDict(
    "UpdateControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "ControlPanelName": str,
    },
)

UpdateControlPanelResponseTypeDef = TypedDict(
    "UpdateControlPanelResponseTypeDef",
    {
        "ControlPanel": "ControlPanelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRoutingControlRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlName": str,
    },
)

UpdateRoutingControlResponseTypeDef = TypedDict(
    "UpdateRoutingControlResponseTypeDef",
    {
        "RoutingControl": "RoutingControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSafetyRuleRequestRequestTypeDef = TypedDict(
    "UpdateSafetyRuleRequestRequestTypeDef",
    {
        "AssertionRuleUpdate": "AssertionRuleUpdateTypeDef",
        "GatingRuleUpdate": "GatingRuleUpdateTypeDef",
    },
    total=False,
)

UpdateSafetyRuleResponseTypeDef = TypedDict(
    "UpdateSafetyRuleResponseTypeDef",
    {
        "AssertionRule": "AssertionRuleTypeDef",
        "GatingRule": "GatingRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
