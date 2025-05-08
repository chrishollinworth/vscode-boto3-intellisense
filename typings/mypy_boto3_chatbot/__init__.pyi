"""
Main interface for chatbot service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chatbot import (
        ChatbotClient,
        Client,
        DescribeChimeWebhookConfigurationsPaginator,
        DescribeSlackChannelConfigurationsPaginator,
        DescribeSlackUserIdentitiesPaginator,
        DescribeSlackWorkspacesPaginator,
        ListAssociationsPaginator,
        ListCustomActionsPaginator,
        ListMicrosoftTeamsChannelConfigurationsPaginator,
        ListMicrosoftTeamsConfiguredTeamsPaginator,
        ListMicrosoftTeamsUserIdentitiesPaginator,
    )

    session = Session()
    client: ChatbotClient = session.client("chatbot")

    describe_chime_webhook_configurations_paginator: DescribeChimeWebhookConfigurationsPaginator = client.get_paginator("describe_chime_webhook_configurations")
    describe_slack_channel_configurations_paginator: DescribeSlackChannelConfigurationsPaginator = client.get_paginator("describe_slack_channel_configurations")
    describe_slack_user_identities_paginator: DescribeSlackUserIdentitiesPaginator = client.get_paginator("describe_slack_user_identities")
    describe_slack_workspaces_paginator: DescribeSlackWorkspacesPaginator = client.get_paginator("describe_slack_workspaces")
    list_associations_paginator: ListAssociationsPaginator = client.get_paginator("list_associations")
    list_custom_actions_paginator: ListCustomActionsPaginator = client.get_paginator("list_custom_actions")
    list_microsoft_teams_channel_configurations_paginator: ListMicrosoftTeamsChannelConfigurationsPaginator = client.get_paginator("list_microsoft_teams_channel_configurations")
    list_microsoft_teams_configured_teams_paginator: ListMicrosoftTeamsConfiguredTeamsPaginator = client.get_paginator("list_microsoft_teams_configured_teams")
    list_microsoft_teams_user_identities_paginator: ListMicrosoftTeamsUserIdentitiesPaginator = client.get_paginator("list_microsoft_teams_user_identities")
    ```
"""

from .client import ChatbotClient
from .paginator import (
    DescribeChimeWebhookConfigurationsPaginator,
    DescribeSlackChannelConfigurationsPaginator,
    DescribeSlackUserIdentitiesPaginator,
    DescribeSlackWorkspacesPaginator,
    ListAssociationsPaginator,
    ListCustomActionsPaginator,
    ListMicrosoftTeamsChannelConfigurationsPaginator,
    ListMicrosoftTeamsConfiguredTeamsPaginator,
    ListMicrosoftTeamsUserIdentitiesPaginator,
)

Client = ChatbotClient

__all__ = (
    "ChatbotClient",
    "Client",
    "DescribeChimeWebhookConfigurationsPaginator",
    "DescribeSlackChannelConfigurationsPaginator",
    "DescribeSlackUserIdentitiesPaginator",
    "DescribeSlackWorkspacesPaginator",
    "ListAssociationsPaginator",
    "ListCustomActionsPaginator",
    "ListMicrosoftTeamsChannelConfigurationsPaginator",
    "ListMicrosoftTeamsConfiguredTeamsPaginator",
    "ListMicrosoftTeamsUserIdentitiesPaginator",
)
