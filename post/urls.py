from django.urls import path
from . import views

app_name="article"

urlpatterns=[
    path("detail/<slug:slug>",views.post,name="article_detail"),
    path("list",views.ArticleList.as_view(),name="article_list"),
    path("category/<int:pk>",views.category_detail,name="category_detail"),
    path("search/",views.search,name="search_article"),
    path("contactus/",views.contactus,name="contact_us"),
    path("add_article",views.AddArticle,name="add_article"),
    path("profile",views.profile,name="profile"),


    ]