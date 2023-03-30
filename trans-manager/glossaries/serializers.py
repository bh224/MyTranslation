from rest_framework.serializers import ModelSerializer
from glossaries.models import Category, Glossary

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields=(
            "pk",
            "name",
        )
        read_only_fields = ['project', "author"]

    def __str__(self) -> str:
        return self.name
    
class GlossarySerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Glossary
        fields=(
            "pk",
            "project",
            "category",
            "origin_word",
            "trans_word",
            "furigana",
            "details",
            "author",
        )
        read_only_fields = ['project', "author"]


