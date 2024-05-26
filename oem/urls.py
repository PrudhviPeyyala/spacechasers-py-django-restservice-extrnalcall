from django.urls import path
from oem.views import OemViewListAll, OemRetriveUpdateDestroy, OemGetByIdOrAll, UserData, BooksInfo , CreateBook

urlpatterns = [
    path("getoems/", OemViewListAll.as_view(), name="get all OEMs"),
    path("putdeleteoems/<int:pk>", OemRetriveUpdateDestroy.as_view(), name="update-delete oems"),
    path("getoembymanufacturer/<manufacturer>", OemGetByIdOrAll.as_view(), name="get by id or all"),
    path("getusersdata/", UserData.as_view(), name="user mock data from external call"),
    path("getallbooksinfo/", BooksInfo.as_view(), name="get all books from another python service"),
    path("createbookinfo/", CreateBook.as_view(), name="create book info")
]
