from typing import Any, Dict, List, Optional
import requests,json
from fakturowniaAPI import enums,errors
from fakturowniaAPI.enums import Kind,PaymentType
class Product:
    name: str
    total_price_gross: float
    quantity: int
    tax : float



class Client:

    url_headers = {
            "Accept":"application/json",
            "Content-Type":"application/json"
        }

    def __init__(self,api_token : str,domain : str):
        self.api_token = api_token
        self.domain = domain



    def addInvoice(self,
                   sell_date : str,
                   issue_date : str,
                   payment_to : str,
                   seller_name : str,
                   seller_tax_no: str,
                   buyer_name : str,
                   buyer_email : str,
                   kind:Kind ,
                   products : [Product],
                   buyer_tax_no : Optional[str] = "",
                   number : Optional[str] = None,
                   ):
        #####


        url_data = {
            "api_token":self.api_token,
            "invoice":{
                "kind":kind,
                "number":number,
                "sell_date":sell_date,
                "issue_date": issue_date,
                "payment_to": payment_to,
                "seller_name": seller_name,
                "seller_tax_no": seller_tax_no,
                "buyer_name": buyer_name,
                "buyer_email": buyer_email,
                "buyer_tax_no": buyer_tax_no,
                "positions": products
            }
        }
        url = f"https://{self.domain}.fakturownia.pl/invoices.json"
        try:
            p = requests.post(url,headers=self.url_headers,json=url_data)
        except requests.exceptions.ProxyError:
            raise errors.fakturowniaAPIError
        else:
            return p

    def addCustomer(self,
                    name : str,
                    tax_no: str,
                    post_code : str,
                    city : str,
                    street : str,
                    first_name : str,
                    last_name : str,
                    kind : str,
                    bank : str,
                    bank_account : str,
                    external_id : str,
                    default_payment_type: PaymentType,
                    person: Optional[str] = "",
                    discount: Optional[str] = "",
                    www: Optional[str] = "",
                    register_number : Optional[str] = "",
                    note : Optional[str] = "",
                    email: Optional[str] = "",
                    phone: Optional[str] = "",
                    mobile_phone: Optional[str] = "",
                    use_delivery_address: Optional[str] = "1",
                    delivery_address : Optional[str] = "",
                    payment_to_kind: str = "30",
                    default_tax: Optional[str] = "23",
                    company: Optional[str] = "1",
                    country: str = "PL",

                    tax_no_kind: str = "NIP",
                    accounting_id : Optional[str] = "",
                    shortcut : Optional[str] = "",

                    ):

        url_data = {"api_token":self.api_token,"client":{
            "name":name,
            "shortcut":shortcut,
            "tax_no_kind":tax_no_kind,
            "tax_no":tax_no,
            "register_number":register_number,
            "accounting_id":accounting_id,
            "post_code":post_code,
            "city":city,
            "street":street,
            "country":country,
            "use_delivery_address":use_delivery_address,
            "delivery_address":delivery_address,
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "phone":phone,
            "mobile_phone":mobile_phone,
            "www":www,
            "note":note,
            "company":company,
            "kind":kind,
            "bank":bank,
            "bank_account":bank_account,
            "discount":discount,
            "default_tax":default_tax,
            "payment_to_kind":payment_to_kind,
            "default_payment_type":default_payment_type,
            "person":person,
            "external_id":external_id

        }}

        url = f"https://{self.domain}.fakturownia.pl/clients.json"

        try:
            p = requests.post(url,headers=self.url_headers,json=url_data)
        except requests.exceptions.ProxyError:
            raise errors.fakturowniaAPIError

        return p


    def addBasicCustomer(self,
                         name : str,
                         tax_no : str,
                         bank : str,
                         bank_account : str,
                         city : str,
                         country : str,
                         email : str,
                         person : str,
                         post_code : str,
                         phone : str,
                         street : str
                         ):

        url_data = {
            "api_token":self.api_token,
            "client":{
                "name":name,
                "tax_no":tax_no,
                "bank":bank,
                "bank_account":bank_account,
                "city":city,
                "country":country,
                "email":email,
                "person":person,
                "post_code":post_code,
                "phone":phone,
                "street":street
            }
        }

        url = f"https://{self.domain}.fakturownia.pl/clients.json"

        p = requests.post(url,headers=self.url_headers,json=url_data)

        return p


    def getAllCustomers(self):
        url = f"https://{self.domain}.fakturownia.pl/clients.json?page=1&per_page=50&api_token={self.api_token}"
        p = requests.get(url,headers=self.url_headers)
        if p.status_code == 200:
            jsoned_text = json.loads(p.text)
        else:
            raise errors.fakturowniaAPIError("Blad podczas")
        return jsoned_text

    def getCustomer(self,tax_no : Optional[str] = "", id : Optional[int] = '',name : Optional[str] = ""):
        if tax_no != "":
            filter_value = tax_no
            filter_field = "tax_no"
        elif id != "":
            filter_value = id
            filter_field = "id"
        elif name != "":
            filter_value = name
            filter_field = "name"
        else:
            filter_value = None
            filter_field = None
        for client in self.getAllCustomers():
            if client[filter_field] == filter_value:
                return client

        return f"Nie znaleziono klienta o filtrze '{filter_field}:{filter_value}'"
