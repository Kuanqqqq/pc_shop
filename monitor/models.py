from django.db import models


# Create your models here.
class Brand(models.Model):
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.brand


class Size(models.Model):
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.size


class Resolution(models.Model):
    k_def = models.CharField(max_length=200)
    resolution_w = models.IntegerField()
    resolution_h = models.IntegerField()

    def __str__(self):
        return self.k_def


class Product(models.Model):
    name = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, null=True, on_delete=models.CASCADE)
    resolution = models.ForeignKey(Resolution, null=True, on_delete=models.CASCADE)

    # product_code = models.CharField(max_length=200) # how to generate code automaticlly?
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', blank=True)

    def resolution_str(self):
        return 'x'.join([self.resolution.resolution_w.__str__(), self.resolution.resolution_h.__str__()])

    def resolution_k(self):
        return self.resolution.k_def

    def product_code(self):
        # product_code = []
        return self.name.__str__() + ' ' + self.size.__str__() + '_' + self.resolution.__str__()

    def __str__(self):
        return self.product_code()
