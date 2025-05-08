"""
Type annotations for lexv2-models service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lexv2_models.client import LexModelsV2Client
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

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeBotAliasRequestWaitTypeDef,
    DescribeBotLocaleRequestWaitExtraExtraTypeDef,
    DescribeBotLocaleRequestWaitExtraTypeDef,
    DescribeBotLocaleRequestWaitTypeDef,
    DescribeBotRequestWaitTypeDef,
    DescribeBotVersionRequestWaitTypeDef,
    DescribeExportRequestWaitTypeDef,
    DescribeImportRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

class BotAliasAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotAliasAvailable.html#LexModelsV2.Waiter.BotAliasAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botaliasavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBotAliasRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotAliasAvailable.html#LexModelsV2.Waiter.BotAliasAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botaliasavailablewaiter)
        """

class BotAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotAvailable.html#LexModelsV2.Waiter.BotAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBotRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotAvailable.html#LexModelsV2.Waiter.BotAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botavailablewaiter)
        """

class BotExportCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotExportCompleted.html#LexModelsV2.Waiter.BotExportCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botexportcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotExportCompleted.html#LexModelsV2.Waiter.BotExportCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botexportcompletedwaiter)
        """

class BotImportCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotImportCompleted.html#LexModelsV2.Waiter.BotImportCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botimportcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImportRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotImportCompleted.html#LexModelsV2.Waiter.BotImportCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botimportcompletedwaiter)
        """

class BotLocaleBuiltWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotLocaleBuilt.html#LexModelsV2.Waiter.BotLocaleBuilt)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botlocalebuiltwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBotLocaleRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotLocaleBuilt.html#LexModelsV2.Waiter.BotLocaleBuilt.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botlocalebuiltwaiter)
        """

class BotLocaleCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotLocaleCreated.html#LexModelsV2.Waiter.BotLocaleCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botlocalecreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBotLocaleRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotLocaleCreated.html#LexModelsV2.Waiter.BotLocaleCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botlocalecreatedwaiter)
        """

class BotLocaleExpressTestingAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotLocaleExpressTestingAvailable.html#LexModelsV2.Waiter.BotLocaleExpressTestingAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botlocaleexpresstestingavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBotLocaleRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotLocaleExpressTestingAvailable.html#LexModelsV2.Waiter.BotLocaleExpressTestingAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botlocaleexpresstestingavailablewaiter)
        """

class BotVersionAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotVersionAvailable.html#LexModelsV2.Waiter.BotVersionAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botversionavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBotVersionRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/waiter/BotVersionAvailable.html#LexModelsV2.Waiter.BotVersionAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters/#botversionavailablewaiter)
        """
