from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies@csv",
                outputs="preprocessed_companies.02_intermediate@parquet",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles.02_intermediate@parquet",
                name="preprocess_shuttles_node",
            ),
            node(
                func=create_model_input_table,
                inputs=[
                    "preprocessed_shuttles.02_intermediate@parquet",
                    "preprocessed_companies.02_intermediate@parquet",
                    "reviews@csv"],
                outputs="model_input_table.03_primary@parquet",
                name="create_model_input_table_node",
            ),
        ]
    )
