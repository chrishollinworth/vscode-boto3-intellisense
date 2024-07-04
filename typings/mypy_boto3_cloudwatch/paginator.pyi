"""
Type annotations for cloudwatch service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudwatch import CloudWatchClient
    from mypy_boto3_cloudwatch.paginator import (
        DescribeAlarmHistoryPaginator,
        DescribeAlarmsPaginator,
        DescribeAnomalyDetectorsPaginator,
        GetMetricDataPaginator,
        ListDashboardsPaginator,
        ListMetricsPaginator,
    )

    client: CloudWatchClient = boto3.client("cloudwatch")

    describe_alarm_history_paginator: DescribeAlarmHistoryPaginator = client.get_paginator("describe_alarm_history")
    describe_alarms_paginator: DescribeAlarmsPaginator = client.get_paginator("describe_alarms")
    describe_anomaly_detectors_paginator: DescribeAnomalyDetectorsPaginator = client.get_paginator("describe_anomaly_detectors")
    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_metrics_paginator: ListMetricsPaginator = client.get_paginator("list_metrics")
    ```
"""

import sys
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AlarmTypeType,
    AnomalyDetectorTypeType,
    HistoryItemTypeType,
    ScanByType,
    StateValueType,
)
from .type_defs import (
    DescribeAlarmHistoryOutputTypeDef,
    DescribeAlarmsOutputTypeDef,
    DescribeAnomalyDetectorsOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    GetMetricDataOutputTypeDef,
    LabelOptionsTypeDef,
    ListDashboardsOutputTypeDef,
    ListMetricsOutputTypeDef,
    MetricDataQueryTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "DescribeAnomalyDetectorsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
)

class DescribeAlarmHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describealarmhistorypaginator)
    """

    def paginate(
        self,
        *,
        AlarmName: str = None,
        AlarmTypes: List[AlarmTypeType] = None,
        HistoryItemType: HistoryItemTypeType = None,
        StartDate: Union[datetime, str] = None,
        EndDate: Union[datetime, str] = None,
        ScanBy: ScanByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAlarmHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describealarmhistorypaginator)
        """

class DescribeAlarmsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describealarmspaginator)
    """

    def paginate(
        self,
        *,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmTypeType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValueType = None,
        ActionPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAlarmsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describealarmspaginator)
        """

class DescribeAnomalyDetectorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAnomalyDetectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describeanomalydetectorspaginator)
    """

    def paginate(
        self,
        *,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        AnomalyDetectorTypes: List[AnomalyDetectorTypeType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAnomalyDetectorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAnomalyDetectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describeanomalydetectorspaginator)
        """

class GetMetricDataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#getmetricdatapaginator)
    """

    def paginate(
        self,
        *,
        MetricDataQueries: List["MetricDataQueryTypeDef"],
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        ScanBy: ScanByType = None,
        LabelOptions: "LabelOptionsTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetMetricDataOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#getmetricdatapaginator)
        """

class ListDashboardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#listdashboardspaginator)
    """

    def paginate(
        self, *, DashboardNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#listdashboardspaginator)
        """

class ListMetricsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#listmetricspaginator)
    """

    def paginate(
        self,
        *,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List["DimensionFilterTypeDef"] = None,
        RecentlyActive: Literal["PT3H"] = None,
        IncludeLinkedAccounts: bool = None,
        OwningAccount: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMetricsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#listmetricspaginator)
        """
