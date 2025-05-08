"""
Main interface for forecastquery service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_forecastquery import (
        Client,
        ForecastQueryServiceClient,
    )

    session = Session()
    client: ForecastQueryServiceClient = session.client("forecastquery")
    ```
"""

from .client import ForecastQueryServiceClient

Client = ForecastQueryServiceClient

__all__ = ("Client", "ForecastQueryServiceClient")
