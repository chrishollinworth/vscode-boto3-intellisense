"""
Type annotations for elasticbeanstalk service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elasticbeanstalk.client import ElasticBeanstalkClient
    from mypy_boto3_elasticbeanstalk.paginator import (
        DescribeApplicationVersionsPaginator,
        DescribeEnvironmentManagedActionHistoryPaginator,
        DescribeEnvironmentsPaginator,
        DescribeEventsPaginator,
        ListPlatformVersionsPaginator,
    )

    session = Session()
    client: ElasticBeanstalkClient = session.client("elasticbeanstalk")

    describe_application_versions_paginator: DescribeApplicationVersionsPaginator = client.get_paginator("describe_application_versions")
    describe_environment_managed_action_history_paginator: DescribeEnvironmentManagedActionHistoryPaginator = client.get_paginator("describe_environment_managed_action_history")
    describe_environments_paginator: DescribeEnvironmentsPaginator = client.get_paginator("describe_environments")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    list_platform_versions_paginator: ListPlatformVersionsPaginator = client.get_paginator("list_platform_versions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ApplicationVersionDescriptionsMessageTypeDef,
    DescribeApplicationVersionsMessagePaginateTypeDef,
    DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef,
    DescribeEnvironmentManagedActionHistoryResultTypeDef,
    DescribeEnvironmentsMessagePaginateTypeDef,
    DescribeEventsMessagePaginateTypeDef,
    EnvironmentDescriptionsMessageTypeDef,
    EventDescriptionsMessageTypeDef,
    ListPlatformVersionsRequestPaginateTypeDef,
    ListPlatformVersionsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ListPlatformVersionsPaginator",
)

if TYPE_CHECKING:
    _DescribeApplicationVersionsPaginatorBase = Paginator[
        ApplicationVersionDescriptionsMessageTypeDef
    ]
else:
    _DescribeApplicationVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeApplicationVersionsPaginator(_DescribeApplicationVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeApplicationVersions.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeapplicationversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeApplicationVersionsMessagePaginateTypeDef]
    ) -> PageIterator[ApplicationVersionDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeApplicationVersions.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeapplicationversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEnvironmentManagedActionHistoryPaginatorBase = Paginator[
        DescribeEnvironmentManagedActionHistoryResultTypeDef
    ]
else:
    _DescribeEnvironmentManagedActionHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEnvironmentManagedActionHistoryPaginator(
    _DescribeEnvironmentManagedActionHistoryPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeEnvironmentManagedActionHistory.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeenvironmentmanagedactionhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEnvironmentManagedActionHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeEnvironmentManagedActionHistory.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeenvironmentmanagedactionhistorypaginator)
        """

if TYPE_CHECKING:
    _DescribeEnvironmentsPaginatorBase = Paginator[EnvironmentDescriptionsMessageTypeDef]
else:
    _DescribeEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEnvironmentsPaginator(_DescribeEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeEnvironments.html#ElasticBeanstalk.Paginator.DescribeEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEnvironmentsMessagePaginateTypeDef]
    ) -> PageIterator[EnvironmentDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeEnvironments.html#ElasticBeanstalk.Paginator.DescribeEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeenvironmentspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[EventDescriptionsMessageTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeEvents.html#ElasticBeanstalk.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[EventDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/DescribeEvents.html#ElasticBeanstalk.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _ListPlatformVersionsPaginatorBase = Paginator[ListPlatformVersionsResultTypeDef]
else:
    _ListPlatformVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlatformVersionsPaginator(_ListPlatformVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/ListPlatformVersions.html#ElasticBeanstalk.Paginator.ListPlatformVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#listplatformversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlatformVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPlatformVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk/paginator/ListPlatformVersions.html#ElasticBeanstalk.Paginator.ListPlatformVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators/#listplatformversionspaginator)
        """
