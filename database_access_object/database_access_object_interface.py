class DAOInterface:
    def start_session(self):
        pass
    
    def end_session(self):
        pass
    
    def add_document(self, file_name: str, file_path: str, paragraphs_embeddings: list, tokens: list) -> str:
        pass
    
    def delete_document(self, doc_id: str) -> bool:
        pass
    
    def get_tf_token(self, token: str, doc_id: str) -> int:
        pass
        
    def get_nq_token(self, token: str) -> int:
        pass
    
    def get_doc_list(self) -> list:
        pass
    
    def get_doc_attributes(self, doc_id: str) -> dict:
        pass