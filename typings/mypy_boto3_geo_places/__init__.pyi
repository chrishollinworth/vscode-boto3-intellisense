"""
Main interface for geo-places service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_geo_places import (
        Client,
        LocationServicePlacesV2Client,
    )

    session = Session()
    client: LocationServicePlacesV2Client = session.client("geo-places")
    ```
"""

from .client import LocationServicePlacesV2Client

Client = LocationServicePlacesV2Client

__all__ = ("Client", "LocationServicePlacesV2Client")
