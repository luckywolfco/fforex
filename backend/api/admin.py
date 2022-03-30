from django.contrib import admin

# Register your models here.
from .models import ClientDataModel, ClientDocumentDataModel, ClientDocumentRequestDataModel, \
    RelationshipManagerEmailIdentityDataModel, RelationshipManagerDataModel, \
    ClientRelationshipManagerDataModel, ClientDocumentEventDataModel

admin.site.register(ClientDataModel)
admin.site.register(ClientDocumentDataModel)
admin.site.register(ClientDocumentRequestDataModel)
admin.site.register(RelationshipManagerEmailIdentityDataModel)
admin.site.register(RelationshipManagerDataModel)
admin.site.register(ClientRelationshipManagerDataModel)
admin.site.register(ClientDocumentEventDataModel)
