"""
Main interface for cognito-identity service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_identity import (
        Client,
        CognitoIdentityClient,
        ListIdentityPoolsPaginator,
    )

    session = boto3.Session()

    client: CognitoIdentityClient = boto3.client("cognito-identity")
    session_client: CognitoIdentityClient = session.client("cognito-identity")

    list_identity_pools_paginator: ListIdentityPoolsPaginator = client.get_paginator("list_identity_pools")
    ```
"""
from .client import CognitoIdentityClient
from .paginator import ListIdentityPoolsPaginator

Client = CognitoIdentityClient

__all__ = ("Client", "CognitoIdentityClient", "ListIdentityPoolsPaginator")
