"""
Main interface for translate service.

Usage::

    ```python
    import boto3
    from mypy_boto3_translate import (
        Client,
        ListTerminologiesPaginator,
        TranslateClient,
    )

    session = boto3.Session()

    client: TranslateClient = boto3.client("translate")
    session_client: TranslateClient = session.client("translate")

    list_terminologies_paginator: ListTerminologiesPaginator = client.get_paginator("list_terminologies")
    ```
"""
from .client import TranslateClient
from .paginator import ListTerminologiesPaginator

Client = TranslateClient

__all__ = ("Client", "ListTerminologiesPaginator", "TranslateClient")
