from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from dotenv import load_dotenv
import os

# from langchain_community.vectorstores import Pinecone as PineconeStore
# from langchain_community.vectorstores import Pinecone
    # from langchain.vectorstores import Pinecone
    # import pinecone
# from pinecone import Pinecone, ServerlessSpec  # AttributeError: init is no longer a top-level attribute of the pinecone package.


load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
index_name = os.environ.get('index_name')

extracted_data = load_pdf("./data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


# pinecone.init(api_key=PINECONE_API_KEY,
#             environment=PINECONE_API_ENV)
# docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)
