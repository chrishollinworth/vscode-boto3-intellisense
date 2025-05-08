"""
Main interface for lexv2-models service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lexv2_models import (
        BotAliasAvailableWaiter,
        BotAvailableWaiter,
        BotExportCompletedWaiter,
        BotImportCompletedWaiter,
        BotLocaleBuiltWaiter,
        BotLocaleCreatedWaiter,
        BotLocaleExpressTestingAvailableWaiter,
        BotVersionAvailableWaiter,
        Client,
        LexModelsV2Client,
    )

    session = Session()
    client: LexModelsV2Client = session.client("lexv2-models")

    bot_alias_available_waiter: BotAliasAvailableWaiter = client.get_waiter("bot_alias_available")
    bot_available_waiter: BotAvailableWaiter = client.get_waiter("bot_available")
    bot_export_completed_waiter: BotExportCompletedWaiter = client.get_waiter("bot_export_completed")
    bot_import_completed_waiter: BotImportCompletedWaiter = client.get_waiter("bot_import_completed")
    bot_locale_built_waiter: BotLocaleBuiltWaiter = client.get_waiter("bot_locale_built")
    bot_locale_created_waiter: BotLocaleCreatedWaiter = client.get_waiter("bot_locale_created")
    bot_locale_express_testing_available_waiter: BotLocaleExpressTestingAvailableWaiter = client.get_waiter("bot_locale_express_testing_available")
    bot_version_available_waiter: BotVersionAvailableWaiter = client.get_waiter("bot_version_available")
    ```
"""

from .client import LexModelsV2Client
from .waiter import (
    BotAliasAvailableWaiter,
    BotAvailableWaiter,
    BotExportCompletedWaiter,
    BotImportCompletedWaiter,
    BotLocaleBuiltWaiter,
    BotLocaleCreatedWaiter,
    BotLocaleExpressTestingAvailableWaiter,
    BotVersionAvailableWaiter,
)

Client = LexModelsV2Client

__all__ = (
    "BotAliasAvailableWaiter",
    "BotAvailableWaiter",
    "BotExportCompletedWaiter",
    "BotImportCompletedWaiter",
    "BotLocaleBuiltWaiter",
    "BotLocaleCreatedWaiter",
    "BotLocaleExpressTestingAvailableWaiter",
    "BotVersionAvailableWaiter",
    "Client",
    "LexModelsV2Client",
)
