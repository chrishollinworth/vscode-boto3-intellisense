"""
Main interface for application-insights service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_application_insights import (
        ApplicationInsightsClient,
        Client,
    )

    session = Session()
    client: ApplicationInsightsClient = session.client("application-insights")
    ```
"""

from .client import ApplicationInsightsClient

Client = ApplicationInsightsClient

__all__ = ("ApplicationInsightsClient", "Client")
