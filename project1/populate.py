from app1.models import *

category1 = Category.objects.create(name="Smartphones")
category2 = Category.objects.create(name="Laptops")
category3 = Category.objects.create(name="Gaming")

subcategory1 = SubCategory.objects.create(name="iPhone", parent_category=category1)
subcategory2 = SubCategory.objects.create(name="Android", parent_category=category1)
subcategory3 = SubCategory.objects.create(name="Mac", parent_category=category2)
subcategory4 = SubCategory.objects.create(name="Windows", parent_category=category2)
subcategory5 = SubCategory.objects.create(name="PlayStation", parent_category=category3)
subcategory6 = SubCategory.objects.create(name="Xbox", parent_category=category3)

product1 = Product.objects.create(
    name="iPhone 15 Pro Max",
    description="The fastest iPhone there is, featuring cutting-edge technology!",
    price=1299,
    image="product1.jpg",
    category=category1,
    sub_category=subcategory1
)

product2 = Product.objects.create(
    name="Samsung Galaxy S23 Ultra",
    description="Revolutionary Android performance in a sleek design!",
    price=1199,
    image="product2.jpg",
    category=category1,
    sub_category=subcategory2
)

product3 = Product.objects.create(
    name="MacBook Pro M2",
    description="Unmatched processing power in a stylish MacBook form!",
    price=1799,
    image="product3.jpg",
    category=category2,
    sub_category=subcategory3
)

product4 = Product.objects.create(
    name="Razer Blade 18",
    description="A gaming powerhouse, perfect for the most demanding games!",
    price=2499,
    image="product4.jpg",
    category=category2,
    sub_category=subcategory4
)

product5 = Product.objects.create(
    name="PlayStation 5 Pro",
    description="Experience the pinnacle of console gaming with cutting-edge graphics!",
    price=499,
    image="product5.jpg",
    category=category3,
    sub_category=subcategory5
)

product6 = Product.objects.create(
    name="Xbox Series X",
    description="Top-tier gaming performance in a sleek, modern console!",
    price=499,
    image="product6.jpg",
    category=category3,
    sub_category=subcategory6
)
