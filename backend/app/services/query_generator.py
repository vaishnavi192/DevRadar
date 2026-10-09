from app.models.product import Product
from app.models.search_hypothesis import SearchHypothesis


def generate_queries(
    product: Product,
) -> list[SearchHypothesis]:

    return [
        SearchHypothesis(
            key="implementation",
            product_name=product.name,
            query=f"{product.name} Python",
            intent="implementation",
            signal_type="developer_demand",
        ),
        SearchHypothesis(
            key="troubleshooting",
            product_name=product.name,
            query=f"{product.name} error problem",
            intent="troubleshooting",
            signal_type="developer_problem",
        ),
        SearchHypothesis(
            key="learning",
            product_name=product.name,
            query=f"{product.name} tutorial",
            intent="learning",
            signal_type="developer_education",
        ),
        SearchHypothesis(
            key="integration",
            product_name=product.name,
            query=f"{product.name} integration",
            intent="integration",
            signal_type="adoption_opportunity",
        ),
    ]