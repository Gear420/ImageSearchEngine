# from elasticsearch_dsl import *
# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import Completion
# from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
#
# # Define a default Elasticsearch client
# connections.create_connection(hosts=["localhost"])
#
# # class CustomAnalyzer(_CustomAnalyzer):
# #     def get_analysis_definition(self):
# #         return {}
#
# # ik_analyzer = CustomAnalyzer('ik_max_word',filter=['lowercase'])
#
#
#
# class Image(DocType):
#     # title_suggest = Completion(analyzer=ik_analyzer, search_analyzer=ik_analyzer)
#     title = String()
#     img_url = String()
#
#     class Meta:
#         index = "images"
#         doc_type = "image"
