# OMP Honk Marketplace

This repository serves as a custom marketplace for Open Model Platform (OMP) plugins. It allows you to discover, install, and manage OMP plugins in a centralized location.

## Overview

The OMP Honk Marketplace is a Git-based registry that follows the Claude Code plugin registry format. It enables you to:
- Publish your own OMP plugins
- Discover and install community plugins
- Manage plugin versions and dependencies
- Maintain a private or public collection of plugins

## Getting Started

### Adding This Marketplace to OMP

To use this marketplace in OMP:

```bash
# Add the marketplace
omp plugin marketplace add https://github.com/hhollenstain/omp-honk-marketplace.git

# Discover available plugins
omp plugin discover omp-honk-marketplace

# Install a plugin (example)
omp plugin install omp-grill-me-skill@omp-honk-marketplace
```

## Publishing Plugins to This Marketplace

### Prerequisites
- A Git repository for your plugin
- Proper plugin metadata in `plugin.json` or `package.json`
- Plugin published to a Git host (GitHub, GitLab, etc.)

### Steps to Publish

1. **Create Plugin Repository**
   - Create a new Git repository for your plugin
   - Include the plugin files with proper metadata
   - Ensure the plugin follows OMP plugin standards

2. **Add Plugin to Marketplace Catalog**
   - Edit `.omp-plugin/marketplace.json` in this repository
   - Add an entry for your plugin:
   
```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Plugin description",
  "source": {
    "source": "github",
    "repo": "yourusername/plugin-repo",
    "ref": "main"
  },
  "author": {
    "name": "Your Name"
  }
}
```

3. **Commit and Push**
   ```bash
   git add .omp-plugin/marketplace.json
   git commit -m "Add plugin-name to marketplace"
   git push origin main
   ```

4. **Update Marketplace Catalog in OMP**
   ```bash
   omp plugin marketplace update omp-honk-marketplace
   ```

## Plugin Structure

Each plugin in this marketplace should follow the standard OMP plugin structure:
- `plugin.json` or `package.json` with metadata
- Plugin code and assets
- Documentation if needed

## Contributing

To contribute plugins to this marketplace:
1. Fork this repository
2. Add your plugin to the catalog
3. Submit a pull request
4. Your plugin will be reviewed and added to the marketplace

## License

This marketplace is licensed under the MIT License - see the LICENSE file for details.