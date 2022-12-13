"""
Test CustomerList Model
"""

from unittest import TestCase
from unittest.mock import patch
from webbrowser import get

from pinterest.generated.client.model.customer_list import CustomerList as GeneratedCustomerList

from pinterest.ads.customer_lists import CustomerList


class TestCustomerList(TestCase):
    """
    Test CustomerList model and its higher level functions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_ad_account_id = "777777777777"
        self.test_customer_list_id = "111111111111"

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    def test_create_customer_list_model_using_existing_customer_list(self, customer_lists_get_mock):
        """
        Test if a CustomerList model/object is created successfully with correct customer_list_id
        """

        customer_lists_get_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
            )

        customer_list_response = CustomerList(
            ad_account_id=self.test_ad_account_id,
            customer_list_id=self.test_customer_list_id
            )

        assert getattr(customer_list_response, '_id') == self.test_customer_list_id
        assert getattr(customer_list_response, '_name') == 'Test Customer List'

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_create')
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    def test_create_new_customer_list(self, customer_lists_get_mock, customer_lists_create_mock):
        """
        Test if a CustomerList model/object is created successfully with correct information
        """
        customer_lists_create_mock.__name__ = "customer_lists_create"
        customer_lists_create_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
            )
        customer_lists_get_mock.return_value = customer_lists_create_mock.return_value

        created_customer_list = CustomerList.create(
            ad_account_id=self.test_ad_account_id,
            name="Test Customer List",
            records="test@pinterest.com",
            list_type="EMAIL",
        )

        assert created_customer_list
        assert getattr(created_customer_list, '_name') == "Test Customer List"

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_update')
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    def test_update_customer_list(self, customer_lists_get_mock, customer_lists_update_mock):
        """
        Test if a CustomerList model/object is created successfully with correct customer_list_id
        """
        customer_lists_update_mock.__name__ = "customer_lists_get"

        old_batch, new_batch = 1.0, 2.0
        old_remove_counter, new_remove_counter = 0.0, 1.0

        customer_lists_get_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=old_batch,
            num_removed_user_records=old_remove_counter,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
            )

        customer_lists_update_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=new_batch,
            num_removed_user_records=new_remove_counter,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
        )

        customer_list_response = CustomerList(
            ad_account_id=self.test_ad_account_id,
            customer_list_id=self.test_customer_list_id
            )

        customer_lists_get_mock.return_value = customer_lists_update_mock.return_value

        update_response = customer_list_response.update_fields(
            records="test_remove@pinterest.com",
            operation_type="REMOVE",
        )

        assert update_response == True
        assert getattr(customer_list_response, "_num_batches") == new_batch
        assert getattr(customer_list_response, "_num_removed_user_records") == new_remove_counter

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_list')
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    def test_get_all_customer_list(self, get_mock, list_mock):
        """
        Test if customer list is updated successfully with passed in kwargs
        """
        get_mock.__name__ = "customer_lists_get"
        list_mock.__name__ = "customer_lists_list"
        list_mock.return_value = {
            "items": [
                {
                    "ad_account_id": self.test_ad_account_id,
                    "created_time": 1452208622,
                    "id": "643",
                    "name": "The Glengarry Glen Ross leads",
                    "num_batches": 2,
                    "num_removed_user_records": 0,
                    "num_uploaded_user_records": 11,
                    "status": "PROCESSING",
                    "type": "customerlist",
                    "updated_time": 1461269616,
                    "exceptions": {},
                }
            ],
            "bookmark": "test_bookmark",
        }

        customer_lists, bookmark = CustomerList.get_all(
            ad_account_id=self.test_ad_account_id,
            page_size=1,
        )

        get_mock.assert_not_called()

        assert customer_lists
        assert bookmark.get_bookmark_token() == "test_bookmark"
        assert getattr(customer_lists[0], "_id") == "643"

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_update')
    def test_add_record_customer_list(self, customer_lists_get_mock, customer_lists_update_mock):
        """
        Test add record customer list
        """
        customer_lists_update_mock.__name__ = "customer_lists_update"
        customer_lists_get_mock.__name__ = "customer_lists_get"

        customer_lists_get_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
        )

        customer_lists_update_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=2.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
        )

        customer_list = CustomerList(
            ad_account_id=self.test_ad_account_id,
            customer_list_id=self.test_customer_list_id
        )

        self.assertTrue(customer_list.add_record('test'))

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_update')
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    def test_add_record_customer_list(self, customer_lists_get_mock, customer_lists_update_mock):
        """
        Test remove record customer list
        """
        customer_lists_update_mock.__name__ = "customer_lists_update"
        customer_lists_get_mock.__name__ = "customer_lists_get"

        customer_lists_get_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
        )

        customer_lists_update_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=2.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
        )

        customer_list = CustomerList(
            ad_account_id=self.test_ad_account_id,
            customer_list_id=self.test_customer_list_id
        )

        self.assertTrue(customer_list.remove_record('test'))
