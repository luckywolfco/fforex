import json
from typing import Dict, Callable, Any, Union

from .domain import ClientDocumentEvent
from .models import ClientDocumentRequestDataModel, ClientDocumentEventDataModel, \
    RelationshipManagerEmailIdentityDataModel, \
    ClientDocumentDataModel
from .unit_of_work import UnitOfWork
from django.utils.crypto import get_random_string


# return Maybe type
def get_client_email(client_id):
    return RelationshipManagerEmailIdentityDataModel.objects.get(client_id=client_id, is_primary=True)


def send_email_to_relationship_manager(event: ClientDocumentEvent):
    # tODO lookup email address + document
    print("Sending email to relationship manager " + event.payload)


def get_client_documents(relationship_manager_id, client_id):
    documents = ClientDocumentDataModel.objects.filter(relationship_manager_id=relationship_manager_id,
                                                       client_id=client_id)

    def function(x):
        return ClientDocumentDataModel.to_domain(x)

    if documents is not None:
        return list(map(function, documents))
    else:
        list()


def get_client_document(relationship_manager_id, client_document_id):
    try:
        document = ClientDocumentDataModel.objects.get(relationship_manager_id=relationship_manager_id,
                                                       client_document_id=client_document_id)

        return ClientDocumentDataModel.to_domain(document)

    except:
        return


def get_client_document(client_document_id):
    try:
        document = ClientDocumentDataModel.objects.get(client_document_id=client_document_id)

        return ClientDocumentDataModel.to_domain(document)

    except:
        return


def capture_document(
        encoded_client_document_request_id,
        storage_location
):
    uow = UnitOfWork()
    with uow:
        document_request = \
            ClientDocumentRequestDataModel.objects.get(
                encoded_client_document_request_id=encoded_client_document_request_id)

        captured = ClientDocumentDataModel.objects.create(
            client_document_request_id=document_request.client_document_request_id,
            relationship_manager_id=document_request.relationship_manager_id,
            client_id=document_request.client_id,
            description=document_request.description,
            storage_location=storage_location
        )

        document_request.request_status = 'uploaded'
        document_request.save()

        payload = json.dumps({'client_document_id': captured.client_document_id,
                              'storage_location': captured.storage_location})

        event = ClientDocumentEventDataModel.objects.create(
            payload=payload,
            event_type="client_document_captured"
        )

        handle_event(ClientDocumentEventDataModel.to_domain(event))

        uow.commit()
    return ClientDocumentDataModel.to_domain(captured)


def request(
        relationship_manager_id,
        client_id,
        description,
        accepted_document_formats,
        update_by
):
    uow = UnitOfWork()
    with uow:
        encoded_id = get_random_string(length=32)
        requested = ClientDocumentRequestDataModel.objects.create(
            relationship_manager_id=relationship_manager_id,
            encoded_client_document_request_id=encoded_id,
            client_id=client_id,
            description=description,
            accepted_document_formats=accepted_document_formats,
            update_by=update_by)

        payload = json.dumps({'client_document_request_id': requested.client_document_request_id,
                              'encoded_client_document_request_id': requested.encoded_client_document_request_id,
                              'client_id': client_id,
                              'relationship_manager_id': relationship_manager_id})

        ClientDocumentEventDataModel.objects.create(
            payload=payload,
            event_type="client_document_requested"
        )

        uow.commit()
        return ClientDocumentRequestDataModel.to_domain(requested)


def get_client_document_requests(relationship_manager_id):
    documents = ClientDocumentRequestDataModel.objects.filter(relationship_manager_id=relationship_manager_id)

    def function(x):
        return ClientDocumentRequestDataModel.to_domain(x)

    if documents is not None:
        return list(map(function, documents))
    else:
        list()


def handle_event(
        event: ClientDocumentEvent
):
    queue = [event]
    while queue:
        event = queue.pop(0)
        for k, v in HANDLERS.items():
            if k == event.event_type:
                v(event)


HANDLERS = {
    "client_document_captured": lambda e: send_email_to_relationship_manager(e),
}
