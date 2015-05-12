
from pysimplesoap.client import SoapClient
from mock import create_autospec, Mock
import unittest


class MockTest(unittest.TestCase):
    def test_create(self):
        real = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/',  # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=True,
            ns=False)
        real.Create = Mock(return_value='Document has not been created.')
        real.Create(doc_name='test', doc_content='<asd>No<asd>')
        real.Create.assert_called_with(doc_name='test', doc_content='<asd>No<asd>')

    def test_read(self):
        real = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/',  # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=True,
            ns=False)
        real.Read = Mock(return_value='Document has not been read.')
        real.Read(doc_name='test', doc_content='<asd>No<asd>')
        real.Read.assert_called_with(doc_name='test', doc_content='<asd>No<asd>')

    def test_update(self):
        real = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/',  # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=True,
            ns=False)
        real.Update = Mock(return_value='Document has not been updated.')
        real.Update(doc_name='test', doc_content='<asd>No<asd>')
        real.Update.assert_called_with(doc_name='test', doc_content='<asd>No<asd>')

    def test_delete(self):
        real = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/',  # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=True,
            ns=False)
        real.Delete = Mock(return_value='Document has not been deleted.')
        real.Delete(doc_name='test', doc_content='<asd>No<asd>')
        real.Delete.assert_called_with(doc_name='test', doc_content='<asd>No<asd>')



