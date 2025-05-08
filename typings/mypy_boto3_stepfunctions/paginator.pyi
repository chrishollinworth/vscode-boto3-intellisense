"""
Type annotations for stepfunctions service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_stepfunctions.client import SFNClient
    from mypy_boto3_stepfunctions.paginator import (
        GetExecutionHistoryPaginator,
        ListActivitiesPaginator,
        ListExecutionsPaginator,
        ListMapRunsPaginator,
        ListStateMachinesPaginator,
    )

    session = Session()
    client: SFNClient = session.client("stepfunctions")

    get_execution_history_paginator: GetExecutionHistoryPaginator = client.get_paginator("get_execution_history")
    list_activities_paginator: ListActivitiesPaginator = client.get_paginator("list_activities")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_map_runs_paginator: ListMapRunsPaginator = client.get_paginator("list_map_runs")
    list_state_machines_paginator: ListStateMachinesPaginator = client.get_paginator("list_state_machines")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetExecutionHistoryInputPaginateTypeDef,
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesInputPaginateTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsInputPaginateTypeDef,
    ListExecutionsOutputTypeDef,
    ListMapRunsInputPaginateTypeDef,
    ListMapRunsOutputTypeDef,
    ListStateMachinesInputPaginateTypeDef,
    ListStateMachinesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListMapRunsPaginator",
    "ListStateMachinesPaginator",
)

if TYPE_CHECKING:
    _GetExecutionHistoryPaginatorBase = Paginator[GetExecutionHistoryOutputTypeDef]
else:
    _GetExecutionHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetExecutionHistoryPaginator(_GetExecutionHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/GetExecutionHistory.html#SFN.Paginator.GetExecutionHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#getexecutionhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetExecutionHistoryInputPaginateTypeDef]
    ) -> PageIterator[GetExecutionHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/GetExecutionHistory.html#SFN.Paginator.GetExecutionHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#getexecutionhistorypaginator)
        """

if TYPE_CHECKING:
    _ListActivitiesPaginatorBase = Paginator[ListActivitiesOutputTypeDef]
else:
    _ListActivitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListActivitiesPaginator(_ListActivitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListActivities.html#SFN.Paginator.ListActivities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#listactivitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActivitiesInputPaginateTypeDef]
    ) -> PageIterator[ListActivitiesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListActivities.html#SFN.Paginator.ListActivities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#listactivitiespaginator)
        """

if TYPE_CHECKING:
    _ListExecutionsPaginatorBase = Paginator[ListExecutionsOutputTypeDef]
else:
    _ListExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExecutionsPaginator(_ListExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListExecutions.html#SFN.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#listexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExecutionsInputPaginateTypeDef]
    ) -> PageIterator[ListExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListExecutions.html#SFN.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#listexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListMapRunsPaginatorBase = Paginator[ListMapRunsOutputTypeDef]
else:
    _ListMapRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMapRunsPaginator(_ListMapRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListMapRuns.html#SFN.Paginator.ListMapRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#listmaprunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMapRunsInputPaginateTypeDef]
    ) -> PageIterator[ListMapRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListMapRuns.html#SFN.Paginator.ListMapRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#listmaprunspaginator)
        """

if TYPE_CHECKING:
    _ListStateMachinesPaginatorBase = Paginator[ListStateMachinesOutputTypeDef]
else:
    _ListStateMachinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListStateMachinesPaginator(_ListStateMachinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListStateMachines.html#SFN.Paginator.ListStateMachines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#liststatemachinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStateMachinesInputPaginateTypeDef]
    ) -> PageIterator[ListStateMachinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/paginator/ListStateMachines.html#SFN.Paginator.ListStateMachines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators/#liststatemachinespaginator)
        """
