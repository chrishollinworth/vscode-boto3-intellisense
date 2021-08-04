"""
Main interface for s3control service.

Usage::

    ```python
    import boto3
    from mypy_boto3_s3control import (
        Client,
        ListAccessPointsForObjectLambdaPaginator,
        S3ControlClient,
    )

    session = boto3.Session()

    client: S3ControlClient = boto3.client("s3control")
    session_client: S3ControlClient = session.client("s3control")

    list_access_points_for_object_lambda_paginator: ListAccessPointsForObjectLambdaPaginator = client.get_paginator("list_access_points_for_object_lambda")
    ```
"""
from .client import S3ControlClient
from .paginator import ListAccessPointsForObjectLambdaPaginator

Client = S3ControlClient

__all__ = ("Client", "ListAccessPointsForObjectLambdaPaginator", "S3ControlClient")
