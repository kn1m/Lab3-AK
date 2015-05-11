
from dbxml import *
from bsddb3.db import *
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer


def db_init(xml_manager):
    container_name = '3.dbxml'
    mgr = xml_manager
    if mgr.existsContainer(container_name) == 0:
        raise "No container with name '%s' found" % container_name
    cont = mgr.openContainer(container_name)
    return cont


def create(doc_name, doc_content):
    try:
        mgr = XmlManager()
        cont = db_init(mgr)
        # all Container modification operations need XmlUpdateContext
        uc = mgr.createUpdateContext()
        cont.putDocument(str(doc_name), str(doc_content), uc)
    except XmlException, inst:
        return inst
    return 'Document added.'


def read(doc_name):
    try:
        mgr = XmlManager()
        cont = db_init(mgr)
        doc = cont.getDocument(str(doc_name))
        doc_content = doc.getContentAsString()
    except XmlException, inst:
        return inst
    return doc_content


def update(doc_name, doc_content):
    try:
        mgr = XmlManager()
        cont = db_init(mgr)
        # all Container modification operations need XmlUpdateContext
        uc = mgr.createUpdateContext()
        document = cont.getDocument(str(doc_name))
        document.setContent(str(doc_content))
        cont.updateDocument(document, uc)
    except XmlException, inst:
        return inst
    return 'Document updated.'


def delete(doc_name):
    try:
        mgr = XmlManager()
        cont = db_init(mgr)
        # all Container modification operations need XmlUpdateContext
        uc = mgr.createUpdateContext()
        document = cont.getDocument(str(doc_name))
        cont.deleteDocument(document, uc)
    except XmlException, inst:
        return inst
    return 'Document deleted.'

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
