"""
Main interface for resiliencehub service.

Usage::

    ```python
    import boto3
    from mypy_boto3_resiliencehub import (
        Client,
        ListAppAssessmentResourceDriftsPaginator,
        ResilienceHubClient,
    )

    session = boto3.Session()

    client: ResilienceHubClient = boto3.client("resiliencehub")
    session_client: ResilienceHubClient = session.client("resiliencehub")

    list_app_assessment_resource_drifts_paginator: ListAppAssessmentResourceDriftsPaginator = client.get_paginator("list_app_assessment_resource_drifts")
    ```
"""

from .client import ResilienceHubClient
from .paginator import ListAppAssessmentResourceDriftsPaginator

Client = ResilienceHubClient

__all__ = ("Client", "ListAppAssessmentResourceDriftsPaginator", "ResilienceHubClient")
