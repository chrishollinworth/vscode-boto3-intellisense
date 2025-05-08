"""
Main interface for cognito-identity service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cognito_identity import (
        Client,
        CognitoIdentityClient,
        ListIdentityPoolsPaginator,
    )

    session = Session()
    client: CognitoIdentityClient = session.client("cognito-identity")

    list_identity_pools_paginator: ListIdentityPoolsPaginator = client.get_paginator("list_identity_pools")
    ```
"""

from .client import CognitoIdentityClient
from .paginator import ListIdentityPoolsPaginator

Client = CognitoIdentityClient

__all__ = ("Client", "CognitoIdentityClient", "ListIdentityPoolsPaginator")
