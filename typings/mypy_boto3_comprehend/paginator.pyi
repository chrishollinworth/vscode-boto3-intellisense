# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for comprehend service client paginators.

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

from mypy_boto3_comprehend.type_defs import (
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
    [Paginator.ListDocumentClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
    """

    def paginate(
        self,
        Filter: DocumentClassificationJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDocumentClassificationJobsResponseTypeDef]:
        """
        [ListDocumentClassificationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs.paginate)
        """


class ListDocumentClassifiersPaginator(Boto3Paginator):
    """
    [Paginator.ListDocumentClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
    """

    def paginate(
        self,
        Filter: DocumentClassifierFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDocumentClassifiersResponseTypeDef]:
        """
        [ListDocumentClassifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers.paginate)
        """


class ListDominantLanguageDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDominantLanguageDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
    """

    def paginate(
        self,
        Filter: DominantLanguageDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDominantLanguageDetectionJobsResponseTypeDef]:
        """
        [ListDominantLanguageDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs.paginate)
        """


class ListEntitiesDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitiesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
    """

    def paginate(
        self,
        Filter: EntitiesDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEntitiesDetectionJobsResponseTypeDef]:
        """
        [ListEntitiesDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs.paginate)
        """


class ListEntityRecognizersPaginator(Boto3Paginator):
    """
    [Paginator.ListEntityRecognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
    """

    def paginate(
        self,
        Filter: EntityRecognizerFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEntityRecognizersResponseTypeDef]:
        """
        [ListEntityRecognizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers.paginate)
        """


class ListKeyPhrasesDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListKeyPhrasesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
    """

    def paginate(
        self,
        Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListKeyPhrasesDetectionJobsResponseTypeDef]:
        """
        [ListKeyPhrasesDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs.paginate)
        """


class ListSentimentDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListSentimentDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
    """

    def paginate(
        self,
        Filter: SentimentDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSentimentDetectionJobsResponseTypeDef]:
        """
        [ListSentimentDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs.paginate)
        """


class ListTopicsDetectionJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTopicsDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
    """

    def paginate(
        self,
        Filter: TopicsDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTopicsDetectionJobsResponseTypeDef]:
        """
        [ListTopicsDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs.paginate)
        """
