"""
Main interface for b2bi service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_b2bi import (
        B2BIClient,
        Client,
        ListCapabilitiesPaginator,
        ListPartnershipsPaginator,
        ListProfilesPaginator,
        ListTransformersPaginator,
        TransformerJobSucceededWaiter,
    )

    session = Session()
    client: B2BIClient = session.client("b2bi")

    transformer_job_succeeded_waiter: TransformerJobSucceededWaiter = client.get_waiter("transformer_job_succeeded")

    list_capabilities_paginator: ListCapabilitiesPaginator = client.get_paginator("list_capabilities")
    list_partnerships_paginator: ListPartnershipsPaginator = client.get_paginator("list_partnerships")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_transformers_paginator: ListTransformersPaginator = client.get_paginator("list_transformers")
    ```
"""

from .client import B2BIClient
from .paginator import (
    ListCapabilitiesPaginator,
    ListPartnershipsPaginator,
    ListProfilesPaginator,
    ListTransformersPaginator,
)
from .waiter import TransformerJobSucceededWaiter

Client = B2BIClient

__all__ = (
    "B2BIClient",
    "Client",
    "ListCapabilitiesPaginator",
    "ListPartnershipsPaginator",
    "ListProfilesPaginator",
    "ListTransformersPaginator",
    "TransformerJobSucceededWaiter",
)
