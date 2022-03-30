# from rest_framework import serializers
#
# from .models import ClientDocumentRequestDataModel, ClientDocumentDataModel, ClientDocumentEventDataModel
#
#
# class IssueClientDocumentRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClientDocumentRequestDataModel
#         fields = '__all__'
#
#
# class HandleClientDocumentUploadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClientDocumentDataModel
#         fields = ('client_document_request_id', 'client_document_request_id')
#
#
# class CreateClientDocumentEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClientDocumentEventDataModel
#
#
# def clientDocumentIssuedToClientDocumentEvent(issued):
#     payload = {}
#     payload["client_document_request_id"] = issued.client_document_request_id
#     return ClientDocumentEventDataModel(payload=payload,
#                                         event_type='client_document_issued',
#                                         create_by=issued['create_by'])
#
#
# class GetClientDocument(serializers.ModelSerializer):
#     class Meta:
#         model = ClientDocumentDataModel
#         fields = ('client_document_request_id', 'client_document_request_id')
