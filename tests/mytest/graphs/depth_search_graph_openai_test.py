"""
depth_search_graph test
"""
import os
import pytest

from dotenv import load_dotenv
from pydantic import BaseModel

from scrapegraphai.graphs import DepthSearchGraph

class Data(BaseModel):
    title: str
    link: str
    image: list | str
    youtube_link: str
    content: str
    date: str

load_dotenv()

@pytest.fixture
def depth_search_graph():
    return DepthSearchGraph(
        prompt='ambilkan saya content dan titlenya dan paginasinya yang lengkap',
        source="https://www.tribunnews.com/mata-lokal-memilih/2024/11/28/pujian-rk-dan-pramono-kepada-dharma-pongrekun-usai-raih-10-persen-suara-versi-quick-count",
        config={
            "llm": {
                "api_key": os.getenv("API_KEY"),
                "base_url": os.getenv("BASE_URL"),
                "model": os.getenv("MODEL"),
            },
            "verbose": True,
            "headless": False,
            "depth": 2,
            "only_inside_links": False
        },
        # schema=Data
    )

def test_depth_search_graph(depth_search_graph: DepthSearchGraph):
    """
    Test the DepthSearchGraph scraping pipeline
    """

    result = depth_search_graph.run()
    print(result)
    # json.dump(result, open('test_depth_search_graph.json', 'w'))
    assert result is not None
