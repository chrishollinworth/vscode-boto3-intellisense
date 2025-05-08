"""
Type annotations for mwaa service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mwaa.client import MWAAClient

    session = Session()
    client: MWAAClient = session.client("mwaa")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListEnvironmentsPaginator
from .type_defs import (
    CreateCliTokenRequestTypeDef,
    CreateCliTokenResponseTypeDef,
    CreateEnvironmentInputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateWebLoginTokenRequestTypeDef,
    CreateWebLoginTokenResponseTypeDef,
    DeleteEnvironmentInputTypeDef,
    GetEnvironmentInputTypeDef,
    GetEnvironmentOutputTypeDef,
    InvokeRestApiRequestTypeDef,
    InvokeRestApiResponseTypeDef,
    ListEnvironmentsInputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PublishMetricsInputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateEnvironmentInputTypeDef,
    UpdateEnvironmentOutputTypeDef,
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

__all__ = ("MWAAClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RestApiClientException: Type[BotocoreClientError]
    RestApiServerException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MWAAClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MWAAClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#generate_presigned_url)
        """

    def create_cli_token(
        self, **kwargs: Unpack[CreateCliTokenRequestTypeDef]
    ) -> CreateCliTokenResponseTypeDef:
        """
        Creates a CLI token for the Airflow CLI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/create_cli_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#create_cli_token)
        """

    def create_environment(
        self, **kwargs: Unpack[CreateEnvironmentInputTypeDef]
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Creates an Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/create_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#create_environment)
        """

    def create_web_login_token(
        self, **kwargs: Unpack[CreateWebLoginTokenRequestTypeDef]
    ) -> CreateWebLoginTokenResponseTypeDef:
        """
        Creates a web login token for the Airflow Web UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/create_web_login_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#create_web_login_token)
        """

    def delete_environment(self, **kwargs: Unpack[DeleteEnvironmentInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/delete_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#delete_environment)
        """

    def get_environment(
        self, **kwargs: Unpack[GetEnvironmentInputTypeDef]
    ) -> GetEnvironmentOutputTypeDef:
        """
        Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/get_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#get_environment)
        """

    def invoke_rest_api(
        self, **kwargs: Unpack[InvokeRestApiRequestTypeDef]
    ) -> InvokeRestApiResponseTypeDef:
        """
        Invokes the Apache Airflow REST API on the webserver with the specified inputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/invoke_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#invoke_rest_api)
        """

    def list_environments(
        self, **kwargs: Unpack[ListEnvironmentsInputTypeDef]
    ) -> ListEnvironmentsOutputTypeDef:
        """
        Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/list_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#list_environments)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the key-value tag pairs associated to the Amazon Managed Workflows for
        Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#list_tags_for_resource)
        """

    def publish_metrics(self, **kwargs: Unpack[PublishMetricsInputTypeDef]) -> Dict[str, Any]:
        """
        <b>Internal only</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/publish_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#publish_metrics)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Associates key-value tag pairs to your Amazon Managed Workflows for Apache
        Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes key-value tag pairs associated to your Amazon Managed Workflows for
        Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#untag_resource)
        """

    def update_environment(
        self, **kwargs: Unpack[UpdateEnvironmentInputTypeDef]
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/update_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#update_environment)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client/#get_paginator)
        """
