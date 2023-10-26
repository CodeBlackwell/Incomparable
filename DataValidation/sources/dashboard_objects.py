false = False
true = True
null = None

edw2_dashboard_objects = {
    "trending_widget": {
        "Sales": {
            "Sales": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "calculation",
                            "calc": "sales + adjustments",
                            "fact": true,
                            "name": "Sales",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "adjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                }
                            },
                            "alias": "net_sales",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "ROAS %": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "calculation",
                            "calc": "(sales + cadjustments) / (sale+incentive+cpc+ppb+bonus+adjustment+nadjustment+ncpc+nppb+nbonus+nsale)",
                            "fact": true,
                            "name": "ROAS %",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "alias": "fact_cpc_earning-affiliate_earnings-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "alias": "fact_ppb_earning-bid_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "alias": "fact_cpc_earning-network_earnings-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "alias": "fact_ppb_earning-network_commission-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "alias": "fact_order_commission-sale_commission_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "alias": "fact_order_bonus-bonus_commission_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "alias": "fact_order_commission-network_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "alias": "fact_order_avantlink-order_amount-02",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "alias": "fact_order_bonus-bonus_network_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "alias": "fact_order_commission-incentive_commission_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-network_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "alias": "fact_order_adjustment-order_combined_adjustment_amount-02",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "return_on_ad_spend_percent",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "ROAS": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "calculation",
                            "calc": "(sales + cadjustments) / (sale+incentive+cpc+ppb+bonus+adjustment+nadjustment+ncpc+nppb+nbonus+nsale)",
                            "fact": true,
                            "name": "ROAS",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "return_on_ad_spend",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Orders": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "fact_order_avantlink-order_hash_key",
                            "fact": true,
                            "name": "Orders",
                            "alias": "number_of_orders",
                            "format": "int",
                            "aggregate": [
                                {
                                    "func": "count",
                                    "distinct": true
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Gross Sales": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "fact_order_avantlink-order_amount",
                            "fact": true,
                            "name": "Gross Sales",
                            "alias": "gross_sales",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": true
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Conversion Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "calculation",
                            "calc": "orders / clicks",
                            "fact": true,
                            "name": "Conversion Rate",
                            "vars": {
                                "clicks": {
                                    "id": "fact_hit-summary_hit_count",
                                    "aggregate": [
                                        {
                                            "func": "sum"
                                        }
                                    ]
                                },
                                "orders": {
                                    "id": "fact_order_avantlink-order_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                }
                            },
                            "alias": "conversion_rate",
                            "format": "percent2"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Average Order Amount": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]
                        },
                        {
                            "id": "calculation",
                            "calc": "sales / total",
                            "fact": true,
                            "name": "Average Order Amount",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ]
                                },
                                "total": {
                                    "id": "fact_order_avantlink-order_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                }
                            },
                            "alias": "avg_order_amount",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            }
        },
        "Combined Commission": {
            "Total Cost": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "sale+incentive+cpc+ppb+bonus+adjustment+nadjustment+ncpc+nppb+nbonus+nsale",
                            "fact": true,
                            "name": "Total Cost",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "total_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Sale Commission": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "affsales+affadjustments+netwsales+netwadjustments",
                            "fact": true,
                            "name": "Sale Commission",
                            "vars": {
                                "affsales": {
                                    "id": "fact_order_commission-sale_commission_amount"
                                },
                                "netwsales": {
                                    "id": "fact_order_commission-network_commission_amount"
                                },
                                "affadjustments": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount"
                                },
                                "netwadjustments": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount"
                                }
                            },
                            "alias": "sale_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Paid Placement": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "affiliateppb + networkppb",
                            "fact": true,
                            "name": "Paid Placement",
                            "vars": {
                                "networkppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                },
                                "affiliateppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                }
                            },
                            "alias": "combined_ppb",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Incentive Commission": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_commission-incentive_commission_amount",
                            "fact": true,
                            "name": "Incentive Commission",
                            "alias": "incentive_commission",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "CPC": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "affiliatecpc + networkcpc",
                            "fact": true,
                            "name": "CPC",
                            "vars": {
                                "networkcpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                },
                                "affiliatecpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                }
                            },
                            "alias": "combined_cpc",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Bonus": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "affiliatebonus + networkcommission",
                            "fact": true,
                            "name": "Bonus",
                            "vars": {
                                "affiliatebonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                },
                                "networkcommission": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                }
                            },
                            "alias": "combined_bonus",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            }
        },
        "Affiliate Commission": {
            "Affiliate Bonus": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_bonus-bonus_commission_amount",
                            "fact": true,
                            "name": "Affiliate Bonus",
                            "alias": "affiliate_bonus",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Affiliate CPC": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_cpc_earning-affiliate_earnings",
                            "fact": true,
                            "name": "Affiliate CPC",
                            "alias": "affiliate_cpc",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Affiliate Incentive Commission": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_commission-incentive_commission_amount",
                            "fact": true,
                            "name": "Affiliate Incentive Commission",
                            "alias": "affiliate_incentive_commission",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Affiliate Paid Placement": {},
            "Affiliate Sale Commission": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "sales+adjustments",
                            "fact": true,
                            "name": "Affiliate Sale Commission",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_commission-sale_commission_amount"
                                },
                                "adjustments": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount"
                                }
                            },
                            "alias": "affiliate_sale_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Affiliate Total Commission Average Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "(sale+incentive+cpc+adjustment) / (sales + cadjustments)",
                            "fact": true,
                            "name": "Affiliate Total Commission Average Rate",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "affiliate_total_commission_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Affiliate Total Earnings": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "sale+incentive+cpc+ppb+bonus+adjustment",
                            "fact": true,
                            "name": "Affiliate Total Earnings",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "affiliate_total_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Affiliate Total Earnings Average Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "(sale+incentive+cpc+ppb+bonus+adjustment)/(sales+cadjustments)",
                            "fact": true,
                            "name": "Affiliate Total Earnings Average Rate",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "alias": "fact_cpc_earning-affiliate_earnings-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "alias": "fact_ppb_earning-bid_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "alias": "fact_order_commission-sale_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "alias": "fact_order_bonus-bonus_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "alias": "fact_order_avantlink-order_amount-01",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "alias": "fact_order_commission-incentive_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "alias": "fact_order_adjustment-order_combined_adjustment_amount-01",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "affiliate_total_earnings_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "EPC": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "(sale+incentive+cpc+ppb+bonus+adjustment)/(clicks/100)",
                            "fact": true,
                            "name": "EPC",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "clicks": {
                                    "id": "fact_hit-summary_hit_count",
                                    "required_groups": [
                                        "clicks"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "earnings_per_click",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            }
        },
        "Network Commission": {
            "Network CPC": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_cpc_earning-network_earnings",
                            "fact": true,
                            "name": "Network CPC",
                            "alias": "network_cpc",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Network Paid Placement": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_ppb_earning-network_commission",
                            "fact": true,
                            "name": "Network Paid Placement",
                            "alias": "network_ppb",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Network Bonus": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_bonus-bonus_network_commission_amount",
                            "fact": true,
                            "name": "Network Bonus",
                            "alias": "network_bonus",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Network Sale Commission": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "sales+adjustments",
                            "fact": true,
                            "name": "Network Sale Commission",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_commission-network_commission_amount"
                                },
                                "adjustments": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount"
                                }
                            },
                            "alias": "network_sale_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Network Total Commission Average Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "(ncpc+nsale+adjustment) / (sales+cadjustments)",
                            "fact": true,
                            "name": "Network Total Commission Average Rate",
                            "vars": {
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "alias": "fact_cpc_earning-network_earnings",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "alias": "fact_order_commission-network_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "alias": "fact_order_avantlink-order_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-network_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "alias": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "network_total_commission_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Network Total Earnings": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "adjustment+cpc+ppb+bonus+sale",
                            "fact": true,
                            "name": "Network Total Earnings",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "network_total_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Network Total Earnings Average Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "(nadjustment+ncpc+nppb+nbonus+nsale) / (sales+cadjustments)",
                            "fact": true,
                            "name": "Network Total Earnings Average Rate",
                            "vars": {
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "network_total_earnings_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            }
        },
        "Clicks % Impressions": {
            "Click Through Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "clicks / impressions",
                            "fact": true,
                            "name": "Click Through Rate",
                            "vars": {
                                "clicks": {
                                    "id": "fact_hit-summary_hit_count",
                                    "aggregate": [
                                        {
                                            "func": "sum"
                                        }
                                    ]
                                },
                                "impressions": {
                                    "id": "fact_impression-summary_impression_count",
                                    "aggregate": [
                                        {
                                            "func": "sum"
                                        }
                                    ]
                                }
                            },
                            "alias": "click_through_rate",
                            "format": "percent2"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Clicks": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_hit-summary_hit_count",
                            "fact": true,
                            "name": "Clicks",
                            "alias": "number_of_clicks",
                            "format": "int"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Impressions": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_impression-summary_impression_count",
                            "fact": true,
                            "name": "Impressions",
                            "alias": "number_of_impressions",
                            "format": "int"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            }
        },
        "Adjustments": {
            "Adjusted Affiliate Earnings": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                            "fact": true,
                            "name": "Adjusted Affiliate Earnings",
                            "alias": "adjusted_affiliate_earnings",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "invert_sort": true
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Adjusted Sales": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_adjustment-order_combined_adjustment_amount",
                            "fact": true,
                            "name": "Adjusted Sales",
                            "alias": "adjustments_sum",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "invert_sort": true
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Adjustments": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "fact_order_adjustment-adjustment_hash_key",
                            "fact": true,
                            "name": "Adjustments",
                            "alias": "adjustments_count",
                            "format": "int",
                            "aggregate": [
                                {
                                    "func": "count",
                                    "distinct": true
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            },
            "Reversal Rate": {
                "trending_widget": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "name": "Day",
                            "alias": "mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range"
                                }
                            ]},
                        {
                            "id": "calculation",
                            "calc": "adjustments/orders",
                            "fact": true,
                            "name": "Reversal Rate",
                            "vars": {
                                "orders": {
                                    "id": "fact_order_avantlink-order_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                },
                                "adjustments": {
                                    "id": "fact_order_adjustment-adjustment_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                }
                            },
                            "alias": "reversal_rate",
                            "format": "percent2"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [

                    ],
                    "totals": false,
                    "widths": false,
                    "counts": false,
                    "partitionLimit": 4,
                    "offset": 0,
                    "currency": "NATIVE",
                    "partitionOffset": 0,
                    "limit": 500
                }
            }
        }
    },
    "top_affiliates_widget": {
        "Sales": {
            "Average Order Amount": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "sales / total",
                            "fact": true,
                            "name": "Average Order Amount",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ]
                                },
                                "total": {
                                    "id": "fact_order_avantlink-order_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                }
                            },
                            "alias": "avg_order_amount",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "avg_order_amount",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "partitionOffset": 0
                }
            },
            "Sales": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "sales + adjustments",
                            "fact": true,
                            "name": "Sales",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "adjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                }
                            },
                            "alias": "net_sales",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "net_sales",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "ROAS %": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(sales + cadjustments) / (sale+incentive+cpc+ppb+bonus+adjustment+nadjustment+ncpc+nppb+nbonus+nsale)",
                            "fact": true,
                            "name": "ROAS %",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "alias": "fact_cpc_earning-affiliate_earnings-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "alias": "fact_ppb_earning-bid_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "alias": "fact_cpc_earning-network_earnings-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "alias": "fact_ppb_earning-network_commission-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "alias": "fact_order_commission-sale_commission_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "alias": "fact_order_bonus-bonus_commission_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "alias": "fact_order_commission-network_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "alias": "fact_order_avantlink-order_amount-02",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "alias": "fact_order_bonus-bonus_network_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "alias": "fact_order_commission-incentive_commission_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-02",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-network_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "alias": "fact_order_adjustment-order_combined_adjustment_amount-02",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "return_on_ad_spend_percent",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "return_on_ad_spend_percent",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "ROAS": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(sales + cadjustments) / (sale+incentive+cpc+ppb+bonus+adjustment+nadjustment+ncpc+nppb+nbonus+nsale)",
                            "fact": true,
                            "name": "ROAS",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "return_on_ad_spend",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "return_on_ad_spend",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Orders": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_avantlink-order_hash_key",
                            "fact": true,
                            "name": "Orders",
                            "alias": "number_of_orders",
                            "format": "int",
                            "aggregate": [
                                {
                                    "func": "count",
                                    "distinct": true
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "number_of_orders",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Gross Sales": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_avantlink-order_amount",
                            "fact": true,
                            "name": "Gross Sales",
                            "alias": "gross_sales",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": true
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "gross_sales",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Conversion Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "orders / clicks",
                            "fact": true,
                            "name": "Conversion Rate",
                            "vars": {
                                "clicks": {
                                    "id": "fact_hit-summary_hit_count",
                                    "aggregate": [
                                        {
                                            "func": "sum"
                                        }
                                    ]
                                },
                                "orders": {
                                    "id": "fact_order_avantlink-order_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                }
                            },
                            "alias": "conversion_rate",
                            "format": "percent2"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "conversion_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            }
        },
        "Combined Commission": {
            "Total Cost": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "sale+incentive+cpc+ppb+bonus+adjustment+nadjustment+ncpc+nppb+nbonus+nsale",
                            "fact": true,
                            "name": "Total Cost",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "total_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "total_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Sale Commission": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "affsales+affadjustments+netwsales+netwadjustments",
                            "fact": true,
                            "name": "Sale Commission",
                            "vars": {
                                "affsales": {
                                    "id": "fact_order_commission-sale_commission_amount"
                                },
                                "netwsales": {
                                    "id": "fact_order_commission-network_commission_amount"
                                },
                                "affadjustments": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount"
                                },
                                "netwadjustments": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount"
                                }
                            },
                            "alias": "sale_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "sale_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Paid Placement": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "affiliateppb + networkppb",
                            "fact": true,
                            "name": "Paid Placement",
                            "vars": {
                                "networkppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                },
                                "affiliateppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                }
                            },
                            "alias": "combined_ppb",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "combined_ppb",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Incentive Commission": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_commission-incentive_commission_amount",
                            "fact": true,
                            "name": "Incentive Commission",
                            "alias": "incentive_commission",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "incentive_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "CPC": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "affiliatecpc + networkcpc",
                            "fact": true,
                            "name": "CPC",
                            "vars": {
                                "networkcpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                },
                                "affiliatecpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                }
                            },
                            "alias": "combined_cpc",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "combined_cpc",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Bonus": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "networkcommission + affiliatebonus",
                            "fact": true,
                            "name": "Bonus",
                            "vars": {
                                "affiliatebonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                },
                                "networkcommission": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "combined commission"
                                    ]
                                }
                            },
                            "alias": "combined_bonus",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "combined_bonus",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            }
        },
        "Affiliate Commission": {
            "Affiliate Bonus": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_bonus-bonus_commission_amount",
                            "fact": true,
                            "name": "Affiliate Bonus",
                            "alias": "affiliate_bonus",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_bonus",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate CPC": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_cpc_earning-affiliate_earnings",
                            "fact": true,
                            "name": "Affiliate CPC",
                            "alias": "affiliate_cpc",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_cpc",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate Incentive Commission": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_commission-incentive_commission_amount",
                            "fact": true,
                            "name": "Affiliate Incentive Commission",
                            "alias": "affiliate_incentive_commission",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_incentive_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate Paid Placement": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_ppb_earning-bid_amount",
                            "fact": true,
                            "name": "Affiliate Paid Placement",
                            "alias": "affiliate_ppb",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_ppb",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate Sale Commission": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "sales+adjustments",
                            "fact": true,
                            "name": "Affiliate Sale Commission",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_commission-sale_commission_amount"
                                },
                                "adjustments": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount"
                                }
                            },
                            "alias": "affiliate_sale_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_sale_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate Total Commission Average Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(sale+incentive+cpc+adjustment) / (sales + cadjustments)",
                            "fact": true,
                            "name": "Affiliate Total Commission Average Rate",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "affiliate_total_commission_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_total_commission_average_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate Total Earnings": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "sale+incentive+cpc+ppb+bonus+adjustment",
                            "fact": true,
                            "name": "Affiliate Total Earnings",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "affiliate_total_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_total_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Affiliate Total Earnings Average Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(sale+incentive+cpc+ppb+bonus+adjustment)/(sales+cadjustments)",
                            "fact": true,
                            "name": "Affiliate Total Earnings Average Rate",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "alias": "fact_cpc_earning-affiliate_earnings-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "alias": "fact_ppb_earning-bid_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "alias": "fact_order_commission-sale_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "alias": "fact_order_bonus-bonus_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "alias": "fact_order_avantlink-order_amount-01",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "alias": "fact_order_commission-incentive_commission_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-order_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "alias": "fact_order_adjustment-order_combined_adjustment_amount-01",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "affiliate_total_earnings_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "affiliate_total_earnings_average_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "EPC": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(sale+incentive+cpc+ppb+bonus+adjustment)/(clicks/100)",
                            "fact": true,
                            "name": "EPC",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-affiliate_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-bid_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-sale_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "clicks": {
                                    "id": "fact_hit-summary_hit_count",
                                    "required_groups": [
                                        "clicks"
                                    ]
                                },
                                "incentive": {
                                    "id": "fact_order_commission-incentive_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "earnings_per_click",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "earnings_per_click",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            }
        },
        "Network Commission": {
            "Network CPC": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_cpc_earning-network_earnings",
                            "fact": true,
                            "name": "Network CPC",
                            "alias": "network_cpc",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_cpc",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Network Paid Placement": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_ppb_earning-network_commission",
                            "fact": true,
                            "name": "Network Paid Placement",
                            "alias": "network_ppb",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_ppb",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Network Bonus": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_bonus-bonus_network_commission_amount",
                            "fact": true,
                            "name": "Network Bonus",
                            "alias": "network_bonus",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum"
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_bonus",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Network Sale Commission": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "sales+adjustments",
                            "fact": true,
                            "name": "Network Sale Commission",
                            "vars": {
                                "sales": {
                                    "id": "fact_order_commission-network_commission_amount"
                                },
                                "adjustments": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount"
                                }
                            },
                            "alias": "network_sale_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_sale_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Network Total Commission Average Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(ncpc+nsale+adjustment) / (sales+cadjustments)",
                            "fact": true,
                            "name": "Network Total Commission Average Rate",
                            "vars": {
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "alias": "fact_cpc_earning-network_earnings",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "alias": "fact_order_commission-network_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "alias": "fact_order_avantlink-order_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "alias": "fact_order_commission_adjustment-network_commission_adjustment_amount-01",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "alias": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "network_total_commission_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_total_commission_average_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }

                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Network Total Earnings": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "adjustment+cpc+ppb+bonus+sale",
                            "fact": true,
                            "name": "Network Total Earnings",
                            "vars": {
                                "cpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "ppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "bonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "adjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "required_groups": [
                                        "commission"
                                    ]
                                }
                            },
                            "alias": "network_total_commission",
                            "format": "money"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_total_commission",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Network Total Earnings Average Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "(nadjustment+ncpc+nppb+nbonus+nsale) / (sales+cadjustments)",
                            "fact": true,
                            "name": "Network Total Earnings Average Rate",
                            "vars": {
                                "ncpc": {
                                    "id": "fact_cpc_earning-network_earnings",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nppb": {
                                    "id": "fact_ppb_earning-network_commission",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nsale": {
                                    "id": "fact_order_commission-network_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "sales": {
                                    "id": "fact_order_avantlink-order_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": true
                                        }
                                    ],
                                    "required_groups": [
                                        "sales"
                                    ]
                                },
                                "nbonus": {
                                    "id": "fact_order_bonus-bonus_network_commission_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "nadjustment": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "format": "money",
                                    "required_groups": [
                                        "commission"
                                    ]
                                },
                                "cadjustments": {
                                    "id": "fact_order_adjustment-order_combined_adjustment_amount",
                                    "format": "money",
                                    "aggregate": [
                                        {
                                            "func": "sum",
                                            "distinct": false
                                        }
                                    ],
                                    "required_groups": [
                                        "adjustments"
                                    ]
                                }
                            },
                            "alias": "network_total_earnings_average_rate",
                            "format": "percent1"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "network_total_earnings_average_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            }
        },
        "Clicks % Impressions": {
            "Click Through Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "clicks / impressions",
                            "fact": true,
                            "name": "Click Through Rate",
                            "vars": {
                                "clicks": {
                                    "id": "fact_hit-summary_hit_count",
                                    "aggregate": [
                                        {
                                            "func": "sum"
                                        }
                                    ]
                                },
                                "impressions": {
                                    "id": "fact_impression-summary_impression_count",
                                    "aggregate": [
                                        {
                                            "func": "sum"
                                        }
                                    ]
                                }
                            },
                            "alias": "click_through_rate",
                            "format": "percent2"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "click_through_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Clicks": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_hit-summary_hit_count",
                            "fact": true,
                            "name": "Clicks",
                            "alias": "number_of_clicks",
                            "format": "int"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "number_of_clicks",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Impressions": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_impression-summary_impression_count",
                            "fact": true,
                            "name": "Impressions",
                            "alias": "number_of_impressions",
                            "format": "int"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "number_of_impressions",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            }
        },
        "Adjustments": {
            "Adjusted Affiliate Earnings": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_commission_adjustment-order_commission_adjustment_amount",
                            "fact": true,
                            "name": "Adjusted Affiliate Earnings",
                            "alias": "adjusted_affiliate_earnings",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "invert_sort": true
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "adjusted_affiliate_earnings",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Adjusted Cost": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "affiliate + network",
                            "fact": true,
                            "name": "Adjusted Cost",
                            "vars": {
                                "network": {
                                    "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                                    "fact": true,
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
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "adjusted_cost",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Adjusted Network Earnings": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_commission_adjustment-network_commission_adjustment_amount",
                            "fact": true,
                            "name": "Adjusted Network Earnings",
                            "alias": "adjusted_network_earnings",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "invert_sort": true
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "adjusted_network_earnings",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Adjusted Sales": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_adjustment-order_combined_adjustment_amount",
                            "fact": true,
                            "name": "Adjusted Sales",
                            "alias": "adjustments_sum",
                            "format": "money",
                            "aggregate": [
                                {
                                    "func": "sum",
                                    "distinct": false
                                }
                            ],
                            "invert_sort": true
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "adjustments_sum",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Adjustments": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "fact_order_adjustment-adjustment_hash_key",
                            "fact": true,
                            "name": "Adjustments",
                            "alias": "adjustments_count",
                            "format": "int",
                            "aggregate": [
                                {
                                    "func": "count",
                                    "distinct": true
                                }
                            ]
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "adjustments_count",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            },
            "Reversal Rate": {
                "top_five_widget": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "name": "Affiliate Default Website",
                            "alias": "affiliate_default_website0"
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "date_range",
                            "name": "Date Range",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "dim": "dim_date-last_thirty_days"
                                }
                            ]
                        },
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_id",
                            "alias": "affiliate_default_website1",
                            "hidden": true
                        },
                        {
                            "id": "calculation",
                            "calc": "adjustments/orders",
                            "fact": true,
                            "name": "Reversal Rate",
                            "vars": {
                                "orders": {
                                    "id": "fact_order_avantlink-order_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                },
                                "adjustments": {
                                    "id": "fact_order_adjustment-adjustment_hash_key",
                                    "aggregate": [
                                        {
                                            "func": "count",
                                            "distinct": true
                                        }
                                    ]
                                }
                            },
                            "alias": "reversal_rate",
                            "format": "percent2"
                        }
                    ],
                    "report_name": "Custom Report",
                    "format": "json",
                    "filters": [
                        {
                            "field": "dim_date-mm_dd_yyyy",
                            "op": "relative_date",
                            "values": [

                            ],
                            "alias": "date_filter1",
                            "allow_empty": true,
                            "to_date": false,
                            "count": 30,
                            "start": -1,
                            "period": "day"
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ],
                            "alias": "merchant_filter1"
                        }
                    ],
                    "partitions": [

                    ],
                    "sort": [
                        {
                            "field": "reversal_rate",
                            "direction": "desc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "totals": true,
                    "widths": true,
                    "counts": true,
                    "partitionLimit": 1,
                    "offset": 0,
                    "limit": 10,
                    "currency": "NATIVE",
                    "partitionOffset": 0
                }
            }
        }
    }
}

