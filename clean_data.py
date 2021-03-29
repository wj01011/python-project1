"""
This file filters the data to central and
south Seattle for better visual
"""


def neighbors(race_file):
    """
    Narrow down neighborhoods to central and south
    Seattle to examine the changes in race within these
    areas
    """
    r_data = gpd.read_file(race_file)
    filter_neighbors = ['Madrona/Leschi', 'South Beacon Hill/NewHolly',
                        'Beacon Hill', 'Pioneer Square/International District',
                        'North Beacon Hill/Jefferson Park', 'Capitol Hill',
                        'Central Area/Squire Park', 'Duwamish/SODO', 'Georgetown',
                        'North Delridge', 'North Capitol Hill', 'Columbia City',
                        'Rainier Beach']
    filter_series = r_data['GEN_ALIAS'].isin(filter_neighbors)
    df = r_data[filter_series]
    return df
