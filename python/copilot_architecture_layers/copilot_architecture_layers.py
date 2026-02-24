from pathlib import Path

# try importing plotly and give a clear, actionable error if it's missing
try:
    import plotly.graph_objects as go
except ImportError as exc:
    raise ImportError(
        "Missing dependency 'plotly'. Install the script dependencies:\n"
        "  python -m pip install -r requirements.txt\n"
        "or\n"
        "  python -m pip install 'plotly[kaleido]'"
    ) from exc

# Define output directory
OUTPUT_DIR = Path("/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/python/copilot_architecture_layers")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Define layers and descriptions
layers = [
    "User Interface Layer",
    "Integration Layer (Microsoft Graph, Connectors)",
    "Orchestration Layer (Grounding, Prompt Engineering)",
    "Foundation Models Layer (OpenAI GPT, Anthropic Claude, Prometheus)"
]

# Appearance settings
colors = ['#2E86AB', '#F6C85F', '#6A4C93', '#FF6B6B']
text_font_size = 14

# Create a layered architecture diagram using a horizontal bar chart
fig = go.Figure()
fig.add_trace(go.Bar(
    x=[1] * len(layers),
    y=layers,
    orientation='h',
    text=layers,
    textposition='inside',
    textfont=dict(size=text_font_size),
    marker=dict(color=colors),
    hoverinfo='text'
))

fig.update_layout(
    title=dict(text="Copilot Architecture Layers", x=0.5, xanchor='center', font=dict(size=20)),
    xaxis=dict(showticklabels=False, visible=False),
    yaxis=dict(showticklabels=True, automargin=True),
    height=700,
    width=1200,
    margin=dict(l=250, r=50, t=80, b=50),
    font=dict(size=text_font_size)
)

# Save diagram as JSON, high-resolution PNG and SVG
fig.write_json(str(OUTPUT_DIR / "copilot_architecture_layers.json"))
try:
    fig.write_image(str(OUTPUT_DIR / "copilot_architecture_layers.png"), scale=2)
    fig.write_image(str(OUTPUT_DIR / "copilot_architecture_layers.svg"))
    print(f"Diagram created in {OUTPUT_DIR}:")
    print("  - copilot_architecture_layers.json")
    print("  - copilot_architecture_layers.png")
    print("  - copilot_architecture_layers.svg")
except Exception as e:
    print("Diagram JSON created but image export failed:", e)
    print("If image export failed, ensure 'kaleido' is installed in the venv.")
