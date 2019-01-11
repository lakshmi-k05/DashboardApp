from django.db import models

class DashData(models.Model):
    statschoice = ((0,'processing'), (1,'success'), (2,'queued'), (3, 'failed'))
    set_id = models.DecimalField(max_digits=4, decimal_places=0)
    name = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=statschoice, default="processing")
    batch_id = models.DecimalField(max_digits=4, decimal_places=0)

class DocumentsData(models.Model):
    statchoice = ((0, 'processing'), (1, 'success'), (2, 'queued'), (3, 'failed'))
    batch_id = models.DecimalField(max_digits=4, decimal_places=0)
    set_id = models.DecimalField(max_digits=4, decimal_places=0)
    doc_id = models.DecimalField(max_digits=4, decimal_places=0)
    name=models.TextField()
    doc_status = models.CharField(max_length=20, choices=statchoice, default="processing")
    uploader = models.CharField(max_length=10)
    date_uploaded = models.DateTimeField()