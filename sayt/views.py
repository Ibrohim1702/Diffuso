from django.shortcuts import render

# Create your views here.

def index(requests):
    ctx = {

    }
    return render(requests, "index.html", ctx)


def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)


def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)


def portfolio(requests):
    ctx = {

    }
    return render(requests, "portfolio.html", ctx)


def service(requests):
    ctx = {

    }
    return render(requests, "service.html", ctx)
