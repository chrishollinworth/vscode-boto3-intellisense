"""
Main interface for sagemaker-featurestore-runtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_featurestore_runtime import (
        Client,
        SageMakerFeatureStoreRuntimeClient,
    )

    session = Session()
    client: SageMakerFeatureStoreRuntimeClient = session.client("sagemaker-featurestore-runtime")
    ```
"""

from .client import SageMakerFeatureStoreRuntimeClient

Client = SageMakerFeatureStoreRuntimeClient

__all__ = ("Client", "SageMakerFeatureStoreRuntimeClient")
