from django.shortcuts import redirect, render
from django.views import View
import requests as req
import xml.etree.ElementTree as ET
from . models import Product
# Create your views here.




class MyView(View):
    def get(self, request):
        product = Product.objects.all()
        context={'product':product}
        # print(product[0].id)
        return render(request,'esewa_pay/home.html',context)

# def detail(request,id):
#     context={}
#     return render(request,'esewa_pay/home.html',context)


class EsewaPay(View):
    def get(self,request,id, *args, **kwargs):
        context={'id':id}
        return render(request,'esewa_pay/esewa-pay.html',context)        


class EsewaVerify(View):

    def get(self,request, *args, **kwargs):
    
        oid = request.GET.get('oid')
        amt = request.GET.get('amt')
        refId = request.GET.get('refId')
        # print(oid,amt,refId)

        url ="https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'EPAYTEST',
            'rid': refId,
            'pid':oid,
            }
        resp = req.post(url, d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()

        product = Product.objects.get(id=oid)

        if status =='Success':
            product.Payment_completed=True
            product.save()    
            return redirect('/')
        else:
            return redirect('/esewapay/?o_id='+oid)    