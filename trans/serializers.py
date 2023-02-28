from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from trans.models import CheckTranslation, Translation

class TranslationDataSerializer(ModelSerializer):
    translation_data = SerializerMethodField("get_translation_data")
    class Meta:
        model = CheckTranslation
        fields=(
            "translation_data",
            "translation",
            "note",
            "is_checked",
        )
    def get_translation_data(self, obj):
        translation_data = {
            "pk": obj.translation.pk,
            "num": obj.translation.num,
            "remark": obj.translation.remark,
            "origin_data": obj.translation.origin_data,
            "trans_data": obj.translation.trans_data,
            "details": obj.translation.details,
            "is_done": obj.translation.is_done
        }
        return translation_data
    
class PutTranslationSerializer(ModelSerializer):
    class Meta:
        model = Translation
        fields=(
            "trans_data",
            "details",
            "is_done",
        )
        read_only_fields = ["pk"]

class PutCheckTranslationSerializer(ModelSerializer):
    class Meta:
        model = CheckTranslation
        fields=(
            "translation",
            "note",
            "is_checked",
        )
        read_only_fields = ["translation"]