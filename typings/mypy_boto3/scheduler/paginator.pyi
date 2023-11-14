"""
Type annotations for scheduler service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_scheduler import EventBridgeSchedulerClient
    from mypy_boto3_scheduler.paginator import (
        ListScheduleGroupsPaginator,
        ListSchedulesPaginator,
    )

    client: EventBridgeSchedulerClient = boto3.client("scheduler")

    list_schedule_groups_paginator: ListScheduleGroupsPaginator = client.get_paginator("list_schedule_groups")
    list_schedules_paginator: ListSchedulesPaginator = client.get_paginator("list_schedules")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ScheduleStateType
from .type_defs import (
    ListScheduleGroupsOutputTypeDef,
    ListSchedulesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListScheduleGroupsPaginator", "ListSchedulesPaginator")

class ListScheduleGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/scheduler.html#EventBridgeScheduler.Paginator.ListScheduleGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html#listschedulegroupspaginator)
    """

    def paginate(
        self, *, NamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScheduleGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/scheduler.html#EventBridgeScheduler.Paginator.ListScheduleGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html#listschedulegroupspaginator)
        """

class ListSchedulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/scheduler.html#EventBridgeScheduler.Paginator.ListSchedules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html#listschedulespaginator)
    """

    def paginate(
        self,
        *,
        GroupName: str = None,
        NamePrefix: str = None,
        State: ScheduleStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchedulesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/scheduler.html#EventBridgeScheduler.Paginator.ListSchedules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/paginators.html#listschedulespaginator)
        """
