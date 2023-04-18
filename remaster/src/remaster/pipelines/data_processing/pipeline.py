"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import filter_stations_close_to_oslo


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=filter_stations_close_to_oslo,
                inputs=["master_raw_dataset_2021", "params:geo_delimitation_options"],
                outputs="filtered_stations",
                name="filter_stations_close_to_oslo",
            )
        ]
    )
