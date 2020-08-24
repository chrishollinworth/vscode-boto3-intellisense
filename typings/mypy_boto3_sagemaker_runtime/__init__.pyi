"""
Main interface for sagemaker-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_runtime import (
        Client,
        SageMakerRuntimeClient,
    )

    session = boto3.Session()

    client: SageMakerRuntimeClient = boto3.client("sagemaker-runtime")
    session_client: SageMakerRuntimeClient = session.client("sagemaker-runtime")
    ```
"""
from mypy_boto3_sagemaker_runtime.client import SageMakerRuntimeClient

Client = SageMakerRuntimeClient


__all__ = ("Client", "SageMakerRuntimeClient")
