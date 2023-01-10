"""
Main interface for sagemaker-metrics service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_metrics import (
        Client,
        SageMakerMetricsClient,
    )

    session = boto3.Session()

    client: SageMakerMetricsClient = boto3.client("sagemaker-metrics")
    session_client: SageMakerMetricsClient = session.client("sagemaker-metrics")
    ```
"""
from .client import SageMakerMetricsClient

Client = SageMakerMetricsClient

__all__ = ("Client", "SageMakerMetricsClient")
