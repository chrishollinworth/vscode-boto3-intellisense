"""
Main interface for forecastquery service.

Usage::

    ```python
    import boto3
    from mypy_boto3_forecastquery import (
        Client,
        ForecastQueryServiceClient,
    )

    session = boto3.Session()

    client: ForecastQueryServiceClient = boto3.client("forecastquery")
    session_client: ForecastQueryServiceClient = session.client("forecastquery")
    ```
"""
from mypy_boto3_forecastquery.client import ForecastQueryServiceClient

Client = ForecastQueryServiceClient


__all__ = ("Client", "ForecastQueryServiceClient")
