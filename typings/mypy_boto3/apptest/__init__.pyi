"""
Main interface for apptest service.

Usage::

    ```python
    import boto3
    from mypy_boto3_apptest import (
        Client,
        ListTestCasesPaginator,
        ListTestConfigurationsPaginator,
        ListTestRunStepsPaginator,
        ListTestRunTestCasesPaginator,
        ListTestRunsPaginator,
        ListTestSuitesPaginator,
        MainframeModernizationApplicationTestingClient,
    )

    session = boto3.Session()

    client: MainframeModernizationApplicationTestingClient = boto3.client("apptest")
    session_client: MainframeModernizationApplicationTestingClient = session.client("apptest")

    list_test_cases_paginator: ListTestCasesPaginator = client.get_paginator("list_test_cases")
    list_test_configurations_paginator: ListTestConfigurationsPaginator = client.get_paginator("list_test_configurations")
    list_test_run_steps_paginator: ListTestRunStepsPaginator = client.get_paginator("list_test_run_steps")
    list_test_run_test_cases_paginator: ListTestRunTestCasesPaginator = client.get_paginator("list_test_run_test_cases")
    list_test_runs_paginator: ListTestRunsPaginator = client.get_paginator("list_test_runs")
    list_test_suites_paginator: ListTestSuitesPaginator = client.get_paginator("list_test_suites")
    ```
"""

from .client import MainframeModernizationApplicationTestingClient
from .paginator import (
    ListTestCasesPaginator,
    ListTestConfigurationsPaginator,
    ListTestRunsPaginator,
    ListTestRunStepsPaginator,
    ListTestRunTestCasesPaginator,
    ListTestSuitesPaginator,
)

Client = MainframeModernizationApplicationTestingClient

__all__ = (
    "Client",
    "ListTestCasesPaginator",
    "ListTestConfigurationsPaginator",
    "ListTestRunStepsPaginator",
    "ListTestRunTestCasesPaginator",
    "ListTestRunsPaginator",
    "ListTestSuitesPaginator",
    "MainframeModernizationApplicationTestingClient",
)
