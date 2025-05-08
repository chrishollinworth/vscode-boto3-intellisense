"""
Type annotations for taxsettings service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_taxsettings.client import TaxSettingsClient

    session = Session()
    client: TaxSettingsClient = session.client("taxsettings")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListSupplementalTaxRegistrationsPaginator,
    ListTaxExemptionsPaginator,
    ListTaxRegistrationsPaginator,
)
from .type_defs import (
    BatchDeleteTaxRegistrationRequestTypeDef,
    BatchDeleteTaxRegistrationResponseTypeDef,
    BatchGetTaxExemptionsRequestTypeDef,
    BatchGetTaxExemptionsResponseTypeDef,
    BatchPutTaxRegistrationRequestTypeDef,
    BatchPutTaxRegistrationResponseTypeDef,
    DeleteSupplementalTaxRegistrationRequestTypeDef,
    DeleteTaxRegistrationRequestTypeDef,
    GetTaxExemptionTypesResponseTypeDef,
    GetTaxInheritanceResponseTypeDef,
    GetTaxRegistrationDocumentRequestTypeDef,
    GetTaxRegistrationDocumentResponseTypeDef,
    GetTaxRegistrationRequestTypeDef,
    GetTaxRegistrationResponseTypeDef,
    ListSupplementalTaxRegistrationsRequestTypeDef,
    ListSupplementalTaxRegistrationsResponseTypeDef,
    ListTaxExemptionsRequestTypeDef,
    ListTaxExemptionsResponseTypeDef,
    ListTaxRegistrationsRequestTypeDef,
    ListTaxRegistrationsResponseTypeDef,
    PutSupplementalTaxRegistrationRequestTypeDef,
    PutSupplementalTaxRegistrationResponseTypeDef,
    PutTaxExemptionRequestTypeDef,
    PutTaxExemptionResponseTypeDef,
    PutTaxInheritanceRequestTypeDef,
    PutTaxRegistrationRequestTypeDef,
    PutTaxRegistrationResponseTypeDef,
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

__all__ = ("TaxSettingsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    AttachmentUploadException: Type[BotocoreClientError]
    CaseCreationLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TaxSettingsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TaxSettingsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#generate_presigned_url)
        """

    def batch_delete_tax_registration(
        self, **kwargs: Unpack[BatchDeleteTaxRegistrationRequestTypeDef]
    ) -> BatchDeleteTaxRegistrationResponseTypeDef:
        """
        Deletes tax registration for multiple accounts in batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/batch_delete_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#batch_delete_tax_registration)
        """

    def batch_get_tax_exemptions(
        self, **kwargs: Unpack[BatchGetTaxExemptionsRequestTypeDef]
    ) -> BatchGetTaxExemptionsResponseTypeDef:
        """
        Get the active tax exemptions for a given list of accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/batch_get_tax_exemptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#batch_get_tax_exemptions)
        """

    def batch_put_tax_registration(
        self, **kwargs: Unpack[BatchPutTaxRegistrationRequestTypeDef]
    ) -> BatchPutTaxRegistrationResponseTypeDef:
        """
        Adds or updates tax registration for multiple accounts in batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/batch_put_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#batch_put_tax_registration)
        """

    def delete_supplemental_tax_registration(
        self, **kwargs: Unpack[DeleteSupplementalTaxRegistrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a supplemental tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/delete_supplemental_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#delete_supplemental_tax_registration)
        """

    def delete_tax_registration(
        self, **kwargs: Unpack[DeleteTaxRegistrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/delete_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#delete_tax_registration)
        """

    def get_tax_exemption_types(self) -> GetTaxExemptionTypesResponseTypeDef:
        """
        Get supported tax exemption types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_tax_exemption_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_tax_exemption_types)
        """

    def get_tax_inheritance(self) -> GetTaxInheritanceResponseTypeDef:
        """
        The get account tax inheritance status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_tax_inheritance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_tax_inheritance)
        """

    def get_tax_registration(
        self, **kwargs: Unpack[GetTaxRegistrationRequestTypeDef]
    ) -> GetTaxRegistrationResponseTypeDef:
        """
        Retrieves tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_tax_registration)
        """

    def get_tax_registration_document(
        self, **kwargs: Unpack[GetTaxRegistrationDocumentRequestTypeDef]
    ) -> GetTaxRegistrationDocumentResponseTypeDef:
        """
        Downloads your tax documents to the Amazon S3 bucket that you specify in your
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_tax_registration_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_tax_registration_document)
        """

    def list_supplemental_tax_registrations(
        self, **kwargs: Unpack[ListSupplementalTaxRegistrationsRequestTypeDef]
    ) -> ListSupplementalTaxRegistrationsResponseTypeDef:
        """
        Retrieves supplemental tax registrations for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/list_supplemental_tax_registrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#list_supplemental_tax_registrations)
        """

    def list_tax_exemptions(
        self, **kwargs: Unpack[ListTaxExemptionsRequestTypeDef]
    ) -> ListTaxExemptionsResponseTypeDef:
        """
        Retrieves the tax exemption of accounts listed in a consolidated billing family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/list_tax_exemptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#list_tax_exemptions)
        """

    def list_tax_registrations(
        self, **kwargs: Unpack[ListTaxRegistrationsRequestTypeDef]
    ) -> ListTaxRegistrationsResponseTypeDef:
        """
        Retrieves the tax registration of accounts listed in a consolidated billing
        family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/list_tax_registrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#list_tax_registrations)
        """

    def put_supplemental_tax_registration(
        self, **kwargs: Unpack[PutSupplementalTaxRegistrationRequestTypeDef]
    ) -> PutSupplementalTaxRegistrationResponseTypeDef:
        """
        Stores supplemental tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/put_supplemental_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#put_supplemental_tax_registration)
        """

    def put_tax_exemption(
        self, **kwargs: Unpack[PutTaxExemptionRequestTypeDef]
    ) -> PutTaxExemptionResponseTypeDef:
        """
        Adds the tax exemption for a single account or all accounts listed in a
        consolidated billing family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/put_tax_exemption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#put_tax_exemption)
        """

    def put_tax_inheritance(
        self, **kwargs: Unpack[PutTaxInheritanceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The updated tax inheritance status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/put_tax_inheritance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#put_tax_inheritance)
        """

    def put_tax_registration(
        self, **kwargs: Unpack[PutTaxRegistrationRequestTypeDef]
    ) -> PutTaxRegistrationResponseTypeDef:
        """
        Adds or updates tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/put_tax_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#put_tax_registration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_supplemental_tax_registrations"]
    ) -> ListSupplementalTaxRegistrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tax_exemptions"]
    ) -> ListTaxExemptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tax_registrations"]
    ) -> ListTaxRegistrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_paginator)
        """
