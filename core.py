
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
from operations import create, read, update, delete

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="http://example.com/sample.wsdl", prefix="ns0",
    trace=True,
    ns=True)

# register the user functions
dispatcher.register_function('Create', create,
    returns={'Node': str},
    args={'doc_name': str, 'doc_content': str})

dispatcher.register_function('Read', read,
    returns={'Node': str},
    args={'doc_name': str})

dispatcher.register_function('Update', update,
    returns={'Node': str},
    args={'doc_name': str, 'doc_content': str})

dispatcher.register_function('Delete', delete,
    returns={'Node': str},
    args={'doc_name': str})

print "Starting server at 8008..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
