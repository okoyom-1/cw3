from app import app


def test_all():
    response = app.test_client().get('/api/posts/')
    dict_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    print(response.json)
    assert response.status_code == 200
    assert type(response.json) == list
    for item in response.json:
        assert len(item.keys()) == len(set(item.keys()).union(dict_keys))


def test_one():
    response = app.test_client().get('/api/posts/1')
    dict_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    print(response.json)
    assert response.status_code == 200
    assert type(response.json) == dict
    assert len(response.json.keys()) == len(set(response.json.keys()).union(dict_keys))
