"""
Main interface for apigatewaymanagementapi service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_apigatewaymanagementapi import (
        ApiGatewayManagementApiClient,
        Client,
    )

    session = Session()
    client: ApiGatewayManagementApiClient = session.client("apigatewaymanagementapi")
    ```
"""

from .client import ApiGatewayManagementApiClient

Client = ApiGatewayManagementApiClient

__all__ = ("ApiGatewayManagementApiClient", "Client")
