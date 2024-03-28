from django.core.management.base import BaseCommand

from app_sectors.models import Produto


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Populando produtos...")
        Produto.objects.create(nome="Camiseta", quantidade_disponivel=50)
        Produto.objects.create(nome="Tinta", quantidade_disponivel=30)
        Produto.objects.create(nome="Lixas", quantidade_disponivel=20)
        print("Produtos populados com sucesso!")
