from django.shortcuts import render

from api.serializer import BookSerializer,ReviewSerializer

from api.models import Book,Review

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework import authentication,permissions

from rest_framework import generics

# Create your views here.

class BookListCreateView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        qs=Book.objects.all()
        
        serializer_instance=BookSerializer(qs,many=True)
        
        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):
        
        serializer_instance=BookSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
    
class BookRetrieveUpdateDestroyView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Book.objects.get(id=id)
        
        serializer_instance=BookSerializer(qs)
        
        return Response(data=serializer_instance.data)
        
        
    def put(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        book_obj=Book.objects.get(id=id)
        
        serializer_instance=BookSerializer(data=request.data,instance=book_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
        
            return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Book.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data)
    
class BookViewSetView(viewsets.ViewSet):
    
    authentication_classes=[authentication.BasicAuthentication]
    
    permission_classes=[permissions.IsAuthenticated]
    
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def list(self,request,*args,**kwargs):
        
        qs=Book.objects.all()
        
        serializer_instance=BookSerializer(qs,many=True)
        
        return Response(data=serializer_instance.data)
    
    def create(self,request,*args,**kwargs):
        
        serializer_instance=BookSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
        
    def retrieve(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Book.objects.get(id=id)
        
        serializer_instance=BookSerializer(qs)
        
        return Response(data=serializer_instance.data)
    
    def update(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        book_obj=Book.objects.get(id=id)
        
        serializer_instance=BookSerializer(data=request.data,instance=book_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
        
    def destroy(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Book.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data=data)
    
    @action(methods=["GET"],detail=False)

    def genre_list(self,request,*args,**kwargs):
    
        genres=Book.objects.all().values_list("genre",flat=True).distinct()
    
        return Response(data=genres)
    
    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        
        book_id=kwargs.get("pk")
        
        book_obj=Book.objects.get(id=book_id)
        
        serializer_instance=ReviewSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save(book_obj=book_obj)
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
    
class ReviewUpdateDestroyViewSet(viewsets.ViewSet):
    
    def destroy(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Review.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data=data)
        
        
    def update(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        review_obj=Review.objects.get(id=id)
        
        serializer_instance=ReviewSerializer(data=request.data,instance=review_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
    def retrieve(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Review.objects.get(id=id)
        
        serializer_instance=ReviewSerializer(qs)
        
        return Response(data=serializer_instance.data)
    
    
class BooksListCreateView(generics.ListCreateAPIView):
    
    serializer_class=BookSerializer
    
    queryset=Book.objects.all()
    
class BooksGenericView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=BookSerializer
    
    queryset=Book.objects.all()
    
    
class ReviewGenericView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=ReviewSerializer
    
    queryset=Review.objects.all()
    
class ReviewCreateView(generics.CreateAPIView):
    
    serializer_class=ReviewSerializer
    
    queryset=Review.objects.all()
    
    def perform_create(self, serializer):
        
        id=self.kwargs.get("pk")
        
        book_obj=Book.objects.get(id=id)
        
        serializer.save(book_objects=book_obj)