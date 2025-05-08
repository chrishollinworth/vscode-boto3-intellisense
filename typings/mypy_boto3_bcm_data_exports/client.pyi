"""
Type annotations for bcm-data-exports service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bcm_data_exports.client import BillingandCostManagementDataExportsClient

    session = Session()
    client: BillingandCostManagementDataExportsClient = session.client("bcm-data-exports")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListExecutionsPaginator, ListExportsPaginator, ListTablesPaginator
from .type_defs import (
    CreateExportRequestTypeDef,
    CreateExportResponseTypeDef,
    DeleteExportRequestTypeDef,
    DeleteExportResponseTypeDef,
    GetExecutionRequestTypeDef,
    GetExecutionResponseTypeDef,
    GetExportRequestTypeDef,
    GetExportResponseTypeDef,
    GetTableRequestTypeDef,
    GetTableResponseTypeDef,
    ListExecutionsRequestTypeDef,
    ListExecutionsResponseTypeDef,
    ListExportsRequestTypeDef,
    ListExportsResponseTypeDef,
    ListTablesRequestTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateExportRequestTypeDef,
    UpdateExportResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BillingandCostManagementDataExportsClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BillingandCostManagementDataExportsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BillingandCostManagementDataExportsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#generate_presigned_url)
        """

    def create_export(
        self, **kwargs: Unpack[CreateExportRequestTypeDef]
    ) -> CreateExportResponseTypeDef:
        """
        Creates a data export and specifies the data query, the delivery preference,
        and any optional resource tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/create_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#create_export)
        """

    def delete_export(
        self, **kwargs: Unpack[DeleteExportRequestTypeDef]
    ) -> DeleteExportResponseTypeDef:
        """
        Deletes an existing data export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/delete_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#delete_export)
        """

    def get_execution(
        self, **kwargs: Unpack[GetExecutionRequestTypeDef]
    ) -> GetExecutionResponseTypeDef:
        """
        Exports data based on the source data update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/get_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#get_execution)
        """

    def get_export(self, **kwargs: Unpack[GetExportRequestTypeDef]) -> GetExportResponseTypeDef:
        """
        Views the definition of an existing data export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/get_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#get_export)
        """

    def get_table(self, **kwargs: Unpack[GetTableRequestTypeDef]) -> GetTableResponseTypeDef:
        """
        Returns the metadata for the specified table and table properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/get_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#get_table)
        """

    def list_executions(
        self, **kwargs: Unpack[ListExecutionsRequestTypeDef]
    ) -> ListExecutionsResponseTypeDef:
        """
        Lists the historical executions for the export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/list_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#list_executions)
        """

    def list_exports(
        self, **kwargs: Unpack[ListExportsRequestTypeDef]
    ) -> ListExportsResponseTypeDef:
        """
        Lists all data export definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/list_exports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#list_exports)
        """

    def list_tables(self, **kwargs: Unpack[ListTablesRequestTypeDef]) -> ListTablesResponseTypeDef:
        """
        Lists all available tables in data exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/list_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#list_tables)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List tags associated with an existing data export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags for an existing data export definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes tags associated with an existing data export definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#untag_resource)
        """

    def update_export(
        self, **kwargs: Unpack[UpdateExportRequestTypeDef]
    ) -> UpdateExportResponseTypeDef:
        """
        Updates an existing data export by overwriting all export parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/update_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#update_export)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_executions"]
    ) -> ListExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_exports"]
    ) -> ListExportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tables"]
    ) -> ListTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client/#get_paginator)
        """
