# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for events service client

Usage::

    ```python
    import boto3
    from mypy_boto3_events import EventBridgeClient

    client: EventBridgeClient = boto3.client("events")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_events.paginator import (
    ListRuleNamesByTargetPaginator,
    ListRulesPaginator,
    ListTargetsByRulePaginator,
)
from mypy_boto3_events.type_defs import (
    CancelReplayResponseTypeDef,
    ConditionTypeDef,
    CreateArchiveResponseTypeDef,
    CreateEventBusResponseTypeDef,
    CreatePartnerEventSourceResponseTypeDef,
    DescribeArchiveResponseTypeDef,
    DescribeEventBusResponseTypeDef,
    DescribeEventSourceResponseTypeDef,
    DescribePartnerEventSourceResponseTypeDef,
    DescribeReplayResponseTypeDef,
    DescribeRuleResponseTypeDef,
    ListArchivesResponseTypeDef,
    ListEventBusesResponseTypeDef,
    ListEventSourcesResponseTypeDef,
    ListPartnerEventSourceAccountsResponseTypeDef,
    ListPartnerEventSourcesResponseTypeDef,
    ListReplaysResponseTypeDef,
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsByRuleResponseTypeDef,
    PutEventsRequestEntryTypeDef,
    PutEventsResponseTypeDef,
    PutPartnerEventsRequestEntryTypeDef,
    PutPartnerEventsResponseTypeDef,
    PutRuleResponseTypeDef,
    PutTargetsResponseTypeDef,
    RemoveTargetsResponseTypeDef,
    ReplayDestinationTypeDef,
    StartReplayResponseTypeDef,
    TagTypeDef,
    TargetTypeDef,
    TestEventPatternResponseTypeDef,
    UpdateArchiveResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EventBridgeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    IllegalStatusException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidEventPatternException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ManagedRuleException: Type[BotocoreClientError]
    OperationDisabledException: Type[BotocoreClientError]
    PolicyLengthExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class EventBridgeClient:
    """
    [EventBridge.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def activate_event_source(self, Name: str) -> None:
        """
        [Client.activate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.activate_event_source)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.can_paginate)
        """

    def cancel_replay(self, ReplayName: str) -> CancelReplayResponseTypeDef:
        """
        [Client.cancel_replay documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.cancel_replay)
        """

    def create_archive(
        self,
        ArchiveName: str,
        EventSourceArn: str,
        Description: str = None,
        EventPattern: str = None,
        RetentionDays: int = None,
    ) -> CreateArchiveResponseTypeDef:
        """
        [Client.create_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.create_archive)
        """

    def create_event_bus(
        self, Name: str, EventSourceName: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateEventBusResponseTypeDef:
        """
        [Client.create_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.create_event_bus)
        """

    def create_partner_event_source(
        self, Name: str, Account: str
    ) -> CreatePartnerEventSourceResponseTypeDef:
        """
        [Client.create_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.create_partner_event_source)
        """

    def deactivate_event_source(self, Name: str) -> None:
        """
        [Client.deactivate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.deactivate_event_source)
        """

    def delete_archive(self, ArchiveName: str) -> Dict[str, Any]:
        """
        [Client.delete_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.delete_archive)
        """

    def delete_event_bus(self, Name: str) -> None:
        """
        [Client.delete_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.delete_event_bus)
        """

    def delete_partner_event_source(self, Name: str, Account: str) -> None:
        """
        [Client.delete_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.delete_partner_event_source)
        """

    def delete_rule(self, Name: str, EventBusName: str = None, Force: bool = None) -> None:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.delete_rule)
        """

    def describe_archive(self, ArchiveName: str) -> DescribeArchiveResponseTypeDef:
        """
        [Client.describe_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.describe_archive)
        """

    def describe_event_bus(self, Name: str = None) -> DescribeEventBusResponseTypeDef:
        """
        [Client.describe_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.describe_event_bus)
        """

    def describe_event_source(self, Name: str) -> DescribeEventSourceResponseTypeDef:
        """
        [Client.describe_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.describe_event_source)
        """

    def describe_partner_event_source(self, Name: str) -> DescribePartnerEventSourceResponseTypeDef:
        """
        [Client.describe_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.describe_partner_event_source)
        """

    def describe_replay(self, ReplayName: str) -> DescribeReplayResponseTypeDef:
        """
        [Client.describe_replay documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.describe_replay)
        """

    def describe_rule(self, Name: str, EventBusName: str = None) -> DescribeRuleResponseTypeDef:
        """
        [Client.describe_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.describe_rule)
        """

    def disable_rule(self, Name: str, EventBusName: str = None) -> None:
        """
        [Client.disable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.disable_rule)
        """

    def enable_rule(self, Name: str, EventBusName: str = None) -> None:
        """
        [Client.enable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.enable_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.generate_presigned_url)
        """

    def list_archives(
        self,
        NamePrefix: str = None,
        EventSourceArn: str = None,
        State: Literal[
            "ENABLED", "DISABLED", "CREATING", "UPDATING", "CREATE_FAILED", "UPDATE_FAILED"
        ] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ListArchivesResponseTypeDef:
        """
        [Client.list_archives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_archives)
        """

    def list_event_buses(
        self, NamePrefix: str = None, NextToken: str = None, Limit: int = None
    ) -> ListEventBusesResponseTypeDef:
        """
        [Client.list_event_buses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_event_buses)
        """

    def list_event_sources(
        self, NamePrefix: str = None, NextToken: str = None, Limit: int = None
    ) -> ListEventSourcesResponseTypeDef:
        """
        [Client.list_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_event_sources)
        """

    def list_partner_event_source_accounts(
        self, EventSourceName: str, NextToken: str = None, Limit: int = None
    ) -> ListPartnerEventSourceAccountsResponseTypeDef:
        """
        [Client.list_partner_event_source_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_partner_event_source_accounts)
        """

    def list_partner_event_sources(
        self, NamePrefix: str, NextToken: str = None, Limit: int = None
    ) -> ListPartnerEventSourcesResponseTypeDef:
        """
        [Client.list_partner_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_partner_event_sources)
        """

    def list_replays(
        self,
        NamePrefix: str = None,
        State: Literal[
            "STARTING", "RUNNING", "CANCELLING", "COMPLETED", "CANCELLED", "FAILED"
        ] = None,
        EventSourceArn: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ListReplaysResponseTypeDef:
        """
        [Client.list_replays documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_replays)
        """

    def list_rule_names_by_target(
        self, TargetArn: str, EventBusName: str = None, NextToken: str = None, Limit: int = None
    ) -> ListRuleNamesByTargetResponseTypeDef:
        """
        [Client.list_rule_names_by_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_rule_names_by_target)
        """

    def list_rules(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ListRulesResponseTypeDef:
        """
        [Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_rules)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_tags_for_resource)
        """

    def list_targets_by_rule(
        self, Rule: str, EventBusName: str = None, NextToken: str = None, Limit: int = None
    ) -> ListTargetsByRuleResponseTypeDef:
        """
        [Client.list_targets_by_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.list_targets_by_rule)
        """

    def put_events(self, Entries: List[PutEventsRequestEntryTypeDef]) -> PutEventsResponseTypeDef:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.put_events)
        """

    def put_partner_events(
        self, Entries: List[PutPartnerEventsRequestEntryTypeDef]
    ) -> PutPartnerEventsResponseTypeDef:
        """
        [Client.put_partner_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.put_partner_events)
        """

    def put_permission(
        self,
        Action: str,
        Principal: str,
        StatementId: str,
        EventBusName: str = None,
        Condition: ConditionTypeDef = None,
    ) -> None:
        """
        [Client.put_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.put_permission)
        """

    def put_rule(
        self,
        Name: str,
        ScheduleExpression: str = None,
        EventPattern: str = None,
        State: Literal["ENABLED", "DISABLED"] = None,
        Description: str = None,
        RoleArn: str = None,
        Tags: List["TagTypeDef"] = None,
        EventBusName: str = None,
    ) -> PutRuleResponseTypeDef:
        """
        [Client.put_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.put_rule)
        """

    def put_targets(
        self, Rule: str, Targets: List["TargetTypeDef"], EventBusName: str = None
    ) -> PutTargetsResponseTypeDef:
        """
        [Client.put_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.put_targets)
        """

    def remove_permission(self, StatementId: str, EventBusName: str = None) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.remove_permission)
        """

    def remove_targets(
        self, Rule: str, Ids: List[str], EventBusName: str = None, Force: bool = None
    ) -> RemoveTargetsResponseTypeDef:
        """
        [Client.remove_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.remove_targets)
        """

    def start_replay(
        self,
        ReplayName: str,
        EventSourceArn: str,
        EventStartTime: datetime,
        EventEndTime: datetime,
        Destination: "ReplayDestinationTypeDef",
        Description: str = None,
    ) -> StartReplayResponseTypeDef:
        """
        [Client.start_replay documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.start_replay)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.tag_resource)
        """

    def test_event_pattern(self, EventPattern: str, Event: str) -> TestEventPatternResponseTypeDef:
        """
        [Client.test_event_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.test_event_pattern)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.untag_resource)
        """

    def update_archive(
        self,
        ArchiveName: str,
        Description: str = None,
        EventPattern: str = None,
        RetentionDays: int = None,
    ) -> UpdateArchiveResponseTypeDef:
        """
        [Client.update_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Client.update_archive)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rule_names_by_target"]
    ) -> ListRuleNamesByTargetPaginator:
        """
        [Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Paginator.ListRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_by_rule"]
    ) -> ListTargetsByRulePaginator:
        """
        [Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)
        """
