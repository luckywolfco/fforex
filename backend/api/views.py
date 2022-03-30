import json
import mimetypes
import os

from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import request as issue_use_case, get_client_documents as get_client_documents_use_case, \
    get_client_document as get_client_document_use_case, \
    get_client_document_requests as get_client_document_requests_use_case, \
    capture_document as capture_document_use_case

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


@api_view(['GET', ])
def render_upload_html(api_request):
    did = api_request.GET.get('did', '')
    return render(api_request, 'upload.html', {"did": did})


@api_view(['GET', ])
def render_download_html(api_request):
    did = api_request.GET.get('did', '')
    return render(api_request, 'download.html', {"did": did})


@api_view(['GET', ])
def get_document_requests(api_request):
    data = json.loads(api_request.body)
    documents = get_client_document_requests_use_case(data["relationship_manager_id"])

    if len(documents):
        docs = []
        for document in documents:
            doc = {"client_document_request_id": document.document_request_id,
                   "relationship_manager_id": document.relationship_manager_id,
                   "status": document.status}
            docs.append(doc)
        api_response = docs
        return Response({"status": "ok", "data": api_response}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "ok", "data": {}}, status=status.HTTP_200_OK)


@api_view(['GET', ])
def get_documents(api_request):
    data = json.loads(api_request.body)
    documents = get_client_documents_use_case(data["relationship_manager_id"],
                                              data["client_id"])

    if len(documents):
        docs = []
        for document in documents:
            doc = {"client_document_id": document.document_id,
                   "relationship_manager_id": document.relationship_manager_id,
                   "description": document.description}
            docs.append(doc)
        api_response = docs
        return Response({"status": "ok", "data": api_response}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "ok", "data": {}}, status=status.HTTP_200_OK)


@api_view(['GET', ])
def get_document(api_request):
    data = json.loads(api_request.body)

    document = get_client_document_use_case(
        data["client_document_id"])

    if document is not None:
        api_response = {
            'document_id': document.document_id,
            'link': document.storage_location
        }
        return Response({"status": "ok", "data": api_response}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "ok", "data": {}}, status=status.HTTP_200_OK)


@api_view(['GET', ])
def download(api_request):
    did = api_request.GET.get('did', '')
    print(did)
    document = get_client_document_use_case(did)

    if document is not None:

        # Define the full file path
        filepath = BASE_DIR + document.storage_location
        # Open the file for reading content
        path = open(filepath, 'r')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filepath
        # Return the response value
        return response

    else:
        return Response({"status": "error", "data": {"Unknown document id"}}, status=status.HTTP_200_OK)


@api_view(['POST', ])
def request(api_request):
    data = json.loads(api_request.body)

    issued = issue_use_case(
        data["relationship_manager_id"],
        data["client_id"],
        data["description"],
        data["accepted_document_formats"],
        data["update_by"]

    )
    api_response = issued.__dict__
    return Response({"status": "ok", "data": api_response}, status=status.HTTP_200_OK)


# Using dynamic path
@api_view(['POST', ])
def upload(api_request, did):
    uploaded = api_request.FILES['upload']
    fss = FileSystemStorage()
    file = fss.save(uploaded.name, uploaded)
    file_url = fss.url(file)
    captured = capture_document_use_case(did, file_url)
    api_response = captured.__dict__

    return Response({"status": "ok", "data": api_response}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def hello(self):
    return Response({"message": "Hello, world!"})
