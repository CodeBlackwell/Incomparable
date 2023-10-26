true = True
false = False

set_1 = [
    {
        "performance_summary": {
            "cols": [
                {
                    "id": "dim_affiliate_default_website-affiliate_website_id",
                    "alias": "affiliate_default_website_id",
                    "name": "affiliate_default_website",
                    "hidden": true
                },
                {
                    "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                    "alias": "affiliate_default_website",
                    "name": "affiliate_default_website"
                },
                {
                    "id": "calculation",
                    "calc": "affiliate + network",
                    "name": "Adjusted Cost",
                    "vars": {
                        "network": {
                            "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                            "alias": "fact_order_commission_adjustment-network_commission_adjustment_amount-02",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "required_groups": [
                                "fact_order_commission_adjustment-network_commission_adjustment_amount-02"
                            ]
                        },
                        "affiliate": {
                            "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                            "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-01",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "required_groups": [
                                "fact_order_commission_adjustment-order_commission_adjustment_amount-01"
                            ]
                        }
                    },
                    "alias": "adjusted_cost",
                    "format": "money",
                    "invert_sort": true
                }
            ],
            "report_name": "Custom Report",
            "format": "json",
            "filters": [
                {
                    "field": "dim_date-mm_dd_yyyy",
                    "op": "relative_date",
                    "values": [],
                    "alias": "date_picker1",
                    "allow_empty": true,
                    "to_date": false,
                    "count": 3,
                    "start": -1,
                    "period": "month"
                }
            ],
            "partitions": [],
            "sort": [],
            "totals": true,
            "widths": true,
            "counts": true,
            "partitionLimit": 26,
            "offset": 0,
            "limit": 30,
            "partitionOffset": 0
        }
    },
    {'rpt': {'cols': [{'aggregate': [{'distinct': False,
                                      'func': 'count'}],
                       'alias': 'affiliate_order_id',
                       'fact': True,
                       'format': 'int',
                       'id': 'affiliate_type_order-order_id',
                       'name': 'Affiliate Orders'}]}}
]
