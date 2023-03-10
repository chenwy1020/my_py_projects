class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s，占地面积为 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.house_item = []
        self.free_area = area

    def __str__(self):
        return "户型是 %s, 总面积是 %.2f，剩余面积为 %.2f, 家具有 %s" \
               % (self.house_type, self.area, self.free_area, self.house_item)

    def add_item(self, item):
        print("要添加 %s " % item)
        if item.area > self.free_area:
            print("该家具面积太大，放不下")
            return
        self.house_item.append(item.name)

        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
clothing_hold = HouseItem("衣柜", 2)
table = HouseItem("饭桌", 1.5)

MyHouse = House("三室两厅", 100)
MyHouse.add_item(bed)
MyHouse.add_item(clothing_hold)
MyHouse.add_item(table)

print(MyHouse)