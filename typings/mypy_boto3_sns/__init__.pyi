"""
Main interface for sns service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sns import (
        Client,
        ListEndpointsByPlatformApplicationPaginator,
        ListPhoneNumbersOptedOutPaginator,
        ListPlatformApplicationsPaginator,
        ListSubscriptionsByTopicPaginator,
        ListSubscriptionsPaginator,
        ListTopicsPaginator,
        SNSClient,
        SNSServiceResource,
        ServiceResource,
    )

    session = boto3.Session()

    client: SNSClient = boto3.client("sns")
    session_client: SNSClient = session.client("sns")

    resource: SNSServiceResource = boto3.resource("sns")
    session_resource: SNSServiceResource = session.resource("sns")

    list_endpoints_by_platform_application_paginator: ListEndpointsByPlatformApplicationPaginator = client.get_paginator("list_endpoints_by_platform_application")
    list_phone_numbers_opted_out_paginator: ListPhoneNumbersOptedOutPaginator = client.get_paginator("list_phone_numbers_opted_out")
    list_platform_applications_paginator: ListPlatformApplicationsPaginator = client.get_paginator("list_platform_applications")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_subscriptions_by_topic_paginator: ListSubscriptionsByTopicPaginator = client.get_paginator("list_subscriptions_by_topic")
    list_topics_paginator: ListTopicsPaginator = client.get_paginator("list_topics")
    ```
"""
from mypy_boto3_sns.client import SNSClient
from mypy_boto3_sns.paginator import (
    ListEndpointsByPlatformApplicationPaginator,
    ListPhoneNumbersOptedOutPaginator,
    ListPlatformApplicationsPaginator,
    ListSubscriptionsByTopicPaginator,
    ListSubscriptionsPaginator,
    ListTopicsPaginator,
)
from mypy_boto3_sns.service_resource import SNSServiceResource

Client = SNSClient


ServiceResource = SNSServiceResource


__all__ = (
    "Client",
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListSubscriptionsPaginator",
    "ListTopicsPaginator",
    "SNSClient",
    "SNSServiceResource",
    "ServiceResource",
)
