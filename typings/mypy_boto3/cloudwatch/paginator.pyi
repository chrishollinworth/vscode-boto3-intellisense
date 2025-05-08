"""
Type annotations for cloudwatch service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudwatch.client import CloudWatchClient
    from mypy_boto3_cloudwatch.paginator import (
        DescribeAlarmHistoryPaginator,
        DescribeAlarmsPaginator,
        DescribeAnomalyDetectorsPaginator,
        GetMetricDataPaginator,
        ListDashboardsPaginator,
        ListMetricsPaginator,
    )

    session = Session()
    client: CloudWatchClient = session.client("cloudwatch")

    describe_alarm_history_paginator: DescribeAlarmHistoryPaginator = client.get_paginator("describe_alarm_history")
    describe_alarms_paginator: DescribeAlarmsPaginator = client.get_paginator("describe_alarms")
    describe_anomaly_detectors_paginator: DescribeAnomalyDetectorsPaginator = client.get_paginator("describe_anomaly_detectors")
    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_metrics_paginator: ListMetricsPaginator = client.get_paginator("list_metrics")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAlarmHistoryInputPaginateTypeDef,
    DescribeAlarmHistoryOutputTypeDef,
    DescribeAlarmsInputPaginateTypeDef,
    DescribeAlarmsOutputTypeDef,
    DescribeAnomalyDetectorsInputPaginateTypeDef,
    DescribeAnomalyDetectorsOutputTypeDef,
    GetMetricDataInputPaginateTypeDef,
    GetMetricDataOutputTypeDef,
    ListDashboardsInputPaginateTypeDef,
    ListDashboardsOutputTypeDef,
    ListMetricsInputPaginateTypeDef,
    ListMetricsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "DescribeAnomalyDetectorsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
)

if TYPE_CHECKING:
    _DescribeAlarmHistoryPaginatorBase = Paginator[DescribeAlarmHistoryOutputTypeDef]
else:
    _DescribeAlarmHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAlarmHistoryPaginator(_DescribeAlarmHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/DescribeAlarmHistory.html#CloudWatch.Paginator.DescribeAlarmHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#describealarmhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAlarmHistoryInputPaginateTypeDef]
    ) -> PageIterator[DescribeAlarmHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/DescribeAlarmHistory.html#CloudWatch.Paginator.DescribeAlarmHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#describealarmhistorypaginator)
        """

if TYPE_CHECKING:
    _DescribeAlarmsPaginatorBase = Paginator[DescribeAlarmsOutputTypeDef]
else:
    _DescribeAlarmsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAlarmsPaginator(_DescribeAlarmsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/DescribeAlarms.html#CloudWatch.Paginator.DescribeAlarms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#describealarmspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAlarmsInputPaginateTypeDef]
    ) -> PageIterator[DescribeAlarmsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/DescribeAlarms.html#CloudWatch.Paginator.DescribeAlarms.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#describealarmspaginator)
        """

if TYPE_CHECKING:
    _DescribeAnomalyDetectorsPaginatorBase = Paginator[DescribeAnomalyDetectorsOutputTypeDef]
else:
    _DescribeAnomalyDetectorsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAnomalyDetectorsPaginator(_DescribeAnomalyDetectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/DescribeAnomalyDetectors.html#CloudWatch.Paginator.DescribeAnomalyDetectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#describeanomalydetectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAnomalyDetectorsInputPaginateTypeDef]
    ) -> PageIterator[DescribeAnomalyDetectorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/DescribeAnomalyDetectors.html#CloudWatch.Paginator.DescribeAnomalyDetectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#describeanomalydetectorspaginator)
        """

if TYPE_CHECKING:
    _GetMetricDataPaginatorBase = Paginator[GetMetricDataOutputTypeDef]
else:
    _GetMetricDataPaginatorBase = Paginator  # type: ignore[assignment]

class GetMetricDataPaginator(_GetMetricDataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/GetMetricData.html#CloudWatch.Paginator.GetMetricData)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#getmetricdatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetMetricDataInputPaginateTypeDef]
    ) -> PageIterator[GetMetricDataOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/GetMetricData.html#CloudWatch.Paginator.GetMetricData.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#getmetricdatapaginator)
        """

if TYPE_CHECKING:
    _ListDashboardsPaginatorBase = Paginator[ListDashboardsOutputTypeDef]
else:
    _ListDashboardsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDashboardsPaginator(_ListDashboardsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/ListDashboards.html#CloudWatch.Paginator.ListDashboards)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#listdashboardspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDashboardsInputPaginateTypeDef]
    ) -> PageIterator[ListDashboardsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/ListDashboards.html#CloudWatch.Paginator.ListDashboards.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#listdashboardspaginator)
        """

if TYPE_CHECKING:
    _ListMetricsPaginatorBase = Paginator[ListMetricsOutputTypeDef]
else:
    _ListMetricsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMetricsPaginator(_ListMetricsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/ListMetrics.html#CloudWatch.Paginator.ListMetrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#listmetricspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMetricsInputPaginateTypeDef]
    ) -> PageIterator[ListMetricsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/paginator/ListMetrics.html#CloudWatch.Paginator.ListMetrics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators/#listmetricspaginator)
        """
