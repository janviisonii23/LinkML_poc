import json
from neo4j import GraphDatabase
from typing import Any
from schema_python.model2 import  ResourceSource, slots  # Your generated Python schema
import uuid


# Get relationship name from slots defined in Python schema
def get_relationship_name(domain_cls: str, slot_name: str) -> str:
    for attr_name in dir(slots):
        if attr_name == slot_name:
            slot = getattr(slots, attr_name)
            if hasattr(slot, 'domain') and slot.domain.__name__ != domain_cls:
                continue  # domain mismatch
            if hasattr(slot, 'inverse') and slot.inverse:
                return slot.inverse.upper()
            elif hasattr(slot, 'name') and slot.name:
                return slot.name.upper()
    return f"HAS_{slot_name.upper()}"

def build_graph(obj: Any, graph, parent_node=None, rel_name=None):
    cls_name = obj.__class__.__name__
    print(f"Processing node: {cls_name}")

    props = {}
    for attr, value in obj.__dict__.items():
        if not attr.startswith('_') and not isinstance(value, (list, dict)) and not hasattr(value, '__dict__'):
            props[attr] = value

    props['label'] = cls_name
    props['uid'] = f"{cls_name}_{uuid.uuid4()}"
    node = graph.run("MERGE (n:`%s` {uid: $uid}) SET n += $props RETURN n" % cls_name, uid=props['uid'], props=props).single()[0]

    if parent_node and rel_name:
        rel_type = get_relationship_name(parent_node['label'], rel_name)
        graph.run("MATCH (a {uid: $from_uid}), (b {uid: $to_uid}) MERGE (a)-[r:`%s`]->(b)" % rel_type,
                  from_uid=parent_node['uid'], to_uid=props['uid'])

    for attr_name, value in obj.__dict__.items():
        if isinstance(value, list):
            for item in value:
                if hasattr(item, '__dict__'):
                    build_graph(item, graph, node, attr_name)
        elif hasattr(value, '__dict__'):
            build_graph(value, graph, node, attr_name)
            
print(f"__name__ is: {__name__}")

if __name__ == '__main__': # Replace with your actual top-level class
    URI = "neo4j+s://a38c58ba.databases.neo4j.io"
    USERNAME = "neo4j"
    PASSWORD = "TnAlTgGxuAsAV7UsD0FbRgoKKSmBuBSekNyGmvzJG5Y"

    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
    # driver = GraphDatabase.driver("bolt://localhost:7689", auth=("neo4j", "TnAlTgGxuAsAV7UsD0FbRgoKKSmBuBSekNyGmvzJG5Y"))
    print("jan")
    # Load JSON data
    with open("smalldata.json") as f:
        data = json.load(f)
    print("janvi")

    # Parse into Python object
    with driver.session() as session:
    # Wipe previous data (optional)
        session.run("MATCH (n) DETACH DELETE n")
        print("🌪️ Cleared old graph.")

    # Loop through each dictionary in the list
        for entry in data:
            try:
                obj = ResourceSource(**entry)
                print(f"Processing Resource CURIE: {obj.item.curie}")
                build_graph(obj, session)
            except Exception as e:
                print(f"❌ Error processing entry: {e}")

    driver.close()
