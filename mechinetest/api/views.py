from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from.models import*
from.serializers import *

# Create your views here.


@api_view(["POST"])
def create(request):

    create_data = JSONParser().parse(request)
    itemunits = create_data["itemunits"]
    itemname = create_data["ItemName"]
    item = Item.objects.filter(ItemName=itemname)
    serializer = CreateSerializers(data=create_data)

    if serializer.is_valid():
        if item:
            return JsonResponse({"message": "Item already exist"})
        else:
            serializer.save()
            print("item saved")
            get_item = Item.objects.get(ItemName=itemname)
            for i in itemunits:
                itemid = get_item.ItemId
                unitid = i.get("UnitId")
                noofunit = i.get("NoOfUnits")
                rate = i.get("Rate")
                units = ItemUnits(ItemId_id=itemid, UnitId=unitid,
                                  NoOfUnits=noofunit, Rate=rate)
                units.save()
                print("item units saved")
            return JsonResponse({"message": "Created successfull"})
    else:
        return JsonResponse(serializer.errors)


@api_view(["PUT"])
def update(request, id):

    item_data = Item.objects.get(ItemId=id)
    item_unit_data = ItemUnits.objects.filter(ItemId=id)
    data = request.data
    item_unit = data['itemunits']
    print(item_unit)
    serializer = UpdateSerializers(instance=item_data, data=request.data)

    if serializer.is_valid():
        serializer.save()
        if item_unit_data:
            for i in item_unit:
                unitid = i.get("UnitId")
                noofunit = i.get("NoOfUnits")
                rate = i.get("Rate")
                for j in item_unit_data:
                    ItemUnits.objects.filter(ItemUnitId=j.ItemUnitId).update(UnitId=unitid,
                                                                             NoOfUnits=noofunit, Rate=rate)
                    print("saved")
    return JsonResponse({"message": "success"})


@api_view(["GET"])
def read(request, id):

    data = {}
    item = {}
    list = []
    itemunit_list = []
    details = Item.objects.get(ItemId=id)
    data['ItemName'] = details.ItemName
    data['MRP'] = details.MRP
    iteamunit = ItemUnits.objects.filter(ItemId=id)

    for unit in iteamunit:
        item['UnitId'] = unit.UnitId
        item['NoOfUnits'] = unit.NoOfUnits
        item['Rate'] = unit.Rate
        itemunit_list.append(item)
    data["itemunits"] = itemunit_list
    list.append(data)
    return JsonResponse({
        "message": "Updated successfull",
        "data": list
    })


@api_view(["DELETE"])
def delete(request, id):
    
    item = Item.objects.get(ItemId=id)
    item.delete()
    return JsonResponse({"message": "Deleted successfull"})
