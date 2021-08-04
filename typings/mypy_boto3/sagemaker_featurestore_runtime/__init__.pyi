"""
Main interface for sagemaker-featurestore-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_featurestore_runtime import (
        Client,
        SageMakerFeatureStoreRuntimeClient,
    )

    session = boto3.Session()

    client: SageMakerFeatureStoreRuntimeClient = boto3.client("sagemaker-featurestore-runtime")
    session_client: SageMakerFeatureStoreRuntimeClient = session.client("sagemaker-featurestore-runtime")
    ```
"""
from .client import SageMakerFeatureStoreRuntimeClient

Client = SageMakerFeatureStoreRuntimeClient

__all__ = ("Client", "SageMakerFeatureStoreRuntimeClient")
