"""
Main interface for personalize-runtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_personalize_runtime import (
        Client,
        PersonalizeRuntimeClient,
    )

    session = Session()
    client: PersonalizeRuntimeClient = session.client("personalize-runtime")
    ```
"""

from .client import PersonalizeRuntimeClient

Client = PersonalizeRuntimeClient

__all__ = ("Client", "PersonalizeRuntimeClient")
