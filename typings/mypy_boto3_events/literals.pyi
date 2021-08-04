"""
Type annotations for events service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_events/literals.html)

Usage::

    ```python
    from mypy_boto3_events.literals import ApiDestinationHttpMethodType

    data: ApiDestinationHttpMethodType = "DELETE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApiDestinationHttpMethodType",
    "ApiDestinationStateType",
    "ArchiveStateType",
    "AssignPublicIpType",
    "ConnectionAuthorizationTypeType",
    "ConnectionOAuthHttpMethodType",
    "ConnectionStateType",
    "EventSourceStateType",
    "LaunchTypeType",
    "ListRuleNamesByTargetPaginatorName",
    "ListRulesPaginatorName",
    "ListTargetsByRulePaginatorName",
    "PlacementConstraintTypeType",
    "PlacementStrategyTypeType",
    "PropagateTagsType",
    "ReplayStateType",
    "RuleStateType",
)

ApiDestinationHttpMethodType = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
ApiDestinationStateType = Literal["ACTIVE", "INACTIVE"]
ArchiveStateType = Literal[
    "CREATE_FAILED", "CREATING", "DISABLED", "ENABLED", "UPDATE_FAILED", "UPDATING"
]
AssignPublicIpType = Literal["DISABLED", "ENABLED"]
ConnectionAuthorizationTypeType = Literal["API_KEY", "BASIC", "OAUTH_CLIENT_CREDENTIALS"]
ConnectionOAuthHttpMethodType = Literal["GET", "POST", "PUT"]
ConnectionStateType = Literal[
    "AUTHORIZED", "AUTHORIZING", "CREATING", "DEAUTHORIZED", "DEAUTHORIZING", "DELETING", "UPDATING"
]
EventSourceStateType = Literal["ACTIVE", "DELETED", "PENDING"]
LaunchTypeType = Literal["EC2", "FARGATE"]
ListRuleNamesByTargetPaginatorName = Literal["list_rule_names_by_target"]
ListRulesPaginatorName = Literal["list_rules"]
ListTargetsByRulePaginatorName = Literal["list_targets_by_rule"]
PlacementConstraintTypeType = Literal["distinctInstance", "memberOf"]
PlacementStrategyTypeType = Literal["binpack", "random", "spread"]
PropagateTagsType = Literal["TASK_DEFINITION"]
ReplayStateType = Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"]
RuleStateType = Literal["DISABLED", "ENABLED"]
