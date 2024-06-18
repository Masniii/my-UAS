from rest_framework import serializers 
from django.contrib.auth.models import User

from berita.models import Kategori, Artikel
from pengguna.models import Biodata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']

class BiodataSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Biodata
        fields = ['user','alamat','telpon','foto']

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'judul']


class ArtikelSerializer(serializers.ModelSerializer):
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    kategori_detail = KategoriSerializer(source='kategori', read_only=True)
    author_detail = UserSerializer(source='author', read_only=True)
    class Meta:
        model = Artikel
        fields = [
            'id','judul','isi','kategori', 'kategori_detail', 'author', 'author_detail', 
            'thumbnail','created_at','slug'
            ]
        read_only_fields = ('kategori_detail', 'author_detail')