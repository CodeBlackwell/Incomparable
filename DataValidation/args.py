# Argument parse for Le's comparison script
# Note that defaults are not needed here because they are passed from deploy.py (which has its own argument set)

import argparse

parser = argparse.ArgumentParser("Run regression over Avantlink Dashboard Reports by report category")
parser.add_argument('-p', '--period', type=str, help="'last year', 'last quarter', or 'last month'", required=False)
parser.add_argument('-m', '--manual', action='store_true',
                    help="Run in manual mode if you want to insert your request objects manually", required=False)
parser.add_argument('-ra', '--run-all', action='store_true')
parser.add_argument('-s', '--sim', type=str, help="i.e 'kiran_dev', 'adam_dev', 'le_dev'")
parser.add_argument('-j', '--join', type=str,
                    help="the name of the colum(s) to perform the join on. If multiple cols - use ',' to separate the cols.")
parser.add_argument('-r', '--remove', type=str,
                    help="the name of the colum(s) to remove. If multiple cols - use ',' to separate the cols.")  # Todo: Add Drop Columns Functionality
parser.add_argument('-d', '--diffs', action='store_true')  # Todo: add show only rows that are different
parser.add_argument('-c', '--comparison-column', type=str,
                    help="The name of the column to be compared (must be an int or float)")
parser.add_argument('-sd', '--start-date', type=str, help="The Start Date - Format == mm_dd_yyyy")
parser.add_argument('-ed', '--end-date', type=str, help="The End Date - Format === mm_dd_yyyy")
parser.add_argument('-mer', '--merchant', type=str, help="The merchant uuid or merchant name")
parser.add_argument('-source', '--source', type=str, help="Gives the specifc data type source to retrieve")
parser.add_argument('-ne', '--no-error', action='store_true')
parser.add_argument('-rh', '--remove_hidden', action="store_true")
parser.add_argument('-rda', '--remove-date-aggs', action="store_true")
parser.add_argument('-rs', '--remove-sort', action="store_true")
parser.add_argument('-ul', '--update-logs', action="store_true", help="including this option will cause the changelogs generated to upload to the company spreadsheet")
parser.add_argument('-native', '--native', action="store_true", help="Including this option will force the test suite to use NATIVE currecny")
parser.add_argument('-mm', '--multi-merchant', type=str,
                        help="The name of the merchants to run - use ',' to separate the merchant names")
args = parser.parse_args()