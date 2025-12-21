"""
Type annotations for partnercentral-benefits service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_benefits.client import PartnerCentralBenefitsClient

    session = Session()
    client: PartnerCentralBenefitsClient = session.client("partnercentral-benefits")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBenefitAllocationsPaginator,
    ListBenefitApplicationsPaginator,
    ListBenefitsPaginator,
)
from .type_defs import (
    AmendBenefitApplicationInputTypeDef,
    AssociateBenefitApplicationResourceInputTypeDef,
    AssociateBenefitApplicationResourceOutputTypeDef,
    CancelBenefitApplicationInputTypeDef,
    CreateBenefitApplicationInputTypeDef,
    CreateBenefitApplicationOutputTypeDef,
    DisassociateBenefitApplicationResourceInputTypeDef,
    DisassociateBenefitApplicationResourceOutputTypeDef,
    GetBenefitAllocationInputTypeDef,
    GetBenefitAllocationOutputTypeDef,
    GetBenefitApplicationInputTypeDef,
    GetBenefitApplicationOutputTypeDef,
    GetBenefitInputTypeDef,
    GetBenefitOutputTypeDef,
    ListBenefitAllocationsInputTypeDef,
    ListBenefitAllocationsOutputTypeDef,
    ListBenefitApplicationsInputTypeDef,
    ListBenefitApplicationsOutputTypeDef,
    ListBenefitsInputTypeDef,
    ListBenefitsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RecallBenefitApplicationInputTypeDef,
    SubmitBenefitApplicationInputTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBenefitApplicationInputTypeDef,
    UpdateBenefitApplicationOutputTypeDef,
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

__all__ = ("PartnerCentralBenefitsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PartnerCentralBenefitsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits.html#PartnerCentralBenefits.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PartnerCentralBenefitsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits.html#PartnerCentralBenefits.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#generate_presigned_url)
        """

    def amend_benefit_application(
        self, **kwargs: Unpack[AmendBenefitApplicationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies an existing benefit application by applying amendments to specific
        fields while maintaining revision control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/amend_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#amend_benefit_application)
        """

    def associate_benefit_application_resource(
        self, **kwargs: Unpack[AssociateBenefitApplicationResourceInputTypeDef]
    ) -> AssociateBenefitApplicationResourceOutputTypeDef:
        """
        Links an AWS resource to an existing benefit application for tracking and
        management purposes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/associate_benefit_application_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#associate_benefit_application_resource)
        """

    def cancel_benefit_application(
        self, **kwargs: Unpack[CancelBenefitApplicationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels a benefit application that is currently in progress, preventing further
        processing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/cancel_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#cancel_benefit_application)
        """

    def create_benefit_application(
        self, **kwargs: Unpack[CreateBenefitApplicationInputTypeDef]
    ) -> CreateBenefitApplicationOutputTypeDef:
        """
        Creates a new benefit application for a partner to request access to AWS
        benefits and programs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/create_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#create_benefit_application)
        """

    def disassociate_benefit_application_resource(
        self, **kwargs: Unpack[DisassociateBenefitApplicationResourceInputTypeDef]
    ) -> DisassociateBenefitApplicationResourceOutputTypeDef:
        """
        Removes the association between an AWS resource and a benefit application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/disassociate_benefit_application_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#disassociate_benefit_application_resource)
        """

    def get_benefit(self, **kwargs: Unpack[GetBenefitInputTypeDef]) -> GetBenefitOutputTypeDef:
        """
        Retrieves detailed information about a specific benefit available in the
        partner catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/get_benefit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#get_benefit)
        """

    def get_benefit_allocation(
        self, **kwargs: Unpack[GetBenefitAllocationInputTypeDef]
    ) -> GetBenefitAllocationOutputTypeDef:
        """
        Retrieves detailed information about a specific benefit allocation that has
        been granted to a partner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/get_benefit_allocation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#get_benefit_allocation)
        """

    def get_benefit_application(
        self, **kwargs: Unpack[GetBenefitApplicationInputTypeDef]
    ) -> GetBenefitApplicationOutputTypeDef:
        """
        Retrieves detailed information about a specific benefit application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/get_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#get_benefit_application)
        """

    def list_benefit_allocations(
        self, **kwargs: Unpack[ListBenefitAllocationsInputTypeDef]
    ) -> ListBenefitAllocationsOutputTypeDef:
        """
        Retrieves a paginated list of benefit allocations based on specified filter
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/list_benefit_allocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#list_benefit_allocations)
        """

    def list_benefit_applications(
        self, **kwargs: Unpack[ListBenefitApplicationsInputTypeDef]
    ) -> ListBenefitApplicationsOutputTypeDef:
        """
        Retrieves a paginated list of benefit applications based on specified filter
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/list_benefit_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#list_benefit_applications)
        """

    def list_benefits(
        self, **kwargs: Unpack[ListBenefitsInputTypeDef]
    ) -> ListBenefitsOutputTypeDef:
        """
        Retrieves a paginated list of available benefits based on specified filter
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/list_benefits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#list_benefits)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves all tags associated with a specific resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#list_tags_for_resource)
        """

    def recall_benefit_application(
        self, **kwargs: Unpack[RecallBenefitApplicationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Recalls a submitted benefit application, returning it to draft status for
        further modifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/recall_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#recall_benefit_application)
        """

    def submit_benefit_application(
        self, **kwargs: Unpack[SubmitBenefitApplicationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Submits a benefit application for review and processing by AWS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/submit_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#submit_benefit_application)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#untag_resource)
        """

    def update_benefit_application(
        self, **kwargs: Unpack[UpdateBenefitApplicationInputTypeDef]
    ) -> UpdateBenefitApplicationOutputTypeDef:
        """
        Updates an existing benefit application with new information while maintaining
        revision control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/update_benefit_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#update_benefit_application)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_benefit_allocations"]
    ) -> ListBenefitAllocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_benefit_applications"]
    ) -> ListBenefitApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_benefits"]
    ) -> ListBenefitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/client/#get_paginator)
        """
