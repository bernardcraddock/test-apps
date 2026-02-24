# Copilot Architecture Layers Visualization

## Overview

This script **generates visual diagrams** of the GitHub Copilot CLI architecture, showing how different components interact at various layers. It creates diagrams in multiple formats (JSON, PNG, SVG) for different use cases.

**What it teaches:**
- How to structure complex system architectures
- Using Python to programmatically generate visualizations
- Mermaid diagram syntax for architecture documentation
- Multi-format output for different platforms

## What It Does

The script generates a **layered architecture diagram** showing:

```
┌─────────────────────────────────────┐
│   User Interface Layer              │
│   (Terminal/CLI - copilot command)  │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│   API Layer                         │
│   (HTTP REST API handlers)          │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│   Service Layer                     │
│   (Business logic, MCP protocol)    │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│   Data Layer                        │
│   (Models, configurations)          │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│   GitHub API / External Services    │
│   (MCP servers, Claude API)         │
└─────────────────────────────────────┘
```

## How to Install and Run

### Prerequisites
- Python 3.14.2
- Located in: `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/python/`
- Shared virtual environment at: `../.venv/`

### Step 1: Activate Virtual Environment
```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps
source .venv/bin/activate
```

### Step 2: Run the Script
```bash
cd python
python copilot_architecture_layers.py
```

### Expected Output
```
Diagram created: copilot_architecture_layers.json, copilot_architecture_layers.png, copilot_architecture_layers.svg
```

### Step 3: View the Generated Files

**PNG (Quick view)**
```bash
open copilot_architecture_layers.png
```

**SVG (Scalable, in VS Code)**
```bash
# Open in VS Code or any browser
```

**JSON (Programmatic access)**
```bash
cat copilot_architecture_layers.json
```

## Technology & Libraries

| Library | Version | Purpose | Why Used |
|---------|---------|---------|----------|
| **plotly** | 6.5.2 | Create interactive diagrams | Rich visualization, multiple formats |
| **kaleido** | 1.2.0 | Export to PNG/SVG | Converts diagrams to static images |
| **json** | Built-in | Handle data structures | Standard for diagram data |

### Installation (Already Installed in `.venv`)
```bash
pip install plotly kaleido
```

## Code Structure

```python
def create_architecture_diagram():
    │
    ├── Define layers (5 tiers)
    ├── Define components per layer
    ├── Define connections/flows
    ├── Create Plotly figure
    │   ├── Add boxes for layers
    │   ├── Add boxes for components
    │   └── Add arrows for connections
    ├── Configure layout and styling
    └── Export to multiple formats

Exported Formats:
    ├── .json   → Raw data structure
    ├── .png    → Raster image (good for docs)
    └── .svg    → Vector image (scalable)
```

## Generated Diagram Explanation

### Layer 1: User Interface (CLI)
**What:** Terminal interface where users run `copilot` command
**Interaction:** Accepts user input, displays results

### Layer 2: API Layer
**What:** HTTP/REST endpoint handlers
**Interaction:** Routes requests to appropriate services

### Layer 3: Service Layer
**What:** Business logic, protocol handling
**Interaction:** Implements MCP protocol, command processing
**Key:** This is where I (Claude) interact via MCP

### Layer 4: Data Layer
**What:** Models, configurations, context
**Interaction:** Manages application state and settings

### Layer 5: External Services
**What:** GitHub API, Claude API, MCP servers
**Interaction:** External dependencies and integrations

## Architecture Diagram

```
GitHub Copilot CLI Architecture
═══════════════════════════════════════════════════════════════

                    ┌─────────────────────┐
                    │   User (Terminal)   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   CLI Interface     │
                    │  (copilot command)  │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
    ┌───▼───┐            ┌────▼─────┐          ┌────▼─────┐
    │ Explain│            │Suggest   │          │ Generate │
    │ Code   │            │Code      │          │Code      │
    └───┬───┘            └────┬─────┘          └────┬─────┘
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Service Layer      │
                    │  (MCP Protocol)     │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
    ┌───▼─────┐        ┌──────▼──────┐        ┌──────▼──────┐
    │GitHub   │        │Claude       │        │MCP          │
    │API      │        │API          │        │Servers      │
    └─────────┘        └─────────────┘        └─────────────┘
```

