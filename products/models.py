from django.db import models


# table CategoryModel
# Column category_name
# Column2 created_at

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductModel(models.Model):
    product_name = models.CharField(max_length=80)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)
    descriptions = models.TextField()
    image = models.FileField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    # pip install pillow
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# Создать модель для Корзины(Заказа)
# class CartModel
# user_id
# user_product -> ForeignKey(ProductModel)
# user_product_quantity
# user_add_date -> DateTimeField

# 2.Вы должны показать этот модель на admin.py