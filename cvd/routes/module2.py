"""

"""
from ..cvd import bp 
from flask import render_template, jsonify, request, Response

# For knowledge graph query
import os
import sys
import time
from pathlib import Path
from rdflib import Graph

@bp.route("/help")
def help():
    return render_template("help.html")

    
# Fetch graph data from Neo4j
def fetch_graph_data():
    # Resolve the path relative to the current script
    base_path = Path(__file__).resolve().parent.parent / "data"
    files = ["cvd_knowledge_graph.ttl"]
    g = Graph()
    for file in files:
        ttl_path = base_path / file
        if ttl_path.exists():
            print(f"Loading: {ttl_path}")
            g.parse(str(ttl_path), format="turtle")
        else:
            print(f"File not found: {ttl_path}")
            
    return g

@bp.route("/graph-data")
def graph_data():
    g = fetch_graph_data()
    # Serialize to JSON-LD string
    json_ld_data = g.serialize(format="json-ld", indent=4)
    print("data", Response(json_ld_data, mimetype='application/ld+json'))
    # Serialize the data
    return Response(json_ld_data, mimetype='application/ld+json')    # jsonify(data)


