"""
Type annotations for amp service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_amp.client import PrometheusServiceClient
    from mypy_boto3_amp.waiter import (
        AnomalyDetectorActiveWaiter,
        AnomalyDetectorDeletedWaiter,
        ScraperActiveWaiter,
        ScraperDeletedWaiter,
        WorkspaceActiveWaiter,
        WorkspaceDeletedWaiter,
    )

    session = Session()
    client: PrometheusServiceClient = session.client("amp")

    anomaly_detector_active_waiter: AnomalyDetectorActiveWaiter = client.get_waiter("anomaly_detector_active")
    anomaly_detector_deleted_waiter: AnomalyDetectorDeletedWaiter = client.get_waiter("anomaly_detector_deleted")
    scraper_active_waiter: ScraperActiveWaiter = client.get_waiter("scraper_active")
    scraper_deleted_waiter: ScraperDeletedWaiter = client.get_waiter("scraper_deleted")
    workspace_active_waiter: WorkspaceActiveWaiter = client.get_waiter("workspace_active")
    workspace_deleted_waiter: WorkspaceDeletedWaiter = client.get_waiter("workspace_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeAnomalyDetectorRequestWaitExtraTypeDef,
    DescribeAnomalyDetectorRequestWaitTypeDef,
    DescribeScraperRequestWaitExtraTypeDef,
    DescribeScraperRequestWaitTypeDef,
    DescribeWorkspaceRequestWaitExtraTypeDef,
    DescribeWorkspaceRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "AnomalyDetectorActiveWaiter",
    "AnomalyDetectorDeletedWaiter",
    "ScraperActiveWaiter",
    "ScraperDeletedWaiter",
    "WorkspaceActiveWaiter",
    "WorkspaceDeletedWaiter",
)

class AnomalyDetectorActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/AnomalyDetectorActive.html#PrometheusService.Waiter.AnomalyDetectorActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#anomalydetectoractivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAnomalyDetectorRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/AnomalyDetectorActive.html#PrometheusService.Waiter.AnomalyDetectorActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#anomalydetectoractivewaiter)
        """

class AnomalyDetectorDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/AnomalyDetectorDeleted.html#PrometheusService.Waiter.AnomalyDetectorDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#anomalydetectordeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAnomalyDetectorRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/AnomalyDetectorDeleted.html#PrometheusService.Waiter.AnomalyDetectorDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#anomalydetectordeletedwaiter)
        """

class ScraperActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/ScraperActive.html#PrometheusService.Waiter.ScraperActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#scraperactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScraperRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/ScraperActive.html#PrometheusService.Waiter.ScraperActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#scraperactivewaiter)
        """

class ScraperDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/ScraperDeleted.html#PrometheusService.Waiter.ScraperDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#scraperdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScraperRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/ScraperDeleted.html#PrometheusService.Waiter.ScraperDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#scraperdeletedwaiter)
        """

class WorkspaceActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/WorkspaceActive.html#PrometheusService.Waiter.WorkspaceActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#workspaceactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspaceRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/WorkspaceActive.html#PrometheusService.Waiter.WorkspaceActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#workspaceactivewaiter)
        """

class WorkspaceDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/WorkspaceDeleted.html#PrometheusService.Waiter.WorkspaceDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#workspacedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspaceRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/waiter/WorkspaceDeleted.html#PrometheusService.Waiter.WorkspaceDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters/#workspacedeletedwaiter)
        """
