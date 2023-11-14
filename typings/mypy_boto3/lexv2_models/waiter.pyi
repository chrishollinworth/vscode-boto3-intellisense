"""
Type annotations for lexv2-models service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_lexv2_models import LexModelsV2Client
    from mypy_boto3_lexv2_models.waiter import (
        BotAliasAvailableWaiter,
        BotAvailableWaiter,
        BotExportCompletedWaiter,
        BotImportCompletedWaiter,
        BotLocaleBuiltWaiter,
        BotLocaleCreatedWaiter,
        BotLocaleExpressTestingAvailableWaiter,
        BotVersionAvailableWaiter,
    )

    client: LexModelsV2Client = boto3.client("lexv2-models")

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
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "BotAliasAvailableWaiter",
    "BotAvailableWaiter",
    "BotExportCompletedWaiter",
    "BotImportCompletedWaiter",
    "BotLocaleBuiltWaiter",
    "BotLocaleCreatedWaiter",
    "BotLocaleExpressTestingAvailableWaiter",
    "BotVersionAvailableWaiter",
)

class BotAliasAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotAliasAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botaliasavailablewaiter)
    """

    def wait(
        self, *, botAliasId: str, botId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotAliasAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botaliasavailablewaiter)
        """

class BotAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botavailablewaiter)
    """

    def wait(self, *, botId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botavailablewaiter)
        """

class BotExportCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotExportCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botexportcompletedwaiter)
    """

    def wait(self, *, exportId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotExportCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botexportcompletedwaiter)
        """

class BotImportCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotImportCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botimportcompletedwaiter)
    """

    def wait(self, *, importId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotImportCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botimportcompletedwaiter)
        """

class BotLocaleBuiltWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleBuilt)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocalebuiltwaiter)
    """

    def wait(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleBuilt.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocalebuiltwaiter)
        """

class BotLocaleCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocalecreatedwaiter)
    """

    def wait(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocalecreatedwaiter)
        """

class BotLocaleExpressTestingAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleExpressTestingAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocaleexpresstestingavailablewaiter)
    """

    def wait(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleExpressTestingAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocaleexpresstestingavailablewaiter)
        """

class BotVersionAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotVersionAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botversionavailablewaiter)
    """

    def wait(
        self, *, botId: str, botVersion: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotVersionAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botversionavailablewaiter)
        """
