"""
Main interface for secretsmanager service.

Usage::

    ```python
    import boto3
    from mypy_boto3_secretsmanager import (
        Client,
        ListSecretsPaginator,
        SecretsManagerClient,
    )

    session = boto3.Session()

    client: SecretsManagerClient = boto3.client("secretsmanager")
    session_client: SecretsManagerClient = session.client("secretsmanager")

    list_secrets_paginator: ListSecretsPaginator = client.get_paginator("list_secrets")
    ```
"""
from .client import SecretsManagerClient
from .paginator import ListSecretsPaginator

Client = SecretsManagerClient

__all__ = ("Client", "ListSecretsPaginator", "SecretsManagerClient")
