"""
Test Keyword Model
"""


from integration_tests.base_test import BaseTestCase

from integration_tests.config import DEFAULT_AD_ACCOUNT_ID

from pinterest.ads.keywords import Keyword
from pinterest.utils.sdk_exceptions import SdkException

from openapi_generated.pinterest_client.model.match_type_response import MatchTypeResponse


class TestCreateKeyword(BaseTestCase):
    """
    Test Keyword create
    """
    def test_create_keyword_success(self):
        """
        Test creating a new keyword
        """
        keyword = Keyword.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            parent_id=self.ad_group_utils.get_ad_group_id(),
            value="string",
            match_type="BROAD",
            bid=1000,
        )

        assert keyword
        assert getattr(keyword, '_id')
        assert getattr(keyword, '_parent_id') == self.ad_group_utils.get_ad_group_id()
        assert getattr(keyword, '_match_type') == MatchTypeResponse("BROAD")

    def test_create_fail_without_matchtype(self):
        """
        Test creating a new keyword
        """
        keyword_arguments = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            parent_id=self.ad_group_utils.get_ad_group_id(),
            value="string",
        )

        with self.assertRaises(SdkException):
            Keyword.create(**keyword_arguments)


class TestGetKeywords(BaseTestCase):
    """
    Test get keywords
    """
    def test_get_keywords_success(self):
        """
        Test get keywords success
        """
        keyword1 = Keyword.create(
                ad_account_id=DEFAULT_AD_ACCOUNT_ID,
                parent_id=self.ad_group_utils.get_ad_group_id(),
                value="Keyword_SDK_1",
                match_type="BROAD",
                bid=1000)
        keyword2 = Keyword.create(
                ad_account_id=DEFAULT_AD_ACCOUNT_ID,
                parent_id=self.ad_group_utils.get_ad_group_id(),
                value="Keyword_SDK_2",
                match_type="BROAD",
                bid=1000)
        keywords = set([getattr(keyword1, "_id"), getattr(keyword2, "_id")])

        keywords_from_get, _ = Keyword.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=self.ad_group_utils.get_ad_group_id(),
            page_size=25,
        )

        assert len(keywords) == len(keywords_from_get)
        for kw in keywords_from_get:
            assert getattr(kw, "_id") in keywords


class TestUpdateKeyword(BaseTestCase):
    """
    Test get keywords
    """
    def test_update_keyword_success(self):
        """
        Test update Keyword success
        """
        Keyword.create(
                ad_account_id=DEFAULT_AD_ACCOUNT_ID,
                parent_id=self.ad_group_utils.get_ad_group_id(),
                value="Keyword_SDK_1",
                match_type="BROAD",
                bid=1000)

        keywords, _ = Keyword.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=self.ad_group_utils.get_ad_group_id(),
            page_size=25,
        )
        keyword = keywords[0]

        new_archived = not getattr(keyword, "_archived")
        keyword.update_fields(
            archived=new_archived
        )

        assert keyword
        assert getattr(keyword, "_archived") == new_archived
