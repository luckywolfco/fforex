from __future__ import annotations

import json


class ClientDocumentRequest:
    def __init__(self, rm: int, client: int, request_id: str, status: str):
        self.relationship_manager_id = rm
        self.client_id = client
        self.document_request_id = request_id
        self.status = status

    def __repr__(self):
        return "<Document request {self.document_request_id}>"


class ClientDocument:
    def __init__(self, document_id: str, document_request_id: str, client: int, rm: int, description: str,
                 storage_location: str):
        self.document_id = document_id
        self.document_request_id = document_request_id
        self.client_id = client
        self.relationship_manager_id = rm
        self.description = description
        self.storage_location = storage_location


class DocumentRequestEmail:
    def __init__(self, to_email: str, from_email: str, subject: str, body: str):
        self.to_email = to_email
        self.from_email = from_email
        self.body = body
        self.subject = subject


class ClientDocumentEvent:
    def __init__(self, event_id: int, event_type: str, payload: json):
        self.event_type = event_type
        self.event_id = event_id
        self.payload = payload
