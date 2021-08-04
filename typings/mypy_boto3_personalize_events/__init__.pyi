"""
Main interface for personalize-events service.

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize_events import (
        Client,
        PersonalizeEventsClient,
    )

    session = boto3.Session()

    client: PersonalizeEventsClient = boto3.client("personalize-events")
    session_client: PersonalizeEventsClient = session.client("personalize-events")
    ```
"""
from .client import PersonalizeEventsClient

Client = PersonalizeEventsClient

__all__ = ("Client", "PersonalizeEventsClient")
