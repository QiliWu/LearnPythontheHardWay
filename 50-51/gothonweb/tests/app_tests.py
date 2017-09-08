from nose.tools import *
from bin.post_form_laid_out import post_form_laid_out
from tests.tools import assert_response

def test_index():
    # Check that we get a 404 on the / URL
    resp = post_form_laid_out.request('/')
    assert_response(resp, status='404')

    # test our first GET request to /hello
    resp = post_form_laid_out.request("/hello")
    assert_response(resp)

    # make sure default values work for the form
    resp = post_form_laid_out.request("/hello", method = POST)
    assert_response(resp, contains="Nobody")

    #test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = post_form_laid_out.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")