from django.db import models

class ScrollModel(models.Model):
    image = models.ImageField(upload_to="scrolls/")
    discount = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "scroll"
        verbose_name_plural = "scrolls"


class GalleryModel(models.Model):
    image = models.ImageField(upload_to="gallery/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "gallery"
        verbose_name_plural = "galleries"


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class MenuModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="menu_products", blank=True, null=True)
    image = models.ImageField(upload_to="menu/")
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu product"
        verbose_name_plural = "Menu products"


class ReservationModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"