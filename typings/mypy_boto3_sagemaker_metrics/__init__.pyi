"""
Main interface for sagemaker-metrics service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_metrics import (
        Client,
        SageMakerMetricsClient,
    )

    session = Session()
    client: SageMakerMetricsClient = session.client("sagemaker-metrics")
    ```
"""

from .client import SageMakerMetricsClient

Client = SageMakerMetricsClient

__all__ = ("Client", "SageMakerMetricsClient")
