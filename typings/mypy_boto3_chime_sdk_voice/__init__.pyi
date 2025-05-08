"""
Main interface for chime-sdk-voice service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_voice import (
        ChimeSDKVoiceClient,
        Client,
        ListSipMediaApplicationsPaginator,
        ListSipRulesPaginator,
    )

    session = Session()
    client: ChimeSDKVoiceClient = session.client("chime-sdk-voice")

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
