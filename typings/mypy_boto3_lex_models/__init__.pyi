"""
Main interface for lex-models service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lex_models import (
        Client,
        GetBotAliasesPaginator,
        GetBotChannelAssociationsPaginator,
        GetBotVersionsPaginator,
        GetBotsPaginator,
        GetBuiltinIntentsPaginator,
        GetBuiltinSlotTypesPaginator,
        GetIntentVersionsPaginator,
        GetIntentsPaginator,
        GetSlotTypeVersionsPaginator,
        GetSlotTypesPaginator,
        LexModelBuildingServiceClient,
    )

    session = Session()
    client: LexModelBuildingServiceClient = session.client("lex-models")

    get_bot_aliases_paginator: GetBotAliasesPaginator = client.get_paginator("get_bot_aliases")
    get_bot_channel_associations_paginator: GetBotChannelAssociationsPaginator = client.get_paginator("get_bot_channel_associations")
    get_bot_versions_paginator: GetBotVersionsPaginator = client.get_paginator("get_bot_versions")
    get_bots_paginator: GetBotsPaginator = client.get_paginator("get_bots")
    get_builtin_intents_paginator: GetBuiltinIntentsPaginator = client.get_paginator("get_builtin_intents")
    get_builtin_slot_types_paginator: GetBuiltinSlotTypesPaginator = client.get_paginator("get_builtin_slot_types")
    get_intent_versions_paginator: GetIntentVersionsPaginator = client.get_paginator("get_intent_versions")
    get_intents_paginator: GetIntentsPaginator = client.get_paginator("get_intents")
    get_slot_type_versions_paginator: GetSlotTypeVersionsPaginator = client.get_paginator("get_slot_type_versions")
    get_slot_types_paginator: GetSlotTypesPaginator = client.get_paginator("get_slot_types")
    ```
"""

from .client import LexModelBuildingServiceClient
from .paginator import (
    GetBotAliasesPaginator,
    GetBotChannelAssociationsPaginator,
    GetBotsPaginator,
    GetBotVersionsPaginator,
    GetBuiltinIntentsPaginator,
    GetBuiltinSlotTypesPaginator,
    GetIntentsPaginator,
    GetIntentVersionsPaginator,
    GetSlotTypesPaginator,
    GetSlotTypeVersionsPaginator,
)

Client = LexModelBuildingServiceClient

__all__ = (
    "Client",
    "GetBotAliasesPaginator",
    "GetBotChannelAssociationsPaginator",
    "GetBotVersionsPaginator",
    "GetBotsPaginator",
    "GetBuiltinIntentsPaginator",
    "GetBuiltinSlotTypesPaginator",
    "GetIntentVersionsPaginator",
    "GetIntentsPaginator",
    "GetSlotTypeVersionsPaginator",
    "GetSlotTypesPaginator",
    "LexModelBuildingServiceClient",
)
