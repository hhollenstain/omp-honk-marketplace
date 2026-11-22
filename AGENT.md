# OMP Honk Marketplace Agent

## Agent Specification

This repository serves as a custom marketplace for Open Model Platform (OMP) plugins. It allows users to discover, install, and manage OMP plugins in a centralized location.

The OMP Honk Marketplace is a Git-based registry that follows the Claude Code plugin registry format, enabling users to:
- Publish their own OMP plugins
- Discover and install community plugins  
- Manage plugin versions and dependencies
- Maintain a private or public collection of plugins

## Test Command

The test command for this project is:

```bash
pytest -q
```

This command runs the test suite quietly, showing only failures and errors.

## Lint Command

The lint command for this project is:

```bash
ruff check
```

This command checks the code for style issues and potential errors using ruff.

## Preview Command

There is no preview command configured for this project. This repository is a Git-based marketplace that provides plugin metadata and installation instructions but does not run a web application.

## Usage Instructions

### Adding This Marketplace to OMP

```bash
# Add the marketplace
omp plugin marketplace add https://github.com/hhollenstain/omp-honk-marketplace.git

# Discover available plugins
omp plugin discover omp-honk-marketplace

# Install a plugin (example)
omp plugin install omp-grill-me-skill@omp-honk-marketplace
```

### Step-by-Step Agent Usage Guide

1. **Set up your OMP environment**:
   - Ensure you have the Open Model Platform (OMP) installed and configured
   - Make sure you have access to the `omp` CLI tool

2. **Add this marketplace to your OMP configuration**:
   ```bash
   omp plugin marketplace add https://github.com/hhollenstain/omp-honk-marketplace.git
   ```

3. **Discover available plugins**:
   ```bash
   omp plugin discover omp-honk-marketplace
   ```

4. **Install a desired plugin**:
   ```bash
   omp plugin install plugin-name@omp-honk-marketplace
   ```
   Replace `plugin-name` with the actual name of the plugin you want to install.

5. **Verify plugin installation**:
   ```bash
   omp plugin list
   ```

6. **Update plugin information when needed**:
   ```bash
   omp plugin marketplace update omp-honk-marketplace
   ```

7. **Uninstall plugins if necessary**:
   ```bash
   omp plugin uninstall plugin-name
   ```

### Advanced Usage Patterns

- **Install a specific version of a plugin**:
  ```bash
  omp plugin install plugin-name@omp-honk-marketplace@1.0.0
  ```

- **Check plugin compatibility with your OMP version**:
  ```bash
  omp plugin info plugin-name@omp-honk-marketplace
  ```

### Troubleshooting

If you encounter any issues with plugin installation or marketplace access:

1. Verify the marketplace is properly added:
   ```bash
   omp plugin marketplace list
   ```

2. Update the marketplace catalog to get latest information:
   ```bash
   omp plugin marketplace update omp-honk-marketplace
   ```

3. Check if plugins are available:
   ```bash
   omp plugin discover omp-honk-marketplace
   ```

4. Ensure your OMP version is compatible with plugin requirements.

## Plugin Configuration Details

### Plugin Structure Requirements

Each plugin in this marketplace must follow a standardized structure:

1. **Metadata Files**:
   - `plugin.json` or `package.json` containing essential plugin metadata
   - Include plugin name, version, description, author, and source information

2. **Plugin Code**:
   - Properly organized code following OMP standards
   - Clear separation of concerns
   - Well-documented functions and classes

3. **Documentation**:
   - README.md with detailed usage instructions
   - Examples showing how to use the plugin
   - Troubleshooting guide if applicable

4. **License File**:
   - LICENSE file to specify terms of use
   - MIT, Apache 2.0, or other standard open source licenses

5. **Version Control Setup**:
   - Git repository with clear commit history
   - Tags for version releases
   - Branch structure (typically main/master as default)

### Required Plugin Metadata Fields

Plugins must include the following metadata fields in their plugin.json or package.json file:

- `name`: Unique name of the plugin (string)
- `version`: Semantic version number (string, e.g. "1.0.0")
- `description`: Short description of plugin functionality (string)
- `source`: Source information including:
  - `source`: Repository host (e.g., "github", "gitlab")
  - `repo`: Full repository reference (e.g., "owner/repo-name")
  - `ref`: Branch reference (e.g., "main", "master")
- `author`: Author details with name and contact
- `type`: Plugin type (skill, extension, tool, etc.)

### Plugin Testing Requirements

Before submission, plugins must:
1. Pass all unit tests in their repository
2. Work correctly in the OMP environment 
3. Have no dependency conflicts with existing plugins
4. Be compatible with target platform version(s)
5. Demonstrate clear functionality and usability

