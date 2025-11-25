"""create_geospatial_tables

Revision ID: 087aa5406af6
Revises: 8851c721ea43
Create Date: 2025-11-24 13:37:55.235680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision: str = '087aa5406af6'
down_revision: Union[str, Sequence[str], None] = '8851c721ea43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Note: PostGIS extension must be installed separately if needed for geometry columns
    # For now, creating tables - PostGIS can be enabled manually: CREATE EXTENSION postgis;

    # Create locations table
    # Note: geom column requires PostGIS - creating without it for now
    # To add PostGIS later: CREATE EXTENSION postgis; then ALTER TABLE locations ADD COLUMN geom geometry(POINT,4326);
    op.create_table(
        'locations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('location_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('building_name', sa.String(), nullable=False),
        sa.Column('floor', sa.String(), nullable=True),
        sa.Column('type', sa.Enum('Classroom', 'Office', 'Restroom', 'Cafeteria', 'Event',
                  'Service', 'Other', name='locationtype', create_type=False), nullable=False),
        # Geometry column commented out - requires PostGIS
        # sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_locations_id'), 'locations', ['id'], unique=False)
    op.create_index(op.f('ix_locations_location_id'),
                    'locations', ['location_id'], unique=True)
    op.create_index(op.f('ix_locations_name'),
                    'locations', ['name'], unique=False)
    op.create_index(op.f('ix_locations_building_name'),
                    'locations', ['building_name'], unique=False)

    # Create buildings table (without geometry for now - requires PostGIS)
    op.create_table(
        'buildings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('building_id', sa.String(), nullable=False),
        sa.Column('building_name', sa.String(), nullable=False),
        sa.Column('floor_plans_ref', sa.String(), nullable=True),
        # Geometry column commented out - requires PostGIS
        # sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_buildings_building_id'),
                    'buildings', ['building_id'], unique=True)
    op.create_index(op.f('ix_buildings_building_name'),
                    'buildings', ['building_name'], unique=False)

    # Create routes table (without geometry for now - requires PostGIS)
    op.create_table(
        'routes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('route_id', sa.String(), nullable=False),
        sa.Column('start_location_id', sa.Integer(), nullable=False),
        sa.Column('end_location_id', sa.Integer(), nullable=False),
        # Geometry column commented out - requires PostGIS
        # sa.Column('path_geom', geoalchemy2.types.Geometry(geometry_type='LINESTRING', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
        sa.Column('is_accessible', sa.Boolean(), nullable=False),
        sa.Column('weight_distance_m', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['start_location_id'], ['locations.id'], ),
        sa.ForeignKeyConstraint(['end_location_id'], ['locations.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_routes_route_id'),
                    'routes', ['route_id'], unique=True)

    # Create events table
    op.create_table(
        'events',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('event_id', sa.String(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('location_id', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.DateTime(), nullable=False),
        sa.Column('end_time', sa.DateTime(), nullable=False),
        sa.Column('organizer_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
        sa.ForeignKeyConstraint(['organizer_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_event_id'),
                    'events', ['event_id'], unique=True)

    # Create emergency_alerts table
    op.create_table(
        'emergency_alerts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('alert_id', sa.String(), nullable=False),
        sa.Column('type', sa.Enum('Security', 'Medical', 'Weather', 'Fire',
                  'Other', name='alerttype', create_type=False), nullable=False),
        sa.Column('location_id', sa.Integer(), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.Column('safe_zone_name', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_emergency_alerts_alert_id'),
                    'emergency_alerts', ['alert_id'], unique=True)

    # Create safety_shares table
    op.create_table(
        'safety_shares',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('route_id', sa.Integer(), nullable=True),
        sa.Column('contact_info', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('start_time', sa.DateTime(), nullable=False),
        sa.Column('share_token', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['route_id'], ['routes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_safety_shares_share_token'),
                    'safety_shares', ['share_token'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_safety_shares_share_token'),
                  table_name='safety_shares')
    op.drop_table('safety_shares')
    op.drop_index(op.f('ix_emergency_alerts_alert_id'),
                  table_name='emergency_alerts')
    op.drop_table('emergency_alerts')
    op.drop_index(op.f('ix_events_event_id'), table_name='events')
    op.drop_table('events')
    op.drop_index(op.f('ix_routes_route_id'), table_name='routes')
    op.drop_table('routes')
    op.drop_index(op.f('ix_buildings_building_name'), table_name='buildings')
    op.drop_index(op.f('ix_buildings_building_id'), table_name='buildings')
    op.drop_table('buildings')
    op.drop_index(op.f('ix_locations_building_name'), table_name='locations')
    op.drop_index(op.f('ix_locations_name'), table_name='locations')
    op.drop_index(op.f('ix_locations_location_id'), table_name='locations')
    op.drop_index(op.f('ix_locations_id'), table_name='locations')
    op.drop_table('locations')

    # Drop enums
    op.execute("DROP TYPE IF EXISTS locationtype")
    op.execute("DROP TYPE IF EXISTS alerttype")
