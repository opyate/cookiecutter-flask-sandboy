# -*- coding: utf-8 -*-
import pytest

class TestFoo:

    def test_foo_endpoint_exists(self, client):
        res = client.get("/foo")
        assert res.status_code == 200

    def test_nonexistent_foo(self, client):
        res = client.get("/foo/1337")
        assert res.status_code == 404