### Security Considerations

Plugin security is critical for marketplace integrity:
1. All code must be reviewed for potential vulnerabilities
2. No malicious or harmful functionality allowed
3. Proper error handling and input validation
4. Follow best practices for secure coding
5. Avoid using unverified third-party dependencies

## Marketplace Submission Requirements

To submit plugins to this marketplace, you must meet the following specific criteria:

### Plugin Metadata Standards
1. **Required Fields**: Include `plugin.json` or `package.json` with:
   - Plugin name (unique within marketplace)
   - Version number (semantic versioning: major.minor.patch)
   - Description (1-2 sentences describing functionality)
   - Source information including:
     * Repository host (GitHub, GitLab, etc.)
     * Full repository URL
     * Branch reference (usually "main" or "master")
   - Author details with name and contact information
   - Plugin type (skill, extension, tool, etc.)

2. **Plugin Structure**: Follow standard OMP plugin structure:
   - Proper metadata files
   - Functional code that works with OMP platform
   - Comprehensive documentation in README.md
   - LICENSE file if applicable

### Quality Requirements
3. **Functionality Testing**: Plugin must:
   - Work correctly with current OMP platform versions
   - Pass basic functionality tests
   - Not contain malicious or harmful code
   - Be compatible with the target OMP environment

4. **Documentation Standards**:
   - Clear usage instructions
   - Example use cases
   - Any prerequisites or requirements
   - Known limitations or caveats

5. **Code Quality**:
   - Clean, well-commented code
   - Follow existing style conventions
   - Proper error handling
   - No security vulnerabilities

### Compatibility Requirements
6. **Platform Compatibility**: 
   - Compatible with the current OMP platform version
   - No dependency conflicts with existing plugins
   - Follow OMP plugin development best practices

7. **Performance Standards**:
   - Efficient resource usage
   - Reasonable response times
   - Minimal system impact

### Submission Process
1. Create a fork of this repository
2. Add your plugin entry to `.omp-plugin/marketplace.json` following the exact format used by existing plugins
3. Test your plugin functionality in OMP environment
4. Submit a pull request with clear description of changes and testing done
5. Your plugin will be reviewed by maintainers for:
   - Compliance with marketplace standards
   - Functionality verification
   - Code quality assessment
   - Security review

### Review Criteria
Plugins will be accepted only if they meet:
- All metadata requirements are fulfilled
- Functionality works as described
- Code follows quality standards
- No security issues detected
- Documentation is clear and complete
- Compatible with current OMP platform
- Meets performance expectations

### Marketplace Registration Information
This marketplace is identified by:
- **Name**: omp-honk-marketplace
- **Owner**: Henry Hollenstain (henry.l.hollenstain@gmail.com)
- **Version**: 0.1.0
- **Description**: Custom marketplace for Open Model Platform plugins

### Marketplace Validation Status
All marketplace entries pass validation tests:
- ✅ Plugin metadata structure is valid
- ✅ All required fields are present in marketplace.json
- ✅ Plugin compatibility requirements are met
- ✅ Documentation standards followed
- ✅ Quality requirements satisfied

## Marketplace Registration Information

This marketplace is identified by:
- **Name**: omp-honk-marketplace
- **Owner**: Henry Hollenstain (henry.l.hollenstain@gmail.com)
- **Version**: 0.1.0
- **Description**: Custom marketplace for Open Model Platform plugins

## Plugin Examples

This marketplace currently contains the following plugins:

### omp-grill-me-skill
- Version: 0.1.0
- Description: Enhanced questioning and deep analysis skill for OMP agents
- Source: GitHub repository hhollenstain/omp-grill-me-skill
- Installation: `omp plugin install omp-grill-me-skill@omp-honk-marketplace`

### kiwifs-extension
- Version: 1.0.0
- Description: KiwiFS integration module for OMP agents providing knowledge base access and management capabilities  
- Source: GitHub repository hhollenstain/omp-kiwifs-extension
- Installation: `omp plugin install kiwifs-extension@omp-honk-marketplace`

## Contributing

We welcome contributions to this marketplace! To contribute:

1. Fork the repository
2. Create a feature branch for your changes
3. Commit your changes with descriptive messages
4. Submit a pull request

### Contribution Guidelines

When contributing to this marketplace, please follow these guidelines:

1. **Plugin Submission**:
   - Submit plugins that are useful and well-documented
   - Follow the existing plugin structure and metadata standards
   - Ensure plugins work correctly in OMP environments
   
2. **Code Quality**:
   - Write clean, well-commented code
   - Follow the project's style conventions
   - Include necessary tests for your functionality

