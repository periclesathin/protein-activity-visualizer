from flask import Flask, render_template
from data_loader import load_volcano_data, load_expression_values
from plots import create_volcano_plot, create_boxplot
from gene_info import get_pubmed_articles

app = Flask(__name__)

@app.route("/")
def index():
    df = load_volcano_data("data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx")
    volcano_html = create_volcano_plot(df)
    return render_template("index.html", plot_html=volcano_html)

@app.route("/gene/<symbol>")
def gene_view(symbol):
    df_expr = load_expression_values("data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx")
    boxplot_html = create_boxplot(df_expr, symbol)
    publications = get_pubmed_articles(symbol)
    return render_template("gene.html", gene=symbol, plot_html=boxplot_html, publications=publications)

if __name__ == "__main__":
    app.run(debug=True)