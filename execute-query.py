import os
import argparse
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j connection details
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

def execute_cypher_file(driver, file_path):
    """Reads a Cypher query file and executes its content."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            query = file.read()
            print(f"Executing: {file_path}")

            with driver.session() as session:
                result = session.run(query)
                for record in result:
                    print(record)

    except Exception as e:
        print(f"Error executing {file_path}: {e}")

def main():
    """Parses arguments and executes the given Cypher file."""
    parser = argparse.ArgumentParser(description="Execute a Cypher query file.")
    parser.add_argument("file", help="Path to the Cypher file to execute")
    args = parser.parse_args()

    file_path = args.file

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        with GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password)) as driver:
            execute_cypher_file(driver, file_path)

    except Exception as e:
        print("Failed to connect to Neo4j:", e)

if __name__ == "__main__":
    main()
