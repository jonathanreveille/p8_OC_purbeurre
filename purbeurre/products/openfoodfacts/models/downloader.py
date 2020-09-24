#! /usr/bin/env python3
# coding : utf-8
import requests
import pprint

class  ProductDownloader:
    """ this class has the responsibility to download
    all the products from the given list of categories.
    It will make sure to take in only data will all the
    information we need from openfoodfacts """

    def __init__(self, url, category):
        """initializer"""
        self.url = url
        
        self.params ={
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": category,
                "sort_by": "unique_scans_n",
                "page_size": 2,
                "json": 1
                }

        self.category = category

    def search_connexion(self):
        """ This method is to download all data needed
        from the URL,
        output = if <Response 200> params : OK
        and url == everything is well set"""

        connexion = True
        # self.response = statut.code()
        self.response = requests.get(self.url,
                                    params=self.params
                                    )
        # si pas de réseau = on arrive sur une exception.

        if not connexion:
            print("<<Not connected to API>>")
        else:
            print("<<Connected to API, loading...>>")


    def fetch_date_from_API(self):
        """this method transforms what we received from
        the API into .json format.
        We get in return a dictionnary 'key :  value'"""

        self.data_product = self.response.json()

        print(self.data_product)
        return self.data_product #this is a dict


    def is_valid_data(self, product):
        """This method to validate the data that is present
        and complete.
        --> we create a list of fields we want to search;
        --> check if the key (field) exists;
        --> check if a value exists for the key
        """

        fields = [
            'product_name_fr', 'nutrition_grade_fr', 'brands',
            'stores', 'url', 'categories', 'code',
            'image_nutrition_url', 'image_front_url'
            ]
            #'image_thumb_url','image_url'

        for field in fields:
            if field not in product or not product[field]:
                return False
        return True


    def get_products(self):
        """this method will add in a list
        all the produts that are valid with 
        all  fields of key:value"""

        self.product_list = []

        for product in self.data_product["products"]:

            if self.is_valid_data(product):
                #contains only object products with all fields
                self.product_list.append(product)
        print("PRODUCT:", self.product_list)
        #pprint.pprint(self.product_list)
        return self.product_list
        

CATEGORY_LIST = ["pizza"] #, "biscuit", "jus de fruit", "pâte à tartiner", "fromage"]

URL_OFOODFACTS = "https://fr.openfoodfacts.org/cgi/search.pl"

def main():
    for category in CATEGORY_LIST:
        a =  ProductDownloader(URL_OFOODFACTS, category)
        a.search_connexion()
        a.fetch_date_from_API()
        a.get_products()

if __name__ == "__main__":
    main()
