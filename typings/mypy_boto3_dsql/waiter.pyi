"""
Type annotations for dsql service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dsql.client import AuroraDSQLClient
    from mypy_boto3_dsql.waiter import (
        ClusterActiveWaiter,
        ClusterNotExistsWaiter,
    )

    session = Session()
    client: AuroraDSQLClient = session.client("dsql")

    cluster_active_waiter: ClusterActiveWaiter = client.get_waiter("cluster_active")
    cluster_not_exists_waiter: ClusterNotExistsWaiter = client.get_waiter("cluster_not_exists")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetClusterInputWaitExtraTypeDef, GetClusterInputWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ClusterActiveWaiter", "ClusterNotExistsWaiter")

class ClusterActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/waiter/ClusterActive.html#AuroraDSQL.Waiter.ClusterActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/waiters/#clusteractivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetClusterInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/waiter/ClusterActive.html#AuroraDSQL.Waiter.ClusterActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/waiters/#clusteractivewaiter)
        """

class ClusterNotExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/waiter/ClusterNotExists.html#AuroraDSQL.Waiter.ClusterNotExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/waiters/#clusternotexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetClusterInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/waiter/ClusterNotExists.html#AuroraDSQL.Waiter.ClusterNotExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/waiters/#clusternotexistswaiter)
        """
