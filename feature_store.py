
from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32


# -------------------------------------------------
# 1. ENTITY
# -------------------------------------------------

skill = Entity(
    name="skill",
    join_keys=["skill_id"],
    description="A technical or professional skill"
)


# -------------------------------------------------
# 2. DATA SOURCE
# -------------------------------------------------

skill_gap_source = FileSource(
    name="skill_gap_source",
    path="data/skill_features.parquet",
    timestamp_field="event_timestamp"
)


# -------------------------------------------------
# 3. FEATURE VIEW
# -------------------------------------------------

skill_features = FeatureView(
    name="skill_features",
    entities=[skill],
    ttl=timedelta(days=365),
    schema=[
        Field(
            name="curriculum_score",
            dtype=Float32
        ),
        Field(
            name="industry_demand",
            dtype=Float32
        ),
        Field(
            name="skill_gap",
            dtype=Float32
        ),
        Field(
            name="gap_percentage",
            dtype=Float32
        ),
    ],
    online=True,
    source=skill_gap_source
)
