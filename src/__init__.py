"""
Property Valuation Analytics Source Package

This package contains the core modules for data ingestion and database operations.
"""

from .database import get_database_connection
from .ingestion import ingest_data

__all__ = [
    'get_database_connection',
    'ingest_data',
]

__version__ = '1.0.0'
