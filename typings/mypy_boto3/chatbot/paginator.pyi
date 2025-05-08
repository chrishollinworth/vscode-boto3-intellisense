"""
Type annotations for chatbot service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_chatbot.client import ChatbotClient
    from mypy_boto3_chatbot.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeChimeWebhookConfigurationsRequestPaginateTypeDef,
    DescribeChimeWebhookConfigurationsResultTypeDef,
    DescribeSlackChannelConfigurationsRequestPaginateTypeDef,
    DescribeSlackChannelConfigurationsResultTypeDef,
    DescribeSlackUserIdentitiesRequestPaginateTypeDef,
    DescribeSlackUserIdentitiesResultTypeDef,
    DescribeSlackWorkspacesRequestPaginateTypeDef,
    DescribeSlackWorkspacesResultTypeDef,
    ListAssociationsRequestPaginateTypeDef,
    ListAssociationsResultTypeDef,
    ListCustomActionsRequestPaginateTypeDef,
    ListCustomActionsResultTypeDef,
    ListMicrosoftTeamsConfiguredTeamsRequestPaginateTypeDef,
    ListMicrosoftTeamsConfiguredTeamsResultTypeDef,
    ListMicrosoftTeamsUserIdentitiesRequestPaginateTypeDef,
    ListMicrosoftTeamsUserIdentitiesResultTypeDef,
    ListTeamsChannelConfigurationsRequestPaginateTypeDef,
    ListTeamsChannelConfigurationsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _DescribeChimeWebhookConfigurationsPaginatorBase = Paginator[
        DescribeChimeWebhookConfigurationsResultTypeDef
    ]
else:
    _DescribeChimeWebhookConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeChimeWebhookConfigurationsPaginator(_DescribeChimeWebhookConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeChimeWebhookConfigurations.html#Chatbot.Paginator.DescribeChimeWebhookConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describechimewebhookconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChimeWebhookConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeChimeWebhookConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeChimeWebhookConfigurations.html#Chatbot.Paginator.DescribeChimeWebhookConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describechimewebhookconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeSlackChannelConfigurationsPaginatorBase = Paginator[
        DescribeSlackChannelConfigurationsResultTypeDef
    ]
else:
    _DescribeSlackChannelConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSlackChannelConfigurationsPaginator(_DescribeSlackChannelConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeSlackChannelConfigurations.html#Chatbot.Paginator.DescribeSlackChannelConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describeslackchannelconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSlackChannelConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSlackChannelConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeSlackChannelConfigurations.html#Chatbot.Paginator.DescribeSlackChannelConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describeslackchannelconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeSlackUserIdentitiesPaginatorBase = Paginator[DescribeSlackUserIdentitiesResultTypeDef]
else:
    _DescribeSlackUserIdentitiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSlackUserIdentitiesPaginator(_DescribeSlackUserIdentitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeSlackUserIdentities.html#Chatbot.Paginator.DescribeSlackUserIdentities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describeslackuseridentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSlackUserIdentitiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSlackUserIdentitiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeSlackUserIdentities.html#Chatbot.Paginator.DescribeSlackUserIdentities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describeslackuseridentitiespaginator)
        """

if TYPE_CHECKING:
    _DescribeSlackWorkspacesPaginatorBase = Paginator[DescribeSlackWorkspacesResultTypeDef]
else:
    _DescribeSlackWorkspacesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSlackWorkspacesPaginator(_DescribeSlackWorkspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeSlackWorkspaces.html#Chatbot.Paginator.DescribeSlackWorkspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describeslackworkspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSlackWorkspacesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSlackWorkspacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/DescribeSlackWorkspaces.html#Chatbot.Paginator.DescribeSlackWorkspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#describeslackworkspacespaginator)
        """

if TYPE_CHECKING:
    _ListAssociationsPaginatorBase = Paginator[ListAssociationsResultTypeDef]
else:
    _ListAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociationsPaginator(_ListAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListAssociations.html#Chatbot.Paginator.ListAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListAssociations.html#Chatbot.Paginator.ListAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listassociationspaginator)
        """

if TYPE_CHECKING:
    _ListCustomActionsPaginatorBase = Paginator[ListCustomActionsResultTypeDef]
else:
    _ListCustomActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomActionsPaginator(_ListCustomActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListCustomActions.html#Chatbot.Paginator.ListCustomActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listcustomactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomActionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListCustomActions.html#Chatbot.Paginator.ListCustomActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listcustomactionspaginator)
        """

if TYPE_CHECKING:
    _ListMicrosoftTeamsChannelConfigurationsPaginatorBase = Paginator[
        ListTeamsChannelConfigurationsResultTypeDef
    ]
else:
    _ListMicrosoftTeamsChannelConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMicrosoftTeamsChannelConfigurationsPaginator(
    _ListMicrosoftTeamsChannelConfigurationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListMicrosoftTeamsChannelConfigurations.html#Chatbot.Paginator.ListMicrosoftTeamsChannelConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listmicrosoftteamschannelconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTeamsChannelConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListTeamsChannelConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListMicrosoftTeamsChannelConfigurations.html#Chatbot.Paginator.ListMicrosoftTeamsChannelConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listmicrosoftteamschannelconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListMicrosoftTeamsConfiguredTeamsPaginatorBase = Paginator[
        ListMicrosoftTeamsConfiguredTeamsResultTypeDef
    ]
else:
    _ListMicrosoftTeamsConfiguredTeamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMicrosoftTeamsConfiguredTeamsPaginator(_ListMicrosoftTeamsConfiguredTeamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListMicrosoftTeamsConfiguredTeams.html#Chatbot.Paginator.ListMicrosoftTeamsConfiguredTeams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listmicrosoftteamsconfiguredteamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMicrosoftTeamsConfiguredTeamsRequestPaginateTypeDef]
    ) -> PageIterator[ListMicrosoftTeamsConfiguredTeamsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListMicrosoftTeamsConfiguredTeams.html#Chatbot.Paginator.ListMicrosoftTeamsConfiguredTeams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listmicrosoftteamsconfiguredteamspaginator)
        """

if TYPE_CHECKING:
    _ListMicrosoftTeamsUserIdentitiesPaginatorBase = Paginator[
        ListMicrosoftTeamsUserIdentitiesResultTypeDef
    ]
else:
    _ListMicrosoftTeamsUserIdentitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMicrosoftTeamsUserIdentitiesPaginator(_ListMicrosoftTeamsUserIdentitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListMicrosoftTeamsUserIdentities.html#Chatbot.Paginator.ListMicrosoftTeamsUserIdentities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listmicrosoftteamsuseridentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMicrosoftTeamsUserIdentitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListMicrosoftTeamsUserIdentitiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/paginator/ListMicrosoftTeamsUserIdentities.html#Chatbot.Paginator.ListMicrosoftTeamsUserIdentities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/paginators/#listmicrosoftteamsuseridentitiespaginator)
        """
