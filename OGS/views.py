from django.shortcuts import render, render_to_response, redirect
from OGS.models import Organization, GoodsServices
from django.core.paginator import Paginator
import random
import ast


def index(request):
    args = {}
    return render_to_response('OGS/index.html', args)


def index2(request):
    args = {}
    return render_to_response('OGS/index2.html', args)


def search(request):
    args = {}
    if request.GET:
        phrase = request.GET["q"]
        args["phrase"] = phrase
        services = GoodsServices.objects.filter(name__contains=phrase)
        n = len(services)
        order = random.sample(range(n), n)
        reorder = [services[i] for i in order]
        reorder = [reorder[i:i + 5] for i in range(0, len(reorder), 5)]
        results = []
        group = {}
        for i, block in enumerate(reorder):
            group["block"] = block
            group["page"] = i+1
            results.append(group)
            group = {}
        args["results"] = results
    return render_to_response('OGS/search.html', args)


def search2(request):
    page_number = 1
    args = {}
    if request.GET:
        queries_without_page = request.GET.copy()
        if 'page' in queries_without_page:
            page_number = int(request.GET["page"])
            del queries_without_page['page']
        phrase = request.GET["q"]
        args["phrase"] = phrase
        services = GoodsServices.objects.filter(name__contains=phrase)
        if 'order' in queries_without_page:
            order = ast.literal_eval(request.GET["order"])
        else:
            n = len(services)
            order = random.sample(range(n), n)
            args["init"] = 1
        args["order"] = order
        results = [services[i] for i in order]
        page = Paginator(results, 5)
        args["page"] = page_number
        args["results"] = page.page(page_number)
        args["queries"] = queries_without_page

    return render_to_response('OGS/search2.html', args)