## Data Flow Example

When you run: `copilot explain`

```
1. User Input
   └─→ "copilot explain code.py"

2. CLI Interface
   └─→ Parse command, extract file content

3. Service Layer
   └─→ Prepare context using MCP protocol

4. Claude API Call
   └─→ Send code + prompt to Claude

5. Response Processing
   └─→ Format and display explanation to user

6. Output
   └─→ Terminal displays result
```

## Key Concepts

### Layered Architecture Benefits
✅ **Separation of Concerns** - Each layer has one responsibility
✅ **Testability** - Easy to test individual layers
✅ **Maintainability** - Changes isolated to specific layers
✅ **Scalability** - Can upgrade layers independently

### MCP Integration
The Service Layer implements the **Model Context Protocol**, which allows:
- 🔌 Connection to external MCP servers
- 📦 Standard message format across tools
- 🔀 Bidirectional communication with Claude

## Diagram Output Formats

### PNG Format
```
✅ Best for: Documentation, presentations, sharing
✅ Size: Smaller file (good for web)
❌ Not scalable (fixed resolution)
❌ Can't edit in drawing tools
```

### SVG Format
```
✅ Best for: Web integration, zooming, editing
✅ Scalable (looks good at any size)
✅ Can be edited with drawing tools
❌ Larger file size
```

### JSON Format
```
✅ Best for: Programmatic access, data analysis
✅ Can rebuild diagram from data
✅ Can integrate with other tools
❌ Not human-readable visually
```

## Files Generated

| File | Format | Size | Usage |
|------|--------|------|-------|
| `copilot_architecture_layers.png` | PNG | ~50KB | Quick view, presentations |
| `copilot_architecture_layers.svg` | SVG | ~30KB | Web, scalable, editing |
| `copilot_architecture_layers.json` | JSON | ~10KB | Data, integration |

## Customization Ideas

### Extend the Diagram
```python
# Add more layers (Security, Analytics, etc.)
# Add more components per layer
# Change colors and styling
# Add component descriptions
# Include data flow indicators
```

### Generate Different Diagrams
```python
# Deployment architecture
# Data flow diagram
# Component interaction diagram
# System boundaries diagram
```

## Learning Outcomes

After running this script, you'll understand:
- ✅ How to structure complex system architectures
- ✅ Layered architecture patterns
- ✅ How to use Plotly for programmatic diagrams
- ✅ Multi-format export capabilities
- ✅ How Copilot CLI components interact

## Comparison to Other Tools

| Tool | Format | Ease | Power |
|------|--------|------|-------|
| **Mermaid** | Plain text | ⭐⭐ | ⭐⭐⭐ |
| **Plotly** (This script) | Python | ⭐⭐⭐ | ⭐⭐⭐ |
| **Draw.io** | GUI | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Lucidchart** | SaaS | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| PNG not created | Check `kaleido` is installed: `pip install kaleido` |
| Missing images | Ensure script has write permissions to folder |
| Diagram looks wrong | Rerun script, it regenerates all files |

## Next Steps

1. **Modify the diagram** - Change colors, add components, reorganize layers
2. **Create variations** - Frontend architecture, database schema, etc.
3. **Automate diagrams** - Generate docs automatically from Python
4. **Add interactivity** - Use Plotly's interactive features

## Files

- `copilot_architecture_layers.py` - Main script (~500 lines)
- `copilot_architecture_layers.json` - Generated data structure
- `copilot_architecture_layers.png` - Generated raster image
- `copilot_architecture_layers.svg` - Generated vector image
- `copilot_architecture_layers.md` - This README

## References

- **Plotly Documentation**: https://plotly.com/python/
- **Kaleido**: https://github.com/plotly/kaleido
- **Architecture Patterns**: https://en.wikipedia.org/wiki/Layered_architecture
- **MCP Protocol**: https://modelcontextprotocol.io/

## Notes

- The diagram is **automatically regenerated** each time you run the script
- All output files are **overwritten** (don't worry about old versions)
- The JSON format lets you **rebuild the diagram programmatically**
- SVG can be **embedded in HTML** for web integration
