"""
Main interface for alexaforbusiness service.

Usage::

    ```python
    import boto3
    from mypy_boto3_alexaforbusiness import (
        AlexaForBusinessClient,
        Client,
        ListBusinessReportSchedulesPaginator,
        ListConferenceProvidersPaginator,
        ListDeviceEventsPaginator,
        ListSkillsPaginator,
        ListSkillsStoreCategoriesPaginator,
        ListSkillsStoreSkillsByCategoryPaginator,
        ListSmartHomeAppliancesPaginator,
        ListTagsPaginator,
        SearchDevicesPaginator,
        SearchProfilesPaginator,
        SearchRoomsPaginator,
        SearchSkillGroupsPaginator,
        SearchUsersPaginator,
    )

    session = boto3.Session()

    client: AlexaForBusinessClient = boto3.client("alexaforbusiness")
    session_client: AlexaForBusinessClient = session.client("alexaforbusiness")

    list_business_report_schedules_paginator: ListBusinessReportSchedulesPaginator = client.get_paginator("list_business_report_schedules")
    list_conference_providers_paginator: ListConferenceProvidersPaginator = client.get_paginator("list_conference_providers")
    list_device_events_paginator: ListDeviceEventsPaginator = client.get_paginator("list_device_events")
    list_skills_paginator: ListSkillsPaginator = client.get_paginator("list_skills")
    list_skills_store_categories_paginator: ListSkillsStoreCategoriesPaginator = client.get_paginator("list_skills_store_categories")
    list_skills_store_skills_by_category_paginator: ListSkillsStoreSkillsByCategoryPaginator = client.get_paginator("list_skills_store_skills_by_category")
    list_smart_home_appliances_paginator: ListSmartHomeAppliancesPaginator = client.get_paginator("list_smart_home_appliances")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_profiles_paginator: SearchProfilesPaginator = client.get_paginator("search_profiles")
    search_rooms_paginator: SearchRoomsPaginator = client.get_paginator("search_rooms")
    search_skill_groups_paginator: SearchSkillGroupsPaginator = client.get_paginator("search_skill_groups")
    search_users_paginator: SearchUsersPaginator = client.get_paginator("search_users")
    ```
"""
from mypy_boto3_alexaforbusiness.client import AlexaForBusinessClient
from mypy_boto3_alexaforbusiness.paginator import (
    ListBusinessReportSchedulesPaginator,
    ListConferenceProvidersPaginator,
    ListDeviceEventsPaginator,
    ListSkillsPaginator,
    ListSkillsStoreCategoriesPaginator,
    ListSkillsStoreSkillsByCategoryPaginator,
    ListSmartHomeAppliancesPaginator,
    ListTagsPaginator,
    SearchDevicesPaginator,
    SearchProfilesPaginator,
    SearchRoomsPaginator,
    SearchSkillGroupsPaginator,
    SearchUsersPaginator,
)

Client = AlexaForBusinessClient


__all__ = (
    "AlexaForBusinessClient",
    "Client",
    "ListBusinessReportSchedulesPaginator",
    "ListConferenceProvidersPaginator",
    "ListDeviceEventsPaginator",
    "ListSkillsPaginator",
    "ListSkillsStoreCategoriesPaginator",
    "ListSkillsStoreSkillsByCategoryPaginator",
    "ListSmartHomeAppliancesPaginator",
    "ListTagsPaginator",
    "SearchDevicesPaginator",
    "SearchProfilesPaginator",
    "SearchRoomsPaginator",
    "SearchSkillGroupsPaginator",
    "SearchUsersPaginator",
)
