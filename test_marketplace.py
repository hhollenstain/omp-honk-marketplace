"""
Test suite for the OMP Honk Marketplace.

This file contains tests for the marketplace functionality.
"""

import json
import os

import pytest


def test_marketplace_json_exists():
    """Test that the marketplace.json file exists."""
    assert os.path.exists('.omp-plugin/marketplace.json')


def test_marketplace_json_valid():
    """Test that the marketplace.json is valid JSON and has expected structure."""
    assert os.path.exists('.omp-plugin/marketplace.json')
    
    with open('.omp-plugin/marketplace.json', 'r') as f:
        data = json.load(f)
    
    # Check required fields
    assert 'name' in data
    assert 'owner' in data
    assert 'metadata' in data
    assert 'plugins' in data
    
    # Check plugins array exists
    assert isinstance(data['plugins'], list)
    assert len(data['plugins']) > 0
    
    # Verify marketplace name is set correctly for honk marketplace submission
    assert data['name'] == 'omp-honk-marketplace'


def test_plugin_entries():
    """Test that plugin entries are correctly formatted."""
    with open('.omp-plugin/marketplace.json', 'r') as f:
        data = json.load(f)
    
    plugins = data['plugins']
    
    # Test each plugin entry
    for plugin in plugins:
        assert 'name' in plugin
        assert 'version' in plugin
        assert 'description' in plugin
        assert 'source' in plugin
        assert 'author' in plugin
        
        # Check source structure
        source = plugin['source']
        assert 'source' in source  # Should be "github"
        assert 'repo' in source
        assert 'ref' in source
        
        # Check author structure
        author = plugin['author']
        assert 'name' in author
        
        # Verify each plugin has compatibility information for marketplace submission
        assert 'compatibility' in plugin
        assert 'omp' in plugin['compatibility']
        assert 'platform' in plugin['compatibility']


def test_plugin_count():
    """Test that we have the expected number of plugins."""
    with open('.omp-plugin/marketplace.json', 'r') as f:
        data = json.load(f)
    
    plugins = data['plugins']
    
    # We expect 2 plugins based on current structure
    assert len(plugins) == 2


def test_plugin_names():
    """Test that plugin names are correct."""
    with open('.omp-plugin/marketplace.json', 'r') as f:
        data = json.load(f)
    
    plugins = data['plugins']
    plugin_names = [p['name'] for p in plugins]
    
    assert 'omp-grill-me-skill' in plugin_names
    assert 'kiwifs-extension' in plugin_names


def test_marketplace_metadata_comprehensive():
    """Test that marketplace metadata meets all submission requirements."""
    with open('.omp-plugin/marketplace.json', 'r') as f:
        data = json.load(f)
    
    # Check that metadata has all required fields for marketplace submission
    assert 'metadata' in data
    metadata = data['metadata']
    assert 'description' in metadata
    assert 'version' in metadata
    assert 'compatibility' in metadata
    
    # Verify compatibility information is present and properly formatted
    assert 'omp' in metadata['compatibility']
    assert 'platform' in metadata['compatibility']
    assert isinstance(metadata['compatibility']['omp'], str)
    assert isinstance(metadata['compatibility']['platform'], str)
    
    # Verify marketplace name matches expected format for honk marketplace submission
    assert data['name'] == 'omp-honk-marketplace'
    
    # Verify owner information is complete
    assert 'owner' in data
    owner = data['owner']
    assert 'name' in owner
    assert 'email' in owner
    
    # Verify specific honk system compatibility 
    assert metadata['compatibility']['omp'] == ">=0.1.0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])