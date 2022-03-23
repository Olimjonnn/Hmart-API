from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from main.models import *
from main.serializer import *


class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']
    def list(self, request):
        logo = Logo.objects.last()
        log = LogoSerializer(logo)
        return Response(log.data)


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']
    def list(self, request):
        slider = Slider.objects.all().order_by("-id")[0:3]
        log = SliderSerializer(slider)
        return Response(log.data)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def list(self, request):
        category = Category.objects.all().order_by("-id")[0:3]
        cat = CategorySerializer(category, many=True)
        return Response(cat.data)

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                name = request.data['name']
                Category.objects.create(name=name)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)    

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    @action(["GET"], detail=False)
    def find(self, request):
        try:
            category = request.GET.get("category")
            product = Product.objects.filter(category_id=category)
            pr = ProductSerializer(product, many=True)
            return Response(pr.data)
        except Exception as arr:
            data = {
                'error': f"{arr}"
            } 
            return Response(data)

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                name = request.data['name']
                price = int(request.data['price'])
                sale = int(request.data['sale'])
                category= request.data['category']
                img1 = request.FILES['img1'] 
                img2 = request.FILES['img2'] 
                img3 = request.FILES['img3'] 
                img4 = request.FILES['img4'] 
                description = request.data['description']
                is_new = request.data['is_new']
                Product.objects.create(name=name, price=price, sale=sale, category_id=category, img1=img1, img2=img2, img3=img3, img4=img4, description=description, is_new=is_new)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user=request.user
            if user.type == 2:
                image = request.FILES['image']
                name = request.data['name']
                text = request.data['text']
                Feedback.objects.create(image=image, name=name, text=text)
                return Response({"Added"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class AdvertisementView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


    def list(self, request):
        try:
            adver = Advertisement.objects.all().order_by("-id")[0:3]
            log = AdvertisementSerializer(adver, many=True)
            return Response(log.data)
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

    def create(slef, request):
        try:
            user = request.user
            if user.type == 1:
                img = request.FILES.get("img")
                category = request.data['category']
                price = request.data['price']
                Advertisement.objects.create(img=img, category=category, price=price)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)


class BrandsView(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

class LatestBlogView(viewsets.ModelViewSet):
    queryset = LatestBlog.objects.all()
    serializer_class = LatestBlogSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def list(self, request):
        latest = LatestBlog.objects.all().order_by("-id")[0:2]
        lat = LatestBlogSerializer(latest, many=True)
        return Response(lat.data)

    def create(self, request):
        try: 
            user = request.user
            if user.type == 1:
                image = request.FILES['image']
                name = request.data['name']
                title = request.data['title']
                text = request.data['text']
                date = request.data['date']
                LatestBlog.objects.create(image=image, name=name,title=title, text=text, date=date)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class LinksView(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


    def create(self, request):
        try: 
            user = request.user
            if user.type == 1:
                 text = request.data['text'],
                 facebook = request.data['facebook'],
                 telegram = request.data['telegram'],
                 twitter = request.data['twitter'],
                 instagram = request.data['instagram'],
                 LatestBlog.objects.create(text=text, facebook=facebook, telegram=telegram, twitter=twitter, instagram=instagram)
                 return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)
             


class ContactInfoView(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                address = request.data['address']
                phone = int(request.data['phone'])
                email = request.data['email']
                ContactInfo.objects.create(address=address, phone=phone, email=email)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)
    def list(self, request):
        contact = ContactInfo.objects.last()
        con = ContactInfoSerializer(con)
        return Response(con.data)


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]




