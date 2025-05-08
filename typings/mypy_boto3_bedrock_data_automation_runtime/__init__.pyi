"""
Main interface for bedrock-data-automation-runtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_data_automation_runtime import (
        Client,
        RuntimeforBedrockDataAutomationClient,
    )

    session = Session()
    client: RuntimeforBedrockDataAutomationClient = session.client("bedrock-data-automation-runtime")
    ```
"""

from .client import RuntimeforBedrockDataAutomationClient

Client = RuntimeforBedrockDataAutomationClient

__all__ = ("Client", "RuntimeforBedrockDataAutomationClient")
