'''
Test Keyword Model
'''
from unittest import TestCase
from unittest.mock import patch

from pinterest.generated.client.model.paginated import Paginated
from pinterest.generated.client.model.keyword import Keyword as GeneratedKeyword
from pinterest.generated.client.model.keywords_response import KeywordsResponse
from pinterest.generated.client.model.match_type_response import MatchTypeResponse


from pinterest.ads.keywords import Keyword

from pinterest.generated.client.model.match_type_response import MatchTypeResponse

class TestKeyword(TestCase):
    '''
    Test Keyword Model and its higher level functions
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_ad_account_id = "777777777777"
        self.test_keyword_id = "888888888888"

    @patch('pinterest.ads.keywords.KeywordsApi.keywords_get')
    def test_create_keyword_model_using_existing_keyword(self, keyword_get_mock):
        '''
        Test if Keyword model/object is created successfully with correct account_id, keyword_id
        '''
        keyword_get_mock.return_value = Paginated(
                items=[
                        {
                            "archived": False,
                            "id": self.test_keyword_id,
                            "parent_id": "383791336903426391",
                            "parent_type": "campaign",
                            "type": "keyword",
                            "bid": 200000,
                            "match_type": "BROAD",
                            "value": "string",
                        },
                ],      
                bookmark="test_keyword",
        )

        keyword_response, _ = Keyword.get_all(
            ad_account_id=self.test_ad_account_id,
            campaign_id="383791336903426391",
            page_size=1,
        )
        keyword = keyword_response[0]
        

        assert getattr(keyword, '_id') == self.test_keyword_id
        assert getattr(keyword, '_ad_account_id') == self.test_ad_account_id
        assert getattr(keyword, '_parent_id') == "383791336903426391"
        assert getattr(keyword, '_parent_type') == "campaign"

    @patch('pinterest.ads.keywords.KeywordsApi.keywords_create')
    @patch('pinterest.ads.keywords.KeywordsApi.keywords_get')
    def test_create_keyword_model_new_keyword(self, keyword_get_mock, keyword_create_mock):
        """
        Test if a Keyword model/object is created successfully with correct account_id and keyword
        """
        keyword_get_mock.return_value = Paginated(
                items=[
                        {
                            "archived": False,
                            "id": self.test_keyword_id,
                            "parent_id": "383791336903426391",
                            "parent_type": "campaign",
                            "type": "keyword",
                            "bid": 200000,
                            "match_type": "BROAD",
                            "value": "string",
                        },
                ],      
                bookmark="string",                
        )

        keyword_create_mock.return_value = KeywordsResponse(
            keywords=[GeneratedKeyword(
                                archived=False,
                                id=self.test_keyword_id,
                                parent_id="383791336903426391",
                                parent_type="campaign",
                                type="keyword",
                                bid=200000,
                                match_type=MatchTypeResponse("BROAD"),
                                value="string",
                            )
                    ],
            errors=[],
        )

        created_keyword = Keyword.create(
            ad_account_id=self.test_ad_account_id,
            parent_id="383791336903426391",
            value="string",
            match_type="BROAD",
        )

        assert created_keyword
        assert getattr(created_keyword, '_id')
        assert getattr(created_keyword, '_ad_account_id') == self.test_ad_account_id
        assert getattr(created_keyword, '_value') == "string"
        assert getattr(created_keyword, '_match_type') == MatchTypeResponse("BROAD")


    @patch('pinterest.ads.keywords.KeywordsApi.keywords_update')
    @patch('pinterest.ads.keywords.KeywordsApi.keywords_get')
    def test_update_keyword_success(self, get_mock, update_mock):
        """
        Test if Keyword Model can be updated
        """
        new_bid = 10

        get_mock.return_value = Paginated(
                items=[
                        {
                            "archived": False,
                            "id": self.test_keyword_id,
                            "parent_id": "383791336903426391",
                            "parent_type": "campaign",
                            "type": "keyword",
                            "bid": 200000,
                            "match_type": "BROAD",
                            "value": "string",
                        },
                ],      
                bookmark="test_keyword",
        )
        update_mock.return_value = KeywordsResponse(
            errors=[
            ],
            keywords=[
                GeneratedKeyword(
                    archived=False,
                    id=self.test_keyword_id,
                    parent_id="383791336903426391",
                    parent_type="campaign",
                    type="keyword",
                    bid=new_bid,
                    match_type=MatchTypeResponse("BROAD"),
                    value="string",
                )
            ]
        )

        keywords, _ = Keyword.get_all(
            ad_account_id=self.test_ad_account_id,
            campaign_id="383791336903426391",
            page_size=1,
        )
        keyword = keywords[0]
        update_response = keyword.update_fields(
            bid=new_bid
        )

        assert update_response == True
        assert getattr(keyword, "_id") == self.test_keyword_id
        assert getattr(keyword, "_bid") == new_bid
