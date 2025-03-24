import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j connection details
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

def test_neo4j_connection(uri, user, password):
    try:
        # Use a 'with' block to manage the driver lifecycle
        with GraphDatabase.driver(uri, auth=(user, password)) as driver:
            # Verify connectivity
            driver.verify_connectivity()

            # Execute queries using execute_query (simpler and more concise)
            records, _, _ = driver.execute_query("MATCH (n) RETURN count(n) AS node_count")
            node_count = records[0]["node_count"]
            print("Node Count:", node_count)

            records, _, _ = driver.execute_query("MATCH ()-[r]->() RETURN count(r) AS relationship_count")
            relationship_count = records[0]["relationship_count"]
            print("Relationship Count:", relationship_count)

    except Exception as e:
        print("Failed to connect to Neo4j:", e)

# Run the test function
test_neo4j_connection(neo4j_uri, neo4j_user, neo4j_password)