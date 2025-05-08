"""
Type annotations for marketplace-agreement service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_agreement.client import AgreementServiceClient

    session = Session()
    client: AgreementServiceClient = session.client("marketplace-agreement")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DescribeAgreementInputTypeDef,
    DescribeAgreementOutputTypeDef,
    GetAgreementTermsInputTypeDef,
    GetAgreementTermsOutputTypeDef,
    SearchAgreementsInputTypeDef,
    SearchAgreementsOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("AgreementServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AgreementServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AgreementServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#generate_presigned_url)
        """

    def describe_agreement(
        self, **kwargs: Unpack[DescribeAgreementInputTypeDef]
    ) -> DescribeAgreementOutputTypeDef:
        """
        Provides details about an agreement, such as the proposer, acceptor, start
        date, and end date.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement/client/describe_agreement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#describe_agreement)
        """

    def get_agreement_terms(
        self, **kwargs: Unpack[GetAgreementTermsInputTypeDef]
    ) -> GetAgreementTermsOutputTypeDef:
        """
        Obtains details about the terms in an agreement that you participated in as
        proposer or acceptor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement/client/get_agreement_terms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#get_agreement_terms)
        """

    def search_agreements(
        self, **kwargs: Unpack[SearchAgreementsInputTypeDef]
    ) -> SearchAgreementsOutputTypeDef:
        """
        Searches across all agreements that a proposer or an acceptor has in AWS
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement/client/search_agreements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#search_agreements)
        """
