"""
Type annotations for apptest service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_apptest.client import MainframeModernizationApplicationTestingClient
    from mypy_boto3_apptest.paginator import (
        ListTestCasesPaginator,
        ListTestConfigurationsPaginator,
        ListTestRunStepsPaginator,
        ListTestRunTestCasesPaginator,
        ListTestRunsPaginator,
        ListTestSuitesPaginator,
    )

    session = Session()
    client: MainframeModernizationApplicationTestingClient = session.client("apptest")

    list_test_cases_paginator: ListTestCasesPaginator = client.get_paginator("list_test_cases")
    list_test_configurations_paginator: ListTestConfigurationsPaginator = client.get_paginator("list_test_configurations")
    list_test_run_steps_paginator: ListTestRunStepsPaginator = client.get_paginator("list_test_run_steps")
    list_test_run_test_cases_paginator: ListTestRunTestCasesPaginator = client.get_paginator("list_test_run_test_cases")
    list_test_runs_paginator: ListTestRunsPaginator = client.get_paginator("list_test_runs")
    list_test_suites_paginator: ListTestSuitesPaginator = client.get_paginator("list_test_suites")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListTestCasesRequestPaginateTypeDef,
    ListTestCasesResponseTypeDef,
    ListTestConfigurationsRequestPaginateTypeDef,
    ListTestConfigurationsResponseTypeDef,
    ListTestRunsRequestPaginateTypeDef,
    ListTestRunsResponseTypeDef,
    ListTestRunStepsRequestPaginateTypeDef,
    ListTestRunStepsResponseTypeDef,
    ListTestRunTestCasesRequestPaginateTypeDef,
    ListTestRunTestCasesResponseTypeDef,
    ListTestSuitesRequestPaginateTypeDef,
    ListTestSuitesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListTestCasesPaginator",
    "ListTestConfigurationsPaginator",
    "ListTestRunStepsPaginator",
    "ListTestRunTestCasesPaginator",
    "ListTestRunsPaginator",
    "ListTestSuitesPaginator",
)

if TYPE_CHECKING:
    _ListTestCasesPaginatorBase = Paginator[ListTestCasesResponseTypeDef]
else:
    _ListTestCasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestCasesPaginator(_ListTestCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestCases.html#MainframeModernizationApplicationTesting.Paginator.ListTestCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestcasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestCasesRequestPaginateTypeDef]
    ) -> PageIterator[ListTestCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestCases.html#MainframeModernizationApplicationTesting.Paginator.ListTestCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestcasespaginator)
        """

if TYPE_CHECKING:
    _ListTestConfigurationsPaginatorBase = Paginator[ListTestConfigurationsResponseTypeDef]
else:
    _ListTestConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestConfigurationsPaginator(_ListTestConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestConfigurations.html#MainframeModernizationApplicationTesting.Paginator.ListTestConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListTestConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestConfigurations.html#MainframeModernizationApplicationTesting.Paginator.ListTestConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListTestRunStepsPaginatorBase = Paginator[ListTestRunStepsResponseTypeDef]
else:
    _ListTestRunStepsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestRunStepsPaginator(_ListTestRunStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestRunSteps.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunSteps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestrunstepspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestRunStepsRequestPaginateTypeDef]
    ) -> PageIterator[ListTestRunStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestRunSteps.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunSteps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestrunstepspaginator)
        """

if TYPE_CHECKING:
    _ListTestRunTestCasesPaginatorBase = Paginator[ListTestRunTestCasesResponseTypeDef]
else:
    _ListTestRunTestCasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestRunTestCasesPaginator(_ListTestRunTestCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestRunTestCases.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunTestCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestruntestcasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestRunTestCasesRequestPaginateTypeDef]
    ) -> PageIterator[ListTestRunTestCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestRunTestCases.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunTestCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestruntestcasespaginator)
        """

if TYPE_CHECKING:
    _ListTestRunsPaginatorBase = Paginator[ListTestRunsResponseTypeDef]
else:
    _ListTestRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestRunsPaginator(_ListTestRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestRuns.html#MainframeModernizationApplicationTesting.Paginator.ListTestRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListTestRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestRuns.html#MainframeModernizationApplicationTesting.Paginator.ListTestRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestrunspaginator)
        """

if TYPE_CHECKING:
    _ListTestSuitesPaginatorBase = Paginator[ListTestSuitesResponseTypeDef]
else:
    _ListTestSuitesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestSuitesPaginator(_ListTestSuitesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestSuites.html#MainframeModernizationApplicationTesting.Paginator.ListTestSuites)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestsuitespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestSuitesRequestPaginateTypeDef]
    ) -> PageIterator[ListTestSuitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/paginator/ListTestSuites.html#MainframeModernizationApplicationTesting.Paginator.ListTestSuites.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators/#listtestsuitespaginator)
        """
