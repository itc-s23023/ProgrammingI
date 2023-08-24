class Katsuo(Nigiri):
    top = "カツオ"
    topping = "生姜とねぎ"
    price = "100"

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))


k1 = Katsuo()
print(k1.show_attributes())
