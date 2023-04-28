"""
Type annotations for scheduler service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_scheduler import EventBridgeSchedulerClient

    client: EventBridgeSchedulerClient = boto3.client("scheduler")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ScheduleStateType
from .paginator import ListScheduleGroupsPaginator, ListSchedulesPaginator
from .type_defs import (
    CreateScheduleGroupOutputTypeDef,
    CreateScheduleOutputTypeDef,
    FlexibleTimeWindowTypeDef,
    GetScheduleGroupOutputTypeDef,
    GetScheduleOutputTypeDef,
    ListScheduleGroupsOutputTypeDef,
    ListSchedulesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagTypeDef,
    TargetTypeDef,
    UpdateScheduleOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EventBridgeSchedulerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EventBridgeSchedulerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EventBridgeSchedulerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#close)
        """
    def create_schedule(
        self,
        *,
        FlexibleTimeWindow: "FlexibleTimeWindowTypeDef",
        Name: str,
        ScheduleExpression: str,
        Target: "TargetTypeDef",
        ClientToken: str = None,
        Description: str = None,
        EndDate: Union[datetime, str] = None,
        GroupName: str = None,
        KmsKeyArn: str = None,
        ScheduleExpressionTimezone: str = None,
        StartDate: Union[datetime, str] = None,
        State: ScheduleStateType = None
    ) -> CreateScheduleOutputTypeDef:
        """
        Creates the specified schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.create_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#create_schedule)
        """
    def create_schedule_group(
        self, *, Name: str, ClientToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateScheduleGroupOutputTypeDef:
        """
        Creates the specified schedule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.create_schedule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#create_schedule_group)
        """
    def delete_schedule(
        self, *, Name: str, ClientToken: str = None, GroupName: str = None
    ) -> Dict[str, Any]:
        """
        Deletes the specified schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.delete_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#delete_schedule)
        """
    def delete_schedule_group(self, *, Name: str, ClientToken: str = None) -> Dict[str, Any]:
        """
        Deletes the specified schedule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.delete_schedule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#delete_schedule_group)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#generate_presigned_url)
        """
    def get_schedule(self, *, Name: str, GroupName: str = None) -> GetScheduleOutputTypeDef:
        """
        Retrieves the specified schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.get_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#get_schedule)
        """
    def get_schedule_group(self, *, Name: str) -> GetScheduleGroupOutputTypeDef:
        """
        Retrieves the specified schedule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.get_schedule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#get_schedule_group)
        """
    def list_schedule_groups(
        self, *, MaxResults: int = None, NamePrefix: str = None, NextToken: str = None
    ) -> ListScheduleGroupsOutputTypeDef:
        """
        Returns a paginated list of your schedule groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.list_schedule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#list_schedule_groups)
        """
    def list_schedules(
        self,
        *,
        GroupName: str = None,
        MaxResults: int = None,
        NamePrefix: str = None,
        NextToken: str = None,
        State: ScheduleStateType = None
    ) -> ListSchedulesOutputTypeDef:
        """
        Returns a paginated list of your EventBridge Scheduler schedules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.list_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#list_schedules)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags associated with the Scheduler resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified EventBridge
        Scheduler resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified EventBridge Scheduler schedule
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#untag_resource)
        """
    def update_schedule(
        self,
        *,
        FlexibleTimeWindow: "FlexibleTimeWindowTypeDef",
        Name: str,
        ScheduleExpression: str,
        Target: "TargetTypeDef",
        ClientToken: str = None,
        Description: str = None,
        EndDate: Union[datetime, str] = None,
        GroupName: str = None,
        KmsKeyArn: str = None,
        ScheduleExpressionTimezone: str = None,
        StartDate: Union[datetime, str] = None,
        State: ScheduleStateType = None
    ) -> UpdateScheduleOutputTypeDef:
        """
        Updates the specified schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Client.update_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/client.html#update_schedule)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_schedule_groups"]
    ) -> ListScheduleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Paginator.ListScheduleGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html#listschedulegroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_schedules"]) -> ListSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/scheduler.html#EventBridgeScheduler.Paginator.ListSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html#listschedulespaginator)
        """
