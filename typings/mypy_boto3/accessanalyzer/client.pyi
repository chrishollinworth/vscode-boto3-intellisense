"""
Type annotations for accessanalyzer service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_accessanalyzer.client import AccessAnalyzerClient

    session = Session()
    client: AccessAnalyzerClient = session.client("accessanalyzer")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetFindingRecommendationPaginator,
    GetFindingV2Paginator,
    ListAccessPreviewFindingsPaginator,
    ListAccessPreviewsPaginator,
    ListAnalyzedResourcesPaginator,
    ListAnalyzersPaginator,
    ListArchiveRulesPaginator,
    ListFindingsPaginator,
    ListFindingsV2Paginator,
    ListPolicyGenerationsPaginator,
    ValidatePolicyPaginator,
)
from .type_defs import (
    ApplyArchiveRuleRequestTypeDef,
    CancelPolicyGenerationRequestTypeDef,
    CheckAccessNotGrantedRequestTypeDef,
    CheckAccessNotGrantedResponseTypeDef,
    CheckNoNewAccessRequestTypeDef,
    CheckNoNewAccessResponseTypeDef,
    CheckNoPublicAccessRequestTypeDef,
    CheckNoPublicAccessResponseTypeDef,
    CreateAccessPreviewRequestTypeDef,
    CreateAccessPreviewResponseTypeDef,
    CreateAnalyzerRequestTypeDef,
    CreateAnalyzerResponseTypeDef,
    CreateArchiveRuleRequestTypeDef,
    DeleteAnalyzerRequestTypeDef,
    DeleteArchiveRuleRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GenerateFindingRecommendationRequestTypeDef,
    GetAccessPreviewRequestTypeDef,
    GetAccessPreviewResponseTypeDef,
    GetAnalyzedResourceRequestTypeDef,
    GetAnalyzedResourceResponseTypeDef,
    GetAnalyzerRequestTypeDef,
    GetAnalyzerResponseTypeDef,
    GetArchiveRuleRequestTypeDef,
    GetArchiveRuleResponseTypeDef,
    GetFindingRecommendationRequestTypeDef,
    GetFindingRecommendationResponseTypeDef,
    GetFindingRequestTypeDef,
    GetFindingResponseTypeDef,
    GetFindingsStatisticsRequestTypeDef,
    GetFindingsStatisticsResponseTypeDef,
    GetFindingV2RequestTypeDef,
    GetFindingV2ResponseTypeDef,
    GetGeneratedPolicyRequestTypeDef,
    GetGeneratedPolicyResponseTypeDef,
    ListAccessPreviewFindingsRequestTypeDef,
    ListAccessPreviewFindingsResponseTypeDef,
    ListAccessPreviewsRequestTypeDef,
    ListAccessPreviewsResponseTypeDef,
    ListAnalyzedResourcesRequestTypeDef,
    ListAnalyzedResourcesResponseTypeDef,
    ListAnalyzersRequestTypeDef,
    ListAnalyzersResponseTypeDef,
    ListArchiveRulesRequestTypeDef,
    ListArchiveRulesResponseTypeDef,
    ListFindingsRequestTypeDef,
    ListFindingsResponseTypeDef,
    ListFindingsV2RequestTypeDef,
    ListFindingsV2ResponseTypeDef,
    ListPolicyGenerationsRequestTypeDef,
    ListPolicyGenerationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartPolicyGenerationRequestTypeDef,
    StartPolicyGenerationResponseTypeDef,
    StartResourceScanRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAnalyzerRequestTypeDef,
    UpdateAnalyzerResponseTypeDef,
    UpdateArchiveRuleRequestTypeDef,
    UpdateFindingsRequestTypeDef,
    ValidatePolicyRequestTypeDef,
    ValidatePolicyResponseTypeDef,
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

__all__ = ("AccessAnalyzerClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AccessAnalyzerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AccessAnalyzerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#generate_presigned_url)
        """

    def apply_archive_rule(
        self, **kwargs: Unpack[ApplyArchiveRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Retroactively applies the archive rule to existing findings that meet the
        archive rule criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/apply_archive_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#apply_archive_rule)
        """

    def cancel_policy_generation(
        self, **kwargs: Unpack[CancelPolicyGenerationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the requested policy generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/cancel_policy_generation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#cancel_policy_generation)
        """

    def check_access_not_granted(
        self, **kwargs: Unpack[CheckAccessNotGrantedRequestTypeDef]
    ) -> CheckAccessNotGrantedResponseTypeDef:
        """
        Checks whether the specified access isn't allowed by a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/check_access_not_granted.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#check_access_not_granted)
        """

    def check_no_new_access(
        self, **kwargs: Unpack[CheckNoNewAccessRequestTypeDef]
    ) -> CheckNoNewAccessResponseTypeDef:
        """
        Checks whether new access is allowed for an updated policy when compared to the
        existing policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/check_no_new_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#check_no_new_access)
        """

    def check_no_public_access(
        self, **kwargs: Unpack[CheckNoPublicAccessRequestTypeDef]
    ) -> CheckNoPublicAccessResponseTypeDef:
        """
        Checks whether a resource policy can grant public access to the specified
        resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/check_no_public_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#check_no_public_access)
        """

    def create_access_preview(
        self, **kwargs: Unpack[CreateAccessPreviewRequestTypeDef]
    ) -> CreateAccessPreviewResponseTypeDef:
        """
        Creates an access preview that allows you to preview IAM Access Analyzer
        findings for your resource before deploying resource permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/create_access_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#create_access_preview)
        """

    def create_analyzer(
        self, **kwargs: Unpack[CreateAnalyzerRequestTypeDef]
    ) -> CreateAnalyzerResponseTypeDef:
        """
        Creates an analyzer for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/create_analyzer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#create_analyzer)
        """

    def create_archive_rule(
        self, **kwargs: Unpack[CreateArchiveRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates an archive rule for the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/create_archive_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#create_archive_rule)
        """

    def delete_analyzer(
        self, **kwargs: Unpack[DeleteAnalyzerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/delete_analyzer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#delete_analyzer)
        """

    def delete_archive_rule(
        self, **kwargs: Unpack[DeleteArchiveRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified archive rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/delete_archive_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#delete_archive_rule)
        """

    def generate_finding_recommendation(
        self, **kwargs: Unpack[GenerateFindingRecommendationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a recommendation for an unused permissions finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/generate_finding_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#generate_finding_recommendation)
        """

    def get_access_preview(
        self, **kwargs: Unpack[GetAccessPreviewRequestTypeDef]
    ) -> GetAccessPreviewResponseTypeDef:
        """
        Retrieves information about an access preview for the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_access_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_access_preview)
        """

    def get_analyzed_resource(
        self, **kwargs: Unpack[GetAnalyzedResourceRequestTypeDef]
    ) -> GetAnalyzedResourceResponseTypeDef:
        """
        Retrieves information about a resource that was analyzed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_analyzed_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_analyzed_resource)
        """

    def get_analyzer(
        self, **kwargs: Unpack[GetAnalyzerRequestTypeDef]
    ) -> GetAnalyzerResponseTypeDef:
        """
        Retrieves information about the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_analyzer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_analyzer)
        """

    def get_archive_rule(
        self, **kwargs: Unpack[GetArchiveRuleRequestTypeDef]
    ) -> GetArchiveRuleResponseTypeDef:
        """
        Retrieves information about an archive rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_archive_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_archive_rule)
        """

    def get_finding(self, **kwargs: Unpack[GetFindingRequestTypeDef]) -> GetFindingResponseTypeDef:
        """
        Retrieves information about the specified finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_finding.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_finding)
        """

    def get_finding_recommendation(
        self, **kwargs: Unpack[GetFindingRecommendationRequestTypeDef]
    ) -> GetFindingRecommendationResponseTypeDef:
        """
        Retrieves information about a finding recommendation for the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_finding_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_finding_recommendation)
        """

    def get_finding_v2(
        self, **kwargs: Unpack[GetFindingV2RequestTypeDef]
    ) -> GetFindingV2ResponseTypeDef:
        """
        Retrieves information about the specified finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_finding_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_finding_v2)
        """

    def get_findings_statistics(
        self, **kwargs: Unpack[GetFindingsStatisticsRequestTypeDef]
    ) -> GetFindingsStatisticsResponseTypeDef:
        """
        Retrieves a list of aggregated finding statistics for an external access or
        unused access analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_findings_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_findings_statistics)
        """

    def get_generated_policy(
        self, **kwargs: Unpack[GetGeneratedPolicyRequestTypeDef]
    ) -> GetGeneratedPolicyResponseTypeDef:
        """
        Retrieves the policy that was generated using
        <code>StartPolicyGeneration</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_generated_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_generated_policy)
        """

    def list_access_preview_findings(
        self, **kwargs: Unpack[ListAccessPreviewFindingsRequestTypeDef]
    ) -> ListAccessPreviewFindingsResponseTypeDef:
        """
        Retrieves a list of access preview findings generated by the specified access
        preview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_access_preview_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_access_preview_findings)
        """

    def list_access_previews(
        self, **kwargs: Unpack[ListAccessPreviewsRequestTypeDef]
    ) -> ListAccessPreviewsResponseTypeDef:
        """
        Retrieves a list of access previews for the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_access_previews.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_access_previews)
        """

    def list_analyzed_resources(
        self, **kwargs: Unpack[ListAnalyzedResourcesRequestTypeDef]
    ) -> ListAnalyzedResourcesResponseTypeDef:
        """
        Retrieves a list of resources of the specified type that have been analyzed by
        the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_analyzed_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_analyzed_resources)
        """

    def list_analyzers(
        self, **kwargs: Unpack[ListAnalyzersRequestTypeDef]
    ) -> ListAnalyzersResponseTypeDef:
        """
        Retrieves a list of analyzers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_analyzers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_analyzers)
        """

    def list_archive_rules(
        self, **kwargs: Unpack[ListArchiveRulesRequestTypeDef]
    ) -> ListArchiveRulesResponseTypeDef:
        """
        Retrieves a list of archive rules created for the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_archive_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_archive_rules)
        """

    def list_findings(
        self, **kwargs: Unpack[ListFindingsRequestTypeDef]
    ) -> ListFindingsResponseTypeDef:
        """
        Retrieves a list of findings generated by the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_findings)
        """

    def list_findings_v2(
        self, **kwargs: Unpack[ListFindingsV2RequestTypeDef]
    ) -> ListFindingsV2ResponseTypeDef:
        """
        Retrieves a list of findings generated by the specified analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_findings_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_findings_v2)
        """

    def list_policy_generations(
        self, **kwargs: Unpack[ListPolicyGenerationsRequestTypeDef]
    ) -> ListPolicyGenerationsResponseTypeDef:
        """
        Lists all of the policy generations requested in the last seven days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_policy_generations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_policy_generations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of tags applied to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#list_tags_for_resource)
        """

    def start_policy_generation(
        self, **kwargs: Unpack[StartPolicyGenerationRequestTypeDef]
    ) -> StartPolicyGenerationResponseTypeDef:
        """
        Starts the policy generation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/start_policy_generation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#start_policy_generation)
        """

    def start_resource_scan(
        self, **kwargs: Unpack[StartResourceScanRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Immediately starts a scan of the policies applied to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/start_resource_scan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#start_resource_scan)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#untag_resource)
        """

    def update_analyzer(
        self, **kwargs: Unpack[UpdateAnalyzerRequestTypeDef]
    ) -> UpdateAnalyzerResponseTypeDef:
        """
        Modifies the configuration of an existing analyzer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/update_analyzer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#update_analyzer)
        """

    def update_archive_rule(
        self, **kwargs: Unpack[UpdateArchiveRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the criteria and values for the specified archive rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/update_archive_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#update_archive_rule)
        """

    def update_findings(
        self, **kwargs: Unpack[UpdateFindingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the status for the specified findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/update_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#update_findings)
        """

    def validate_policy(
        self, **kwargs: Unpack[ValidatePolicyRequestTypeDef]
    ) -> ValidatePolicyResponseTypeDef:
        """
        Requests the validation of a policy and returns a list of findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/validate_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#validate_policy)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_finding_recommendation"]
    ) -> GetFindingRecommendationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_finding_v2"]
    ) -> GetFindingV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_preview_findings"]
    ) -> ListAccessPreviewFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_previews"]
    ) -> ListAccessPreviewsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_analyzed_resources"]
    ) -> ListAnalyzedResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_analyzers"]
    ) -> ListAnalyzersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_archive_rules"]
    ) -> ListArchiveRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_findings"]
    ) -> ListFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_findings_v2"]
    ) -> ListFindingsV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_generations"]
    ) -> ListPolicyGenerationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["validate_policy"]
    ) -> ValidatePolicyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client/#get_paginator)
        """
