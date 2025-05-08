"""
Main interface for geo-maps service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_geo_maps import (
        Client,
        LocationServiceMapsV2Client,
    )

    session = Session()
    client: LocationServiceMapsV2Client = session.client("geo-maps")
    ```
"""

from .client import LocationServiceMapsV2Client

Client = LocationServiceMapsV2Client

__all__ = ("Client", "LocationServiceMapsV2Client")
