"""
Type annotations for elasticbeanstalk service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_elasticbeanstalk import ElasticBeanstalkClient
    from mypy_boto3_elasticbeanstalk.paginator import (
        DescribeApplicationVersionsPaginator,
        DescribeEnvironmentManagedActionHistoryPaginator,
        DescribeEnvironmentsPaginator,
        DescribeEventsPaginator,
        ListPlatformVersionsPaginator,
    )

    client: ElasticBeanstalkClient = boto3.client("elasticbeanstalk")

    describe_application_versions_paginator: DescribeApplicationVersionsPaginator = client.get_paginator("describe_application_versions")
    describe_environment_managed_action_history_paginator: DescribeEnvironmentManagedActionHistoryPaginator = client.get_paginator("describe_environment_managed_action_history")
    describe_environments_paginator: DescribeEnvironmentsPaginator = client.get_paginator("describe_environments")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    list_platform_versions_paginator: ListPlatformVersionsPaginator = client.get_paginator("list_platform_versions")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import EventSeverityType
from .type_defs import (
    ApplicationVersionDescriptionsMessageTypeDef,
    DescribeEnvironmentManagedActionHistoryResultTypeDef,
    EnvironmentDescriptionsMessageTypeDef,
    EventDescriptionsMessageTypeDef,
    ListPlatformVersionsResultTypeDef,
    PaginatorConfigTypeDef,
    PlatformFilterTypeDef,
)

__all__ = (
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ListPlatformVersionsPaginator",
)

class DescribeApplicationVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeapplicationversionspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ApplicationVersionDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeapplicationversionspaginator)
        """

class DescribeEnvironmentManagedActionHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeenvironmentmanagedactionhistorypaginator)
    """

    def paginate(
        self,
        *,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEnvironmentManagedActionHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeenvironmentmanagedactionhistorypaginator)
        """

class DescribeEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EnvironmentDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeenvironmentspaginator)
        """

class DescribeEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeeventspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: EventSeverityType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeeventspaginator)
        """

class ListPlatformVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#listplatformversionspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["PlatformFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlatformVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#listplatformversionspaginator)
        """
