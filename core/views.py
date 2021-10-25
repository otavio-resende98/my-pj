from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)

def handler404(request):
    response = HttpResponseNotFound('{"status":"Failed"}', content_type="application/json")
    return response

def handler500(request):
    response = HttpResponseServerError('{"status":"Failed"}', content_type="application/json")
    return response
