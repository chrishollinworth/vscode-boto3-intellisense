"""
Main interface for chime-sdk-voice service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_voice import (
        ChimeSDKVoiceClient,
        Client,
        ListSipMediaApplicationsPaginator,
        ListSipRulesPaginator,
    )

    session = boto3.Session()

    client: ChimeSDKVoiceClient = boto3.client("chime-sdk-voice")
    session_client: ChimeSDKVoiceClient = session.client("chime-sdk-voice")

    list_sip_media_applications_paginator: ListSipMediaApplicationsPaginator = client.get_paginator("list_sip_media_applications")
    list_sip_rules_paginator: ListSipRulesPaginator = client.get_paginator("list_sip_rules")
    ```
"""

from .client import ChimeSDKVoiceClient
from .paginator import ListSipMediaApplicationsPaginator, ListSipRulesPaginator

Client = ChimeSDKVoiceClient

__all__ = (
    "ChimeSDKVoiceClient",
    "Client",
    "ListSipMediaApplicationsPaginator",
    "ListSipRulesPaginator",
)
