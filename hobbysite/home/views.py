from django.shortcuts import render

def index(request):
    services = [
        {
            "name": "Wiki",
            "url": "wiki:articles_list"
        },
        {
            "name": "Commissions",
            "url": "commissions:commission"
        },
        {
            "name": "Forum",
            "url": "forum:thread_list"
        },
        {
            "name": "Blog",
            "url": "blog:index"
        },
        {
            "name": "Merchandise Store",
            "url": "merchstore:index"
        },
    ]
    return render(request, "home/index.html", {
        'services': services,
    })