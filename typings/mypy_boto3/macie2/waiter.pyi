"""
Type annotations for macie2 service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_macie2.client import Macie2Client
    from mypy_boto3_macie2.waiter import (
        FindingRevealedWaiter,
    )

    session = Session()
    client: Macie2Client = session.client("macie2")

    finding_revealed_waiter: FindingRevealedWaiter = client.get_waiter("finding_revealed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetSensitiveDataOccurrencesRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("FindingRevealedWaiter",)

class FindingRevealedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/waiter/FindingRevealed.html#Macie2.Waiter.FindingRevealed)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters/#findingrevealedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSensitiveDataOccurrencesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/waiter/FindingRevealed.html#Macie2.Waiter.FindingRevealed.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters/#findingrevealedwaiter)
        """
