import unittest
from sources import AvantMetricsComparison

class TestAvantMetricsComparison(unittest.TestCase):
    def setUp(self):
        # Setup code to run before each test. For example, you might instantiate the class here.
        self.comparison = AvantMetricsComparison(report_name="Test Report", reports=[])

    def test_init(self):
        # Test the __init__ method
        self.assertEqual(self.comparison.report_name, "Test Report")
        self.assertEqual(self.comparison.reports, [])
        # Add more assertions as needed

    def test_convert_date_range_for_classic(self):
        # Test the __convert_date_range_for_classic__ static method
        result = AvantMetricsComparison.__convert_date_range_for_classic__("01/01/2023 - 01/02/2023")
        self.assertEqual(result, ("01", "01", "2023", "02", "01", "2023"))
        # Add more assertions as needed

    def test_convert_date_range_for_classic(self):
        # Test the __convert_date_range_for_classic__ method
        pass

    def test_search_merchant(self):
        # Test the search_merchant method
        pass

    def test_replace_merchant(self):
        # Test the replace_merchant method
        pass

    def test_get_prepared_cols(self):
        # Test the get_prepared_cols method
        pass

    def test_retrieve_request_object(self):
        # Test the __retrieve_request_object__ method
        pass

    def test_insert_edw2_avantmetrics_request_filters(self):
        # Test the insert_edw2_avantmetrics_request_filters method
        pass

    def test_fetch_classic_report(self):
        # Test the fetch_classic_report method
        pass

    def test_fetch_picker_report(self):
        # Test the fetch_picker_report method
        pass

    def test_compare_reports(self):
        # Test the compare_reports method
        pass

    def test_compare_website_order_details(self):
        # Test the compare_website_order_details method
        pass

    def test_compare_referral_group_order_details(self):
        # Test the compare_referral_group_order_details method
        pass

if __name__ == '__main__':
    unittest.main()

