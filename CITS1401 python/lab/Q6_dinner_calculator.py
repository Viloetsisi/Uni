def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    return (meal_cost + drinks_cost * 0.7) * (1 + 0.15)