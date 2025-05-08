"""
Main interface for bedrock-data-automation service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_data_automation import (
        Client,
        DataAutomationforBedrockClient,
        ListBlueprintsPaginator,
        ListDataAutomationProjectsPaginator,
    )

    session = Session()
    client: DataAutomationforBedrockClient = session.client("bedrock-data-automation")

    list_blueprints_paginator: ListBlueprintsPaginator = client.get_paginator("list_blueprints")
    list_data_automation_projects_paginator: ListDataAutomationProjectsPaginator = client.get_paginator("list_data_automation_projects")
    ```
"""

from .client import DataAutomationforBedrockClient
from .paginator import ListBlueprintsPaginator, ListDataAutomationProjectsPaginator

Client = DataAutomationforBedrockClient

__all__ = (
    "Client",
    "DataAutomationforBedrockClient",
    "ListBlueprintsPaginator",
    "ListDataAutomationProjectsPaginator",
)
