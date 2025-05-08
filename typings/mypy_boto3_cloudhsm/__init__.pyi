"""
Main interface for cloudhsm service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudhsm import (
        Client,
        CloudHSMClient,
        ListHapgsPaginator,
        ListHsmsPaginator,
        ListLunaClientsPaginator,
    )

    session = Session()
    client: CloudHSMClient = session.client("cloudhsm")

    list_hapgs_paginator: ListHapgsPaginator = client.get_paginator("list_hapgs")
    list_hsms_paginator: ListHsmsPaginator = client.get_paginator("list_hsms")
    list_luna_clients_paginator: ListLunaClientsPaginator = client.get_paginator("list_luna_clients")
    ```
"""

from .client import CloudHSMClient
from .paginator import ListHapgsPaginator, ListHsmsPaginator, ListLunaClientsPaginator

Client = CloudHSMClient

__all__ = (
    "Client",
    "CloudHSMClient",
    "ListHapgsPaginator",
    "ListHsmsPaginator",
    "ListLunaClientsPaginator",
)
