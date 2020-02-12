from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

#def anasayfa(request):
 #   return {'anasayfa': RenkFont.objects.first()}

