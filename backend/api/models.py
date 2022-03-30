from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
from .domain import ClientDocumentRequest, ClientDocument, ClientDocumentEvent


class RelationshipManagerDataModel(models.Model):
    relationship_manager_id = models.AutoField(primary_key=True)


class RelationshipManagerEmailIdentityDataModel(models.Model):
    relationship_manager_id = models.IntegerField()
    email = models.CharField(max_length=50)
    update_ts = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(default=0)


class ClientDataModel(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_names = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    update_ts = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(default=0)


class ClientEmailIdentityDataModel(models.Model):
    client_id = models.IntegerField()
    email = models.CharField(max_length=50)
    is_primary = models.BooleanField(default=True),
    update_ts = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(default=0)


class ClientRelationshipManagerDataModel(models.Model):
    relationship_manager_id = models.IntegerField(primary_key=True, auto_created=True)
    client_id = models.IntegerField()
    update_ts = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(default=0)


class ClientDocumentRequestDataModel(models.Model):
    client_document_request_id = models.AutoField(primary_key=True)
    encoded_client_document_request_id = models.CharField(max_length=32, default=get_random_string(length=32))
    relationship_manager_id = models.IntegerField()
    client_id = models.IntegerField()
    description = models.CharField(max_length=300, default="Client document request")
    accepted_document_formats = models.CharField(max_length=20, default="all")
    request_status = models.CharField(max_length=20, default="pending")
    update_ts = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(default=0)

    def to_domain(self):
        return ClientDocumentRequest(
            rm=self.relationship_manager_id,
            client=self.client_id,
            request_id=self.encoded_client_document_request_id,
            status=self.request_status
        )


class ClientDocumentDataModel(models.Model):
    client_document_id = models.AutoField(primary_key=True)
    client_document_request_id = models.IntegerField()
    client_id = models.IntegerField()
    relationship_manager_id = models.IntegerField()
    description = models.CharField(max_length=300, default="Client document")
    storage_location = models.CharField(max_length=200)
    update_ts = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(default=0)

    def to_domain(self):
        return ClientDocument(
            document_id=self.client_document_id,
            document_request_id=self.client_document_request_id,
            client=self.client_id,
            rm=self.relationship_manager_id,
            description=self.description,
            storage_location=self.storage_location
        )


class ClientDocumentEventDataModel(models.Model):
    event_id = models.AutoField(primary_key=True)
    payload = models.JSONField()
    event_type = models.CharField(max_length=50)
    create_ts = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=0)

    def to_domain(self):
        return ClientDocumentEvent(
            event_id=self.event_id,
            event_type=self.event_type,
            payload=self.payload
        )
