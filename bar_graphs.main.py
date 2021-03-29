"""
This file creates multiple bar graphs from the race datasets
of different decades and different neighborhoods in Seattle.
The race datasets will be cleaned and passed to methods to be plot
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib  # for patches
import seaborn as sns
import clean_data
sns.set()


def main():

    race_file_path = ACS_and_LTDB_Race_Data_by_Community_Reporting_Area.shp
    filter_neighbors = clean_data.neighbors(race_file_path)
    plot_bar_on_race00(filter_neighbors)  # race pop. changes 1990 to 2000
    plot_bar_on_race10(filter_neighbors)  # race pop. changes 2000 to 2010


def plot_bar_on_race00(filter_neighbors):
    """
    plot_line_on_race00 function plots population changes of
    African American, Asian, and Hispanic populations in Seattle
    neighborhoods from 1990 to 2000
    """
    fig, ax = plt.subplots(1)
    sns.barplot(data=filter_neighbors, x='GEN_ALIAS',
                y='NHBLK90t_1', color='#58508d')

    sns.barplot(data=filter_neighbors, x='GEN_ALIAS',
                y='ASIAN90t_1', color='#ff6361')
    sns.barplot(data=filter_neighbors, x='GEN_ALIAS',
                y='HISP90to_1', color='#ffa600')

    # create labels for each color bar
    name_to_color = {'African American': '#58508d',
                     'Asian': '#ff6361',
                     'Hispanic': '#ffa600'}
    patches = [matplotlib.patches.Patch(
        color=v, label=k) for k, v in name_to_color.items()]
    matplotlib.pyplot.legend(handles=patches)

    plt.xlabel('Neighborhoods in Seattle')
    plt.ylabel('Change In Population (%)')
    plt.title('Population Change in Seattle Neighborhoods 1990 To 2000')
    plt.xticks(rotation=45, horizontalalignment='right')
    fig.savefig('changes_neighborhoods_1990_to_2000.png')


def plot_bar_on_race10(filter_neighbors):
    """
    plot_line_on_race10 function plots population changes of
    African American, Asian, and Hispanic populations in Seattle
    neighborhoods from 2000 to 2010
    """
    fig, ax = plt.subplots(1)

    sns.barplot(data=filter_neighbors, x='GEN_ALIAS',
                y='NHBLK00t_1', color='#58508d')
    sns.barplot(data=filter_neighbors, x='GEN_ALIAS',
                y='ASIAN00t_1', color='#ff6361')
    sns.barplot(data=filter_neighbors, x='GEN_ALIAS',
                y='HISP00to_1', color='#ffa600')
    # create labels for each color bar
    name_to_color = {'African American': '#58508d',
                     'Asian': '#ff6361',
                     'Hispanic': '#ffa600'}
    patches = [matplotlib.patches.Patch(
        color=v, label=k) for k, v in name_to_color.items()]
    matplotlib.pyplot.legend(handles=patches)

    plt.xlabel('Neighborhoods in Seattle')
    plt.ylabel('Change In Population (%)')
    plt.title('Population Change in Seattle Neighborhoods 2000 To 2010')
    plt.xticks(rotation=45, horizontalalignment='right')
    fig.savefig('changes_neighborhoods_2000_to_2010.png')
