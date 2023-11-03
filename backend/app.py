import pathway as pw

from common.embedder import embeddings, index_embeddings
from common.prompt import prompt


def run(host, port):
    # Given a user question as a query from your API
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )
    print("1",query,response_writer)
    # Real-time data coming from external data sources such as jsonlines file
    sales_data = pw.io.jsonlines.read(
        "./data",
        schema=DataInputSchema,
        mode="streaming"
    )
    print("2",sales_data)

    # Compute embeddings for each document using the OpenAI Embeddings API
    embedded_data = embeddings(context=sales_data, data_to_embed=sales_data.doc)
    print("3",embedded_data)
    # Construct an index on the generated embeddings in real-time
    index = index_embeddings(embedded_data)
    print("4",index)
    # Generate embeddings for the query from the OpenAI Embeddings API
    embedded_query = embeddings(context=query, data_to_embed=pw.this.query)
    print("5",embedded_query)
    # Build prompt using indexed data
    responses = prompt(index, embedded_query, pw.this.query)
    print("6",responses)
    # Feed the prompt to ChatGPT and obtain the generated answer.
    response_writer(responses)
    print("7",response_writer)
    # Run the pipeline
    pw.run()


class DataInputSchema(pw.Schema):
    doc: str


class QueryInputSchema(pw.Schema):
    query: str
