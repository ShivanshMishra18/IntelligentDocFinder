from utils import *
from paragraphs_extractor.iterator_factory import IteratorFactory
from document_preprocessor.data_cleaners import *
from document_preprocessor.distributed_pipeline import *
from document_preprocessor.accumulator import DocPreprocessingAccumulator

def test_txt_file():
    iterator = IteratorFactory.get_iterator(generate_filename("txt"), "txt")
    doc_preprocessing_accumulator = DocPreprocessingAccumulator()
    preprocess_pipeline = DistributedPipeline(file_iterator = iterator,
                                              stage_functions = [
                                                  tokenize,
                                                  lemmatizer_and_lowertext,
                                                  remove_punctuation,
                                                  remove_stopwords,
                                                  stemm_text,
                                              ], 
                                              accumulator = doc_preprocessing_accumulator)
    
    preprocessed_data = preprocess_pipeline.run()
    print("DONE")    
    print(preprocessed_data)    
    print("DONE")
    
test_txt_file()