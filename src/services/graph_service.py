import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)

from text2graph.graph_builder import GraphBuilder


class GraphService:
    def __init__(self):
        self.builder = GraphBuilder(window_size=2, pmi_threshold=0.1)

    def build(self, text):
        data = self.builder.build_graph_from_text(text, directed=False)
        for k, v in data.items():
            print(k, v[:10])

        return data


_graph_service = GraphService()
