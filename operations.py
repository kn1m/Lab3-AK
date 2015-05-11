__author__ = 'm3sc4'

from dbxml import *
from bsddb3.db import *


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
        print 'Problems while creating new doc: ', inst
        return 'Document has not been added.'
    return 'Document has been added.'


def read(doc_name):
    try:
        mgr = XmlManager()
        cont = db_init(mgr)
        doc = cont.getDocument(str(doc_name))
        doc_content = doc.getContentAsString()
    except XmlException, inst:
        print 'Problems while reading doc: ', inst
        return 'Document has not been read.'
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
        print 'Problems while updating doc: ', inst
        return 'Document has not been updated.'
    return 'Document has been updated.'


def delete(doc_name):
    try:
        mgr = XmlManager()
        cont = db_init(mgr)
        # all Container modification operations need XmlUpdateContext
        uc = mgr.createUpdateContext()
        document = cont.getDocument(str(doc_name))
        cont.deleteDocument(document, uc)
    except XmlException, inst:
        print 'Problems while deleting doc: ', inst
        return 'Document has not been deleted.'
    return 'Document has been deleted.'