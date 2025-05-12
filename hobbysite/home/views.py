from django.shortcuts import render

def index(request):
    services = [
        {
            "name": "Wiki",
            "url": "wiki:articles_list",
            "motto": "Your hub of knowledge, built by the community.",
            "owner": "Nicole Christine Verial",
            "icon": "home/icons/wiki.png",
        },
        {
            "name": "Commissions",
            "url": "commissions:commission",
            "motto": "Connecting talent in a single click.",
            "owner": "Marcus Jet Esteban",
            "icon": "home/icons/commission.png",
        },
        {
            "name": "Forum",
            "url": "forum:thread_list",
            "motto": "Where ideas meet conversations.",
            "owner": "Justin Bon Dela Cruz",
            "icon": "home/icons/forum.png",
        },
        {
            "name": "Blog",
            "url": "blog:index",
            "motto": "Stories, ideas and thoughts, all shared in One Spot.",
            "owner": "Charles Matthew Ong",
            "icon": "home/icons/blog.png",
        },
        {
            "name": "Merchandise Store",
            "url": "merchstore:index",
            "motto": "A Trusted Place to Buy & Sell.",
            "owner": "Martin Angelo Funelas",
            "icon": "home/icons/store.png",
        },
    ]
    return render(request, "home/index.html", {
        'services': services,
    })