from project import db


class Product(db.Document):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''
    product_id = db.StringField(unique=True)
    title = db.StringField()
    description = db.StringField()
    link = db.URLField()
    image_link = db.URLField()
    color = db.StringField()
    size = db.StringField()
    pattern = db.StringField()
    material = db.StringField()
    gender = db.StringField()

    # #Shopify fields
    product_type = db.StringField()
    brand = db.StringField()
    gtin = db.StringField()
    mpn = db.StringField()
    price = db.StringField()
    compare_at_price = db.StringField()
    sale_price = db.StringField()
    tags = db.StringField()

    # #Facebook fields
    labels = db.StringField()
    availability = db.StringField()
    condition = db.StringField()
    item_group_id = db.StringField()
    shipping_weight = db.StringField()

    # #Google fields
    google_product_category = db.StringField()
    custom_label_0 = db.StringField()
    custom_label_1 = db.StringField()
    custom_label_2 = db.StringField()
    custom_label_3 = db.StringField()
    custom_label_4 = db.StringField()
    age_group = db.StringField()

    # locale data(title, description and maybe something else)
    locale = db.StringField()

    meta = {
        'collection': 'Product',
        'strict': False
    }
