def test_index(api):
    res = api.get('/')
    assert res.status == '200 OK'
    assert b'URL Shortener' in res.data