edw3_dashboard_objects = {
    "trending_widget": {
        "Sales": {
            "Sales": {
                "kAkIWvWTx1v01b4LH": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "5aab673b-e77d-4744-a743-25a3f0d079db"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "ROAS %": {
                "kVZ12OO7jWFoNKhpO": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }

                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "e8cdff6c-5aec-4ea8-b078-907524040784"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "ROAS": {
                "kyTloaLq2uihFp237": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }

                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "ebf77986-b88e-4521-9345-1500ff68cce7"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Orders": {
                "kyGXDuME8CIt2ROZn": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "5a1b9d70-1db3-4670-bb4e-6710dc6e736a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Gross Sales": {
                "kSpg6tVrgRFmf3pGu": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Mm Dd Yyyy"
                        },
                        {
                            "prepared_id": "29c95852-5c17-4899-b4c9-3465fc943ec2"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Conversion Rate": {
                "kQ4gzZ1A7k2Evj1Nn": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "ef559898-c0d1-41d0-ad0b-25ae17040c14"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Average Order Amount": {
                "klQWbdAX7ge1IeWe9": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Mm Dd Yyyy"
                        },
                        {
                            "prepared_id": "c045f0b3-2e56-428b-a552-d256b22855a7"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            }
        },
        "Combined Commission": {
            "Total Cost": {
                "klfVJRnJHBBGidEBL": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "2d6b94d6-4bbe-4fc6-bb91-25f1b69cc0f2"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Sale Commission": {
                "kSE3zUcldxafIHa5U": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "67f503b5-29bc-4199-828f-66b02b2c4009"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Paid Placement": {
                "kEe5WaXjDjAT1Uc6W": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "dcd37006-96ab-4818-8c9e-abc1c2785969"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Incentive Commission": {
                "kRZ3YdxBjQBjPhmX0": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "680cbb72-e7be-4ebd-8661-051bf7599027"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "CPC": {
                "kvipwMZRd1FzRdd60": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "27945e4c-710f-407c-a0b6-21b965c27136"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Bonus": {
                "kZYQISrL294bak5Cs": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "5dff3e61-2760-4f74-86ed-3109761a02a2"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            }
        },
        "Network Commission": {
            "Network Bonus": {
                "kJWV0qWKYqXSpsNKq": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "9ca05455-5a3e-4bc6-929f-a8a823c97fde"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Network CPC": {
                "k1YtYEkWRmky13GTW": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "d4e60199-a71b-4431-aa44-3f86217bd5d3"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Network Paid Placement": {
                "kmaw4EYXATtH5tfCe": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "7de2e941-13a9-4e7e-9397-6008cc4160b3"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Network Sale Commission": {
                "kpxjEQqcdKEMwJ68L": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "36de7153-a578-4878-9657-31113bad1a14"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Network Total Commission Average Rate": {
                "kKMuwL6SUHZqf2oAP": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "fbf8a786-fd4c-4e4e-aafb-6aa2f66bae7b"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Network Total Earnings": {
                "kt20jactGWTDLLVJD": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "32a9cf02-0375-494f-b196-ef976d283aed"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Network Total Earnings Average Rate": {
                "kvq3ymeeIHUhBorXE": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "b3dbfb92-c7e7-4ef8-9e5c-865cf54f8c2e"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            }
        },
        "Clicks % Impressions": {
            "Click Through Rate": {
                "kaKWCqLmVaW9fXDSh": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "6323f6bb-1843-4ac3-a358-1b3ab6111a46"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Clicks": {
                "kShz5mMSParKBAZNW": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "d6e33659-669e-432b-8727-7c4f871011cb"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Impressions": {
                "kls0ldeEqpbJi2Lql": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "f8017c89-c326-48a9-a3cd-7362ab43eb95"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            }
        },
        "Adjustments": {
            "Adjusted Affiliate Earnings": {
                "kcEI87M2kyLdVvWcI": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "77872d95-6d07-4061-9f27-44f7b77d0500"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Adjusted Sales": {
                "kUvks4lJa7UjlI4Xi": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "c9ba8ae6-ce4c-4490-b8c3-6607dda92a0c"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Adjustments": {
                "ki6atyIuukeXSpI8S": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "fd05e48f-47b5-4739-9f9d-c3edff158bb7"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Reversal Rate": {
                "k3SdWvr6CVKSp4LXY": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "a8244e92-7afb-45f9-b228-1e04f8ec273a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            }
        },
        "Affiliate Commission": {
            "Affiliate Bonus": {
                "k0BUgU0Q60blioBhb": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "d922887c-4c50-49ef-93f7-37a37944dca8"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate CPC": {
                "kCJJa33nHyiiGyW09": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "c57ca314-145b-4131-bdaf-87beef851324"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate Incentive Commission": {
                "kQZrXnKlYGI4DaHpK": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "370a8642-95d4-4977-a96a-615783a6c923"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate Paid Placement": {
                "kEsij857XhvLWNiXI": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "ecaff0d4-5759-4c74-85e3-f3d37346bc19"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate Sale Commission": {
                "kX9hBiVb05Dg8h2ST": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "3afeb2e0-2335-45fb-a902-99c9715fa08a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate Total Commission Average Rate": {
                "kPqCcXqkdcGaNLo2n": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "2bef698d-4072-4f48-a623-c74f3531b059"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate Total Earnings": {
                "kSLosVMpnQIuTnMST": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "7b9f9d22-c9ea-4407-a3d6-957619421a15"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "Affiliate Total Earnings Average Rate": {
                "krHJoymusOrvcfVvs": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "cdc0cebb-2e59-43ee-bf95-44f16d8e361c"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            },
            "EPC": {
                "klIEElXZRiwtMfqXZ": {
                    "cols": [
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "range",
                                    "upper_bound": null,
                                    "lower_bound": null
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Day"
                        },
                        {
                            "prepared_id": "978db2eb-7437-4087-98c0-4b937cbe0d9a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "totals": false,
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 500,
                    "format": "json"
                }
            }
        }
    },
    "top_affiliates_widget": {
        "Sales": {
            "Average Order Amount": {
                "k2zgUvBpLARmtaOMo": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "c045f0b3-2e56-428b-a552-d256b22855a7"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "avg_order_amount",
                            "direction": "desc",
                            "alias": "avg_order_amount"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Sales": {
                "kxpeDJPdggGsOv4bM": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "5aab673b-e77d-4744-a743-25a3f0d079db"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "net_sales",
                            "direction": "desc",
                            "alias": "net_sales"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "ROAS %": {
                "kfYQE1rgAzqMIL6IN": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "e8cdff6c-5aec-4ea8-b078-907524040784"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "return_on_ad_spend_percent",
                            "direction": "desc",
                            "alias": "return_on_ad_spend_percent"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "ROAS": {
                "k0wwvLGkmdqBZaVtL": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "ebf77986-b88e-4521-9345-1500ff68cce7"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "return_on_ad_spend",
                            "direction": "desc",
                            "alias": "return_on_ad_spend"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Orders": {
                "ky5H5dkfzP8ds1lv5": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "5a1b9d70-1db3-4670-bb4e-6710dc6e736a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "number_of_orders",
                            "direction": "desc",
                            "alias": "number_of_orders"
                        }, {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Gross Sales": {
                "kt1F7iYtWJFGB9rTF": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "29c95852-5c17-4899-b4c9-3465fc943ec2"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "gross_sales",
                            "direction": "desc",
                            "alias": "gross_sales"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Conversion Rate": {
                "kcyeMwWuGMpnfz3B6": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "ef559898-c0d1-41d0-ad0b-25ae17040c14"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "conversion_rate",
                            "direction": "desc",
                            "alias": "conversion_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            }
        },
        "Combined Commission": {
            "Total Cost": {
                "k2LqpeOshzQ4JYkRJ": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "2d6b94d6-4bbe-4fc6-bb91-25f1b69cc0f2"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "total_commission",
                            "direction": "desc",
                            "alias": "total_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Sale Commission": {
                "kVyCeEUSGr2hwVZ4V": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "67f503b5-29bc-4199-828f-66b02b2c4009"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "sale_commission",
                            "direction": "desc",
                            "alias": "sale_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Paid Placement": {
                "kb0XcWSxQAYQX8ZyK": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "dcd37006-96ab-4818-8c9e-abc1c2785969"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "combined_ppb",
                            "direction": "desc",
                            "alias": "combined_ppb"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Incentive Commission": {
                "kNLrXugPgD6mBUkk4": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "680cbb72-e7be-4ebd-8661-051bf7599027"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "incentive_commission",
                            "direction": "desc",
                            "alias": "incentive_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "CPC": {
                "k9SChwZjoBGdKcja9": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "27945e4c-710f-407c-a0b6-21b965c27136"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "combined_cpc",
                            "direction": "desc",
                            "alias": "combined_cpc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Bonus": {
                "kOa4UvCo0klyPdDJt": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "c1a67fab-8540-44e6-8e50-fa51388a3f26"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "combined_bonus",
                            "direction": "desc",
                            "alias": "combined_bonus"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            }
        },
        "Affiliate Commission": {
            "Affiliate Bonus": {
                "kPER4sXjR8vhyCEfZ": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "54f5cc7c-949c-4ef1-95e4-9af10c224862"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_bonus",
                            "direction": "desc",
                            "alias": "affiliate_bonus"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate CPC": {
                "kb2WYo65nL2u4ame0": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "c57ca314-145b-4131-bdaf-87beef851324"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_cpc",
                            "direction": "desc",
                            "alias": "affiliate_cpc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate Incentive Commission": {
                "kRAI5ENr5QgG9YlNA": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "370a8642-95d4-4977-a96a-615783a6c923"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_incentive_commission",
                            "direction": "desc",
                            "alias": "affiliate_incentive_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate Paid Placement": {
                "kYQfq1DfLbkBNcttp": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "ecaff0d4-5759-4c74-85e3-f3d37346bc19"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_ppb",
                            "direction": "desc",
                            "alias": "affiliate_ppb"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate Sale Commission": {
                "kvlxMwR57NDugQMYO": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "3afeb2e0-2335-45fb-a902-99c9715fa08a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_sale_commission",
                            "direction": "desc",
                            "alias": "affiliate_sale_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate Total Commission Average Rate": {
                "krSeMO0UYyworoGpo": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "2bef698d-4072-4f48-a623-c74f3531b059"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_total_commission_average_rate",
                            "direction": "desc",
                            "alias": "affiliate_total_commission_average_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate Total Earnings": {
                "kwOlhQ2qXYTIYc4cy": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "7b9f9d22-c9ea-4407-a3d6-957619421a15"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_total_earnings",
                            "direction": "desc",
                            "alias": "affiliate_total_earnings"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Affiliate Total Earnings Average Rate": {
                "kQHH6yTJI0K2IKt4S": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "cdc0cebb-2e59-43ee-bf95-44f16d8e361c"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_total_earnings_average_rate",
                            "direction": "desc",
                            "alias": "affiliate_total_earnings_average_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "EPC": {
                "kbNA0X39IGTxAlJVe": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "978db2eb-7437-4087-98c0-4b937cbe0d9a"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "earnings_per_click",
                            "direction": "desc",
                            "alias": "earnings_per_click"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            }
        },
        "Network Commission": {
            "Network CPC": {
                "krne3PeV3TjCDBYBt": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "d4e60199-a71b-4431-aa44-3f86217bd5d3"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_cpc",
                            "direction": "desc",
                            "alias": "network_cpc"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Network Paid Placement": {
                "kaLP78wN9utUVi6Dw": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "7de2e941-13a9-4e7e-9397-6008cc4160b3"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_ppb",
                            "direction": "desc",
                            "alias": "network_ppb"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Network Bonus": {
                "kT1DSaNy1nssqiZeJ": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "e5c4e787-63e6-4a34-bb4d-676198d61b78"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_bonus",
                            "direction": "desc",
                            "alias": "network_bonus"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Network Sale Commission": {
                "kMz3XGWyQYyu7bij4": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "36de7153-a578-4878-9657-31113bad1a14"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_sale_commission",
                            "direction": "desc",
                            "alias": "network_sale_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Network Total Commission Average Rate": {
                "k1cYoE1X669cE0i6T": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "fbf8a786-fd4c-4e4e-aafb-6aa2f66bae7b"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_total_commission_average_rate",
                            "direction": "desc",
                            "alias": "network_total_commission_average_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Network Total Earnings": {
                "kdqBswTQycsjKU63b": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "32a9cf02-0375-494f-b196-ef976d283aed"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_total_commission",
                            "direction": "desc",
                            "alias": "network_total_commission"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Network Total Earnings Average Rate": {
                "kkBj1B39SnRQdoOLO": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "b3dbfb92-c7e7-4ef8-9e5c-865cf54f8c2e"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "network_total_earnings_average_rate",
                            "direction": "desc",
                            "alias": "network_total_earnings_average_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            }
        },
        "Clicks % Impressions": {
            "Click Through Rate": {
                "kmBR08lcJKq9gqOei": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "6323f6bb-1843-4ac3-a358-1b3ab6111a46"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "click_through_rate",
                            "direction": "desc",
                            "alias": "click_through_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Clicks": {
                "kQmt96FD6Qnkqruhp": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "d6e33659-669e-432b-8727-7c4f871011cb"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "affiliate_clicks",
                            "direction": "desc",
                            "alias": "affiliate_clicks"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Impressions": {
                "k1HA64ODQMdfgjpp9": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "f8017c89-c326-48a9-a3cd-7362ab43eb95"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "number_of_impressions",
                            "direction": "desc",
                            "alias": "number_of_impressions"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            }
        },
        "Adjustments": {
            "Adjusted Affiliate Earnings": {
                "kzA4aWAWqkChlDEaS": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "77872d95-6d07-4061-9f27-44f7b77d0500"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "adjusted_affiliate_earnings",
                            "direction": "desc",
                            "alias": "adjusted_affiliate_earnings"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Adjusted Cost": {
                "kwAHoaYSRp1cuO4pa": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "28421ce9-5f78-4992-8229-98f01a06d601"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "adjusted_cost",
                            "direction": "desc",
                            "alias": "adjusted_cost"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Adjusted Network Earnings": {
                "kkZ97YJ28KGluP0Ue": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "443af97f-53cd-491a-becb-de7954c3bf09"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "adjusted_network_earnings",
                            "direction": "desc",
                            "alias": "adjusted_network_earnings"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Adjusted Sales": {
                "kavbt0HSGNvyh0Zwb": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "4939ce2e-6579-4de3-a507-8aafed7f0df6"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "event_action_amount",
                            "direction": "desc",
                            "alias": "event_action_amount"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Adjustments": {
                "knnbugxL1Wphsqh6i": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "098b750a-d718-4e44-8773-0f5e2e0d08fa"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "adjustments_count",
                            "direction": "desc",
                            "alias": "adjustments_count"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            },
            "Reversal Rate": {
                "ksCtmPwxkTG9001mV": {
                    "cols": [
                        {
                            "id": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "alias": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "aggregate": [

                            ],
                            "name": "Affiliate Website Url Stripped"
                        },
                        {
                            "id": "dim_affiliate-affiliate_uuid",
                            "alias": "dim_affiliate-affiliate_uuid",
                            "aggregate": [

                            ],
                            "name": "Affiliate Uuid",
                            "hidden": true
                        },
                        {
                            "id": "dim_date-mm_dd_yyyy",
                            "alias": "dim_date-mm_dd_yyyy",
                            "aggregate": [
                                {
                                    "func": "band",
                                    "bands": null,
                                    "dim": "dim_date-last_thirty_days"
                                },
                                {
                                    "func": "all"
                                }
                            ],
                            "name": "Date Range"
                        },
                        {
                            "prepared_id": "2e6cd77b-d40d-47d9-a3c0-637d6cc904bc"
                        }
                    ],
                    "filters": [
                        {
                            "op": "relative_date",
                            "field": "dim_date-mm_dd_yyyy",
                            "period": "day",
                            "start": -1,
                            "count": 30,
                            "allow_empty": true,
                            "to_date": false
                        },
                        {
                            "field": "dim_merchant-merchant_uuid",
                            "op": "eq",
                            "values": [
                                "e295c418-295a-447c-b265-734e25f82503"
                            ]
                        }
                    ],
                    "sort": [
                        {
                            "field": "reversal_rate",
                            "direction": "desc",
                            "alias": "reversal_rate"
                        },
                        {
                            "field": "dim_affiliate_default_website-affiliate_website_url_stripped",
                            "direction": "asc"
                        }
                    ],
                    "offset": 0,
                    "currency": "NATIVE",
                    "limit": 10,
                    "format": "json"
                }
            }
        }
    }
}

dashboard_objects = {
    "edw2_dashboard_objects": edw2_dashboard_objects,
    "edw3_dashboard_objects": edw3_dashboard_objects
}
