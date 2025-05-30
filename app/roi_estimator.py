
def estimate_roi(analysis):
    panel_cost = 200  # USD per panel
    installation_cost = 500  # Flat fee
    incentive = 1000  # Govt subsidy

    total_cost = analysis['recommended_panels'] * panel_cost + installation_cost
    net_cost = total_cost - incentive
    annual_savings = 180 * analysis['recommended_panels'] / 12  # USD saved per year
    payback_years = round(net_cost / annual_savings, 2)

    return {
        "total_cost_usd": total_cost,
        "incentive_usd": incentive,
        "net_cost_usd": net_cost,
        "estimated_annual_savings_usd": round(annual_savings, 2),
        "payback_period_years": payback_years
    }
