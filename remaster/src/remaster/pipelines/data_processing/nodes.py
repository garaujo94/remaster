"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.7
"""
from typing import Dict, List

import folium
import pandas as pd


def create_norway_map() -> folium.Map:
    """
    Create a norway map centered in Oslo
    """
    return folium.Map(location=[59.921914, 10.721945])


def add_markers_on_map(folium_map: folium.Map, coords: List):
    """
    Add stations as marker in folium map
    """
    for station in coords:
        folium.Marker(
            [station[0], station[1]], tooltip=f"{station[0]}, {station[1]}"
        ).add_to(folium_map)


def extract_coords_as_list(stations_df: pd.DataFrame) -> List:
    return stations_df[["lat", "long"]].values.tolist()


# def plot_original_map(master_raw_dataset_2021: pd.DataFrame):
#     map = create_norway_map()
#     coords = extract_coords_as_list(master_raw_dataset_2021)
#     add_markers_on_map(map, coords)

#     map.save("data/02_intermediate/original_map.html")


def filter_stations_close_to_oslo(
    master_raw_dataset_2021: pd.DataFrame, parameters: Dict
) -> pd.DataFrame:
    filtered_dataset = master_raw_dataset_2021.loc[
        (master_raw_dataset_2021["lat"] > parameters["min_lat"])
        & (master_raw_dataset_2021["long"] > parameters["min_long"])
        & (master_raw_dataset_2021["lat"] < parameters["max_lat"])
        & (master_raw_dataset_2021["long"] < parameters["max_long"])
    ]
    return filtered_dataset
