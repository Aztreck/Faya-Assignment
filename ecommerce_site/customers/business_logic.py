from datetime import datetime, timedelta
from .models import Product


def deactivate_old_products():
    two_months_ago = datetime.now() - timedelta(days=60)
    Product.objects.filter(registered_at__lte=two_months_ago).update(is_active=False)
