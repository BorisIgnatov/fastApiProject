class BookSerializer:

    def __init__(self, query_result: dict):
        self.query_result = query_result

    def to_representation(self, many=False):
        response = {}
        response['id'] = self.query_result.get('id')
        response['name'] = self.query_result.get('name')
        response['rating'] = self.query_result.get('rating')
        response['author'] = {}
        response['author']['id'] = self.query_result.get('author_id')
        response['author']['name'] = self.query_result.get('author_name')
        return response


