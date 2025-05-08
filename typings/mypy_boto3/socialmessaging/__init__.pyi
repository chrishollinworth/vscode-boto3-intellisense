"""
Main interface for socialmessaging service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_socialmessaging import (
        Client,
        EndUserMessagingSocialClient,
        ListLinkedWhatsAppBusinessAccountsPaginator,
    )

    session = Session()
    client: EndUserMessagingSocialClient = session.client("socialmessaging")

    list_linked_whatsapp_business_accounts_paginator: ListLinkedWhatsAppBusinessAccountsPaginator = client.get_paginator("list_linked_whatsapp_business_accounts")
    ```
"""

from .client import EndUserMessagingSocialClient
from .paginator import ListLinkedWhatsAppBusinessAccountsPaginator

Client = EndUserMessagingSocialClient

__all__ = ("Client", "EndUserMessagingSocialClient", "ListLinkedWhatsAppBusinessAccountsPaginator")
