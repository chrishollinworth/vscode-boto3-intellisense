"""
Main interface for signer service.

Usage::

    ```python
    import boto3
    from mypy_boto3_signer import (
        Client,
        ListSigningJobsPaginator,
        ListSigningPlatformsPaginator,
        ListSigningProfilesPaginator,
        SuccessfulSigningJobWaiter,
        signerClient,
    )

    session = boto3.Session()

    client: signerClient = boto3.client("signer")
    session_client: signerClient = session.client("signer")

    successful_signing_job_waiter: SuccessfulSigningJobWaiter = client.get_waiter("successful_signing_job")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""
from .client import signerClient
from .paginator import (
    ListSigningJobsPaginator,
    ListSigningPlatformsPaginator,
    ListSigningProfilesPaginator,
)
from .waiter import SuccessfulSigningJobWaiter

Client = signerClient

__all__ = (
    "Client",
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
    "SuccessfulSigningJobWaiter",
    "signerClient",
)