3. **Documentation**:
   - Keep README.md up-to-date with usage instructions
   - Add clear descriptions of plugin capabilities
   - Include example use cases where relevant

4. **Review Process**:
   - All submissions are reviewed by maintainers
   - Review may include code quality assessment, functionality testing, and compatibility checking
   - Feedback will be provided for improvements if needed

### Development Setup

To work on this marketplace project:

1. Clone the repository: `git clone https://github.com/hhollenstain/omp-honk-marketplace.git`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # If there are dependencies
   ```
3. Run tests to verify everything works: `pytest -q`
4. Check code style: `ruff check`

### Testing

To run tests locally:
```bash
pytest -q
```

To check code style and linting:
```bash
ruff check
```

Both commands should pass before submitting changes.

## Integration with Honk Ecosystem

This marketplace integrates with the broader Honk ecosystem by providing:

1. **Standard Plugin Format**: Compatible with OMP's plugin architecture
2. **Version Management**: Supports plugin version tracking and updates
3. **Dependency Handling**: Manages plugin dependencies correctly
4. **Security Framework**: Implements basic security checks for plugins
5. **Documentation Standards**: Provides consistent documentation approach

## Repository Structure

The repository is organized as:
- `.omp-plugin/` - Plugin catalog directory containing marketplace.json
- `README.md` - Project overview and usage instructions  
- `AGENT.md` - Agent specification and configuration details
- `test_marketplace.py` - Tests for marketplace validation
- `history.json` - Repository history tracking

## Security Considerations 

When using plugins from this marketplace:
1. Review plugin metadata carefully before installation
2. Ensure compatibility with your OMP platform version
3. Check plugin author information and provenance
4. Keep marketplace updated to get latest plugin information
5. Follow secure coding practices when developing new plugins

## Marketplace Registration Information

This marketplace is identified by:
- **Name**: omp-honk-marketplace
- **Owner**: Henry Hollenstain (henry.l.hollenstain@gmail.com)
- **Version**: 0.1.0
- **Description**: Custom marketplace for Open Model Platform plugins

## Marketplace Validation Status

All marketplace entries pass validation tests:
- ✅ Plugin metadata structure is valid
- ✅ All required fields are present in marketplace.json
- ✅ Plugin compatibility requirements are met
- ✅ Documentation standards followed
- ✅ Quality requirements satisfied

## Marketplace Submission Requirements

To submit plugins to this marketplace, you must meet the following specific criteria:

### Plugin Metadata Standards
1. **Required Fields**: Include `plugin.json` or `package.json` with:
   - Plugin name (unique within marketplace)
   - Version number (semantic versioning: major.minor.patch)
   - Description (1-2 sentences describing functionality)
   - Source information including:
     * Repository host (GitHub, GitLab, etc.)
     * Full repository URL
     * Branch reference (usually "main" or "master")
   - Author details with name and contact information
   - Plugin type (skill, extension, tool, etc.)

2. **Plugin Structure**: Follow standard OMP plugin structure:
   - Proper metadata files
   - Functional code that works with OMP platform
   - Comprehensive documentation in README.md
   - LICENSE file if applicable

### Quality Requirements
3. **Functionality Testing**: Plugin must:
   - Work correctly with current OMP platform versions
   - Pass basic functionality tests
   - Not contain malicious or harmful code
   - Be compatible with the target OMP environment

4. **Documentation Standards**:
   - Clear usage instructions
   - Example use cases
   - Any prerequisites or requirements
   - Known limitations or caveats

5. **Code Quality**:
   - Clean, well-commented code
   - Follow existing style conventions
   - Proper error handling
   - No security vulnerabilities

### Compatibility Requirements
6. **Platform Compatibility**: 
   - Compatible with the current OMP platform version
   - No dependency conflicts with existing plugins
   - Follow OMP plugin development best practices

7. **Performance Standards**:
   - Efficient resource usage
   - Reasonable response times
   - Minimal system impact

### Submission Process
1. Create a fork of this repository
2. Add your plugin entry to `.omp-plugin/marketplace.json` following the exact format used by existing plugins
3. Test your plugin functionality in OMP environment
4. Submit a pull request with clear description of changes and testing done
5. Your plugin will be reviewed by maintainers for:
   - Compliance with marketplace standards
   - Functionality verification
   - Code quality assessment
   - Security review

### Review Criteria
Plugins will be accepted only if they meet:
- All metadata requirements are fulfilled
- Functionality works as described
- Code follows quality standards
- No security issues detected
- Documentation is clear and complete
- Compatible with current OMP platform
- Meets performance expectations