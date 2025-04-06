import plotly.express as px
import pandas as pd

def create_volcano_plot(df: pd.DataFrame) -> str:
    fig = px.scatter(
        df,
        x="logFC",
        y="-log10(adj.P.Val)",
        hover_name="EntrezGeneSymbol",
        custom_data=["EntrezGeneSymbol"],
        title="Volcano Plot: Protein Activity",
        template="plotly_white"
    )

    fig.update_traces(
        marker=dict(size=6),
        selector=dict(mode='markers')
    )

    fig.update_layout(
        clickmode='event+select'
    )

    volcano_html = fig.to_html(full_html=False)
    volcano_html += """
    <script>
    const plot = document.querySelectorAll(".plotly-graph-div")[0];
    plot.on('plotly_click', function(data) {
        const gene = data.points[0].customdata[0];
        window.location.href = "/gene/" + gene;
    });
    </script>
    """
    return volcano_html

import plotly.graph_objects as go

def create_boxplot(df: pd.DataFrame, gene: str) -> str:
   
    row = df[df["EntrezGeneSymbol"] == gene]
    if row.empty:
        return f"<p>Gene {gene} not found in expression data.</p>"

    
    donor_cols = [col for col in df.columns if "Set002" in col and (".OD" in col or ".YD" in col)]
    
    data = []
    for col in donor_cols:
        age_group = "Old" if ".OD" in col else "Young"
        value = float(row[col].iloc[0])
        data.append({"group": age_group, "value": value})
    
    box_df = pd.DataFrame(data)

    fig = go.Figure()
    fig.add_trace(go.Box(y=box_df[box_df["group"] == "Young"]["value"], name="Young", boxpoints="all", jitter=0.4))
    fig.add_trace(go.Box(y=box_df[box_df["group"] == "Old"]["value"], name="Old", boxpoints="all", jitter=0.4))
    fig.update_layout(title=f"Protein concentration of {gene}", template="plotly_white")
    
    return fig.to_html(full_html=False)