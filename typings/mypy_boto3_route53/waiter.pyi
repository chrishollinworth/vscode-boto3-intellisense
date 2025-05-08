"""
Type annotations for route53 service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53.client import Route53Client
    from mypy_boto3_route53.waiter import (
        ResourceRecordSetsChangedWaiter,
    )

    session = Session()
    client: Route53Client = session.client("route53")

    resource_record_sets_changed_waiter: ResourceRecordSetsChangedWaiter = client.get_waiter("resource_record_sets_changed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetChangeRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ResourceRecordSetsChangedWaiter",)

class ResourceRecordSetsChangedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/waiter/ResourceRecordSetsChanged.html#Route53.Waiter.ResourceRecordSetsChanged)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters/#resourcerecordsetschangedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetChangeRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/waiter/ResourceRecordSetsChanged.html#Route53.Waiter.ResourceRecordSetsChanged.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters/#resourcerecordsetschangedwaiter)
        """
