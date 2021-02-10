"""
Main interface for lexv2-models service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_models import (
        Client,
        LexModelsV2Client,
    )

    session = boto3.Session()

    client: LexModelsV2Client = boto3.client("lexv2-models")
    session_client: LexModelsV2Client = session.client("lexv2-models")
    ```
"""
from mypy_boto3_lexv2_models.client import LexModelsV2Client

Client = LexModelsV2Client


__all__ = ("Client", "LexModelsV2Client")
