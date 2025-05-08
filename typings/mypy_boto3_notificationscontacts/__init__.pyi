"""
Main interface for notificationscontacts service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_notificationscontacts import (
        Client,
        ListEmailContactsPaginator,
        UserNotificationsContactsClient,
    )

    session = Session()
    client: UserNotificationsContactsClient = session.client("notificationscontacts")

    list_email_contacts_paginator: ListEmailContactsPaginator = client.get_paginator("list_email_contacts")
    ```
"""

from .client import UserNotificationsContactsClient
from .paginator import ListEmailContactsPaginator

Client = UserNotificationsContactsClient

__all__ = ("Client", "ListEmailContactsPaginator", "UserNotificationsContactsClient")
