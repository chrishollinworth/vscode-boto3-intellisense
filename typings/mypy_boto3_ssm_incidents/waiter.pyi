"""
Type annotations for ssm-incidents service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm_incidents.client import SSMIncidentsClient
    from mypy_boto3_ssm_incidents.waiter import (
        WaitForReplicationSetActiveWaiter,
        WaitForReplicationSetDeletedWaiter,
    )

    session = Session()
    client: SSMIncidentsClient = session.client("ssm-incidents")

    wait_for_replication_set_active_waiter: WaitForReplicationSetActiveWaiter = client.get_waiter("wait_for_replication_set_active")
    wait_for_replication_set_deleted_waiter: WaitForReplicationSetDeletedWaiter = client.get_waiter("wait_for_replication_set_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetReplicationSetInputWaitExtraTypeDef, GetReplicationSetInputWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("WaitForReplicationSetActiveWaiter", "WaitForReplicationSetDeletedWaiter")

class WaitForReplicationSetActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/waiter/WaitForReplicationSetActive.html#SSMIncidents.Waiter.WaitForReplicationSetActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters/#waitforreplicationsetactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetReplicationSetInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/waiter/WaitForReplicationSetActive.html#SSMIncidents.Waiter.WaitForReplicationSetActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters/#waitforreplicationsetactivewaiter)
        """

class WaitForReplicationSetDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/waiter/WaitForReplicationSetDeleted.html#SSMIncidents.Waiter.WaitForReplicationSetDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters/#waitforreplicationsetdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetReplicationSetInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/waiter/WaitForReplicationSetDeleted.html#SSMIncidents.Waiter.WaitForReplicationSetDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters/#waitforreplicationsetdeletedwaiter)
        """
