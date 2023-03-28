from post.models import article,Category

def recent_articles(request):
    recent_articles=article.objects.order_by("-created")
    return {"recent_articles":recent_articles}
def categories(request):
    categories=Category.objects.all()
    return {"categories":categories}