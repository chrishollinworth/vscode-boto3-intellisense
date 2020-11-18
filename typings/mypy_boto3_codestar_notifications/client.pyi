# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for codestar-notifications service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar_notifications import CodeStarNotificationsClient

    client: CodeStarNotificationsClient = boto3.client("codestar-notifications")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_codestar_notifications.paginator import (
    ListEventTypesPaginator,
    ListNotificationRulesPaginator,
    ListTargetsPaginator,
)
from mypy_boto3_codestar_notifications.type_defs import (
    CreateNotificationRuleResultTypeDef,
    DeleteNotificationRuleResultTypeDef,
    DescribeNotificationRuleResultTypeDef,
    ListEventTypesFilterTypeDef,
    ListEventTypesResultTypeDef,
    ListNotificationRulesFilterTypeDef,
    ListNotificationRulesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    ListTargetsFilterTypeDef,
    ListTargetsResultTypeDef,
    SubscribeResultTypeDef,
    TagResourceResultTypeDef,
    TargetTypeDef,
    UnsubscribeResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeStarNotificationsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConfigurationException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeStarNotificationsClient:
    """
    [CodeStarNotifications.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.can_paginate)
        """

    def create_notification_rule(
        self,
        Name: str,
        EventTypeIds: List[str],
        Resource: str,
        Targets: List[TargetTypeDef],
        DetailType: Literal["BASIC", "FULL"],
        ClientRequestToken: str = None,
        Tags: Dict[str, str] = None,
        Status: Literal["ENABLED", "DISABLED"] = None,
    ) -> CreateNotificationRuleResultTypeDef:
        """
        [Client.create_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.create_notification_rule)
        """

    def delete_notification_rule(self, Arn: str) -> DeleteNotificationRuleResultTypeDef:
        """
        [Client.delete_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_notification_rule)
        """

    def delete_target(self, TargetAddress: str, ForceUnsubscribeAll: bool = None) -> Dict[str, Any]:
        """
        [Client.delete_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_target)
        """

    def describe_notification_rule(self, Arn: str) -> DescribeNotificationRuleResultTypeDef:
        """
        [Client.describe_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.describe_notification_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.generate_presigned_url)
        """

    def list_event_types(
        self,
        Filters: List[ListEventTypesFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEventTypesResultTypeDef:
        """
        [Client.list_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_event_types)
        """

    def list_notification_rules(
        self,
        Filters: List[ListNotificationRulesFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListNotificationRulesResultTypeDef:
        """
        [Client.list_notification_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_notification_rules)
        """

    def list_tags_for_resource(self, Arn: str) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_tags_for_resource)
        """

    def list_targets(
        self,
        Filters: List[ListTargetsFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTargetsResultTypeDef:
        """
        [Client.list_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_targets)
        """

    def subscribe(
        self, Arn: str, Target: TargetTypeDef, ClientRequestToken: str = None
    ) -> SubscribeResultTypeDef:
        """
        [Client.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.subscribe)
        """

    def tag_resource(self, Arn: str, Tags: Dict[str, str]) -> TagResourceResultTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.tag_resource)
        """

    def unsubscribe(self, Arn: str, TargetAddress: str) -> UnsubscribeResultTypeDef:
        """
        [Client.unsubscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.unsubscribe)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.untag_resource)
        """

    def update_notification_rule(
        self,
        Arn: str,
        Name: str = None,
        Status: Literal["ENABLED", "DISABLED"] = None,
        EventTypeIds: List[str] = None,
        Targets: List[TargetTypeDef] = None,
        DetailType: Literal["BASIC", "FULL"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Client.update_notification_rule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_event_types"]) -> ListEventTypesPaginator:
        """
        [Paginator.ListEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notification_rules"]
    ) -> ListNotificationRulesPaginator:
        """
        [Paginator.ListNotificationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_targets"]) -> ListTargetsPaginator:
        """
        [Paginator.ListTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets)
        """
