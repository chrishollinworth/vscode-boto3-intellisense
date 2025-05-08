"""
Main interface for sagemaker-edge service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_edge import (
        Client,
        SagemakerEdgeManagerClient,
    )

    session = Session()
    client: SagemakerEdgeManagerClient = session.client("sagemaker-edge")
    ```
"""

from .client import SagemakerEdgeManagerClient

Client = SagemakerEdgeManagerClient

__all__ = ("Client", "SagemakerEdgeManagerClient")
