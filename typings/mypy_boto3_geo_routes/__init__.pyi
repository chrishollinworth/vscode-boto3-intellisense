"""
Main interface for geo-routes service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_routes/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_geo_routes import (
        Client,
        LocationServiceRoutesV2Client,
    )

    session = Session()
    client: LocationServiceRoutesV2Client = session.client("geo-routes")
    ```
"""

from .client import LocationServiceRoutesV2Client

Client = LocationServiceRoutesV2Client

__all__ = ("Client", "LocationServiceRoutesV2Client")
