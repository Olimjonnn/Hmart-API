from rest_framework import routers
from main.views import *  

router = routers.DefaultRouter()

router.register("slider", SliderView)
router.register("category", CategoryView)
router.register("product", ProductView)
router.register("feedback", FeedbackView)
router.register("advertisement", AdvertisementView)
router.register("brands", BrandsView)
router.register("latestblog", LatestBlogView)
router.register("links", LinksView)
router.register("contactinfo", ContactInfoView)
router.register("cart", CartView)
router.register("wishlist", WishlistView)