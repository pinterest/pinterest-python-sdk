"""
Test CustomerList Model
"""
from unittest.mock import patch

from openapi_generated.pinterest_client.exceptions import ApiValueError

from pinterest.ads.customer_lists import CustomerList

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID


class TestCreateCustomerList(BaseTestCase):
    """
    Test creating CustomerList model
    """
    def test_create_customer_list_success(self):
        """
        Test creating a new CustomerList successfully
        """
        customer_list = CustomerList.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Customer List",
            records="test@pinterest.com",
            list_type="EMAIL",
        )

        assert customer_list
        assert getattr(customer_list, '_id')
        assert getattr(customer_list, '_name') == "SDK Test Customer List"

    def test_create_customer_list_failure_incorrect_list_type(self):
        """
        Verify a new CustomerList response failure and catching exceptions
        """
        customer_list_arguments = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Customer List",
            records="test@pinterest.com",
            list_type="INCORRECT_LIST_TYPE"
        )
        with self.assertRaisesRegex(ApiValueError, "Invalid"):
            CustomerList.create(**customer_list_arguments)


class TestGetCustomerList(BaseTestCase):
    """
    Test retrieving CustomerList model
    """
    def test_get_existing_customer_list_success(self):
        """
        Test if a Customer model/object is created successfully with correct customer_list_id
        """
        customer_list = CustomerList(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            customer_list_id=self.customer_list_utils.get_customer_list_id(),
            client=self.test_client
            )
        assert customer_list
        assert getattr(customer_list, '_id') == self.customer_list_utils.get_customer_list_id()


class TestUpdateCustomerList(BaseTestCase):
    """
    Test updating fields in CustomerList model
    """
    def test_update_field_with_append_operation_success(self):
        """
        Test upating field successfully with APPEND operation
        """
        customer_list = CustomerList(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            customer_list_id=self.customer_list_utils.get_customer_list_id(),
            client=self.test_client
            )

        old_add_counter = getattr(customer_list, "_num_uploaded_user_records")
        old_batches_counter = getattr(customer_list, "_num_batches")

        customer_list.update_fields(
            records="test_add@pinterest.com",
            operation_type="ADD",
            )

        assert customer_list
        assert getattr(customer_list, "_num_uploaded_user_records") == old_add_counter+1
        assert getattr(customer_list, "_num_batches") == old_batches_counter+1

    def test_update_field_with_remove_operation_success(self):
        """
        Test upating field successfully with REMOVE operation
        """
        customer_list = CustomerList(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            customer_list_id=self.customer_list_utils.get_customer_list_id(),
            client=self.test_client
            )

        old_remove_counter = getattr(customer_list, "_num_removed_user_records")
        old_batches_counter = getattr(customer_list, "_num_batches")

        customer_list.update_fields(
            records="test_remove@pinterest.com",
            operation_type="REMOVE",
            )

        assert customer_list
        assert getattr(customer_list, "_num_removed_user_records") == old_remove_counter+1
        assert getattr(customer_list, "_num_batches") == old_batches_counter+1

    def test_update_missing_require_field(self):
        """
        Test missing required field: records
        """
        customer_list = CustomerList(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            customer_list_id=self.customer_list_utils.get_customer_list_id(),
            client=self.test_client
            )

        customer_list_arguments = dict(
            operation_type="ADD",
            )

        with self.assertRaises(TypeError):
            customer_list.update_fields(**customer_list_arguments)

class TestGetListCustomerList(BaseTestCase):
    """
    Test get list in CustomerList model
    """
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    def test_get_all(self, customer_lists_get_mock):
        # pylint: disable=consider-using-set-comprehension
        """
        Test if all customer list can be retrived from Ad account
        """
        NUMBER_OF_NEW_CUSTOMER_LIST = 3
        created_customer_list_ids = set(
            getattr(self.customer_list_utils.create_new_customer_list(), '_id') \
            for _ in range(NUMBER_OF_NEW_CUSTOMER_LIST)
        )

        assert len(created_customer_list_ids) == NUMBER_OF_NEW_CUSTOMER_LIST

        customer_lists_list, _ = CustomerList.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            order="DESCENDING",
            page_size=NUMBER_OF_NEW_CUSTOMER_LIST,
        )

        assert customer_lists_get_mock.call_count - 1 == NUMBER_OF_NEW_CUSTOMER_LIST
        assert len(created_customer_list_ids) == len(customer_lists_list)

        get_all_customer_lists_ids = set()
        for customer_list in customer_lists_list:
            get_all_customer_lists_ids.add(getattr(customer_list, '_id'))
            assert isinstance(customer_list, CustomerList)

        assert created_customer_list_ids == get_all_customer_lists_ids


class TestAddRemoveCustomerList(BaseTestCase):
    """
    Test add/remove list in CustomerList model
    """
    def setUp(self) -> None:
        super().setUp()
        self.record_default = 'EA7583CD-B890-48BC-B542-42ECB2B48606'
        self.records_aux = [
            'EA7583CD-B890-48BC-B816-42ECB2B48606',
            'EA7583CD-P667-48BC-B856-42ECB2B48606',
            'EA7583CD-P667-48BC-B866-42ECB2B48606',
        ]
        self.all_records = self.records_aux + [self.record_default]

    def test_add_customer_list(self):
        """
        Test add list to CustomerList model
        """
        customer_list = self.customer_list_utils.create_new_customer_list(
            records=self.record_default
        )
        self.assertEqual(getattr(customer_list, '_num_uploaded_user_records'), 1)

        for record in self.records_aux:
            customer_list.add_record(record)

        self.assertEqual(getattr(customer_list, '_num_uploaded_user_records'), len(self.all_records))

    def test_remove_customer_list(self):
        """
        Test remove list to CustomerList model
        """
        customer_list = self.customer_list_utils.create_new_customer_list(
            records=self.record_default
        )
        for record in self.records_aux:
            customer_list.add_record(record)

        prev_count = getattr(customer_list, '_num_uploaded_user_records')

        for record in self.records_aux:
            customer_list.remove_record(record)

        next_count = getattr(customer_list, '_num_removed_user_records')

        self.assertEqual(prev_count, len(self.all_records))
        self.assertEqual(next_count, len(self.all_records)-1)
