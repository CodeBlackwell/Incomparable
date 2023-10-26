# aggregates
count = "count"
sum = "sum"

# filters
hit = "HIT"
order = "ORDER"
cpc = "CPC"
ppb = "PPB"
bonus = "BONUS"
none = None
impression = "IMPRESSION"
adjustment = "ADJUSTMENT"
commission = "COMMISSION"

# @TODO: leave in option to override Aggregate option

columns_map = {
    "affiliate_type_order-order_amount": {"table_id": "fact_event_active_conversion-total_event_amount",
                                          "filter": order,
                                          "aggregate": sum},

    "affiliate_type_order-order_id": {"table_id": "fact_event_active_conversion-order_number",
                                      "filter": order,
                                      "aggregate": count},

    "fact_affiliate_type_order_summary-checkout_influencer_count": {
        "table_id": "fact_event_active_conversion-checkoutinfluencer_count",
        "filter": order,
        "aggregate": sum},

    "fact_affiliate_type_order_summary-influencer_count": {"table_id": "fact_event_active_conversion-influencer_count",
                                                           "filter": order,
                                                           "aggregate": sum},

    "fact_affiliate_type_order_summary-introducer_count": {"table_id": "fact_event_active_conversion-introducer_count",
                                                           "filter": order,
                                                           "aggregate": sum},

    "fact_cpc_earning-affiliate_earnings": {"table_id": "fact_calculation-calculation_action_amount",
                                            "filter": cpc,
                                            "aggregate": sum},

    "fact_cpc_earning-network_earnings": {"table_id": "fact_calculation-calculation_network_amount",
                                          "filter": cpc,
                                          "aggregate": sum},

    "fact_event_hit-event_id": {"table_id": "fact_event_hit-event-id",
                                "filter": hit,
                                "aggregate": count
                                },

    "fact_hit-summary_hit_count": {"table_id": "fact_event_hit-event_id",
                                   "filter": hit,
                                   "aggregate": count},

    "fact_impression-summary_impression_count": {"table_id": "fact_event_passive_conversion-event_id",
                                                 "filter": impression,
                                                 "aggregate": count},

    "fact_order_adjustment-adjustment_amount": {"table_id": "fact_calculation-calculation_action_amount",
                                                "filter": adjustment,
                                                "aggregate": sum},

    "fact_order_adjustment-adjustment_hash_key": {"table_id": "fact_calculation-calculation_uuid",
                                                  "filter": adjustment,
                                                  "aggregate": count},

    "fact_order_adjustment-order_combined_adjustment_amount": {"table_id": "fact_calculation-calculation_action_amount",
                                                               "filter": order,
                                                               "aggregate": sum},

    "fact_order_avantlink-order_amount": {"table_id": "fact_event_active_conversion-total_event_amount",
                                          "filter": order,
                                          "aggregate": sum},

    "fact_order_avantlink-order_hash_key": {"table_id": "fact_event_active_conversion-event_id",
                                            "filter": order,
                                            "aggregate": count},

    "fact_order_bonus-bonus_commission_amount": {"table_id": "fact_calculation-calculation_action_amount",
                                                 "filter": bonus,
                                                 "aggregate": sum},

    "fact_order_bonus-bonus_network_commission_amount": {"table_id": "fact_calculation-calculation_network_amount",
                                                         "filter": bonus,
                                                         "aggregate": sum},

    "fact_order_channel_summary-order_count": {"table_id": "fact_event_active_conversion-order_number",
                                               "filter": order,
                                               "aggregate": count},

    "fact_order_commission-incentive_commission_amount": {"table_id": "fact_calculation-calculation_action_amount",
                                                          "filter": bonus,
                                                          "aggregate": sum},

    "fact_order_commission-network_commission_amount": {"table_id": "fact_calculation-calculation_network_amount",
                                                        "filter": commission,
                                                        "aggregate": sum
                                                        },
    "fact_order_commission-sale_commission_amount": {"table_id": "fact_calculation-calculation_attribution_amount",
                                                     "filter": commission,
                                                     "aggregate": sum
                                                     },

    "fact_order_commission_adjustment-network_commission_adjustment_amount": {
        "table_id": "fact_calculation-calculation_network_amount",
        "filter": adjustment,
        "aggregate": sum},

    "fact_order_commission_adjustment-order_commission_adjustment_amount": {
        "table_id": "fact_calculation-calculation_attribution_amount",
        "filter": adjustment,
        "aggregate": sum},

    "fact_ppb_earning-bid_amount": {"table_id": "fact_calculation-calculation_action_amount",
                                    "filter": ppb,
                                    "aggregate": sum},

    "fact_ppb_earning-network_commission": {"table_id": "fact_calculation-calculation_network_amount",
                                            "filter": ppb,
                                            "aggregate": sum},

    "fact_sales_projections-actual_network_earnings": {"table_id": "fact_calculation-calculation_network_amount",
                                                       # @TODO: Ask Dinesh about no filter
                                                       "filter": none,
                                                       "aggregate": sum},

    "fact_sales_projections-actual_sales": {"table_id": "fact_event_active_conversion-total_event_amount",
                                            "filter": order,
                                            "aggregate": sum},

    "fact_sales_projections-projected_network_earnings_hourly": {
        "table_id": "fact_calculation-calculation_network_amount_time_adjusted",
        # @TODO: Ask Dinesh about no filter
        "filter": none,
        "aggregate": sum},

    "fact_sales_projections-projected_sales_hourly": {
        "table_id": "fact_event_active_conversion-total_event_amount_time_adjusted",
        "filter": order,
        "aggregate": sum}

}
