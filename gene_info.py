import requests

def get_pubmed_articles(gene_symbol: str, max_results: int = 5):
    # 1. Szukaj artykułów w PubMed
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": f"{gene_symbol} aging",
        "retmode": "json",
        "retmax": max_results
    }

    search_response = requests.get(search_url, params=params)
    search_data = search_response.json()
    id_list = search_data.get("esearchresult", {}).get("idlist", [])

    if not id_list:
        return []

    # 2. Pobierz szczegóły artykułów
    summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    summary_params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "json"
    }

    summary_response = requests.get(summary_url, params=summary_params)
    summary_data = summary_response.json()

    articles = []
    for pmid in id_list:
        doc = summary_data.get("result", {}).get(pmid, {})
        title = doc.get("title", f"PubMed ID: {pmid}")
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        articles.append({
            "title": title,
            "url": url
        })

    return articles