# -*- coding: utf-8 -*-
import pytest
import json

class TestBasket:
    def test_endpoint_exists(self, client):
        res = client.get("/basket")
        assert res.status_code == 200

    def test_nonexistent(self, client):
        res = client.get("/basket/1337")
        assert res.status_code == 404


    def test_create_and_read(self, client):
        payload = {
            'name': 'a test basket'
        }
        res_post = client.post('/basket', data=json.dumps(payload))
        assert res_post.status_code == 201
        newid = json.loads(res_post.data.decode('utf-8'))['id']
        assert newid == 1

        # read the thing we just created
        res_get = client.get('/basket/%i' % newid)
        assert res_get.status_code == 200

        # ensure 204 if we double-submit
        res_post2 = client.post('/basket', data=json.dumps(payload))
        assert res_post2.status_code == 204
        
        
class TestFoo:
    def test_endpoint_exists(self, client):
        res = client.get("/foo")
        assert res.status_code == 200

    def test_nonexistent(self, client):
        res = client.get("/foo/1337")
        assert res.status_code == 404

    def test_foo_and_basket(self, client):
        basket_payload = {
            'name': 'a test basket'
        }
        res_basket = client.post('/basket', data=json.dumps(basket_payload))
        basketid = json.loads(res_basket.data.decode('utf-8'))['id']

        foo_payload = {
            'bar': 42,
            'baz': 'some text',
            'basket_id': basketid
        }
        res_foo = client.post('/foo', data=json.dumps(foo_payload))
        assert res_foo.status_code == 201

        
    def test_foo_and_nonexistent_basket(self, client):
        foo_payload = {
            'bar': 42,
            'baz': 'some text',
            'basket_id': 99999
        }
        res_foo = client.post('/foo', data=json.dumps(foo_payload))
        # TODO 500 is wrong. Fix sandboy
        assert res_foo.status_code == 500

        


