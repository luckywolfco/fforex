from .models import RelationshipManagerDataModel, RelationshipManagerEmailIdentityDataModel, ClientDataModel, \
    ClientEmailIdentityDataModel


def setup():
    rm = RelationshipManagerDataModel.objects.create()
    RelationshipManagerEmailIdentityDataModel.objects.create(relationship_manager_id=rm.relationship_manager_id,
                                                             email="demo@junk.com")
    cm = ClientDataModel.objects.create(first_names='John', last_name='Smith')
    ClientEmailIdentityDataModel.objects.create(client_id=cm.client_id, email="demo@rubbish.com")

    cm2 = ClientDataModel.objects.create(first_names='Jess', last_name='Kane')
    ClientEmailIdentityDataModel.objects.create(client_id=cm2.client_id, email="demo2@rubbish.com")
