from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    is_new = models.BooleanField(default=False, verbose_name="Nouveauté")
    is_promo = models.BooleanField(default=False, verbose_name="En promotion")
    promo_price = models.FloatField(null=True, blank=True, verbose_name="Prix promo")

    def __str__(self):
        return self.name

    def get_display_price(self):
        if self.is_promo and self.promo_price:
            return self.promo_price
        return self.price

    def get_image_url(self):
        if not self.image:
            return None
        image_str = str(self.image)
        if image_str.startswith('http'):
            return image_str
    # ID Cloudinary pur (sans extension, sans '/')
        if '.' not in image_str and '/' not in image_str:
            return f"https://res.cloudinary.com/dpcuiczqn/image/upload/{image_str}"
    # Chemin products/fichier.jpg
        return f"https://res.cloudinary.com/dpcuiczqn/image/upload/{image_str}"

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"