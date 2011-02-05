# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from blog_core.models import Blog_records
import datetime

class blog_entry:
    title = 1
    body = 2

def current_datetime(request):
    try:
        post_list = Blog_records.objects.all()
    except Blog_records.DoesNotExist:
        print "Apress isn't in the database yet."
    else:
        print "Apress is in the database."

    for post in post_list:
        post.body = 'posts/'+str(post.number)+'.htm'
    
    return render_to_response('index.html', {'post_list': post_list })
