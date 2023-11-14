"""
Main interface for personalize-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize_runtime import (
        Client,
        PersonalizeRuntimeClient,
    )

    session = boto3.Session()

    client: PersonalizeRuntimeClient = boto3.client("personalize-runtime")
    session_client: PersonalizeRuntimeClient = session.client("personalize-runtime")
    ```
"""
from .client import PersonalizeRuntimeClient

Client = PersonalizeRuntimeClient

__all__ = ("Client", "PersonalizeRuntimeClient")
