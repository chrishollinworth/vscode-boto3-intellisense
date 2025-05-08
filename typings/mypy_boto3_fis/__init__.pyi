"""
Main interface for fis service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_fis import (
        Client,
        FISClient,
        ListActionsPaginator,
        ListExperimentResolvedTargetsPaginator,
        ListExperimentTemplatesPaginator,
        ListExperimentsPaginator,
        ListTargetAccountConfigurationsPaginator,
        ListTargetResourceTypesPaginator,
    )

    session = Session()
    client: FISClient = session.client("fis")

    list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
    list_experiment_resolved_targets_paginator: ListExperimentResolvedTargetsPaginator = client.get_paginator("list_experiment_resolved_targets")
    list_experiment_templates_paginator: ListExperimentTemplatesPaginator = client.get_paginator("list_experiment_templates")
    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_target_account_configurations_paginator: ListTargetAccountConfigurationsPaginator = client.get_paginator("list_target_account_configurations")
    list_target_resource_types_paginator: ListTargetResourceTypesPaginator = client.get_paginator("list_target_resource_types")
    ```
"""

from .client import FISClient
from .paginator import (
    ListActionsPaginator,
    ListExperimentResolvedTargetsPaginator,
    ListExperimentsPaginator,
    ListExperimentTemplatesPaginator,
    ListTargetAccountConfigurationsPaginator,
    ListTargetResourceTypesPaginator,
)

Client = FISClient

__all__ = (
    "Client",
    "FISClient",
    "ListActionsPaginator",
    "ListExperimentResolvedTargetsPaginator",
    "ListExperimentTemplatesPaginator",
    "ListExperimentsPaginator",
    "ListTargetAccountConfigurationsPaginator",
    "ListTargetResourceTypesPaginator",
)
