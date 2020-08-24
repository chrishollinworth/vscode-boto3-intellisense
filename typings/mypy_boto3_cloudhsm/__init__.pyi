"""
Main interface for cloudhsm service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudhsm import (
        Client,
        CloudHSMClient,
        ListHapgsPaginator,
        ListHsmsPaginator,
        ListLunaClientsPaginator,
    )

    session = boto3.Session()

    client: CloudHSMClient = boto3.client("cloudhsm")
    session_client: CloudHSMClient = session.client("cloudhsm")

    list_hapgs_paginator: ListHapgsPaginator = client.get_paginator("list_hapgs")
    list_hsms_paginator: ListHsmsPaginator = client.get_paginator("list_hsms")
    list_luna_clients_paginator: ListLunaClientsPaginator = client.get_paginator("list_luna_clients")
    ```
"""
from mypy_boto3_cloudhsm.client import CloudHSMClient
from mypy_boto3_cloudhsm.paginator import (
    ListHapgsPaginator,
    ListHsmsPaginator,
    ListLunaClientsPaginator,
)

Client = CloudHSMClient


__all__ = (
    "Client",
    "CloudHSMClient",
    "ListHapgsPaginator",
    "ListHsmsPaginator",
    "ListLunaClientsPaginator",
)
