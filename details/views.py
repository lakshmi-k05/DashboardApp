from django.shortcuts import render
import json
from pprint import pprint
from .models import DocumentsData, DashData



def fill_data_view(request):

    with open('C:\\Users\\Lakshmi\\PycharmProjects\\dashboard\\dashboard\\details\\static\\dashboard.json') as f:
        data = json.load(f)

    batch_no = 1
    # for eachBatch in data:
    #     temp_set_id=eachBatch['set_id']
    #     temp_name=eachBatch['name']
    #     temp_stat = eachBatch['status']
    #     temp_doc = eachBatch['documents']
    #     for eachDoc in temp_doc:
    #         doc_temp_set_id = eachDoc['set_id']
    #         doc_temp_doc_id = eachDoc['doc_id']
    #         doc_temp_name = eachDoc['name']
    #         doc_temp_stat = eachDoc['status']
    #         doc_temp_uploader = eachDoc['uploader']
    #         doc_temp_date = eachDoc['date_uploaded']
    #         print(doc_temp_set_id,doc_temp_doc_id, doc_temp_name,
    #                                      doc_temp_name,doc_temp_stat,doc_temp_uploader,
    #                                      doc_temp_date)
    #         DocumentsData.objects.create(set_id = doc_temp_set_id,doc_id=doc_temp_doc_id,name = doc_temp_name,doc_status = doc_temp_stat,uploader=doc_temp_uploader,date_uploaded=doc_temp_date, batch_id=batch_no)
    #
    #     DashData.objects.create(set_id=temp_set_id, name=temp_name, status=temp_stat, batch_id=batch_no)

    #    batch_no=batch_no+1
    return render(request, "details/details.html")

def display_batch_view(request):

    batches = DashData.objects.all()
    context = {
        'batch': batches
    }
    return render(request, "details/tableview.html", context)

def display_doc_view(request, bid):

    documents = DocumentsData.objects.filter(batch_id=bid)
    context = {
        'docs': documents,
        'bid':bid
    }
    return render(request, "details/docsview.html", context)