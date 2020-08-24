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
        SignerClient,
        SuccessfulSigningJobWaiter,
    )

    session = boto3.Session()

    client: SignerClient = boto3.client("signer")
    session_client: SignerClient = session.client("signer")

    successful_signing_job_waiter: SuccessfulSigningJobWaiter = client.get_waiter("successful_signing_job")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""
from mypy_boto3_signer.client import SignerClient
from mypy_boto3_signer.paginator import (
    ListSigningJobsPaginator,
    ListSigningPlatformsPaginator,
    ListSigningProfilesPaginator,
)
from mypy_boto3_signer.waiter import SuccessfulSigningJobWaiter

Client = SignerClient


__all__ = (
    "Client",
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
    "SignerClient",
    "SuccessfulSigningJobWaiter",
)
