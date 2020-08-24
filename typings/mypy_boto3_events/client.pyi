# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_events.paginator import (
    ListRuleNamesByTargetPaginator,
    ListRulesPaginator,
    ListTargetsByRulePaginator,
)
from mypy_boto3_events.type_defs import (
    ConditionTypeDef,
    CreateEventBusResponseTypeDef,
    CreatePartnerEventSourceResponseTypeDef,
    DescribeEventBusResponseTypeDef,
    DescribeEventSourceResponseTypeDef,
    DescribePartnerEventSourceResponseTypeDef,
    DescribeRuleResponseTypeDef,
    ListEventBusesResponseTypeDef,
    ListEventSourcesResponseTypeDef,
    ListPartnerEventSourceAccountsResponseTypeDef,
    ListPartnerEventSourcesResponseTypeDef,
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
    TagTypeDef,
    TargetTypeDef,
    TestEventPatternResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EventBridgeClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    InternalException: Type[Boto3ClientError]
    InvalidEventPatternException: Type[Boto3ClientError]
    InvalidStateException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ManagedRuleException: Type[Boto3ClientError]
    OperationDisabledException: Type[Boto3ClientError]
    PolicyLengthExceededException: Type[Boto3ClientError]
    ResourceAlreadyExistsException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class EventBridgeClient:
    """
    [EventBridge.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client)
    """

    exceptions: Exceptions

    def activate_event_source(self, Name: str) -> None:
        """
        [Client.activate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.activate_event_source)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.can_paginate)
        """

    def create_event_bus(
        self, Name: str, EventSourceName: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateEventBusResponseTypeDef:
        """
        [Client.create_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.create_event_bus)
        """

    def create_partner_event_source(
        self, Name: str, Account: str
    ) -> CreatePartnerEventSourceResponseTypeDef:
        """
        [Client.create_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.create_partner_event_source)
        """

    def deactivate_event_source(self, Name: str) -> None:
        """
        [Client.deactivate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.deactivate_event_source)
        """

    def delete_event_bus(self, Name: str) -> None:
        """
        [Client.delete_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.delete_event_bus)
        """

    def delete_partner_event_source(self, Name: str, Account: str) -> None:
        """
        [Client.delete_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.delete_partner_event_source)
        """

    def delete_rule(self, Name: str, EventBusName: str = None, Force: bool = None) -> None:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.delete_rule)
        """

    def describe_event_bus(self, Name: str = None) -> DescribeEventBusResponseTypeDef:
        """
        [Client.describe_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.describe_event_bus)
        """

    def describe_event_source(self, Name: str) -> DescribeEventSourceResponseTypeDef:
        """
        [Client.describe_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.describe_event_source)
        """

    def describe_partner_event_source(self, Name: str) -> DescribePartnerEventSourceResponseTypeDef:
        """
        [Client.describe_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.describe_partner_event_source)
        """

    def describe_rule(self, Name: str, EventBusName: str = None) -> DescribeRuleResponseTypeDef:
        """
        [Client.describe_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.describe_rule)
        """

    def disable_rule(self, Name: str, EventBusName: str = None) -> None:
        """
        [Client.disable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.disable_rule)
        """

    def enable_rule(self, Name: str, EventBusName: str = None) -> None:
        """
        [Client.enable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.enable_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.generate_presigned_url)
        """

    def list_event_buses(
        self, NamePrefix: str = None, NextToken: str = None, Limit: int = None
    ) -> ListEventBusesResponseTypeDef:
        """
        [Client.list_event_buses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_event_buses)
        """

    def list_event_sources(
        self, NamePrefix: str = None, NextToken: str = None, Limit: int = None
    ) -> ListEventSourcesResponseTypeDef:
        """
        [Client.list_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_event_sources)
        """

    def list_partner_event_source_accounts(
        self, EventSourceName: str, NextToken: str = None, Limit: int = None
    ) -> ListPartnerEventSourceAccountsResponseTypeDef:
        """
        [Client.list_partner_event_source_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_partner_event_source_accounts)
        """

    def list_partner_event_sources(
        self, NamePrefix: str, NextToken: str = None, Limit: int = None
    ) -> ListPartnerEventSourcesResponseTypeDef:
        """
        [Client.list_partner_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_partner_event_sources)
        """

    def list_rule_names_by_target(
        self, TargetArn: str, EventBusName: str = None, NextToken: str = None, Limit: int = None
    ) -> ListRuleNamesByTargetResponseTypeDef:
        """
        [Client.list_rule_names_by_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_rule_names_by_target)
        """

    def list_rules(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ListRulesResponseTypeDef:
        """
        [Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_rules)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_tags_for_resource)
        """

    def list_targets_by_rule(
        self, Rule: str, EventBusName: str = None, NextToken: str = None, Limit: int = None
    ) -> ListTargetsByRuleResponseTypeDef:
        """
        [Client.list_targets_by_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.list_targets_by_rule)
        """

    def put_events(self, Entries: List[PutEventsRequestEntryTypeDef]) -> PutEventsResponseTypeDef:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.put_events)
        """

    def put_partner_events(
        self, Entries: List[PutPartnerEventsRequestEntryTypeDef]
    ) -> PutPartnerEventsResponseTypeDef:
        """
        [Client.put_partner_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.put_partner_events)
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
        [Client.put_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.put_permission)
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
        [Client.put_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.put_rule)
        """

    def put_targets(
        self, Rule: str, Targets: List["TargetTypeDef"], EventBusName: str = None
    ) -> PutTargetsResponseTypeDef:
        """
        [Client.put_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.put_targets)
        """

    def remove_permission(self, StatementId: str, EventBusName: str = None) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.remove_permission)
        """

    def remove_targets(
        self, Rule: str, Ids: List[str], EventBusName: str = None, Force: bool = None
    ) -> RemoveTargetsResponseTypeDef:
        """
        [Client.remove_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.remove_targets)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.tag_resource)
        """

    def test_event_pattern(self, EventPattern: str, Event: str) -> TestEventPatternResponseTypeDef:
        """
        [Client.test_event_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.test_event_pattern)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rule_names_by_target"]
    ) -> ListRuleNamesByTargetPaginator:
        """
        [Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_by_rule"]
    ) -> ListTargetsByRulePaginator:
        """
        [Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
