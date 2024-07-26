from django.shortcuts import render


def index(request, slug: str | None = None):
    return render(request, "drawer/index.html", context={"slug": slug})
