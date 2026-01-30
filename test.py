def convert_pricemap_to_graph_data(price_map, currencies = None | list, special_nodes=None | list):
        """Converts a Beancount PriceMap into a graph schema for visualization.

    This function extracts all currency pairs from the PriceMap to build a 
    network topology. It identifies every currency as a node and every 
    pricing relationship (base -> quote) as a connection.
    
    If there are currencies provided in the `currencies` argument, which are not
    present in the PriceMap, they will still be included as isolated nodes

    Args:
        price_map (dict): A Beancount PriceMap object (or similar dict) where 
            keys are tuples of strings: (base_currency, quote_currency).
            Values are ignored for the graph structure.
        
        currencies (list of str): A list of currency codes used in all entries.    
        
        special_nodes (list of str, optional): A list of currency codes 
            (e.g., ['USD', 'EUR']) that should be flagged as 'special' 
            in the output data. Defaults to None.

    Returns:
        dict: A dictionary conforming to the graph_data schema:
            {
                "USD": {"name": "USD", "connections": ["EUR"], "special": True},
                "EUR": {"name": "EUR", "connections": ["USD"], "special": False},
                ...
            }
    """
