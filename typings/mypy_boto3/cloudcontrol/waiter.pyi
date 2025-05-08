"""
Type annotations for cloudcontrol service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudcontrol.client import CloudControlApiClient
    from mypy_boto3_cloudcontrol.waiter import (
        ResourceRequestSuccessWaiter,
    )

    session = Session()
    client: CloudControlApiClient = session.client("cloudcontrol")

    resource_request_success_waiter: ResourceRequestSuccessWaiter = client.get_waiter("resource_request_success")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetResourceRequestStatusInputWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ResourceRequestSuccessWaiter",)

class ResourceRequestSuccessWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/waiter/ResourceRequestSuccess.html#CloudControlApi.Waiter.ResourceRequestSuccess)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/waiters/#resourcerequestsuccesswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceRequestStatusInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/waiter/ResourceRequestSuccess.html#CloudControlApi.Waiter.ResourceRequestSuccess.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/waiters/#resourcerequestsuccesswaiter)
        """
