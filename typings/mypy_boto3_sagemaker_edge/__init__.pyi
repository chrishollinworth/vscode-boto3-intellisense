"""
Main interface for sagemaker-edge service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_edge import (
        Client,
        SagemakerEdgeManagerClient,
    )

    session = boto3.Session()

    client: SagemakerEdgeManagerClient = boto3.client("sagemaker-edge")
    session_client: SagemakerEdgeManagerClient = session.client("sagemaker-edge")
    ```
"""
from mypy_boto3_sagemaker_edge.client import SagemakerEdgeManagerClient

Client = SagemakerEdgeManagerClient


__all__ = ("Client", "SagemakerEdgeManagerClient")
