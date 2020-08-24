"""
Main interface for compute-optimizer service.

Usage::

    ```python
    import boto3
    from mypy_boto3_compute_optimizer import (
        Client,
        ComputeOptimizerClient,
    )

    session = boto3.Session()

    client: ComputeOptimizerClient = boto3.client("compute-optimizer")
    session_client: ComputeOptimizerClient = session.client("compute-optimizer")
    ```
"""
from mypy_boto3_compute_optimizer.client import ComputeOptimizerClient

Client = ComputeOptimizerClient


__all__ = ("Client", "ComputeOptimizerClient")
