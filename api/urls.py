from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register("v1/books",views.BookViewSetView,basename="books"),

router.register("v1/reviews",views.ReviewUpdateDestroyViewSet,basename="reviews")



urlpatterns = [
   
    path('books/',views.BookListCreateView.as_view()),
    path('books/',views.BookListCreateView.as_view()),
    path('books/<int:pk>/',views.BookRetrieveUpdateDestroyView.as_view()),
    path('v2/books/',views.BookListCreateView.as_view()),
    path('v2/books/<int:pk>/',views.BookRetrieveUpdateDestroyView.as_view()),
    path('v2/reviews/<int:pk>/',views.ReviewGenericView.as_view()),
    path('v2/books/<int:pk>/reviews/add/',views.ReviewCreateView.as_view())
]+router.urls
