from rest_framework import serializers
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, SectionCard, MediaAsset,
    CustomPage, CustomPageBlock, CustomPageCard,
)


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class NavItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavItem
        fields = "__all__"


class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = "__all__"


class SectionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCard
        fields = "__all__"


class PageSectionSerializer(serializers.ModelSerializer):
    cards = SectionCardSerializer(many=True, read_only=True)

    class Meta:
        model = PageSection
        fields = "__all__"


class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = "__all__"


class CustomPageCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPageCard
        fields = [
            'id', 'title_uz', 'title_kr', 'title_ru',
            'text_uz', 'text_kr', 'text_ru',
            'icon', 'image', 'link', 'order',
        ]


class CustomPageBlockSerializer(serializers.ModelSerializer):
    cards = CustomPageCardSerializer(many=True, read_only=True)

    class Meta:
        model = CustomPageBlock
        fields = [
            'id', 'block_type',
            'title_uz', 'title_kr', 'title_ru',
            'content_uz', 'content_kr', 'content_ru',
            'image', 'image_position',
            'link_text_uz', 'link_text_kr', 'link_text_ru',
            'link_url', 'order', 'is_active',
            'cards',
        ]


class CustomPageSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    def get_blocks(self, obj):
        qs = obj.blocks.filter(is_active=True)
        return CustomPageBlockSerializer(qs, many=True, context=self.context).data

    class Meta:
        model = CustomPage
        fields = [
            'id', 'slug',
            'title_uz', 'title_kr', 'title_ru',
            'meta_description_uz',
            'show_in_nav', 'nav_order',
            'is_active', 'updated_at',
            'blocks',
        ]


class CustomPageListSerializer(serializers.ModelSerializer):
    """Lighter serializer for nav/listing (no blocks)."""
    class Meta:
        model = CustomPage
        fields = [
            'id', 'slug',
            'title_uz', 'title_kr', 'title_ru',
            'show_in_nav', 'nav_order',
        ]
