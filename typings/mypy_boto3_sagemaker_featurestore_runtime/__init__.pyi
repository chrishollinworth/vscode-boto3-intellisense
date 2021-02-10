"""
Main interface for sagemaker-featurestore-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_featurestore_runtime import (
        Client,
        SagemakerFeatureStoreRuntimeClient,
    )

    session = boto3.Session()

    client: SagemakerFeatureStoreRuntimeClient = boto3.client("sagemaker-featurestore-runtime")
    session_client: SagemakerFeatureStoreRuntimeClient = session.client("sagemaker-featurestore-runtime")
    ```
"""
from mypy_boto3_sagemaker_featurestore_runtime.client import SagemakerFeatureStoreRuntimeClient

Client = SagemakerFeatureStoreRuntimeClient


__all__ = ("Client", "SagemakerFeatureStoreRuntimeClient")
