"""
Main interface for signer service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_signer import (
        Client,
        ListSigningJobsPaginator,
        ListSigningPlatformsPaginator,
        ListSigningProfilesPaginator,
        SignerClient,
        SuccessfulSigningJobWaiter,
    )

    session = Session()
    client: SignerClient = session.client("signer")

    successful_signing_job_waiter: SuccessfulSigningJobWaiter = client.get_waiter("successful_signing_job")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""

from .client import SignerClient
from .paginator import (
    ListSigningJobsPaginator,
    ListSigningPlatformsPaginator,
    ListSigningProfilesPaginator,
)
from .waiter import SuccessfulSigningJobWaiter

Client = SignerClient

__all__ = (
    "Client",
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
    "SignerClient",
    "SuccessfulSigningJobWaiter",
)
