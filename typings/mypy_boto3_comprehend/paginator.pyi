"""
Type annotations for comprehend service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_comprehend import ComprehendClient
    from mypy_boto3_comprehend.paginator import (
        ListDocumentClassificationJobsPaginator,
        ListDocumentClassifiersPaginator,
        ListDominantLanguageDetectionJobsPaginator,
        ListEntitiesDetectionJobsPaginator,
        ListEntityRecognizersPaginator,
        ListKeyPhrasesDetectionJobsPaginator,
        ListSentimentDetectionJobsPaginator,
        ListTopicsDetectionJobsPaginator,
    )

    client: ComprehendClient = boto3.client("comprehend")

    list_document_classification_jobs_paginator: ListDocumentClassificationJobsPaginator = client.get_paginator("list_document_classification_jobs")
    list_document_classifiers_paginator: ListDocumentClassifiersPaginator = client.get_paginator("list_document_classifiers")
    list_dominant_language_detection_jobs_paginator: ListDominantLanguageDetectionJobsPaginator = client.get_paginator("list_dominant_language_detection_jobs")
    list_entities_detection_jobs_paginator: ListEntitiesDetectionJobsPaginator = client.get_paginator("list_entities_detection_jobs")
    list_entity_recognizers_paginator: ListEntityRecognizersPaginator = client.get_paginator("list_entity_recognizers")
    list_key_phrases_detection_jobs_paginator: ListKeyPhrasesDetectionJobsPaginator = client.get_paginator("list_key_phrases_detection_jobs")
    list_sentiment_detection_jobs_paginator: ListSentimentDetectionJobsPaginator = client.get_paginator("list_sentiment_detection_jobs")
    list_topics_detection_jobs_paginator: ListTopicsDetectionJobsPaginator = client.get_paginator("list_topics_detection_jobs")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DocumentClassificationJobFilterTypeDef,
    DocumentClassifierFilterTypeDef,
    DominantLanguageDetectionJobFilterTypeDef,
    EntitiesDetectionJobFilterTypeDef,
    EntityRecognizerFilterTypeDef,
    KeyPhrasesDetectionJobFilterTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    PaginatorConfigTypeDef,
    SentimentDetectionJobFilterTypeDef,
    TopicsDetectionJobFilterTypeDef,
)

__all__ = (
    "ListDocumentClassificationJobsPaginator",
    "ListDocumentClassifiersPaginator",
    "ListDominantLanguageDetectionJobsPaginator",
    "ListEntitiesDetectionJobsPaginator",
    "ListEntityRecognizersPaginator",
    "ListKeyPhrasesDetectionJobsPaginator",
    "ListSentimentDetectionJobsPaginator",
    "ListTopicsDetectionJobsPaginator",
)

class ListDocumentClassificationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassificationjobspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "DocumentClassificationJobFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentClassificationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassificationjobspaginator)
        """

class ListDocumentClassifiersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassifierspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "DocumentClassifierFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentClassifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassifierspaginator)
        """

class ListDominantLanguageDetectionJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdominantlanguagedetectionjobspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "DominantLanguageDetectionJobFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDominantLanguageDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdominantlanguagedetectionjobspaginator)
        """

class ListEntitiesDetectionJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentitiesdetectionjobspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "EntitiesDetectionJobFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntitiesDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentitiesdetectionjobspaginator)
        """

class ListEntityRecognizersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentityrecognizerspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "EntityRecognizerFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntityRecognizersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentityrecognizerspaginator)
        """

class ListKeyPhrasesDetectionJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listkeyphrasesdetectionjobspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "KeyPhrasesDetectionJobFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeyPhrasesDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listkeyphrasesdetectionjobspaginator)
        """

class ListSentimentDetectionJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listsentimentdetectionjobspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "SentimentDetectionJobFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSentimentDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listsentimentdetectionjobspaginator)
        """

class ListTopicsDetectionJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listtopicsdetectionjobspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "TopicsDetectionJobFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicsDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listtopicsdetectionjobspaginator)
        """
